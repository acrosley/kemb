"""Inspect — content-aware preview of files about to be sent to LlamaCloud.

``inspect`` is the natural follow-on to ``probe``: probe answers "what files
are here?" (metadata only), inspect answers "what are these files actually
like?" — page counts, scan-vs-text PDFs, form fields, encryption, optional
text snippets. Like probe, it makes zero network calls and spends zero
credits; everything happens locally.

Backbone fit: this is L1 in the seven-layer pipeline (L0 walk → **L1 inspect**
→ L2 classify → L3 extract → ...). Its job is to surface the few facts a
downstream parse plan actually needs to make routing decisions: which PDFs
need OCR (`is_scan`), which need an encryption password (`is_encrypted`),
which have AcroForm fields (`has_form_fields`), and roughly how much text
sits in each.

PDF inspection uses PyMuPDF (``import fitz``) as a soft dependency. If
PyMuPDF is not installed, PDF entries fall back to a single
``inspector_notes`` line explaining the missing dep — the rest of the report
still renders.

Exit codes mirror probe:
    0 — inspection completed
    2 — bad arguments (missing path, etc.)
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import _probe
from ._common import err

# Files we know how to peek into beyond metadata. Anything not in this set
# still appears in the report — just without L1 enrichment.
PDF_EXTENSIONS = frozenset({".pdf"})
TEXT_EXTENSIONS = frozenset({
    ".txt", ".md", ".rst", ".csv", ".tsv",
    ".html", ".htm", ".xml", ".json", ".yaml", ".yml",
    ".log", ".ini", ".toml", ".cfg",
})

# Heuristic threshold for "this PDF is a scan, not a text PDF". A typical
# text page has 1000–3000 characters of extractable text; a scanned page
# yields near-zero. 50 chars/page is a conservative cutoff that almost never
# flags a real text PDF as a scan, even ones with sparse text (cover pages,
# diagram-heavy decks). Tunable later if it misclassifies in the wild.
SCAN_TEXT_DENSITY_THRESHOLD = 50

# Number of leading pages we sample for the text-density estimate. Sampling
# the whole document would defeat the "fast preflight" purpose; the first
# few pages are nearly always representative of whether OCR is needed.
DENSITY_SAMPLE_PAGES = 3

# How many bytes to read off the front of a text file when computing
# `--snippet`. Capped so the inspector doesn't try to slurp a 2GB CSV into
# memory just to render a 200-char preview.
TEXT_SNIPPET_READ_CAP = 64 * 1024


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "inspect",
        help="Content-aware preview of files (page counts, scans, snippets).",
        description=(
            "Walk a directory and report each file's content shape — page "
            "count, scan-vs-text, form fields, encryption, optional text "
            "snippet. Spends zero credits; pair with `probe` for a layered "
            "preflight before sending anything to LlamaCloud."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  llamaparse inspect ./inbox\n"
            "  llamaparse inspect ./inbox/report.pdf\n"
            "  llamaparse inspect ./inbox --snippet 200\n"
            "  llamaparse inspect ./inbox --ext pdf --json > inspect.json\n"
            "  llamaparse inspect ./inbox --supported-only --max-files 50\n"
            "\n"
            "PDF inspection needs PyMuPDF: `pip install pymupdf`.\n"
        ),
    )
    p.add_argument(
        "target",
        type=Path,
        help="Directory to inspect. A single file is also accepted.",
    )
    p.add_argument(
        "--ext",
        default=None,
        help="Comma-separated extension allowlist (e.g. 'pdf,docx'). "
             "Leading dots optional, case-insensitive.",
    )
    p.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Maximum recursion depth (0 = target directory only).",
    )
    p.add_argument(
        "--max-files",
        type=int,
        default=_probe.DEFAULT_MAX_FILES,
        help=f"Stop after this many files (default: {_probe.DEFAULT_MAX_FILES}).",
    )
    p.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include dotfiles and hidden directories (skipped by default).",
    )
    p.add_argument(
        "--supported-only",
        action="store_true",
        help="Only emit files with extensions LlamaCloud is known to accept.",
    )
    p.add_argument(
        "--follow-symlinks",
        action="store_true",
        help="Follow symlinked directories during the walk.",
    )
    p.add_argument(
        "--snippet",
        type=int,
        default=0,
        metavar="N",
        help="Include up to N characters of extracted text per file "
             "(default: 0 = no snippet). PDFs sample the first "
             f"{DENSITY_SAMPLE_PAGES} pages; text files read the head of the file.",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Emit a single JSON document instead of the human-readable table.",
    )
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write the inspect report to this file (in addition to stdout).",
    )
    p.set_defaults(func=run)
    return p


# --------------------------------------------------------------------------- #
# Per-file inspection
# --------------------------------------------------------------------------- #


def inspect_file(path, *, snippet_chars=0):
    """Return the L1 fields for a single file.

    The shape is always the same regardless of extension — fields that don't
    apply (e.g. `page_count` for a `.txt`) are simply ``None``. This keeps
    the JSON output stable for downstream tooling.
    """
    ext = path.suffix.lower()
    result = _empty_inspection()

    if ext in PDF_EXTENSIONS:
        _merge_inspection(result, inspect_pdf(path, snippet_chars=snippet_chars))
    elif ext in TEXT_EXTENSIONS:
        _merge_inspection(result, inspect_text(path, snippet_chars=snippet_chars))
    else:
        # Office docs, images, etc. — recognized formats we just don't have a
        # local L1 inspector for. Flag so the report is honest about the gap.
        if ext in _probe.SUPPORTED_EXTENSIONS:
            result["inspector_notes"].append(
                f"no local inspector for {ext}; metadata only"
            )
        else:
            result["inspector_notes"].append(
                f"unsupported extension {ext or '(none)'}; metadata only"
            )

    return result


def _empty_inspection():
    """The canonical inspection-result shape, with every field set to its 'unknown' default."""
    return {
        "is_text": None,
        "is_scan": None,
        "page_count": None,
        "text_density": None,
        "has_form_fields": None,
        "is_encrypted": None,
        "snippet": None,
        "inspector_notes": [],
    }


def _merge_inspection(target, updates):
    """Copy non-None fields from ``updates`` into ``target``, concatenating notes."""
    notes = updates.pop("inspector_notes", []) if isinstance(updates, dict) else []
    for key, value in (updates or {}).items():
        if value is not None:
            target[key] = value
    target["inspector_notes"].extend(notes)


# --------------------------------------------------------------------------- #
# PDF inspection (PyMuPDF)
# --------------------------------------------------------------------------- #


def inspect_pdf(path, *, snippet_chars=0):
    """Inspect a PDF with PyMuPDF; degrade gracefully if it's missing or unreadable.

    Returns the same dict shape as ``_empty_inspection`` plus
    ``inspector_notes`` to explain anything we couldn't determine.
    """
    try:
        import fitz  # type: ignore  # PyMuPDF
    except ImportError:
        return {
            "inspector_notes": [
                "pymupdf not installed; PDF inspection skipped "
                "(install with `pip install pymupdf`)."
            ],
        }

    notes = []
    try:
        doc = fitz.open(str(path))
    except Exception as exc:  # PyMuPDF raises a variety of types; collapse to one note
        return {
            "inspector_notes": [f"could not open PDF: {type(exc).__name__}: {exc}"],
        }

    try:
        is_encrypted = bool(getattr(doc, "is_encrypted", False)) and getattr(
            doc, "needs_pass", False
        )
        if is_encrypted:
            # Without the password fitz returns metadata but page text is
            # blocked. Report what we can and bail before trying to read
            # text — otherwise text_density would be misleadingly zero and
            # we'd flag the file as a scan.
            notes.append("PDF is encrypted; text inspection skipped.")
            return {
                "page_count": doc.page_count,
                "is_encrypted": True,
                "is_text": False,
                "is_scan": None,
                "text_density": None,
                "has_form_fields": _safe_has_form_fields(doc, notes),
                "snippet": None,
                "inspector_notes": notes,
            }

        page_count = doc.page_count
        text_chars, sampled_pages, sampled_text = _sample_pdf_text(
            doc, DENSITY_SAMPLE_PAGES, notes
        )
        if sampled_pages > 0:
            text_density = text_chars // sampled_pages
        else:
            text_density = 0
        is_scan = text_density < SCAN_TEXT_DENSITY_THRESHOLD
        is_text = not is_scan

        snippet = None
        if snippet_chars > 0 and sampled_text:
            snippet = _condense_whitespace(sampled_text)[:snippet_chars]

        return {
            "page_count": page_count,
            "is_encrypted": False,
            "is_text": is_text,
            "is_scan": is_scan,
            "text_density": text_density,
            "has_form_fields": _safe_has_form_fields(doc, notes),
            "snippet": snippet,
            "inspector_notes": notes,
        }
    finally:
        try:
            doc.close()
        except Exception:
            pass


def _sample_pdf_text(doc, sample_pages, notes):
    """Pull text from up to ``sample_pages`` of ``doc``; return (chars, pages_sampled, joined_text)."""
    page_count = doc.page_count
    limit = min(sample_pages, page_count)
    chunks = []
    total_chars = 0
    pages_sampled = 0
    for i in range(limit):
        try:
            page = doc.load_page(i)
            text = page.get_text() or ""
        except Exception as exc:
            notes.append(f"page {i + 1} text extraction failed: {type(exc).__name__}")
            continue
        chunks.append(text)
        total_chars += len(text)
        pages_sampled += 1
    return total_chars, pages_sampled, "\n".join(chunks)


def _safe_has_form_fields(doc, notes):
    """Return True iff the PDF advertises AcroForm fields; never raises."""
    # `is_form_pdf` is the canonical PyMuPDF accessor and is non-zero when
    # any AcroForm widget exists. It's been present since PyMuPDF 1.18 but
    # we still guard for the off chance an unusual build doesn't expose it.
    try:
        flag = getattr(doc, "is_form_pdf", None)
        if flag is None:
            return None
        return bool(flag)
    except Exception as exc:
        notes.append(f"form-field check failed: {type(exc).__name__}")
        return None


def _condense_whitespace(text):
    """Collapse runs of whitespace so snippets don't burn characters on PDF newlines."""
    return " ".join(text.split())


