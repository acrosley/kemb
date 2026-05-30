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
import stat
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, List, Optional, TypedDict

from ._common import err


# --------------------------------------------------------------------------- #
# Output shapes
#
# probe's table and --json output are a public contract — downstream tools pipe
# the JSON into other steps. These TypedDicts document that contract in one
# place. They add no runtime overhead (with `from __future__ import
# annotations` the bodies are never evaluated) and serialize as plain dicts.
# --------------------------------------------------------------------------- #


class FileInfo(TypedDict):
    """Per-file metadata, one entry in the report's ``files`` list."""

    path: str
    relative: str
    name: str
    extension: str
    size: int
    size_human: str
    mtime: float
    mtime_iso: Optional[str]
    mime_type: Optional[str]
    supported: bool
    readable: bool
    error: Optional[str]


class WalkError(TypedDict):
    """A directory ``os.walk`` could not enter (permission denied, etc.)."""

    path: str
    error: str


class ExtensionBucket(TypedDict):
    """Aggregate counts for one extension in the summary."""

    count: int
    bytes: int


class ProbeSummary(TypedDict):
    """Corpus-level totals computed from the file stream."""

    total_files: int
    total_bytes: int
    total_size_human: str
    supported_files: int
    supported_bytes: int
    supported_size_human: str
    unreadable: int
    truncated: bool
    truncated_limit: Optional[int]
    walk_errors: List[WalkError]
    by_extension: dict


class ProbeReport(TypedDict):
    """The full ``--json`` envelope."""

    generated_at: str
    files: List[FileInfo]
    summary: ProbeSummary

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
            "  kemb probe ./inbox\n"
            "  kemb probe ./inbox --ext pdf,docx\n"
            "  kemb probe ./inbox --max-depth 2 --supported-only\n"
            "  kemb probe ./inbox --json > inventory.json\n"
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


# On Windows, hidden files are marked by an NTFS attribute bit rather than a
# leading dot (Thumbs.db, desktop.ini, anything `attrib +h`'d via Explorer).
# Falls back to the POSIX dot convention everywhere; the attribute check is
# additive so a dotfile on Windows is still treated as hidden.
_WINDOWS_HIDDEN_BIT = getattr(stat, "FILE_ATTRIBUTE_HIDDEN", 0x2)


def _is_hidden(path):
    """Return True if ``path`` is hidden by POSIX or Windows convention.

    Accepts either a bare name (str) or a Path. The Windows attribute check
    requires a real path and is skipped when only a name is supplied — callers
    that want full cross-platform behavior should pass a Path.
    """
    name = path.name if isinstance(path, Path) else str(path)
    if name.startswith("."):
        return True
    if os.name == "nt" and isinstance(path, Path):
        try:
            attrs = path.stat().st_file_attributes
        except (OSError, AttributeError):
            return False
        return bool(attrs & _WINDOWS_HIDDEN_BIT)
    return False


def _passes_filters(info, *, extensions, supported_only):
    """Return True if a described file survives the user-supplied filters.

    Used for both directory walks and single-file targets so a `probe file.txt
    --ext pdf` rejects what `probe ./dir --ext pdf` would have skipped over.
    """
    if extensions is not None and info["extension"] not in extensions:
        return False
    if supported_only and not info["supported"]:
        return False
    return True


