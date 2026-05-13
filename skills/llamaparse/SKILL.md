---
name: llamaparse
description: Parse documents with LlamaIndex's LlamaParse v2 service — PDFs, Word, PowerPoint, Excel, images, and scans — into clean markdown or text. Use whenever the user names LlamaParse or LlamaCloud, asks to OCR a scan, or wants a higher-quality parse than pdfplumber/pypdf produces (tables, multi-column layout, mixed text + images).
---

# LlamaParse

LlamaParse is LlamaIndex's hosted document parsing service. It turns messy real-world documents — PDFs with tables and multi-column layouts, scanned forms, Office files, images — into clean markdown or text that's actually usable downstream.

This skill targets **LlamaParse API v2** via the official `llama-cloud` Python SDK (https://pypi.org/project/llama-cloud/). The legacy `llama-cloud-services` / `llama-parse` packages cover v1 and are slated for archive after roughly mid-2026; this skill does not use them.

## When to use

Use it when either (a) the user explicitly mentions LlamaParse / LlamaCloud, or (b) the document has structure that simpler tools mangle — tables, multi-column layout, scanned pages, mixed text and images. For plain-text PDFs where `pdfplumber` or `pypdf` already produces clean output, use those; reach for LlamaParse when quality matters.

## Setup

Authentication: the user must export `LLAMA_CLOUD_API_KEY` in their shell. Verify before parsing:

```bash
test -n "$LLAMA_CLOUD_API_KEY" && echo "key is set" || echo "MISSING: export LLAMA_CLOUD_API_KEY=llx-..."
```

If it's missing, ask the user to set it in their shell or host environment before proceeding. Do not prompt for the key in chat — that puts secrets in transcripts. Get a key at <https://cloud.llamaindex.ai/api-key>.

The bundled script (`scripts/parse_document.py`) accepts `--auto-install`, which will `pip install llama-cloud` on first run if it isn't already importable. Always pass `--auto-install` from this skill so the user doesn't have to manage Python deps manually.

If outbound HTTPS to `api.cloud.llamaindex.ai` is blocked (e.g. Cowork sandbox without allowlist), surface the upstream error verbatim and direct the user to **Settings → Capabilities → network allowlist**. Running the script outside the sandbox is always a fallback.

## Cost model

LlamaParse charges credits per page, multiplied by a tier coefficient. `fast` returns plain text only; the higher three tiers also expose a structured markdown expansion:

| Tier             | Multiplier (approx — verify on llamaindex.ai) | Best for                                       |
|------------------|-----------------------------------------------|------------------------------------------------|
| `fast`           | ~1 credit/page                                | Plain text, simple layouts                     |
| `cost_effective` | ~3 credits/page                               | Default. Text-heavy docs with light structure  |
| `agentic`        | ~15 credits/page                              | Tables, multi-column, mixed media              |
| `agentic_plus`   | ~30+ credits/page                             | Dense tables, charts, the hardest documents    |

Count pages with `pdfinfo "$file"` or `pypdf` first and report `pages × tier_multiplier` to the user before calling the API on anything over ~10 pages. Get explicit confirmation for batches above 100 pages.

## Versioning

v2 takes a `version` parameter on every parse request. Use `"latest"` during interactive use; pin to a dated version (e.g. `"2026-04-09"`) for reproducible production runs. The bundled script defaults to `"latest"`.

## Quick start

Run the bundled script from the skill directory:

```bash
python scripts/parse_document.py <input_file> --auto-install \
    --output <output_path> --result-type markdown --tier cost_effective
```

Flags:

- `--result-type {markdown,text}` — output format (default: `markdown`)
- `--output PATH` — destination file (default: `<input>.md` next to the input)
- `--tier {fast,cost_effective,agentic,agentic_plus}` — quality/cost tier (default: `cost_effective`)
- `--version` — parse model version (default: `latest`); pin to e.g. `2026-04-09` for reproducibility
- `--strip-noise` — post-process to drop LlamaParse layout-hint HTML comments (`<!-- layout: ... -->`) and recurring header/footer image refs (alt text seen 3+ times). Off by default; useful for narrative documents like deposition transcripts and reports.
- `--auto-install` — `pip install llama-cloud` if it isn't importable. Always pass this from the skill.
- `--rest` — force the REST path even if the SDK is installed (useful for debugging)
- `--poll-timeout SECONDS` — REST mode only; defaults to 600

> v2 auto-detects document language. The v1 `input_options.language` field was removed by LlamaIndex and is no longer accepted — sending it produces a `422 extra_forbidden` error.

If the SDK isn't installable for some reason, the script automatically falls back to REST using just the `requests` library.

## SDK usage (for custom pipelines)

When the bundled script doesn't fit (batch jobs, custom pre/post-processing, integration into a larger pipeline), use the SDK directly:

```python
from llama_cloud import LlamaCloud

client = LlamaCloud()  # reads LLAMA_CLOUD_API_KEY from env

with open("./report.pdf", "rb") as fh:
    result = client.parsing.parse(
        tier="cost_effective",       # fast | cost_effective | agentic | agentic_plus
        version="latest",             # or pin: "2026-04-09"
        upload_file=fh,               # pass the file directly — no separate upload step
        expand=["markdown"],          # or ["text"], or both, or ["items"]
    )

markdown = "\n\n".join(
    p.markdown for p in result.markdown.pages if getattr(p, "success", True)
)
```

`client.parsing.parse()` is a one-shot helper that internally calls `create()`, `wait_for_completion()`, and `get()` — no manual polling needed.

Other useful `expand` values:

- `expand=["text"]` — plain text per page (read as `result.text.pages[i].text`)
- `expand=["markdown", "text"]` — both
- `expand=["items"]` — structured per-page items (paragraphs, tables, image references)

For chunked output, iterate over `result.markdown.pages` directly rather than joining.

## REST API usage

The full REST reference is in `references/rest_api.md`. The flow: `POST /api/v2/parse/upload` (multipart: file + `configuration` JSON) → poll `GET /api/v2/parse/{job_id}` until `status == "COMPLETED"` → fetch with `?expand=markdown`. All requests need `Authorization: Bearer $LLAMA_CLOUD_API_KEY`. The configuration JSON requires both `tier` and `version`.

## Output handling

After parsing, save the result somewhere the user can find it. The bundled script writes to the `--output` path automatically. For RAG/embedding workflows, iterate over `result.markdown.pages` for per-page chunks instead of joining — or parse first and chunk separately with the user's preferred chunker.

## Troubleshooting

If parsing fails or returns unexpected output, see `references/troubleshooting.md`. Common issues: missing API key, network block on `api.cloud.llamaindex.ai`, file too large (default limit ~300MB), unsupported file type, a stuck job (poll timeout), or installing the wrong SDK package (must be `llama-cloud`, not `llama-cloud-services`). Surface the underlying error message to the user verbatim rather than guessing.

## What this skill does NOT do

- Embedding or vector storage. Pair with a separate RAG pipeline.
- Schema-driven structured extraction — that's the **`llamaextract`** sibling skill (LlamaExtract). If the user wants typed JSON fields out, route them there instead of trying to fake it through LlamaParse.
- Single-label document classification with confidence scores — see the **`llamaclassify`** sibling skill (LlamaClassify).
- Splitting a long document into typed sections by category — see the **`llamasplit`** sibling skill (LlamaSplit beta).
- Store API keys. Keys come from the environment, every run.
