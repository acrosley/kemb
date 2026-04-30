---
name: llamaparse
description: Use this skill whenever the user wants to parse a document with LlamaParse — including PDFs, Word docs, PowerPoint, Excel, images, scanned/OCR documents, or any complex document where layout matters (tables, multi-column text, forms). Trigger on phrases like "use LlamaParse", "parse this PDF with LlamaCloud", "extract markdown from this document", "OCR this scan", or whenever the user uploads a document and wants high-quality structured text or markdown back rather than raw text extraction. Also trigger when basic PDF text extraction has produced garbled output and the user needs a higher-quality parse. Prefer this skill over generic PDF text extraction whenever LlamaParse is mentioned by name or when output quality matters for downstream use (RAG ingestion, summarization, data extraction).
---

# LlamaParse

LlamaParse is LlamaIndex's hosted document parsing service. It turns messy real-world documents — PDFs with tables and multi-column layouts, scanned forms, Office files, images — into clean markdown or text that's actually usable downstream.

This skill uses the official Python SDK by default and falls back to direct REST calls when the SDK isn't installable.

## When to use this skill

Use it whenever a document needs parsing and either (a) the user explicitly mentions LlamaParse / LlamaCloud, or (b) the document has structure that simpler tools mangle — tables, multi-column layout, scanned pages, mixed text and images. For plain-text PDFs where pdfplumber or pypdf already produces clean output, those are fine; reach for LlamaParse when quality matters.

## Setup

Install the SDK (the `LlamaParse` class lives in `llama-cloud-services`, NOT in the bare `llama-cloud` package):

```bash
pip install llama-cloud-services --break-system-packages
```

Authentication: LlamaParse requires an API key from https://cloud.llamaindex.ai/api-key. The skill reads it from the `LLAMA_CLOUD_API_KEY` environment variable. The key never lands in code, chat history, or files.

Before parsing, verify the env var is set:

```bash
test -n "$LLAMA_CLOUD_API_KEY" && echo "key is set" || echo "MISSING: export LLAMA_CLOUD_API_KEY=llx-..."
```

If it's missing, ask the user to set it (`export LLAMA_CLOUD_API_KEY=llx-...` in their shell, or add it to their Cowork environment) before proceeding. Do not prompt for the key in chat — that puts secrets in transcripts.

**Network requirement:** the Cowork sandbox must be allowed to reach `api.cloud.llamaindex.ai`. If a proxy returns HTTP 403 on CONNECT, the host needs to be allowlisted in Cowork's Admin settings → Capabilities (owner-only on Team/Enterprise plans). Falling back to running the script outside the sandbox is always an option.

## Cost model

LlamaParse charges in credits per page, multiplied by a tier coefficient:

| Tier            | Multiplier (approx, verify on llamaindex.ai)     |
|-----------------|--------------------------------------------------|
| `fast`          | ~1 credit/page (text-only — no markdown)         |
| `cost_effective`| ~3 credits/page (default; balanced quality)      |
| `agentic`       | ~15 credits/page                                 |
| `agentic_plus`  | ~30+ credits/page (best quality, layout-perfect) |

Always count pages with `pdfinfo "$file"` or `pypdf` first and report `pages × tier_multiplier` to the user before calling the API on anything over ~10 pages. Get explicit confirmation for batches above 100 pages.

## Quick start

The bundled script handles the common case end-to-end:

```bash
python scripts/parse_document.py <input_file> --output <output_path> --result-type markdown --tier cost_effective
```

Flags:
- `--result-type {markdown,text}` — output format (default: markdown)
- `--output PATH` — destination file (default: `<input>.md` next to input)
- `--language CODE` — document language hint, e.g. `en`, `es` (default: `en`)
- `--tier {fast,cost_effective,agentic,agentic_plus}` — quality/cost tier (default: `cost_effective`). Note: `fast` cannot return markdown — only text.
- `--rest` — force the REST path even if the SDK is installed (useful for debugging)
- `--poll-timeout SECONDS` — REST mode only; defaults to 300

If the SDK isn't installable, `--rest` works with just the `requests` library.

## SDK usage

When the bundled script doesn't fit (batch jobs, custom pre/post-processing, integration into a larger pipeline), use the SDK directly:

```python
import asyncio
import os
from llama_cloud_services import LlamaParse  # NOT `from llama_cloud import LlamaParse`

parser = LlamaParse(
    api_key=os.environ["LLAMA_CLOUD_API_KEY"],
    # Quality/cost tier:
    #   "fast"           — text-only, cheapest, no markdown
    #   "cost_effective" — balanced (sensible default)
    #   "agentic"        — higher accuracy, slower
    #   "agentic_plus"   — best quality, most expensive
    tier="cost_effective",
    language="en",
)

async def parse_one(path: str) -> str:
    result = await parser.aparse(path)
    documents = await result.aget_markdown_documents(split_by_page=False)
    return "\n\n".join(d.text for d in documents)

markdown = asyncio.run(parse_one("./report.pdf"))
```

The result object also exposes:
- `aget_text_documents()` — plain text per document
- `aget_markdown_nodes(split_by_page=True)` / `aget_text_nodes(split_by_page=True)` — per-page nodes for chunking
- `aget_json()` — structured per-page output with items, tables, image references

Synchronous variants exist (drop the `a` prefix) but async is preferred for batch work.

## REST API usage

The full REST reference is in `references/rest_api.md`. The flow: POST file → poll job → fetch result with `?expand=markdown`. All requests need `Authorization: Bearer $LLAMA_CLOUD_API_KEY`.

## Output handling

After parsing, save the result somewhere the user can find it. In Cowork, that means writing under the workspace folder (or outputs directory) and sharing a `computer://` link. The bundled script does this automatically when `--output` points there.

For RAG/embedding workflows the user might want chunks rather than one big markdown blob — use `aget_markdown_nodes(split_by_page=True)` from the SDK, or parse first and chunk separately with the user's preferred chunker. Don't over-engineer chunking inside this skill.

## Troubleshooting

If parsing fails or returns unexpected output, see `references/troubleshooting.md`. Common issues: missing API key, sandbox network block (403 from proxy), file too large (default limit ~300MB), unsupported file type, a stuck job (poll timeout), or asking for `markdown` while using the `fast` tier (not supported — switch tier or request `text`). The script surfaces the underlying error message — pass it to the user verbatim rather than guessing.

## What this skill does NOT do

- It does not handle embedding or vector storage. Pair with a separate RAG pipeline.
- It does not parse with LlamaExtract (structured-schema extraction) — that's a sibling product. If the user wants schema-driven JSON extraction, mention it but don't try to fake it through LlamaParse.
- It does not store API keys. Keys come from the environment, every run.
