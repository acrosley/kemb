"""Extract — pull structured JSON out of a document against a schema.

REST: POST /api/v2/extract → poll GET /api/v2/extract/{job_id}
SDK:  client.extract.run(file_input=..., configuration={...})

The job consumes an uploaded file (by id) plus either an inline configuration
(carrying a `data_schema` JSON Schema) or the id of a saved configuration /
extraction agent. A `data_schema` is required either way.
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

REST_BASE = f"{API_HOST}/api/v2/extract"


def extract_with_sdk(input_path, schema, configuration, configuration_id,
                     project_id, auto_install):
    client = load_sdk_client(auto_install)
    if client is None:
        raise ImportError(
            "llama-cloud SDK not available. Install with "
            "`pip install llama-cloud` (or pass --auto-install to retry)."
        )

    file_id = upload_file_sdk(client, input_path, purpose="extract")
    config = _build_configuration(schema, configuration, configuration_id)

    kwargs = {"file_input": file_id}
    if configuration_id:
        kwargs["configuration_id"] = configuration_id
    else:
        kwargs["configuration"] = config
    if project_id:
        kwargs["project_id"] = project_id

    try:
        result = client.extract.run(**kwargs)
    except Exception as e:
        surface_api_error("extract failed", e)

    return _extract_data(result)


def extract_with_rest(input_path, schema, configuration, configuration_id,
                      project_id, poll_timeout):
    requests = import_requests()
    headers = {**auth_headers(), "Content-Type": "application/json"}

    file_id = upload_file_rest(input_path, purpose="extract")
    body = {"file_input": file_id}
    if configuration_id:
        body["configuration_id"] = configuration_id
    else:
        body["configuration"] = _build_configuration(
            schema, configuration, configuration_id
        )
    if project_id:
        body["project_id"] = project_id

    resp = requests.post(REST_BASE, headers=headers, json=body, timeout=120)
    if resp.status_code >= 400:
        err(f"extract create failed ({resp.status_code}): {resp.text}", code=3)
    job = resp.json()
    job_id = job.get("id") or job.get("job_id") or (job.get("job") or {}).get("id")
    if not job_id:
        err(f"create response missing job id: {json.dumps(job)[:500]}", code=3)

    final = poll_job(f"{REST_BASE}/{job_id}", auth_headers(), poll_timeout)
    return _extract_data(final)


def _schema_summary(schema):
    """Short description of a JSON Schema for the dry-run preview."""
    if schema is None:
        return None
    keys = list(schema.keys())[:6]
    props = schema.get("properties") if isinstance(schema, dict) else None
    if isinstance(props, dict):
        prop_keys = list(props.keys())
        suffix = f", properties: {prop_keys[:8]}"
        if len(prop_keys) > 8:
            suffix = suffix[:-1] + ", ...]"
    else:
        suffix = ""
    return f"keys={keys}{suffix}"


def _build_configuration(schema, configuration, configuration_id) -> dict:
    if configuration_id:
        return {}
    cfg = dict(configuration or {})
    if schema is not None:
        cfg.setdefault("data_schema", schema)
    if "data_schema" not in cfg:
        err(
            "extract requires a data schema. Pass --schema @path/to/schema.json, "
            "embed `data_schema` in --configuration, or use --configuration-id "
            "to reference a saved configuration."
        )
    return cfg


def _extract_data(payload):
    """Return the extracted data as a JSON string, regardless of envelope shape.

    The SDK's `ExtractV2Job` exposes the result under `.extract_result`; older
    or REST-direct payloads may use `data` / `extract` / `result`. Try them
    in priority order.
    """
    data = None
    for key in ("extract_result", "data", "extract", "extraction", "result", "results"):
        v = getattr(payload, key, None) if not isinstance(payload, dict) else payload.get(key)
        if v is not None:
            data = v
            break
    if data is None and isinstance(payload, dict):
        nested = payload.get("job") or {}
        for key in ("extract_result", "data", "extract", "result"):
            if key in nested:
                data = nested[key]
                break
    if data is None:
        if isinstance(payload, dict):
            keys = list(payload.keys())
        else:
            keys = [a for a in dir(payload) if not a.startswith("_")]
        err(f"could not locate extracted data. Visible fields: {keys[:20]}", code=3)
    if hasattr(data, "model_dump"):
        data = data.model_dump()
    elif hasattr(data, "dict"):
        try:
            data = data.dict()
        except Exception:
            pass
    return json.dumps(data, indent=2, default=str, ensure_ascii=False)


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "extract",
        help="Extract structured JSON from a document against a schema.",
        description=(
            "Extract structured data from a document using LlamaExtract. "
            "Provide a JSON Schema via --schema (file or literal), or "
            "reference a saved configuration via --configuration-id."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  kemb extract ./invoice.pdf --schema @invoice_schema.json\n"
            "  kemb extract ./form.pdf --configuration-id cfg_abc123\n"
        ),
    )
    p.add_argument("input", type=Path, help="Path to the document to extract from.")
    p.add_argument("--output", type=Path, default=None,
                   help="Output file path for the JSON result "
                        "(default: <input>.extract.json).")
    p.add_argument("--schema", default=None,
                   help="JSON Schema for the extraction. Pass either an inline "
                        "JSON string or `@path/to/schema.json`. Required unless "
                        "--configuration or --configuration-id supplies one.")
    p.add_argument("--configuration", default=None,
                   help="Full ExtractConfigurationParam JSON (inline or @file). "
                        "If both --schema and --configuration are given, "
                        "--schema is merged in as `data_schema`.")
    p.add_argument("--configuration-id", default=None,
                   help="Reference a saved configuration / extraction agent "
                        "by id; mutually exclusive with --configuration.")
    p.add_argument("--project-id", default=None,
                   help="Optional LlamaCloud project id to scope the job.")
    p.add_argument("--rest", action="store_true",
                   help="Force REST path even if the SDK is installed.")
    p.add_argument("--poll-timeout", type=float, default=600.0,
                   help="REST mode only. Max seconds to wait for the job.")
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
    if not args.schema and not args.configuration and not args.configuration_id:
        err(
            "extract requires a data schema. Pass --schema @path/to/schema.json, "
            "--configuration with `data_schema` embedded, or --configuration-id "
            "to reference a saved configuration."
        )

    schema = coerce_json_arg(args.schema, "--schema") if args.schema else None
    configuration = (
        coerce_json_arg(args.configuration, "--configuration")
        if args.configuration else None
    )

    out_path = args.output or args.input.with_suffix(".extract.json")

    if args.dry_run:
        transport = "REST (forced)" if args.rest else "SDK (REST fallback)"
        # Resolve the configuration that *would* have been sent, so users
        # catch missing fields before paying for an upload. If the inputs are
        # invalid, _build_configuration calls err() and exits non-zero here —
        # which is the point: dry-run surfaces the problem before any upload.
        resolved_cfg = _build_configuration(
            schema, configuration, args.configuration_id,
        )
        print(render_dry_run("extract", {
            "input": describe_input(args.input),
            "output": out_path,
            "schema": _schema_summary(schema),
            "configuration-id": args.configuration_id,
            "configuration": resolved_cfg if not args.configuration_id else None,
            "project-id": args.project_id,
            "transport": transport,
        }))
        return 0

    if args.rest:
        text = extract_with_rest(
            args.input, schema, configuration, args.configuration_id,
            args.project_id, args.poll_timeout,
        )
    else:
        try:
            text = extract_with_sdk(
                args.input, schema, configuration, args.configuration_id,
                args.project_id, args.auto_install,
            )
        except ImportError as e:
            print(f"note: {e}\nfalling back to REST.", file=sys.stderr)
            text = extract_with_rest(
                args.input, schema, configuration, args.configuration_id,
                args.project_id, args.poll_timeout,
            )

    write_output(out_path, text)
    if args.stdout:
        sys.stdout.write(text)
    return 0
