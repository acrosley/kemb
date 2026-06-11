---
name: kemb
description: Comb a document corpus into agent-ready form using LlamaCloud document APIs (LlamaParse, LlamaClassify). Use when the user names Kemb, LlamaParse, or LlamaCloud; wants to parse a PDF / Word / scan to clean markdown; classify or categorize a document; inventory / triage / scope a directory of documents before a batch run; or maintain / search a persistent index of a large corpus. Single-document facets plus local zero-credit probe and index today; broader corpus orchestration (probe → plan → pass → mirror) in progress. Once parse yields markdown, do schema extraction and section splitting yourself — read the markdown; no API call needed.
---

# Kemb

**Kembing** — combing a document corpus into agent-ready form. Raw documents in, structured agent-readable mirror out.

This skill exposes two single-document facets backed by LlamaCloud APIs, plus two local facets that scope a corpus before you spend any credits:

| Facet     | Use for                                                | Facet doc                |
|-----------|--------------------------------------------------------|--------------------------|
| `parse`   | PDFs / Office / scans → clean markdown or text         | `references/parse.md`    |
| `classify`| Assign one of N labels with confidence + reasoning     | `references/classify.md` |
| `probe`   | One-shot inventory / triage of a directory — size, type, text samples | `references/probe.md` |
| `index`   | Persistent SQLite inventory of a big corpus — incremental rescans, dedup, full-text search | `references/index.md` |

**Post-parse structured work is yours, not an API's.** Once `parse` has produced clean markdown, do schema extraction, classification refinement, and section splitting by reading the markdown directly — zero credits, zero plumbing, full conversation context. Only reach for `classify` when routing documents *before* parsing (e.g. scans you can't read locally, in `--mode multimodal`).

`probe` and `index` are the first shipped steps of the "kembing" arc — probe → plan → pass → mirror. `probe` walks a directory and reports per-file metadata with zero credits and no network call, so you can feel out a pile before parsing it; `index` is its persistent form — the arc's queryable manifest — for corpora too large or too long-lived to re-read every time. The rest of the arc (draft a plan, execute a pass, render into a markdown mirror with hash-stamped frontmatter) is the project's direction — see `docs/goal.txt` — and is still in progress. For now, route each request to the matching facet.

## Setup (shared across all facets)

The document facets (`parse`, `classify`) need `LLAMA_CLOUD_API_KEY` exported in the shell (`probe` and `index` are local-only and need no key):

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
kemb index <directory>            # persistent corpus index, incremental rescans
kemb index <directory> --search "net 30"   # full-text search the index
kemb doctor                       # preflight check
```

Otherwise fall back to the bundled shim from the skill directory, which locates the kemb package on its own — the repo's `src/` when run from a checkout, an installed `kemb` package when the skill directory lives elsewhere (marketplace installs, snapshots):

```bash
python scripts/kemb_cli.py parse <file> --tier cost_effective --auto-install
```

Always pass `--auto-install` from the shim path — it `pip install`s whatever is missing on first run: `llama-cloud`, and `kemb` itself (from GitHub) when the skill directory is outside the repo. If the SDK can't install, every facet falls back to a `requests`-only REST path automatically.

## Routing — which facet for which request

- "Parse / OCR / convert to markdown / read this PDF" → `parse` (`references/parse.md`)
- "Pull these specific fields out as JSON" / "give me structured data" → `parse` first if it's a scan or complex layout, then extract the fields yourself from the markdown (no API call). For text-friendly files, read the file directly.
- "Classify / categorize / route this document by type" → if you can read it (text layer, or parsed markdown), classify it yourself; use `classify` for scans / layout-heavy files you can't read (`references/classify.md`)
- "Split this long document into intro / methodology / results / sections" → `parse` to markdown, then split by headings yourself (no API call)
- "What's in this folder? / inventory a directory / scope a batch before parsing / which of these files can LlamaCloud take?" → `probe` (`references/probe.md`)
- "What ARE these documents? / triage this corpus / which of these are scans / what's worth parsing?" → `probe --sample` (`references/probe.md`) — local first-words sample of every file, readable in one pass
- "Index this corpus / search across these documents / find duplicates / huge corpus (thousands of files) / I'll be coming back to this pile" → `index` (`references/index.md`) — persistent SQLite inventory; incremental rescans take seconds, `--search` is local full-text over the samples
- "What does each facet cost? / how does v2 of the API work?" → `references/rest_api.md`
- Setup failures, weird response shapes, network blocks, encrypted PDFs → `references/troubleshooting.md`

## What this skill does NOT do

- Schema extraction or section splitting via API — former `extract` / `split` facets were removed; once parse yields markdown, the agent does that work itself for zero credits.
- Embedding or vector storage — pair with a separate RAG pipeline.
- End-to-end corpus orchestration (plan / pass / mirror) — `probe` and `index` ship today as the local first steps, but automated planning, batch execution, and the hash-stamped markdown mirror are still in progress; track them in `docs/goal.txt`.
- Store API keys — keys come from the environment, every run.
