"""L1 - Triage / fingerprinting.

Stub. Future: cheap per-PDF probe that records page count, text-vs-image
ratio, embedded font count, presence of form fields, and a scan-quality
estimate. Output feeds the L2 classifier and the L4 arbiter.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any


def fingerprint(pdf_path: Path) -> dict[str, Any]:
    """Return a small JSON-able fingerprint for the PDF."""
    raise NotImplementedError("Layer 1 (triage): not implemented in v0 spine")
