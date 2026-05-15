"""Fetch every LlamaCloud doc page as markdown and (re)build the manifest.

Usage:
    python scripts/fetch_docs.py            # full refresh
    python scripts/fetch_docs.py --limit 5  # smoke-test a handful of pages
    python scripts/fetch_docs.py --dry-run  # list URLs only, write nothing

The fetcher hits `<page>/index.md` for every LlamaCloud URL in the sitemap,
writes the markdown to `docs/llamacloud/<mirrored-path>/index.md`, then
rewrites `_manifest.json` with one entry per page. Existing files are
overwritten so the mirror is always a clean reflection of upstream.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
import time
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from docs_common import (
    DOCS_ROOT,
    MANIFEST_PATH,
    DocEntry,
    filter_llamacloud,
    http_get,
    list_sitemap_urls,
    log,
    page_url_to_md_url,
    page_url_to_rel_path,
    save_manifest,
    sha256_bytes,
)


class FetchResult:
    """Outcome of fetching one page."""

    __slots__ = ("page_url", "md_url", "rel_path", "entry", "status", "error")

    def __init__(
        self,
        page_url: str,
        md_url: str,
        rel_path: str,
        entry: DocEntry | None,
        status: str,
        error: str | None,
    ) -> None:
        self.page_url = page_url
        self.md_url = md_url
        self.rel_path = rel_path
        self.entry = entry
        self.status = status  # "ok" | "missing" | "error"
        self.error = error


def fetch_one(page_url: str) -> FetchResult:
    md_url = page_url_to_md_url(page_url)
    rel_path = page_url_to_rel_path(page_url)
    try:
        body = http_get(md_url)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return FetchResult(page_url, md_url, rel_path, None, "missing", f"HTTP 404")
        return FetchResult(page_url, md_url, rel_path, None, "error", f"HTTP {exc.code}: {exc.reason}")
    except Exception as exc:  # noqa: BLE001 - network / DNS / TLS / etc.
        return FetchResult(page_url, md_url, rel_path, None, "error", f"{type(exc).__name__}: {exc}")

    entry = DocEntry(
        url=md_url,
        rel_path=rel_path,
        sha256=sha256_bytes(body),
        bytes=len(body),
        fetched_at=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
    )
    out_path = DOCS_ROOT / rel_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(body)
    return FetchResult(page_url, md_url, rel_path, entry, "ok", None)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=None, help="Fetch only the first N URLs (debugging).")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent fetches (default 8).")
    parser.add_argument("--dry-run", action="store_true", help="Print URLs that would be fetched, then exit.")
    args = parser.parse_args(argv)

    log(f"Listing sitemap at {len(list_sitemap_urls())} entries...")
    all_urls = list_sitemap_urls()
    page_urls = filter_llamacloud(all_urls)
    log(f"Filtered to {len(page_urls)} LlamaCloud pages.")

    if args.limit:
        page_urls = page_urls[: args.limit]
        log(f"--limit set, fetching {len(page_urls)} pages.")

    if args.dry_run:
        for u in page_urls:
            print(u)
        return 0

    entries: dict[str, dict] = {}
    missing: dict[str, str] = {}
    errors: list[tuple[str, str]] = []
    start = time.monotonic()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(fetch_one, u) for u in page_urls]
        done = 0
        for fut in as_completed(futures):
            res = fut.result()
            done += 1
            if res.status == "ok":
                assert res.entry is not None
                entries[res.entry.rel_path] = {
                    "url": res.entry.url,
                    "sha256": res.entry.sha256,
                    "bytes": res.entry.bytes,
                    "fetched_at": res.entry.fetched_at,
                }
                if done % 25 == 0 or done == len(page_urls):
                    log(f"  [{done:>4}/{len(page_urls)}] OK   {res.rel_path}")
            elif res.status == "missing":
                missing[res.md_url] = res.error or "HTTP 404"
                log(f"  [{done:>4}/{len(page_urls)}] 404  {res.md_url}")
            else:
                errors.append((res.page_url, res.error or "unknown error"))
                log(f"  [{done:>4}/{len(page_urls)}] FAIL {res.page_url}: {res.error}")

    elapsed = time.monotonic() - start
    log(
        f"Fetched {len(entries)} pages in {elapsed:.1f}s "
        f"({len(missing)} known-missing, {len(errors)} hard failures)."
    )

    manifest = {
        "docs_host": "https://developers.llamaindex.ai",
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "page_count": len(entries),
        "entries": entries,
        # URLs that 404'd at fetch time. The checker compares this set so a
        # page flipping between 200 and 404 still counts as drift.
        "known_missing": missing,
    }
    save_manifest(manifest)
    log(f"Wrote manifest: {MANIFEST_PATH}")

    if errors:
        log("\nHard failures (non-404):")
        for url, err in errors:
            log(f"  {url}\n    {err}")
        return 1
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
