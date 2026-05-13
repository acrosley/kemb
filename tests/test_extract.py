"""Tests for ``_extract``: configuration building and result envelope parsing."""
from __future__ import annotations

import json
from types import SimpleNamespace

import pytest

from llamaparse_cli import _extract


# ---------------------------------------------------------------------------
# _build_configuration
# ---------------------------------------------------------------------------


class TestBuildConfiguration:
    def test_schema_injected_as_data_schema(self):
        schema = {"type": "object", "properties": {"a": {"type": "string"}}}
        cfg = _extract._build_configuration(schema, None, None)
        assert cfg == {"data_schema": schema}

    def test_existing_configuration_not_overwritten(self):
        """`coerce_json_arg` returns a configuration dict; if it already has a
        `data_schema`, --schema should not replace it (setdefault semantics)."""
        existing = {"data_schema": {"existing": True}, "extra": "keep"}
        cfg = _extract._build_configuration(
            schema={"new": True}, configuration=existing, configuration_id=None
        )
        assert cfg == {"data_schema": {"existing": True}, "extra": "keep"}

    def test_missing_schema_and_no_id_exits(self):
        with pytest.raises(SystemExit):
            _extract._build_configuration(None, None, None)

    def test_missing_schema_with_non_schema_config_exits(self):
        """A configuration without `data_schema` should still error out."""
        with pytest.raises(SystemExit):
            _extract._build_configuration(None, {"unrelated": "value"}, None)

    def test_configuration_id_short_circuits(self):
        """When configuration_id is supplied, schema is not required."""
        assert _extract._build_configuration(None, None, "cfg-123") == {}
        # Even with a schema, the id path returns an empty cfg.
        assert _extract._build_configuration({"x": 1}, None, "cfg-123") == {}


# ---------------------------------------------------------------------------
# _extract_data
# ---------------------------------------------------------------------------


class TestExtractData:
    def test_dict_with_data_key(self):
        result = _extract._extract_data({"data": {"name": "Acme", "n": 1}})
        assert json.loads(result) == {"name": "Acme", "n": 1}

    def test_dict_with_extract_key(self):
        result = _extract._extract_data({"extract": {"x": 1}})
        assert json.loads(result) == {"x": 1}

    def test_object_with_data_attribute(self):
        obj = SimpleNamespace(data={"foo": "bar"})
        assert json.loads(_extract._extract_data(obj)) == {"foo": "bar"}

    def test_object_with_extract_attribute(self):
        obj = SimpleNamespace(extract={"baz": 42}, data=None)
        assert json.loads(_extract._extract_data(obj)) == {"baz": 42}

    def test_pydantic_style_model_dump(self):
        """When .data is a pydantic-style object exposing model_dump(), use it."""

        class _PydLike:
            def model_dump(self):
                return {"from": "model_dump"}

        result = _extract._extract_data({"data": _PydLike()})
        assert json.loads(result) == {"from": "model_dump"}

    def test_nested_in_job_envelope(self):
        """`payload.job.data` (REST poll-final shape) should be picked up."""
        result = _extract._extract_data(
            {"job": {"data": {"nested": True}}, "status": "COMPLETED"}
        )
        assert json.loads(result) == {"nested": True}

    def test_missing_data_exits(self):
        with pytest.raises(SystemExit):
            _extract._extract_data({"status": "COMPLETED"})
