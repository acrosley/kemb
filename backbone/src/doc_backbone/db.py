"""SQLite-backed state for the backbone: corpus.db schema + connection helper."""
from __future__ import annotations

import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
    hash TEXT PRIMARY KEY,
    path TEXT NOT NULL,
    size_bytes INTEGER NOT NULL,
    pages INTEGER,
    doc_type TEXT,
    first_seen_utc TEXT NOT NULL,
    last_seen_utc TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS parses (
    hash TEXT NOT NULL,
    extractor TEXT NOT NULL,
    extractor_version TEXT NOT NULL,
    cir_path TEXT NOT NULL,
    md_path TEXT,
    quality_score REAL,
    parsed_utc TEXT NOT NULL,
    PRIMARY KEY (hash, extractor)
);

CREATE TABLE IF NOT EXISTS mirror_state (
    hash TEXT PRIMARY KEY,
    md_path TEXT NOT NULL,
    rendered_utc TEXT NOT NULL,
    cir_hash TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_documents_doc_type ON documents(doc_type);
CREATE INDEX IF NOT EXISTS idx_parses_hash ON parses(hash);
"""


def connect(db_path: Path) -> sqlite3.Connection:
    """Open corpus.db, ensuring schema + WAL mode."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript(SCHEMA)
    conn.commit()
    return conn
