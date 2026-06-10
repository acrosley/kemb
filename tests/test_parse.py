"""Tests for ``_parse``: noise stripping and REST response shape extraction."""
from __future__ import annotations

import pytest

from kemb import _parse


# ---------------------------------------------------------------------------
# strip_noise
# ---------------------------------------------------------------------------


class TestStripNoise:
    def test_layout_comment_removed(self):
        text = (
            "Hello\n"
            "<!-- layout: header -->\n"
            "world\n"
        )
        out, layout_dropped, images_dropped = _parse.strip_noise(text)
        assert "<!-- layout:" not in out
        assert layout_dropped == 1
        assert images_dropped == 0
        assert "Hello" in out
        assert "world" in out

    def test_multiple_layout_comments_removed(self):
        text = (
            "<!-- layout: a -->\n"
            "Body\n"
            "<!-- layout: b -->\n"
            "<!-- layout: c -->\n"
        )
        out, layout_dropped, _ = _parse.strip_noise(text)
        assert layout_dropped == 3
        assert "<!-- layout:" not in out
        assert "Body" in out

    def test_no_layout_comments_no_drops(self):
        text = "Just some plain text\nwith no annotations."
        out, layout_dropped, images_dropped = _parse.strip_noise(text)
        assert out == text
        assert layout_dropped == 0
        assert images_dropped == 0

    def test_repeating_image_refs_dropped_at_threshold(self):
        """Image refs whose alt repeats >= repeat_threshold should be removed."""
        text = (
            "# Doc\n"
            "![Header Logo](images/page_1_image_1.png)\n"
            "page 1 body\n"
            "![Header Logo](images/page_2_image_1.png)\n"
            "page 2 body\n"
            "![Header Logo](images/page_3_image_1.png)\n"
            "page 3 body\n"
        )
        out, layout_dropped, images_dropped = _parse.strip_noise(text, repeat_threshold=3)
        assert layout_dropped == 0
        assert images_dropped == 3
        assert "Header Logo" not in out
        assert "page 1 body" in out
        assert "page 3 body" in out

    def test_non_repeating_image_refs_kept_below_threshold(self):
        """Image refs whose alt count < threshold must stay in place."""
        text = (
            "# Doc\n"
            "![Header Logo](images/page_1_image_1.png)\n"
            "page 1\n"
            "![Header Logo](images/page_2_image_1.png)\n"
            "page 2\n"
        )
        out, layout_dropped, images_dropped = _parse.strip_noise(text, repeat_threshold=3)
        # alt 'Header Logo' appears twice (< 3), so nothing dropped.
        assert images_dropped == 0
        assert out.count("Header Logo") == 2

    def test_distinct_alts_not_dropped(self):
        text = (
            "![Alpha](images/page_1_image_1.png)\n"
            "![Beta](images/page_2_image_1.png)\n"
            "![Gamma](images/page_3_image_1.png)\n"
        )
        out, _, images_dropped = _parse.strip_noise(text, repeat_threshold=3)
        assert images_dropped == 0
        assert "Alpha" in out
        assert "Beta" in out
        assert "Gamma" in out

    def test_threshold_one_drops_everything_recurring(self):
        text = (
            "![Banner](images/page_1_image_1.png)\n"
            "body\n"
            "![Banner](images/page_2_image_1.png)\n"
        )
        out, _, images_dropped = _parse.strip_noise(text, repeat_threshold=2)
        assert images_dropped == 2
        assert "Banner" not in out


# ---------------------------------------------------------------------------
# _extract_rest_field
# ---------------------------------------------------------------------------


