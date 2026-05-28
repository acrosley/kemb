# LlamaCloud docs mirror

A read-only mirror of every public LlamaCloud documentation page, fetched as
raw markdown from `developers.llamaindex.ai` (the canonical docs host —
`docs.cloud.llamaindex.ai` redirects there).

This mirror exists so that:

- Skills and agents can grep / read docs locally without hitting the network
  on every prompt.
- The plugin can be developed against a frozen-in-time view of the API surface
  and we can prove when our understanding has gone stale.
- Future model context windows can be primed from a single tree instead of
  ~900 individual HTTP requests.

## What is mirrored

| Prefix          | Pages | Contents                                                          |
| --------------- | ----- | ----------------------------------------------------------------- |
| `llamaparse/`   | ~170  | Product docs for Parse, Extract, Classify, Split, Sheets, etc.    |
| `reference/`    | ~715  | Auto-generated CLI / Python / TypeScript / Go / REST SDK reference |

Scope is locked to those two prefixes via `INCLUDED_PREFIXES` in
[`scripts/docs_common.py`](../../scripts/docs_common.py). The LlamaIndex
*framework* docs (`/python/*`, `/typescript/framework/*`) and LiteParse are
intentionally excluded — they are not part of LlamaCloud.

## File layout

```
docs/llamacloud/
├── _manifest.json                              ← single source of truth
├── llamaparse/
│   ├── index.md
│   ├── parse/getting_started/index.md
│   └── ...
└── reference/
    ├── cli/...
    ├── python/...
    ├── typescript/...
    └── ...
```

Each page is stored at `<upstream-path>/index.md` so the directory structure
mirrors the URL structure 1:1.

## The manifest

`_manifest.json` records, per page:

- `url`         — upstream raw-markdown URL (`<page>/index.md`)
- `sha256`      — hash of the raw markdown body
- `bytes`       — content length
- `fetched_at`  — ISO-8601 UTC timestamp

Plus a top-level `known_missing` map for URLs that 404 upstream (e.g. landing
pages that redirect). The staleness checker treats a flip in either direction
(known-missing → 200, or 200 → 404) as drift.

## Refreshing the mirror

```bash
python scripts/fetch_docs.py          # full refresh, ~30s
python scripts/fetch_docs.py --limit 5  # smoke test
python scripts/fetch_docs.py --dry-run  # list URLs only
```

The fetcher is idempotent — it overwrites files unconditionally and rewrites
the manifest, so the diff in `git status` exactly equals the upstream change
since the last refresh.

## Staleness tracking

```bash
python scripts/check_docs_staleness.py          # human-readable report, exit 1 on drift
python scripts/check_docs_staleness.py --json   # machine-readable report
python scripts/check_docs_staleness.py --quiet  # exit code only
```

The script re-fetches every URL in the manifest, re-hashes, and classifies
each result:

| Class         | Meaning                                                |
| ------------- | ------------------------------------------------------ |
| `unchanged`   | sha256 still matches the manifest                      |
| `modified`    | sha256 differs — upstream changed                      |
| `gone`        | tracked URL now 404s upstream                          |
| `resurrected` | URL was in `known_missing`, now returns 200            |
| `added`       | new page appeared in the sitemap, not yet mirrored     |
| `removed`     | tracked URL no longer in the sitemap                   |

Any non-zero count of the last five exits 1.

## CI

[`.github/workflows/docs-staleness.yml`](../../.github/workflows/docs-staleness.yml)
runs the check weekly (Mondays 14:00 UTC) and on manual dispatch. When drift
is detected it opens or updates a tracking issue labeled `docs-drift`, attaches
the full JSON report as an artifact, and closes the issue automatically once
the mirror is back in sync.

## When to refresh

Run `scripts/fetch_docs.py` and commit the result whenever:

- The weekly CI job opens a `docs-drift` issue.
- You touch parsing/extract/classify/split behavior and want the latest API
  surface reflected in `docs/llamacloud/reference/`.
- A new LlamaCloud feature ships that you need agents to know about.

The commit message convention is `Refresh LlamaCloud docs mirror (<date>)`.
