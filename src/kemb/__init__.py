"""kemb — corpus curation toolkit for agent-ready PDF libraries.

The kembing process: probe a corpus, plan a pass, execute, render into a
mirror. Single-document operations (parse, classify) remain as facets — each
shares auth and the SDK-with-REST-fallback pattern, and the per-feature
implementations live in sibling modules so callers can import a single
capability without paying for the others. Schema extraction and section
splitting are deliberately absent: once parse yields clean markdown, the
consuming agent does that work itself.
"""
from __future__ import annotations

from ._core import __version__, main
from ._parse import parse_with_sdk, parse_with_rest, strip_noise
from ._classify import classify_with_sdk, classify_with_rest
from ._probe import scan_directory, summarize

__all__ = [
    "__version__",
    "main",
    "parse_with_sdk",
    "parse_with_rest",
    "strip_noise",
    "classify_with_sdk",
    "classify_with_rest",
    "scan_directory",
    "summarize",
]