class TestExtractRestField:
    def test_top_level_string(self):
        payload = {"markdown": "# Hello world"}
        assert _parse._extract_rest_field(payload, "markdown") == "# Hello world"

    def test_top_level_string_text_field(self):
        payload = {"text": "plain text body"}
        assert _parse._extract_rest_field(payload, "text") == "plain text body"

    def test_nested_dict_with_same_key(self):
        """When markdown is a dict, look inside for the same key."""
        payload = {"markdown": {"markdown": "# Inner"}}
        assert _parse._extract_rest_field(payload, "markdown") == "# Inner"

    def test_nested_dict_with_pages_joined(self):
        payload = {
            "markdown": {
                "pages": [
                    {"markdown": "page one"},
                    {"markdown": "page two"},
                    {"markdown": "page three"},
                ]
            }
        }
        result = _parse._extract_rest_field(payload, "markdown")
        assert result == "page one\n\npage two\n\npage three"

    def test_nested_pages_skips_failed(self):
        payload = {
            "markdown": {
                "pages": [
                    {"markdown": "good"},
                    {"markdown": "skip-me", "success": False},
                    {"markdown": "also good"},
                ]
            }
        }
        result = _parse._extract_rest_field(payload, "markdown")
        assert "skip-me" not in result
        assert "good" in result
        assert "also good" in result

    def test_nested_pages_skips_non_string_entries(self):
        payload = {
            "markdown": {
                "pages": [
                    {"markdown": "valid"},
                    {"markdown": None},
                    "not-a-dict",
                ]
            }
        }
        result = _parse._extract_rest_field(payload, "markdown")
        assert result == "valid"

    def test_markdown_full_fallback(self):
        """When the primary shape is missing, fall back to `<key>_full`."""
        payload = {"markdown_full": "complete body here"}
        assert _parse._extract_rest_field(payload, "markdown") == "complete body here"

    def test_text_full_fallback(self):
        payload = {"text_full": "plain body"}
        assert _parse._extract_rest_field(payload, "text") == "plain body"

    def test_returns_none_when_nothing_matches(self):
        assert _parse._extract_rest_field({"other": "data"}, "markdown") is None

    def test_returns_none_for_non_dict_input(self):
        assert _parse._extract_rest_field("a string", "markdown") is None
        assert _parse._extract_rest_field(None, "markdown") is None

    def test_empty_markdown_full_treated_as_missing(self):
        """An empty `<key>_full` should NOT be returned as the result."""
        payload = {"markdown_full": ""}
        assert _parse._extract_rest_field(payload, "markdown") is None


# ---------------------------------------------------------------------------
# run() — FAST tier compatibility
# ---------------------------------------------------------------------------


class TestRunFastTier:
    """FAST tier can't expand markdown; the CLI should transparently fetch text."""

    def _make_args(self, tmp_path, **overrides):
        import argparse

        input_file = tmp_path / "doc.pdf"
        input_file.write_bytes(b"%PDF-1.4 stub")
        defaults = dict(
            input=input_file,
            output=None,
            result_type="markdown",
            tier="fast",
            version="latest",
            strip_noise=False,
            rest=True,  # avoid SDK import path
            poll_timeout=600.0,
            auto_install=False,
            stdout=False,
            dry_run=False,
        )
        defaults.update(overrides)
        return argparse.Namespace(**defaults)

    def test_fast_with_markdown_default_fetches_text(self, tmp_path, monkeypatch, capsys):
        """FAST + default markdown should auto-fallback to text and warn."""
        captured_calls = {}

        def fake_rest(input_path, result_type, tier, version, poll_timeout):
            captured_calls["result_type"] = result_type
            captured_calls["tier"] = tier
            return "extracted plain text"

        monkeypatch.setattr(_parse, "parse_with_rest", fake_rest)

        args = self._make_args(tmp_path)
        rc = _parse.run(args)

        assert rc == 0
        # The fetcher must be called with text, not markdown.
        assert captured_calls["result_type"] == "text"
        assert captured_calls["tier"] == "fast"
        # Output extension still respects the user's intent (markdown → .md).
        assert (tmp_path / "doc.md").read_text(encoding="utf-8") == "extracted plain text"
        # Note explaining the fallback should be on stderr.
        assert "FAST tier" in capsys.readouterr().err

    def test_fast_with_explicit_text_unchanged(self, tmp_path, monkeypatch, capsys):
        """FAST + explicit text should pass through with no warning."""
        captured_calls = {}

        def fake_rest(input_path, result_type, tier, version, poll_timeout):
            captured_calls["result_type"] = result_type
            return "plain"

        monkeypatch.setattr(_parse, "parse_with_rest", fake_rest)

        args = self._make_args(tmp_path, result_type="text")
        rc = _parse.run(args)

        assert rc == 0
        assert captured_calls["result_type"] == "text"
        assert (tmp_path / "doc.txt").read_text(encoding="utf-8") == "plain"
        assert "FAST tier" not in capsys.readouterr().err

    def test_higher_tier_with_markdown_unchanged(self, tmp_path, monkeypatch, capsys):
        """Non-FAST tiers must still request markdown when asked."""
        captured_calls = {}

        def fake_rest(input_path, result_type, tier, version, poll_timeout):
            captured_calls["result_type"] = result_type
            captured_calls["tier"] = tier
            return "# Heading"

        monkeypatch.setattr(_parse, "parse_with_rest", fake_rest)

        args = self._make_args(tmp_path, tier="cost_effective")
        rc = _parse.run(args)

        assert rc == 0
        assert captured_calls["result_type"] == "markdown"
        assert captured_calls["tier"] == "cost_effective"
        assert "FAST tier" not in capsys.readouterr().err
