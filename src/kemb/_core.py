#!/usr/bin/env python3
"""kemb CLI — subcommand dispatcher.

Subcommands:
    parse     — convert a document to markdown/text (the original behaviour)
    classify  — categorize a document into one of a defined set of classes
    probe     — recursively scan a directory and report file metadata
    doctor    — preflight checks (Python, deps, API key, reachability)

Once `parse` has produced clean markdown, schema extraction and section
splitting are jobs for the consuming agent — Claude reads the markdown
directly, so those former facets carry no CLI surface here.

Backward compatible: `kemb ./file.pdf [--tier ...]` (no subcommand) still
works and is dispatched as `parse`.

API key auth: every subcommand reads LLAMA_CLOUD_API_KEY from the environment.
Get a key at https://cloud.llamaindex.ai/api-key.
"""
from __future__ import annotations

import argparse
import sys
from importlib.metadata import PackageNotFoundError, version as _pkg_version

from . import _classify, _doctor, _parse, _probe

try:
    __version__ = _pkg_version("kemb")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

SUBCOMMANDS = ("parse", "classify", "probe", "doctor")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="kemb",
        description=(
            "Run LlamaCloud document operations (parse / classify) and local "
            "corpus tools (probe / doctor) from the command line. Each "
            "subcommand has its own --help."
        ),
        epilog=(
            "Examples:\n"
            "  kemb parse ./contract.pdf --tier agentic\n"
            "  kemb classify ./doc.pdf --rules @rules.json\n"
            "  kemb probe ./inbox                           # scan dir metadata\n"
            "  kemb probe ./cases --sample                  # corpus triage sample\n"
            "  kemb parse ./contract.pdf --dry-run          # validate without uploading\n"
            "  kemb doctor                                  # preflight checks\n"
            "\n"
            "For backward compatibility, `kemb <file> ...` (no\n"
            "subcommand) is treated as `kemb parse <file> ...`.\n"
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
    _classify.add_subparser(subparsers)
    _probe.add_subparser(subparsers)
    _doctor.add_subparser(subparsers)
    return p


def _normalize_argv(argv):
    """Insert `parse` if the user invoked the legacy form `kemb <file>`."""
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
