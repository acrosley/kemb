# llamaparse-plugin

A Claude Cowork / Claude Code plugin that bundles a single skill, `llamaparse`, for parsing documents with [LlamaIndex's hosted LlamaParse API](https://cloud.llamaindex.ai). Once installed, the skill auto-triggers whenever you ask Claude to parse a PDF, scan, Office doc, or other complex document, and it works across every Cowork session — no per-project setup.

## What's inside

```
llamaparse-plugin/
├── .claude-plugin/
│   ├── marketplace.json            — marketplace manifest (root of repo)
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
            ├── rest_api.md         — REST API reference
            └── troubleshooting.md  — common failure modes and fixes
```

## Install (recommended: from GitHub)

This installs the plugin globally for your Cowork user — every session and every project on this machine will pick up the `llamaparse` skill automatically.

In Cowork, open the slash menu and run:

```
/plugin marketplace add acrosley/llamaparse-plugin
/plugin install llamaparse-plugin@llamaparse
```

To pull updates later:

```
/plugin marketplace update llamaparse
```

To uninstall:

```
/plugin uninstall llamaparse-plugin@llamaparse
/plugin marketplace remove llamaparse
```

## Install (alternative: local clone)

If you'd rather run from a working copy on disk:

```
/plugin marketplace add C:\path\to\llamaparse-plugin
/plugin install llamaparse-plugin@llamaparse
```

Cowork will read `.claude-plugin/marketplace.json` from that path. Useful while iterating on the skill itself.

## Prerequisites

1. **API key.** Get one from <https://cloud.llamaindex.ai/api-key>. Set it as a persistent user environment variable (PowerShell):
   ```powershell
   setx LLAMA_CLOUD_API_KEY "llx-..."
   ```
   Fully quit and relaunch Cowork after `setx` so the new env var propagates into the sandbox.

2. **Network access.** The Cowork sandbox must be allowed to reach `api.cloud.llamaindex.ai`. If you see `403 Forbidden` from the proxy, add the host under Settings → Capabilities → network allowlist (or, on Team/Enterprise, ask an org owner to do it in Admin settings), then fully restart Cowork.

3. **Python deps.** Auto-installed inside the sandbox the first time the skill runs:
   ```bash
   pip install llama-cloud-services --break-system-packages
   ```

## How to invoke the skill

After installation the skill auto-triggers on natural-language requests like:

- "Parse this PDF with LlamaParse and give me clean markdown."
- "OCR this scan."
- "Extract the tables from contract.pdf."

You can also invoke it explicitly via the slash menu: `/llamaparse-plugin:llamaparse`.

## Cost

LlamaParse charges credits per page, scaled by tier:

| Tier            | Approx multiplier   | Notes                                |
|-----------------|---------------------|--------------------------------------|
| `fast`          | ~1 cr/page          | Text-only — no markdown              |
| `cost_effective`| ~3 cr/page          | Default; balanced quality            |
| `agentic`       | ~15 cr/page         | Better tables / layout               |
| `agentic_plus`  | ~30+ cr/page        | Best quality, most expensive         |

The skill always counts pages first and confirms the estimated cost (`pages × multiplier`) before parsing anything over ~10 pages. Verify current pricing at <https://cloud.llamaindex.ai> before committing to large batches.

## Updating

Bump `version` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, commit, and push. Users pull the new version with `/plugin marketplace update llamaparse`.

## License

MIT — see [LICENSE](./LICENSE).
