"""Probe — recursively scan a directory and report file metadata.

Walks a target directory and reports per-file metadata (size, mtime,
extension, mime type, and whether LlamaCloud is likely to accept it). No
network calls, no LlamaCloud credits spent — it's a local-only preflight
for batch jobs and a companion to `--dry-run`.

Output is a human-readable table by default; `--json` emits a single JSON
object so downstream tools can pipe results into a shell loop.

Exit codes:
    0 — directory scanned (even if it contained zero files)
    2 — bad arguments (missing path, etc.)
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from ._common import err

# File formats LlamaCloud's document APIs (parse/extract/classify/split) will
# accept. Kept as a conservative set drawn from the public LlamaParse
# supported-formats list — formats outside this set still upload, but may be
# rejected server-side, so probe flags them as "unsupported" upfront.
SUPPORTED_EXTENSIONS = frozenset({
    # PDF
    ".pdf",
    # Microsoft Office
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    # OpenDocument
    ".odt", ".ods", ".odp",
    # Plain text / markup
    ".txt", ".md", ".rst", ".csv", ".tsv", ".html", ".htm", ".xml",
    # Rich text / e-books
    ".rtf", ".epub",
    # Images (parse handles OCR)
    ".png", ".jpg", ".jpeg", ".tiff", ".tif", ".webp", ".bmp", ".gif",
})

# Caps so an accidental probe over `/` or a huge tree doesn't blow up the
# terminal. The defaults are generous; --max-files / --max-depth tighten.
DEFAULT_MAX_FILES = 10_000


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "probe",
        help="Scan a directory recursively and report file metadata.",
        description=(
            "Walk a directory and report each file's size, mtime, extension, "
            "and whether LlamaCloud is likely to accept it. Spends zero "
            "credits — useful for previewing batch jobs and pairing with "
            "`--dry-run` on parse/extract/classify/split."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  llamaparse probe ./inbox\n"
            "  llamaparse probe ./inbox --ext pdf,docx\n"
            "  llamaparse probe ./inbox --max-depth 2 --supported-only\n"
            "  llamaparse probe ./inbox --json > inventory.json\n"
        ),
    )
    p.add_argument(
        "target",
        type=Path,
        help="Directory to scan. A single file is also accepted and reported as-is.",
    )
    p.add_argument(
        "--ext",
        default=None,
        help="Comma-separated extension allowlist (e.g. 'pdf,docx,png'). "
             "Leading dots optional, case-insensitive.",
    )
    p.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Maximum recursion depth (0 = target directory only). Unlimited by default.",
    )
    p.add_argument(
        "--max-files",
        type=int,
        default=DEFAULT_MAX_FILES,
        help=f"Stop scanning after this many files (default: {DEFAULT_MAX_FILES}).",
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
        help="Follow symlinked directories during the walk (off by default to "
             "avoid loops).",
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
        help="Write the probe report to this file (in addition to stdout).",
    )
    p.set_defaults(func=run)
    return p


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _normalize_extensions(raw):
    """Turn 'pdf, .DOCX,png' into the set {'.pdf', '.docx', '.png'}."""
    if not raw:
        return None
    out = set()
    for part in str(raw).split(","):
        s = part.strip().lower()
        if not s:
            continue
        if not s.startswith("."):
            s = "." + s
        out.add(s)
    return out or None


def _human_size(n):
    """Render a byte count as a short, fixed-width string ('4.2 KB')."""
    if n < 1024:
        return f"{n} B"
    units = ("KB", "MB", "GB", "TB", "PB")
    size = float(n)
    for unit in units:
        size /= 1024.0
        if size < 1024.0 or unit == units[-1]:
            return f"{size:.1f} {unit}"
    return f"{size:.1f} {units[-1]}"


def _iso_mtime(ts):
    """Format a POSIX mtime as ISO-8601 UTC ('2026-04-09T12:34:56Z')."""
    try:
        return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, OSError, OverflowError):
        return "?"


def _is_hidden(name):
    return name.startswith(".")


def scan_directory(
    target,
    *,
    extensions=None,
    max_depth=None,
    max_files=DEFAULT_MAX_FILES,
    include_hidden=False,
    supported_only=False,
    follow_symlinks=False,
):
    """Yield per-file metadata dicts for everything under ``target``.

    Files are emitted in walk order. The caller decides how to display or
    aggregate — see `run()` for the table/JSON renderers.
    """
    target = Path(target)
    if not target.exists():
        err(f"probe target not found: {target}")

    if target.is_file():
        # Treat a single-file target as a one-entry scan.
        yield _describe_file(target, target.parent)
        return

    if not target.is_dir():
        err(f"probe target is neither a file nor a directory: {target}")

    base_depth = len(target.parts)
    emitted = 0
    truncated = False

    for root, dirs, files in os.walk(target, followlinks=follow_symlinks):
        root_path = Path(root)

        if not include_hidden:
            # Prune hidden directories in place so os.walk skips them entirely.
            dirs[:] = [d for d in dirs if not _is_hidden(d)]

        if max_depth is not None:
            depth = len(root_path.parts) - base_depth
            if depth >= max_depth:
                # We've already listed the files at this depth; stop descending.
                dirs[:] = []

        # Stable order for predictable test snapshots and predictable batch runs.
        dirs.sort()
        files.sort()

        for name in files:
            if not include_hidden and _is_hidden(name):
                continue

            info = _describe_file(root_path / name, target)

            if extensions is not None and info["extension"] not in extensions:
                continue
            if supported_only and not info["supported"]:
                continue

            yield info
            emitted += 1
            if emitted >= max_files:
                truncated = True
                break
        if truncated:
            break

    if truncated:
        # Signal truncation via a final sentinel dict the renderer can detect.
        yield {"_truncated": True, "limit": max_files}


def _describe_file(path, base):
    """Build the metadata dict for one file."""
    try:
        st = path.stat()
        size = st.st_size
        mtime = st.st_mtime
        readable = True
    except OSError as e:
        size = 0
        mtime = 0.0
        readable = False
        read_error = str(e)
    else:
        read_error = None

    ext = path.suffix.lower()
    mime, _ = mimetypes.guess_type(path.name)

    try:
        relative = str(path.relative_to(base))
    except ValueError:
        relative = str(path)

    return {
        "path": str(path),
        "relative": relative,
        "name": path.name,
        "extension": ext,
        "size": size,
        "size_human": _human_size(size),
        "mtime": mtime,
        "mtime_iso": _iso_mtime(mtime) if mtime else None,
        "mime_type": mime,
        "supported": ext in SUPPORTED_EXTENSIONS,
        "readable": readable,
        "error": read_error,
    }


def summarize(entries):
    """Reduce the per-file stream to aggregate counts."""
    total_files = 0
    total_bytes = 0
    supported_files = 0
    supported_bytes = 0
    unreadable = 0
    truncated = False
    truncated_limit = None
    by_ext = {}

    for entry in entries:
        if entry.get("_truncated"):
            truncated = True
            truncated_limit = entry.get("limit")
            continue
        total_files += 1
        total_bytes += entry["size"]
        if entry["supported"]:
            supported_files += 1
            supported_bytes += entry["size"]
        if not entry["readable"]:
            unreadable += 1
        ext = entry["extension"] or "(no ext)"
        bucket = by_ext.setdefault(ext, {"count": 0, "bytes": 0})
        bucket["count"] += 1
        bucket["bytes"] += entry["size"]

    return {
        "total_files": total_files,
        "total_bytes": total_bytes,
        "total_size_human": _human_size(total_bytes),
        "supported_files": supported_files,
        "supported_bytes": supported_bytes,
        "supported_size_human": _human_size(supported_bytes),
        "unreadable": unreadable,
        "truncated": truncated,
        "truncated_limit": truncated_limit,
        "by_extension": by_ext,
    }


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def render_table(entries, summary):
    """Render the probe report as a fixed-width ASCII table.

    Returns the full report as one string so the caller can both print it
    and (optionally) write it to --output.
    """
    lines = []
    if not entries:
        lines.append("no files matched.")
    else:
        # Compute column widths from the data, with sensible minimums so
        # short scans still line up nicely.
        path_w = max(8, *(len(e["relative"]) for e in entries))
        size_w = max(8, *(len(e["size_human"]) for e in entries))
        mtime_w = 20  # ISO-8601 timestamps are 20 chars.

        header = f"{'PATH':<{path_w}}  {'SIZE':>{size_w}}  {'MODIFIED':<{mtime_w}}  TYPE"
        lines.append(header)
        lines.append("-" * len(header))
        for e in entries:
            kind = "ok" if e["supported"] else "skip"
            if not e["readable"]:
                kind = "err"
            lines.append(
                f"{e['relative']:<{path_w}}  "
                f"{e['size_human']:>{size_w}}  "
                f"{(e['mtime_iso'] or '?'):<{mtime_w}}  "
                f"{e['extension'] or '(none)'} [{kind}]"
            )

    lines.append("")
    lines.append(_summary_block(summary))
    return "\n".join(lines)


def _summary_block(summary):
    """Multi-line human summary printed after the table."""
    parts = [
        "summary:",
        f"  total files     : {summary['total_files']}",
        f"  total size      : {summary['total_size_human']} "
        f"({summary['total_bytes']:,} bytes)",
        f"  supported files : {summary['supported_files']} "
        f"({summary['supported_size_human']})",
    ]
    if summary["unreadable"]:
        parts.append(f"  unreadable      : {summary['unreadable']}")
    if summary["by_extension"]:
        parts.append("  by extension    :")
        for ext, bucket in sorted(
            summary["by_extension"].items(),
            key=lambda kv: (-kv[1]["count"], kv[0]),
        ):
            parts.append(
                f"    {ext:<10} {bucket['count']:>5} files  "
                f"{_human_size(bucket['bytes']):>10}"
            )
    if summary["truncated"]:
        parts.append(
            f"  note: truncated at --max-files={summary['truncated_limit']}; "
            f"raise the cap to see the rest."
        )
    return "\n".join(parts)


def render_json(entries, summary):
    """Compose the JSON envelope: files + summary + generated_at."""
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

    extensions = _normalize_extensions(args.ext)

    entries = []
    truncated_marker = None
    for item in scan_directory(
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
        else:
            entries.append(item)

    # Re-attach the truncation flag for summarize() to see.
    if truncated_marker:
        entries_for_summary = entries + [truncated_marker]
    else:
        entries_for_summary = entries
    summary = summarize(entries_for_summary)

    if args.json:
        report = render_json(entries, summary)
    else:
        report = render_table(entries, summary)

    print(report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report + "\n", encoding="utf-8")
        print(f"wrote probe report to {args.output}", file=sys.stderr)
    return 0
