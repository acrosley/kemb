"""llamaparse-cli — thin wrapper around LlamaCloud document APIs.

Subcommands: parse, extract, classify, split. Each shares the same auth and
SDK-with-REST-fallback pattern; the per-feature implementations live in
sibling modules so callers can import a single capability without paying for
the others.
"""
from __future__ import annotations

from ._core import __version__, main
from ._parse import parse_with_sdk, parse_with_rest, strip_noise
from ._extract import extract_with_sdk, extract_with_rest
from ._classify import classify_with_sdk, classify_with_rest
from ._split import split_with_sdk, split_with_rest

__all__ = [
    "__version__",
    "main",
    "parse_with_sdk",
    "parse_with_rest",
    "strip_noise",
    "extract_with_sdk",
    "extract_with_rest",
    "classify_with_sdk",
    "classify_with_rest",
    "split_with_sdk",
    "split_with_rest",
]
