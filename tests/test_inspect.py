"""Tests for the ``inspect`` subcommand and shared inspection helpers.

Like ``probe`` tests, these never touch the network — inspect is local-only.
PDF fixtures are built on the fly with PyMuPDF so the suite has no external
file dependencies.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

# PyMuPDF is an optional dependency at runtime (the inspector falls back to
# a note when it's missing) but it's a hard requirement for these tests —
# without it we can't even build the fixtures.
fitz = pytest.importorskip("fitz")

from llamaparse_cli import _core, _inspect, _probe


# ---------------------------------------------------------------------------
# PDF fixture builders
# ---------------------------------------------------------------------------


def _make_text_pdf(path: Path, *, pages=2, text_per_page="Hello world. " * 100):
    """Create a PDF whose pages each contain extractable text."""
    doc = fitz.open()
    try:
        for _ in range(pages):
            page = doc.new_page()
            page.insert_text((72, 72), text_per_page, fontsize=11)
        doc.save(str(path))
    finally:
        doc.close()


def _make_scan_like_pdf(path: Path, *, pages=1):
    """Create a PDF whose pages have no extractable text (mimics a scan).

    A real scan is a wrapped JPEG with zero text layer; for the inspector
    heuristic what matters is that ``page.get_text()`` returns ~nothing, so
    empty pages are an adequate proxy.
    """
    doc = fitz.open()
    try:
        for _ in range(pages):
            doc.new_page()
        doc.save(str(path))
    finally:
        doc.close()


def _make_encrypted_pdf(path: Path, *, password="secret"):
    """Create a PDF protected by ``password``."""
    doc = fitz.open()
    try:
        page = doc.new_page()
        page.insert_text((72, 72), "encrypted body text", fontsize=11)
        doc.save(
            str(path),
            encryption=fitz.PDF_ENCRYPT_AES_256,
            owner_pw=password,
            user_pw=password,
        )
    finally:
        doc.close()


@pytest.fixture
def text_pdf(tmp_path: Path) -> Path:
    p = tmp_path / "text.pdf"
    _make_text_pdf(p, pages=2)
    return p


@pytest.fixture
def scan_pdf(tmp_path: Path) -> Path:
    p = tmp_path / "scan.pdf"
    _make_scan_like_pdf(p, pages=1)
    return p


@pytest.fixture
def encrypted_pdf(tmp_path: Path) -> Path:
    p = tmp_path / "encrypted.pdf"
    _make_encrypted_pdf(p)
    return p


@pytest.fixture
def mixed_tree(tmp_path: Path) -> Path:
    """A directory with one text PDF, one scan PDF, and a plain-text file."""
    base = tmp_path / "corpus"
    base.mkdir()
    _make_text_pdf(base / "text.pdf", pages=2)
    _make_scan_like_pdf(base / "scan.pdf", pages=1)
    (base / "notes.txt").write_text(
        "These are the notes. " * 50, encoding="utf-8"
    )
    (base / "raw.bin").write_bytes(b"\x00" * 50)
    return base


# ---------------------------------------------------------------------------
# _empty_inspection / _merge_inspection
# ---------------------------------------------------------------------------


class TestEmptyInspection:
    def test_shape_is_stable(self):
        empty = _inspect._empty_inspection()
        assert set(empty.keys()) == {
            "is_text",
            "is_scan",
            "page_count",
            "text_density",
            "has_form_fields",
            "is_encrypted",
            "snippet",
            "inspector_notes",
        }
        # Every value except the notes list starts as None.
        assert empty["inspector_notes"] == []
        for key, value in empty.items():
            if key != "inspector_notes":
                assert value is None


class TestMergeInspection:
    def test_overwrites_non_none(self):
        target = _inspect._empty_inspection()
        _inspect._merge_inspection(
            target,
            {"is_text": True, "page_count": 7, "inspector_notes": ["a note"]},
        )
        assert target["is_text"] is True
        assert target["page_count"] == 7
        assert target["inspector_notes"] == ["a note"]

    def test_does_not_clobber_with_none(self):
        target = _inspect._empty_inspection()
        target["is_text"] = True
        _inspect._merge_inspection(target, {"is_text": None})
        # None updates are treated as "no information" and shouldn't wipe
        # a value the inspector already set.
        assert target["is_text"] is True

    def test_appends_notes(self):
        target = _inspect._empty_inspection()
        target["inspector_notes"].append("first")
        _inspect._merge_inspection(target, {"inspector_notes": ["second"]})
        assert target["inspector_notes"] == ["first", "second"]


# ---------------------------------------------------------------------------
# inspect_pdf
# ---------------------------------------------------------------------------


class TestInspectPdf:
    def test_text_pdf_classified_as_text(self, text_pdf):
        result = _inspect.inspect_pdf(text_pdf)
        assert result["page_count"] == 2
        assert result["is_text"] is True
        assert result["is_scan"] is False
        assert result["is_encrypted"] is False
        # Heuristic: text PDF has plenty of chars per page.
        assert result["text_density"] > _inspect.SCAN_TEXT_DENSITY_THRESHOLD

    def test_scan_pdf_classified_as_scan(self, scan_pdf):
        result = _inspect.inspect_pdf(scan_pdf)
        assert result["page_count"] == 1
        assert result["is_text"] is False
        assert result["is_scan"] is True
        assert result["text_density"] < _inspect.SCAN_TEXT_DENSITY_THRESHOLD

    def test_encrypted_pdf_reports_encryption_and_skips_text(self, encrypted_pdf):
        result = _inspect.inspect_pdf(encrypted_pdf)
        assert result["is_encrypted"] is True
        assert result["is_text"] is False
        # We don't claim is_scan for an encrypted PDF — we just couldn't read it.
        assert result["is_scan"] is None
        assert result["text_density"] is None
        assert any("encrypted" in n.lower() for n in result["inspector_notes"])

    def test_snippet_extracts_text(self, text_pdf):
        result = _inspect.inspect_pdf(text_pdf, snippet_chars=40)
        assert result["snippet"] is not None
        assert len(result["snippet"]) <= 40
        assert "Hello" in result["snippet"]

    def test_snippet_off_by_default(self, text_pdf):
        result = _inspect.inspect_pdf(text_pdf)
        assert result["snippet"] is None

    def test_missing_pymupdf_returns_note(self, text_pdf, monkeypatch):
        # Force the lazy import to fail so we exercise the soft-dep branch.
        import builtins

        real_import = builtins.__import__

        def fake_import(name, *args, **kwargs):
            if name == "fitz":
                raise ImportError("simulated missing PyMuPDF")
            return real_import(name, *args, **kwargs)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        result = _inspect.inspect_pdf(text_pdf)
        assert result["inspector_notes"]
        assert "pymupdf" in result["inspector_notes"][0].lower()
        # Other fields should be absent (None / not set).
        assert "page_count" not in result or result["page_count"] is None

    def test_unreadable_pdf_returns_note(self, tmp_path: Path):
        broken = tmp_path / "broken.pdf"
        broken.write_bytes(b"this is not actually a pdf")
        result = _inspect.inspect_pdf(broken)
        assert result["inspector_notes"]
        assert any("could not open" in n.lower() for n in result["inspector_notes"])


# ---------------------------------------------------------------------------
# inspect_text
# ---------------------------------------------------------------------------


class TestInspectText:
    def test_basic_text_file(self, tmp_path: Path):
        p = tmp_path / "notes.txt"
        p.write_text("hello world", encoding="utf-8")
        result = _inspect.inspect_text(p)
        assert result["is_text"] is True
        assert result["is_scan"] is False
        assert result["snippet"] is None

    def test_snippet_truncates(self, tmp_path: Path):
        p = tmp_path / "notes.txt"
        p.write_text("abcdefghij" * 100, encoding="utf-8")
        result = _inspect.inspect_text(p, snippet_chars=15)
        assert result["snippet"] is not None
        assert len(result["snippet"]) <= 15
        assert result["snippet"].startswith("abc")

    def test_invalid_utf8_decodes_with_replacement(self, tmp_path: Path):
        p = tmp_path / "binary.txt"
        # Mix of valid UTF-8 and a stray continuation byte that would crash
        # a strict decode.
        p.write_bytes(b"start \xff\xfe end")
        result = _inspect.inspect_text(p, snippet_chars=50)
        assert result["snippet"] is not None
        assert "start" in result["snippet"]
        assert "end" in result["snippet"]


# ---------------------------------------------------------------------------
# inspect_file dispatch
# ---------------------------------------------------------------------------


class TestInspectFile:
    def test_pdf_routes_to_pdf_inspector(self, text_pdf):
        result = _inspect.inspect_file(text_pdf)
        assert result["page_count"] == 2
        assert result["is_text"] is True

    def test_txt_routes_to_text_inspector(self, tmp_path: Path):
        p = tmp_path / "x.txt"
        p.write_text("hi", encoding="utf-8")
        result = _inspect.inspect_file(p)
        assert result["is_text"] is True
        assert result["page_count"] is None

    def test_office_doc_gets_note_about_missing_inspector(self, tmp_path: Path):
        p = tmp_path / "x.docx"
        p.write_bytes(b"PK\x03\x04 fake docx")
        result = _inspect.inspect_file(p)
        assert result["inspector_notes"]
        assert any("no local inspector" in n for n in result["inspector_notes"])

    def test_unsupported_ext_gets_note(self, tmp_path: Path):
        p = tmp_path / "x.bin"
        p.write_bytes(b"\x00")
        result = _inspect.inspect_file(p)
        assert any("unsupported" in n for n in result["inspector_notes"])


# ---------------------------------------------------------------------------
# summarize
# ---------------------------------------------------------------------------


class TestSummarize:
    def test_counts_pdfs_by_kind(self):
        entries = [
            {
                "extension": ".pdf", "size": 100,
                "is_text": True, "is_scan": False,
                "is_encrypted": False, "has_form_fields": False,
                "page_count": 3,
            },
            {
                "extension": ".pdf", "size": 200,
                "is_text": False, "is_scan": True,
                "is_encrypted": False, "has_form_fields": False,
                "page_count": 1,
            },
            {
                "extension": ".pdf", "size": 50,
                "is_text": False, "is_scan": None,
                "is_encrypted": True, "has_form_fields": False,
                "page_count": 2,
            },
            {
                "extension": ".txt", "size": 20,
                "is_text": True,
            },
        ]
        summary = _inspect.summarize(entries)
        assert summary["total_files"] == 4
        assert summary["pdf_total"] == 3
        assert summary["pdf_text"] == 1
        assert summary["pdf_scans"] == 1
        assert summary["pdf_encrypted"] == 1
        assert summary["pdf_total_pages"] == 6
        assert summary["by_extension"][".pdf"]["count"] == 3
        assert summary["by_extension"][".txt"]["count"] == 1

    def test_truncation_sentinel_propagates(self):
        entries = [
            {"extension": ".pdf", "size": 10, "page_count": 1, "is_text": True},
            {"_truncated": True, "limit": 1},
        ]
        summary = _inspect.summarize(entries)
        assert summary["truncated"] is True
        assert summary["truncated_limit"] == 1
        assert summary["total_files"] == 1


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


class TestRendering:
    def test_render_table_includes_summary_and_kind(self, mixed_tree):
        rc = _core.main(["inspect", str(mixed_tree)])
        assert rc == 0  # End-to-end smoke check; table rendering exercised below.

    def test_render_table_direct(self, mixed_tree):
        entries = []
        for item in _probe.scan_directory(mixed_tree):
            if item.get("_truncated"):
                continue
            item.update(_inspect.inspect_file(Path(item["path"])))
            entries.append(item)
        summary = _inspect.summarize(entries)
        out = _inspect.render_table(entries, summary)
        assert "summary:" in out
        assert "text-pdf" in out  # text PDF kind
        assert "scan-pdf" in out  # scan PDF kind
        assert "PDFs" in out

    def test_render_json_round_trips(self, mixed_tree):
        entries = []
        for item in _probe.scan_directory(mixed_tree):
            if item.get("_truncated"):
                continue
            item.update(_inspect.inspect_file(Path(item["path"])))
            entries.append(item)
        summary = _inspect.summarize(entries)
        out = _inspect.render_json(entries, summary)
        decoded = json.loads(out)
        assert "files" in decoded and "summary" in decoded
        assert decoded["summary"]["total_files"] == len(entries)
        # All inspect fields should round-trip.
        a_pdf = next(f for f in decoded["files"] if f["extension"] == ".pdf")
        assert "is_scan" in a_pdf
        assert "is_text" in a_pdf

    def test_render_table_handles_empty_match(self):
        out = _inspect.render_table([], _inspect.summarize([]))
        assert "no files matched" in out

    def test_render_table_shows_snippets_when_present(self, mixed_tree):
        """Snippets must surface in human-table mode, not just JSON.

        Before the fix, `--snippet N` (without `--json`) silently extracted
        text but never displayed it because the table row dropped the field.
        Regression guard for the Codex P2 review on PR #6.
        """
        entries = []
        for item in _probe.scan_directory(mixed_tree):
            if item.get("_truncated"):
                continue
            item.update(_inspect.inspect_file(Path(item["path"]), snippet_chars=60))
            entries.append(item)
        summary = _inspect.summarize(entries)
        out = _inspect.render_table(entries, summary)
        # Continuation-line marker plus the actual snippet content.
        assert "> " in out
        # The text PDF contains "Hello world." in its body; the notes.txt
        # fixture contains "These are the notes."
        assert "Hello world" in out or "These are the notes" in out

    def test_render_table_omits_continuation_when_no_snippet(self, mixed_tree):
        """No `> ` continuation lines when the user didn't ask for snippets."""
        entries = []
        for item in _probe.scan_directory(mixed_tree):
            if item.get("_truncated"):
                continue
            item.update(_inspect.inspect_file(Path(item["path"])))  # snippet_chars=0
            entries.append(item)
        summary = _inspect.summarize(entries)
        out = _inspect.render_table(entries, summary)
        # Every line should be either header/divider/row/summary — never a
        # bare `    > ` snippet continuation.
        for line in out.splitlines():
            assert not line.startswith("    > ")


