"""Stemma — page-hash, block-level provenance for a parsed document.

This is the provenance kernel of *kembing*: take a parsed document, comb it into
a markdown **mirror** an agent can read, and stamp every block with a **stemma**
record — `{source, page, sha256, char_span, bbox?}` — so any verbatim quote in an
agent's answer can be resolved back to a source page (and bounding box, when the
parser supplied layout items).

Two ways in, one core:

* live   — ``kemb stemma ./doc.pdf`` parses via LlamaParse, then combs the pages.
* offline — ``kemb stemma --from-parse-json result.json --source doc.pdf`` combs a
  saved parse result. Zero credits; this is the path the tests exercise.

The build is deterministic (no timestamps in the rendered artifacts) so the same
parse result always yields the same mirror and manifest — a property the hash-
stamped provenance story depends on.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

from ._common import err, write_output

MANIFEST_SUFFIX = ".stemma.json"
MIRROR_DIRNAME = "mirror"

_WS_RE = re.compile(r"\s+")
_BLANKLINE_RE = re.compile(r"\n[ \t]*\n")


# --------------------------------------------------------------------------- #
# Provenance model
# --------------------------------------------------------------------------- #
@dataclass
class Strand:
    """One combed block of a document, with its lineage back to the source."""

    id: str
    page: int
    text: str
    sha256: str
    char_start: int
    char_end: int
    bbox: Optional[dict] = None

    def to_record(self) -> dict:
        rec = {
            "id": self.id,
            "page": self.page,
            "sha256": self.sha256,
            "char_start": self.char_start,
            "char_end": self.char_end,
            "text": self.text,
        }
        if self.bbox is not None:
            rec["bbox"] = self.bbox
        return rec


def _normalize(text: str) -> str:
    """Collapse runs of whitespace and strip — the canonical form we hash/match."""
    return _WS_RE.sub(" ", text).strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(_normalize(text).encode("utf-8")).hexdigest()


def compute_file_sha256(path: Path) -> Optional[str]:
    try:
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None


# --------------------------------------------------------------------------- #
# Defensive page/item accessors — parse payloads vary (SDK object vs REST JSON)
# --------------------------------------------------------------------------- #
def _get(obj: Any, *keys: str):
    for key in keys:
        if isinstance(obj, dict):
            if obj.get(key) is not None:
                return obj[key]
        else:
            val = getattr(obj, key, None)
            if val is not None:
                return val
    return None


def _page_number(page: Any, fallback: int) -> int:
    n = _get(page, "page", "page_number", "page_index")
    try:
        return int(n)
    except (TypeError, ValueError):
        return fallback


def _page_md(page: Any) -> str:
    val = _get(page, "md", "markdown", "text")
    return val if isinstance(val, str) else ""


def _page_items(page: Any) -> list:
    items = _get(page, "items", "layout", "elements")
    return items if isinstance(items, list) else []


def _item_text(item: Any) -> str:
    val = _get(item, "md", "value", "text", "content")
    return val if isinstance(val, str) else ""


def _item_bbox(item: Any) -> Optional[dict]:
    """Normalize a layout item's bounding box to {x, y, w, h}.

    LlamaParse has used both ``{x, y, w, h}`` and ``{x0, y0, x1, y1}`` shapes;
    accept either and return None when no usable box is present.
    """
    box = _get(item, "bBox", "bbox", "box")
    if not isinstance(box, dict):
        return None
    if all(k in box for k in ("x", "y", "w", "h")):
        try:
            return {k: float(box[k]) for k in ("x", "y", "w", "h")}
        except (TypeError, ValueError):
            return None
    if all(k in box for k in ("x0", "y0", "x1", "y1")):
        try:
            x0, y0, x1, y1 = (float(box[k]) for k in ("x0", "y0", "x1", "y1"))
        except (TypeError, ValueError):
            return None
        return {"x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0}
    return None


def _union_bbox(boxes: list) -> Optional[dict]:
    boxes = [b for b in boxes if b]
    if not boxes:
        return None
    x = min(b["x"] for b in boxes)
    y = min(b["y"] for b in boxes)
    right = max(b["x"] + b["w"] for b in boxes)
    bottom = max(b["y"] + b["h"] for b in boxes)
    return {"x": x, "y": y, "w": right - x, "h": bottom - y}


def _bbox_for_block(block_text: str, items: list) -> Optional[dict]:
    """Best-effort: union the boxes of layout items whose text sits in the block.

    Provenance bbox is only as good as the parser's layout items; when a tier
    returns none, strands simply carry no bbox and we fall back to page-level
    citation. Matching is by normalized-substring containment in either
    direction so short headings and split lines still attach.
    """
    if not items:
        return None
    norm_block = _normalize(block_text)
    if not norm_block:
        return None
    hits = []
    for item in items:
        norm_item = _normalize(_item_text(item))
        if not norm_item:
            continue
        if norm_item in norm_block or norm_block in norm_item:
            box = _item_bbox(item)
            if box:
                hits.append(box)
    return _union_bbox(hits)


# --------------------------------------------------------------------------- #
# Block splitting
# --------------------------------------------------------------------------- #
def split_blocks(page_md: str) -> list:
    """Split a page's markdown into (raw_text, char_start, char_end) blocks.

    Blocks are blank-line-separated runs. Offsets are into the *raw* page
    string so a resolver can map a verbatim quote back to an exact character
    span. Empty/whitespace-only blocks are dropped.
    """
    blocks = []
    pos = 0
    for piece in _BLANKLINE_RE.split(page_md):
        start = page_md.find(piece, pos)
        if start < 0:  # defensive; split pieces are always findable
            start = pos
        end = start + len(piece)
        pos = end
        if piece.strip():
            blocks.append((piece, start, end))
    return blocks


def build_strands(pages: list) -> list:
    """Comb a list of parse pages into ordered Strands with provenance.

    ``pages`` is whatever the parser returned — a list of dicts or SDK page
    objects. Each contributes zero or more strands, ids of the form
    ``p{page}-b{n}``.
    """
    strands: list = []
    for idx, page in enumerate(pages):
        page_no = _page_number(page, idx + 1)
        md = _page_md(page)
        if _get(page, "success") is False:
            continue
        items = _page_items(page)
        for b_idx, (text, c0, c1) in enumerate(split_blocks(md)):
            strands.append(
                Strand(
                    id=f"p{page_no}-b{b_idx}",
                    page=page_no,
                    text=text.strip(),
                    sha256=sha256_text(text),
                    char_start=c0,
                    char_end=c1,
                    bbox=_bbox_for_block(text, items),
                )
            )
    return strands


# --------------------------------------------------------------------------- #
# Rendering: mirror markdown + manifest JSON
# --------------------------------------------------------------------------- #
def render_mirror(source: str, strands: list, source_sha256: Optional[str]) -> str:
    """Render the agent-readable mirror: each block prefixed by a stemma anchor.

    The anchor is an HTML comment, so the body still reads as clean markdown to
    an agent while carrying machine-resolvable provenance inline.
    """
    pages = sorted({s.page for s in strands})
    lines = [
        "---",
        f"source: {source}",
        f"source_sha256: {source_sha256 or '(unavailable)'}",
        f"pages: {len(pages)}",
        f"strands: {len(strands)}",
        "generator: kemb stemma",
        "---",
        "",
    ]
    current_page = None
    for s in strands:
        if s.page != current_page:
            lines.append(f"<!-- page: {s.page} -->")
            current_page = s.page
        bbox = json.dumps(s.bbox, separators=(",", ":")) if s.bbox else "null"
        lines.append(
            f"<!-- strand: {s.id} page={s.page} sha256={s.sha256} "
            f"span={s.char_start}:{s.char_end} bbox={bbox} -->"
        )
        lines.append(s.text)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_manifest(source: str, source_sha256: Optional[str], strands: list) -> dict:
    pages = sorted({s.page for s in strands})
    return {
        "source": source,
        "source_sha256": source_sha256,
        "page_count": len(pages),
        "strand_count": len(strands),
        "strands": [s.to_record() for s in strands],
    }


def write_mirror(out_dir: Path, source_path: Path, strands: list) -> tuple:
    """Write mirror markdown + stemma manifest into ``out_dir``; return their paths."""
    stem = source_path.stem
    source_sha256 = compute_file_sha256(source_path)
    source_label = source_path.name

    mirror_path = out_dir / f"{stem}.md"
    manifest_path = out_dir / f"{stem}{MANIFEST_SUFFIX}"

    write_output(mirror_path, render_mirror(source_label, strands, source_sha256))
    manifest = build_manifest(source_label, source_sha256, strands)
    write_output(manifest_path, json.dumps(manifest, indent=2) + "\n")
    return mirror_path, manifest_path


# --------------------------------------------------------------------------- #
# Resolver — verbatim quote → provenance (used by `kemb cite`)
# --------------------------------------------------------------------------- #
def _quote_regex(quote: str) -> Optional["re.Pattern"]:
    norm = _normalize(quote)
    if not norm:
        return None
    parts = [re.escape(tok) for tok in norm.split(" ")]
    return re.compile(r"\s+".join(parts))


def resolve_quote(quote: str, manifest: dict) -> list:
    """Resolve a verbatim quote to the strand(s) it came from.

    Whitespace-insensitive: the quote is matched against each strand's text with
    runs of whitespace treated as flexible, so line wrapping in the mirror does
    not break a citation. Returns one match per strand the quote appears in,
    each with the precise character span *within the source page*.
    """
    pat = _quote_regex(quote)
    if pat is None:
        return []
    matches = []
    for strand in manifest.get("strands", []):
        text = strand.get("text", "")
        m = pat.search(text)
        if not m:
            continue
        base = strand.get("char_start", 0)
        matches.append(
            {
                "source": manifest.get("source"),
                "page": strand.get("page"),
                "strand_id": strand.get("id"),
                "sha256": strand.get("sha256"),
                "char_start": base + m.start(),
                "char_end": base + m.end(),
                "bbox": strand.get("bbox"),
                "matched_text": m.group(0),
            }
        )
    matches.sort(key=lambda r: (r.get("page") or 0, r.get("char_start") or 0))
    return matches


# --------------------------------------------------------------------------- #
# Live parse → pages (best-effort; the offline path is what tests cover)
# --------------------------------------------------------------------------- #
def fetch_parse_pages(input_path, tier, version, *, rest, auto_install, poll_timeout):
    """Parse a document and return its raw per-page payloads (with layout items).

    Mirrors ``_parse``'s SDK-first / REST-fallback contract but keeps page
    structure instead of flattening to text, so block offsets and bbox survive.
    """
    if rest:
        return _fetch_pages_rest(input_path, tier, version, poll_timeout)
    try:
        return _fetch_pages_sdk(input_path, tier, version, auto_install)
    except ImportError as e:
        print(f"note: {e}\nfalling back to REST.", file=sys.stderr)
        return _fetch_pages_rest(input_path, tier, version, poll_timeout)


def _pages_from_payload(payload: Any) -> list:
    container = _get(payload, "markdown") if isinstance(payload, dict) else None
    pages = _get(container, "pages") if container is not None else None
    if pages is None:
        pages = _get(payload, "pages")
    if isinstance(pages, list):
        return pages
    err("parse result contained no pages to comb.", code=3)


def _fetch_pages_rest(input_path, tier, version, poll_timeout) -> list:
    from ._common import API_HOST, auth_headers, import_requests, poll_job

    requests = import_requests()
    headers = auth_headers()
    base = f"{API_HOST}/api/v2/parse"
    configuration = {"tier": tier, "version": version}
    with open(input_path, "rb") as fh:
        files = {"file": (input_path.name, fh)}
        data = {"configuration": json.dumps(configuration)}
        resp = requests.post(f"{base}/upload", headers=headers, files=files,
                             data=data, timeout=300)
    if resp.status_code >= 400:
        err(f"upload failed ({resp.status_code}): {resp.text}", code=3)
    job = resp.json()
    job_id = job.get("id") or job.get("job_id")
    if not job_id:
        err(f"upload response missing job id: {json.dumps(job)[:500]}", code=3)
    poll_job(f"{base}/{job_id}", headers, poll_timeout)
    r = requests.get(f"{base}/{job_id}", headers=headers,
                     params={"expand": "markdown"}, timeout=120)
    if r.status_code >= 400:
        err(f"result fetch failed ({r.status_code}): {r.text}", code=3)
    return _pages_from_payload(r.json())


def _fetch_pages_sdk(input_path, tier, version, auto_install) -> list:
    from ._common import load_sdk_client, surface_api_error

    client = load_sdk_client(auto_install)
    if client is None:
        raise ImportError(
            "llama-cloud SDK not available. Install with "
            "`pip install llama-cloud` (or pass --auto-install to retry)."
        )
    try:
        with open(input_path, "rb") as fh:
            result = client.parsing.parse(
                tier=tier, version=version, upload_file=fh,
                expand=["markdown"], timeout=600.0,
            )
    except Exception as e:
        surface_api_error("parse failed", e)
    md = _get(result, "markdown")
    pages = _get(md, "pages") if md is not None else None
    if pages is None:
        pages = _get(result, "pages")
    if not isinstance(pages, list):
        err(f"SDK parse result had no pages: {result!r}", code=3)
    return pages


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def add_subparser(subparsers):
    p = subparsers.add_parser(
        "stemma",
        help="Comb a document into a provenance-stamped markdown mirror.",
        description=(
            "Build a markdown mirror of a document where every block carries a "
            "stemma record (source, page, sha256, char span, bbox) so verbatim "
            "quotes resolve back to the source. Parses live, or combs a saved "
            "parse result with --from-parse-json (zero credits)."
        ),
    )
    p.add_argument("input", type=Path, nargs="?",
                   help="Document to parse and comb (omit when using "
                        "--from-parse-json).")
    p.add_argument("--from-parse-json", type=Path, default=None,
                   help="Comb a saved LlamaParse result JSON instead of parsing "
                        "live. Requires --source to label the mirror.")
    p.add_argument("--source", type=Path, default=None,
                   help="Source document path recorded in the mirror/manifest "
                        "(required with --from-parse-json).")
    p.add_argument("--out-dir", type=Path, default=None,
                   help=f"Directory for the mirror (default: ./{MIRROR_DIRNAME}).")
    p.add_argument("--tier", default="cost_effective",
                   help="Parse tier for the live path (default: cost_effective).")
    p.add_argument("--version", default="latest",
                   help="Parse model version for the live path (default: latest).")
    p.add_argument("--rest", action="store_true",
                   help="Force the REST path on a live parse.")
    p.add_argument("--auto-install", action="store_true",
                   help="If llama-cloud isn't importable, try to pip install it.")
    p.add_argument("--poll-timeout", type=float, default=600.0,
                   help="REST mode only. Max seconds to wait for a parse job.")
    p.set_defaults(func=run)
    return p


def _load_pages_from_json(path: Path) -> list:
    if not path.exists():
        err(f"parse-json file not found: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        err(f"could not read parse JSON from {path}: {e}")
    if isinstance(payload, list):
        return payload
    return _pages_from_payload(payload)


def run(args):
    out_dir = args.out_dir or Path(MIRROR_DIRNAME)

    if args.from_parse_json is not None:
        if args.source is None:
            err("--from-parse-json requires --source <path> to label the mirror.")
        pages = _load_pages_from_json(args.from_parse_json)
        source_path = args.source
    else:
        if args.input is None:
            err("provide a document path, or --from-parse-json with --source.")
        if not args.input.exists():
            err(f"input file not found: {args.input}")
        pages = fetch_parse_pages(
            args.input, args.tier, args.version,
            rest=args.rest, auto_install=args.auto_install,
            poll_timeout=args.poll_timeout,
        )
        source_path = args.input

    strands = build_strands(pages)
    if not strands:
        err("no text blocks found to comb — nothing to mirror.", code=3)

    mirror_path, manifest_path = write_mirror(out_dir, source_path, strands)
    print(
        f"combed {len(strands)} strands across "
        f"{len({s.page for s in strands})} page(s).",
        file=sys.stderr,
    )
    print(f"  mirror:   {mirror_path}", file=sys.stderr)
    print(f"  manifest: {manifest_path}", file=sys.stderr)
    return 0
