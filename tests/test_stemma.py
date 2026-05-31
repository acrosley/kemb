"""Tests for the provenance slice: ``stemma`` (build) and ``cite`` (resolve).

The offline path (``--from-parse-json``) is fully hermetic — no network, no
credits — and is what these tests exercise. A live parse is mocked at the
``fetch_parse_pages`` boundary to confirm wiring without hitting LlamaCloud.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from kemb import _cite, _core, _stemma

PAGES = [
    {
        "page": 1,
        "md": "# Title\n\nAlpha beta gamma delta.\n\nSecond block here.",
        "items": [
            {"md": "Title", "bBox": {"x": 10, "y": 10, "w": 100, "h": 20}},
            {"md": "Alpha beta gamma delta.",
             "bBox": {"x": 10, "y": 40, "w": 200, "h": 20}},
        ],
    },
    {
        "page": 2,
        "md": "Confidential information must be held in strict confidence.",
        "items": [
            {"md": "Confidential information must be held in strict confidence.",
             "bBox": {"x0": 10, "y0": 10, "x1": 210, "y1": 30}},
        ],
    },
]


# --------------------------------------------------------------------------- #
# Normalization + hashing
# --------------------------------------------------------------------------- #
class TestNormalizeAndHash:
    def test_normalize_collapses_whitespace(self):
        assert _stemma._normalize("a\n  b\t c ") == "a b c"

    def test_hash_is_whitespace_insensitive(self):
        assert _stemma.sha256_text("a b c") == _stemma.sha256_text("a   b\n c")

    def test_hash_is_deterministic(self):
        assert _stemma.sha256_text("hello") == _stemma.sha256_text("hello")


# --------------------------------------------------------------------------- #
# Block splitting
# --------------------------------------------------------------------------- #
class TestSplitBlocks:
    def test_splits_on_blank_lines(self):
        blocks = _stemma.split_blocks("one\n\ntwo\n\nthree")
        assert [b[0] for b in blocks] == ["one", "two", "three"]

    def test_offsets_point_into_raw_text(self):
        md = "first\n\nsecond"
        blocks = _stemma.split_blocks(md)
        for text, start, end in blocks:
            assert md[start:end] == text

    def test_drops_empty_blocks(self):
        assert _stemma.split_blocks("\n\n  \n\n") == []

    def test_single_block(self):
        blocks = _stemma.split_blocks("just one paragraph")
        assert len(blocks) == 1
        assert blocks[0][0] == "just one paragraph"


# --------------------------------------------------------------------------- #
# bbox handling
# --------------------------------------------------------------------------- #
class TestBbox:
    def test_xywh_passthrough(self):
        box = _stemma._item_bbox({"bBox": {"x": 1, "y": 2, "w": 3, "h": 4}})
        assert box == {"x": 1.0, "y": 2.0, "w": 3.0, "h": 4.0}

    def test_x0y0x1y1_converted(self):
        box = _stemma._item_bbox({"bBox": {"x0": 10, "y0": 20, "x1": 40, "y1": 60}})
        assert box == {"x": 10.0, "y": 20.0, "w": 30.0, "h": 40.0}

    def test_missing_bbox_is_none(self):
        assert _stemma._item_bbox({"md": "no box"}) is None

    def test_union_of_boxes(self):
        boxes = [{"x": 0, "y": 0, "w": 10, "h": 10},
                 {"x": 5, "y": 5, "w": 10, "h": 10}]
        assert _stemma._union_bbox(boxes) == {"x": 0, "y": 0, "w": 15, "h": 15}

    def test_block_bbox_unions_matching_items(self):
        items = [
            {"md": "Alpha beta", "bBox": {"x": 0, "y": 0, "w": 10, "h": 10}},
            {"md": "gamma delta", "bBox": {"x": 20, "y": 0, "w": 10, "h": 10}},
            {"md": "unrelated", "bBox": {"x": 99, "y": 99, "w": 1, "h": 1}},
        ]
        box = _stemma._bbox_for_block("Alpha beta gamma delta", items)
        assert box == {"x": 0, "y": 0, "w": 30, "h": 10}


# --------------------------------------------------------------------------- #
# Strand construction
# --------------------------------------------------------------------------- #
class TestBuildStrands:
    def test_strand_count_and_ids(self):
        strands = _stemma.build_strands(PAGES)
        ids = [s.id for s in strands]
        assert ids == ["p1-b0", "p1-b1", "p1-b2", "p2-b0"]

    def test_pages_assigned(self):
        strands = _stemma.build_strands(PAGES)
        assert strands[0].page == 1
        assert strands[-1].page == 2

    def test_offsets_map_into_source_page(self):
        page_md = PAGES[0]["md"]
        first = _stemma.build_strands(PAGES)[0]
        assert page_md[first.char_start:first.char_end].strip() == first.text

    def test_bbox_attached_when_items_present(self):
        strands = _stemma.build_strands(PAGES)
        assert strands[1].bbox is not None  # "Alpha beta gamma delta."

    def test_skips_failed_pages(self):
        pages = [{"page": 1, "md": "kept"}, {"page": 2, "md": "dropped",
                                             "success": False}]
        strands = _stemma.build_strands(pages)
        assert [s.text for s in strands] == ["kept"]

    def test_falls_back_to_index_page_number(self):
        pages = [{"md": "no explicit page number"}]
        assert _stemma.build_strands(pages)[0].page == 1


# --------------------------------------------------------------------------- #
# Rendering + manifest
# --------------------------------------------------------------------------- #
class TestRenderAndManifest:
    def test_mirror_has_frontmatter_and_anchors(self):
        strands = _stemma.build_strands(PAGES)
        out = _stemma.render_mirror("doc.pdf", strands, "abc123")
        assert out.startswith("---\n")
        assert "source: doc.pdf" in out
        assert "source_sha256: abc123" in out
        assert "<!-- strand: p1-b0" in out
        assert "<!-- page: 2 -->" in out

    def test_render_is_deterministic(self):
        strands = _stemma.build_strands(PAGES)
        a = _stemma.render_mirror("doc.pdf", strands, "abc")
        b = _stemma.render_mirror("doc.pdf", strands, "abc")
        assert a == b

    def test_manifest_shape(self):
        strands = _stemma.build_strands(PAGES)
        man = _stemma.build_manifest("doc.pdf", "abc", strands)
        assert man["page_count"] == 2
        assert man["strand_count"] == 4
        assert man["strands"][0]["id"] == "p1-b0"
        assert "text" in man["strands"][0]


# --------------------------------------------------------------------------- #
# Resolver
# --------------------------------------------------------------------------- #
class TestResolveQuote:
    @pytest.fixture
    def manifest(self):
        strands = _stemma.build_strands(PAGES)
        return _stemma.build_manifest("doc.pdf", "abc", strands)

    def test_exact_phrase_resolves(self, manifest):
        matches = _stemma.resolve_quote("strict confidence", manifest)
        assert len(matches) == 1
        assert matches[0]["page"] == 2

    def test_precise_span_within_block(self, manifest):
        matches = _stemma.resolve_quote("strict confidence", manifest)
        m = matches[0]
        page_md = PAGES[1]["md"]
        assert page_md[m["char_start"]:m["char_end"]] == "strict confidence"

    def test_whitespace_insensitive(self, manifest):
        matches = _stemma.resolve_quote("Alpha    beta\ngamma", manifest)
        assert len(matches) == 1
        assert matches[0]["page"] == 1

    def test_no_match_returns_empty(self, manifest):
        assert _stemma.resolve_quote("nonexistent phrase", manifest) == []

    def test_empty_quote_returns_empty(self, manifest):
        assert _stemma.resolve_quote("   ", manifest) == []

    def test_match_carries_bbox(self, manifest):
        matches = _stemma.resolve_quote("Alpha beta", manifest)
        assert matches[0]["bbox"] is not None


# --------------------------------------------------------------------------- #
# CLI: stemma build (offline) + cite
# --------------------------------------------------------------------------- #
class TestStemmaCli:
    @pytest.fixture
    def parse_json(self, tmp_path):
        path = tmp_path / "result.json"
        path.write_text(json.dumps({"markdown": {"pages": PAGES}}), encoding="utf-8")
        return path

    def test_build_writes_mirror_and_manifest(self, tmp_path, parse_json, capsys):
        out_dir = tmp_path / "mirror"
        rc = _core.main([
            "stemma", "--from-parse-json", str(parse_json),
            "--source", str(tmp_path / "doc.pdf"),
            "--out-dir", str(out_dir),
        ])
        assert rc == 0
        assert (out_dir / "doc.md").exists()
        manifest = out_dir / "doc.stemma.json"
        assert manifest.exists()
        data = json.loads(manifest.read_text(encoding="utf-8"))
        assert data["strand_count"] == 4

    def test_build_requires_source_with_json(self, parse_json):
        with pytest.raises(SystemExit) as exc:
            _core.main(["stemma", "--from-parse-json", str(parse_json)])
        assert exc.value.code == 2

    def test_missing_json_file_errors(self, tmp_path):
        with pytest.raises(SystemExit) as exc:
            _core.main([
                "stemma", "--from-parse-json", str(tmp_path / "nope.json"),
                "--source", str(tmp_path / "doc.pdf"),
            ])
        assert exc.value.code == 2

    def test_no_input_at_all_errors(self):
        with pytest.raises(SystemExit) as exc:
            _core.main(["stemma"])
        assert exc.value.code == 2


class TestCiteCli:
    @pytest.fixture
    def manifest_path(self, tmp_path, parse_json_factory):
        out_dir = tmp_path / "mirror"
        _core.main([
            "stemma", "--from-parse-json", str(parse_json_factory),
            "--source", str(tmp_path / "doc.pdf"),
            "--out-dir", str(out_dir),
        ])
        return out_dir / "doc.stemma.json"

    @pytest.fixture
    def parse_json_factory(self, tmp_path):
        path = tmp_path / "result.json"
        path.write_text(json.dumps({"markdown": {"pages": PAGES}}), encoding="utf-8")
        return path

    def test_cite_human_output(self, manifest_path, capsys):
        rc = _core.main(["cite", "strict confidence",
                         "--manifest", str(manifest_path)])
        assert rc == 0
        out = capsys.readouterr().out
        assert "doc.pdf p.2" in out
        assert "bbox" in out

    def test_cite_json_output(self, manifest_path, capsys):
        rc = _core.main(["cite", "strict confidence",
                         "--manifest", str(manifest_path), "--json"])
        assert rc == 0
        data = json.loads(capsys.readouterr().out)
        assert data[0]["page"] == 2

    def test_cite_no_match_returns_1(self, manifest_path):
        rc = _core.main(["cite", "not in the document",
                         "--manifest", str(manifest_path)])
        assert rc == 1

    def test_cite_missing_manifest_errors(self, tmp_path):
        with pytest.raises(SystemExit) as exc:
            _core.main(["cite", "x", "--manifest", str(tmp_path / "nope.json")])
        assert exc.value.code == 2


# --------------------------------------------------------------------------- #
# Live path wiring (mocked at the parse boundary — no network)
# --------------------------------------------------------------------------- #
class TestLiveWiring:
    def test_live_path_calls_fetch_and_builds(self, tmp_path, monkeypatch):
        called = {}

        def fake_fetch(input_path, tier, version, **kw):
            called["input"] = input_path
            return PAGES

        monkeypatch.setattr(_stemma, "fetch_parse_pages", fake_fetch)
        doc = tmp_path / "doc.pdf"
        doc.write_bytes(b"%PDF-1.4 fake")
        out_dir = tmp_path / "mirror"
        rc = _core.main(["stemma", str(doc), "--out-dir", str(out_dir)])
        assert rc == 0
        assert called["input"] == doc
        assert (out_dir / "doc.md").exists()

    def test_round_trip_build_then_resolve(self, tmp_path, monkeypatch):
        """End-to-end: live parse → mirror → cite resolves to the right page."""
        monkeypatch.setattr(_stemma, "fetch_parse_pages",
                            lambda *a, **k: PAGES)
        doc = tmp_path / "doc.pdf"
        doc.write_bytes(b"%PDF-1.4 fake")
        out_dir = tmp_path / "mirror"
        _core.main(["stemma", str(doc), "--out-dir", str(out_dir)])
        manifest = json.loads(
            (out_dir / "doc.stemma.json").read_text(encoding="utf-8"))
        matches = _stemma.resolve_quote("Alpha beta gamma", manifest)
        assert len(matches) == 1
        assert matches[0]["page"] == 1
        assert matches[0]["sha256"]