def scan_directory(
    target,
    *,
    extensions=None,
    max_depth=None,
    max_files=DEFAULT_MAX_FILES,
    include_hidden=False,
    supported_only=False,
    follow_symlinks=False,
) -> Iterator[dict]:
    """Yield per-file metadata dicts for everything under ``target``.

    Files are emitted in walk order. The caller decides how to display or
    aggregate — see `run()` for the table/JSON renderers.

    Two sentinel shapes may also be yielded so callers can surface them:
      - ``{"_truncated": True, "limit": N}`` — once, at the end, if --max-files
        was reached.
      - ``{"_walk_error": {"path": str, "error": str}}`` — once per directory
        os.walk could not enter (permission denied, race-deleted, etc.). These
        are reported rather than silently dropped so an inventory the user
        believes is complete cannot quietly omit an unreadable subtree.
    """
    target = Path(target)
    if not target.exists():
        err(f"probe target not found: {target}")

    if target.is_file():
        # Treat a single-file target as a one-entry scan, but apply the same
        # --ext / --supported-only / hidden filters the directory walk uses so
        # `probe a.txt --ext pdf` and `probe ./dir --ext pdf` agree on `a.txt`.
        if not include_hidden and _is_hidden(target):
            return
        info = _describe_file(target, target.parent)
        if _passes_filters(info, extensions=extensions, supported_only=supported_only):
            yield info
        return

    if not target.is_dir():
        err(f"probe target is neither a file nor a directory: {target}")

    base_depth = len(target.parts)
    emitted = 0
    truncated = False

    # os.walk defaults to onerror=None, which silently ignores scandir errors
    # (PermissionError, a directory race-deleted mid-walk, etc.). Collect them
    # so they can be reported instead of vanishing from the inventory.
    walk_errors = []

    def _on_walk_error(exc):
        walk_errors.append({
            "path": getattr(exc, "filename", None) or str(target),
            "error": f"{type(exc).__name__}: {exc}",
        })

    for root, dirs, files in os.walk(
        target, followlinks=follow_symlinks, onerror=_on_walk_error
    ):
        root_path = Path(root)

        if not include_hidden:
            # Prune hidden directories in place so os.walk skips them entirely.
            # Pass the full Path so the Windows attribute check sees the inode.
            dirs[:] = [d for d in dirs if not _is_hidden(root_path / d)]

        if max_depth is not None:
            depth = len(root_path.parts) - base_depth
            if depth >= max_depth:
                # We've already listed the files at this depth; stop descending.
                dirs[:] = []

        # Stable order for predictable test snapshots and predictable batch runs.
        dirs.sort()
        files.sort()

        for name in files:
            if not include_hidden and _is_hidden(root_path / name):
                continue

            info = _describe_file(root_path / name, target)

            if not _passes_filters(
                info, extensions=extensions, supported_only=supported_only
            ):
                continue

            yield info
            emitted += 1
            if emitted >= max_files:
                truncated = True
                break
        if truncated:
            break

    # Surface any directories os.walk could not enter, after the file stream.
    for walk_error in walk_errors:
        yield {"_walk_error": walk_error}

    if truncated:
        # Signal truncation via a final sentinel dict the renderer can detect.
        yield {"_truncated": True, "limit": max_files}


def _describe_file(path, base) -> FileInfo:
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


def summarize(entries) -> ProbeSummary:
    """Reduce the per-file stream to aggregate counts."""
    total_files = 0
    total_bytes = 0
    supported_files = 0
    supported_bytes = 0
    unreadable = 0
    truncated = False
    truncated_limit = None
    walk_errors = []
    by_ext = {}

    for entry in entries:
        if entry.get("_truncated"):
            truncated = True
            truncated_limit = entry.get("limit")
            continue
        if entry.get("_walk_error"):
            walk_errors.append(entry["_walk_error"])
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
        "walk_errors": walk_errors,
        "by_extension": by_ext,
    }


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def render_table(entries, summary) -> str:
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
    walk_errors = summary.get("walk_errors") or []
    if walk_errors:
        parts.append(f"  unreadable dirs : {len(walk_errors)}")
        for we in walk_errors:
            parts.append(f"    {we['path']}: {we['error']}")
    return "\n".join(parts)


def render_json(entries, summary) -> str:
    """Compose the JSON envelope: files + summary + generated_at."""
    report: ProbeReport = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "files": entries,
        "summary": summary,
    }
    return json.dumps(report, indent=2, ensure_ascii=False)


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
    sentinels = []
    for item in scan_directory(
        args.target,
        extensions=extensions,
        max_depth=args.max_depth,
        max_files=args.max_files,
        include_hidden=args.include_hidden,
        supported_only=args.supported_only,
        follow_symlinks=args.follow_symlinks,
    ):
        if item.get("_truncated") or item.get("_walk_error"):
            sentinels.append(item)
        else:
            entries.append(item)

    # summarize() reads the truncation + walk-error sentinels alongside files.
    summary = summarize(entries + sentinels)

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
