"""Tests for the facet ``run()`` orchestration: the SDK-first / REST-fallback
contract and an end-to-end (mocked-HTTP) pass through each REST runner.

The per-facet unit tests cover the leaf helpers (config building, envelope
parsing); these cover the wiring that turns those helpers into a working job:
the try-SDK/except-ImportError/fall-back-to-REST branch in ``run()`` and the
upload → create → poll → extract sequence in each ``*_with_rest`` runner.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pytest
import requests_mock

from kemb import _classify, _common, _extract, _split


# ---------------------------------------------------------------------------
# SDK → REST fallback in run()
#
# CLAUDE.md calls SDK-first/REST-fallback the canonical facet contract, yet
# nothing exercised it. Each case forces the SDK path to raise ImportError and
# asserts run() transparently falls back to REST and notes it on stderr.
# ---------------------------------------------------------------------------


def _make_doc(tmp_path: Path) -> Path:
    f = tmp_path / "doc.pdf"
    f.write_bytes(b"%PDF-1.4 stub")
    return f


class TestSdkToRestFallback:
    def test_extract_falls_back(self, tmp_path, monkeypatch, capsys):
        doc = _make_doc(tmp_path)

        def _no_sdk(*a, **k):
            raise ImportError("llama-cloud SDK not available")

        monkeypatch.setattr(_extract, "extract_with_sdk", _no_sdk)
        monkeypatch.setattr(
            _extract, "extract_with_rest",
            lambda *a, **k: '{"rest": true}',
        )
        args = argparse.Namespace(
            input=doc, output=None, schema='{"type":"object"}',
            configuration=None, configuration_id=None, project_id=None,
            rest=False, poll_timeout=600.0, auto_install=False, stdout=False,
            dry_run=False,
        )
        rc = _extract.run(args)
        assert rc == 0
        assert (tmp_path / "doc.extract.json").read_text(encoding="utf-8") == '{"rest": true}'
        assert "falling back to REST" in capsys.readouterr().err

    def test_classify_falls_back(self, tmp_path, monkeypatch, capsys):
        doc = _make_doc(tmp_path)

        def _no_sdk(*a, **k):
            raise ImportError("llama-cloud SDK not available")

        monkeypatch.setattr(_classify, "classify_with_sdk", _no_sdk)
        monkeypatch.setattr(
            _classify, "classify_with_rest",
            lambda *a, **k: '{"type": "invoice"}',
        )
        args = argparse.Namespace(
            input=doc, output=None, rules='[{"type":"a","description":"b"}]',
            configuration=None, configuration_id=None, mode=None,
            project_id=None, rest=False, poll_timeout=600.0, auto_install=False,
            stdout=False, dry_run=False,
        )
        rc = _classify.run(args)
        assert rc == 0
        assert (tmp_path / "doc.classify.json").read_text(encoding="utf-8") == '{"type": "invoice"}'
        assert "falling back to REST" in capsys.readouterr().err

    def test_split_falls_back(self, tmp_path, monkeypatch, capsys):
        doc = _make_doc(tmp_path)

        def _no_sdk(*a, **k):
            raise ImportError("Installed llama-cloud SDK has no beta.split")

        monkeypatch.setattr(_split, "split_with_sdk", _no_sdk)
        monkeypatch.setattr(
            _split, "split_with_rest",
            lambda *a, **k: '{"segments": []}',
        )
        args = argparse.Namespace(
            input=doc, output=None, categories='[{"name":"a","description":"b"}]',
            configuration=None, configuration_id=None, splitting_strategy=None,
            project_id=None, rest=False, poll_timeout=600.0, auto_install=False,
            stdout=False, dry_run=False,
        )
        rc = _split.run(args)
        assert rc == 0
        assert (tmp_path / "doc.split.json").read_text(encoding="utf-8") == '{"segments": []}'
        assert "falling back to REST" in capsys.readouterr().err


# ---------------------------------------------------------------------------
# End-to-end REST runners (upload → create → poll → extract), all mocked.
#
# Proves the URLs, job-id extraction, and result-envelope plumbing actually
# line up — the kind of bug (wrong job-id key, wrong status field) that the
# leaf-helper tests can't catch.
# ---------------------------------------------------------------------------


UPLOAD_URL = f"{_common.API_HOST}/api/v1/beta/files"


class TestRestRunnersEndToEnd:
    @pytest.fixture(autouse=True)
    def _no_sleep(self, monkeypatch):
        monkeypatch.setattr(_common.time, "sleep", lambda _: None)

    def test_extract_rest_roundtrip(self, tmp_path):
        doc = _make_doc(tmp_path)
        create = f"{_common.API_HOST}/api/v2/extract"
        with requests_mock.Mocker() as m:
            m.post(UPLOAD_URL, json={"id": "file-1"})
            m.post(create, json={"id": "job-1"})
            m.get(f"{create}/job-1", json={
                "status": "COMPLETED",
                "data": {"invoice_number": "A-100"},
            })
            out = _extract.extract_with_rest(
                doc, {"type": "object"}, None, None, None, 30.0
            )
        assert json.loads(out) == {"invoice_number": "A-100"}

    def test_classify_rest_roundtrip(self, tmp_path):
        doc = _make_doc(tmp_path)
        create = f"{_common.API_HOST}/api/v2/classify"
        with requests_mock.Mocker() as m:
            m.post(UPLOAD_URL, json={"id": "file-1"})
            m.post(create, json={"id": "job-1"})
            m.get(f"{create}/job-1", json={
                "status": "COMPLETED",
                "result": {"type": "invoice", "confidence": 0.9},
            })
            out = _classify.classify_with_rest(
                doc, [{"type": "invoice", "description": "a bill"}],
                None, None, None, None, 30.0,
            )
        assert json.loads(out) == {"type": "invoice", "confidence": 0.9}

    def test_split_rest_roundtrip_lowercase_status(self, tmp_path):
        """Split uses a custom status getter and lowercase statuses; prove the
        whole chain (including the split-specific job-id key) works."""
        doc = _make_doc(tmp_path)
        base = f"{_common.API_HOST}/api/v1/beta/split/jobs"
        with requests_mock.Mocker() as m:
            m.post(UPLOAD_URL, json={"id": "file-1"})
            m.post(base, json={"split_job_id": "job-1"})
            m.get(f"{base}/job-1", json={
                "status": "completed",
                "result": {"segments": [{"name": "intro"}]},
            })
            out = _split.split_with_rest(
                doc, [{"name": "intro", "description": "opening"}],
                None, None, None, None, 30.0,
            )
        assert json.loads(out) == {"segments": [{"name": "intro"}]}

    def test_extract_rest_create_error_exits(self, tmp_path):
        doc = _make_doc(tmp_path)
        create = f"{_common.API_HOST}/api/v2/extract"
        with requests_mock.Mocker() as m:
            m.post(UPLOAD_URL, json={"id": "file-1"})
            m.post(create, status_code=400, text="bad schema")
            with pytest.raises(SystemExit) as exc:
                _extract.extract_with_rest(
                    doc, {"type": "object"}, None, None, None, 30.0
                )
            assert exc.value.code == 3
