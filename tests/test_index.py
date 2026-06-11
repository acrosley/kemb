"""Tests for the index facet: schema, incremental scan, search, stats.

Everything here runs against real temp directories and real SQLite — the
whole point of the facet is filesystem/database reconciliation, so mocking
either side would test nothing.
"""
from __future__ import annotations

import json
import os
import sqlite3
from contextlib import closing
from pathlib import Path

import pytest

from kemb import _core, _index


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Fixed, far-apart mtimes so "changed" vs "unchanged" never depends on the
# filesystem's timestamp granularity (FAT: 2s; some NTFS ops: 100ns ticks).
T0 = 1_700_000_000
T1 = 1_700_100_000


def write(path: Path, text: str, mtime: int = T0) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    os.utime(path, (mtime, mtime))
    return path


def make_corpus(root: Path) -> None:
    write(root / "contracts" / "acme.txt", "master services agreement net thirty days")
    write(root / "contracts" / "acme-copy.txt", "master services agreement net thirty days")
    write(root / "notes.md", "quarterly revenue summary for the board")
    write(root / "data.zip", "not really a zip")  # unsupported, no extractor


def scan(root: Path, **kwargs):
    """Create-or-open the default-location index, scan, return the report."""
    db_path = kwargs.pop("db_path", _index.default_db_path(root))
    conn = _index.open_index(db_path, root, create=True)
    with closing(conn):
        return _index.scan_into_index(conn, root, db_path, **kwargs)


def query(root: Path, sql: str, *params):
    conn = _index.open_index(_index.default_db_path(root), root, create=False)
    with closing(conn):
        return conn.execute(sql, params).fetchall()


# ---------------------------------------------------------------------------
# Fresh scan
# ---------------------------------------------------------------------------


