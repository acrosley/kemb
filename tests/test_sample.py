"""Tests for ``probe --sample`` and the local text extractors.

All checks are local-only — sampling never makes a network call.
"""
from __future__ import annotations

import json
import zipfile
from pathlib import Path

import pytest

from llamaparse_cli import _core, _probe, _sample


# ---------------------------------------------------------------------------
# Fixture documents
# ---------------------------------------------------------------------------


def _make_text_pdf(path: Path, text: str, pages: int = 1) -> None:
    """Write a minimal PDF with a real text layer using pypdf."""
    from pypdf import PdfWriter
    from pypdf.generic import (
        ArrayObject,
        DictionaryObject,
        NameObject,
        StreamObject,
    )

    writer = PdfWriter()
    for _ in range(pages):
        page = writer.add_blank_page(width=612, height=792)
        content = StreamObject()
        content.set_data(
            f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET".encode("latin-1")
        )
        content_ref = writer._add_object(content)
        page[NameObject("/Contents")] = content_ref
        font = DictionaryObject({
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject("/Helvetica"),
        })
        font_ref = writer._add_object(font)
        page[NameObject("/Resources")] = DictionaryObject({
            NameObject("/Font"): DictionaryObject({NameObject("/F1"): font_ref}),
            NameObject("/ProcSet"): ArrayObject(
                [NameObject("/PDF"), NameObject("/Text")]
            ),
        })
    with open(path, "wb") as fh:
        writer.write(fh)


def _make_blank_pdf(path: Path, pages: int = 2) -> None:
    """Write a PDF with no text layer at all (stand-in for a scan)."""
    from pypdf import PdfWriter

    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=612, height=792)
    with open(path, "wb") as fh:
        writer.write(fh)


def _make_docx(path: Path, text: str) -> None:
    """Write a minimal .docx (zip with word/document.xml)."""
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        "<w:document><w:body><w:p><w:r><w:t>"
        f"{text}"
        "</w:t></w:r></w:p></w:body></w:document>"
    )
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("word/document.xml", document)


# ---------------------------------------------------------------------------
# sample_file extractors
# ---------------------------------------------------------------------------


class TestSampleFile:
    def test_plain_text(self, tmp_path: Path):
        p = tmp_path / "notes.txt"
        p.write_text("alpha beta gamma delta")
        result = _sample.sample_file(p, ".txt", max_words=3)
        assert result["status"] == _sample.STATUS_OK
        assert result["text"] == "alpha beta gamma"
        assert result["words"] == 3
        assert result["pages"] is None

    def test_empty_text_file_reports_no_text(self, tmp_path: Path):
        p = tmp_path / "empty.txt"
        p.write_text("")
        result = _sample.sample_file(p, ".txt")
        assert result["status"] == _sample.STATUS_NO_TEXT

    def test_html_tags_stripped(self, tmp_path: Path):
        p = tmp_path / "page.html"
        p.write_text(
            "<html><head><style>body{color:red}</style></head>"
            "<body><h1>Quarterly Report</h1><p>Revenue rose.</p></body></html>"
        )
        result = _sample.sample_file(p, ".html")
        assert result["status"] == _sample.STATUS_OK
        assert "Quarterly Report Revenue rose." in result["text"]
        assert "color:red" not in result["text"]

    def test_docx_body_extracted(self, tmp_path: Path):
        p = tmp_path / "memo.docx"
        _make_docx(p, "Settlement terms attached for review")
        result = _sample.sample_file(p, ".docx")
        assert result["status"] == _sample.STATUS_OK
        assert "Settlement terms attached" in result["text"]

    def test_corrupt_docx_reports_error(self, tmp_path: Path):
        p = tmp_path / "broken.docx"
        p.write_bytes(b"not a zip archive")
        result = _sample.sample_file(p, ".docx")
        assert result["status"] == _sample.STATUS_ERROR

    def test_pdf_with_text_layer(self, tmp_path: Path):
        p = tmp_path / "complaint.pdf"
        _make_text_pdf(p, "Plaintiff alleges breach of contract", pages=2)
        result = _sample.sample_file(p, ".pdf")
        assert result["status"] == _sample.STATUS_OK
        assert "Plaintiff alleges breach" in result["text"]
        assert result["pages"] == 2

    def test_blank_pdf_flagged_as_scan(self, tmp_path: Path):
        p = tmp_path / "scan.pdf"
        _make_blank_pdf(p, pages=3)
        result = _sample.sample_file(p, ".pdf")
        assert result["status"] == _sample.STATUS_NO_TEXT
        assert result["pages"] == 3
        assert "scan" in result["detail"]

    def test_pdf_respects_word_cap(self, tmp_path: Path):
        p = tmp_path / "long.pdf"
        _make_text_pdf(p, "word " * 50, pages=1)
        result = _sample.sample_file(p, ".pdf", max_words=10)
        assert result["words"] == 10

    def test_unknown_format_unsupported(self, tmp_path: Path):
        p = tmp_path / "photo.png"
        p.write_bytes(b"\x89PNG\r\n")
        result = _sample.sample_file(p, ".png")
        assert result["status"] == _sample.STATUS_UNSUPPORTED


