"""Extractor contract.

All extractors (native_pdf, ocr_tesseract, marker, llamaparse_premium, ...)
implement this protocol so the renderer and arbitration layers never have to
know which one produced a given CIR.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from doc_backbone.cir import CIR


class Extractor(ABC):
    """A pluggable PDF -> CIR backend."""

    name: str = ""
    version: str = "0.0.0"

    @abstractmethod
    def extract(self, pdf_path: Path, *, source_hash: str, doc_type: str) -> CIR:
        """Parse pdf_path and return a CIR. Must populate `source_hash`,
        `source_path`, `doc_type`, `pages`, `extractor`, `extractor_version`."""
        raise NotImplementedError
