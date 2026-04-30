# LlamaParse troubleshooting (v2)

This skill targets LlamaParse API v2 only. When something goes wrong, surface the upstream error to the user verbatim before guessing — the remediation almost always lives in the response body.

## "LLAMA_CLOUD_API_KEY is not set"

The skill never accepts the key as a CLI argument or stores it in a config file — it only reads `LLAMA_CLOUD_API_KEY` from the environment. Have the user run:

```bash
export LLAMA_CLOUD_API_KEY=llx-...
```

…in the same shell session before invoking the script. For a permanent setup on Windows, use `setx LLAMA_CLOUD_API_KEY "llx-..."` and fully restart your Claude host; on macOS/Linux, add it to the shell rc file. Keys come from https://cloud.llamaindex.ai/api-key.

If the user has stored their key under a different env var name (e.g., `LLAMAPARSE_API_KEY`), alias it for the run:

```bash
export LLAMA_CLOUD_API_KEY="$LLAMAPARSE_API_KEY"
```

## `403 Forbidden` from proxy on `api.cloud.llamaindex.ai`

Some Claude hosts (notably Cowork) run the script inside a sandbox with an HTTPS allowlist enforced at a local proxy. If outbound HTTPS to `api.cloud.llamaindex.ai` returns `403 Forbidden` *before* reaching the LlamaParse server, the host is not on the allowlist. Verify with:

```bash
curl -sS -o /dev/null -w "HTTP %{http_code}\n" --max-time 10 https://api.cloud.llamaindex.ai/
```

A 403 here is a host-side block, not a LlamaParse auth failure. To unblock:

1. Add `api.cloud.llamaindex.ai` to the host's network allowlist (in Cowork: Settings → Capabilities; org owners only on Team/Enterprise plans, where it lives under Admin settings).
2. Fully restart the host so the new allowlist takes effect.
3. Retry — should now hit the LlamaParse server.

If allowlisting isn't possible (e.g., the user isn't an org owner), fall back to running `parse_document.py` outside the sandbox in their normal terminal.

## `ImportError: llama_cloud` or `cannot import name 'LlamaCloud'`

The v2 SDK lives in the `llama-cloud` package:

```bash
pip install llama-cloud --break-system-packages
```

**Do not install `llama-cloud-services` or `llama-parse`.** Those are the v1 packages, deprecated by LlamaIndex and slated for archive after May 1, 2026. The bundled script will not use them.

If the SDK still won't install, rerun with `--rest` to use the REST path, which only needs `requests`.

## `400 Bad Request` with "version is required" or "tier is required"

In v2, both `tier` and `version` are required fields in the `configuration` JSON. The bundled script always sends them (defaults: `tier=cost_effective`, `version=latest`). If you see this error from a custom integration, add both to your configuration envelope:

```json
{
  "tier": "cost_effective",
  "version": "latest"
}
```

For reproducible production runs, pin `version` to a dated value like `"2026-01-08"` instead of `"latest"`.

## SDK install fails with dependency conflicts

`llama-cloud` is much leaner than the old `llama-cloud-services` (which pulled in llama-index-core, sqlalchemy, nltk, tiktoken, etc.). Conflicts are rare. If pip can't resolve in the user's existing environment, install into a fresh venv or use `--rest` mode and skip the SDK entirely. The REST path produces identical output for the markdown/text use cases.

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

1. **Tier too low for the document.** Complex layouts, small fonts, or noisy scans benefit from `agentic` or `agentic_plus`. The default `cost_effective` is a good starting point but isn't optimal for everything.
2. **Encrypted PDF**. LlamaParse can't open a password-protected PDF. Decrypt first with `qpdf --decrypt`.
3. **Scanned image with low DPI**. If pages are sub-150-DPI scans, OCR quality will be poor regardless of parser. Suggest re-scanning or running the source through an image upscaler first.
4. **Wrong result type**. `text` strips formatting — for tables or layout-sensitive content, use `markdown`.
5. **Non-English document**. v2 auto-detects language; the v1 `input_options.language` override was removed. If detection fails on a non-English doc, check the current LlamaIndex docs for any new override path before assuming the parser is broken.

## SDK or REST response shape changed unexpectedly

LlamaParse APIs evolve. If a script that worked yesterday breaks today on field names, check the SDK source at https://github.com/run-llama/llama-cloud-py and the API reference on the LlamaIndex docs site.

The bundled script defends against several known v2 shape variations (e.g., `id` vs `job_id`, expanded content under `result` vs at top level, single string vs `pages` array). If a new variant appears, adjust `_extract_sdk_result` / `_extract_rest_field` in `scripts/parse_document.py` rather than working around it in user code.

## Rate limiting (`429`)

Free-tier accounts have a limited daily page quota. Paid plans have higher rate limits but they exist. On a 429, back off 30–60s and retry; if it persists, the user has hit their plan's cap and needs to upgrade or wait for the quota reset.

## "Why doesn't the skill use llama-cloud-services?"

Per LlamaIndex's announcement (Q1 2026), `llama-cloud-services` and the older `llama-parse` package only support API v1 and are scheduled for archive after May 1, 2026. The new `llama-cloud` package supports v2 only. This skill is v2-only, so it depends on `llama-cloud`. If a user is locked into v1 for some legacy reason, they need a different skill.
