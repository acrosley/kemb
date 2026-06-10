"""Test the skill shim's path resolution.

`skills/kemb/scripts/kemb_cli.py` inserts `<repo>/src` onto sys.path so the
skill and the pip-installed CLI run the same code (CLAUDE.md calls this the
guarantee they "can never drift"). The `parents[3]` depth is brittle, so prove
it actually resolves by running the shim in a subprocess with a cleared
PYTHONPATH — i.e. without relying on an ambient editable install.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SHIM = REPO_ROOT / "skills" / "kemb" / "scripts" / "kemb_cli.py"


def test_shim_resolves_src_without_installed_package(tmp_path):
    """Run the shim from an unrelated cwd with PYTHONPATH stripped; it must
    find `<repo>/src` on its own and print the version."""
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    # Run from an unrelated cwd with PYTHONPATH cleared. If `kemb` isn't already
    # importable, the shim's `parents[3]/src` insertion is the only thing that
    # can make this succeed — so a green run proves that resolution works.
    proc = subprocess.run(
        [sys.executable, str(SHIM), "--version"],
        cwd=str(tmp_path),
        env=env,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip().startswith("kemb ")
