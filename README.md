# Kemb

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-8A2BE2.svg)](https://claude.ai/code)
[![Cowork compatible](https://img.shields.io/badge/Cowork-compatible-1f6feb.svg)](https://claude.ai)
[![Changelog](https://img.shields.io/badge/changelog-keepachangelog-orange.svg)](./CHANGELOG.md)

> Comb document corpora into agent-ready form. One CLI, one Claude skill,
> four LlamaCloud-backed facets — parse, extract, classify, split — plus a
> local, zero-credit `probe` for scoping a directory before you spend a thing.

**Kembing** is the discipline of preparing document corpora for agents: survey
the pile, plan the pass, then comb each document into a structured markdown
mirror that an LLM can actually use. Today `kemb` ships the four single-file
document facets that make up a pass, plus a local `probe` that surveys a
directory before you process it — the first shipped step of that arc. The rest
of the orchestration (plan → execute → mirror with hash-stamped provenance) is
in active development — see [`docs/goal.txt`](./docs/goal.txt).

| Facet       | What it does                                                    | API                 |
|-------------|-----------------------------------------------------------------|---------------------|
| **parse**   | Document → clean markdown / text (tables, multi-column, scans)  | LlamaParse v2       |
| **extract** | Document + JSON Schema → typed JSON object                      | LlamaExtract v2     |
| **classify**| Document + categories → matched label + confidence              | LlamaClassify v2    |
| **split**   | Document + categories → typed sections with page ranges         | LlamaSplit v1 beta  |
| **probe**   | Directory → per-file inventory (size, type, LlamaCloud support)  | local, zero credits |

`probe` and `doctor` are local, zero-credit tools — `probe` scopes a directory
and `doctor` runs a preflight check — neither uploads a document or starts a job.

## 30-second quickstart

```bash
# 1. Install
pipx install git+https://github.com/acrosley/kemb

# 2. Set your key (get one at https://cloud.llamaindex.ai/api-key)
export LLAMA_CLOUD_API_KEY="llx-..."

# 3. Parse anything
kemb parse ./contract.pdf      # → contract.md
```

That's it. `extract`, `classify`, and `split` follow the same shape — see
[Real examples](#real-examples) below.

## What this is for

- **Knowledge workers and analysts** drowning in PDFs, scans, and Office docs
  who want one tool that goes from "file on disk" to "usable text or JSON" —
  no per-format glue code.
- **Teams already using Claude Code or Cowork** who want LlamaCloud's parsing
  quality available as one native skill, with corpus-level orchestration on
  the roadmap.
- **Legal, research, and analyst teams** prepping large document collections
  for agent retrieval — the next phase of kemb (probe → plan → pass → mirror)
  targets exactly this workflow.
- **Anyone tempted to write `requests.post(...)` against LlamaCloud yourself**
  — kemb handles upload, polling, retries, REST/SDK fallback, error surfacing,
  and output paths so you can focus on the result.

## Two ways to use it

| Mode   | What you run                                                                                                  | What you get                                                                                                                                                            |
|--------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plugin | `/plugin install kemb@kemb` in Claude Code (or "Add marketplace from GitHub" in Cowork)                       | One orchestrating skill that routes by facet, with per-facet reference docs that load on demand.                                                                        |
| CLI    | `pipx install git+https://github.com/acrosley/kemb`                                                           | A `kemb` command on your PATH with four facet subcommands and a preflight `doctor`.                                                                                     |

You only need a LlamaCloud API key — grab one at
<https://cloud.llamaindex.ai/api-key>.

## Prerequisites (one-time)

Export your API key as a persistent environment variable.

**macOS / Linux** (bash/zsh):

```bash
echo 'export LLAMA_CLOUD_API_KEY="llx-..."' >> ~/.zshrc   # or ~/.bashrc
source ~/.zshrc
```

**Windows** (PowerShell):

```powershell
setx LLAMA_CLOUD_API_KEY "llx-..."
```

Restart your terminal (and Claude Code / Cowork) so the new env var
propagates.

## Install — CLI

```bash
pipx install git+https://github.com/acrosley/kemb
```

or, without pipx:

```bash
pip install git+https://github.com/acrosley/kemb
```

You'll get a `kemb` command:

```bash
kemb --help                                    # top-level help
kemb parse     --help
kemb extract   --help
kemb classify  --help
kemb split     --help
kemb probe     --help                          # scan a directory (zero credits)
kemb doctor                                    # preflight checks (zero credits)
```

After install, run `kemb doctor` to confirm your Python, deps, and
`LLAMA_CLOUD_API_KEY` are all set up — it makes one non-billable auth probe
against LlamaCloud and never starts a job. Add `--offline` to skip the
network check.

`llama-cloud` and `requests` install automatically as dependencies.

### parse — document → markdown / text

```bash
kemb parse ./contract.pdf                       # → contract.md
kemb parse ./scan.pdf --tier agentic            # agentic tier
kemb parse ./report.pdf --output ./out.md       # explicit output path
kemb parse ./report.pdf --result-type text      # → report.txt
kemb parse ./report.pdf --strip-noise           # drop layout-hint comments
kemb parse ./report.pdf --rest                  # force REST path (no SDK)
```

**Shortcut:** `kemb ./file.pdf [...]` (no subcommand) dispatches as `parse`.

### extract — document + JSON Schema → typed JSON

```bash
kemb extract ./invoice.pdf --schema @invoice_schema.json
kemb extract ./form.pdf    --configuration-id cfg_abc123    # saved agent
kemb extract ./doc.pdf     --schema '{"type":"object","properties":{"name":{"type":"string"}}}'
```

Pass a JSON Schema describing the shape you want back. Save once, reference
with `@path.json`, or inline small ones. Output defaults to
`<input>.extract.json`.

### classify — document + categories → label + confidence

```bash
kemb classify ./doc.pdf --rules @rules.json
kemb classify ./doc.pdf --rules '[{"type":"invoice","description":"A bill requesting payment"}]'
kemb classify ./doc.pdf --mode multimodal       # vision for scans / layout-heavy
```

`--rules` is a JSON list of `{type, description}` objects. The classifier
returns `{type, confidence, reasoning}`. Output defaults to
`<input>.classify.json`.

### split — long document → typed sections with page ranges

```bash
kemb split ./report.pdf --categories @cats.json
kemb split ./report.pdf --categories '[{"name":"intro","description":"Opening summary"}]'
kemb split ./report.pdf --splitting-strategy semantic
```

LlamaSplit is currently a **v1 beta** endpoint — its response shape may
evolve. Output defaults to `<input>.split.json`.

### probe — recursively inventory a directory (zero credits)

```bash
kemb probe ./inbox                              # human-readable table
kemb probe ./inbox --ext pdf,docx               # filter by extension
kemb probe ./inbox --max-depth 2                # cap recursion depth
kemb probe ./inbox --supported-only             # only LlamaCloud-friendly files
kemb probe ./inbox --json > inventory.json      # machine-readable
```

`probe` walks the target directory recursively and reports per-file size,
mtime, extension, mime type, and whether LlamaCloud is likely to accept the
format. It never makes a network call — use it to preview a batch before
running `parse` / `extract` / `classify` / `split` over a directory. Hidden
files and directories are skipped unless `--include-hidden` is passed.

### --dry-run — preview a job without spending credits

```bash
kemb parse    ./contract.pdf --dry-run
kemb extract  ./invoice.pdf  --schema @invoice.json --dry-run
kemb classify ./doc.pdf      --rules @rules.json   --dry-run
kemb split    ./report.pdf   --categories @cats.json --dry-run
```

Adds a `--dry-run` mode to every job subcommand. It validates the inputs
(file exists, schema/rules/categories parse, mutually-exclusive flags
aren't combined), resolves the output path, and prints the configuration
that *would* be sent — without uploading the document or starting a job.
Pair it with `probe` to scope a batch run before any credits are spent.

## Real examples

Concrete recipes for the four facets. Schema/rule files referenced below
ship in [`examples/`](./examples/) so you can copy and run them as-is.

### Extract invoice line items

```bash
kemb extract ./acme-invoice-2025-04.pdf \
    --schema @examples/schemas/invoice.json \
    --output ./acme-2025-04.json
```

Pulls vendor, invoice number, dates, every line item, and totals into one
typed JSON file you can pipe into a ledger or a spreadsheet.

### Route incoming docs by type

```bash
for f in inbox/*.pdf; do
    kemb classify "$f" --rules @examples/rules/document_routing.json
done
```

Each call writes `<file>.classify.json` with the matched label (contract,
invoice, receipt, correspondence, other) plus a confidence score — wire that
into a shell loop and `mv` files into per-type folders.

### Split a research report by section

```bash
kemb split ./annual-report.pdf \
    --categories @examples/categories/report_sections.json
```

Get back labeled page ranges for intro, methodology, results, discussion,
references, and appendix — ready to feed into per-section summarizers or
chunkers.

### Parse a multi-column scan to markdown

```bash
kemb parse ./scanned-deposition.pdf --tier agentic --strip-noise
```

`agentic` handles the multi-column OCR; `--strip-noise` drops repeating
header/footer artifacts so the resulting markdown is paste-ready.

### Scope a directory, then run the batch

```bash
# 1. See what's in the folder and which files LlamaCloud will accept (free)
kemb probe ./inbox --supported-only

# 2. Confirm the config one file would send — no upload, no credits
kemb parse ./inbox/sample.pdf --tier agentic --dry-run

# 3. Run the batch once the inventory and config look right
for f in inbox/*.pdf; do kemb parse "$f" --tier agentic; done
```

`probe` and `--dry-run` together let you understand cost and scope before a
single credit is spent — survey the pile, preview the job, then commit.

## Install — Claude Code plugin

```
/plugin marketplace add acrosley/kemb
/plugin install kemb@kemb
```

Updates / removal:

```
/plugin marketplace update kemb
/plugin uninstall kemb@kemb
/plugin marketplace remove kemb
```

One orchestrating skill (`kemb`) loads on demand. Its routing table sends
each request to a facet under `references/`:

| Request                                                                                                                  | Facet doc                |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------|
| "Parse this PDF with LlamaParse." / "OCR this scan." / "Convert this Excel to markdown."                                 | `references/parse.md`    |
| "Extract invoice number and total from this PDF." / "Pull fields out as JSON using this schema."                         | `references/extract.md`  |
| "Classify this document — is it a contract, invoice, or receipt?" / "Route incoming docs by type."                       | `references/classify.md` |
| "Split this long report into intro / methodology / results / appendix sections."                                         | `references/split.md`    |
| "What's in this folder? / inventory a directory / scope a batch before parsing."                                         | `references/probe.md`    |

Invoke the skill explicitly via the slash menu: `/kemb:kemb`.

The first time the skill runs in a fresh sandbox it `pip install`s `llama-cloud`
automatically (the bundled shim passes `--auto-install`), so you don't need
to set anything up beyond the API key.

## Install — Claude Cowork plugin

Cowork manages plugins through the **Customize** menu (there's no `/plugin`
slash command in Cowork).

1. Open Claude Desktop → **Cowork** tab.
2. Click **Customize** in the left sidebar.
3. Click **+** → **Add marketplace from GitHub**.
4. Enter `acrosley/kemb`.
5. Find `kemb` in the marketplace and click **Install**.
6. Fully quit Cowork from the system tray and relaunch.

### Network allowlist (Cowork only)

The Cowork sandbox uses an HTTPS allowlist. If you see `403 Forbidden` /
`Host not in allowlist` from the proxy when calling
`api.cloud.llamaindex.ai`, add the host under **Settings → Capabilities →
network allowlist** (Team/Enterprise plans require an org owner to do this
in Admin settings), then fully restart Cowork. Claude Code has no such
restriction.

### Local-folder install (plugin development)

If you've cloned the repo and want to test changes without pushing:

1. **Customize** → **+** → **Add marketplace from local folder**
2. Point it at the cloned `kemb` directory
3. Install as above

## Cost

The four document facets bill per page processed. Parse exposes a tier knob;
extract / classify / split each have a single per-page rate. `probe` and
`doctor` are local and free — they never spend a credit.

**Parse tiers:**

| Tier             | Approx multiplier | Best for                                       |
|------------------|-------------------|------------------------------------------------|
| `fast`           | ~1 cr/page        | Plain text, simple layouts                     |
| `cost_effective` | ~3 cr/page        | Default; balanced quality                      |
| `agentic`        | ~15 cr/page       | Tables, multi-column, mixed media              |
| `agentic_plus`   | ~30+ cr/page      | Dense tables, charts, the hardest documents    |

`fast` returns plain text only; the other three tiers also expose a
structured markdown expansion. The CLI handles this transparently — pass
`--tier fast` and you'll get text saved to your chosen output path (with a
one-line note if you asked for markdown). Verify current pricing at
<https://cloud.llamaindex.ai> before committing to large batches.

**Classify** offers two `--mode` settings: `fast` (text-only, cheap) and
`multimodal` (reads images and layout — better for scans).

## What's inside

```
kemb/
├── .claude-plugin/
│   ├── marketplace.json            — marketplace manifest
│   └── plugin.json                 — plugin manifest
├── pyproject.toml                  — packaging for the `kemb` CLI
├── src/kemb/
│   ├── __init__.py                 — public exports
│   ├── _core.py                    — subcommand dispatcher (parse / extract / classify / split / probe / doctor)
│   ├── _common.py                  — shared helpers (auth, SDK loader, REST poller, file upload)
│   ├── _parse.py                   — LlamaParse v2
│   ├── _extract.py                 — LlamaExtract v2
│   ├── _classify.py                — LlamaClassify v2
│   ├── _split.py                   — LlamaSplit v1 beta
│   ├── _probe.py                   — recursive directory metadata scan (local-only)
│   └── _doctor.py                  — zero-credit preflight
├── skills/kemb/                    — single orchestrating skill
│   ├── SKILL.md                    — routes requests to facets
│   ├── scripts/kemb_cli.py         — shim into src/kemb/
│   └── references/
│       ├── parse.md                — parse facet (LlamaParse v2)
│       ├── extract.md              — extract facet (LlamaExtract v2)
│       ├── classify.md             — classify facet (LlamaClassify v2)
│       ├── split.md                — split facet (LlamaSplit v1 beta)
│       ├── probe.md                — probe facet (local directory scan)
│       ├── rest_api.md             — LlamaCloud v2 REST reference
│       └── troubleshooting.md      — common failure modes
├── examples/                       — copy-pasteable schemas, rules, categories
├── docs/
│   ├── goal.txt                    — corpus-curation north star
│   └── llamacloud/                 — local mirror of the entire LlamaCloud
│                                     docs site (~900 pages) + sha256 manifest
├── scripts/
│   ├── fetch_docs.py               — refresh the mirror from upstream
│   ├── check_docs_staleness.py     — compare local hashes against upstream
│   └── docs_common.py              — shared helpers
├── tests/                          — pytest suite
├── CHANGELOG.md                    — version history
├── CONTRIBUTING.md                 — dev setup and PR guide
└── README.md
```

The docs mirror has its own [README](./docs/llamacloud/README.md) covering
scope, layout, and the weekly staleness CI job that watches for upstream drift.

The plugin skill and the standalone CLI both shell into the same `kemb`
package, so the two invocation paths never drift.

## Contributing

Bug reports, feature requests, and PRs welcome. See
[CONTRIBUTING.md](./CONTRIBUTING.md) for dev setup, the test workflow, and
the pattern to follow when adding a new facet.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for the release history (Keep a Changelog
format).

## License

MIT — see [LICENSE](./LICENSE).
