#!/usr/bin/env python3
"""Skill entry point. Forwards to the package implementation.

This file is the canonical command the `llamaparse` skill invokes. To keep the
plugin and the standalone CLI in sync, the real logic lives in
`src/llamaparse_cli/_core.py` at the repo root. This shim makes sure both
invocation paths share the same code:

- Skill: Claude runs `python parse_document.py <args>` directly. The shim
  adds `<repo>/src` to sys.path and calls into `llamaparse_cli._core`.
- CLI: `pip install llamaparse-cli` (or `pip install
  git+https://github.com/acrosley/llamaparse-plugin`) creates a `llamaparse`
  command that calls into the same module.
"""
from __future__ import annotations

import sys
from pathlib import Path


def _import_core():
    try:
        from llamaparse_cli._core import main as _main
        return _main
    except ImportError:
        pass
    repo_src = Path(__file__).resolve().parents[3] / "src"
    if repo_src.is_dir() and str(repo_src) not in sys.path:
        sys.path.insert(0, str(repo_src))
    from llamaparse_cli._core import main as _main  # type: ignore
    return _main


if __name__ == "__main__":
    raise SystemExit(_import_core()())
