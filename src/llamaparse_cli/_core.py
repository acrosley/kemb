#!/usr/bin/env python3
"""parse_document.py — Parse a document with LlamaParse (API v2).

Uses the official `llama-cloud` Python SDK (https://pypi.org/project/llama-cloud/).
Falls back to direct REST calls if the SDK isn't importable. Reads the API
key from the LLAMA_CLOUD_API_KEY environment variable.

Usage:
    python parse_document.py <input_file> [--output PATH] [--result-type markdown|text]
                             [--tier fast|cost_effective|agentic|agentic_plus]
                             [--version latest|YYYY-MM-DD]
                             [--strip-noise] [--rest] [--poll-timeout SECONDS]
                             [--auto-install]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

REST_BASE = "https://api.cloud.llamaindex.ai/api/v2/parse"
TIERS = ("fast", "cost_effective", "agentic", "agentic_plus")
DEFAULT_VERSION = "latest"

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
        _err(
            "LLAMA_CLOUD_API_KEY is not set. Get a key at "
            "https://cloud.llamaindex.ai/api-key and export it before running."
        )
    return key


def _surface_api_error(label, exc):
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


def _try_install_sdk():
    """Best-effort `pip install llama-cloud` for the running interpreter."""
    cmds = [
        [sys.executable, "-m", "pip", "install", "--quiet", "llama-cloud"],
        [sys.executable, "-m", "pip", "install", "--quiet",
         "--break-system-packages", "llama-cloud"],
    ]
    for cmd in cmds:
        try:
            subprocess.check_call(cmd, stdout=subprocess.DEVNULL,
                                  stderr=subprocess.STDOUT)
            return True
        except Exception:
            continue
    return False


def _load_sdk(auto_install):
    try:
        from llama_cloud import LlamaCloud  # type: ignore
        return LlamaCloud
    except ImportError:
        if not auto_install:
            return None
        print("note: llama-cloud not installed; attempting pip install...",
              file=sys.stderr)
        if not _try_install_sdk():
            return None
        try:
            from llama_cloud import LlamaCloud  # type: ignore
            return LlamaCloud
        except ImportError:
            return None


def parse_with_sdk(input_path, result_type, tier, version, auto_install):
    LlamaCloud = _load_sdk(auto_install)
    if LlamaCloud is None:
        raise ImportError(
            "llama-cloud SDK not available. Install with "
            "`pip install llama-cloud` (or pass --auto-install to retry)."
        )

    _require_api_key()
    client = LlamaCloud()  # reads LLAMA_CLOUD_API_KEY from env

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
        _surface_api_error("parse failed", e)

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
        if isinstance(container, str):
            return container
        _err(f"SDK result '{key}' field had no pages: {container!r}", code=3)

    chunks = []
    for p in pages:
        # MarkdownPageFailedMarkdownPage / failure pages don't carry the field;
        # skip them but record the error if present.
        if getattr(p, "success", True) is False:
            err = getattr(p, "error", None)
            if err:
                print(f"warn: page {getattr(p, 'page_number', '?')} failed: {err}",
                      file=sys.stderr)
            continue
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
        raise ImportError(
            "requests is not installed. `pip install requests`."
        ) from e

    headers = {"Authorization": f"Bearer {_require_api_key()}"}
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
        _err(f"upload failed ({resp.status_code}): {resp.text}", code=3)
    job = resp.json()
    job_id = job.get("id") or job.get("job_id")
    if not job_id:
        _err(f"upload response missing job id: {json.dumps(job)[:500]}", code=3)

    deadline = time.monotonic() + poll_timeout
    backoff = 1.0
    while True:
        if time.monotonic() > deadline:
            _err(
                f"timed out after {poll_timeout:.0f}s waiting for job {job_id}.",
                code=4,
            )
        s = requests.get(f"{REST_BASE}/{job_id}", headers=headers, timeout=30)
        if s.status_code >= 400:
            _err(f"status check failed ({s.status_code}): {s.text}", code=3)
        payload = s.json()
        # Job metadata lives under .job.status in v2.
        status = (
            (payload.get("job") or {}).get("status")
            or payload.get("status")
            or ""
        ).upper()
        if status == "COMPLETED":
            break
        if status in ("FAILED", "CANCELLED"):
            _err(
                f"job {job_id} ended with {status}: {json.dumps(payload)[:500]}",
                code=3,
            )
        time.sleep(min(backoff, 5.0))
        backoff = min(backoff * 1.5, 5.0)

    expand = "markdown" if result_type == "markdown" else "text"
    r = requests.get(
        f"{REST_BASE}/{job_id}",
        headers=headers,
        params={"expand": expand},
        timeout=120,
    )
    if r.status_code >= 400:
        _err(f"result fetch failed ({r.status_code}): {r.text}", code=3)
    payload = r.json()

    text = _extract_rest_field(payload, expand)
    if not text:
        _err(
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

    # Some responses also expose `markdown_full` / `text_full`.
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


def build_parser():
    p = argparse.ArgumentParser(
        prog="llamaparse",
        description="Parse a document with LlamaParse (API v2).",
    )
    p.add_argument("input", type=Path, help="Path to the document to parse.")
    p.add_argument("--output", type=Path, default=None,
                   help="Output file path (default: <input>.md or <input>.txt).")
    p.add_argument("--result-type", choices=("markdown", "text"),
                   default="markdown",
                   help="Output format (default: markdown).")
    p.add_argument("--tier", choices=TIERS, default="cost_effective",
                   help="Quality / cost tier (default: cost_effective).")
    p.add_argument("--version", default=DEFAULT_VERSION,
                   help="Parse model version: 'latest' (default) or a dated "
                        "pin like '2026-04-09' for reproducibility.")
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
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)

    if not args.input.exists():
        _err(f"input file not found: {args.input}")
    _require_api_key()

    ext = ".md" if args.result_type == "markdown" else ".txt"
    out_path = args.output or args.input.with_suffix(ext)

    if args.rest:
        text = parse_with_rest(
            args.input, args.result_type, args.tier, args.version,
            args.poll_timeout,
        )
    else:
        try:
            text = parse_with_sdk(
                args.input, args.result_type, args.tier, args.version,
                args.auto_install,
            )
        except ImportError as e:
            print(f"note: {e}\nfalling back to REST.", file=sys.stderr)
            text = parse_with_rest(
                args.input, args.result_type, args.tier, args.version,
                args.poll_timeout,
            )

    if args.strip_noise:
        text, layout_dropped, images_dropped = strip_noise(text)
        print(
            f"strip-noise: dropped {layout_dropped} layout comments, "
            f"{images_dropped} repeating image refs",
            file=sys.stderr,
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text):,} chars to {out_path}")
    if args.stdout:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