# ---------------------------------------------------------------------------
# End-to-end: `llamaparse inspect ...` through _core.main
# ---------------------------------------------------------------------------


class TestInspectCommand:
    def test_inspect_in_subcommands_tuple(self):
        assert "inspect" in _core.SUBCOMMANDS

    def test_inspect_appears_in_help(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["--help"])
        assert exc_info.value.code == 0
        out = capsys.readouterr().out
        assert "inspect" in out

    def test_inspect_basic_run(self, capsys, mixed_tree):
        rc = _core.main(["inspect", str(mixed_tree)])
        assert rc == 0
        out = capsys.readouterr().out
        assert "summary:" in out
        assert "text.pdf" in out

    def test_inspect_json_run(self, capsys, mixed_tree):
        rc = _core.main(["inspect", str(mixed_tree), "--json"])
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        assert decoded["summary"]["total_files"] >= 3
        names = {f["name"] for f in decoded["files"]}
        assert "text.pdf" in names
        assert "scan.pdf" in names
        assert "notes.txt" in names

    def test_inspect_ext_filter(self, capsys, mixed_tree):
        rc = _core.main(
            ["inspect", str(mixed_tree), "--ext", "pdf", "--json"]
        )
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        for entry in decoded["files"]:
            assert entry["extension"] == ".pdf"

    def test_inspect_supported_only(self, capsys, mixed_tree):
        rc = _core.main(
            ["inspect", str(mixed_tree), "--supported-only", "--json"]
        )
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        # raw.bin should be excluded.
        names = {f["name"] for f in decoded["files"]}
        assert "raw.bin" not in names

    def test_inspect_snippet_flag(self, capsys, mixed_tree):
        rc = _core.main(
            ["inspect", str(mixed_tree), "--snippet", "50", "--json"]
        )
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        text_pdf = next(f for f in decoded["files"] if f["name"] == "text.pdf")
        notes_txt = next(f for f in decoded["files"] if f["name"] == "notes.txt")
        # Both should now carry snippets.
        assert text_pdf["snippet"] is not None
        assert notes_txt["snippet"] is not None
        assert len(text_pdf["snippet"]) <= 50
        assert len(notes_txt["snippet"]) <= 50

    def test_inspect_snippet_visible_in_table_mode(self, capsys, mixed_tree):
        """Without `--json`, the snippet must still be visible.

        Regression guard: previously `inspect ... --snippet N` (table mode)
        extracted snippets but the table renderer dropped the field, so the
        feature appeared to do nothing from the user's POV.
        """
        rc = _core.main(["inspect", str(mixed_tree), "--snippet", "60"])
        assert rc == 0
        out = capsys.readouterr().out
        # Continuation-line marker introduced for snippet rendering.
        assert "> " in out
        # Content from one of the fixtures should appear in the snippet line.
        assert "Hello world" in out or "These are the notes" in out

    def test_inspect_single_file(self, capsys, text_pdf):
        rc = _core.main(["inspect", str(text_pdf), "--json"])
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        assert len(decoded["files"]) == 1
        entry = decoded["files"][0]
        assert entry["name"] == "text.pdf"
        assert entry["is_text"] is True
        assert entry["page_count"] == 2

    def test_inspect_writes_output_file(self, tmp_path: Path, mixed_tree, capsys):
        out_file = tmp_path / "report.txt"
        rc = _core.main(
            ["inspect", str(mixed_tree), "--output", str(out_file)]
        )
        assert rc == 0
        assert out_file.exists()
        assert "summary:" in out_file.read_text(encoding="utf-8")

    def test_inspect_missing_target_exits_nonzero(self, capsys, tmp_path: Path):
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["inspect", str(tmp_path / "nope")])
        assert exc_info.value.code == 2

    def test_inspect_negative_snippet_rejected(self, capsys, mixed_tree):
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["inspect", str(mixed_tree), "--snippet", "-1"])
        assert exc_info.value.code == 2

    def test_inspect_single_file_ext_filter_consistent(self, capsys, mixed_tree):
        """Matches the probe regression: a single-file target must respect --ext."""
        rc = _core.main([
            "inspect", str(mixed_tree / "notes.txt"),
            "--ext", "pdf", "--json",
        ])
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        assert decoded["files"] == []


# ---------------------------------------------------------------------------
# Network safety
# ---------------------------------------------------------------------------


class TestNoNetwork:
    def test_inspect_does_not_require_api_key(self, capsys, monkeypatch, mixed_tree):
        """If inspect tried to call LlamaCloud, removing the API key would
        either trigger a `require_api_key()` exit or fail to authenticate.
        A clean rc == 0 confirms inspect stays local-only.
        """
        monkeypatch.delenv("LLAMA_CLOUD_API_KEY", raising=False)
        rc = _core.main(["inspect", str(mixed_tree)])
        assert rc == 0

    def test_inspect_does_not_import_requests(self, monkeypatch, mixed_tree):
        """Inspect should never hit the requests module — it has no reason
        to. We catch any accidental future regression by making the import
        loudly fail.
        """
        import builtins

        real_import = builtins.__import__

        def fake_import(name, *args, **kwargs):
            if name == "requests" or name.startswith("requests."):
                raise AssertionError(
                    "inspect imported requests; it must stay local-only"
                )
            return real_import(name, *args, **kwargs)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        rc = _core.main(["inspect", str(mixed_tree), "--json"])
        assert rc == 0
