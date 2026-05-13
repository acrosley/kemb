"""Tests for ``_parse``: noise stripping and REST response shape extraction."""
from __future__ import annotations

import pytest

from llamaparse_cli import _parse


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
