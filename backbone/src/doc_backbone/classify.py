"""L2 - Doc-type classification.

Stub. Future: small classifier over fingerprint + first-N-pages text + filename
hints. Falls back to an LLM zero-shot classifier below a confidence threshold.
In v0 everything is `doc_type = "unknown"`.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any


def classify(pdf_path: Path, fingerprint: dict[str, Any]) -> tuple[str, float, dict[str, Any]]:
    """Return (doc_type, confidence, evidence)."""
    raise NotImplementedError("Layer 2 (classify): not implemented in v0 spine")


def default_doc_type() -> str:
    return "unknown"
