# Changelog

All notable changes to `llamaparse-plugin` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `probe` subcommand: recursively walks a target directory and reports
  per-file metadata (path, size, mtime, extension, mime type, whether the
  format is LlamaCloud-friendly) with a summary block at the end. Supports
  `--ext`, `--max-depth`, `--max-files`, `--include-hidden`,
  `--supported-only`, `--follow-symlinks`, `--json`, and `--output`. Spends
  zero credits — useful for previewing batch jobs before paying for them.
- `--dry-run` flag on `parse`, `extract`, `classify`, and `split`. Validates
  inputs (file exists, schema/rules/categories parse, mutually-exclusive
  flags aren't combined), resolves the output path, and prints the
  configuration that would be sent without uploading the document or
  starting a job. Pairs with `probe` for safe batch planning.
- `doctor` subcommand: preflight checks for Python version, package version,
  `requests` and `llama-cloud` availability, `LLAMA_CLOUD_API_KEY` presence
  (masked when printed), and a non-billable HEAD probe against
  `api.cloud.llamaindex.ai` to confirm the key authenticates. Spends zero
  credits — never uploads a document or starts a job. Use `--offline` to
  skip the network probe.

## [0.5.0] - 2026-05-13

### Added
- `extract` subcommand wrapping LlamaExtract v2 (schema-driven structured
  JSON extraction).
- `classify` subcommand wrapping LlamaClassify v2 (document categorization
  with confidence + reasoning).
- `split` subcommand wrapping LlamaSplit v1 beta (typed section splitting
  with page ranges).
- Subcommand dispatcher in `src/llamaparse_cli/_core.py` exposing
  `parse / extract / classify / split` under one `llamaparse` binary.
- Three new lazy-loaded skills — `llamaextract`, `llamaclassify`,
  `llamasplit` — each with its own `SKILL.md` and runner script under
  `skills/`.
- Shared helpers consolidated into `src/llamaparse_cli/_common.py`
  (auth, SDK loader, REST poller, file upload, error surfacing).

### Changed
- README documents all four capabilities and both installation modes
  (plugin and CLI).
- `pyproject.toml` description updated to reflect the multi-capability
  surface.

### Preserved
- `llamaparse <file>` (no subcommand) still dispatches as `parse`, so
  existing scripts and workflows keep working unchanged.

## [0.4.0] - 2026-05-13

### Added
- Standalone `llamaparse` CLI exposed via a `console_script` in
  `pyproject.toml`; implementation moved to `src/llamaparse_cli/_core.py`
  so the CLI and the skill share one source of truth.
- `--auto-install` flag installs `llama-cloud` on first run inside fresh
  sandboxes.

### Fixed
- Parse flow no longer calls the invalid `files.create(purpose="parse")`
  step; `client.parsing.parse(upload_file=...)` handles upload, polling,
  and fetch in one call.
- REST status reads from `.job.status` (v2's actual shape) instead of the
  top-level `.status` that v1 used.
- Default poll timeout bumped from 300s to 600s to accommodate large
  scans.

## [0.3.0] - 2026-04-30

### Added
- `--strip-noise` post-processor: drops LlamaParse layout-hint HTML
  comments and repeating image refs (e.g. header/footer logos).
- API errors are surfaced verbatim instead of as Python tracebacks.

### Fixed
- v2 API rejected `input_options.language` with `extra_forbidden`. The
  field (and the matching `--language` CLI flag) is removed; v2
  auto-detects language.

## [0.2.0] - 2026-04-30

### Changed
- Upgraded to LlamaParse API v2 (`/api/v2/parse/...`).
- SKILL.md, REST reference, troubleshooting guide, and script rewritten
  around the v2 lifecycle (upload → poll → fetch).

## [0.1.0] - 2026-04-30

### Added
- Initial release of the llamaparse Cowork plugin (parse only).
- LlamaParse skill with `SKILL.md`, REST API reference, troubleshooting
  guide, and `parse_document.py` runner.
- Marketplace and plugin manifests under `.claude-plugin/`.
- MIT license.

[Unreleased]: https://github.com/acrosley/llamaparse-plugin/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/acrosley/llamaparse-plugin/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/acrosley/llamaparse-plugin/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/acrosley/llamaparse-plugin/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/acrosley/llamaparse-plugin/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/acrosley/llamaparse-plugin/releases/tag/v0.1.0
