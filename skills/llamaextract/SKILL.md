---
name: llamaextract
description: Extract structured JSON from a document against a JSON Schema, using LlamaIndex's LlamaExtract v2 service. Use whenever the user names LlamaExtract or asks to pull structured fields (invoice line items, contract terms, form data, named entities, etc.) out of a PDF or other document and wants the result as JSON or a schema-conformant object.
---

# LlamaExtract

LlamaExtract is LlamaIndex's hosted schema-driven extraction service. Give it a document and a JSON Schema; it returns a JSON object that conforms to the schema. This skill targets **LlamaExtract API v2** via the `llama-cloud` Python SDK.

## When to use

Use it when (a) the user explicitly mentions LlamaExtract / structured extraction, or (b) they have a defined shape they want pulled out — invoices, contracts, forms, anything where "I want these specific fields" is more useful than "give me the markdown." For ad-hoc reading / summarization, use the `llamaparse` skill instead.

## Setup

Same auth as parse: requires `LLAMA_CLOUD_API_KEY` exported in the shell.

```bash
test -n "$LLAMA_CLOUD_API_KEY" && echo "key is set" || echo "MISSING: export LLAMA_CLOUD_API_KEY=llx-..."
```

If missing, ask the user to set it in their shell or host environment. Get a key at <https://cloud.llamaindex.ai/api-key>. Do not prompt for the key in chat.

The bundled script accepts `--auto-install`, which `pip install`s `llama-cloud` on first run if it isn't already importable. Always pass `--auto-install` from this skill.

## Schema

Extraction requires a **JSON Schema** describing the shape you want back. The simplest form:

```json
{
  "type": "object",
  "properties": {
    "invoice_number": { "type": "string" },
    "total_amount":   { "type": "number" },
    "line_items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "description": { "type": "string" },
          "quantity":    { "type": "integer" },
          "unit_price":  { "type": "number" }
        }
      }
    }
  },
  "required": ["invoice_number", "total_amount"]
}
```

Save the schema to a file and pass it with `--schema @path/to/schema.json`, or inline a small one with `--schema '{"type":"object",...}'`.

For repeated runs against the same shape, create a saved **configuration / extraction agent** in LlamaCloud and pass `--configuration-id <cfg_id>` instead — the schema lives server-side.

## Quick start

```bash
python scripts/run_extract.py <input_file> --auto-install \
    --schema @schema.json \
    --output result.json
```

Flags:

- `--schema` — JSON Schema (file via `@path` or inline JSON). Required unless `--configuration-id` is given.
- `--configuration` — full `ExtractConfigurationParam` JSON (advanced; lets you set extra options alongside `data_schema`).
- `--configuration-id` — reference a saved configuration / extraction agent by id.
- `--project-id` — scope the job to a specific LlamaCloud project.
- `--output PATH` — destination file (default: `<input>.extract.json`).
- `--rest` — force the REST path even if the SDK is installed.
- `--auto-install` — `pip install llama-cloud` if it isn't importable.
- `--poll-timeout SECONDS` — REST mode only; defaults to 600.

## SDK usage (custom pipelines)

```python
from llama_cloud import LlamaCloud

client = LlamaCloud()  # reads LLAMA_CLOUD_API_KEY

# Upload the file first — extract takes a file id, not raw bytes.
with open("./invoice.pdf", "rb") as fh:
    f = client.files.create(upload_file=fh)

result = client.extract.run(
    file_input=f.id,
    configuration={
        "data_schema": {  # JSON Schema
            "type": "object",
            "properties": {"invoice_number": {"type": "string"}},
        },
    },
)
# result.data — the extracted JSON object
```

`extract.run(...)` is a one-shot helper that internally calls `create()` + `wait_for_completion()` + `get()`. If you need finer control (custom backoff, partial progress, etc.) call those primitives directly.

## REST API

- `POST /api/v2/extract` — JSON body `{file_input, configuration, ...}`
- `GET /api/v2/extract/{job_id}` — poll for status; statuses `PENDING|RUNNING|COMPLETED|FAILED`
- Auth: `Authorization: Bearer $LLAMA_CLOUD_API_KEY`

See `../llamaparse/references/rest_api.md` for the broader v2 lifecycle pattern (upload → poll → fetch), which is shared across parse / extract / classify.

## Cost

Extract is billed per page processed, similar to parse. Verify current pricing at <https://cloud.llamaindex.ai> before large batches and surface the page-count estimate to the user for anything over ~10 pages.

## What this skill does NOT do

- Parsing to markdown/text — use the `llamaparse` skill instead.
- Classification or document splitting — see the `llamaclassify` and `llamasplit` skills.
- Store API keys. Keys come from the environment, every run.
