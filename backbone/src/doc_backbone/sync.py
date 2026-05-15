"""L6 - Mirror reconciliation.

Partial in v0: only the immediate post-extract write into mirror/ is wired
up here. A full sync (detect drift between corpus.db and disk, garbage-
collect orphaned cache entries, re-render on renderer changes) is left as
a stub.

The cache layout is content-addressed:
    backbone/cache/<ab>/<cdef...>/cir.json
    backbone/cache/<ab>/<cdef...>/doc.md
The mirror is a flat (or doc-type-bucketed) view of the same docs, named
for human navigation.
"""
from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path


def cache_dir(backbone_root: Path, source_hash: str) -> Path:
    return backbone_root / "cache" / source_hash[:2] / source_hash[2:]


def mirror_path(backbone_root: Path, source_hash: str, doc_type: str, source_path: str) -> Path:
    """Where the rendered markdown should live in the mirror tree."""
    stem = Path(source_path).stem.replace(" ", "_")
    safe_stem = "".join(c for c in stem if c.isalnum() or c in "-_.")[:80] or "doc"
    fname = f"{source_hash[:8]}__{safe_stem}.md"
    return backbone_root / "mirror" / doc_type / fname


def publish_to_mirror(cache_md: Path, mirror_md: Path) -> None:
    """Copy the cache's rendered markdown into the mirror. Copy (not symlink)
    so the mirror survives moves and works without admin on Windows."""
    mirror_md.parent.mkdir(parents=True, exist_ok=True)
    if mirror_md.exists():
        if mirror_md.read_bytes() == cache_md.read_bytes():
            return
    shutil.copy2(cache_md, mirror_md)


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def full_reconcile(backbone_root: Path) -> None:
    """Walk corpus.db, regenerate any markdown whose cir_hash drifted, GC
    orphan cache entries. Stub for v0."""
    raise NotImplementedError("Layer 6 (full reconcile): not implemented in v0 spine")
