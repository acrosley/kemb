#!/usr/bin/env python3
"""parse_document.py - Parse a document with LlamaParse.

Uses the official LlamaParse Python SDK (`llama-cloud-services`) by default and
falls back to the LlamaParse REST API if the SDK isn't installed.

Auth: reads LLAMA_CLOUD_API_KEY from the environment. Never accepts the key
as a CLI argument - that would leak it into shell history and logs.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

REST_BASE = "https://api.cloud.llamaindex.ai/api/v2/parse"
TIERS = ("fast", "cost_effective", "agentic", "agentic_plus")


def _err(msg, code=2):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def _require_api_key():
    key = os.environ.get("LLAMA_CLOUD_API_KEY")
    if not key:
        _err("LLAMA_CLOUD_API_KEY is not set. Get a key at "
             "https://cloud.llamaindex.ai/api-key and export it before running.")
    return key


def _validate_tier_and_format(tier, result_type):
    if tier == "fast" and result_type == "markdown":
        _err("tier='fast' does not support markdown output. Either pass "
             "--result-type text, or switch to --tier cost_effective (or higher).")


def parse_with_sdk(input_path, result_type, language, tier):
    # The LlamaParse class lives in `llama-cloud-services` (preferred) or the
    # legacy `llama-parse` package. The bare `llama-cloud` package does NOT
    # expose LlamaParse. Try each import in order.
    LlamaParse = None
    last_err = None
    for module_name in ("llama_cloud_services", "llama_parse"):
        try:
            mod = __import__(module_name, fromlist=["LlamaParse"])
            LlamaParse = getattr(mod, "LlamaParse", None)
            if LlamaParse is not None:
                break
        except ImportError as e:
            last_err = e
    if LlamaParse is None:
        raise ImportError(
            "LlamaParse SDK not found. Install with "
            "`pip install llama-cloud-services --break-system-packages` "
            "(preferred) or `pip install llama-parse --break-system-packages`. "
            f"Last error: {last_err}"
        )

    parser = LlamaParse(api_key=_require_api_key(), tier=tier, language=language)

    async def _run():
        result = await parser.aparse(str(input_path))
        if result_type == "markdown":
            docs = await result.aget_markdown_documents(split_by_page=False)
        else:
            docs = await result.aget_text_documents(split_by_page=False)
        return "\n\n".join(getattr(d, "text", str(d)) for d in docs)

    return asyncio.run(_run())


def parse_with_rest(input_path, result_type, language, tier, poll_timeout):
    try:
        import requests
    except ImportError as e:
        raise ImportError("requests is not installed. `pip install requests`.") from e

    headers = {"Authorization": f"Bearer {_require_api_key()}"}
    configuration = {"tier": tier, "input_options": {"language": language}}

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

    expand = "markdown" if result_type == "markdown" else "text"
    r = requests.get(f"{REST_BASE}/{job_id}", headers=headers,
                     params={"expand": expand}, timeout=60)
    if r.status_code >= 400:
        _err(f"result fetch failed ({r.status_code}): {r.text}", code=3)
    payload = r.json()

    def _extract(obj, key):
        if not isinstance(obj, dict):
            return None
        if isinstance(obj.get(key), str):
            return obj[key]
        nested = obj.get("result") if isinstance(obj.get("result"), dict) else {}
        if isinstance(nested.get(key), str):
            return nested[key]
        pages = obj.get("pages") or nested.get("pages")
        if isinstance(pages, list):
            chunks = [p.get(key, "") for p in pages if isinstance(p, dict)]
            if any(chunks):
                return "\n\n".join(chunks)
        return None

    text = _extract(payload, expand)
    if not text:
        _err(f"could not find '{expand}' content. Keys: {list(payload.keys())[:20]}",
             code=3)
    return text


def main(argv=None):
    p = argparse.ArgumentParser(description="Parse a document with LlamaParse.")
    p.add_argument("input", type=Path)
    p.add_argument("--output", type=Path, default=None)
    p.add_argument("--result-type", choices=("markdown", "text"), default="markdown")
    p.add_argument("--tier", choices=TIERS, default="cost_effective",
                   help="Quality tier. 'fast' is text-only.")
    p.add_argument("--language", default="en")
    p.add_argument("--rest", action="store_true",
                   help="Force REST path even if SDK is installed.")
    p.add_argument("--poll-timeout", type=float, default=300.0)
    args = p.parse_args(argv)

    if not args.input.exists():
        _err(f"input file not found: {args.input}")
    _validate_tier_and_format(args.tier, args.result_type)
    _require_api_key()

    ext = ".md" if args.result_type == "markdown" else ".txt"
    out_path = args.output or args.input.with_suffix(ext)

    if args.rest:
        text = parse_with_rest(args.input, args.result_type, args.language,
                               args.tier, args.poll_timeout)
    else:
        try:
            text = parse_with_sdk(args.input, args.result_type, args.language, args.tier)
        except ImportError as e:
            print(f"note: {e}\nfalling back to REST.", file=sys.stderr)
            text = parse_with_rest(args.input, args.result_type, args.language,
                                   args.tier, args.poll_timeout)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text):,} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