# ---------------------------------------------------------------------------
# attach_samples (budget + stats)
# ---------------------------------------------------------------------------


def _scan_entries(target):
    return [
        item
        for item in _probe.scan_directory(target)
        if not item.get("_truncated") and not item.get("_walk_error")
    ]


class TestAttachSamples:
    def test_budget_exhaustion_keeps_inventory(self, tmp_path: Path):
        for i in range(3):
            (tmp_path / f"doc{i}.txt").write_text("one two three four five")
        entries = _scan_entries(tmp_path)
        stats = _probe.attach_samples(
            entries, max_words=5, pdf_pages=3, budget=7
        )
        statuses = [e["sample_status"] for e in entries]
        # First file takes 5 words, second is capped at the 2 remaining,
        # third gets no budget — but all three stay in the inventory.
        assert statuses == ["ok", "ok", _sample.STATUS_SKIPPED]
        assert entries[1]["sample_words"] == 2
        assert stats["total_words"] == 7
        assert stats["by_status"]["ok"] == 2

    def test_no_text_pdfs_collected(self, tmp_path: Path):
        _make_blank_pdf(tmp_path / "scan.pdf")
        entries = _scan_entries(tmp_path)
        stats = _probe.attach_samples(
            entries, max_words=50, pdf_pages=3, budget=1000
        )
        assert stats["no_text_files"] == ["scan.pdf"]


# ---------------------------------------------------------------------------
# CLI: probe --sample end to end
# ---------------------------------------------------------------------------


class TestProbeSampleCli:
    def _corpus(self, tmp_path: Path) -> Path:
        root = tmp_path / "cases"
        (root / "smith").mkdir(parents=True)
        (root / "jones").mkdir(parents=True)
        _make_text_pdf(root / "smith" / "complaint.pdf", "Plaintiff alleges fraud")
        _make_blank_pdf(root / "smith" / "exhibit.pdf")
        (root / "jones" / "notes.txt").write_text("Deposition scheduled for May")
        return root

    def test_sample_output_format(self, tmp_path: Path, capsys):
        root = self._corpus(tmp_path)
        rc = _core.main(["probe", str(root), "--sample"])
        assert rc == 0
        out = capsys.readouterr().out
        assert out.count("===document===") == 3
        assert "===document=== smith/complaint.pdf" in out
        assert "Plaintiff alleges fraud" in out
        assert "Deposition scheduled for May" in out
        # The scan is flagged inline and in the header roll-up.
        assert "no text layer" in out
        assert "route to an OCR-capable parse tier" in out
        # Per-document metadata line is present.
        assert "1 pages" in out
        assert "text: ok" in out

    def test_sample_json_includes_fields(self, tmp_path: Path, capsys):
        root = self._corpus(tmp_path)
        rc = _core.main(["probe", str(root), "--sample", "--json"])
        assert rc == 0
        report = json.loads(capsys.readouterr().out)
        by_name = {f["name"]: f for f in report["files"]}
        assert by_name["complaint.pdf"]["sample_status"] == "ok"
        assert by_name["complaint.pdf"]["pages"] == 1
        assert "fraud" in by_name["complaint.pdf"]["sample"]
        assert by_name["exhibit.pdf"]["sample_status"] == "no-text"

    def test_sample_writes_output_file(self, tmp_path: Path, capsys):
        root = self._corpus(tmp_path)
        out_file = tmp_path / "corpus_sample.txt"
        rc = _core.main(
            ["probe", str(root), "--sample", "--output", str(out_file)]
        )
        assert rc == 0
        assert out_file.exists()
        assert "===document===" in out_file.read_text()

    def test_plain_probe_has_no_sample_fields(self, tmp_path: Path, capsys):
        root = self._corpus(tmp_path)
        rc = _core.main(["probe", str(root), "--json"])
        assert rc == 0
        report = json.loads(capsys.readouterr().out)
        assert "sample" not in report["files"][0]

    @pytest.mark.parametrize(
        "flag,value",
        [("--sample-words", "50"), ("--sample-pages", "1"), ("--sample-budget", "10")],
    )
    def test_sample_flags_require_sample(self, tmp_path: Path, flag, value):
        root = self._corpus(tmp_path)
        with pytest.raises(SystemExit) as exc:
            _core.main(["probe", str(root), flag, value])
        assert exc.value.code == 2

    def test_sample_words_flag_caps_text(self, tmp_path: Path, capsys):
        root = tmp_path / "docs"
        root.mkdir()
        (root / "long.txt").write_text("w1 w2 w3 w4 w5 w6 w7 w8")
        rc = _core.main(
            ["probe", str(root), "--sample", "--sample-words", "4"]
        )
        assert rc == 0
        out = capsys.readouterr().out
        assert "w1 w2 w3 w4" in out
        assert "w5" not in out
