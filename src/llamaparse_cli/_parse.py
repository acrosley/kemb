"""Parse — convert a document to clean markdown/text via LlamaParse v2.

REST: POST /api/v2/parse/upload → poll → GET /api/v2/parse/{id}?expand=...
SDK:  client.parsing.parse(tier=..., version=..., upload_file=..., expand=[...])
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from ._common import (
    API_HOST,
    DEFAULT_VERSION,
    PARSE_TIERS,
    auth_headers,
    err,
    import_requests,
    load_sdk_client,
    poll_job,
    surface_api_error,
    write_output,
)

REST_BASE = f"{API_HOST}/api/v2/parse"

_LAYOUT_COMMENT_RE = re.compile(r"<!--\s*layout:[^>]*-->\s*\n?")
_IMAGE_REF_RE = re.compile(
    r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]*page_\d+_image_\d+[^)]*)\)\s*\n?"
)


def parse_with_sdk(input_path, result_type, tier, version, auto_install):
    client = load_sdk_client(auto_install)
    if client is None:
        raise ImportError(
            "llama-cloud SDK not available. Install with "
            "`pip install llama-cloud` (or pass --auto-install to retry)."
        )

    expand = ["markdown"] if result_type == "markdown" else ["text"]

    try:
        with open(input_path, "rb") as fh:
            result = client.parsing.parse(
                tier=tier,
                version=version,
                upload_file=fh,
                expand=expand,
                timeout=600.0,
            )
    except Exception as e:
        surface_api_error("parse failed", e)

    return _extract_sdk_result(result, result_type)


def _extract_sdk_result(result, result_type):
    """Pull markdown/text out of the SDK's parse() result, joining per-page chunks."""
    key = "markdown" if result_type == "markdown" else "text"

    container = getattr(result, key, None)
    if container is None and isinstance(result, dict):
        container = result.get(key)
    if container is None:
        err(f"SDK result missing '{key}' field. Got: {result!r}", code=3)

    pages = getattr(container, "pages", None)
    if pages is None and isinstance(container, dict):
        pages = container.get("pages")

    if pages is None:
        if isinstance(container, str):
            return container
        err(f"SDK result '{key}' field had no pages: {container!r}", code=3)

    chunks = []
    for p in pages:
        if getattr(p, "success", True) is False:
            page_err = getattr(p, "error", None)
            if page_err:
                print(
                    f"warn: page {getattr(p, 'page_number', '?')} failed: {page_err}",
                    file=sys.stderr,
                )
            continue
        v = getattr(p, key, None)
        if v is None and isinstance(p, dict):
            v = p.get(key)
        if isinstance(v, str):
            chunks.append(v)

    if not chunks:
        err(f"SDK result pages had no '{key}' content.", code=3)
    return "\n\n".join(chunks)


def parse_with_rest(input_path, result_type, tier, version, poll_timeout):
    """Parse via the v2 REST API. Only requires the `requests` package."""
    requests = import_requests()
    headers = auth_headers()
    configuration = {"tier": tier, "version": version}

    with open(input_path, "rb") as fh:
        files = {"file": (input_path.name, fh)}
        data = {"configuration": json.dumps(configuration)}
        resp = requests.post(
            f"{REST_BASE}/upload",
            headers=headers,
            files=files,
            data=data,
            timeout=300,
        )
    if resp.status_code >= 400:
        err(f"upload failed ({resp.status_code}): {resp.text}", code=3)
    job = resp.json()
    job_id = job.get("id") or job.get("job_id")
    if not job_id:
        err(f"upload response missing job id: {json.dumps(job)[:500]}", code=3)

    poll_job(f"{REST_BASE}/{job_id}", headers, poll_timeout)

    expand = "markdown" if result_type == "markdown" else "text"
    r = requests.get(
        f"{REST_BASE}/{job_id}",
        headers=headers,
        params={"expand": expand},
        timeout=120,
    )
    if r.status_code >= 400:
        err(f"result fetch failed ({r.status_code}): {r.text}", code=3)
    payload = r.json()

    text = _extract_rest_field(payload, expand)
    if not text:
        err(
            f"could not find '{expand}' content. Keys: {list(payload.keys())[:20]}",
            code=3,
        )
    return text


