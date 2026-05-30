# Split facet — LlamaSplit v1 beta

LlamaSplit is LlamaIndex's hosted document-splitting service. Provide a set of categories (each with a name + natural-language description) and a document; it returns per-segment page ranges, the matched category, and a confidence score per section. This skill targets **LlamaSplit API v1 beta** via the `llama-cloud` Python SDK (`client.beta.split`).

LlamaSplit is currently a **beta** endpoint. Response shape and the `/api/v1/beta/` path may change. Pin a working SDK version for production runs.

## When to use

Use it when the user wants a document **broken into typed sections** — separating contract clauses by type, segmenting a long report into intro / methodology / results / appendix, splitting a deposition transcript by speaker / topic, etc. If they want every field pulled, use `extract` (`extract.md`). If they want one label for the whole document, use `classify` (`classify.md`).

## Setup

Same auth as the rest of the suite: `LLAMA_CLOUD_API_KEY` exported in the shell.

```bash
test -n "$LLAMA_CLOUD_API_KEY" && echo "key is set" || echo "MISSING: export LLAMA_CLOUD_API_KEY=llx-..."
```

The bundled script accepts `--auto-install` to `pip install llama-cloud` on first run. Always pass it from this skill.

## Categories

Express section types as a JSON list of `{name, description}` objects. The `name` is the label that comes back per section; the `description` is the natural-language rule the splitter uses to match content:

```json
[
  { "name": "introduction",  "description": "Opening summary, motivation, and scope." },
  { "name": "methodology",   "description": "Description of methods, data, and procedures used." },
  { "name": "results",       "description": "Findings, analysis, and outcomes." },
  { "name": "discussion",    "description": "Interpretation of results, limitations, future work." },
  { "name": "references",    "description": "Bibliography, citations, works cited." }
]
```

Save to a file and pass with `--categories @cats.json`, or inline with `--categories '[{"name":...,"description":...}]'`.

For repeated workflows, save the configuration in LlamaCloud and pass `--configuration-id <cfg_id>`.

## Quick start

```bash
python scripts/run_split.py <input_file> --auto-install \
    --categories @cats.json \
    --output result.json
```

Flags:

- `--categories` — JSON list of `{name, description}` (file via `@path` or inline).
- `--configuration` — full split configuration JSON.
- `--configuration-id` — reference a saved configuration by id.
- `--splitting-strategy` — optional hint passed through to the API (e.g. `page`, `semantic`).
- `--project-id` — scope the job to a specific LlamaCloud project.
- `--output PATH` — destination file (default: `<input>.split.json`).
- `--rest` — force the REST path even if the SDK is installed.
- `--auto-install` — `pip install llama-cloud` if it isn't importable.
- `--poll-timeout SECONDS` — defaults to 600.

## Result shape

The response contains a list of segments. Each segment carries the matched category name, a page range, and a confidence score:

```json
{
  "segments": [
    { "name": "introduction", "start_page": 1, "end_page": 3, "confidence": 0.94 },
    { "name": "methodology",  "start_page": 4, "end_page": 9, "confidence": 0.88 },
    { "name": "results",      "start_page": 10, "end_page": 18, "confidence": 0.91 }
  ]
}
```

(Exact field names may evolve while the API is in beta — the bundled script preserves whatever the server returns.)

## SDK usage (custom pipelines)

```python
from llama_cloud import LlamaCloud

client = LlamaCloud()

with open("./report.pdf", "rb") as fh:
    f = client.files.create(file=fh, purpose="split")

# Convenience wrapper: creates + polls + returns the final result.
result = client.beta.split.split(
    document_input={"file_id": f.id},
    categories=[
        {"name": "introduction", "description": "Opening summary."},
        {"name": "results",      "description": "Findings and analysis."},
    ],
    splitting_strategy="semantic",  # optional
)
```

If you need finer control: `client.beta.split.create(...)` returns a job, then `client.beta.split.wait_for_completion(job_id)` polls until done.

## REST API

- `POST /api/v1/beta/split/jobs` — JSON body `{document_input, configuration, ...}`
- `GET /api/v1/beta/split/jobs/{split_job_id}` — poll for status
- Auth: `Authorization: Bearer $LLAMA_CLOUD_API_KEY`

**Note:** unlike parse/extract/classify, status values here are **lowercase**: `pending|processing|completed|failed|cancelled`. The bundled poller handles both cases.

## What this skill does NOT do

- Convert to markdown — use `parse` (`parse.md`).
- Pull structured fields — use `extract` (`extract.md`).
- Single-label categorization — use `classify` (`classify.md`).
- Store API keys. Keys come from the environment, every run.
