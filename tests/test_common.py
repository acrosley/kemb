"""Tests for shared helpers in ``_common``."""
from __future__ import annotations

import json
from pathlib import Path
from unittest import mock

import pytest
import requests_mock

from kemb import _common


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

    def test_failed_status_surfaces_reason(self, monkeypatch, capsys):
        """A FAILED job must lead with the human-readable reason, not just
        the raw envelope dump."""
        monkeypatch.setattr(_common.time, "sleep", lambda _: None)
        with requests_mock.Mocker() as m:
            m.get(URL, json={
                "status": "FAILED",
                "error_message": "password-protected PDF",
            })
            with pytest.raises(SystemExit) as exc:
                _common.poll_job(URL, {}, 30.0)
            assert exc.value.code == 3
            assert "password-protected PDF" in capsys.readouterr().err

    def test_custom_status_getter_used(self, monkeypatch):
        """A caller-supplied status_getter (split passes one) is honored."""
        monkeypatch.setattr(_common.time, "sleep", lambda _: None)
        with requests_mock.Mocker() as m:
            # Status lives somewhere the default getter wouldn't look.
            m.get(URL, json={"phase": "completed", "ok": True})
            out = _common.poll_job(
                URL, {}, 30.0,
                status_getter=lambda p: p.get("phase", ""),
            )
            assert out == {"phase": "completed", "ok": True}

    def test_http_error_during_poll_exits(self, monkeypatch):
        """A 4xx/5xx while polling exits with code 3."""
        monkeypatch.setattr(_common.time, "sleep", lambda _: None)
        with requests_mock.Mocker() as m:
            m.get(URL, status_code=503, text="upstream down")
            with pytest.raises(SystemExit) as exc:
                _common.poll_job(URL, {}, 30.0)
            assert exc.value.code == 3

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


# ---------------------------------------------------------------------------
# surface_api_error
# ---------------------------------------------------------------------------


class TestSurfaceApiError:
    def test_body_dict_rendered_and_exits_3(self, capsys):
        exc = Exception("oops")
        exc.body = {"detail": "schema validation failed", "field": "total"}
        with pytest.raises(SystemExit) as si:
            _common.surface_api_error("extract failed", exc)
        assert si.value.code == 3
        err = capsys.readouterr().err
        assert "extract failed" in err
        assert "schema validation failed" in err

    def test_response_text_used_when_no_body(self, capsys):
        exc = Exception("boom")
        exc.response = mock.Mock(text="upstream 500 detail")
        with pytest.raises(SystemExit):
            _common.surface_api_error("classify failed", exc)
        assert "upstream 500 detail" in capsys.readouterr().err

    def test_bare_exception_falls_back_to_repr(self, capsys):
        with pytest.raises(SystemExit):
            _common.surface_api_error("split failed", ValueError("naked"))
        err = capsys.readouterr().err
        assert "split failed" in err
        assert "naked" in err


# ---------------------------------------------------------------------------
# _failure_reason
# ---------------------------------------------------------------------------


class TestFailureReason:
    def test_top_level_error_message(self):
        assert _common._failure_reason(
            {"error_message": "bad scan"}
        ) == "bad scan"

    def test_falls_back_through_keys(self):
        assert _common._failure_reason({"detail": "nope"}) == "nope"

    def test_nested_under_job(self):
        assert _common._failure_reason(
            {"job": {"error": "worker died"}}
        ) == "worker died"

    def test_no_reason_present(self):
        assert _common._failure_reason(
            {"status": "FAILED"}
        ) == "(no reason in payload)"


# ---------------------------------------------------------------------------
# try_install_sdk
# ---------------------------------------------------------------------------


class TestTryInstallSdk:
    def test_success_returns_true(self, monkeypatch):
        monkeypatch.setattr(
            _common.subprocess, "run",
            lambda *a, **k: mock.Mock(returncode=0, stdout=""),
        )
        assert _common.try_install_sdk() is True

    def test_failure_returns_false_and_reports_stderr(self, monkeypatch, capsys):
        """When every pip attempt fails, the user (who asked for
        --auto-install) must see *why*, not a silent False."""
        monkeypatch.setattr(
            _common.subprocess, "run",
            lambda *a, **k: mock.Mock(
                returncode=1, stdout="ERROR: could not resolve llama-cloud"
            ),
        )
        assert _common.try_install_sdk() is False
        assert "could not resolve llama-cloud" in capsys.readouterr().err
