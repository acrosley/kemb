"""Tests for the top-level argparse dispatcher in ``_core``."""
from __future__ import annotations

import pytest

from kemb import _core


# ---------------------------------------------------------------------------
# _normalize_argv
# ---------------------------------------------------------------------------


class TestNormalizeArgv:
    def test_empty_argv_passes_through(self):
        assert _core._normalize_argv([]) == []

    @pytest.mark.parametrize("flag", ["-h", "--help"])
    def test_help_flags_pass_through(self, flag):
        assert _core._normalize_argv([flag]) == [flag]

    @pytest.mark.parametrize("cmd", ["parse", "classify"])
    def test_explicit_subcommand_passes_through(self, cmd):
        assert _core._normalize_argv([cmd, "./file.pdf"]) == [cmd, "./file.pdf"]

    def test_legacy_positional_file_gets_parse_prefix(self):
        """Bare `<file>` argv should be dispatched as `parse <file>`."""
        assert _core._normalize_argv(["./contract.pdf"]) == ["parse", "./contract.pdf"]

    def test_legacy_positional_with_flags(self):
        argv = ["./contract.pdf", "--tier", "agentic"]
        assert _core._normalize_argv(argv) == ["parse", "./contract.pdf", "--tier", "agentic"]

    def test_leading_flag_is_left_alone(self):
        """A leading `-x` shouldn't trick us into prepending `parse`."""
        assert _core._normalize_argv(["--version"]) == ["--version"]


# ---------------------------------------------------------------------------
# build_parser
# ---------------------------------------------------------------------------


class TestBuildParser:
    def test_returns_argument_parser(self):
        import argparse

        parser = _core.build_parser()
        assert isinstance(parser, argparse.ArgumentParser)
        assert parser.prog == "kemb"

    def test_all_subcommands_registered(self):
        """parse / classify must all be selectable subcommands."""
        parser = _core.build_parser()

        choices = None
        for action in parser._actions:
            if getattr(action, "choices", None) and "parse" in action.choices:
                choices = action.choices
                break

        assert choices is not None, "no subparser action found"
        for cmd in ("parse", "classify"):
            assert cmd in choices, f"{cmd!r} subparser missing"


class TestAutoInstallAcceptedEverywhere:
    """The skill shim passes --auto-install on every facet (and consumes it
    itself to bootstrap a relocated install), so every subcommand must accept
    the flag — meaningfully on parse/classify, as a no-op on probe/doctor.
    Otherwise the run dies with `unrecognized arguments` right after the
    shim's bootstrap succeeds."""

    @pytest.mark.parametrize("argv", [
        ["parse", "./file.pdf", "--auto-install"],
        ["classify", "./file.pdf", "--auto-install"],
        ["probe", ".", "--auto-install"],
        ["doctor", "--offline", "--auto-install"],
    ])
    def test_subcommand_accepts_auto_install(self, argv):
        parser = _core.build_parser()
        args = parser.parse_args(argv)  # SystemExit(2) here means rejection
        assert args.command == argv[0]
        assert args.auto_install is True


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------


class TestMainHelp:
    """``kemb <cmd> --help`` should exit with code 0 for every subcommand."""

    @pytest.mark.parametrize("cmd", ["parse", "classify"])
    def test_subcommand_help_exits_cleanly(self, cmd, capsys):
        with pytest.raises(SystemExit) as exc_info:
            _core.main([cmd, "--help"])
        # argparse exits with 0 on --help
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        # Help output should mention the subcommand or its argparse "usage:" prefix
        assert "usage" in captured.out.lower()

    def test_top_level_help_exits_cleanly(self):
        with pytest.raises(SystemExit) as exc_info:
            _core.main(["--help"])
        assert exc_info.value.code == 0

    def test_empty_argv_prints_help_and_returns_2(self, capsys):
        """No args / no subcommand → print help to stderr and return 2."""
        rc = _core.main([])
        assert rc == 2
        captured = capsys.readouterr()
        assert "usage" in captured.err.lower()


class TestVersionFlag:
    """``kemb --version`` / ``-V`` should print the package version and exit 0."""

    @pytest.mark.parametrize("flag", ["--version", "-V"])
    def test_version_flag_prints_and_exits_cleanly(self, flag, capsys):
        with pytest.raises(SystemExit) as exc_info:
            _core.main([flag])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        # argparse's version action writes "<prog> <version>" to stdout
        assert captured.out.startswith("kemb ")
        assert _core.__version__ in captured.out
