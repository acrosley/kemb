"""End-to-end spine tests: CIR roundtrip, deterministic render, idempotent ingest."""
from __future__ import annotations

import io
import json
import sqlite3
from pathlib import Path

import pytest
from click.testing import CliRunner
from pypdf import PdfWriter

from doc_backbone import db as db_mod
from doc_backbone import render as render_mod
from doc_backbone.cir import CIR, Block, BlockKind
from doc_backbone.cli import main as cli_main


def _make_pdf(path: Path, pages: int = 2) -> None:
    """pypdf can't author a content-bearing PDF from scratch, but a blank
    multi-page PDF is enough to exercise the pipeline (zero text blocks)."""
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=612, height=792)
    with path.open("wb") as f:
        writer.write(f)


def _sample_cir() -> CIR:
    return CIR(
        source_hash="a" * 64,
        source_path="sample.pdf",
        doc_type="unknown",
        pages=2,
        extractor="native_pdf",
        extractor_version="0.1.0",
        blocks=[
            Block(kind=BlockKind.HEADING, page=1, text="Title", level=1,
                  source_extractor="native_pdf"),
            Block(kind=BlockKind.PARAGRAPH, page=1, text="Hello world.",
                  source_extractor="native_pdf"),
            Block(kind=BlockKind.PAGE_BREAK, page=1, source_extractor="native_pdf"),
            Block(kind=BlockKind.PARAGRAPH, page=2, text="Second page.",
                  source_extractor="native_pdf"),
        ],
        metadata={"text_blocks": 3},
    )


def test_cir_roundtrip():
    cir = _sample_cir()
    blob = json.dumps(cir.to_dict(), sort_keys=True)
    restored = CIR.from_dict(json.loads(blob))
    assert restored.to_dict() == cir.to_dict()
    assert restored.blocks[0].kind is BlockKind.HEADING
    assert restored.blocks[0].level == 1


def test_render_is_deterministic():
    cir = _sample_cir()
    a = render_mod.render(cir, parsed_utc="2026-01-01T00:00:00+00:00")
    b = render_mod.render(cir, parsed_utc="2026-01-01T00:00:00+00:00")
    assert a == b
    assert "## Page 1" in a and "## Page 2" in a
    assert "source_hash: " + ("a" * 64) in a


def test_ingest_is_idempotent(tmp_path: Path):
    backbone_root = tmp_path / "backbone"
    (backbone_root / "config").mkdir(parents=True)
    (backbone_root / "config" / "doc_types.yaml").write_text(
        "default_doc_type: unknown\n"
        "doc_types:\n"
        "  unknown:\n"
        "    extractors:\n"
        "      - native_pdf\n",
        encoding="utf-8",
    )
    pdf = tmp_path / "sample.pdf"
    _make_pdf(pdf, pages=2)

    runner = CliRunner()
    first = runner.invoke(cli_main, ["ingest", str(pdf), "--root", str(backbone_root)])
    assert first.exit_code == 0, first.output
    assert "parse  " in first.output

    conn = db_mod.connect(backbone_root / "corpus.db")
    row = conn.execute("SELECT cir_path, md_path FROM parses").fetchone()
    assert row is not None
    md_first = Path(row["md_path"]).read_bytes()
    cir_first = Path(row["cir_path"]).read_bytes()

    second = runner.invoke(cli_main, ["ingest", str(pdf), "--root", str(backbone_root)])
    assert second.exit_code == 0, second.output
    assert "skip   " in second.output

    md_second = Path(row["md_path"]).read_bytes()
    cir_second = Path(row["cir_path"]).read_bytes()
    assert md_first == md_second
    assert cir_first == cir_second
