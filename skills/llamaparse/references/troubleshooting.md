# LlamaParse troubleshooting

When something goes wrong, surface the upstream error to the user verbatim before guessing. The remediation almost always lives in the response body.

## "LLAMA_CLOUD_API_KEY is not set"

The skill never accepts the key as a CLI argument or stores it in a config file — it only reads `LLAMA_CLOUD_API_KEY` from the environment. Have the user run:

```bash
export LLAMA_CLOUD_API_KEY=llx-...
```

…in the same shell session before invoking the script. For a permanent setup, add it to their shell rc file or to Cowork's environment configuration. Keys come from https://cloud.llamaindex.ai/api-key.

If the user has stored their key under a different env var name (e.g., `LLAMAPARSE_API_KEY`), alias it for the run:

```bash
export LLAMA_CLOUD_API_KEY="$LLAMAPARSE_API_KEY"
```

## `403 Forbidden` from proxy on api.cloud.llamaindex.ai

Cowork's sandbox uses a network allowlist enforced at the HTTP proxy. If outbound HTTPS to `api.cloud.llamaindex.ai` returns `403 Forbidden` *before* reaching the LlamaParse server, the host is not on the allowlist. Verify with:

```bash
curl -sS -o /dev/null -w "HTTP %{http_code}\n" --max-time 10 https://api.cloud.llamaindex.ai/
```

A 403 here is a Cowork-side block, not a LlamaParse auth failure. To unblock:

1. Org owner adds `api.cloud.llamaindex.ai` to Admin settings → Capabilities → network allowlist.
2. Fully restart Cowork (system tray → Quit, then relaunch).
3. Retry — should now hit the LlamaParse server.

If the user isn't an org owner or the setting doesn't exist on their plan, fall back to running `parse_document.py` outside the sandbox in their normal terminal.

## `ImportError: llama_cloud` or `cannot import name 'LlamaParse' from 'llama_cloud'`

The bare `llama-cloud` package does NOT export `LlamaParse`. The class lives in `llama-cloud-services`:

```bash
pip install llama-cloud-services --break-system-packages
```

Or use the legacy `llama-parse` package if you prefer. The bundled script tries both.

If the SDK still won't install, rerun with `--rest` to use the REST path, which only needs `requests`.

## SDK install fails with dependency conflicts

The SDK pulls a fairly large dependency tree (llama-index-core, sqlalchemy, nltk, tiktoken, etc.). If pip can't resolve in the user's existing environment, install into a fresh venv or use `--rest` mode and skip the SDK entirely. The REST path produces identical output for the markdown/text use cases.

## "tier='fast' does not support markdown output"

The `fast` tier is text-only — it can't return markdown, items, or per-format content metadata. Either:
- Switch tier: `--tier cost_effective` (or `agentic` / `agentic_plus`).
- Switch format: `--result-type text`.

This is a deliberate constraint of the tier system, not a bug.

## Job stuck in `PENDING` / `RUNNING`

Large or scanned documents can take several minutes. The bundled script defaults to a 300-second poll timeout. If a real job needs longer:

```bash
python scripts/parse_document.py big.pdf --rest --poll-timeout 900
```

If a job genuinely hangs (stays `RUNNING` past 10 minutes for a normal-sized doc), it's worth canceling and resubmitting — occasionally a worker dies and the queue takes a while to notice.

## `413 Payload Too Large`

The file exceeds LlamaParse's per-job size cap (around 300MB at time of writing). Split the document with `pdftk` / `qpdf` / `pypdf` and parse the chunks separately, then concatenate the markdown.

## Parsed output looks garbled or empty

A few things to check, in order:

1. **Wrong language**. If the document is non-English, set `--language es` (or whatever code matches). LlamaParse defaults to `en` and that hurts OCR on other-language scans.
2. **Tier too low for the document.** Complex layouts, small fonts, or noisy scans benefit from `agentic` or `agentic_plus`. The default `cost_effective` is a good starting point but isn't optimal for everything.
3. **Encrypted PDF**. LlamaParse can't open a password-protected PDF. Decrypt first with `qpdf --decrypt`.
4. **Scanned image with low DPI**. If pages are sub-150-DPI scans, OCR quality will be poor regardless of parser. Suggest re-scanning or running the source through an image upscaler first.
5. **Wrong result type**. `text` strips formatting — for tables or layout-sensitive content, always use `markdown` (and a non-`fast` tier).

## SDK or REST response shape changed unexpectedly

LlamaParse APIs evolve. If a script that worked yesterday breaks today on field names, check the SDK source at `https://github.com/run-llama/llama-cloud-py` and the API reference on the LlamaIndex docs site.

The bundled script already defends against several known shape variations (e.g., `id` vs `job_id`, expanded content at top level vs under `result` vs under a `pages` array). If a new variant appears, adjust `parse_with_rest` in `scripts/parse_document.py` rather than working around it in user code.

## Rate limiting (`429`)

Free-tier accounts have a limited daily page quota. Paid plans have higher rate limits but they exist. On a 429, back off 30–60s and retry; if it persists, the user has hit their plan's cap and needs to upgrade or wait for the quota reset.
