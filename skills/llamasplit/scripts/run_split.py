#!/usr/bin/env python3
"""Skill entry point for LlamaSplit — forwards to the shared CLI dispatcher.

The real logic lives in `src/llamaparse_cli/_split.py` at the repo root.
This shim just calls into `llamaparse_cli` with `split` as the subcommand.
"""
from __future__ import annotations

import sys
from pathlib import Path


def _import_main():
    try:
        from llamaparse_cli import main as _main
        return _main
    except ImportError:
        pass
    repo_src = Path(__file__).resolve().parents[3] / "src"
    if repo_src.is_dir() and str(repo_src) not in sys.path:
        sys.path.insert(0, str(repo_src))
    from llamaparse_cli import main as _main  # type: ignore
    return _main


if __name__ == "__main__":
    raise SystemExit(_import_main()(["split", *sys.argv[1:]]))
