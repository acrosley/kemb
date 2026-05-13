# llamaparse-plugin

A Claude plugin **and** a tiny standalone CLI for parsing documents with
[LlamaIndex's hosted LlamaParse v2 API](https://cloud.llamaindex.ai).

Same code path in both modes:

| Mode | What you run | What it gives you |
|---|---|---|
| Plugin | `/plugin install llamaparse-plugin@llamaparse` in Claude Code (or "Add marketplace from GitHub" in Cowork) | A `llamaparse` skill that auto-triggers when you ask Claude to parse a PDF / scan / Office doc |
| CLI | `pipx install git+https://github.com/acrosley/llamaparse-plugin` | A `llamaparse` command on your PATH |

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

That gives you a `llamaparse` command:

```bash
llamaparse ./contract.pdf                       # → contract.md
llamaparse ./scan.pdf --tier agentic            # agentic tier
llamaparse ./report.pdf --output ./out.md       # explicit output path
llamaparse ./report.pdf --result-type text      # → report.txt
llamaparse ./report.pdf --strip-noise           # drop layout-hint comments
llamaparse ./report.pdf --rest                  # force REST path (no SDK)
llamaparse --help
```

The CLI installs `llama-cloud` and `requests` automatically as
dependencies, so nothing else is needed.

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

After installation the skill auto-triggers on requests like:

- "Parse this PDF with LlamaParse and give me clean markdown."
- "OCR this scan."
- "Extract the tables from contract.pdf."

You can also invoke it explicitly via the slash menu:
`/llamaparse-plugin:llamaparse`.

The first time the skill runs in a fresh sandbox it will `pip install
llama-cloud` automatically (the bundled script passes `--auto-install`), so
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

LlamaParse charges credits per page, scaled by tier:

| Tier             | Approx multiplier | Best for                                       |
|------------------|-------------------|------------------------------------------------|
| `fast`           | ~1 cr/page        | Plain text, simple layouts                     |
| `cost_effective` | ~3 cr/page        | Default; balanced quality                      |
| `agentic`        | ~15 cr/page       | Tables, multi-column, mixed media              |
| `agentic_plus`   | ~30+ cr/page      | Dense tables, charts, the hardest documents    |

All four tiers can return markdown in v2 (the v1 "fast = text-only"
restriction is gone). Verify current pricing at <https://cloud.llamaindex.ai>
before committing to large batches.

## What's inside

```
llamaparse-plugin/
├── .claude-plugin/
│   ├── marketplace.json            — marketplace manifest
│   └── plugin.json                 — plugin manifest
├── pyproject.toml                  — packaging for the `llamaparse` CLI
├── src/llamaparse_cli/
│   ├── __init__.py
│   └── _core.py                    — canonical parse implementation
├── skills/llamaparse/
│   ├── SKILL.md                    — skill definition
│   ├── scripts/parse_document.py   — thin shim that calls llamaparse_cli._core
│   └── references/
│       ├── rest_api.md             — REST API reference
│       └── troubleshooting.md      — common failure modes
└── README.md
```

Both modes share `src/llamaparse_cli/_core.py`, so the CLI and the skill
never drift.

## License

MIT — see [LICENSE](./LICENSE).
