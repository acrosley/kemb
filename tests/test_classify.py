"""Tests for ``_classify``: rules normalization, configuration, result parsing."""
from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from llamaparse_cli import _classify


# ---------------------------------------------------------------------------
# _normalize_rules
# ---------------------------------------------------------------------------


class TestNormalizeRules:
    def test_none_returns_none(self):
        assert _classify._normalize_rules(None) is None

    def test_valid_inline_json_list(self):
        rules = '[{"type":"contract","description":"a legal agreement"}]'
        result = _classify._normalize_rules(rules)
        assert result == [{"type": "contract", "description": "a legal agreement"}]

    def test_at_file_reference(self, tmp_path: Path):
        p = tmp_path / "rules.json"
        p.write_text(
            json.dumps([{"type": "invoice", "description": "bill"}]),
            encoding="utf-8",
        )
        assert _classify._normalize_rules(f"@{p}") == [
            {"type": "invoice", "description": "bill"}
        ]

    def test_invalid_json_exits(self):
        with pytest.raises(SystemExit):
            _classify._normalize_rules("{not valid json")

    def test_non_list_exits(self):
        """`--rules` must be an array, not an object."""
        with pytest.raises(SystemExit):
            _classify._normalize_rules('{"type": "x", "description": "y"}')

    def test_missing_type_key_exits(self):
        with pytest.raises(SystemExit):
            _classify._normalize_rules('[{"description": "only desc"}]')

    def test_missing_description_key_exits(self):
        with pytest.raises(SystemExit):
            _classify._normalize_rules('[{"type": "only-type"}]')

    def test_rule_not_dict_exits(self):
        with pytest.raises(SystemExit):
            _classify._normalize_rules('["not-an-object"]')

    def test_at_file_missing_exits(self, tmp_path: Path):
        with pytest.raises(SystemExit):
            _classify._normalize_rules(f"@{tmp_path}/missing.json")


# ---------------------------------------------------------------------------
# _build_configuration
# ---------------------------------------------------------------------------


class TestBuildConfiguration:
    def test_rules_required(self):
        with pytest.raises(SystemExit):
            _classify._build_configuration(None, None, None)

    def test_rules_passed_through(self):
        rules = [{"type": "a", "description": "x"}]
        cfg = _classify._build_configuration(rules, None, None)
        assert cfg == {"rules": rules}

    def test_mode_added_when_specified(self):
        rules = [{"type": "a", "description": "x"}]
        cfg = _classify._build_configuration(rules, None, "fast")
        assert cfg == {"rules": rules, "mode": "fast"}

    def test_mode_not_overwritten(self):
        rules = [{"type": "a", "description": "x"}]
        existing = {"rules": rules, "mode": "multimodal"}
        cfg = _classify._build_configuration(None, existing, "fast")
        assert cfg["mode"] == "multimodal"

    def test_empty_rules_list_in_config_still_exits(self):
        """Empty list counts as no rules → error."""
        with pytest.raises(SystemExit):
            _classify._build_configuration(None, {"rules": []}, None)


# ---------------------------------------------------------------------------
# _extract_result
# ---------------------------------------------------------------------------


class TestExtractResult:
    def test_dict_with_result_key(self):
        out = _classify._extract_result(
            {"result": {"type": "invoice", "confidence": 0.9}}
        )
        assert json.loads(out) == {"type": "invoice", "confidence": 0.9}

    def test_dict_with_classification_key(self):
        out = _classify._extract_result(
            {"classification": {"type": "contract", "confidence": 0.7}}
        )
        assert json.loads(out) == {"type": "contract", "confidence": 0.7}

    def test_top_level_type_and_confidence(self):
        """When the response IS the result, accept it directly."""
        payload = {"type": "invoice", "confidence": 0.8, "reasoning": "headers"}
        out = _classify._extract_result(payload)
        assert json.loads(out) == payload

    def test_object_with_result_attribute(self):
        obj = SimpleNamespace(result={"type": "x", "confidence": 1.0})
        assert json.loads(_classify._extract_result(obj)) == {
            "type": "x",
            "confidence": 1.0,
        }

    def test_pydantic_style_model_dump(self):
        class _PydLike:
            def model_dump(self):
                return {"type": "y", "confidence": 0.5}

        out = _classify._extract_result({"result": _PydLike()})
        assert json.loads(out) == {"type": "y", "confidence": 0.5}

    def test_missing_result_exits(self):
        with pytest.raises(SystemExit):
            _classify._extract_result({"status": "COMPLETED"})
