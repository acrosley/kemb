"""Tests for shared helpers in ``_common``."""
from __future__ import annotations

import json
from pathlib import Path
from unittest import mock

import pytest
import requests_mock

from llamaparse_cli import _common


# ---------------------------------------------------------------------------
# coerce_json_arg
# ---------------------------------------------------------------------------


class TestCoerceJsonArg:
    def test_none_returns_empty_dict(self):
        assert _common.coerce_json_arg(None, "--schema") == {}

    def test_dict_passes_through(self):
        d = {"a": 1}
        assert _common.coerce_json_arg(d, "--schema") is d

    def test_inline_json_string_parsed(self):
        result = _common.coerce_json_arg('{"foo": "bar", "n": 1}', "--schema")
        assert result == {"foo": "bar", "n": 1}

    def test_at_file_reference_reads_and_parses(self, tmp_path: Path):
        p = tmp_path / "schema.json"
        p.write_text('{"type": "object"}', encoding="utf-8")
        result = _common.coerce_json_arg(f"@{p}", "--schema")
        assert result == {"type": "object"}

    def test_missing_at_file_exits(self, tmp_path: Path):
        with pytest.raises(SystemExit):
            _common.coerce_json_arg(f"@{tmp_path}/missing.json", "--schema")

    def test_invalid_json_exits(self):
        with pytest.raises(SystemExit):
            _common.coerce_json_arg("{not json", "--schema")

    def test_non_object_json_exits(self):
        """A bare JSON array isn't a dict, so it should be rejected."""
        with pytest.raises(SystemExit):
            _common.coerce_json_arg("[1, 2, 3]", "--schema")


# ---------------------------------------------------------------------------
# poll_job
# ---------------------------------------------------------------------------


URL = "https://api.cloud.llamaindex.ai/api/v2/parse/job-abc"


class TestPollJob:
    def test_returns_payload_when_completed(self, monkeypatch):
        # Skip time.sleep to keep things fast.
        monkeypatch.setattr(_common.time, "sleep", lambda _: None)
        with requests_mock.Mocker() as m:
            payload = {"job": {"status": "COMPLETED"}, "data": "done"}
            m.get(URL, json=payload)
            out = _common.poll_job(URL, {"Authorization": "Bearer x"}, 30.0)
            assert out == payload

    def test_raises_on_failed_status(self, monkeypatch):
        monkeypatch.setattr(_common.time, "sleep", lambda _: None)
        with requests_mock.Mocker() as m:
            m.get(URL, json={"job": {"status": "FAILED"}, "error": "boom"})
            with pytest.raises(SystemExit):
                _common.poll_job(URL, {}, 30.0)

    def test_polls_until_completion_lowercase_status(self, monkeypatch):
        """Split-style lowercase `pending → completed` transitions must work."""
        monkeypatch.setattr(_common.time, "sleep", lambda _: None)
        with requests_mock.Mocker() as m:
            m.get(
                URL,
                [
                    {"json": {"status": "pending"}},
                    {"json": {"status": "completed", "ok": True}},
                ],
            )
            out = _common.poll_job(URL, {}, 30.0)
            assert out == {"status": "completed", "ok": True}

    def test_timeout_exits(self, monkeypatch):
        """When the deadline elapses before COMPLETED, exit with err()."""
        monkeypatch.setattr(_common.time, "sleep", lambda _: None)

        # Advance monotonic time so the deadline check trips on the first loop.
        clock = {"t": 0.0}

        def _fake_monotonic():
            clock["t"] += 100.0
            return clock["t"]

        monkeypatch.setattr(_common.time, "monotonic", _fake_monotonic)
        with requests_mock.Mocker() as m:
            m.get(URL, json={"status": "pending"})
            with pytest.raises(SystemExit):
                _common.poll_job(URL, {}, poll_timeout=0.01)


# ---------------------------------------------------------------------------
# upload_file_rest
# ---------------------------------------------------------------------------


class TestUploadFileRest:
    def test_happy_path_returns_file_id(self, tmp_path: Path):
        f = tmp_path / "doc.pdf"
        f.write_bytes(b"%PDF-1.4 fake")
        with requests_mock.Mocker() as m:
            m.post(
                f"{_common.API_HOST}/api/v1/beta/files",
                json={"id": "file-xyz-123"},
                status_code=200,
            )
            file_id = _common.upload_file_rest(f)
            assert file_id == "file-xyz-123"
            assert m.call_count == 1

    def test_falls_back_to_file_id_key(self, tmp_path: Path):
        f = tmp_path / "doc.pdf"
        f.write_bytes(b"data")
        with requests_mock.Mocker() as m:
            m.post(
                f"{_common.API_HOST}/api/v1/beta/files",
                json={"file_id": "alt-id-456"},
            )
            assert _common.upload_file_rest(f) == "alt-id-456"

    def test_http_error_exits(self, tmp_path: Path):
        f = tmp_path / "doc.pdf"
        f.write_bytes(b"data")
        with requests_mock.Mocker() as m:
            m.post(
                f"{_common.API_HOST}/api/v1/beta/files",
                status_code=500,
                text="server error",
            )
            with pytest.raises(SystemExit):
                _common.upload_file_rest(f)

    def test_response_missing_id_exits(self, tmp_path: Path):
        f = tmp_path / "doc.pdf"
        f.write_bytes(b"data")
        with requests_mock.Mocker() as m:
            m.post(f"{_common.API_HOST}/api/v1/beta/files", json={"unrelated": True})
            with pytest.raises(SystemExit):
                _common.upload_file_rest(f)
