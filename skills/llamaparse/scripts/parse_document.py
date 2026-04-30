#!/usr/bin/env python3
"""parse_document.py - Parse a document with LlamaParse (API v2).

Targets LlamaParse API v2 only. Uses the official `llama-cloud` Python SDK
by default and falls back to direct REST calls when the SDK isn't installable.

The legacy `llama-cloud-services` / `llama-parse` packages and API v1 are NOT
supported here. Per LlamaIndex's announcement, llama-cloud-services is
deprecated and will be archived after May 1, 2026.

Auth: reads LLAMA_CLOUD_API_KEY from the environment. Never accepts the key
as a CLI argument - that would leak it into shell history and logs.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

REST_BASE = "https://api.cloud.llamaindex.ai/api/v2/parse"
TIERS = ("fast", "cost_effective", "agentic", "agentic_plus")
DEFAULT_VERSION = "latest"

# Patterns used by --strip-noise.
_LAYOUT_COMMENT_RE = re.compile(r"<!--\s*layout:[^>]*-->\s*\n?")
_IMAGE_REF_RE = re.compile(
    r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]*page_\d+_image_\d+[^)]*)\)\s*\n?"
)


def _err(msg, code=2):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def _require_api_key():
    key = os.environ.get("LLAMA_CLOUD_API_KEY")
    if not key:
        _err("LLAMA_CLOUD_API_KEY is not set. Get a key at "
             "https://cloud.llamaindex.ai/api-key and export it before running.")
    return key


def _surface_api_error(label, exc):
    """Print the upstream API response body verbatim, then exit cleanly.

    The llama-cloud SDK raises subclasses of `ApiError` carrying a `body` attr
    with the parsed JSON response. Falling back to repr(exc) preserves the
    error chain for unexpected exception types.
    """
    body = getattr(exc, "body", None)
    if body is None:
        resp = getattr(exc, "response", None)
        if resp is not None:
            body = getattr(resp, "text", None) or repr(resp)
    if body is None:
        body = repr(exc)
    if isinstance(body, (dict, list)):
        body = json.dumps(body, indent=2, default=str)
    _err(f"{label} ({type(exc).__name__}): {body}", code=3)


def parse_with_sdk(input_path, result_type, tier, version):
    """Parse via the v2 `llama-cloud` SDK.

    Shape (April 2026):
        from llama_cloud import LlamaCloud
        client = LlamaCloud()  # reads LLAMA_CLOUD_API_KEY
        f = client.files.create(file=open(path, "rb"), purpose="parse")
        result = client.parsing.parse(
            file_id=f.id,
            tier="cost_effective",
            version="latest",
            expand=["markdown"] or ["text"],
        )
        # markdown:  result.markdown.pages[i].markdown
        # text:      result.text.pages[i].text
    """
    try:
        from llama_cloud import LlamaCloud  # type: ignore
    except ImportError as e:
        raise ImportError(
            "llama-cloud SDK not found. Install with "
            "`pip install llama-cloud --break-system-packages`. "
            "(The legacy llama-cloud-services / llama-parse packages are v1-only "
            "and are not supported by this skill.) "
            f"Underlying error: {e}"
        ) from e

    _require_api_key()  # SDK reads it from env, but fail fast if missing
    client = LlamaCloud()

    expand = ["markdown"] if result_type == "markdown" else ["text"]

    try:
        with open(input_path, "rb") as fh:
            uploaded = client.files.create(file=fh, purpose="parse")
    except Exception as e:
        _surface_api_error("file upload failed", e)

    file_id = getattr(uploaded, "id", None) or (
        uploaded.get("id") if isinstance(uploaded, dict) else None
    )
    if not file_id:
        _err(f"file upload returned no id: {uploaded!r}", code=3)

    try:
        result = client.parsing.parse(
            file_id=file_id,
            tier=tier,
            version=version,
            expand=expand,
        )
    except Exception as e:
        _surface_api_error("parse request failed", e)

    return _extract_sdk_result(result, result_type)


def _extract_sdk_result(result, result_type):
    """Pull markdown/text out of the SDK's parse() result, joining per-page chunks."""
    key = "markdown" if result_type == "markdown" else "text"

    container = getattr(result, key, None)
    if container is None and isinstance(result, dict):
        container = result.get(key)
    if container is None:
        _err(f"SDK result missing '{key}' field. Got: {result!r}", code=3)

    pages = getattr(container, "pages", None)
    if pages is None and isinstance(container, dict):
        pages = container.get("pages")

    if pages is None:
        # Some shapes return a single string under the field directly.
        if isinstance(container, str):
            return container
        _err(f"SDK result '{key}' field had no pages: {container!r}", code=3)

    chunks = []
    for p in pages:
        v = getattr(p, key, None)
        if v is None and isinstance(p, dict):
            v = p.get(key)
        if isinstance(v, str):
            chunks.append(v)

    if not chunks:
        _err(f"SDK result pages had no '{key}' content.", code=3)
    return "\n\n".join(chunks)


