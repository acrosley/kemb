#!/usr/bin/env python3
"""Skill entry point. Forwards to the kemb CLI dispatcher.

The real logic lives in `src/kemb/_core.py` at the repo root. This shim
keeps both invocation paths working with the same code:

- Skill: Claude runs `python scripts/kemb_cli.py <args>` from this skill dir.
  The shim adds `<repo>/src` to sys.path and calls into `kemb._core`.
- CLI: `pipx install git+https://github.com/acrosley/kemb` creates a `kemb`
  command on PATH that calls into the same module.
"""
from __future__ import annotations

import sys
from pathlib import Path


def _import_core():
    try:
        from kemb._core import main as _main
        return _main
    except ImportError:
        pass
    repo_src = Path(__file__).resolve().parents[3] / "src"
    if repo_src.is_dir() and str(repo_src) not in sys.path:
        sys.path.insert(0, str(repo_src))
    from kemb._core import main as _main  # type: ignore
    return _main


if __name__ == "__main__":
    raise SystemExit(_import_core()())