# --------------------------------------------------------------------------- #
# Plain-text inspection
# --------------------------------------------------------------------------- #


def inspect_text(path, *, snippet_chars=0):
    """Inspect a plain-text or markup file: always text, no pages, optional snippet."""
    notes = []
    snippet = None

    if snippet_chars > 0:
        try:
            with open(path, "rb") as fh:
                # Read enough bytes that snippet_chars worth of text will
                # almost always fit even after multi-byte decoding, but cap
                # so a giant file doesn't pull megabytes into memory.
                raw = fh.read(min(TEXT_SNIPPET_READ_CAP, max(snippet_chars * 4, 1024)))
            decoded = raw.decode("utf-8", errors="replace")
            snippet = _condense_whitespace(decoded)[:snippet_chars]
        except OSError as exc:
            notes.append(f"could not read text snippet: {exc}")

    return {
        "is_text": True,
        "is_scan": False,
        "snippet": snippet,
        "inspector_notes": notes,
    }


# --------------------------------------------------------------------------- #
# Aggregation
# --------------------------------------------------------------------------- #


def summarize(entries):
    """Aggregate the per-file inspection results into corpus-level totals."""
    total = 0
    by_ext = {}
    pdf_count = 0
    pdf_scans = 0
    pdf_text = 0
    pdf_encrypted = 0
    pdf_with_forms = 0
    total_pages = 0
    truncated = False
    truncated_limit = None

    for entry in entries:
        if entry.get("_truncated"):
            truncated = True
            truncated_limit = entry.get("limit")
            continue
        total += 1
        ext = entry.get("extension") or "(no ext)"
        bucket = by_ext.setdefault(ext, {"count": 0, "bytes": 0})
        bucket["count"] += 1
        bucket["bytes"] += entry.get("size") or 0

        if ext == ".pdf":
            pdf_count += 1
            if entry.get("is_scan"):
                pdf_scans += 1
            elif entry.get("is_text"):
                pdf_text += 1
            if entry.get("is_encrypted"):
                pdf_encrypted += 1
            if entry.get("has_form_fields"):
                pdf_with_forms += 1
            if entry.get("page_count"):
                total_pages += entry["page_count"]

    return {
        "total_files": total,
        "by_extension": by_ext,
        "pdf_total": pdf_count,
        "pdf_scans": pdf_scans,
        "pdf_text": pdf_text,
        "pdf_encrypted": pdf_encrypted,
        "pdf_with_forms": pdf_with_forms,
        "pdf_total_pages": total_pages,
        "truncated": truncated,
        "truncated_limit": truncated_limit,
    }


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def render_table(entries, summary):
    """Render an ASCII table summarizing what each file looks like."""
    lines = []
    if not entries:
        lines.append("no files matched.")
    else:
        path_w = max(8, *(len(e["relative"]) for e in entries))
        kind_w = 10
        pages_w = 5
        density_w = 7

        header = (
            f"{'PATH':<{path_w}}  {'KIND':<{kind_w}}  "
            f"{'PAGES':>{pages_w}}  {'CH/PG':>{density_w}}  NOTES"
        )
        lines.append(header)
        lines.append("-" * len(header))
        for e in entries:
            kind = _kind_label(e)
            pages = "" if e.get("page_count") is None else str(e["page_count"])
            density = (
                "" if e.get("text_density") is None else str(e["text_density"])
            )
            notes = _short_notes(e)
            lines.append(
                f"{e['relative']:<{path_w}}  "
                f"{kind:<{kind_w}}  "
                f"{pages:>{pages_w}}  "
                f"{density:>{density_w}}  "
                f"{notes}"
            )

    lines.append("")
    lines.append(_summary_block(summary))
    return "\n".join(lines)


