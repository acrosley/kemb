"""Native-text extractor: pypdf, no OCR. The cheapest tier of L3.

Suitable for digitally-generated PDFs (court filings, expert reports, CVs).
Will produce empty / sparse output on scans; the L4 arbiter is responsible
for escalating to an OCR tier when that happens (not yet wired in v0).
"""
from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader

from doc_backbone.cir import CIR, Block, BlockKind
from doc_backbone.extractors.base import Extractor

_PARAGRAPH_SPLIT = re.compile(r"\n\s*\n+")
_WS = re.compile(r"[ \t]+")


def _clean(text: str) -> str:
    text = _WS.sub(" ", text)
    return text.strip()


def _paragraphs(page_text: str) -> list[str]:
    if not page_text:
        return []
    parts = (_clean(p) for p in _PARAGRAPH_SPLIT.split(page_text))
    return [p for p in parts if p]


class NativePdfExtractor(Extractor):
    name = "native_pdf"
    version = "0.1.0"

    def extract(self, pdf_path: Path, *, source_hash: str, doc_type: str) -> CIR:
        reader = PdfReader(str(pdf_path))
        blocks: list[Block] = []
        for i, page in enumerate(reader.pages, start=1):
            try:
                raw = page.extract_text() or ""
            except Exception:
                raw = ""
            for para in _paragraphs(raw):
                blocks.append(
                    Block(
                        kind=BlockKind.PARAGRAPH,
                        page=i,
                        text=para,
                        source_extractor=self.name,
                    )
                )
            if i < len(reader.pages):
                blocks.append(
                    Block(kind=BlockKind.PAGE_BREAK, page=i, source_extractor=self.name)
                )
        return CIR(
            source_hash=source_hash,
            source_path=pdf_path.as_posix(),
            doc_type=doc_type,
            pages=len(reader.pages),
            extractor=self.name,
            extractor_version=self.version,
            blocks=blocks,
            metadata={"text_blocks": sum(1 for b in blocks if b.kind == BlockKind.PARAGRAPH)},
        )
