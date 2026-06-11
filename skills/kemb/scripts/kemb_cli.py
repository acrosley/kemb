#!/usr/bin/env python3
"""Skill entry point. Forwards to the kemb CLI dispatcher.

The real logic lives in `src/kemb/_core.py` at the repo root. This shim
keeps every invocation path working with the same code:

- Skill (in-repo): Claude runs `python scripts/kemb_cli.py <args>` from this
  skill dir. The shim adds `<repo>/src` to sys.path and calls `kemb._core`.
- Skill (relocated): marketplace installs and snapshots copy the skill dir
  outside the repo, so the relative guess misses. The shim falls back to an
  installed `kemb` package; with --auto-install it pip-installs kemb from
  GitHub the same way the CLI auto-installs llama-cloud.
- CLI: `pipx install git+https://github.com/acrosley/kemb` creates a `kemb`
  command on PATH that calls into the same module.
"""
from __future__ import annotations

import importlib
import subprocess
import sys
from pathlib import Path

GITHUB_SPEC = "git+https://github.com/acrosley/kemb"


def _try_import():
    try:
        from kemb._core import main as _main  # type: ignore
        return _main
    except ImportError:
        return None


def _try_install_kemb() -> bool:
    """Best-effort pip install of kemb from GitHub, mirroring the CLI's
    llama-cloud auto-install (`kemb._common.try_install_sdk`): plain install
    first, then retry with --break-system-packages for PEP 668 "externally
    managed" environments. On total failure, prints the last attempt's output
    to stderr so the user can see *why* rather than just the fallout.
    """
    cmds = [
        [sys.executable, "-m", "pip", "install", "--quiet", GITHUB_SPEC],
        [sys.executable, "-m", "pip", "install", "--quiet",
         "--break-system-packages", GITHUB_SPEC],
    ]
    last_output = ""
    for cmd in cmds:
        try:
            proc = subprocess.run(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True,
            )
        except OSError as e:
            last_output = str(e)
            continue
        if proc.returncode == 0:
            return True
        last_output = (proc.stdout or "").strip()
    tail = last_output[-500:] if last_output else "(no output captured)"
    print(f"note: pip install {GITHUB_SPEC} failed: {tail}", file=sys.stderr)
    return False


def _import_core():
    main = _try_import()  # already-installed kemb (pip / pipx / editable)
    if main:
        return main

    # In a repo checkout the shim sits at skills/kemb/scripts/, so the package
    # source is three levels up. Relocated copies land at arbitrary (possibly
    # shallow) depths, so treat the guess as best-effort.
    parents = Path(__file__).resolve().parents
    if len(parents) > 3:
        repo_src = parents[3] / "src"
        if repo_src.is_dir() and str(repo_src) not in sys.path:
            sys.path.insert(0, str(repo_src))
            main = _try_import()
            if main:
                return main

    if "--auto-install" in sys.argv[1:]:
        print(f"note: kemb not importable; attempting pip install {GITHUB_SPEC}...",
              file=sys.stderr)
        if _try_install_kemb():
            importlib.invalidate_caches()  # see packages added mid-process
            main = _try_import()
            if main:
                return main

    print(
        "error: kemb is not importable (the shim is outside its repo and no "
        "installed package was found); rerun with --auto-install or run: "
        f"pip install {GITHUB_SPEC}",
        file=sys.stderr,
    )
    return None


if __name__ == "__main__":
    _main = _import_core()
    raise SystemExit(2 if _main is None else _main())
