---
name: kemb
description: Comb a document corpus into agent-ready form using LlamaCloud document APIs (LlamaParse, LlamaExtract, LlamaClassify, LlamaSplit). Use when the user names Kemb, LlamaParse, or LlamaCloud; wants to parse a PDF / Word / scan to clean markdown; pull structured JSON from a document against a schema; classify or categorize a document; split a long document into typed sections; or inventory / scope a directory of documents before a batch run. Single-document facets plus a local zero-credit probe today; broader corpus orchestration (probe → plan → pass → mirror) in progress.
---

# Kemb

**Kembing** — combing a document corpus into agent-ready form. Raw documents in, structured agent-readable mirror out.

This skill exposes four single-document facets backed by LlamaCloud APIs, plus a local `probe` facet that scopes a directory before you spend any credits:

| Facet     | Use for                                                | Facet doc                |
|-----------|--------------------------------------------------------|--------------------------|
| `parse`   | PDFs / Office / scans → clean markdown or text         | `references/parse.md`    |
| `extract` | Pull structured JSON against a JSON Schema             | `references/extract.md`  |
| `classify`| Assign one of N labels with confidence + reasoning     | `references/classify.md` |
| `split`   | Break a long doc into typed sections by category       | `references/split.md`    |
| `probe`   | Inventory a directory locally — size, type, support    | `references/probe.md`    |

`probe` is the first shipped step of the "kembing" arc — probe → plan → pass → mirror. It walks a directory and reports per-file metadata with zero credits and no network call, so you can feel out a pile before parsing it. The rest of that arc (draft a plan, execute a pass, render into a markdown mirror with hash-stamped frontmatter and a queryable manifest) is the project's direction — see `docs/goal.txt` — and is still in progress. For now, route each request to the matching facet.

## Setup (shared across all facets)

The four document facets need `LLAMA_CLOUD_API_KEY` exported in the shell (`probe` is local-only and needs no key):

```bash
test -n "$LLAMA_CLOUD_API_KEY" && echo "key is set" || echo "MISSING: export LLAMA_CLOUD_API_KEY=llx-..."
```

Get a key at <https://cloud.llamaindex.ai/api-key>. Do not accept the key in chat — that puts secrets in transcripts. If outbound HTTPS to `api.cloud.llamaindex.ai` is blocked by a host allowlist (e.g. Cowork sandbox), see `references/troubleshooting.md`.

## Invoking a facet

If `kemb` is on the user's PATH (installed via `pipx install git+https://github.com/acrosley/kemb`), invoke directly:

```bash
kemb parse <file> --tier cost_effective
kemb extract <file> --schema @schema.json
kemb classify <file> --rules @rules.json
kemb split <file> --categories @cats.json
kemb probe <directory>            # inventory a folder (zero credits, local)
kemb probe <directory> --sample   # + first words of each doc, for corpus triage
kemb doctor                       # preflight check
```

Otherwise fall back to the bundled shim from the skill directory, which adds the repo's `src/` to `sys.path`:

```bash
python scripts/kemb_cli.py parse <file> --tier cost_effective --auto-install
```

Always pass `--auto-install` from the shim path — it `pip install`s `llama-cloud` on first run if it isn't importable. If the SDK can't install, every facet falls back to a `requests`-only REST path automatically.

## Routing — which facet for which request

- "Parse / OCR / convert to markdown / read this PDF" → `parse` (`references/parse.md`)
- "Pull these specific fields out as JSON" / "give me structured data" → `extract` (`references/extract.md`)
- "Classify / categorize / route this document by type" → `classify` (`references/classify.md`)
- "Split this long document into intro / methodology / results / sections" → `split` (`references/split.md`)
- "What's in this folder? / inventory a directory / scope a batch before parsing / which of these files can LlamaCloud take?" → `probe` (`references/probe.md`)
- "What ARE these documents? / triage this corpus / which of these are scans / what's worth parsing?" → `probe --sample` (`references/probe.md`) — local first-words sample of every file, readable in one pass
- "What does each facet cost? / how does v2 of the API work?" → `references/rest_api.md`
- Setup failures, weird response shapes, network blocks, encrypted PDFs → `references/troubleshooting.md`

## What this skill does NOT do

- Embedding or vector storage — pair with a separate RAG pipeline.
- End-to-end corpus orchestration (plan / pass / mirror) — `probe` ships today as the local first step, but automated planning, batch execution, and the hash-stamped markdown mirror are still in progress; track them in `docs/goal.txt`.
- Store API keys — keys come from the environment, every run.
