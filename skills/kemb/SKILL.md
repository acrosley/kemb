---
name: kemb
description: Comb a document corpus into agent-ready form using LlamaCloud document APIs (LlamaParse, LlamaClassify). Use when the user names Kemb, LlamaParse, or LlamaCloud; wants to parse a PDF / Word / scan to clean markdown; classify or categorize a document; or inventory / triage / scope a directory of documents before a batch run. Single-document facets plus a local zero-credit probe today; broader corpus orchestration (probe → plan → pass → mirror) in progress. Once parse yields markdown, do schema extraction and section splitting yourself — read the markdown; no API call needed.
---

# Kemb

**Kembing** — combing a document corpus into agent-ready form. Raw documents in, structured agent-readable mirror out.

This skill exposes two single-document facets backed by LlamaCloud APIs, plus a local `probe` facet that scopes a directory before you spend any credits:

| Facet     | Use for                                                | Facet doc                |
|-----------|--------------------------------------------------------|--------------------------|
| `parse`   | PDFs / Office / scans → clean markdown or text         | `references/parse.md`    |
| `classify`| Assign one of N labels with confidence + reasoning     | `references/classify.md` |
| `probe`   | Inventory / triage a directory locally — size, type, text samples | `references/probe.md` |

**Post-parse structured work is yours, not an API's.** Once `parse` has produced clean markdown, do schema extraction, classification refinement, and section splitting by reading the markdown directly — zero credits, zero plumbing, full conversation context. Only reach for `classify` when routing documents *before* parsing (e.g. scans you can't read locally, in `--mode multimodal`).

`probe` is the first shipped step of the "kembing" arc — probe → plan → pass → mirror. It walks a directory and reports per-file metadata with zero credits and no network call, so you can feel out a pile before parsing it. The rest of that arc (draft a plan, execute a pass, render into a markdown mirror with hash-stamped frontmatter and a queryable manifest) is the project's direction — see `docs/goal.txt` — and is still in progress. For now, route each request to the matching facet.

## Setup (shared across all facets)

The document facets (`parse`, `classify`) need `LLAMA_CLOUD_API_KEY` exported in the shell (`probe` is local-only and needs no key):

```bash
test -n "$LLAMA_CLOUD_API_KEY" && echo "key is set" || echo "MISSING: export LLAMA_CLOUD_API_KEY=llx-..."
```

Get a key at <https://cloud.llamaindex.ai/api-key>. Do not accept the key in chat — that puts secrets in transcripts. If outbound HTTPS to `api.cloud.llamaindex.ai` is blocked by a host allowlist (e.g. Cowork sandbox), see `references/troubleshooting.md`.

## Invoking a facet

If `kemb` is on the user's PATH (installed via `pipx install git+https://github.com/acrosley/kemb`), invoke directly:

```bash
kemb parse <file> --tier cost_effective
kemb classify <file> --rules @rules.json
kemb probe <directory>            # inventory a folder (zero credits, local)
kemb probe <directory> --sample   # + first words of each doc, for corpus triage
kemb doctor                       # preflight check
```

Otherwise fall back to the bundled shim from the skill directory, which adds the repo's `src/` to `sys.path`:

```bash
python scripts/kemb_cli.py parse <file> --tier cost_effective --auto-install
```

For the API-backed facets (`parse`, `classify`), pass `--auto-install` from the shim path — it `pip install`s `llama-cloud` on first run if it isn't importable; if the SDK can't install, those facets fall back to a `requests`-only REST path automatically. `probe` and `doctor` do **not** accept the flag — passing it there is a usage error (exit 2). (`probe` is fully local; `doctor` runs a non-billable HEAD reachability probe unless `--offline` is passed.)

## Routing — which facet for which request

- "Parse / OCR / convert to markdown / read this PDF" → `parse` (`references/parse.md`)
- "Pull these specific fields out as JSON" / "give me structured data" → check the file locally first: extract its text with pypdf (or read it directly for text formats). If real text comes back, work from that **full text** — no probe, no API call. Empty text means a scan: `parse` it, then extract from the markdown. Don't route a single known file through `probe` — probe inventories piles; for one file it's a detour. And never extract fields from a `probe --sample` snippet: samples are first-words truncations for triage and will silently drop fields that appear later in the document.
- "Classify / categorize / route this document by type" → if you can read it (text layer, or parsed markdown), classify it yourself; use `classify` for scans / layout-heavy files you can't read (`references/classify.md`)
- "Split this long document into intro / methodology / results / sections" → `parse` to markdown, then split by headings yourself (no API call)
- "What's in this folder? / inventory a directory / scope a batch before parsing / which of these files can LlamaCloud take?" → `probe` (`references/probe.md`)
- "What ARE these documents? / triage this corpus / which of these are scans / what's worth parsing?" → `probe --sample` (`references/probe.md`) — local first-words sample of every file, readable in one pass. For PDFs the sample marks `text="no-text"` (scans), you can still identify the content for free: you are multimodal — Read the PDF's first page (or render it to an image) and look at it before deciding whether and at what tier to parse.
- "What does each facet cost? / how does v2 of the API work?" → `references/rest_api.md`
- Setup failures, weird response shapes, network blocks, encrypted PDFs → `references/troubleshooting.md`

## What this skill does NOT do

- Schema extraction or section splitting via API — former `extract` / `split` facets were removed; once parse yields markdown, the agent does that work itself for zero credits.
- Embedding or vector storage — pair with a separate RAG pipeline.
- End-to-end corpus orchestration (plan / pass / mirror) — `probe` ships today as the local first step, but automated planning, batch execution, and the hash-stamped markdown mirror are still in progress; track them in `docs/goal.txt`.
- Store API keys — keys come from the environment, every run.
