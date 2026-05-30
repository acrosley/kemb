# Contributing

Thanks for your interest in `kemb`. Bug reports, feature
requests, and pull requests are all welcome.

## Dev setup

```bash
git clone https://github.com/acrosley/kemb
cd kemb
pip install -e ".[test]"
```

Set your LlamaCloud key before running anything that touches the network:

```bash
export LLAMA_CLOUD_API_KEY="llx-..."   # get one at https://cloud.llamaindex.ai/api-key
```

## Running tests

```bash
pytest
```

Tests should not require live API access. Anything that would call out to
LlamaCloud must be mocked — never commit a fixture that requires a real key.

## Code style

- Match the patterns already in the repo. Two spaces of import grouping
  (stdlib / third-party / local), `from __future__ import annotations` at the
  top of every module, type hints on public helpers.
- Cross-cutting concerns (auth, SDK loading, REST polling, file upload, JSON
  parsing, error surfacing, output writing) live in
  `src/kemb/_common.py`. Reuse them — don't reinvent.
- Each capability gets its own module under `src/kemb/`. All capabilities
  surface through the single `skills/kemb/` orchestrating skill, with
  per-facet docs under `skills/kemb/references/`. Keep capability modules
  focused on what makes them different (request shape, response shape,
  post-processing).

## Adding a new capability

Use `_parse.py`, `_extract.py`, `_classify.py`, or `_split.py` as a template
(`_extract.py` is the closest "standard" example — SDK + REST + JSON I/O).
Each module exposes the same three things:

1. `*_with_sdk(...)` and `*_with_rest(...)` runner functions that share the
   helpers in `_common.py`.
2. `add_subparser(subparsers)` that wires up `argparse` flags.
3. `run(args)` that orchestrates SDK-first / REST-fallback and writes output.

Then register the subcommand in `src/kemb/_core.py` (add it to
`SUBCOMMANDS` and call its `add_subparser` from `build_parser`), and add a
facet doc under `skills/kemb/references/<name>.md` describing when to use
it. Update the routing table in `skills/kemb/SKILL.md` so the orchestrating
skill knows about the new facet.

## Pull requests

- Tests pass (`pytest`).
- No API keys, tokens, or live-response fixtures in commits.
- Update `CHANGELOG.md` under `[Unreleased]` (Keep a Changelog format) —
  Added / Changed / Fixed / Removed as appropriate.
- Keep PRs focused; one capability or one fix per PR is easier to review.

## Reporting issues

File issues at <https://github.com/acrosley/kemb/issues>.
Include the CLI command you ran, the LlamaCloud API the failure came from
(parse / extract / classify / split), and the verbatim error. **Never paste
your API key**, even partially — the CLI surfaces errors with `error: …`
prefixes that should be safe to share, but double-check before posting.
