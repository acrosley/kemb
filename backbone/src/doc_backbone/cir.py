"""Canonical Intermediate Representation.

The load-bearing abstraction of the backbone: every extractor (present and
future) emits a CIR; the renderer and downstream layers only ever see this
shape. Adding a new extractor is a one-file change as long as it produces a
valid CIR.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from typing import Any


class BlockKind(StrEnum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LIST = "list"
    TABLE = "table"
    FIGURE = "figure"
    FOOTNOTE = "footnote"
    PAGE_BREAK = "page_break"


@dataclass(slots=True)
class Block:
    """One logical unit of extracted content, tagged with provenance."""

    kind: BlockKind
    page: int
    text: str | None = None
    level: int | None = None
    table: list[list[str]] | None = None
    bbox: tuple[float, float, float, float] | None = None
    confidence: float = 1.0
    source_extractor: str = ""

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["kind"] = self.kind.value
        if self.bbox is not None:
            d["bbox"] = list(self.bbox)
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Block:
        bbox = d.get("bbox")
        return cls(
            kind=BlockKind(d["kind"]),
            page=int(d["page"]),
            text=d.get("text"),
            level=d.get("level"),
            table=d.get("table"),
            bbox=tuple(bbox) if bbox is not None else None,
            confidence=float(d.get("confidence", 1.0)),
            source_extractor=d.get("source_extractor", ""),
        )


@dataclass(slots=True)
class CIR:
    """A document's parsed content in canonical form."""

    source_hash: str
    source_path: str
    doc_type: str
    pages: int
    extractor: str
    extractor_version: str
    blocks: list[Block] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_hash": self.source_hash,
            "source_path": self.source_path,
            "doc_type": self.doc_type,
            "pages": self.pages,
            "extractor": self.extractor,
            "extractor_version": self.extractor_version,
            "blocks": [b.to_dict() for b in self.blocks],
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> CIR:
        return cls(
            source_hash=d["source_hash"],
            source_path=d["source_path"],
            doc_type=d["doc_type"],
            pages=int(d["pages"]),
            extractor=d["extractor"],
            extractor_version=d["extractor_version"],
            blocks=[Block.from_dict(b) for b in d.get("blocks", [])],
            metadata=dict(d.get("metadata", {})),
        )
