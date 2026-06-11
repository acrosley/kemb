"""Test the skill shim's package resolution across invocation contexts.

`skills/kemb/scripts/kemb_cli.py` must find the kemb package three different
ways: `<repo>/src` when run from the repo checkout (the `parents[3]` depth is
brittle, so prove it resolves), an installed `kemb` package when the skill dir
has been copied outside the repo (marketplace installs, snapshots), and a pip
install from GitHub when --auto-install is passed and neither is present.
Every test runs the shim in a subprocess with a controlled PYTHONPATH so the
resolution under test is the only one that can succeed.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SHIM = REPO_ROOT / "skills" / "kemb" / "scripts" / "kemb_cli.py"
GITHUB_SPEC = "git+https://github.com/acrosley/kemb"


def _run_shim(shim, cwd, pythonpath=None, args=("--version",)):
    """Run a shim copy in a subprocess. PYTHONPATH is stripped unless the
    test supplies one, so an ambient editable install can't leak in."""
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    if pythonpath is not None:
        env["PYTHONPATH"] = str(pythonpath)
    return subprocess.run(
        [sys.executable, str(shim), *args],
        cwd=str(cwd),
        env=env,
        capture_output=True,
        text=True,
    )


def _relocate_shim(tmp_path):
    """Copy the shim outside the repo, as a marketplace install would. The
    copy's `parents[3]/src` points into pytest's tmp tree, so the repo-relative
    guess is guaranteed to miss."""
    scripts = tmp_path / "skill-copy" / "scripts"
    scripts.mkdir(parents=True)
    return Path(shutil.copy2(SHIM, scripts / "kemb_cli.py"))


def _make_shadow_kemb(tmp_path):
    """A `kemb` package with no `_core`, for putting on PYTHONPATH. It shadows
    any real kemb in the test interpreter's site-packages, making the
    'no usable package anywhere' case deterministic."""
    shadow = tmp_path / "shadow"
    (shadow / "kemb").mkdir(parents=True)
    (shadow / "kemb" / "__init__.py").write_text("", encoding="utf-8")
    return shadow


def test_shim_resolves_src_without_installed_package(tmp_path):
    """Run the in-repo shim from an unrelated cwd with PYTHONPATH stripped; it
    must find `<repo>/src` on its own and print the version. If `kemb` isn't
    already importable, the `parents[3]/src` insertion is the only thing that
    can make this succeed — so a green run proves that resolution works."""
    proc = _run_shim(SHIM, tmp_path)
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip().startswith("kemb ")


def test_relocated_shim_falls_back_to_installed_package(tmp_path):
    """When the skill dir is copied outside the repo, the relative src/ guess
    misses but an installed `kemb` must still be found. Simulate the installed
    package by putting `<repo>/src` on PYTHONPATH — importable without any
    help from the shim, exactly like site-packages would be."""
    shim = _relocate_shim(tmp_path)
    proc = _run_shim(shim, tmp_path, pythonpath=REPO_ROOT / "src")
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip().startswith("kemb ")


def test_relocated_shim_exits_with_remedy_message(tmp_path):
    """No repo, no installed package, no --auto-install: the shim must exit 2
    with a one-line remedy naming both fixes — not an ImportError traceback."""
    shim = _relocate_shim(tmp_path)
    proc = _run_shim(shim, tmp_path, pythonpath=_make_shadow_kemb(tmp_path))
    assert proc.returncode == 2
    assert "Traceback" not in proc.stderr
    lines = proc.stderr.strip().splitlines()
    assert len(lines) == 1, proc.stderr
    assert lines[0].startswith("error:")
    assert "--auto-install" in lines[0]
    assert f"pip install {GITHUB_SPEC}" in lines[0]


def test_relocated_shim_auto_installs_from_github(tmp_path):
    """With --auto-install and no package anywhere, the shim must pip-install
    kemb from GitHub and then import it. Stub `pip` on PYTHONPATH (shadowing
    the real one for `python -m pip`): the stub records its argv and
    'installs' kemb by materializing `_core.py` inside the shadow package, so
    the real install-then-retry-import path runs without touching the
    network."""
    shim = _relocate_shim(tmp_path)
    shadow = _make_shadow_kemb(tmp_path)
    pip_stub = shadow / "pip"
    pip_stub.mkdir()
    (pip_stub / "__init__.py").write_text("", encoding="utf-8")
    (pip_stub / "__main__.py").write_text(
        "import sys\n"
        "from pathlib import Path\n"
        "shadow = Path(__file__).resolve().parents[1]\n"
        "(shadow / 'pip_argv.txt').write_text("
        "' '.join(sys.argv[1:]), encoding='utf-8')\n"
        f"if sys.argv[-1] != {GITHUB_SPEC!r}:\n"
        "    sys.exit(1)\n"
        "(shadow / 'kemb' / '_core.py').write_text(\n"
        "    'def main():\\n    print(\"kemb-fake-installed\")\\n"
        "    return 0\\n',\n"
        "    encoding='utf-8')\n"
        "sys.exit(0)\n",
        encoding="utf-8",
    )
    proc = _run_shim(shim, tmp_path, pythonpath=shadow,
                     args=("--auto-install",))
    assert proc.returncode == 0, proc.stderr
    assert "kemb-fake-installed" in proc.stdout
    # Installed with the same shape as the llama-cloud auto-install, from the
    # canonical GitHub spec.
    argv = (shadow / "pip_argv.txt").read_text(encoding="utf-8")
    assert argv == f"install --quiet {GITHUB_SPEC}"


def test_relocated_shim_auto_install_failure_still_gives_remedy(tmp_path):
    """If the pip install itself fails, the shim must surface pip's output as
    a note and still end on the one-line remedy with exit 2."""
    shim = _relocate_shim(tmp_path)
    shadow = _make_shadow_kemb(tmp_path)
    pip_stub = shadow / "pip"
    pip_stub.mkdir()
    (pip_stub / "__init__.py").write_text("", encoding="utf-8")
    (pip_stub / "__main__.py").write_text(
        "import sys\n"
        "print('No matching distribution found (stub)')\n"
        "sys.exit(1)\n",
        encoding="utf-8",
    )
    proc = _run_shim(shim, tmp_path, pythonpath=shadow,
                     args=("--auto-install",))
    assert proc.returncode == 2
    assert "No matching distribution found (stub)" in proc.stderr
    assert f"pip install {GITHUB_SPEC}" in proc.stderr.strip().splitlines()[-1]
