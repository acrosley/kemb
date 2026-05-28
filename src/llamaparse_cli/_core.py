#!/usr/bin/env python3
"""llamaparse CLI — subcommand dispatcher.

Subcommands:
    parse     — convert a document to markdown/text (the original behaviour)
    extract   — pull structured JSON out of a document against a schema
    classify  — categorize a document into one of a defined set of classes
    split     — break a document into sections (by category or strategy)
    probe     — recursively scan a directory and report file metadata
    inspect   — content-aware preview (page counts, scans, snippets)
    doctor    — preflight checks (Python, deps, API key, reachability)

Backward compatible: `llamaparse ./file.pdf [--tier ...]` (no subcommand) still
works and is dispatched as `parse`.

API key auth: every subcommand reads LLAMA_CLOUD_API_KEY from the environment.
Get a key at https://cloud.llamaindex.ai/api-key.
"""
from __future__ import annotations

import argparse
import sys
from importlib.metadata import PackageNotFoundError, version as _pkg_version

from . import _classify, _doctor, _extract, _inspect, _parse, _probe, _split

try:
    __version__ = _pkg_version("llamaparse-cli")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

SUBCOMMANDS = ("parse", "extract", "classify", "split", "probe", "inspect", "doctor")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="llamaparse",
        description=(
            "Run LlamaCloud document operations (parse / extract / classify / "
            "split) from the command line. Each subcommand has its own --help."
        ),
        epilog=(
            "Examples:\n"
            "  llamaparse parse ./contract.pdf --tier agentic\n"
            "  llamaparse extract ./invoice.pdf --schema @invoice_schema.json\n"
            "  llamaparse classify ./doc.pdf --rules @rules.json\n"
            "  llamaparse split ./report.pdf --categories @cats.json\n"
            "  llamaparse probe ./inbox                           # scan dir metadata\n"
            "  llamaparse inspect ./inbox --snippet 200           # peek at content\n"
            "  llamaparse parse ./contract.pdf --dry-run          # validate without uploading\n"
            "  llamaparse doctor                                  # preflight checks\n"
            "\n"
            "For backward compatibility, `llamaparse <file> ...` (no\n"
            "subcommand) is treated as `llamaparse parse <file> ...`.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    subparsers = p.add_subparsers(dest="command", metavar="<command>")
    _parse.add_subparser(subparsers)
    _extract.add_subparser(subparsers)
    _classify.add_subparser(subparsers)
    _split.add_subparser(subparsers)
    _probe.add_subparser(subparsers)
    _inspect.add_subparser(subparsers)
    _doctor.add_subparser(subparsers)
    return p


def _normalize_argv(argv):
    """Insert `parse` if the user invoked the legacy form `llamaparse <file>`."""
    if not argv:
        return argv
    first = argv[0]
    if first in SUBCOMMANDS or first in ("-h", "--help"):
        return argv
    if first.startswith("-"):
        return argv
    return ["parse", *argv]


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    argv = _normalize_argv(argv)

    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, "func", None):
        parser.print_help(sys.stderr)
        return 2
    return args.func(args) or 0


if __name__ == "__main__":
    raise SystemExit(main())


# Public surface kept stable for callers that imported the old helpers.
parse_with_sdk = _parse.parse_with_sdk
parse_with_rest = _parse.parse_with_rest
strip_noise = _parse.strip_noise
