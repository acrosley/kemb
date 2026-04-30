---
name: llamaparse
description: Parse documents with LlamaIndex's LlamaParse v2 service — PDFs, Word, PowerPoint, Excel, images, and scans — into clean markdown or text. Use whenever the user names LlamaParse or LlamaCloud, asks to OCR a scan, or wants a higher-quality parse than pdfplumber/pypdf produces (tables, multi-column layout, mixed text + images).
---

# LlamaParse

LlamaParse is LlamaIndex's hosted document parsing service. It turns messy real-world documents — PDFs with tables and multi-column layouts, scanned forms, Office files, images — into clean markdown or text that's actually usable downstream.

This skill targets **LlamaParse API v2 only**. The legacy `llama-cloud-services` and `llama-parse` packages (v1) are deprecated by LlamaIndex and slated for archive after May 1, 2026; this skill uses the new `llama-cloud` SDK and v2 REST endpoints exclusively.

## When to use

Use it when either (a) the user explicitly mentions LlamaParse / LlamaCloud, or (b) the document has structure that simpler tools mangle — tables, multi-column layout, scanned pages, mixed text and images. For plain-text PDFs where `pdfplumber` or `pypdf` already produces clean output, use those; reach for LlamaParse when quality matters.

## Setup

Install the v2 SDK:

```bash
pip install llama-cloud --break-system-packages
```

Do **not** install `llama-cloud-services` or `llama-parse` for this skill — those are v1 and will not be maintained past May 2026.

Authentication: get an API key at <https://cloud.llamaindex.ai/api-key>. The skill reads it from the `LLAMA_CLOUD_API_KEY` environment variable. The key never lands in code, chat history, or files.

Before parsing, verify the env var is set:

```bash
test -n "$LLAMA_CLOUD_API_KEY" && echo "key is set" || echo "MISSING: export LLAMA_CLOUD_API_KEY=llx-..."
```

If it's missing, ask the user to set it in their shell or host environment before proceeding. Do not prompt for the key in chat — that puts secrets in transcripts.

If outbound HTTPS to `api.cloud.llamaindex.ai` is blocked by a sandbox or proxy, the host needs to be on the network allowlist. Falling back to running the script outside the sandbox is always an option. (See the host's documentation for allowlist configuration.)

## Cost model

LlamaParse charges credits per page, multiplied by a tier coefficient. v2 supports markdown output on every tier (this is a change from v1):

| Tier             | Multiplier (approx — verify on llamaindex.ai) | Best for                                       |
|------------------|-----------------------------------------------|------------------------------------------------|
| `fast`           | ~1 credit/page                                | Plain text, simple layouts                     |
| `cost_effective` | ~3 credits/page                               | Default. Text-heavy docs with light structure  |
| `agentic`        | ~15 credits/page                              | Tables, multi-column, mixed media              |
| `agentic_plus`   | ~30+ credits/page                             | Dense tables, charts, the hardest documents    |

Always count pages with `pdfinfo "$file"` or `pypdf` first and report `pages × tier_multiplier` to the user before calling the API on anything over ~10 pages. Get explicit confirmation for batches above 100 pages.

## Versioning

v2 takes a `version` parameter on every parse request. Use `"latest"` during interactive use; pin to a dated version (e.g. `"2026-01-08"`) for reproducible production runs. The bundled script defaults to `"latest"`.

## Quick start

The bundled script handles the common case end-to-end:

```bash
python scripts/parse_document.py <input_file> --output <output_path> --result-type markdown --tier cost_effective
```

Flags:

- `--result-type {markdown,text}` — output format (default: `markdown`)
- `--output PATH` — destination file (default: `<input>.md` next to the input)
- `--language CODE` — document language hint, e.g. `en`, `es` (default: `en`)
- `--tier {fast,cost_effective,agentic,agentic_plus}` — quality/cost tier (default: `cost_effective`)
- `--version` — parse model version (default: `latest`); pin to e.g. `2026-01-08` for reproducibility
- `--rest` — force the REST path even if the SDK is installed (useful for debugging)
- `--poll-timeout SECONDS` — REST mode only; defaults to 300

If the SDK isn't installable, `--rest` works with just the `requests` library.

## SDK usage

When the bundled script doesn't fit (batch jobs, custom pre/post-processing, integration into a larger pipeline), use the SDK directly:

```python
from llama_cloud import LlamaCloud

client = LlamaCloud()  # reads LLAMA_CLOUD_API_KEY from env

with open("./report.pdf", "rb") as fh:
    uploaded = client.files.create(file=fh, purpose="parse")

result = client.parsing.parse(
    file_id=uploaded.id,
    tier="cost_effective",          # fast | cost_effective | agentic | agentic_plus
    version="latest",                # or pin: "2026-01-08"
    input_options={"language": "en"},
    expand=["markdown"],             # or ["text"], or both
)

markdown = "\n\n".join(p.markdown for p in result.markdown.pages)
```

`client.parsing.parse()` blocks until the job completes — no manual polling needed.

Other useful expansions:

- `expand=["text"]` — plain text per page
- `expand=["markdown", "text"]` — both
- `expand=["items"]` — structured per-page items (paragraphs, tables, image references)

For chunked output, iterate over `result.markdown.pages` directly rather than joining.

## REST API usage

The full REST reference is in `references/rest_api.md`. The flow: POST file + configuration JSON → poll job → fetch result with `?expand=markdown`. All requests need `Authorization: Bearer $LLAMA_CLOUD_API_KEY`. The configuration JSON requires both `tier` and `version`.

## Output handling

After parsing, save the result somewhere the user can find it. The bundled script writes to the `--output` path automatically. For RAG/embedding workflows, iterate over `result.markdown.pages` for per-page chunks instead of joining — or parse first and chunk separately with the user's preferred chunker.

## Troubleshooting

If parsing fails or returns unexpected output, see `references/troubleshooting.md`. Common issues: missing API key, network block on `api.cloud.llamaindex.ai`, file too large (default limit ~300MB), unsupported file type, a stuck job (poll timeout), or installing the wrong SDK package (must be `llama-cloud`, not `llama-cloud-services`). Surface the underlying error message to the user verbatim rather than guessing.

## What this skill does NOT do

- Embedding or vector storage. Pair with a separate RAG pipeline.
- LlamaExtract (structured-schema extraction) — sibling product in the same SDK. If the user wants schema-driven JSON extraction, mention it but don't try to fake it through LlamaParse.
- Store API keys. Keys come from the environment, every run.
- Target API v1.
