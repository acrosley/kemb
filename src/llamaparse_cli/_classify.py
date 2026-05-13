"""Classify — categorize a document into one of a defined set of classes.

REST: POST /api/v2/classify → poll GET /api/v2/classify/{job_id}
SDK:  client.classify.create(file_input=..., configuration={...})

The configuration carries `rules` (each rule: {type, description}) plus an
optional `mode` ("fast" or "multimodal"). The job returns the matched type,
a confidence score (0.0–1.0), and a brief reasoning string.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ._common import (
    API_HOST,
    auth_headers,
    coerce_json_arg,
    err,
    import_requests,
    load_sdk_client,
    poll_job,
    surface_api_error,
    upload_file_rest,
    upload_file_sdk,
    write_output,
)

REST_BASE = f"{API_HOST}/api/v2/classify"
CLASSIFY_MODES = ("fast", "multimodal")


def classify_with_sdk(input_path, rules, configuration, configuration_id,
                      mode, project_id, auto_install, poll_timeout):
    client = load_sdk_client(auto_install)
    if client is None:
        raise ImportError(
            "llama-cloud SDK not available. Install with "
            "`pip install llama-cloud` (or pass --auto-install to retry)."
        )

    file_id = upload_file_sdk(client, input_path)

    kwargs = {"file_input": file_id}
    if configuration_id:
        kwargs["configuration_id"] = configuration_id
    else:
        kwargs["configuration"] = _build_configuration(rules, configuration, mode)
    if project_id:
        kwargs["project_id"] = project_id

    try:
        job = client.classify.create(**kwargs)
    except Exception as e:
        surface_api_error("classify create failed", e)

    job_id = getattr(job, "id", None) or (job.get("id") if isinstance(job, dict) else None)
    if not job_id:
        err(f"classify create returned no job id: {job!r}", code=3)

    # SDK doesn't ship a wait_for_completion for classify, so poll via REST.
    final = poll_job(
        f"{REST_BASE}/{job_id}", auth_headers(), poll_timeout,
    )
    return _extract_result(final)


def classify_with_rest(input_path, rules, configuration, configuration_id,
                       mode, project_id, poll_timeout):
    requests = import_requests()
    headers = {**auth_headers(), "Content-Type": "application/json"}

    file_id = upload_file_rest(input_path)
    body = {"file_input": file_id}
    if configuration_id:
        body["configuration_id"] = configuration_id
    else:
        body["configuration"] = _build_configuration(rules, configuration, mode)
    if project_id:
        body["project_id"] = project_id

    resp = requests.post(REST_BASE, headers=headers, json=body, timeout=120)
    if resp.status_code >= 400:
        err(f"classify create failed ({resp.status_code}): {resp.text}", code=3)
    job = resp.json()
    job_id = job.get("id") or job.get("job_id") or (job.get("job") or {}).get("id")
    if not job_id:
        err(f"create response missing job id: {json.dumps(job)[:500]}", code=3)

    final = poll_job(f"{REST_BASE}/{job_id}", auth_headers(), poll_timeout)
    return _extract_result(final)


def _build_configuration(rules, configuration, mode) -> dict:
    cfg = dict(configuration or {})
    if rules is not None:
        cfg.setdefault("rules", rules)
    if mode and "mode" not in cfg:
        cfg["mode"] = mode
    if not cfg.get("rules"):
        err(
            "classify requires rules. Pass --rules @path/to/rules.json "
            "(a JSON list of {type, description} entries) or embed `rules` "
            "in --configuration, or use --configuration-id."
        )
    return cfg


def _extract_result(payload):
    """Pull the classification result out of the v2 response envelope."""
    candidate = None
    for key in ("result", "classification", "classify"):
        v = getattr(payload, key, None) if not isinstance(payload, dict) else payload.get(key)
        if v is not None:
            candidate = v
            break
    if candidate is None and isinstance(payload, dict):
        if "type" in payload and "confidence" in payload:
            candidate = payload

    if candidate is None:
        keys = list(payload.keys()) if isinstance(payload, dict) else dir(payload)
        err(f"could not locate classify result. Top-level keys: {keys[:20]}", code=3)

    if hasattr(candidate, "model_dump"):
        candidate = candidate.model_dump()
    elif hasattr(candidate, "dict"):
        try:
            candidate = candidate.dict()
        except Exception:
            pass
    return json.dumps(candidate, indent=2, default=str, ensure_ascii=False)


def _normalize_rules(value):
    """Accept a JSON list of {type, description} dicts."""
    if value is None:
        return None
    s = str(value).strip()
    if s.startswith("@"):
        path = s[1:]
        try:
            with open(path, "r", encoding="utf-8") as fh:
                s = fh.read()
        except OSError as e:
            err(f"could not read --rules from {path}: {e}")
    try:
        parsed = json.loads(s)
    except json.JSONDecodeError as e:
        err(f"invalid JSON for --rules: {e.msg} (line {e.lineno})")
    if not isinstance(parsed, list):
        err(f"--rules must be a JSON array, got {type(parsed).__name__}")
    for i, rule in enumerate(parsed):
        if not isinstance(rule, dict) or "type" not in rule or "description" not in rule:
            err(f"--rules[{i}] must be an object with `type` and `description`")
    return parsed


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "classify",
        help="Classify a document into one of a defined set of categories.",
        description=(
            "Categorize a document with LlamaClassify. Define categories as "
            "rules — each rule has a `type` (label) and a natural-language "
            "`description` of what belongs in that category."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  llamaparse classify ./doc.pdf --rules @rules.json\n"
            "  llamaparse classify ./doc.pdf --rules '[{\"type\":\"contract\",\"description\":\"legal agreement\"}]'\n"
            "  llamaparse classify ./doc.pdf --configuration-id cfg_xyz789\n"
        ),
    )
    p.add_argument("input", type=Path, help="Path to the document to classify.")
    p.add_argument("--output", type=Path, default=None,
                   help="Output file for the classification result JSON "
                        "(default: <input>.classify.json).")
    p.add_argument("--rules", default=None,
                   help="Categorization rules. JSON array of "
                        "{type, description} objects, inline or @file.")
    p.add_argument("--configuration", default=None,
                   help="Full ClassifyConfigurationParam JSON (inline or @file).")
    p.add_argument("--configuration-id", default=None,
                   help="Reference a saved configuration by id; mutually "
                        "exclusive with --configuration.")
    p.add_argument("--mode", choices=CLASSIFY_MODES, default=None,
                   help="Classification mode (default: server-chosen).")
    p.add_argument("--project-id", default=None,
                   help="Optional LlamaCloud project id to scope the job.")
    p.add_argument("--rest", action="store_true",
                   help="Force REST path even if the SDK is installed.")
    p.add_argument("--poll-timeout", type=float, default=600.0,
                   help="Max seconds to wait for the job.")
    p.add_argument("--auto-install", action="store_true",
                   help="If llama-cloud isn't importable, try `pip install` it.")
    p.add_argument("--stdout", action="store_true",
                   help="Also write the result to stdout.")
    p.set_defaults(func=run)
    return p


def run(args):
    if not args.input.exists():
        err(f"input file not found: {args.input}")
    if args.configuration and args.configuration_id:
        err("--configuration and --configuration-id are mutually exclusive.")

    rules = _normalize_rules(args.rules) if args.rules else None
    configuration = (
        coerce_json_arg(args.configuration, "--configuration")
        if args.configuration else None
    )

    out_path = args.output or args.input.with_suffix(".classify.json")

    if args.rest:
        text = classify_with_rest(
            args.input, rules, configuration, args.configuration_id,
            args.mode, args.project_id, args.poll_timeout,
        )
    else:
        try:
            text = classify_with_sdk(
                args.input, rules, configuration, args.configuration_id,
                args.mode, args.project_id, args.auto_install, args.poll_timeout,
            )
        except ImportError as e:
            print(f"note: {e}\nfalling back to REST.", file=sys.stderr)
            text = classify_with_rest(
                args.input, rules, configuration, args.configuration_id,
                args.mode, args.project_id, args.poll_timeout,
            )

    write_output(out_path, text)
    if args.stdout:
        sys.stdout.write(text)
    return 0
