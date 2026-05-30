# Examples

Copy-pasteable schema / rule / category files for the `kemb` CLI.
All four examples below are referenced from the top-level
[README](../README.md#real-examples). Each file is a starting point — adapt
the field names, descriptions, and structures to your own documents.

The CLI accepts JSON arguments inline (`--schema '{"type":"object",…}'`) or
loaded from disk via the `@` prefix (`--schema @examples/schemas/invoice.json`).
The examples here use the `@` form because it's the only one that scales past
a handful of fields.

## `schemas/invoice.json`

A realistic invoice JSON Schema with vendor, billing, line items, totals, and
payment terms. Feed it to `kemb extract` to pull a typed JSON object
out of any invoice PDF:

```bash
kemb extract ./acme-invoice-2025-04.pdf \
    --schema @examples/schemas/invoice.json \
    --output ./acme-2025-04.json
```

Edit the field descriptions to match your vendors' invoice vocabulary — the
extractor uses them as natural-language hints.

## `rules/document_routing.json`

Five-way classifier rules (contract / invoice / receipt / correspondence /
other) suitable for routing a mixed inbox. Pass it to `kemb classify`:

```bash
for f in inbox/*.pdf; do
    kemb classify "$f" --rules @examples/rules/document_routing.json
done
```

Each call writes `<file>.classify.json` with the matched type, a confidence
score, and the classifier's reasoning — pipe that into a shell loop and `mv`
files into per-type folders.

## `categories/report_sections.json`

Six section categories for splitting a long research report (intro,
methodology, results, discussion, references, appendix). Pass it to
`kemb split`:

```bash
kemb split ./annual-report.pdf \
    --categories @examples/categories/report_sections.json
```

You'll get back labeled page ranges per section — feed each range into a
per-section summarizer, chunker, or vector indexer.

## Adapting for your own use

Categories and rules are just JSON arrays of `{name|type, description}`
objects. The descriptions do the heavy lifting — describe each category in
the vocabulary a human would use, including the kinds of phrases and
structural cues that identify it, and the classifier / splitter performs
noticeably better.
