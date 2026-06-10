"""Tests for the `doctor` subcommand.

All checks must be mock-only — no live LlamaCloud calls.
"""
from __future__ import annotations

import sys

import pytest
import requests
import requests_mock

from kemb import _common, _core, _doctor


# ---------------------------------------------------------------------------
# mask_key
# ---------------------------------------------------------------------------


class TestMaskKey:
    def test_full_key_redacts_middle(self):
        assert _doctor.mask_key("llx-ABCD1234EFGH5678") == "llx-...5678"

    def test_short_key_fully_masked(self):
        assert _doctor.mask_key("abc") == "****"

    def test_whitespace_stripped(self):
        assert _doctor.mask_key("  llx-ABCD1234  ") == "llx-...1234"


# ---------------------------------------------------------------------------
# check_python_version
# ---------------------------------------------------------------------------


class TestCheckPythonVersion:
    def test_current_interpreter_passes(self):
        """The interpreter running the tests is necessarily supported."""
        status, headline, _ = _doctor.check_python_version()
        assert status == _doctor._OK
        assert "Python" in headline

    def test_old_python_fails(self, monkeypatch):
        monkeypatch.setattr(_doctor.sys, "version_info", (3, 8, 0, "final", 0))
        status, _, detail = _doctor.check_python_version()
        assert status == _doctor._FAIL
        assert "3.9" in (detail or "")


# ---------------------------------------------------------------------------
# check_requests / check_sdk
# ---------------------------------------------------------------------------


class TestCheckRequests:
    def test_requests_importable(self):
        status, headline, _ = _doctor.check_requests()
        assert status == _doctor._OK
        assert headline.startswith("requests ")


class TestCheckSdk:
    def test_warn_when_missing(self, monkeypatch):
        """Simulate `llama_cloud` not being importable."""
        # Hide a previously-imported llama_cloud so the fresh import fails.
        monkeypatch.setitem(sys.modules, "llama_cloud", None)
        status, headline, detail = _doctor.check_sdk()
        assert status == _doctor._WARN
        assert "not installed" in headline
        assert "REST fallback" in (detail or "")


# ---------------------------------------------------------------------------
# check_api_key
# ---------------------------------------------------------------------------


class TestCheckApiKey:
    def test_present_key_is_masked(self, monkeypatch):
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-ABCD1234EFGH5678")
        status, headline, _ = _doctor.check_api_key()
        assert status == _doctor._OK
        assert "llx-...5678" in headline
        # The full key must never appear in the headline.
        assert "ABCD1234EFGH" not in headline

    def test_missing_key_fails(self, monkeypatch):
        monkeypatch.delenv("LLAMA_CLOUD_API_KEY", raising=False)
        status, headline, detail = _doctor.check_api_key()
        assert status == _doctor._FAIL
        assert "LLAMA_CLOUD_API_KEY" in headline
        assert "https://cloud.llamaindex.ai" in (detail or "")


# ---------------------------------------------------------------------------
# check_api_reachable
# ---------------------------------------------------------------------------


REACH_URL = f"{_common.API_HOST}/api/v1/beta/files"


class TestCheckApiReachable:
    def test_2xx_means_auth_works(self, monkeypatch):
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-good")
        with requests_mock.Mocker() as m:
            m.head(REACH_URL, status_code=200)
            status, headline, _ = _doctor.check_api_reachable(timeout=5)
            assert status == _doctor._OK
            assert "-> 200" in headline

    def test_405_method_not_allowed_means_auth_works(self, monkeypatch):
        """A POST-only endpoint that returns 405 to a HEAD still proves auth."""
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-good")
        with requests_mock.Mocker() as m:
            m.head(REACH_URL, status_code=405)
            status, headline, _ = _doctor.check_api_reachable(timeout=5)
            assert status == _doctor._OK
            assert "-> 405" in headline

    def test_401_means_bad_key(self, monkeypatch):
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-bad")
        with requests_mock.Mocker() as m:
            m.head(REACH_URL, status_code=401)
            status, headline, detail = _doctor.check_api_reachable(timeout=5)
            assert status == _doctor._FAIL
            assert "rejected" in headline
            assert "401" in headline
            assert "rotate" in (detail or "").lower() or "typo" in (detail or "").lower()

    def test_403_surfaces_allowlist_hint(self, monkeypatch):
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-restricted")
        with requests_mock.Mocker() as m:
            m.head(REACH_URL, status_code=403)
            status, _, detail = _doctor.check_api_reachable(timeout=5)
            assert status == _doctor._FAIL
            # Cowork hint should appear so the user knows where to look.
            assert "allowlist" in (detail or "").lower()

    def test_connection_error_is_network_failure(self, monkeypatch):
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-good")
        with requests_mock.Mocker() as m:
            m.head(REACH_URL, exc=requests.exceptions.ConnectionError("dns dead"))
            status, headline, _ = _doctor.check_api_reachable(timeout=5)
            assert status == _doctor._FAIL
            assert "could not reach" in headline

    def test_no_key_skips_probe(self, monkeypatch):
        monkeypatch.delenv("LLAMA_CLOUD_API_KEY", raising=False)
        status, _, _ = _doctor.check_api_reachable(timeout=5)
        assert status == _doctor._SKIP


# ---------------------------------------------------------------------------
# End-to-end: `kemb doctor` through _core.main
# ---------------------------------------------------------------------------


class TestDoctorCommand:
    def test_offline_doctor_runs_clean_with_key(self, capsys, monkeypatch):
        """Doctor with --offline should exit 0 when env is healthy."""
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-good-test-key")
        rc = _core.main(["doctor", "--offline"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "kemb doctor" in out
        assert "auth probe skipped" in out

    def test_offline_doctor_fails_without_key(self, capsys, monkeypatch):
        monkeypatch.delenv("LLAMA_CLOUD_API_KEY", raising=False)
        rc = _core.main(["doctor", "--offline"])
        assert rc == 1
        out = capsys.readouterr().out
        assert _doctor._FAIL in out

    def test_online_doctor_with_mocked_api(self, capsys, monkeypatch):
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-good-test-key")
        with requests_mock.Mocker() as m:
            m.head(REACH_URL, status_code=200)
            rc = _core.main(["doctor"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "LlamaCloud reachable" in out

    def test_doctor_appears_in_help(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["--help"])
        assert exc_info.value.code == 0
        out = capsys.readouterr().out
        assert "doctor" in out

    def test_doctor_in_subcommands_tuple(self):
        assert "doctor" in _core.SUBCOMMANDS

    def test_output_is_ascii_safe_on_cp1252_consoles(self, capsys, monkeypatch):
        """Regression: doctor must not emit chars cp1252 can't encode.

        Windows consoles default to cp1252; a non-ASCII char in the output
        crashes the print() call with UnicodeEncodeError. Cover every status
        branch so future contributors don't reintroduce one.
        """
        monkeypatch.setenv("LLAMA_CLOUD_API_KEY", "llx-good-test-key")
        with requests_mock.Mocker() as m:
            m.head(REACH_URL, status_code=200)
            _core.main(["doctor"])
        captured = capsys.readouterr()
        combined = captured.out + captured.err
        # If any character can't round-trip through cp1252, this raises.
        combined.encode("cp1252")
