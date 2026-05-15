"""L4 - Quality scoring + extractor arbitration.

Stub. Future: scores each CIR on text density, heading-hierarchy coherence,
table-cell completeness, and average per-block confidence. If a CIR's score
falls below the doc_type's threshold, the arbiter escalates to the next
extractor in the chain.
"""
from __future__ import annotations

from doc_backbone.cir import CIR


def score(cir: CIR) -> float:
    """Return a 0..1 quality score for the CIR."""
    raise NotImplementedError("Layer 4 (score): not implemented in v0 spine")


def should_escalate(cir: CIR, threshold: float) -> bool:
    raise NotImplementedError("Layer 4 (arbitrate): not implemented in v0 spine")
