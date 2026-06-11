"""Index — a persistent, incremental SQLite inventory of a corpus.

`probe` answers "what's in this pile?" by re-walking and re-reading the tree
on every invocation. That's fine at hundreds of files and hopeless at
100,000+: re-opening every PDF takes hours and nothing remembers the result.
`index` is the persistent version: one SQLite database per corpus that scans
incrementally — only files whose (size, mtime) changed since the last run are
re-read — so the first scan pays full price and every scan after is seconds.

The database is the "queryable manifest" of the kembing arc (probe → plan →
pass → mirror): `plan` can partition it into shards with SQL, `pass` can
record per-file job status in it (making 100k-file batches resumable), and
the mirror can stamp its frontmatter from the stored content hashes.

Queries (`--stats`, `--search`) run that same incremental refresh before
answering — sync-on-read, the git model — so they never serve a confidently
stale view of a corpus that's still on disk. `--stale` skips the refresh for
zero-I/O reads.

Like probe, this facet is **local-only and free**: no network, no API key,
no credits.

Schema (``PRAGMA user_version = 1``)
------------------------------------

``files`` — one row per file ever seen under the corpus root:

    id              INTEGER PRIMARY KEY
    relative        TEXT UNIQUE     -- posix relative path; the document id
    name            TEXT
    extension       TEXT            -- lowercased, with dot
    size            INTEGER         -- bytes, at last scan
    mtime           REAL            -- POSIX mtime, at last scan
    mime_type       TEXT
    supported       INTEGER         -- LlamaCloud likely accepts (0/1)
    sha256          TEXT            -- content hash; powers dedup + mirror stamps
    pages           INTEGER         -- PDFs only
    sample_status   TEXT            -- ok | no-text | no-extractor | error
    sample_detail   TEXT            -- why, when status != ok
    sample_text     TEXT            -- first words, extracted locally
    sample_words    INTEGER
    first_seen      TEXT            -- ISO-8601 UTC
    last_seen       TEXT            -- bumped every scan that sees the file
    content_scanned TEXT            -- when hash/sample were last computed
    missing         INTEGER         -- 1 = was indexed, gone from disk now

``passes`` — one row per parse/classify job over a file. Nothing writes it
yet; it ships in schema v1 so the upcoming batch facet can record and resume
work against existing databases without a migration:

    id, file_id → files(id), facet, tier,
    status (pending|running|done|failed|skipped),
    credits, output_path, started, finished, error

``files_fts`` — FTS5 external-content index over (relative, sample_text),
kept in sync by triggers. Created only when the sqlite build has FTS5;
`--search` degrades to a LIKE substring scan without it.

``meta`` — key/value: schema_version, root, created, fts, kemb_version.

Incremental contract: a file is re-read (hashed + sampled) only when it is
new, its (size, mtime) pair changed, or ``--full`` forces it. A rewrite that
preserves both size and mtime is invisible — the same trade every
mtime-based build tool makes.

Exit codes:
    0 — scan / stats / search completed
    2 — bad arguments, missing index for --stats/--search
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from ._common import err
from ._probe import (
    DEFAULT_SAMPLE_PAGES,
    DEFAULT_SAMPLE_WORDS,
    _human_size,
    _normalize_extensions,
    scan_directory,
)
from ._sample import sample_file

SCHEMA_VERSION = 1

# Default location of the database, relative to the corpus root. Dot-prefixed
# so default walks (which skip hidden directories) never index the index.
DB_DIRNAME = ".kemb"
DB_FILENAME = "index.db"

_HASH_CHUNK = 1 << 20  # 1 MiB

_SCHEMA = """
CREATE TABLE meta (
    key   TEXT PRIMARY KEY,
    value TEXT
);
CREATE TABLE files (
    id              INTEGER PRIMARY KEY,
    relative        TEXT NOT NULL UNIQUE,
    name            TEXT NOT NULL,
    extension       TEXT NOT NULL,
    size            INTEGER NOT NULL,
    mtime           REAL NOT NULL,
    mime_type       TEXT,
    supported       INTEGER NOT NULL,
    sha256          TEXT,
    pages           INTEGER,
    sample_status   TEXT,
    sample_detail   TEXT,
    sample_text     TEXT,
    sample_words    INTEGER NOT NULL DEFAULT 0,
    first_seen      TEXT NOT NULL,
    last_seen       TEXT NOT NULL,
    content_scanned TEXT,
    missing         INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX ix_files_sha256 ON files(sha256);
CREATE INDEX ix_files_extension ON files(extension);
CREATE TABLE passes (
    id          INTEGER PRIMARY KEY,
    file_id     INTEGER NOT NULL REFERENCES files(id) ON DELETE CASCADE,
    facet       TEXT NOT NULL,
    tier        TEXT,
    status      TEXT NOT NULL DEFAULT 'pending',
    credits     INTEGER,
    output_path TEXT,
    started     TEXT,
    finished    TEXT,
    error       TEXT
);
CREATE INDEX ix_passes_file ON passes(file_id);
CREATE INDEX ix_passes_status ON passes(status);
"""

# External-content FTS5: the files table stays the single source of truth and
# the triggers keep the index in lockstep with every insert/update/delete.
_FTS_SCHEMA = """
CREATE VIRTUAL TABLE files_fts USING fts5(
    relative, sample_text, content='files', content_rowid='id'
);
CREATE TRIGGER files_ai AFTER INSERT ON files BEGIN
    INSERT INTO files_fts(rowid, relative, sample_text)
    VALUES (new.id, new.relative, new.sample_text);
END;
CREATE TRIGGER files_ad AFTER DELETE ON files BEGIN
    INSERT INTO files_fts(files_fts, rowid, relative, sample_text)
    VALUES ('delete', old.id, old.relative, old.sample_text);
END;
CREATE TRIGGER files_au AFTER UPDATE ON files BEGIN
    INSERT INTO files_fts(files_fts, rowid, relative, sample_text)
    VALUES ('delete', old.id, old.relative, old.sample_text);
    INSERT INTO files_fts(rowid, relative, sample_text)
    VALUES (new.id, new.relative, new.sample_text);
END;
"""


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "index",
        help="Maintain a persistent SQLite inventory of a corpus (incremental).",
        description=(
            "Scan a directory into a per-corpus SQLite database. Only files "
            "whose size or mtime changed since the last run are re-read, so "
            "repeat scans over large corpora take seconds. Stores per-file "
            "metadata, a sha256 content hash, and a locally extracted text "
            "sample; query it with --stats and --search. Zero credits, no "
            "network."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  kemb index ./corpus                       # create or refresh the index\n"
            "  kemb index ./corpus --stats               # report on the index, no rescan\n"
            "  kemb index ./corpus --search 'force majeure'\n"
            "  kemb index ./corpus --full                # re-read every file\n"
            "  kemb index ./corpus --json > scan.json    # machine-readable scan report\n"
        ),
    )
    p.add_argument(
        "target",
        type=Path,
        help="Corpus root directory to index.",
    )
    p.add_argument(
        "--db",
        type=Path,
        default=None,
        help=f"Database path (default: <target>/{DB_DIRNAME}/{DB_FILENAME}).",
    )
    p.add_argument(
        "--stats",
        action="store_true",
        help="Report on the existing index (counts, duplicates, sample "
             "statuses, passes). Runs an incremental refresh first unless "
             "--stale is passed.",
    )
    p.add_argument(
        "--search",
        metavar="QUERY",
        default=None,
        help="Full-text search the indexed samples and paths (FTS5 syntax; "
             "falls back to substring match when FTS5 is unavailable).",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Max results for --search (default: 20).",
    )
    p.add_argument(
        "--stale",
        action="store_true",
        help="Skip the incremental refresh --stats/--search run before "
             "answering; serve whatever the index already holds (zero "
             "filesystem reads).",
    )
    p.add_argument(
        "--full",
        action="store_true",
        help="Re-hash and re-sample every file even when size+mtime are "
             "unchanged (catches edits that preserved both).",
    )
    p.add_argument(
        "--ext",
        default=None,
        help="Comma-separated extension allowlist for the scan (e.g. 'pdf,docx').",
    )
    p.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Maximum recursion depth (0 = target directory only). Unlimited "
             "by default.",
    )
    p.add_argument(
        "--max-files",
        type=int,
        default=None,
        help="Stop scanning after this many files. Unlimited by default — "
             "unlike probe, an index is meant to see the whole corpus.",
    )
    p.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include dotfiles and hidden directories (skipped by default).",
    )
    p.add_argument(
        "--follow-symlinks",
        action="store_true",
        help="Follow symlinked directories during the walk (off by default).",
    )
    p.add_argument(
        "--sample-words",
        type=int,
        default=DEFAULT_SAMPLE_WORDS,
        help=f"Max words sampled per document (default: {DEFAULT_SAMPLE_WORDS}).",
    )
    p.add_argument(
        "--sample-pages",
        type=int,
        default=DEFAULT_SAMPLE_PAGES,
        help="Max PDF pages to pull sample text from "
             f"(default: {DEFAULT_SAMPLE_PAGES}).",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of the human report.",
    )
    p.add_argument(
        "--auto-install",
        action="store_true",
        help="No-op: index is local-only and never needs the llama-cloud "
             "SDK. Accepted so callers (including the bundled skill shim) "
             "can pass it on every facet.",
    )
    p.set_defaults(func=run)
    return p


# --------------------------------------------------------------------------- #
# Database plumbing
# --------------------------------------------------------------------------- #


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def default_db_path(target: Path) -> Path:
    return Path(target) / DB_DIRNAME / DB_FILENAME


def _connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path), timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        # WAL lets a reader (--stats/--search) coexist with a running scan.
        # Some filesystems (network mounts) refuse it; the default journal
        # works there, just without concurrent readers.
        conn.execute("PRAGMA journal_mode = WAL")
    except sqlite3.OperationalError:
        pass
    return conn


def _fts_available(conn: sqlite3.Connection) -> bool:
    try:
        conn.execute(
            "CREATE VIRTUAL TABLE temp.fts_probe USING fts5(x)"
        )
        conn.execute("DROP TABLE temp.fts_probe")
        return True
    except sqlite3.OperationalError:
        return False


def _kemb_version() -> str:
    try:
        from importlib.metadata import version
        return version("kemb")
    except Exception:
        return "unknown"


def open_index(db_path: Path, root: Path, *, create: bool) -> sqlite3.Connection:
    """Open the index database, creating and initializing it if allowed.

    ``create=False`` (the --stats/--search paths) errors out when no index
    exists instead of silently materializing an empty one.
    """
    db_path = Path(db_path)
    if not db_path.exists():
        if not create:
            err(
                f"no index at {db_path} — run `kemb index {root}` first to "
                "build one"
            )
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = _connect(db_path)
        with conn:
            conn.executescript(_SCHEMA)
            fts = _fts_available(conn)
            if fts:
                conn.executescript(_FTS_SCHEMA)
            conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
            conn.executemany(
                "INSERT INTO meta (key, value) VALUES (?, ?)",
                [
                    ("schema_version", str(SCHEMA_VERSION)),
                    ("root", str(Path(root).resolve())),
                    ("created", _now_iso()),
                    ("fts", "1" if fts else "0"),
                    ("kemb_version", _kemb_version()),
                    ("sample_words", str(DEFAULT_SAMPLE_WORDS)),
                    ("sample_pages", str(DEFAULT_SAMPLE_PAGES)),
                ],
            )
        return conn

    conn = _connect(db_path)
    found = conn.execute("PRAGMA user_version").fetchone()[0]
    if found != SCHEMA_VERSION:
        conn.close()
        err(
            f"index at {db_path} has schema v{found}, this kemb expects "
            f"v{SCHEMA_VERSION} — rebuild it (delete the file and rescan) or "
            "upgrade kemb"
        )
    return conn


def _meta(conn: sqlite3.Connection) -> dict:
    return {
        row["key"]: row["value"]
        for row in conn.execute("SELECT key, value FROM meta")
    }


# --------------------------------------------------------------------------- #
# Content scanning (the expensive part the incremental check avoids)
# --------------------------------------------------------------------------- #


def _hash_file(path: str) -> Optional[str]:
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            while True:
                chunk = fh.read(_HASH_CHUNK)
                if not chunk:
                    break
                h.update(chunk)
    except OSError:
        return None
    return h.hexdigest()


def _content_fields(info: dict, *, sample_words: int, sample_pages: int) -> dict:
    """Hash + sample one file. This is the only full read of the file."""
    if info["readable"]:
        sha = _hash_file(info["path"])
        sample = sample_file(
            info["path"], info["extension"],
            max_words=sample_words, pdf_pages=sample_pages,
        )
    else:
        sha = None
        sample = {
            "status": "error", "text": "", "words": 0, "pages": None,
            "detail": info["error"],
        }
    return {
        "sha256": sha,
        "pages": sample["pages"],
        "sample_status": sample["status"],
        "sample_detail": sample["detail"],
        "sample_text": sample["text"],
        "sample_words": sample["words"],
        "content_scanned": _now_iso(),
    }


def _row_params(info: dict, content: dict, scan_time: str) -> dict:
    """Exactly the named parameters the INSERT/UPDATE statements bind.

    Built explicitly (rather than splatting the walked-info dict) so the
    statements never depend on probe's FileInfo shape staying superset-
    compatible with the schema.
    """
    return {
        "relative": info["relative"],
        "name": info["name"],
        "extension": info["extension"],
        "size": info["size"],
        "mtime": info["mtime"],
        "mime_type": info["mime_type"],
        "supported": 1 if info["supported"] else 0,
        "sha256": content["sha256"],
        "pages": content["pages"],
        "sample_status": content["sample_status"],
        "sample_detail": content["sample_detail"],
        "sample_text": content["sample_text"],
        "sample_words": content["sample_words"],
        "first_seen": scan_time,
        "last_seen": scan_time,
        "content_scanned": content["content_scanned"],
    }


# --------------------------------------------------------------------------- #
# Incremental scan
# --------------------------------------------------------------------------- #


def scan_into_index(
    conn: sqlite3.Connection,
    target: Path,
    db_path: Path,
    *,
    extensions=None,
    max_depth=None,
    max_files=None,
    include_hidden=False,
    follow_symlinks=False,
    full=False,
    sample_words=DEFAULT_SAMPLE_WORDS,
    sample_pages=DEFAULT_SAMPLE_PAGES,
) -> dict:
    """Walk ``target`` and reconcile the database with the filesystem.

    Returns a scan report dict (counts + timing). Decision per walked file:

      - not in the database              → ADD    (hash + sample + insert)
      - (size, mtime) changed or --full  → CHANGE (hash + sample + update)
      - previously missing, now back     → RESTORE (content re-read only if
                                           size/mtime moved while it was gone)
      - otherwise                        → UNCHANGED (bump last_seen only;
                                           the file is never opened)

    Rows in the database but absent from the walk are marked ``missing=1``
    rather than deleted — pass history may reference them, and a file that
    reappears keeps its identity and history.
    """
    started = time.monotonic()
    scan_time = _now_iso()

    known = {
        row["relative"]: row
        for row in conn.execute(
            "SELECT id, relative, size, mtime, missing FROM files"
        )
    }

    # Never index the index. The default location is hidden (skipped anyway),
    # but a custom --db inside the corpus, or --include-hidden, would
    # otherwise pull the database (and its WAL siblings) into itself.
    db_abs = os.path.normcase(os.path.abspath(str(db_path)))
    skip_paths = {db_abs, db_abs + "-wal", db_abs + "-shm"}

    added = changed = unchanged = restored = 0
    walk_errors = []
    truncated = False

    seen_ids = []          # rows to bump last_seen on, in bulk
    inserts = []
    updates = []

    for info in scan_directory(
        target,
        extensions=extensions,
        max_depth=max_depth,
        max_files=max_files if max_files is not None else sys.maxsize,
        include_hidden=include_hidden,
        supported_only=False,
        follow_symlinks=follow_symlinks,
    ):
        if info.get("_walk_error"):
            walk_errors.append(info["_walk_error"])
            continue
        if info.get("_truncated"):
            truncated = True
            continue
        if os.path.normcase(os.path.abspath(info["path"])) in skip_paths:
            continue

        row = known.pop(info["relative"], None)
        if row is None:
            content = _content_fields(
                info, sample_words=sample_words, sample_pages=sample_pages
            )
            inserts.append(_row_params(info, content, scan_time))
            added += 1
            continue

        stat_changed = (row["size"] != info["size"]
                        or row["mtime"] != info["mtime"])
        was_missing = bool(row["missing"])
        if stat_changed or full:
            content = _content_fields(
                info, sample_words=sample_words, sample_pages=sample_pages
            )
            params = _row_params(info, content, scan_time)
            params["id"] = row["id"]
            updates.append(params)
            if was_missing:
                restored += 1
            elif stat_changed:
                changed += 1
            else:
                unchanged += 1  # --full re-read of a stat-identical file
        else:
            seen_ids.append((scan_time, row["id"]))
            if was_missing:
                restored += 1
            else:
                unchanged += 1

    # Everything left in `known` was indexed before but not seen this walk.
    # On a filtered or truncated scan that's expected for the files the
    # filter excluded — only mark missing what this walk could have seen.
    newly_missing = 0
    if not truncated and extensions is None and max_depth is None:
        to_mark = [
            (scan_time, row["id"]) for row in known.values() if not row["missing"]
        ]
        newly_missing = len(to_mark)
        with conn:
            conn.executemany(
                "UPDATE files SET missing = 1, last_seen = ? WHERE id = ?",
                to_mark,
            )

    with conn:
        if inserts:
            conn.executemany(
                """
                INSERT INTO files (
                    relative, name, extension, size, mtime, mime_type,
                    supported, sha256, pages, sample_status, sample_detail,
                    sample_text, sample_words, first_seen, last_seen,
                    content_scanned, missing
                ) VALUES (
                    :relative, :name, :extension, :size, :mtime, :mime_type,
                    :supported, :sha256, :pages, :sample_status,
                    :sample_detail, :sample_text, :sample_words,
                    :first_seen, :last_seen, :content_scanned, 0
                )
                """,
                inserts,
            )
        if updates:
            conn.executemany(
                """
                UPDATE files SET
                    size = :size, mtime = :mtime, mime_type = :mime_type,
                    supported = :supported, sha256 = :sha256, pages = :pages,
                    sample_status = :sample_status,
                    sample_detail = :sample_detail,
                    sample_text = :sample_text, sample_words = :sample_words,
                    last_seen = :last_seen, content_scanned = :content_scanned,
                    missing = 0
                WHERE id = :id
                """,
                updates,
            )
        if seen_ids:
            conn.executemany(
                "UPDATE files SET last_seen = ?, missing = 0 WHERE id = ?",
                seen_ids,
            )
        # Remember the sample settings so the sync-on-read refresh resamples
        # changed files the same way this scan did, not at the defaults.
        conn.executemany(
            "INSERT OR REPLACE INTO meta (key, value) VALUES (?, ?)",
            [("sample_words", str(sample_words)),
             ("sample_pages", str(sample_pages))],
        )

    totals = conn.execute(
        """
        SELECT COUNT(*) AS files,
               COALESCE(SUM(size), 0) AS bytes,
               COALESCE(SUM(supported), 0) AS supported,
               COALESCE(SUM(missing), 0) AS missing
        FROM files
        """
    ).fetchone()
    dup = conn.execute(
        """
        SELECT COUNT(*) AS groups, COALESCE(SUM(n), 0) AS files
        FROM (
            SELECT COUNT(*) AS n FROM files
            WHERE missing = 0 AND sha256 IS NOT NULL
            GROUP BY sha256 HAVING COUNT(*) > 1
        )
        """
    ).fetchone()

    return {
        "db": str(db_path),
        "root": str(target),
        "scan_time": scan_time,
        "added": added,
        "changed": changed,
        "unchanged": unchanged,
        "restored": restored,
        "newly_missing": newly_missing,
        "total_files": totals["files"],
        "total_bytes": totals["bytes"],
        "supported_files": totals["supported"],
        "missing_files": totals["missing"],
        "duplicate_groups": dup["groups"],
        "duplicate_files": dup["files"],
        "walk_errors": walk_errors,
        "truncated": truncated,
        "elapsed_s": round(time.monotonic() - started, 3),
    }


# --------------------------------------------------------------------------- #
# Stats and search (read-only)
# --------------------------------------------------------------------------- #


def index_stats(conn: sqlite3.Connection, db_path: Path) -> dict:
    meta = _meta(conn)
    totals = conn.execute(
        """
        SELECT COUNT(*) AS files,
               COALESCE(SUM(size), 0) AS bytes,
               COALESCE(SUM(supported), 0) AS supported,
               COALESCE(SUM(missing), 0) AS missing,
               COALESCE(SUM(pages), 0) AS pages
        FROM files
        """
    ).fetchone()
    by_ext = {
        row["extension"] or "(no ext)": {"count": row["n"], "bytes": row["b"]}
        for row in conn.execute(
            """
            SELECT extension, COUNT(*) AS n, COALESCE(SUM(size), 0) AS b
            FROM files WHERE missing = 0
            GROUP BY extension ORDER BY n DESC, extension
            """
        )
    }
    by_status = {
        row["sample_status"] or "(none)": row["n"]
        for row in conn.execute(
            """
            SELECT sample_status, COUNT(*) AS n FROM files
            WHERE missing = 0 GROUP BY sample_status ORDER BY n DESC
            """
        )
    }
    dup_groups = [
        {"sha256": row["sha256"], "count": row["n"],
         "paths": row["paths"].split("\n")}
        for row in conn.execute(
            """
            SELECT sha256, COUNT(*) AS n,
                   GROUP_CONCAT(relative, char(10)) AS paths
            FROM files WHERE missing = 0 AND sha256 IS NOT NULL
            GROUP BY sha256 HAVING COUNT(*) > 1
            ORDER BY n DESC, sha256
            """
        )
    ]
    passes = {
        row["status"]: row["n"]
        for row in conn.execute(
            "SELECT status, COUNT(*) AS n FROM passes GROUP BY status"
        )
    }
    return {
        "db": str(db_path),
        "schema_version": int(meta.get("schema_version", 0)),
        "fts": meta.get("fts") == "1",
        "root": meta.get("root"),
        "created": meta.get("created"),
        "total_files": totals["files"],
        "total_bytes": totals["bytes"],
        "supported_files": totals["supported"],
        "missing_files": totals["missing"],
        "total_pages": totals["pages"],
        "by_extension": by_ext,
        "by_sample_status": by_status,
        "duplicate_groups": dup_groups,
        "passes_by_status": passes,
    }


def search_index(conn: sqlite3.Connection, query: str, limit: int) -> dict:
    """Full-text search over indexed paths and sample text.

    Uses FTS5 when the database was built with it; otherwise (or for queries
    FTS5 can't parse) falls back to a case-insensitive substring scan so
    --search always answers.
    """
    meta = _meta(conn)
    rows = None
    engine = "fts5"
    if meta.get("fts") == "1":
        try:
            rows = conn.execute(
                """
                SELECT f.relative, f.size, f.extension, f.sample_status,
                       snippet(files_fts, 1, '[', ']', ' .. ', 12) AS snippet
                FROM files_fts
                JOIN files f ON f.id = files_fts.rowid
                WHERE files_fts MATCH ? AND f.missing = 0
                ORDER BY rank LIMIT ?
                """,
                (query, limit),
            ).fetchall()
        except sqlite3.OperationalError:
            rows = None  # FTS5 query syntax error — fall back to substring
    if rows is None:
        engine = "substring"
        like = f"%{query}%"
        rows = conn.execute(
            """
            SELECT relative, size, extension, sample_status,
                   substr(sample_text, 1, 120) AS snippet
            FROM files
            WHERE missing = 0
              AND (sample_text LIKE ? OR relative LIKE ?)
            ORDER BY relative LIMIT ?
            """,
            (like, like, limit),
        ).fetchall()

    return {
        "query": query,
        "engine": engine,
        "limit": limit,
        "results": [
            {
                "relative": r["relative"],
                "size": r["size"],
                "extension": r["extension"],
                "sample_status": r["sample_status"],
                "snippet": (r["snippet"] or "").replace("\n", " ").strip(),
            }
            for r in rows
        ],
    }


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def render_scan_report(report: dict) -> str:
    lines = [
        f"indexed {report['root']} -> {report['db']}",
        f"  added      : {report['added']:,}",
        f"  changed    : {report['changed']:,}",
        f"  unchanged  : {report['unchanged']:,}",
    ]
    if report["restored"]:
        lines.append(f"  restored   : {report['restored']:,}")
    if report["newly_missing"]:
        lines.append(f"  now missing: {report['newly_missing']:,}")
    lines.append(
        f"  total      : {report['total_files']:,} files "
        f"({_human_size(report['total_bytes'])}), "
        f"{report['supported_files']:,} supported"
        + (f", {report['missing_files']:,} missing"
           if report["missing_files"] else "")
    )
    if report["duplicate_groups"]:
        lines.append(
            f"  duplicates : {report['duplicate_groups']:,} groups "
            f"({report['duplicate_files']:,} files) -- see --stats"
        )
    lines.append(f"  elapsed    : {report['elapsed_s']}s")
    if report["truncated"]:
        lines.append(
            "  note: walk stopped at --max-files; missing-file detection "
            "skipped on this partial scan."
        )
    for we in report["walk_errors"]:
        lines.append(f"  unreadable dir: {we['path']}: {we['error']}")
    return "\n".join(lines)


def render_stats(stats: dict) -> str:
    lines = [
        f"index: {stats['db']} (schema v{stats['schema_version']}, "
        f"fts {'enabled' if stats['fts'] else 'unavailable'})",
        f"  root       : {stats['root']}",
        f"  created    : {stats['created']}",
        f"  files      : {stats['total_files']:,} "
        f"({_human_size(stats['total_bytes'])}), "
        f"{stats['supported_files']:,} supported"
        + (f", {stats['missing_files']:,} missing"
           if stats["missing_files"] else ""),
    ]
    if stats["total_pages"]:
        lines.append(f"  pdf pages  : {stats['total_pages']:,}")
    if stats["by_extension"]:
        lines.append("  by extension:")
        for ext, bucket in stats["by_extension"].items():
            lines.append(
                f"    {ext:<10} {bucket['count']:>6,} files  "
                f"{_human_size(bucket['bytes']):>10}"
            )
    if stats["by_sample_status"]:
        lines.append("  sample status:")
        for status, n in stats["by_sample_status"].items():
            lines.append(f"    {status:<14} {n:>6,}")
    if stats["duplicate_groups"]:
        lines.append(f"  duplicates : {len(stats['duplicate_groups'])} groups")
        for group in stats["duplicate_groups"][:10]:
            lines.append(f"    {group['sha256'][:12]}.. x{group['count']}:")
            for p in group["paths"]:
                lines.append(f"      {p}")
        if len(stats["duplicate_groups"]) > 10:
            lines.append(
                f"    .. and {len(stats['duplicate_groups']) - 10} more "
                "groups (use --json for all)"
            )
    if stats["passes_by_status"]:
        rendered = ", ".join(
            f"{status}: {n}" for status, n in
            sorted(stats["passes_by_status"].items())
        )
        lines.append(f"  passes     : {rendered}")
    else:
        lines.append("  passes     : none recorded yet")
    return "\n".join(lines)


def render_search(result: dict) -> str:
    if not result["results"]:
        return (
            f"no matches for {result['query']!r} "
            f"({result['engine']} search)"
        )
    lines = [
        f"{len(result['results'])} match(es) for {result['query']!r} "
        f"({result['engine']} search):"
    ]
    for r in result["results"]:
        lines.append(
            f"  {r['relative']}  ({_human_size(r['size'])}, "
            f"text={r['sample_status']})"
        )
        if r["snippet"]:
            lines.append(f"    {r['snippet']}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #


def _refresh_before_query(conn, target: Path, db_path: Path) -> None:
    """Sync-on-read: reconcile the index with the filesystem before answering.

    A persistent index's worst failure mode is a confidently stale answer —
    a --search that misses yesterday's files still *looks* authoritative. An
    incremental refresh is just walk + stat for unchanged files, so queries
    pay seconds at most. Re-sampling honors the settings the index was built
    with (stored in meta). Reports to stderr only when something moved;
    stdout stays clean for --json consumers.
    """
    if not target.is_dir():
        print(
            f"warning: corpus root {target} not found; results may be stale "
            "(pass --stale to silence this)",
            file=sys.stderr,
        )
        return
    meta = _meta(conn)
    report = scan_into_index(
        conn, target, db_path,
        sample_words=int(meta.get("sample_words", DEFAULT_SAMPLE_WORDS)),
        sample_pages=int(meta.get("sample_pages", DEFAULT_SAMPLE_PAGES)),
    )
    moved = {
        k: report[k]
        for k in ("added", "changed", "restored", "newly_missing")
        if report[k]
    }
    if moved:
        rendered = ", ".join(f"{v:,} {k.replace('_', ' ')}" for k, v in moved.items())
        print(
            f"refreshed index before query: {rendered} "
            f"({report['elapsed_s']}s)",
            file=sys.stderr,
        )


def run(args):
    if args.stats and args.search is not None:
        err("--stats and --search are mutually exclusive")
    if args.stale and not (args.stats or args.search is not None):
        err("--stale only applies to --stats/--search (a plain scan always reads)")
    if args.limit <= 0:
        err("--limit must be > 0")
    if args.max_depth is not None and args.max_depth < 0:
        err("--max-depth must be >= 0")
    if args.max_files is not None and args.max_files <= 0:
        err("--max-files must be > 0")
    if args.sample_words <= 0:
        err("--sample-words must be > 0")
    if args.sample_pages <= 0:
        err("--sample-pages must be > 0")

    target = Path(args.target)
    db_path = Path(args.db) if args.db else default_db_path(target)
    read_only = args.stats or args.search is not None

    if not read_only and not target.is_dir():
        err(f"index target is not a directory: {target}")

    conn = open_index(db_path, target, create=not read_only)
    try:
        if read_only and not args.stale:
            _refresh_before_query(conn, target, db_path)
        if args.stats:
            stats = index_stats(conn, db_path)
            out = json.dumps(stats, indent=2, ensure_ascii=False) \
                if args.json else render_stats(stats)
        elif args.search is not None:
            result = search_index(conn, args.search, args.limit)
            out = json.dumps(result, indent=2, ensure_ascii=False) \
                if args.json else render_search(result)
        else:
            report = scan_into_index(
                conn,
                target,
                db_path,
                extensions=_normalize_extensions(args.ext),
                max_depth=args.max_depth,
                max_files=args.max_files,
                include_hidden=args.include_hidden,
                follow_symlinks=args.follow_symlinks,
                full=args.full,
                sample_words=args.sample_words,
                sample_pages=args.sample_pages,
            )
            out = json.dumps(report, indent=2, ensure_ascii=False) \
                if args.json else render_scan_report(report)
    finally:
        conn.close()

    print(out)
    return 0
