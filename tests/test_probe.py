"""Tests for the ``probe`` subcommand and shared scanning helpers.

All checks are local-only — probe never makes a network call.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from llamaparse_cli import _core, _probe


# ---------------------------------------------------------------------------
# _normalize_extensions / _human_size
# ---------------------------------------------------------------------------


class TestNormalizeExtensions:
    def test_none_returns_none(self):
        assert _probe._normalize_extensions(None) is None

    def test_empty_string_returns_none(self):
        assert _probe._normalize_extensions("") is None

    def test_adds_leading_dot(self):
        assert _probe._normalize_extensions("pdf") == {".pdf"}

    def test_lowercases(self):
        assert _probe._normalize_extensions("PDF,DocX") == {".pdf", ".docx"}

    def test_handles_dots_and_whitespace(self):
        assert _probe._normalize_extensions(" .pdf , docx ") == {".pdf", ".docx"}


class TestHumanSize:
    def test_bytes(self):
        assert _probe._human_size(512) == "512 B"

    def test_kilobytes(self):
        assert _probe._human_size(2048) == "2.0 KB"

    def test_megabytes(self):
        assert _probe._human_size(5 * 1024 * 1024) == "5.0 MB"

    def test_gigabytes(self):
        assert _probe._human_size(3 * 1024 ** 3) == "3.0 GB"


class TestIsHidden:
    def test_dotfile_detected_by_name(self):
        assert _probe._is_hidden(".rc") is True

    def test_normal_name_is_not_hidden(self):
        assert _probe._is_hidden("README.md") is False

    def test_dotfile_path_detected(self, tmp_path: Path):
        p = tmp_path / ".dotfile"
        p.write_text("x")
        assert _probe._is_hidden(p) is True

    def test_normal_path_not_hidden(self, tmp_path: Path):
        p = tmp_path / "plain.txt"
        p.write_text("x")
        assert _probe._is_hidden(p) is False

    @pytest.mark.skipif(os.name != "nt", reason="Windows-only attribute check")
    def test_windows_hidden_attribute_detected(self, tmp_path: Path):
        # Files marked hidden via the NTFS attribute (Thumbs.db, desktop.ini,
        # `attrib +h foo`) have no leading dot but should still be skipped.
        p = tmp_path / "secret.txt"
        p.write_text("x")
        subprocess.run(["attrib", "+h", str(p)], check=True)
        assert _probe._is_hidden(p) is True

    @pytest.mark.skipif(os.name != "nt", reason="Windows-only attribute check")
    def test_windows_hidden_file_excluded_from_scan(self, tmp_path: Path):
        # End-to-end: a Windows-hidden file should not appear in scan output.
        (tmp_path / "visible.txt").write_text("v")
        hidden = tmp_path / "Thumbs.db"
        hidden.write_text("h")
        subprocess.run(["attrib", "+h", str(hidden)], check=True)

        items = [
            e for e in _probe.scan_directory(tmp_path)
            if not e.get("_truncated") and not e.get("_walk_error")
        ]
        names = sorted(e["name"] for e in items)
        assert names == ["visible.txt"]


# ---------------------------------------------------------------------------
# scan_directory
# ---------------------------------------------------------------------------


@pytest.fixture
def sample_tree(tmp_path: Path) -> Path:
    """Build a small directory tree for scan tests.

    sample/
      a.pdf
      b.docx
      notes.txt
      raw.bin                 <- unsupported extension
      .hidden.md              <- hidden file
      .secret/                <- hidden directory
        skip.pdf
      sub/
        c.pdf
        deeper/
          d.png
    """
    base = tmp_path / "sample"
    base.mkdir()
    (base / "a.pdf").write_bytes(b"%PDF-1.4 " + b"x" * 100)
    (base / "b.docx").write_bytes(b"PK\x03\x04" + b"y" * 200)
    (base / "notes.txt").write_text("hello world", encoding="utf-8")
    (base / "raw.bin").write_bytes(b"\x00" * 50)
    (base / ".hidden.md").write_text("secret notes", encoding="utf-8")

    secret = base / ".secret"
    secret.mkdir()
    (secret / "skip.pdf").write_bytes(b"%PDF-hidden")

    sub = base / "sub"
    sub.mkdir()
    (sub / "c.pdf").write_bytes(b"%PDF-1.4 sub")

    deeper = sub / "deeper"
    deeper.mkdir()
    (deeper / "d.png").write_bytes(b"\x89PNG\r\n\x1a\n")

    return base


class TestScanDirectory:
    def test_visible_files_collected(self, sample_tree):
        items = [e for e in _probe.scan_directory(sample_tree) if not e.get("_truncated")]
        names = sorted(e["name"] for e in items)
        # Hidden files and hidden directory contents are skipped by default.
        assert names == ["a.pdf", "b.docx", "c.pdf", "d.png", "notes.txt", "raw.bin"]

    def test_extension_filter(self, sample_tree):
        items = [
            e for e in _probe.scan_directory(sample_tree, extensions={".pdf"})
            if not e.get("_truncated")
        ]
        names = sorted(e["name"] for e in items)
        assert names == ["a.pdf", "c.pdf"]

    def test_max_depth_zero_keeps_top_level_only(self, sample_tree):
        items = [
            e for e in _probe.scan_directory(sample_tree, max_depth=0)
            if not e.get("_truncated")
        ]
        names = sorted(e["name"] for e in items)
        # Top-level only (no sub/, no sub/deeper/).
        assert names == ["a.pdf", "b.docx", "notes.txt", "raw.bin"]

    def test_max_depth_one_includes_first_subdir(self, sample_tree):
        items = [
            e for e in _probe.scan_directory(sample_tree, max_depth=1)
            if not e.get("_truncated")
        ]
        names = sorted(e["name"] for e in items)
        # Includes sub/c.pdf but not sub/deeper/d.png.
        assert "c.pdf" in names
        assert "d.png" not in names

    def test_include_hidden_picks_up_hidden_files_and_dirs(self, sample_tree):
        items = [
            e for e in _probe.scan_directory(sample_tree, include_hidden=True)
            if not e.get("_truncated")
        ]
        names = sorted(e["name"] for e in items)
        assert ".hidden.md" in names
        assert "skip.pdf" in names

    def test_supported_only_filters_unsupported_extensions(self, sample_tree):
        items = [
            e for e in _probe.scan_directory(sample_tree, supported_only=True)
            if not e.get("_truncated")
        ]
        names = sorted(e["name"] for e in items)
        # raw.bin has an unsupported extension, so it should be dropped.
        assert "raw.bin" not in names
        assert "a.pdf" in names

    def test_max_files_truncates_with_sentinel(self, sample_tree):
        items = list(_probe.scan_directory(sample_tree, max_files=2))
        # Sentinel comes last when truncation kicks in.
        assert items[-1].get("_truncated") is True
        assert items[-1]["limit"] == 2
        # Two file entries before the sentinel.
        files = [e for e in items if not e.get("_truncated")]
        assert len(files) == 2

    def test_single_file_target_yields_one_entry(self, sample_tree):
        items = list(_probe.scan_directory(sample_tree / "a.pdf"))
        assert len(items) == 1
        assert items[0]["name"] == "a.pdf"

    # The single-file branch must apply the same filters the directory walk
    # uses — otherwise `probe a.txt --ext pdf` reports a.txt while
    # `probe ./dir --ext pdf` correctly skips it. See PR #3 review for the bug
    # this guards against.
    def test_single_file_ext_filter_drops_mismatch(self, sample_tree):
        items = list(
            _probe.scan_directory(sample_tree / "notes.txt", extensions={".pdf"})
        )
        assert items == []

    def test_single_file_ext_filter_keeps_match(self, sample_tree):
        items = list(
            _probe.scan_directory(sample_tree / "a.pdf", extensions={".pdf"})
        )
        assert len(items) == 1
        assert items[0]["name"] == "a.pdf"

    def test_single_file_supported_only_drops_unsupported(self, sample_tree):
        items = list(
            _probe.scan_directory(sample_tree / "raw.bin", supported_only=True)
        )
        assert items == []

    def test_single_file_supported_only_keeps_supported(self, sample_tree):
        items = list(
            _probe.scan_directory(sample_tree / "a.pdf", supported_only=True)
        )
        assert len(items) == 1

    def test_single_file_hidden_dropped_by_default(self, sample_tree):
        items = list(_probe.scan_directory(sample_tree / ".hidden.md"))
        assert items == []

    def test_single_file_hidden_kept_with_include_hidden(self, sample_tree):
        items = list(
            _probe.scan_directory(sample_tree / ".hidden.md", include_hidden=True)
        )
        assert len(items) == 1
        assert items[0]["name"] == ".hidden.md"

    def test_missing_target_exits(self, tmp_path: Path):
        with pytest.raises(SystemExit):
            list(_probe.scan_directory(tmp_path / "does-not-exist"))


# ---------------------------------------------------------------------------
# summarize
# ---------------------------------------------------------------------------


class TestSummarize:
    def test_aggregates_counts_and_bytes(self):
        entries = [
            {"extension": ".pdf", "size": 100, "supported": True, "readable": True},
            {"extension": ".pdf", "size": 200, "supported": True, "readable": True},
            {"extension": ".bin", "size": 50, "supported": False, "readable": True},
        ]
        summary = _probe.summarize(entries)
        assert summary["total_files"] == 3
        assert summary["total_bytes"] == 350
        assert summary["supported_files"] == 2
        assert summary["supported_bytes"] == 300
        assert summary["by_extension"][".pdf"]["count"] == 2
        assert summary["by_extension"][".pdf"]["bytes"] == 300
        assert summary["by_extension"][".bin"]["count"] == 1

    def test_picks_up_truncation_sentinel(self):
        entries = [
            {"extension": ".pdf", "size": 10, "supported": True, "readable": True},
            {"_truncated": True, "limit": 1},
        ]
        summary = _probe.summarize(entries)
        assert summary["truncated"] is True
        assert summary["truncated_limit"] == 1
        # Total still reflects only the real entries.
        assert summary["total_files"] == 1

    def test_counts_unreadable(self):
        entries = [
            {"extension": ".pdf", "size": 0, "supported": True, "readable": False},
            {"extension": ".pdf", "size": 10, "supported": True, "readable": True},
        ]
        summary = _probe.summarize(entries)
        assert summary["unreadable"] == 1

    def test_collects_walk_error_sentinels(self):
        entries = [
            {"extension": ".pdf", "size": 10, "supported": True, "readable": True},
            {"_walk_error": {"path": "/locked", "error": "PermissionError: denied"}},
        ]
        summary = _probe.summarize(entries)
        assert summary["total_files"] == 1
        assert len(summary["walk_errors"]) == 1
        assert summary["walk_errors"][0]["path"] == "/locked"


# ---------------------------------------------------------------------------
# Type contract — keep the TypedDicts in lockstep with what the code emits
# ---------------------------------------------------------------------------


class TestTypeContract:
    def test_file_info_keys_match_describe_file(self, tmp_path: Path):
        p = tmp_path / "a.pdf"
        p.write_bytes(b"%PDF-1.4")
        info = _probe._describe_file(p, tmp_path)
        assert set(info.keys()) == set(_probe.FileInfo.__annotations__)

    def test_summary_keys_match_typed_shape(self):
        summary = _probe.summarize([])
        assert set(summary.keys()) == set(_probe.ProbeSummary.__annotations__)


# ---------------------------------------------------------------------------
# os.walk error surfacing
# ---------------------------------------------------------------------------


class TestWalkErrors:
    def test_scan_surfaces_walk_errors(self, tmp_path: Path, monkeypatch):
        """A directory os.walk cannot enter is reported, not silently dropped."""
        (tmp_path / "ok.pdf").write_bytes(b"%PDF-1.4")
        real_walk = os.walk

        def fake_walk(top, *args, **kwargs):
            onerror = kwargs.get("onerror")
            if onerror is not None:
                exc = PermissionError(13, "Permission denied")
                exc.filename = str(tmp_path / "locked")
                onerror(exc)
            # Drop onerror so the real walk doesn't try to re-handle it.
            kwargs.pop("onerror", None)
            yield from real_walk(top, *args, **kwargs)

        monkeypatch.setattr(_probe.os, "walk", fake_walk)
        items = list(_probe.scan_directory(tmp_path))

        files = [e for e in items if not e.get("_truncated") and not e.get("_walk_error")]
        walk_errors = [e["_walk_error"] for e in items if e.get("_walk_error")]
        assert [e["name"] for e in files] == ["ok.pdf"]
        assert len(walk_errors) == 1
        assert "Permission denied" in walk_errors[0]["error"]
        assert "locked" in walk_errors[0]["path"]

    def test_walk_errors_appear_in_table_and_json(
        self, tmp_path: Path, monkeypatch, capsys
    ):
        (tmp_path / "ok.pdf").write_bytes(b"%PDF-1.4")
        real_walk = os.walk

        def fake_walk(top, *args, **kwargs):
            onerror = kwargs.get("onerror")
            if onerror is not None:
                exc = PermissionError(13, "Permission denied")
                exc.filename = str(tmp_path / "locked")
                onerror(exc)
            kwargs.pop("onerror", None)
            yield from real_walk(top, *args, **kwargs)

        monkeypatch.setattr(_probe.os, "walk", fake_walk)

        # JSON envelope carries the walk errors under summary.
        rc = _core.main(["probe", str(tmp_path), "--json"])
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        assert len(decoded["summary"]["walk_errors"]) == 1

        # Table output names the unreadable directory.
        rc = _core.main(["probe", str(tmp_path)])
        assert rc == 0
        table = capsys.readouterr().out
        assert "unreadable dirs" in table
        assert "locked" in table


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


class TestRendering:
    def test_render_table_includes_summary_and_paths(self, sample_tree):
        entries = [
            e for e in _probe.scan_directory(sample_tree) if not e.get("_truncated")
        ]
        summary = _probe.summarize(entries)
        out = _probe.render_table(entries, summary)
        assert "summary:" in out
        assert "total files" in out
        # At least one of our top-level files should appear by name.
        assert "a.pdf" in out

    def test_render_json_round_trips(self, sample_tree):
        entries = [
            e for e in _probe.scan_directory(sample_tree) if not e.get("_truncated")
        ]
        summary = _probe.summarize(entries)
        out = _probe.render_json(entries, summary)
        decoded = json.loads(out)
        assert "files" in decoded and "summary" in decoded
        assert decoded["summary"]["total_files"] == len(entries)

    def test_render_table_handles_empty_match(self):
        out = _probe.render_table([], _probe.summarize([]))
        assert "no files matched" in out


# ---------------------------------------------------------------------------
# End-to-end: `llamaparse probe ...` through _core.main
# ---------------------------------------------------------------------------


class TestProbeCommand:
    def test_probe_in_subcommands_tuple(self):
        assert "probe" in _core.SUBCOMMANDS

    def test_probe_appears_in_help(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["--help"])
        assert exc_info.value.code == 0
        out = capsys.readouterr().out
        assert "probe" in out

    def test_probe_basic_run(self, capsys, sample_tree):
        rc = _core.main(["probe", str(sample_tree)])
        assert rc == 0
        out = capsys.readouterr().out
        assert "summary:" in out
        assert "a.pdf" in out

    def test_probe_json_run(self, capsys, sample_tree):
        rc = _core.main(["probe", str(sample_tree), "--json"])
        assert rc == 0
        out = capsys.readouterr().out
        decoded = json.loads(out)
        assert decoded["summary"]["total_files"] >= 1
        names = {f["name"] for f in decoded["files"]}
        assert "a.pdf" in names

    def test_probe_ext_filter_run(self, capsys, sample_tree):
        rc = _core.main(["probe", str(sample_tree), "--ext", "pdf", "--json"])
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        for entry in decoded["files"]:
            assert entry["extension"] == ".pdf"

    def test_probe_missing_target_exits_nonzero(self, capsys, tmp_path: Path):
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["probe", str(tmp_path / "nope")])
        # err() exits with code 2 by default.
        assert exc_info.value.code == 2

    def test_probe_writes_output_file(self, tmp_path: Path, sample_tree, capsys):
        out_file = tmp_path / "report.txt"
        rc = _core.main(
            ["probe", str(sample_tree), "--output", str(out_file)]
        )
        assert rc == 0
        assert out_file.exists()
        content = out_file.read_text(encoding="utf-8")
        assert "summary:" in content

    def test_probe_single_file_ext_filter_consistent_with_directory(
        self, capsys, sample_tree
    ):
        """`probe notes.txt --ext pdf` must agree with `probe ./dir --ext pdf`.

        Before the fix, the single-file branch unconditionally emitted the
        target, so this would report notes.txt while the directory walk
        correctly excluded it.
        """
        rc = _core.main(
            ["probe", str(sample_tree / "notes.txt"), "--ext", "pdf", "--json"]
        )
        assert rc == 0
        decoded = json.loads(capsys.readouterr().out)
        assert decoded["files"] == []
        assert decoded["summary"]["total_files"] == 0