class TestFreshScan:
    def test_counts_and_rows(self, tmp_path):
        make_corpus(tmp_path)
        report = scan(tmp_path)

        assert report["added"] == 4
        assert report["changed"] == 0
        assert report["unchanged"] == 0
        assert report["newly_missing"] == 0
        assert report["total_files"] == 4

        rows = query(tmp_path, "SELECT * FROM files ORDER BY relative")
        assert [r["relative"] for r in rows] == [
            "contracts/acme-copy.txt", "contracts/acme.txt",
            "data.zip", "notes.md",
        ]

    def test_content_fields_populated(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        (row,) = query(
            tmp_path, "SELECT * FROM files WHERE relative = ?", "notes.md"
        )
        assert row["sha256"] and len(row["sha256"]) == 64
        assert row["sample_status"] == "ok"
        assert "quarterly revenue" in row["sample_text"]
        assert row["sample_words"] == 6
        assert row["supported"] == 1
        assert row["first_seen"] == row["last_seen"]
        assert row["content_scanned"] is not None
        assert row["missing"] == 0

    def test_unsupported_format_still_hashed(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        (row,) = query(
            tmp_path, "SELECT * FROM files WHERE relative = ?", "data.zip"
        )
        assert row["sample_status"] == "no-extractor"
        assert row["sha256"] is not None  # dedup works even without a sampler
        assert row["supported"] == 0

    def test_duplicates_reported(self, tmp_path):
        make_corpus(tmp_path)
        report = scan(tmp_path)
        assert report["duplicate_groups"] == 1
        assert report["duplicate_files"] == 2

    def test_schema_version_stamped(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        conn = sqlite3.connect(str(_index.default_db_path(tmp_path)))
        with closing(conn):
            assert conn.execute("PRAGMA user_version").fetchone()[0] == 1


# ---------------------------------------------------------------------------
# Incremental behavior — the contract that makes 100k-file corpora workable
# ---------------------------------------------------------------------------


class TestIncrementalScan:
    def test_rescan_unchanged_never_reopens_files(self, tmp_path, monkeypatch):
        make_corpus(tmp_path)
        scan(tmp_path)

        reads = []
        monkeypatch.setattr(
            _index, "_hash_file", lambda p: reads.append(p) or "x"
        )
        monkeypatch.setattr(
            _index, "sample_file",
            lambda *a, **k: reads.append(a) or {},
        )
        report = scan(tmp_path)

        assert report["unchanged"] == 4
        assert report["added"] == report["changed"] == 0
        assert reads == []  # no file was hashed or sampled

    def test_rescan_bumps_last_seen(self, tmp_path):
        make_corpus(tmp_path)
        first = scan(tmp_path)
        second = scan(tmp_path)
        (row,) = query(
            tmp_path, "SELECT * FROM files WHERE relative = ?", "notes.md"
        )
        assert row["first_seen"] == first["scan_time"]
        assert row["last_seen"] == second["scan_time"]

    def test_changed_file_is_rescanned(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        (before,) = query(
            tmp_path, "SELECT sha256 FROM files WHERE relative = ?", "notes.md"
        )

        write(tmp_path / "notes.md", "completely new text here", mtime=T1)
        report = scan(tmp_path)

        assert report["changed"] == 1
        assert report["unchanged"] == 3
        (after,) = query(
            tmp_path,
            "SELECT sha256, sample_text FROM files WHERE relative = ?",
            "notes.md",
        )
        assert after["sha256"] != before["sha256"]
        assert "completely new text" in after["sample_text"]

    def test_same_size_same_mtime_rewrite_is_invisible(self, tmp_path):
        """The documented mtime-tool trade: content swap that preserves both
        size and mtime is not detected without --full."""
        make_corpus(tmp_path)
        scan(tmp_path)
        (before,) = query(
            tmp_path, "SELECT sha256 FROM files WHERE relative = ?", "notes.md"
        )

        original = (tmp_path / "notes.md").read_text(encoding="utf-8")
        write(tmp_path / "notes.md", original[::-1], mtime=T0)  # same length
        report = scan(tmp_path)

        assert report["changed"] == 0
        (after,) = query(
            tmp_path, "SELECT sha256 FROM files WHERE relative = ?", "notes.md"
        )
        assert after["sha256"] == before["sha256"]  # stale, by design

    def test_full_forces_rescan(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        original = (tmp_path / "notes.md").read_text(encoding="utf-8")
        write(tmp_path / "notes.md", original[::-1], mtime=T0)

        scan(tmp_path, full=True)

        (after,) = query(
            tmp_path, "SELECT sample_text FROM files WHERE relative = ?",
            "notes.md",
        )
        assert after["sample_text"].startswith(original[::-1].split()[0])

    def test_new_file_added_on_rescan(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        write(tmp_path / "new-arrival.txt", "fresh document", mtime=T1)
        report = scan(tmp_path)
        assert report["added"] == 1
        assert report["unchanged"] == 4
        assert report["total_files"] == 5


class TestMissingFiles:
    def test_deleted_file_marked_missing_not_deleted(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        (tmp_path / "notes.md").unlink()

        report = scan(tmp_path)

        assert report["newly_missing"] == 1
        assert report["missing_files"] == 1
        assert report["total_files"] == 4  # row retained
        (row,) = query(
            tmp_path, "SELECT missing FROM files WHERE relative = ?", "notes.md"
        )
        assert row["missing"] == 1

    def test_reappearing_file_is_restored_with_history(self, tmp_path):
        make_corpus(tmp_path)
        first = scan(tmp_path)
        original = (tmp_path / "notes.md").read_text(encoding="utf-8")
        (tmp_path / "notes.md").unlink()
        scan(tmp_path)

        write(tmp_path / "notes.md", original, mtime=T0)
        report = scan(tmp_path)

        assert report["restored"] == 1
        assert report["missing_files"] == 0
        (row,) = query(
            tmp_path,
            "SELECT missing, first_seen FROM files WHERE relative = ?",
            "notes.md",
        )
        assert row["missing"] == 0
        assert row["first_seen"] == first["scan_time"]  # identity kept

    def test_filtered_scan_does_not_mark_missing(self, tmp_path):
        """An --ext pdf scan cannot see .txt files; it must not conclude
        they're gone."""
        make_corpus(tmp_path)
        scan(tmp_path)
        report = scan(tmp_path, extensions={".pdf"})
        assert report["newly_missing"] == 0
        assert report["missing_files"] == 0

    def test_truncated_scan_does_not_mark_missing(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        report = scan(tmp_path, max_files=2)
        assert report["truncated"] is True
        assert report["newly_missing"] == 0


# ---------------------------------------------------------------------------
# Self-exclusion
# ---------------------------------------------------------------------------


class TestSelfExclusion:
    def test_default_db_invisible_even_with_include_hidden(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        report = scan(tmp_path, include_hidden=True)
        rows = query(tmp_path, "SELECT relative FROM files")
        assert all(".kemb" not in r["relative"] for r in rows)
        assert report["added"] == 0

    def test_custom_db_inside_corpus_excluded(self, tmp_path):
        make_corpus(tmp_path)
        db_path = tmp_path / "index.db"  # visible location inside the corpus
        scan(tmp_path, db_path=db_path)
        conn = _index.open_index(db_path, tmp_path, create=False)
        with closing(conn):
            rows = conn.execute("SELECT relative FROM files").fetchall()
        names = [r["relative"] for r in rows]
        assert "index.db" not in names
        assert len(names) == 4


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------


class TestSearch:
    def _open(self, root):
        return _index.open_index(_index.default_db_path(root), root, create=False)

    def test_fts_match(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        with closing(self._open(tmp_path)) as conn:
            result = _index.search_index(conn, "quarterly revenue", 20)
        assert result["engine"] == "fts5"
        assert [r["relative"] for r in result["results"]] == ["notes.md"]
        assert "[quarterly]" in result["results"][0]["snippet"]

    def test_path_terms_match(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        with closing(self._open(tmp_path)) as conn:
            result = _index.search_index(conn, "acme", 20)
        found = {r["relative"] for r in result["results"]}
        assert found == {"contracts/acme.txt", "contracts/acme-copy.txt"}

    def test_missing_files_excluded_from_results(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        (tmp_path / "notes.md").unlink()
        scan(tmp_path)
        with closing(self._open(tmp_path)) as conn:
            result = _index.search_index(conn, "quarterly", 20)
        assert result["results"] == []

    def test_bad_fts_syntax_falls_back_to_substring(self, tmp_path):
        """A query FTS5 can't parse still answers via the substring path."""
        make_corpus(tmp_path)
        write(tmp_path / "invoice.txt", 'total due "net thirty" on receipt')
        scan(tmp_path)
        with closing(self._open(tmp_path)) as conn:
            # Unbalanced quote: an FTS5 syntax error, but a real substring.
            result = _index.search_index(conn, '"net thirty', 20)
        assert result["engine"] == "substring"
        assert [r["relative"] for r in result["results"]] == ["invoice.txt"]

    def test_substring_engine_when_fts_unavailable(self, tmp_path, monkeypatch):
        monkeypatch.setattr(_index, "_fts_available", lambda conn: False)
        make_corpus(tmp_path)
        scan(tmp_path)
        with closing(self._open(tmp_path)) as conn:
            result = _index.search_index(conn, "quarterly revenue", 20)
        assert result["engine"] == "substring"
        assert [r["relative"] for r in result["results"]] == ["notes.md"]

    def test_limit_respected(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        with closing(self._open(tmp_path)) as conn:
            result = _index.search_index(conn, "agreement", 1)
        assert len(result["results"]) == 1


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------


class TestStats:
    def test_stats_shape(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        db_path = _index.default_db_path(tmp_path)
        conn = _index.open_index(db_path, tmp_path, create=False)
        with closing(conn):
            stats = _index.index_stats(conn, db_path)

        assert stats["schema_version"] == 1
        assert stats["total_files"] == 4
        assert stats["supported_files"] == 3
        assert stats["by_extension"][".txt"]["count"] == 2
        assert stats["by_sample_status"]["ok"] == 3
        assert stats["by_sample_status"]["no-extractor"] == 1
        assert len(stats["duplicate_groups"]) == 1
        assert sorted(stats["duplicate_groups"][0]["paths"]) == [
            "contracts/acme-copy.txt", "contracts/acme.txt",
        ]
        assert stats["passes_by_status"] == {}


# ---------------------------------------------------------------------------
# Guard rails
# ---------------------------------------------------------------------------


class TestGuards:
    def test_stats_without_index_errors(self, tmp_path):
        with pytest.raises(SystemExit) as exc_info:
            _index.open_index(
                _index.default_db_path(tmp_path), tmp_path, create=False
            )
        assert exc_info.value.code == 2

    def test_schema_mismatch_errors(self, tmp_path):
        make_corpus(tmp_path)
        scan(tmp_path)
        db_path = _index.default_db_path(tmp_path)
        conn = sqlite3.connect(str(db_path))
        with closing(conn):
            conn.execute("PRAGMA user_version = 99")
        with pytest.raises(SystemExit) as exc_info:
            _index.open_index(db_path, tmp_path, create=True)
        assert exc_info.value.code == 2

    def test_passes_table_exists_for_future_facets(self, tmp_path):
        """Schema v1 reserves the passes table so the upcoming batch facet
        can resume against v1 databases without a migration."""
        make_corpus(tmp_path)
        scan(tmp_path)
        conn = sqlite3.connect(str(_index.default_db_path(tmp_path)))
        with closing(conn):
            cols = {
                row[1] for row in conn.execute("PRAGMA table_info(passes)")
            }
        assert {"file_id", "facet", "tier", "status", "credits",
                "output_path", "started", "finished", "error"} <= cols


# ---------------------------------------------------------------------------
# Sync-on-read: queries refresh the index before answering
# ---------------------------------------------------------------------------


class TestSyncOnRead:
    def test_search_sees_file_added_after_last_scan(self, tmp_path, capsys):
        make_corpus(tmp_path)
        _core.main(["index", str(tmp_path)])
        write(tmp_path / "late-arrival.txt", "indemnification rider", mtime=T1)
        capsys.readouterr()

        rc = _core.main(
            ["index", str(tmp_path), "--search", "indemnification", "--json"]
        )

        assert rc == 0
        captured = capsys.readouterr()
        result = json.loads(captured.out)
        assert [r["relative"] for r in result["results"]] == ["late-arrival.txt"]
        assert "1 added" in captured.err  # refresh reported, on stderr only

    def test_stats_sees_deletion_after_last_scan(self, tmp_path, capsys):
        make_corpus(tmp_path)
        _core.main(["index", str(tmp_path)])
        (tmp_path / "notes.md").unlink()
        capsys.readouterr()

        rc = _core.main(["index", str(tmp_path), "--stats", "--json"])

        assert rc == 0
        stats = json.loads(capsys.readouterr().out)
        assert stats["missing_files"] == 1

    def test_stale_skips_the_refresh(self, tmp_path, capsys):
        make_corpus(tmp_path)
        _core.main(["index", str(tmp_path)])
        write(tmp_path / "late-arrival.txt", "indemnification rider", mtime=T1)
        capsys.readouterr()

        _core.main(
            ["index", str(tmp_path), "--search", "indemnification",
             "--json", "--stale"]
        )

        captured = capsys.readouterr()
        assert json.loads(captured.out)["results"] == []
        assert captured.err == ""

    def test_refresh_quiet_when_nothing_moved(self, tmp_path, capsys):
        make_corpus(tmp_path)
        _core.main(["index", str(tmp_path)])
        capsys.readouterr()
        _core.main(["index", str(tmp_path), "--stats"])
        assert capsys.readouterr().err == ""

    def test_refresh_honors_stored_sample_settings(self, tmp_path, capsys):
        make_corpus(tmp_path)
        _core.main(["index", str(tmp_path), "--sample-words", "2"])
        write(tmp_path / "late-arrival.txt",
              "one two three four five six", mtime=T1)
        capsys.readouterr()

        _core.main(["index", str(tmp_path), "--stats"])

        (row,) = query(
            tmp_path,
            "SELECT sample_words FROM files WHERE relative = ?",
            "late-arrival.txt",
        )
        assert row["sample_words"] == 2  # not the default 120

    def test_query_survives_vanished_corpus_root(self, tmp_path, capsys):
        """A detached index (--db elsewhere, corpus gone) still answers,
        with a staleness warning instead of a crash."""
        corpus = tmp_path / "corpus"
        write(corpus / "doc.txt", "quarterly revenue")
        db = tmp_path / "detached.db"
        _core.main(["index", str(corpus), "--db", str(db)])
        import shutil
        shutil.rmtree(corpus)
        capsys.readouterr()

        rc = _core.main(
            ["index", str(corpus), "--db", str(db),
             "--search", "quarterly", "--json"]
        )

        assert rc == 0
        captured = capsys.readouterr()
        result = json.loads(captured.out)
        assert [r["relative"] for r in result["results"]] == ["doc.txt"]
        assert "may be stale" in captured.err

    def test_stale_requires_a_query_mode(self, tmp_path):
        make_corpus(tmp_path)
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["index", str(tmp_path), "--stale"])
        assert exc_info.value.code == 2


# ---------------------------------------------------------------------------
# CLI integration
# ---------------------------------------------------------------------------


class TestCli:
    def test_dispatcher_registered(self):
        parser = _core.build_parser()
        args = parser.parse_args(["index", ".", "--auto-install"])
        assert args.command == "index"
        assert args.auto_install is True

    def test_scan_json_envelope(self, tmp_path, capsys):
        make_corpus(tmp_path)
        rc = _core.main(["index", str(tmp_path), "--json"])
        assert rc == 0
        report = json.loads(capsys.readouterr().out)
        assert report["added"] == 4
        assert report["truncated"] is False

    def test_search_json_envelope(self, tmp_path, capsys):
        make_corpus(tmp_path)
        _core.main(["index", str(tmp_path)])
        capsys.readouterr()
        rc = _core.main(
            ["index", str(tmp_path), "--search", "quarterly", "--json"]
        )
        assert rc == 0
        result = json.loads(capsys.readouterr().out)
        assert result["results"][0]["relative"] == "notes.md"

    def test_stats_and_search_mutually_exclusive(self, tmp_path):
        with pytest.raises(SystemExit) as exc_info:
            _core.main(
                ["index", str(tmp_path), "--stats", "--search", "x"]
            )
        assert exc_info.value.code == 2

    def test_target_must_be_directory_for_scan(self, tmp_path):
        target = write(tmp_path / "file.txt", "hi")
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["index", str(target)])
        assert exc_info.value.code == 2
