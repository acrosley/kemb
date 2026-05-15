"""Extractor registry: maps extractor names + doc_types to Extractor instances.

The chain for each doc_type comes from config/doc_types.yaml. New extractors
register themselves here so the L3 routing logic doesn't need to know they
exist.
"""
from __future__ import annotations

from pathlib import Path
from typing import Type

import yaml

from doc_backbone.extractors.base import Extractor
from doc_backbone.extractors.native_pdf import NativePdfExtractor

_EXTRACTORS: dict[str, Type[Extractor]] = {
    NativePdfExtractor.name: NativePdfExtractor,
}


def available_extractors() -> list[str]:
    return sorted(_EXTRACTORS)


def get_extractor(name: str) -> Extractor:
    try:
        return _EXTRACTORS[name]()
    except KeyError as e:
        raise KeyError(
            f"unknown extractor {name!r}; available: {available_extractors()}"
        ) from e


def load_doc_types_config(config_path: Path) -> dict:
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def chain_for(doc_type: str, config: dict) -> list[str]:
    """Return the ordered extractor chain for a doc_type, falling back to the
    configured default_doc_type when the type is unknown."""
    types = config.get("doc_types", {})
    default = config.get("default_doc_type", "unknown")
    spec = types.get(doc_type) or types.get(default) or {"extractors": ["native_pdf"]}
    return list(spec.get("extractors", []))
