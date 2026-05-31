# Stemma facet — provenance-stamped mirror + verbatim citation

`stemma` is the provenance kernel of "kembing": it combs a document into a markdown **mirror** an agent can read, stamping every block with a **stemma record** — `{source, page, sha256, char span, bbox?}` — so any verbatim quote in an agent's answer can be traced back to the exact source page (and bounding box, when the parser returned layout items). Its companion `cite` resolves a quote against that manifest.

This is the first shipped piece of the "mirror with hash-stamped frontmatter" step in the probe → plan → pass → mirror arc. It works on **one document** today.

## When to use

- "Parse this so I can cite it" / "I need page-level provenance" / "where did this sentence come from?"
- Legal, research, and analyst workflows where an agent's claim must link back to a source page verbatim.
- Building a grounded RAG corpus where retrieved chunks must carry stable, hash-stamped lineage.

For a plain markdown conversion with no provenance, route to `parse` instead.

## Two paths, one core

```bash
# Live: parse the document, then comb it (spends parse credits, needs API key)
kemb stemma ./agreement.pdf --tier agentic

# Offline: comb a parse result you already have (zero credits, no network)
kemb stemma --from-parse-json ./agreement.parse.json --source ./agreement.pdf
```

Both write into `./mirror/` (override with `--out-dir`):

- `mirror/<doc>.md` — the agent-readable mirror. Each block is preceded by an HTML-comment anchor carrying its stemma record, so the body still reads as clean markdown.
- `mirror/<doc>.stemma.json` — the manifest: one record per strand (block), each with `id`, `page`, `sha256`, `char_start`, `char_end`, `text`, and `bbox` when available.

The build is deterministic — the same parse result always yields the same mirror and manifest, which is what makes the hashes trustworthy as provenance.

## Citing a quote

```bash
kemb cite "held in strict confidence" --manifest mirror/agreement.stemma.json
# → agreement.pdf p.2  [p2-b1]  chars 95-112  bbox x=72 y=130 w=468 h=48

kemb cite "held in strict confidence" --manifest mirror/agreement.stemma.json --json
```

`cite` is whitespace-insensitive (line wrapping in the mirror won't break a citation) and reports the **precise character span within the source page**, not just the block. It exits non-zero when the quote isn't found — useful for catching an agent that paraphrased instead of quoting.

## Notes & limits

- **bbox is best-effort.** It is populated only when the parse tier returns layout items with bounding boxes; otherwise strands carry no bbox and citation falls back to page + character span. Higher tiers (`agentic`, `agentic_plus`) are more likely to supply layout.
- **Block granularity.** Strands are blank-line-separated blocks. Sub-block quotes still resolve to a precise character span; the bbox is the block's.
- **Single-document today.** Corpus-wide mirroring across a directory (the `pass` step) is still in progress — `stemma` is the per-document foundation it will build on.
