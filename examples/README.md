# Examples

Copy-pasteable rule files for the `kemb` CLI. Referenced from the top-level
[README](../README.md#real-examples). Each file is a starting point — adapt
the types, descriptions, and structures to your own documents.

The CLI accepts JSON arguments inline (`--rules '[{"type":…}]'`) or loaded
from disk via the `@` prefix (`--rules @examples/rules/document_routing.json`).
The `@` form is the only one that scales past a handful of entries.

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

## Adapting for your own use

Rules are just JSON arrays of `{type, description}` objects. The descriptions
do the heavy lifting — describe each category in the vocabulary a human would
use, including the kinds of phrases and structural cues that identify it, and
the classifier performs noticeably better.

## Where did the schema / category examples go?

`schemas/invoice.json` and `categories/report_sections.json` shipped when
`extract` and `split` were API facets. Those facets are gone: once `kemb
parse` produces clean markdown, the consuming agent extracts fields and
splits sections itself — zero credits, zero extra plumbing. The old files
remain in git history if you need them.