def _extract_rest_field(obj, key):
    """Best-effort lookup for the expanded field across known v2 response shapes."""
    if not isinstance(obj, dict):
        return None

    if isinstance(obj.get(key), str):
        return obj[key]

    container = obj.get(key)
    if isinstance(container, dict):
        if isinstance(container.get(key), str):
            return container[key]
        pages = container.get("pages")
        if isinstance(pages, list):
            chunks = []
            for p in pages:
                if not isinstance(p, dict):
                    continue
                if p.get("success") is False:
                    continue
                v = p.get(key)
                if isinstance(v, str):
                    chunks.append(v)
            if chunks:
                return "\n\n".join(chunks)

    full = obj.get(f"{key}_full")
    if isinstance(full, str) and full:
        return full

    return None


def strip_noise(text, repeat_threshold=3):
    layout_dropped = len(_LAYOUT_COMMENT_RE.findall(text))
    text = _LAYOUT_COMMENT_RE.sub("", text)

    alt_counts = {}
    for m in _IMAGE_REF_RE.finditer(text):
        alt = m.group("alt").strip()
        alt_counts[alt] = alt_counts.get(alt, 0) + 1

    repeating_alts = {alt for alt, n in alt_counts.items() if n >= repeat_threshold}
    images_dropped = 0

    def _maybe_drop(m):
        nonlocal images_dropped
        if m.group("alt").strip() in repeating_alts:
            images_dropped += 1
            return ""
        return m.group(0)

    text = _IMAGE_REF_RE.sub(_maybe_drop, text)
    return text, layout_dropped, images_dropped


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "parse",
        help="Parse a document into markdown or plain text.",
        description="Parse a document with LlamaParse (API v2).",
    )
    p.add_argument("input", type=Path, help="Path to the document to parse.")
    p.add_argument("--output", type=Path, default=None,
                   help="Output file path (default: <input>.md or <input>.txt).")
    p.add_argument("--result-type", choices=("markdown", "text"),
                   default="markdown",
                   help="Output format (default: markdown).")
    p.add_argument("--tier", choices=PARSE_TIERS, default="cost_effective",
                   help="Quality / cost tier (default: cost_effective).")
    p.add_argument("--version", default=DEFAULT_VERSION,
                   help="Parse model version: 'latest' (default) or a dated "
                        "pin like '2026-04-09'.")
    p.add_argument("--strip-noise", action="store_true",
                   help="Drop LlamaParse layout-hint HTML comments and "
                        "recurring header/footer image refs (alt seen 3+ times).")
    p.add_argument("--rest", action="store_true",
                   help="Force REST path even if the SDK is installed.")
    p.add_argument("--poll-timeout", type=float, default=600.0,
                   help="REST mode only. Max seconds to wait for a job.")
    p.add_argument("--auto-install", action="store_true",
                   help="If llama-cloud isn't importable, try `pip install` it.")
    p.add_argument("--stdout", action="store_true",
                   help="Also write the result to stdout.")
    p.set_defaults(func=run)
    return p


def run(args):
    if not args.input.exists():
        err(f"input file not found: {args.input}")

    # FAST tier physically only produces text — markdown expansion is
    # rejected upstream. Quietly fetch text instead and write it to the
    # user's chosen output path (plain text is valid markdown).
    fetch_type = args.result_type
    if args.tier == "fast" and args.result_type == "markdown":
        print(
            "note: FAST tier returns plain text; saving as markdown. "
            "Use --tier cost_effective or higher for structured markdown.",
            file=sys.stderr,
        )
        fetch_type = "text"

    ext = ".md" if args.result_type == "markdown" else ".txt"
    out_path = args.output or args.input.with_suffix(ext)

    if args.rest:
        text = parse_with_rest(
            args.input, fetch_type, args.tier, args.version,
            args.poll_timeout,
        )
    else:
        try:
            text = parse_with_sdk(
                args.input, fetch_type, args.tier, args.version,
                args.auto_install,
            )
        except ImportError as e:
            print(f"note: {e}\nfalling back to REST.", file=sys.stderr)
            text = parse_with_rest(
                args.input, fetch_type, args.tier, args.version,
                args.poll_timeout,
            )

    if args.strip_noise:
        text, layout_dropped, images_dropped = strip_noise(text)
        print(
            f"strip-noise: dropped {layout_dropped} layout comments, "
            f"{images_dropped} repeating image refs",
            file=sys.stderr,
        )

    write_output(out_path, text)
    if args.stdout:
        sys.stdout.write(text)
    return 0
