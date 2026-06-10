# Classify facet — LlamaClassify v2

LlamaClassify is LlamaIndex's hosted document categorization service. Define categories as natural-language rules; it returns the matched category, a confidence score (0.0–1.0), and a brief reasoning string. This skill targets **LlamaClassify API v2** via the `llama-cloud` Python SDK.

## When to use

Use it when the user wants to **assign one of N labels** to a document — routing intake forms, sorting contracts vs invoices, flagging complaint type, gating a downstream workflow on document type. If they want every field pulled out, use the `extract` facet (`extract.md`) instead. If they want markdown, use `parse` (`parse.md`).

## Setup

Same auth as parse / extract: `LLAMA_CLOUD_API_KEY` exported in the shell.

```bash
test -n "$LLAMA_CLOUD_API_KEY" && echo "key is set" || echo "MISSING: export LLAMA_CLOUD_API_KEY=llx-..."
```

The bundled shim accepts `--auto-install` to `pip install llama-cloud` on first run. Always pass it from this skill.

## Rules

Categories are expressed as a JSON list of `{type, description}` objects. The `type` is the label that will come back; the `description` is the natural-language rule the classifier uses to decide:

```json
[
  { "type": "invoice",      "description": "A bill or invoice requesting payment for goods or services." },
  { "type": "contract",     "description": "A legal agreement between two or more parties." },
  { "type": "receipt",      "description": "Proof of completed payment for goods or services." },
  { "type": "other",        "description": "Anything that doesn't fit the categories above." }
]
```

Save the rules to a file and pass with `--rules @rules.json`, or inline a small list with `--rules '[{"type":...,"description":...}]'`.

For repeated workflows, save the configuration in LlamaCloud and pass `--configuration-id <cfg_id>` instead.

## Quick start

```bash
python scripts/kemb_cli.py classify <input_file> --auto-install \
    --rules @rules.json \
    --output result.json
```

Flags:

- `--rules` — JSON list of `{type, description}` rules (file via `@path` or inline).
- `--configuration` — full `ClassifyConfigurationParam` JSON, if you need to set advanced options alongside the rules.
- `--configuration-id` — reference a saved configuration by id.
- `--mode {fast,multimodal}` — `fast` is text-only and cheap; `multimodal` reads images/layout (better for scans, layout-heavy docs).
- `--project-id` — scope the job to a specific LlamaCloud project.
- `--output PATH` — destination file (default: `<input>.classify.json`).
- `--rest` — force the REST path even if the SDK is installed.
- `--auto-install` — `pip install llama-cloud` if it isn't importable.
- `--poll-timeout SECONDS` — defaults to 600.

## Result shape

```json
{
  "type": "invoice",
  "confidence": 0.92,
  "reasoning": "The document lists itemized charges, a total due, and a payment-by date — characteristic of an invoice."
}
```

Use `confidence` to decide whether to auto-route or to escalate for human review. A common pattern: confidence ≥ 0.85 → auto-route; otherwise queue for review.

## SDK usage (custom pipelines)

```python
from llama_cloud import LlamaCloud

client = LlamaCloud()

with open("./doc.pdf", "rb") as fh:
    f = client.files.create(file=fh, purpose="classify")

job = client.classify.create(
    file_input=f.id,
    configuration={
        "rules": [
            {"type": "invoice",  "description": "A bill requesting payment."},
            {"type": "contract", "description": "A legal agreement between parties."},
        ],
        "mode": "fast",
    },
)
# Poll client.classify.get(job.id) until status == COMPLETED.
```

The SDK does **not** ship a `wait_for_completion` helper for classify (it does for parse/extract/split). Poll `client.classify.get(job_id)` manually, or use the bundled shim — it handles polling.

## REST API

- `POST /api/v2/classify` — JSON body `{file_input, configuration, ...}`
- `GET /api/v2/classify/{job_id}` — poll for status
- Auth: `Authorization: Bearer $LLAMA_CLOUD_API_KEY`

Status enum is uppercase: `PENDING|RUNNING|COMPLETED|FAILED`.

## What this skill does NOT do

- Pull structured fields from the document — use `extract` (`extract.md`).
- Split a document into sections — use `split` (`split.md`).
- Convert to markdown — use `parse` (`parse.md`).
- Store API keys. Keys come from the environment, every run.