def _kind_label(entry):
    """One-word classification for the table's KIND column."""
    if entry.get("is_encrypted"):
        return "encrypted"
    if entry.get("is_scan"):
        return "scan-pdf"
    if entry.get("extension") == ".pdf" and entry.get("is_text"):
        return "text-pdf"
    if entry.get("is_text"):
        return "text"
    if entry.get("extension") in _probe.SUPPORTED_EXTENSIONS:
        return entry["extension"].lstrip(".") or "file"
    return "unknown"


def _short_notes(entry):
    """One-line condensation of inspector_notes plus key flags."""
    flags = []
    if entry.get("has_form_fields"):
        flags.append("form-fields")
    if entry.get("is_encrypted"):
        flags.append("encrypted")
    notes = entry.get("inspector_notes") or []
    if notes:
        # Truncate the longest note rather than count them so the user sees
        # the actual reason something is missing data.
        first = notes[0]
        if len(first) > 60:
            first = first[:57] + "..."
        flags.append(first)
    return "; ".join(flags)


def _summary_block(summary):
    parts = [
        "summary:",
        f"  total files     : {summary['total_files']}",
    ]
    if summary["pdf_total"]:
        parts.append(
            f"  PDFs            : {summary['pdf_total']} "
            f"(text: {summary['pdf_text']}, scans: {summary['pdf_scans']}, "
            f"encrypted: {summary['pdf_encrypted']}, "
            f"with-forms: {summary['pdf_with_forms']})"
        )
        if summary["pdf_total_pages"]:
            parts.append(f"  total PDF pages : {summary['pdf_total_pages']}")
    if summary["by_extension"]:
        parts.append("  by extension    :")
        for ext, bucket in sorted(
            summary["by_extension"].items(),
            key=lambda kv: (-kv[1]["count"], kv[0]),
        ):
            parts.append(
                f"    {ext:<10} {bucket['count']:>5} files  "
                f"{_probe._human_size(bucket['bytes']):>10}"
            )
    if summary["truncated"]:
        parts.append(
            f"  note: truncated at --max-files={summary['truncated_limit']}; "
            f"raise the cap to see the rest."
        )
    return "\n".join(parts)


