# llamaparse-plugin

A Claude plugin **and** a tiny standalone CLI for four LlamaCloud document
operations: **parse**, **extract**, **classify**, and **split**. Built on
[LlamaIndex's hosted APIs](https://cloud.llamaindex.ai) — LlamaParse v2,
LlamaExtract v2, LlamaClassify v2, and LlamaSplit v1 beta.

| Capability | What it does | API |
|---|---|---|
| **parse** | Document → clean markdown / text (tables, multi-column, scans) | LlamaParse v2 |
| **extract** | Document + JSON Schema → typed JSON object | LlamaExtract v2 |
| **classify** | Document + categories → matched label + confidence | LlamaClassify v2 |
| **split** | Document + categories → typed sections with page ranges | LlamaSplit v1 beta |

Two ways to use them:

| Mode | What you run | What it gives you |
|---|---|---|
| Plugin | `/plugin install llamaparse-plugin@llamaparse` in Claude Code (or "Add marketplace from GitHub" in Cowork) | Four lazy-loaded skills (`llamaparse`, `llamaextract`, `llamaclassify`, `llamasplit`). Only the relevant skill's context loads for any given request. |
| CLI | `pipx install git+https://github.com/acrosley/llamaparse-plugin` | A `llamaparse` command on your PATH with four subcommands |

You only need a LlamaCloud API key. Get one at
<https://cloud.llamaindex.ai/api-key>.

## Prerequisites (one-time, applies to both modes)

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

or, if you don't have pipx:

```bash
pip install git+https://github.com/acrosley/llamaparse-plugin
```

That gives you a `llamaparse` command with four subcommands:

```bash
llamaparse --help                              # top-level help (lists subcommands)
llamaparse parse     --help
llamaparse extract   --help
llamaparse classify  --help
llamaparse split     --help
```

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
and is dispatched as `parse` so existing scripts and workflows don't break.

### extract — document + JSON Schema → typed JSON

```bash
llamaparse extract ./invoice.pdf --schema @invoice_schema.json
llamaparse extract ./form.pdf    --configuration-id cfg_abc123    # saved agent
llamaparse extract ./doc.pdf     --schema '{"type":"object","properties":{"name":{"type":"string"}}}'
```

The schema is a JSON Schema describing the shape you want back. Save once,
pass with `@path.json`, or inline small ones. Output defaults to
`<input>.extract.json`.

### classify — document + categories → label + confidence

```bash
llamaparse classify ./doc.pdf --rules @rules.json
llamaparse classify ./doc.pdf --rules '[{"type":"invoice","description":"A bill requesting payment"}]'
llamaparse classify ./doc.pdf --mode multimodal       # use vision for scans/layout-heavy
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

The CLI installs `llama-cloud` and `requests` automatically as dependencies,
so nothing else is needed.

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

After installation, four lazy-loaded skills become available. Each has its
own trigger conditions; only the matching skill's context is pulled into
Claude's window per request:

| Skill | Triggers on requests like |
|---|---|
| `llamaparse` | "Parse this PDF with LlamaParse." / "OCR this scan." / "Convert this Excel to markdown." |
| `llamaextract` | "Extract invoice number and total from this PDF." / "Pull fields out as JSON using this schema." |
| `llamaclassify` | "Classify this document — is it a contract, invoice, or receipt?" / "Route incoming docs by type." |
| `llamasplit` | "Split this long report into intro / methodology / results / appendix sections." |

You can also invoke any of them explicitly via the slash menu:
`/llamaparse-plugin:<skill>`.

The first time a skill runs in a fresh sandbox it will `pip install
llama-cloud` automatically (the bundled scripts pass `--auto-install`), so
you don't need to set anything up beyond the API key.

## Install — Claude Cowork plugin

Cowork manages plugins through the **Customize** menu (no `/plugin` slash
command in Cowork).

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
in Admin settings), then fully restart Cowork. Claude Code does not have
this restriction.

### Local-folder install (plugin development)

If you've cloned the repo and want to test changes without pushing:

1. **Customize** → **+** → **Add marketplace from local folder**
2. Point it at the cloned `llamaparse-plugin` directory
3. Install as above

## Cost

All four capabilities are billed per page processed. Parse exposes a tier
knob; extract / classify / split don't (one per-page rate each).

**Parse tiers:**

| Tier             | Approx multiplier | Best for                                       |
|------------------|-------------------|------------------------------------------------|
| `fast`           | ~1 cr/page        | Plain text, simple layouts                     |
| `cost_effective` | ~3 cr/page        | Default; balanced quality                      |
| `agentic`        | ~15 cr/page       | Tables, multi-column, mixed media              |
| `agentic_plus`   | ~30+ cr/page      | Dense tables, charts, the hardest documents    |

All four parse tiers can return markdown in v2 (the v1 "fast = text-only"
restriction is gone). Verify current pricing at <https://cloud.llamaindex.ai>
before committing to large batches.

**Classify** has two `--mode` settings: `fast` (text-only, cheap) and
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
│   └── _split.py                   — LlamaSplit v1 beta
├── skills/
│   ├── llamaparse/                 — parse → markdown/text
│   │   ├── SKILL.md
│   │   ├── scripts/parse_document.py
│   │   └── references/{rest_api,troubleshooting}.md
│   ├── llamaextract/               — schema-driven structured extraction
│   │   ├── SKILL.md
│   │   └── scripts/run_extract.py
│   ├── llamaclassify/              — categorization with confidence
│   │   ├── SKILL.md
│   │   └── scripts/run_classify.py
│   └── llamasplit/                 — section splitting (v1 beta)
│       ├── SKILL.md
│       └── scripts/run_split.py
└── README.md
```

Each skill is independent and lazy-loaded: Claude pulls in only the
SKILL.md whose description matches the user's request, so feature context
stays out of the window until needed. All four shell into the same
`llamaparse_cli` package, so the CLI and the skills never drift.

## License

MIT — see [LICENSE](./LICENSE).
