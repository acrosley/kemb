"""Tests for ``--dry-run`` across parse / classify.

These tests verify that dry-run never touches the network. The ``_ban_network``
fixture below makes that a hard assertion: every ``requests`` HTTP verb is
replaced with a stub that fails the test if called. Without it the suite would
rely on ``requests.post`` *happening* to fail (because the stubbed API key is
rejected), which would silently pass on a machine behind a captive portal that
returns 200.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import requests

from kemb import _common, _core


@pytest.fixture(autouse=True)
def _ban_network(monkeypatch):
    """Fail loudly if any dry-run path makes an HTTP call.

    Applied to every test in this module so a regression that uploads under
    --dry-run fails as an explicit assertion rather than an incidental
    connection error.
    """
    def _forbidden(verb):
        def _fail(*args, **kwargs):
            pytest.fail(
                f"dry-run made a network call: requests.{verb}"
                f"(args={args!r}, kwargs={kwargs!r})"
            )
        return _fail

    for verb in ("get", "post", "put", "patch", "delete", "head", "request"):
        monkeypatch.setattr(requests, verb, _forbidden(verb))


@pytest.fixture
def fake_pdf(tmp_path: Path) -> Path:
    p = tmp_path / "sample.pdf"
    p.write_bytes(b"%PDF-1.4 fake content " + b"x" * 256)
    return p


@pytest.fixture
def rules_file(tmp_path: Path) -> Path:
    p = tmp_path / "rules.json"
    p.write_text(json.dumps([
        {"type": "invoice", "description": "A bill"},
        {"type": "contract", "description": "A legal agreement"},
    ]), encoding="utf-8")
    return p


# ---------------------------------------------------------------------------
# Shared dry-run renderer
# ---------------------------------------------------------------------------


class TestRenderDryRun:
    def test_basic_layout_and_trailer(self):
        out = _common.render_dry_run("parse", {"input": "foo.pdf", "tier": "fast"})
        assert out.startswith("[dry-run] kemb parse")
        assert "input" in out
        assert "tier" in out
        assert "fast" in out
        assert out.endswith("no upload, no job, no credits spent.")

    def test_none_renders_as_placeholder(self):
        out = _common.render_dry_run("classify", {"project-id": None})
        assert "(none)" in out

    def test_long_dict_truncated(self):
        big = {"k": "v" * 1000}
        out = _common.render_dry_run("classify", {"configuration": big})
        # Truncation should keep the line readable.
        assert "..." in out


class TestDescribeInput:
    def test_includes_size(self, fake_pdf):
        desc = _common.describe_input(fake_pdf)
        assert str(fake_pdf) in desc
        assert "B" in desc  # bytes / KB / etc.


# ---------------------------------------------------------------------------
# Per-subcommand dry-run smoke tests
# ---------------------------------------------------------------------------


class TestParseDryRun:
    def test_emits_plan_and_no_network(self, fake_pdf, capsys):
        rc = _core.main(["parse", str(fake_pdf), "--dry-run", "--tier", "agentic"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "[dry-run] kemb parse" in out
        assert "agentic" in out
        assert "no upload" in out
        # Default markdown output path should appear.
        assert str(fake_pdf.with_suffix(".md")) in out

    def test_missing_input_still_errors(self, tmp_path: Path):
        with pytest.raises(SystemExit):
            _core.main(["parse", str(tmp_path / "nope.pdf"), "--dry-run"])

    def test_rest_flag_reflected_in_transport(self, fake_pdf, capsys):
        _core.main(["parse", str(fake_pdf), "--dry-run", "--rest"])
        out = capsys.readouterr().out
        assert "REST" in out


class TestClassifyDryRun:
    def test_emits_plan_with_rule_labels(self, fake_pdf, rules_file, capsys):
        rc = _core.main([
            "classify", str(fake_pdf),
            "--rules", f"@{rules_file}",
            "--mode", "multimodal",
            "--dry-run",
        ])
        assert rc == 0
        out = capsys.readouterr().out
        assert "[dry-run] kemb classify" in out
        assert "invoice" in out
        assert "multimodal" in out

    def test_missing_rules_still_errors(self, fake_pdf):
        with pytest.raises(SystemExit):
            _core.main(["classify", str(fake_pdf), "--dry-run"])
