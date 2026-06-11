# Kemb

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-8A2BE2.svg)](https://claude.ai/code)
[![Cowork compatible](https://img.shields.io/badge/Cowork-compatible-1f6feb.svg)](https://claude.ai)
[![Changelog](https://img.shields.io/badge/changelog-keepachangelog-orange.svg)](./CHANGELOG.md)

> Comb document corpora into agent-ready form. One CLI, one Claude skill,
> two LlamaCloud-backed facets — parse and classify — plus local, zero-credit
> `probe` and `index` for triaging a directory before you spend a thing.

**Kembing** is the discipline of preparing document corpora for agents: survey
the pile, plan the pass, then comb each document into a structured markdown
mirror that an LLM can actually use. Today `kemb` ships the two single-file
document facets that make up a pass, plus a local `probe` that surveys and
triages a directory before you process it — the first shipped step of that
arc. The rest of the orchestration (plan → execute → mirror with hash-stamped
provenance) is in active development — see [`docs/goal.txt`](./docs/goal.txt).

| Facet       | What it does                                                    | API                 |
|-------------|-----------------------------------------------------------------|---------------------|
| **parse**   | Document → clean markdown / text (tables, multi-column, scans)  | LlamaParse v2       |
| **classify**| Document + categories → matched label + confidence              | LlamaClassify v2    |
| **probe**   | Directory → per-file inventory + text samples for triage         | local, zero credits |
| **index**   | Corpus → persistent SQLite inventory; incremental rescans, dedup, full-text search | local, zero credits |

**Why only two API facets?** Because the third party in the room is an LLM.
Once `parse` has produced clean markdown, the consuming agent extracts fields
to a schema, classifies, and splits sections itself — zero LlamaCloud credits,
zero extra plumbing, full conversation context. The former `extract` and
`split` facets were removed for exactly that reason; `classify` stays for
routing documents *before* parsing (scans and layout-heavy files an agent
can't read locally).

`probe`, `index`, and `doctor` are local, zero-credit tools — `probe` scopes a
directory, `index` keeps a persistent inventory of it, and `doctor` runs a
preflight check — none of them uploads a document or starts a job.

## 30-second quickstart

```bash
# 1. Install
pipx install git+https://github.com/acrosley/kemb

# 2. Set your key (get one at https://cloud.llamaindex.ai/api-key)
export LLAMA_CLOUD_API_KEY="llx-..."

# 3. Parse anything
kemb parse ./contract.pdf      # → contract.md
```

That's it. `classify` follows the same shape — see
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
| CLI    | `pipx install git+https://github.com/acrosley/kemb`                                                           | A `kemb` command on your PATH with `parse`, `classify`, `probe`, and `index` subcommands and a preflight `doctor`.                                                      |

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
kemb classify  --help
kemb probe     --help                          # scan a directory (zero credits)
kemb index     --help                          # persistent corpus index (zero credits)
kemb doctor                                    # preflight checks (zero credits)
```

After install, run `kemb doctor` to confirm your Python, deps, and
`LLAMA_CLOUD_API_KEY` are all set up — it makes one non-billable auth probe
against LlamaCloud and never starts a job. Add `--offline` to skip the
network check.

`llama-cloud`, `requests`, and `pypdf` install automatically as dependencies.

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

### classify — document + categories → label + confidence

```bash
kemb classify ./doc.pdf --rules @rules.json
kemb classify ./doc.pdf --rules '[{"type":"invoice","description":"A bill requesting payment"}]'
kemb classify ./doc.pdf --mode multimodal       # vision for scans / layout-heavy
```

`--rules` is a JSON list of `{type, description}` objects. The classifier
returns `{type, confidence, reasoning}`. Output defaults to
`<input>.classify.json`.

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
running `parse` / `classify` over a directory. Hidden
files and directories are skipped unless `--include-hidden` is passed.

#### probe --sample — corpus triage in one text file (zero credits)

```bash
kemb probe ./cases --sample                            # XML-tagged corpus sample
kemb probe ./cases --sample --output corpus_sample.txt # write it to a file
kemb probe ./cases --sample --sample-words 200         # more words per doc
kemb probe ./cases --sample --sample-budget 20000      # tighter corpus-wide cap
kemb probe ./cases --sample --json                     # samples embedded in the JSON
```

`--sample` extracts the first words of every document **locally** — PDFs via
`pypdf`, Office/OpenDocument files via their XML, text/HTML directly — and
renders one text file of XML-tagged blocks (the structure LLMs parse most
reliably): a `<document>` tag per file carrying labeled metadata attributes
(`path`, `size`, `pages`, `modified`, `type`, `text` status), with up to
`--sample-words` words of content as the body. An agent can read that single
file and weigh an entire multi-directory case corpus — what each document is,
which are scans (PDFs with no text layer collapse to a self-closing tag with
a `note` flagging them for OCR-capable parse tiers), what to parse now versus
defer — without uploading anything or running a per-file model pass.

```xml
<corpus_sample generated="2026-06-10T01:52:23Z" files="4" total_size="4.3 KB"
               sampled_words="69" status="no-text: 1, ok: 3">
<document path="smith/complaint.pdf" size="2.2 KB" pages="4" modified="..." type=".pdf" text="ok">
IN THE DISTRICT COURT Plaintiff John Smith alleges breach of contract and fraud ...
</document>
<document path="smith/exhibit-a.pdf" size="1.7 KB" pages="12" modified="..." type=".pdf"
          text="no-text" note="no text layer — likely a scan; needs an OCR-capable parse tier"/>
...
</corpus_sample>
```

`--sample-budget` caps total sampled words corpus-wide so the output stays
readable in one context window; files past the budget keep their inventory
line but skip the text. PDFs also gain page counts — the input you need to
estimate parse cost (pages × tier) before committing to a batch.

### index — persistent corpus inventory, incremental rescans (zero credits)

```bash
kemb index ./corpus                          # create or refresh the index
kemb index ./corpus --stats                  # report on it, no rescan
kemb index ./corpus --search "force majeure" # full-text search the samples
kemb index ./corpus --full                   # force re-read of every file
```

`probe` is stateless — it re-reads everything on every run, which stops
scaling somewhere in the thousands of files. `index` is the persistent
version: one SQLite database per corpus (`<corpus>/.kemb/index.db`) holding
each file's metadata, a sha256 content hash, and the same locally extracted
text sample. Rescans are **incremental**: only files whose size or mtime
changed get re-read, so the first scan pays full price and every scan after
takes seconds — 100k-file corpora stay workable.

On top of the inventory you get duplicate detection (same hash, different
paths — parse one, reuse for its twins), FTS5 full-text search over the
samples and paths (`--search "liability AND audit"`), and a `--stats` report
with by-extension and scan-vs-text breakdowns. Deleted files are marked
missing rather than dropped, so a file that reappears keeps its history. The
schema also reserves a `passes` table for the upcoming batch facet to record
per-file job status — what will make huge batch runs resumable.

Queries **sync on read**: `--stats` and `--search` run the same incremental
refresh before answering, so nobody has to remember to rescan — new files
appear in results, deleted files drop out, and the cost is a walk + stat
pass. Pass `--stale` for a zero-I/O answer from the cached view.

### --dry-run — preview a job without spending credits

```bash
kemb parse    ./contract.pdf --dry-run
kemb classify ./doc.pdf      --rules @rules.json   --dry-run
```

Adds a `--dry-run` mode to every job subcommand. It validates the inputs
(file exists, rules parse, mutually-exclusive flags
aren't combined), resolves the output path, and prints the configuration
that *would* be sent — without uploading the document or starting a job.
Pair it with `probe` to scope a batch run before any credits are spent.

## Real examples

Concrete recipes. Rule files referenced below ship in
[`examples/`](./examples/) so you can copy and run them as-is.

### Route incoming docs by type

```bash
for f in inbox/*.pdf; do
    kemb classify "$f" --rules @examples/rules/document_routing.json
done
```

Each call writes `<file>.classify.json` with the matched label (contract,
invoice, receipt, correspondence, other) plus a confidence score — wire that
into a shell loop and `mv` files into per-type folders.

### Parse a multi-column scan to markdown

```bash
kemb parse ./scanned-deposition.pdf --tier agentic --strip-noise
```

`agentic` handles the multi-column OCR; `--strip-noise` drops repeating
header/footer artifacts so the resulting markdown is paste-ready.

### Triage a multi-directory case corpus before spending credits

```bash
kemb probe ./case-files --sample --output corpus_sample.txt
```

One zero-credit command produces an XML-tagged sample of the whole tree —
first words, page counts, and scan flags for every document.
Hand `corpus_sample.txt` to Claude (or read it yourself) to decide doc types,
parse tiers, and priorities, then run `parse` over only the files that earn
it — and extract or split from the resulting markdown yourself.

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
| "Classify this document — is it a contract, invoice, or receipt?" / "Route incoming docs by type."                       | `references/classify.md` |
| "What's in this folder? / triage this corpus / scope a batch before parsing."                                            | `references/probe.md`    |

Requests to extract fields or split sections route through `parse` first;
Claude then does the structured work from the markdown directly — no extra
API call, no extra credits.

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

The two document facets bill per page processed. Parse exposes a tier knob;
classify has a single per-page rate. `probe` and `doctor` are local and
free — they never spend a credit. Post-parse extraction and splitting happen
in your agent, so they add no LlamaCloud cost at all.

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
│   ├── _core.py                    — subcommand dispatcher (parse / classify / probe / doctor)
│   ├── _common.py                  — shared helpers (auth, SDK loader, REST poller, file upload)
│   ├── _parse.py                   — LlamaParse v2
│   ├── _classify.py                — LlamaClassify v2
│   ├── _probe.py                   — local directory scan + corpus text sampling
│   ├── _sample.py                  — per-format local text extractors (pypdf, zip/XML)
│   └── _doctor.py                  — zero-credit preflight
├── skills/kemb/                    — single orchestrating skill
│   ├── SKILL.md                    — routes requests to facets
│   ├── scripts/kemb_cli.py         — shim into src/kemb/
│   └── references/
│       ├── parse.md                — parse facet (LlamaParse v2)
│       ├── classify.md             — classify facet (LlamaClassify v2)
│       ├── probe.md                — probe facet (local scan + triage sample)
│       ├── rest_api.md             — LlamaCloud v2 REST reference
│       └── troubleshooting.md      — common failure modes
├── examples/                       — copy-pasteable classifier rules
├── docs/
│   └── goal.txt                    — corpus-curation north star
├── tests/                          — pytest suite
├── CHANGELOG.md                    — version history
├── CONTRIBUTING.md                 — dev setup and PR guide
└── README.md
```

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