def parse_with_rest(input_path, result_type, tier, version, poll_timeout):
    """Parse via the v2 REST API. Only requires the `requests` package."""
    try:
        import requests  # type: ignore
    except ImportError as e:
        raise ImportError("requests is not installed. `pip install requests`.") from e

    headers = {"Authorization": f"Bearer {_require_api_key()}"}

    # v2 configuration envelope. tier and version are required.
    configuration = {
        "tier": tier,
        "version": version,
    }

    # POST /api/v2/parse/upload — multipart with file + configuration JSON.
    with open(input_path, "rb") as fh:
        files = {"file": (input_path.name, fh)}
        data = {"configuration": json.dumps(configuration)}
        resp = requests.post(f"{REST_BASE}/upload", headers=headers,
                             files=files, data=data, timeout=120)
    if resp.status_code >= 400:
        _err(f"upload failed ({resp.status_code}): {resp.text}", code=3)
    job = resp.json()
    job_id = job.get("id") or job.get("job_id")
    if not job_id:
        _err(f"upload response missing job id: {json.dumps(job)[:500]}", code=3)

    # Poll the job status.
    deadline = time.monotonic() + poll_timeout
    backoff = 1.0
    while True:
        if time.monotonic() > deadline:
            _err(f"timed out after {poll_timeout:.0f}s waiting for job {job_id}.",
                 code=4)
        s = requests.get(f"{REST_BASE}/{job_id}", headers=headers, timeout=30)
        if s.status_code >= 400:
            _err(f"status check failed ({s.status_code}): {s.text}", code=3)
        payload = s.json()
        status = (payload.get("status") or "").upper()
        if status == "COMPLETED":
            break
        if status in ("FAILED", "CANCELLED"):
            _err(f"job {job_id} ended with {status}: {json.dumps(payload)[:500]}",
                 code=3)
        time.sleep(min(backoff, 5.0))
        backoff = min(backoff * 1.5, 5.0)

    # Fetch result with ?expand=<field>.
    expand = "markdown" if result_type == "markdown" else "text"
    r = requests.get(f"{REST_BASE}/{job_id}", headers=headers,
                     params={"expand": expand}, timeout=60)
    if r.status_code >= 400:
        _err(f"result fetch failed ({r.status_code}): {r.text}", code=3)
    payload = r.json()

    text = _extract_rest_field(payload, expand)
    if not text:
        _err(f"could not find '{expand}' content. Keys: {list(payload.keys())[:20]}",
             code=3)
    return text


def _extract_rest_field(obj, key):
    """Best-effort lookup for the expanded field across known v2 response shapes."""
    if not isinstance(obj, dict):
        return None

    # Direct top-level scalar (older shape).
    if isinstance(obj.get(key), str):
        return obj[key]

    # v2 typical: {"markdown": {"pages": [{"markdown": "..."}, ...]}}
    container = obj.get(key)
    if isinstance(container, dict):
        if isinstance(container.get(key), str):
            return container[key]
        pages = container.get("pages")
        if isinstance(pages, list):
            chunks = [
                p.get(key, "") for p in pages
                if isinstance(p, dict) and isinstance(p.get(key), str)
            ]
            if any(chunks):
                return "\n\n".join(chunks)

    # Nested under "result" (defensive — some legacy responses).
    nested = obj.get("result") if isinstance(obj.get("result"), dict) else None
    if nested:
        sub = _extract_rest_field(nested, key)
        if sub:
            return sub

    # Top-level pages list.
    pages = obj.get("pages")
    if isinstance(pages, list):
        chunks = [p.get(key, "") for p in pages if isinstance(p, dict)]
        if any(chunks):
            return "\n\n".join(chunks)

    return None


def strip_noise(text, repeat_threshold=3):
    """Drop pure-noise artifacts from LlamaParse markdown.

    Removes:
    - `<!-- layout: ... -->` HTML comments (LlamaParse layout hints; no signal).
    - Image refs whose alt text recurs `repeat_threshold` or more times across
      the document. This catches recurring page-header/footer logos while
      preserving single-instance exhibits.

    Returns: (cleaned_text, layout_dropped, images_dropped)
    """
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


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Parse a document with LlamaParse (API v2).")
    p.add_argument("input", type=Path)
    p.add_argument("--output", type=Path, default=None)
    p.add_argument("--result-type", choices=("markdown", "text"), default="markdown")
    p.add_argument("--tier", choices=TIERS, default="cost_effective",
                   help="Quality tier. v2 supports markdown on every tier.")
    p.add_argument("--version", default=DEFAULT_VERSION,
                   help="Parse model version. 'latest' (default) or a dated pin "
                        "like '2026-01-08'.")
    p.add_argument("--strip-noise", action="store_true",
                   help="Post-process the output to drop LlamaParse layout-hint "
                        "HTML comments and recurring header/footer image refs "
                        "(alt text seen 3+ times). Off by default to preserve "
                        "raw output; safe to enable for narrative documents "
                        "like deposition transcripts and reports.")
    p.add_argument("--rest", action="store_true",
                   help="Force REST path even if SDK is installed.")
    p.add_argument("--poll-timeout", type=float, default=300.0)
    args = p.parse_args(argv)

    if not args.input.exists():
        _err(f"input file not found: {args.input}")
    _require_api_key()

    ext = ".md" if args.result_type == "markdown" else ".txt"
    out_path = args.output or args.input.with_suffix(ext)

    if args.rest:
        text = parse_with_rest(args.input, args.result_type,
                               args.tier, args.version, args.poll_timeout)
    else:
        try:
            text = parse_with_sdk(args.input, args.result_type,
                                  args.tier, args.version)
        except ImportError as e:
            print(f"note: {e}\nfalling back to REST.", file=sys.stderr)
            text = parse_with_rest(args.input, args.result_type,
                                   args.tier, args.version, args.poll_timeout)

    if args.strip_noise:
        text, layout_dropped, images_dropped = strip_noise(text)
        print(f"strip-noise: dropped {layout_dropped} layout comments, "
              f"{images_dropped} repeating image refs", file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text):,} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
