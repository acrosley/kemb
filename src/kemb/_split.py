"""Split — break a document into sections by category or strategy.

REST: POST /api/v1/beta/split/jobs → poll GET /api/v1/beta/split/jobs/{id}
SDK:  client.beta.split.split(categories=[...], document_input=..., splitting_strategy=...)

LlamaSplit is currently a v1 beta. Configuration carries `categories` (each
with a name + natural-language description) plus an optional `splitting_strategy`.
Statuses on this endpoint are lowercase (pending|processing|completed|failed|
cancelled), unlike the uppercase enums used by parse/extract/classify.
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
    describe_input,
    err,
    import_requests,
    load_sdk_client,
    poll_job,
    render_dry_run,
    surface_api_error,
    upload_file_rest,
    upload_file_sdk,
    write_output,
)

REST_BASE = f"{API_HOST}/api/v1/beta/split/jobs"


def split_with_sdk(input_path, categories, configuration, configuration_id,
                   splitting_strategy, project_id, auto_install, poll_timeout):
    client = load_sdk_client(auto_install)
    if client is None:
        raise ImportError(
            "llama-cloud SDK not available. Install with "
            "`pip install llama-cloud` (or pass --auto-install to retry)."
        )
    if not hasattr(client, "beta") or not hasattr(client.beta, "split"):
        raise ImportError(
            "Installed llama-cloud SDK has no `beta.split` resource. Upgrade "
            "with `pip install -U llama-cloud` or use --rest."
        )

    file_id = upload_file_sdk(client, input_path, purpose="split")
    document_input = {"file_id": file_id}

    kwargs = {"document_input": document_input}
    if configuration_id:
        kwargs["configuration_id"] = configuration_id
    elif configuration is not None or categories is not None or splitting_strategy:
        kwargs["configuration"] = _build_configuration(
            categories, configuration, splitting_strategy
        )
    if project_id:
        kwargs["project_id"] = project_id

    try:
        # The convenience wrapper combines create + poll, but only when we're
        # supplying an inline configuration (it builds one internally from
        # `categories` + `splitting_strategy`). When using a saved
        # configuration id, drop down to the explicit create + wait flow.
        if not configuration_id:
            cfg = kwargs.pop("configuration", {})
            final = client.beta.split.split(
                document_input=document_input,
                categories=cfg.get("categories") or categories or [],
                splitting_strategy=cfg.get("splitting_strategy") or splitting_strategy,
                project_id=project_id,
            )
        else:
            job = client.beta.split.create(**kwargs)
            job_id = getattr(job, "id", None) or (
                job.get("id") if isinstance(job, dict) else None
            )
            if not job_id:
                err(f"split create returned no job id: {job!r}", code=3)
            final = client.beta.split.wait_for_completion(
                job_id, project_id=project_id,
            )
    except Exception as e:
        surface_api_error("split failed", e)

    return _extract_result(final)


def split_with_rest(input_path, categories, configuration, configuration_id,
                    splitting_strategy, project_id, poll_timeout):
    requests = import_requests()
    headers = {**auth_headers(), "Content-Type": "application/json"}

    file_id = upload_file_rest(input_path, purpose="split")
    body = {"document_input": {"file_id": file_id}}
    if configuration_id:
        body["configuration_id"] = configuration_id
    else:
        body["configuration"] = _build_configuration(
            categories, configuration, splitting_strategy
        )
    if project_id:
        body["project_id"] = project_id

    resp = requests.post(REST_BASE, headers=headers, json=body, timeout=120)
    if resp.status_code >= 400:
        err(f"split create failed ({resp.status_code}): {resp.text}", code=3)
    job = resp.json()
    job_id = job.get("id") or job.get("split_job_id") or job.get("job_id")
    if not job_id:
        err(f"create response missing job id: {json.dumps(job)[:500]}", code=3)

    final = poll_job(
        f"{REST_BASE}/{job_id}", auth_headers(), poll_timeout,
        status_getter=_split_status,
    )
    return _extract_result(final)


def _split_status(payload):
    return (
        payload.get("status")
        or (payload.get("job") or {}).get("status")
        or ""
    )


def _build_configuration(categories, configuration, splitting_strategy) -> dict:
    cfg = dict(configuration or {})
    if categories is not None:
        cfg.setdefault("categories", categories)
    if splitting_strategy and "splitting_strategy" not in cfg:
        cfg["splitting_strategy"] = splitting_strategy
    if not cfg.get("categories"):
        err(
            "split requires categories. Pass --categories @path/to/cats.json "
            "(a JSON list of {name, description} entries) or embed `categories` "
            "in --configuration, or use --configuration-id."
        )
    return cfg


def _extract_result(payload):
    candidate = None
    for key in ("result", "split", "segments", "sections"):
        v = getattr(payload, key, None) if not isinstance(payload, dict) else payload.get(key)
        if v is not None:
            candidate = v
            break
    if candidate is None:
        # No recognized result key. Mirror extract/classify and fail loud
        # rather than silently emitting the raw job envelope (status, ids,
        # timestamps) as a success — that would look like a clean split that
        # actually produced no segments. Beta shapes drift, so list what we
        # did see to make the next fix obvious.
        if hasattr(payload, "model_dump"):
            visible = payload.model_dump()
        elif isinstance(payload, dict):
            visible = payload
        else:
            visible = {"repr": repr(payload)}
        keys = list(visible)[:20] if isinstance(visible, dict) else visible
        err(
            "could not locate split result in the completed job "
            f"(looked for result/split/segments/sections). Visible fields: {keys}",
            code=3,
        )

    if hasattr(candidate, "model_dump"):
        candidate = candidate.model_dump()
    elif hasattr(candidate, "dict"):
        try:
            candidate = candidate.dict()
        except Exception:
            pass
    return json.dumps(candidate, indent=2, default=str, ensure_ascii=False)


def _normalize_categories(value):
    if value is None:
        return None
    s = str(value).strip()
    if s.startswith("@"):
        path = s[1:]
        try:
            with open(path, "r", encoding="utf-8") as fh:
                s = fh.read()
        except OSError as e:
            err(f"could not read --categories from {path}: {e}")
    try:
        parsed = json.loads(s)
    except json.JSONDecodeError as e:
        err(f"invalid JSON for --categories: {e.msg} (line {e.lineno})")
    if not isinstance(parsed, list):
        err(f"--categories must be a JSON array, got {type(parsed).__name__}")
    for i, cat in enumerate(parsed):
        if not isinstance(cat, dict) or "name" not in cat or "description" not in cat:
            err(f"--categories[{i}] must be an object with `name` and `description`")
    return parsed


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "split",
        help="Split a document into sections by category (LlamaSplit beta).",
        description=(
            "Break a document into sections using LlamaSplit. Define each "
            "section type as a category with a name + natural-language "
            "description; LlamaSplit assigns page ranges and confidence "
            "scores per section. Currently a v1 beta endpoint."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  kemb split ./report.pdf --categories @cats.json\n"
            "  kemb split ./report.pdf --categories '[{\"name\":\"intro\",\"description\":\"opening summary\"}]'\n"
            "  kemb split ./report.pdf --configuration-id cfg_split_1\n"
        ),
    )
    p.add_argument("input", type=Path, help="Path to the document to split.")
    p.add_argument("--output", type=Path, default=None,
                   help="Output file for the split result JSON "
                        "(default: <input>.split.json).")
    p.add_argument("--categories", default=None,
                   help="JSON array of {name, description} category objects, "
                        "inline or @file.")
    p.add_argument("--configuration", default=None,
                   help="Full split configuration JSON (inline or @file).")
    p.add_argument("--configuration-id", default=None,
                   help="Reference a saved configuration by id; mutually "
                        "exclusive with --configuration.")
    p.add_argument("--splitting-strategy", default=None,
                   help="Optional splitting strategy hint passed through to "
                        "the API (e.g. 'page', 'semantic').")
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
    p.add_argument("--dry-run", action="store_true",
                   help="Validate inputs and print the resolved plan without "
                        "uploading the document or starting a job (zero credits).")
    p.set_defaults(func=run)
    return p


def run(args):
    if not args.input.exists():
        err(f"input file not found: {args.input}")
    if args.configuration and args.configuration_id:
        err("--configuration and --configuration-id are mutually exclusive.")
    if not args.categories and not args.configuration and not args.configuration_id:
        err(
            "split requires categories. Pass --categories @path/to/cats.json "
            "(a JSON list of {name, description} entries), --configuration with "
            "`categories` embedded, or --configuration-id."
        )

    categories = _normalize_categories(args.categories) if args.categories else None
    configuration = (
        coerce_json_arg(args.configuration, "--configuration")
        if args.configuration else None
    )

    out_path = args.output or args.input.with_suffix(".split.json")

    if args.dry_run:
        transport = "REST (forced)" if args.rest else "SDK (REST fallback)"
        if args.configuration_id:
            resolved_cfg = None
            category_names = None
        else:
            resolved_cfg = _build_configuration(
                categories, configuration, args.splitting_strategy
            )
            category_names = (
                [c.get("name") for c in resolved_cfg.get("categories", [])]
                if resolved_cfg.get("categories") else None
            )
        print(render_dry_run("split", {
            "input": describe_input(args.input),
            "output": out_path,
            "categories": category_names,
            "splitting-strategy": args.splitting_strategy,
            "configuration-id": args.configuration_id,
            "configuration": resolved_cfg,
            "project-id": args.project_id,
            "transport": transport,
        }))
        return 0

    if args.rest:
        text = split_with_rest(
            args.input, categories, configuration, args.configuration_id,
            args.splitting_strategy, args.project_id, args.poll_timeout,
        )
    else:
        try:
            text = split_with_sdk(
                args.input, categories, configuration, args.configuration_id,
                args.splitting_strategy, args.project_id, args.auto_install,
                args.poll_timeout,
            )
        except ImportError as e:
            print(f"note: {e}\nfalling back to REST.", file=sys.stderr)
            text = split_with_rest(
                args.input, categories, configuration, args.configuration_id,
                args.splitting_strategy, args.project_id, args.poll_timeout,
            )

    write_output(out_path, text)
    if args.stdout:
        sys.stdout.write(text)
    return 0
