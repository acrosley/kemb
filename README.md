# llamaparse-plugin

A Claude plugin (works in **Claude Cowork** and **Claude Code**) that bundles a single skill, `llamaparse`, for parsing documents with [LlamaIndex's hosted LlamaParse API](https://cloud.llamaindex.ai). Once installed, the skill auto-triggers whenever you ask Claude to parse a PDF, scan, Office doc, or other complex document.

> **API v2 only.** This plugin uses the new `llama-cloud` Python SDK and the v2 REST endpoints. The legacy `llama-cloud-services` / `llama-parse` packages (v1) are deprecated by LlamaIndex and slated for archive after May 1, 2026, and are not supported here.

## What's inside

```
llamaparse-plugin/
├── .claude-plugin/
│   ├── marketplace.json            — marketplace manifest
│   └── plugin.json                 — plugin manifest
├── LICENSE
├── README.md
├── .gitignore
└── skills/
    └── llamaparse/
        ├── SKILL.md                — skill definition (YAML frontmatter + instructions)
        ├── scripts/
        │   └── parse_document.py   — driver script (SDK with REST fallback)
        └── references/
            ├── rest_api.md         — v2 REST API reference
            └── troubleshooting.md  — common failure modes and fixes
```

## Install in Claude Cowork

Cowork manages plugins through the **Customize** menu — there's no `/plugin` slash command in Cowork.

1. Open Claude Desktop and switch to the **Cowork** tab.
2. Click **Customize** in the left sidebar.
3. Click the **+** button → **Add marketplace from GitHub**.
4. Enter `acrosley/llamaparse-plugin` (or your fork's `<owner>/<repo>`).
5. Once the marketplace appears, find `llamaparse-plugin` and click **Install**.
6. Fully quit Cowork from the system tray and relaunch.

After the restart, the skill auto-loads in every Cowork session on your machine.

To pull updates later, return to **Customize** and refresh the marketplace.

### Local-folder install (for plugin development)

If you've cloned the repo and want to test changes without pushing:

1. **Customize** → **+** → **Add marketplace from local folder**
2. Point it at the cloned `llamaparse-plugin` directory
3. Install as above

## Install in Claude Code

Claude Code does support the slash-command flow:

```
/plugin marketplace add acrosley/llamaparse-plugin
/plugin install llamaparse-plugin@llamaparse
```

Updates:

```
/plugin marketplace update llamaparse
```

Uninstall:

```
/plugin uninstall llamaparse-plugin@llamaparse
/plugin marketplace remove llamaparse
```

## Prerequisites

### 1. API key

Get one from <https://cloud.llamaindex.ai/api-key> and set it as a persistent environment variable:

**macOS / Linux** (bash/zsh):

```bash
echo 'export LLAMA_CLOUD_API_KEY="llx-..."' >> ~/.zshrc   # or ~/.bashrc
source ~/.zshrc
```

**Windows** (PowerShell):

```powershell
setx LLAMA_CLOUD_API_KEY "llx-..."
```

Restart Claude (Cowork or Claude Code) afterward so the new env var propagates into the sandbox.

### 2. Network access

The Cowork sandbox uses an HTTPS allowlist. If you see `403 Forbidden` from the proxy when calling `api.cloud.llamaindex.ai`, add the host under **Settings → Capabilities → network allowlist** (Team/Enterprise plans require an org owner to do this in Admin settings), then fully restart Cowork. Claude Code does not have this restriction.

### 3. Python deps

Auto-installed inside the sandbox the first time the skill runs:

```bash
pip install llama-cloud --break-system-packages
```

Do **not** install `llama-cloud-services` — that's the v1 package and is not used by this plugin.

## How to invoke the skill

After installation the skill auto-triggers on natural-language requests like:

- "Parse this PDF with LlamaParse and give me clean markdown."
- "OCR this scan."
- "Extract the tables from contract.pdf."

You can also invoke it explicitly via the slash menu: `/llamaparse-plugin:llamaparse`.

## Cost

LlamaParse charges credits per page, scaled by tier:

| Tier             | Approx multiplier | Best for                                  |
|------------------|-------------------|-------------------------------------------|
| `fast`           | ~1 cr/page        | Plain text, simple layouts                |
| `cost_effective` | ~3 cr/page        | Default; balanced quality                 |
| `agentic`        | ~15 cr/page       | Tables, multi-column, mixed media         |
| `agentic_plus`   | ~30+ cr/page      | Dense tables, charts, the hardest documents |

In v2, all four tiers can return markdown — the v1 "fast tier is text-only" restriction is gone.

The skill counts pages first and confirms the estimated cost (`pages × multiplier`) before parsing anything over ~10 pages. Verify current pricing at <https://cloud.llamaindex.ai> before committing to large batches.

## Updating the plugin

Bump `version` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, commit, and push. Users pull the new version through their host's update flow (Customize → refresh in Cowork; `/plugin marketplace update llamaparse` in Claude Code).

## License

MIT — see [LICENSE](./LICENSE).
