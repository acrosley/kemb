# Changelog

All notable changes to `kemb` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `index` facet: a persistent, incremental SQLite inventory of a corpus
  (`kemb index ./corpus`, database at `<corpus>/.kemb/index.db`). Stores
  per-file metadata, a sha256 content hash, and the same locally extracted
  text sample `probe --sample` produces. Rescans are incremental — only
  files whose size or mtime changed are re-read — so repeat scans over
  100k-file corpora take seconds. Includes duplicate detection by content
  hash, FTS5 full-text search over samples and paths (`--search`, with a
  substring fallback when FTS5 is unavailable), a `--stats` report, and
  missing-file tracking that preserves history when files reappear. Queries
  sync on read — `--stats`/`--search` run the incremental refresh before
  answering (skip with `--stale`) so they never serve a stale view. Schema
  v1 also reserves a `passes` table so the upcoming batch facet can record
  resumable per-file job status without a migration. Local-only: zero
  credits, no network, no API key.
- `probe --sample`: extracts the first words of every document locally (PDF
  via `pypdf`, DOCX/PPTX/XLSX/ODT/ODS/ODP via their XML, text/HTML/CSV
  directly) and renders a single corpus sample of XML-tagged `<document>`
  blocks — labeled metadata attributes (path, size, PDF page count, mtime,
  type, text status) with up to `--sample-words` words of content as the
  body. PDFs with no text layer collapse to a self-closing tag whose `note`
  flags them as likely scans needing an OCR-capable parse tier.
  `--sample-budget` caps total words corpus-wide (files past the budget keep
  their inventory line; only sample text is skipped); `--sample-pages`
  bounds how many PDF pages are read. Combines with `--json` to embed
  `sample` / `sample_status` / `pages` fields per file. Lets an agent weigh
  a large multi-directory corpus in one read — zero network calls, zero
  credits, no per-file model pass required.
- New dependency: `pypdf>=4.0` (pure-Python; powers PDF sampling and page
  counts).

### Removed
- `extract` and `split` facets — subcommands, `_extract.py` / `_split.py`
  modules, skill references, example schema/category files, and tests.
  Rationale: once `parse` has produced clean markdown, the consuming agent
  (Claude) extracts fields to a schema and splits sections itself — zero
  LlamaCloud credits, zero extra plumbing, full conversation context.
  `classify` remains for routing documents *before* parsing (scans and
  layout-heavy files an agent can't read locally). The removed code stays
  in git history if an API-side extract/split is ever needed again.
- `docs/llamacloud/` — the local mirror of the LlamaCloud docs site
  (~900 pages) and its support tooling: `scripts/fetch_docs.py`,
  `scripts/check_docs_staleness.py`, `scripts/docs_common.py`, and the
  weekly `docs-staleness` workflow with its `docs-drift` tracking issues.
  Nothing in the package, skill, or tests referenced the mirror — the
  skill ships its own distilled per-facet references — and the weekly
  drift triage competed with building the corpus-curation core
  (`docs/goal.txt`). The mirror remains available in git history.

### Fixed
- The bundled skill shim (`skills/kemb/scripts/kemb_cli.py`) now degrades
  gracefully when the skill directory is copied outside the repo (plugin
  marketplace installs, snapshots), where its repo-relative `src/` lookup
  can't work: it falls back to an installed `kemb` package, pip-installs
  kemb from `git+https://github.com/acrosley/kemb` under `--auto-install`
  (mirroring the llama-cloud auto-install), and otherwise exits with a
  one-line remedy instead of an `ImportError` traceback.

## [0.6.0] - 2026-05-30

### Changed
- **Rebrand: `llamaparse-plugin` → `kemb`.** Repository, Python package
  (`llamaparse_cli` → `kemb`), CLI command (`llamaparse` → `kemb`), and
  plugin/marketplace identifiers all renamed. Project reframed from
  "LlamaCloud wrapper" to corpus curation for agent-ready PDF libraries
  (see `docs/goal.txt`). The four LlamaCloud APIs (parse, extract,
  classify, split) remain as facets under a single orchestrating `kemb`
  skill, now joined by a local `probe` facet (see Added); the previous four
  user-facing skills folded into
  `skills/kemb/references/{parse,extract,classify,split}.md`.

### Removed
- `llamaparse` CLI command — no deprecated alias. Use `kemb` instead.
- `skills/llamaparse/`, `skills/llamaextract/`, `skills/llamaclassify/`,
  `skills/llamasplit/` — replaced by the single `skills/kemb/` orchestrator
  with per-facet reference docs.

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

### Fixed
- `repository` field in `.claude-plugin/plugin.json` is now a string URL
  (matches Claude Code's plugin manifest schema). Previously it was an
  npm-style `{ type, url }` object, which caused `/plugin install` to
  fail with `repository: Invalid input: expected string, received object`.

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

[Unreleased]: https://github.com/acrosley/kemb/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/acrosley/kemb/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/acrosley/kemb/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/acrosley/kemb/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/acrosley/kemb/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/acrosley/kemb/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/acrosley/kemb/releases/tag/v0.1.0
