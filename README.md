# llamaparse-plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-8A2BE2.svg)](https://claude.ai/code)
[![Cowork compatible](https://img.shields.io/badge/Cowork-compatible-1f6feb.svg)](https://claude.ai)
[![Changelog](https://img.shields.io/badge/changelog-keepachangelog-orange.svg)](./CHANGELOG.md)

> Turn any document into clean markdown, typed JSON, a classification, or
> split sections — from one CLI or four lazy-loaded Claude skills.

`llamaparse-plugin` wraps four LlamaCloud APIs (LlamaParse v2, LlamaExtract v2,
LlamaClassify v2, LlamaSplit v1 beta) behind a single `llamaparse` command
**and** ships them as Claude Code / Cowork skills that load on demand.

| Capability  | What it does                                                    | API                 |
|-------------|-----------------------------------------------------------------|---------------------|
| **parse**   | Document → clean markdown / text (tables, multi-column, scans)  | LlamaParse v2       |
| **extract** | Document + JSON Schema → typed JSON object                      | LlamaExtract v2     |
| **classify**| Document + categories → matched label + confidence              | LlamaClassify v2    |
| **split**   | Document + categories → typed sections with page ranges         | LlamaSplit v1 beta  |

## 30-second quickstart

```bash
# 1. Install
pipx install git+https://github.com/acrosley/llamaparse-plugin

# 2. Set your key (get one at https://cloud.llamaindex.ai/api-key)
export LLAMA_CLOUD_API_KEY="llx-..."

# 3. Parse anything
llamaparse parse ./contract.pdf      # → contract.md
```

That's it. `extract`, `classify`, and `split` follow the same shape — see
[Real examples](#real-examples) below.

> screenshot/asciinema goes here

## What this is for

- **Knowledge workers and analysts** drowning in PDFs, scans, and Office docs
  who want one tool that goes from "file on disk" to "usable text or JSON" —
  no per-format glue code.
- **Teams already using Claude Code or Cowork** who want LlamaCloud's parsing
  quality available as native skills without bloating every prompt with
  feature documentation Claude rarely needs.
- **Anyone tempted to write `requests.post(...)` against LlamaCloud yourself**
  — this handles upload, polling, retries, REST/SDK fallback, error surfacing,
  and output paths so you can focus on the result.

## Two ways to use it

| Mode   | What you run                                                                                                  | What you get                                                                                                                                                            |
|--------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plugin | `/plugin install llamaparse-plugin@llamaparse` in Claude Code (or "Add marketplace from GitHub" in Cowork)    | Four lazy-loaded skills (`llamaparse`, `llamaextract`, `llamaclassify`, `llamasplit`). Only the matching skill's context loads per request.                              |
| CLI    | `pipx install git+https://github.com/acrosley/llamaparse-plugin`                                              | A `llamaparse` command on your PATH with four subcommands.                                                                                                              |

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
pipx install git+https://github.com/acrosley/llamaparse-plugin
```

or, without pipx:

```bash
pip install git+https://github.com/acrosley/llamaparse-plugin
```

You'll get a `llamaparse` command with four subcommands:

```bash
llamaparse --help                              # top-level help
llamaparse parse     --help
llamaparse extract   --help
llamaparse classify  --help
llamaparse split     --help
llamaparse probe     --help                    # scan a directory (zero credits)
llamaparse doctor                              # preflight checks (zero credits)
```

After install, run `llamaparse doctor` to confirm your Python, deps, and
`LLAMA_CLOUD_API_KEY` are all set up — it makes one non-billable auth probe
against LlamaCloud and never starts a job. Add `--offline` to skip the
network check.

`llama-cloud` and `requests` install automatically as dependencies.

### parse — document → markdown / text

```bash
llamaparse parse ./contract.pdf                       # → contract.md
llamaparse parse ./scan.pdf --tier agentic            # agentic tier
llamaparse parse ./report.pdf --output ./out.md       # explicit output path
llamaparse parse ./report.pdf --result-type text      # → report.txt
llamaparse parse ./report.pdf --strip-noise           # drop layout-hint comments
llamaparse parse ./report.pdf --rest                  # force REST path (no SDK)
```

**Backward compat:** `llamaparse ./file.pdf [...]` (no subcommand) still works
and dispatches as `parse`, so existing scripts keep running.

### extract — document + JSON Schema → typed JSON

```bash
llamaparse extract ./invoice.pdf --schema @invoice_schema.json
llamaparse extract ./form.pdf    --configuration-id cfg_abc123    # saved agent
llamaparse extract ./doc.pdf     --schema '{"type":"object","properties":{"name":{"type":"string"}}}'
```

Pass a JSON Schema describing the shape you want back. Save once, reference
with `@path.json`, or inline small ones. Output defaults to
`<input>.extract.json`.

### classify — document + categories → label + confidence

```bash
llamaparse classify ./doc.pdf --rules @rules.json
llamaparse classify ./doc.pdf --rules '[{"type":"invoice","description":"A bill requesting payment"}]'
llamaparse classify ./doc.pdf --mode multimodal       # vision for scans / layout-heavy
```

`--rules` is a JSON list of `{type, description}` objects. The classifier
returns `{type, confidence, reasoning}`. Output defaults to
`<input>.classify.json`.

### split — long document → typed sections with page ranges

```bash
llamaparse split ./report.pdf --categories @cats.json
llamaparse split ./report.pdf --categories '[{"name":"intro","description":"Opening summary"}]'
llamaparse split ./report.pdf --splitting-strategy semantic
```

LlamaSplit is currently a **v1 beta** endpoint — its response shape may
evolve. Output defaults to `<input>.split.json`.

### probe — recursively inventory a directory (zero credits)

```bash
llamaparse probe ./inbox                              # human-readable table
llamaparse probe ./inbox --ext pdf,docx               # filter by extension
llamaparse probe ./inbox --max-depth 2                # cap recursion depth
llamaparse probe ./inbox --supported-only             # only LlamaCloud-friendly files
llamaparse probe ./inbox --json > inventory.json      # machine-readable
```

`probe` walks the target directory recursively and reports per-file size,
mtime, extension, mime type, and whether LlamaCloud is likely to accept the
format. It never makes a network call — use it to preview a batch before
running `parse` / `extract` / `classify` / `split` over a directory. Hidden
files and directories are skipped unless `--include-hidden` is passed.

### --dry-run — preview a job without spending credits

```bash
llamaparse parse    ./contract.pdf --dry-run
llamaparse extract  ./invoice.pdf  --schema @invoice.json --dry-run
llamaparse classify ./doc.pdf      --rules @rules.json   --dry-run
llamaparse split    ./report.pdf   --categories @cats.json --dry-run
```

Adds a `--dry-run` mode to every job subcommand. It validates the inputs
(file exists, schema/rules/categories parse, mutually-exclusive flags
aren't combined), resolves the output path, and prints the configuration
that *would* be sent — without uploading the document or starting a job.
Pair it with `probe` to scope a batch run before any credits are spent.

## Real examples

Concrete recipes for the four subcommands. Schema/rule files referenced below
ship in [`examples/`](./examples/) so you can copy and run them as-is.

### Extract invoice line items

```bash
llamaparse extract ./acme-invoice-2025-04.pdf \
    --schema @examples/schemas/invoice.json \
    --output ./acme-2025-04.json
```

Pulls vendor, invoice number, dates, every line item, and totals into one
typed JSON file you can pipe into a ledger or a spreadsheet.

### Route incoming docs by type

```bash
for f in inbox/*.pdf; do
    llamaparse classify "$f" --rules @examples/rules/document_routing.json
done
```

Each call writes `<file>.classify.json` with the matched label (contract,
invoice, receipt, correspondence, other) plus a confidence score — wire that
into a shell loop and `mv` files into per-type folders.

### Split a research report by section

```bash
llamaparse split ./annual-report.pdf \
    --categories @examples/categories/report_sections.json
```

Get back labeled page ranges for intro, methodology, results, discussion,
references, and appendix — ready to feed into per-section summarizers or
chunkers.

### Parse a multi-column scan to markdown

```bash
llamaparse parse ./scanned-deposition.pdf --tier agentic --strip-noise
```

`agentic` handles the multi-column OCR; `--strip-noise` drops repeating
header/footer artifacts so the resulting markdown is paste-ready.

## Install — Claude Code plugin

```
/plugin marketplace add acrosley/llamaparse-plugin
/plugin install llamaparse-plugin@llamaparse
```

Updates / removal:

```
/plugin marketplace update llamaparse
/plugin uninstall llamaparse-plugin@llamaparse
/plugin marketplace remove llamaparse
```

Four lazy-loaded skills become available after install. Each has its own
trigger conditions; Claude pulls in only the matching skill's context per
request:

| Skill           | Triggers on requests like                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| `llamaparse`    | "Parse this PDF with LlamaParse." / "OCR this scan." / "Convert this Excel to markdown."                                 |
| `llamaextract`  | "Extract invoice number and total from this PDF." / "Pull fields out as JSON using this schema."                         |
| `llamaclassify` | "Classify this document — is it a contract, invoice, or receipt?" / "Route incoming docs by type."                       |
| `llamasplit`    | "Split this long report into intro / methodology / results / appendix sections."                                         |

Invoke any of them explicitly via the slash menu: `/llamaparse-plugin:<skill>`.

The first time a skill runs in a fresh sandbox it `pip install`s `llama-cloud`
automatically (the bundled scripts pass `--auto-install`), so you don't need
to set anything up beyond the API key.

## Install — Claude Cowork plugin

Cowork manages plugins through the **Customize** menu (there's no `/plugin`
slash command in Cowork).

1. Open Claude Desktop → **Cowork** tab.
2. Click **Customize** in the left sidebar.
3. Click **+** → **Add marketplace from GitHub**.
4. Enter `acrosley/llamaparse-plugin`.
5. Find `llamaparse-plugin` in the marketplace and click **Install**.
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
2. Point it at the cloned `llamaparse-plugin` directory
3. Install as above

## Cost

All four capabilities bill per page processed. Parse exposes a tier knob;
extract / classify / split each have a single per-page rate.

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
llamaparse-plugin/
├── .claude-plugin/
│   ├── marketplace.json            — marketplace manifest
│   └── plugin.json                 — plugin manifest
├── pyproject.toml                  — packaging for the `llamaparse` CLI
├── src/llamaparse_cli/
│   ├── __init__.py                 — public exports
│   ├── _core.py                    — subcommand dispatcher (parse / extract / classify / split)
│   ├── _common.py                  — shared helpers (auth, SDK loader, REST poller, file upload)
│   ├── _parse.py                   — LlamaParse v2
│   ├── _extract.py                 — LlamaExtract v2
│   ├── _classify.py                — LlamaClassify v2
│   ├── _split.py                   — LlamaSplit v1 beta
│   ├── _probe.py                   — recursive directory metadata scan (local-only)
│   └── _doctor.py                  — preflight checks (local-only)
├── skills/
│   ├── llamaparse/                 — parse → markdown/text
│   │   ├── SKILL.md
│   │   ├── scripts/parse_document.py
│   │   └── references/{rest_api,troubleshooting}.md
│   ├── llamaextract/               — schema-driven structured extraction
│   ├── llamaclassify/              — categorization with confidence
│   └── llamasplit/                 — section splitting (v1 beta)
├── examples/                       — copy-pasteable schemas, rules, categories
├── tests/                          — pytest suite
├── CHANGELOG.md                    — version history
├── CONTRIBUTING.md                 — dev setup and PR guide
└── README.md
```

Each skill is independent and lazy-loaded: Claude pulls in only the SKILL.md
whose description matches the user's request, so feature context stays out of
the window until needed. All four shell into the same `llamaparse_cli`
package, so CLI and skills never drift.

## Contributing

Bug reports, feature requests, and PRs welcome. See
[CONTRIBUTING.md](./CONTRIBUTING.md) for dev setup, the test workflow, and
the pattern to follow when adding a new capability.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for the release history (Keep a Changelog
format).

## License

MIT — see [LICENSE](./LICENSE).