def render_json(entries, summary):
    """JSON envelope with the inspect-specific summary block."""
    return json.dumps(
        {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "files": entries,
            "summary": summary,
        },
        indent=2,
        ensure_ascii=False,
    )


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #


def run(args):
    if args.max_depth is not None and args.max_depth < 0:
        err("--max-depth must be >= 0")
    if args.max_files is not None and args.max_files <= 0:
        err("--max-files must be > 0")
    if args.snippet < 0:
        err("--snippet must be >= 0")

    extensions = _probe._normalize_extensions(args.ext)

    entries = []
    truncated_marker = None
    for item in _probe.scan_directory(
        args.target,
        extensions=extensions,
        max_depth=args.max_depth,
        max_files=args.max_files,
        include_hidden=args.include_hidden,
        supported_only=args.supported_only,
        follow_symlinks=args.follow_symlinks,
    ):
        if item.get("_truncated"):
            truncated_marker = item
            continue
        # Layer L1 enrichment on top of L0 metadata. Done one file at a time
        # so a single corrupt PDF doesn't take down the whole report.
        l1 = inspect_file(Path(item["path"]), snippet_chars=args.snippet)
        item.update(l1)
        entries.append(item)

    entries_for_summary = entries + ([truncated_marker] if truncated_marker else [])
    summary = summarize(entries_for_summary)

    if args.json:
        report = render_json(entries, summary)
    else:
        report = render_table(entries, summary)

    print(report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report + "\n", encoding="utf-8")
        print(f"wrote inspect report to {args.output}", file=sys.stderr)
    return 0
