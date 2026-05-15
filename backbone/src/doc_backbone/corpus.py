"""L0 - Corpus index.

Walks a PDF tree, content-hashes each file, and registers it in corpus.db.
This is the "what exists" layer; everything downstream keys off the sha256.
"""
from __future__ import annotations

import hashlib
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

_CHUNK = 1 << 20  # 1 MiB


@dataclass(slots=True)
class CorpusEntry:
    hash: str
    path: str  # relative to corpus root
    size_bytes: int


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(_CHUNK):
            h.update(chunk)
    return h.hexdigest()


def iter_pdfs(root: Path) -> Iterator[Path]:
    """Yield every .pdf under root (or just root itself if it's a file)."""
    if root.is_file():
        if root.suffix.lower() == ".pdf":
            yield root
        return
    yield from (p for p in root.rglob("*.pdf") if p.is_file())


def register(conn: sqlite3.Connection, pdf_path: Path, corpus_root: Path) -> CorpusEntry:
    """Hash + upsert a single PDF into the documents table. Idempotent."""
    digest = sha256_file(pdf_path)
    size = pdf_path.stat().st_size
    try:
        rel = pdf_path.resolve().relative_to(corpus_root.resolve()).as_posix()
    except ValueError:
        rel = pdf_path.as_posix()
    now = _utcnow_iso()

    cur = conn.execute("SELECT hash FROM documents WHERE hash = ?", (digest,))
    if cur.fetchone() is None:
        conn.execute(
            "INSERT INTO documents (hash, path, size_bytes, first_seen_utc, last_seen_utc) "
            "VALUES (?, ?, ?, ?, ?)",
            (digest, rel, size, now, now),
        )
    else:
        conn.execute(
            "UPDATE documents SET path = ?, size_bytes = ?, last_seen_utc = ? WHERE hash = ?",
            (rel, size, now, digest),
        )
    conn.commit()
    return CorpusEntry(hash=digest, path=rel, size_bytes=size)


def scan(conn: sqlite3.Connection, root: Path) -> list[CorpusEntry]:
    """Register every PDF under root. Returns the entries seen."""
    return [register(conn, p, root) for p in iter_pdfs(root)]
