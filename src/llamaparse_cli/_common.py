"""Shared helpers for every LlamaCloud capability (parse, extract, classify, split).

Auth, error surfacing, SDK loading, and the REST polling loop all live here so
that the per-feature modules stay focused on what makes them different.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from typing import Any, Callable, NoReturn, Optional

API_HOST = "https://api.cloud.llamaindex.ai"
DEFAULT_VERSION = "latest"
PARSE_TIERS = ("fast", "cost_effective", "agentic", "agentic_plus")


def err(msg: str, code: int = 2) -> NoReturn:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def require_api_key() -> str:
    key = os.environ.get("LLAMA_CLOUD_API_KEY")
    if not key:
        err(
            "LLAMA_CLOUD_API_KEY is not set. Get a key at "
            "https://cloud.llamaindex.ai/api-key and export it before running."
        )
    return key


def surface_api_error(label: str, exc: Exception) -> None:
    body = getattr(exc, "body", None)
    if body is None:
        resp = getattr(exc, "response", None)
        if resp is not None:
            body = getattr(resp, "text", None) or repr(resp)
    if body is None:
        body = repr(exc)
    if isinstance(body, (dict, list)):
        body = json.dumps(body, indent=2, default=str)
    err(f"{label} ({type(exc).__name__}): {body}", code=3)


def try_install_sdk() -> bool:
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


def load_sdk_client(auto_install: bool):
    """Return an instantiated LlamaCloud SDK client, or None if unavailable."""
    try:
        from llama_cloud import LlamaCloud  # type: ignore
    except ImportError:
        if not auto_install:
            return None
        print("note: llama-cloud not installed; attempting pip install...",
              file=sys.stderr)
        if not try_install_sdk():
            return None
        try:
            from llama_cloud import LlamaCloud  # type: ignore
        except ImportError:
            return None
    require_api_key()
    return LlamaCloud()  # reads LLAMA_CLOUD_API_KEY from env


def auth_headers() -> dict:
    return {"Authorization": f"Bearer {require_api_key()}"}


def poll_job(
    status_url: str,
    headers: dict,
    poll_timeout: float,
    *,
    status_getter: Optional[Callable[[dict], str]] = None,
) -> dict:
    """Poll a job URL until status == COMPLETED, FAILED, or CANCELLED.

    `status_getter` extracts the status string from each response payload;
    defaults to the v2 parse shape (`.job.status` with `.status` fallback).
    Returns the final payload dict. Handles both uppercase (parse/extract/
    classify) and lowercase (split beta) status strings.
    """
    import requests  # type: ignore

    def _default_status(payload: dict) -> str:
        return (
            (payload.get("job") or {}).get("status")
            or payload.get("status")
            or ""
        )

    get_status = status_getter or _default_status
    deadline = time.monotonic() + poll_timeout
    backoff = 1.0
    while True:
        if time.monotonic() > deadline:
            err(
                f"timed out after {poll_timeout:.0f}s waiting for {status_url}.",
                code=4,
            )
        s = requests.get(status_url, headers=headers, timeout=30)
        if s.status_code >= 400:
            err(f"status check failed ({s.status_code}): {s.text}", code=3)
        payload = s.json()
        status = (get_status(payload) or "").upper()
        if status == "COMPLETED":
            return payload
        if status in ("FAILED", "CANCELLED"):
            err(
                f"job ended with {status}: {json.dumps(payload)[:500]}",
                code=3,
            )
        time.sleep(min(backoff, 5.0))
        backoff = min(backoff * 1.5, 5.0)


def upload_file_rest(file_path, purpose: str = "user_data") -> str:
    """Upload a file via REST and return its `file_id`.

    Extract / classify / split all consume an already-uploaded file id rather
    than the raw bytes (parse is the exception — it accepts a multipart upload
    in one shot). Endpoint: POST /api/v1/beta/files. `purpose` indicates how
    the file will be used (`user_data`, `parse`, `extract`, `classify`,
    `split`, `sheet`, or `agent_app`).
    """
    requests = import_requests()
    headers = auth_headers()
    with open(file_path, "rb") as fh:
        files = {"file": (file_path.name, fh)}
        data = {"purpose": purpose}
        resp = requests.post(
            f"{API_HOST}/api/v1/beta/files",
            headers=headers,
            files=files,
            data=data,
            timeout=300,
        )
    if resp.status_code >= 400:
        err(f"file upload failed ({resp.status_code}): {resp.text}", code=3)
    payload = resp.json()
    file_id = payload.get("id") or payload.get("file_id")
    if not file_id:
        err(f"upload response missing file id: {json.dumps(payload)[:500]}", code=3)
    return file_id


def upload_file_sdk(client, file_path, purpose: str = "user_data") -> str:
    """Upload a file via the SDK and return its `file_id`."""
    try:
        with open(file_path, "rb") as fh:
            result = client.files.create(file=fh, purpose=purpose)
    except Exception as e:
        surface_api_error("file upload failed", e)
    file_id = getattr(result, "id", None)
    if not file_id and isinstance(result, dict):
        file_id = result.get("id") or result.get("file_id")
    if not file_id:
        err(f"SDK upload returned no file id: {result!r}", code=3)
    return file_id


def import_requests():
    try:
        import requests  # type: ignore
        return requests
    except ImportError as e:
        raise ImportError(
            "requests is not installed. `pip install requests`."
        ) from e


def coerce_json_arg(value: Any, label: str) -> dict:
    """Accept either a JSON string or `@path/to/file.json` and return a dict."""
    if value is None:
        return {}
    if isinstance(value, dict):
        return value
    s = str(value).strip()
    if s.startswith("@"):
        path = s[1:]
        try:
            with open(path, "r", encoding="utf-8") as fh:
                s = fh.read()
        except OSError as e:
            err(f"could not read {label} from {path}: {e}")
    try:
        parsed = json.loads(s)
    except json.JSONDecodeError as e:
        err(f"invalid JSON for {label}: {e.msg} (line {e.lineno})")
    if not isinstance(parsed, dict):
        err(f"{label} must be a JSON object, got {type(parsed).__name__}")
    return parsed


def write_output(out_path, text: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text):,} chars to {out_path}")
