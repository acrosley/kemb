"""Tests for ``_split``: categories normalization, status casing, result fallback."""
from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from kemb import _split


# ---------------------------------------------------------------------------
# _normalize_categories
# ---------------------------------------------------------------------------


class TestNormalizeCategories:
    def test_none_returns_none(self):
        assert _split._normalize_categories(None) is None

    def test_valid_inline(self):
        cats = '[{"name":"intro","description":"opening summary"}]'
        assert _split._normalize_categories(cats) == [
            {"name": "intro", "description": "opening summary"}
        ]

    def test_at_file_reference(self, tmp_path: Path):
        p = tmp_path / "cats.json"
        p.write_text(
            json.dumps([{"name": "body", "description": "main content"}]),
            encoding="utf-8",
        )
        assert _split._normalize_categories(f"@{p}") == [
            {"name": "body", "description": "main content"}
        ]

    def test_invalid_json_exits(self):
        with pytest.raises(SystemExit):
            _split._normalize_categories("not valid json")

    def test_non_list_exits(self):
        with pytest.raises(SystemExit):
            _split._normalize_categories('{"name": "x", "description": "y"}')

    def test_missing_name_exits(self):
        with pytest.raises(SystemExit):
            _split._normalize_categories('[{"description": "only desc"}]')

    def test_missing_description_exits(self):
        with pytest.raises(SystemExit):
            _split._normalize_categories('[{"name": "only-name"}]')

    def test_category_not_dict_exits(self):
        with pytest.raises(SystemExit):
            _split._normalize_categories('["bare-string"]')


# ---------------------------------------------------------------------------
# _split_status — lowercase handling
# ---------------------------------------------------------------------------


class TestSplitStatus:
    def test_top_level_lowercase_status(self):
        assert _split._split_status({"status": "completed"}) == "completed"

    def test_nested_job_status(self):
        assert _split._split_status({"job": {"status": "pending"}}) == "pending"

    def test_missing_status_returns_empty_string(self):
        assert _split._split_status({"unrelated": True}) == ""

    def test_top_level_wins_over_nested(self):
        payload = {"status": "completed", "job": {"status": "pending"}}
        assert _split._split_status(payload) == "completed"


# ---------------------------------------------------------------------------
# _extract_result — fallback chain
# ---------------------------------------------------------------------------


class TestExtractResult:
    def test_dict_with_result_key(self):
        out = _split._extract_result({"result": {"sections": [1, 2]}})
        assert json.loads(out) == {"sections": [1, 2]}

    def test_dict_with_split_key(self):
        out = _split._extract_result({"split": {"sections": [{"a": 1}]}})
        assert json.loads(out) == {"sections": [{"a": 1}]}

    def test_dict_with_segments_key(self):
        out = _split._extract_result({"segments": [{"id": 1}]})
        assert json.loads(out) == [{"id": 1}]

    def test_object_with_result_attribute(self):
        obj = SimpleNamespace(result={"sections": []})
        assert json.loads(_split._extract_result(obj)) == {"sections": []}

    def test_pydantic_style_model_dump_on_payload(self):
        """When no result/split/segments key, fall back to dumping payload."""

        class _PydLike:
            def model_dump(self):
                return {"top-level": True, "sections": []}

        out = _split._extract_result(_PydLike())
        assert json.loads(out) == {"top-level": True, "sections": []}

    def test_plain_dict_passthrough_when_no_known_key(self):
        """A bare dict with no recognized envelope key should be returned as-is."""
        payload = {"job_id": "abc", "other": "data"}
        out = _split._extract_result(payload)
        assert json.loads(out) == payload

    def test_pydantic_style_dump_inside_envelope(self):
        class _PydLike:
            def model_dump(self):
                return {"nested": "value"}

        out = _split._extract_result({"result": _PydLike()})
        assert json.loads(out) == {"nested": "value"}
