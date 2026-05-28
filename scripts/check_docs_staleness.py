"""Detect when the upstream LlamaCloud docs have drifted from our local mirror.

Usage:
    python scripts/check_docs_staleness.py           # report + exit 1 on drift
    python scripts/check_docs_staleness.py --json    # machine-readable report
    python scripts/check_docs_staleness.py --quiet   # exit code only

The check re-fetches every URL recorded in `docs/llamacloud/_manifest.json`,
hashes the response, and classifies each result as:

  * unchanged      sha256 matches the manifest
  * modified       sha256 differs (content updated upstream)
  * gone           was a tracked page, now 404 upstream
  * resurrected    was in known_missing, now 200 upstream
  * added          present in sitemap, not in manifest (new upstream page)
  * removed        in manifest but no longer in sitemap

Any non-zero count of `modified | gone | resurrected | added | removed`
counts as drift and exits 1. The CI workflow files this as a GitHub issue
(see .github/workflows/docs-staleness.yml).
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import sys
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from docs_common import (
    DOCS_HOST,
    INCLUDED_PREFIXES,
    MANIFEST_PATH,
    filter_llamacloud,
    http_get,
    list_sitemap_urls,
    log,
    page_url_to_md_url,
    sha256_bytes,
)


@dataclasses.dataclass
class DriftReport:
    modified: list[str] = dataclasses.field(default_factory=list)  # rel_paths
    gone: list[str] = dataclasses.field(default_factory=list)
    resurrected: list[str] = dataclasses.field(default_factory=list)  # md urls
    added: list[str] = dataclasses.field(default_factory=list)  # page urls
    removed: list[str] = dataclasses.field(default_factory=list)  # md urls
    unchanged_count: int = 0
    errors: list[tuple[str, str]] = dataclasses.field(default_factory=list)

    @property
    def has_drift(self) -> bool:
        return bool(self.modified or self.gone or self.resurrected or self.added or self.removed)

    def summary(self) -> str:
        return (
            f"unchanged={self.unchanged_count} modified={len(self.modified)} "
            f"gone={len(self.gone)} resurrected={len(self.resurrected)} "
            f"added={len(self.added)} removed={len(self.removed)} "
            f"errors={len(self.errors)}"
        )


def hash_url(md_url: str) -> tuple[str, str | None, str | None]:
    """Return (md_url, sha256, error). exactly one of sha/error is None."""
    try:
        body = http_get(md_url)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return md_url, None, "404"
        return md_url, None, f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001
        return md_url, None, f"{type(exc).__name__}: {exc}"
    return md_url, sha256_bytes(body), None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit a JSON report on stdout.")
    parser.add_argument("--quiet", action="store_true", help="Suppress per-page output; report by exit code only.")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args(argv)

    if not MANIFEST_PATH.exists():
        log(f"No manifest at {MANIFEST_PATH}. Run scripts/fetch_docs.py first.")
        return 2

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    entries: dict[str, dict] = manifest.get("entries", {})
    known_missing: dict[str, str] = manifest.get("known_missing", {})

    # md_url -> manifest entry (for quick lookup against re-hashed pages)
    by_md_url = {e["url"]: (rel_path, e) for rel_path, e in entries.items()}

    # 1) Re-hash every tracked URL.
    report = DriftReport()
    targets = list(by_md_url.keys()) + list(known_missing.keys())
    if not args.quiet:
        log(f"Re-checking {len(targets)} tracked URLs ({len(entries)} live, {len(known_missing)} known-missing)...")

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(hash_url, u) for u in targets]
        done = 0
        for fut in as_completed(futures):
            md_url, new_sha, err = fut.result()
            done += 1
            if md_url in by_md_url:
                rel_path, entry = by_md_url[md_url]
                if err == "404":
                    report.gone.append(rel_path)
                elif err:
                    report.errors.append((md_url, err))
                elif new_sha != entry["sha256"]:
                    report.modified.append(rel_path)
                else:
                    report.unchanged_count += 1
            else:
                # Was in known_missing. Now check if it's back.
                if err == "404":
                    report.unchanged_count += 1
                elif err:
                    report.errors.append((md_url, err))
                else:
                    report.resurrected.append(md_url)
            if not args.quiet and done % 100 == 0:
                log(f"  [{done:>4}/{len(targets)}] checked")

    # 2) Compare manifest URLs vs current sitemap to detect added/removed.
    try:
        sitemap_urls = filter_llamacloud(list_sitemap_urls())
    except Exception as exc:  # noqa: BLE001
        log(f"WARN: could not fetch sitemap for add/remove check: {exc}")
        sitemap_urls = []

    sitemap_md_urls = {page_url_to_md_url(u) for u in sitemap_urls}
    tracked_md_urls = set(by_md_url.keys()) | set(known_missing.keys())

    for md_url in sorted(sitemap_md_urls - tracked_md_urls):
        report.added.append(md_url)
    for md_url in sorted(tracked_md_urls - sitemap_md_urls):
        report.removed.append(md_url)

    # 3) Report.
    if args.json:
        print(
            json.dumps(
                {
                    "summary": report.summary(),
                    "has_drift": report.has_drift,
                    "modified": report.modified,
                    "gone": report.gone,
                    "resurrected": report.resurrected,
                    "added": report.added,
                    "removed": report.removed,
                    "errors": report.errors,
                },
                indent=2,
            )
        )
    else:
        print(report.summary())
        for label, items in [
            ("MODIFIED", report.modified),
            ("GONE (was tracked, now 404)", report.gone),
            ("RESURRECTED (was 404, now back)", report.resurrected),
            ("ADDED (new upstream page)", report.added),
            ("REMOVED (no longer in sitemap)", report.removed),
        ]:
            if items:
                print(f"\n{label}:")
                for it in items:
                    print(f"  {it}")
        if report.errors:
            print("\nERRORS (treated as inconclusive, not drift):")
            for url, err in report.errors:
                print(f"  {url}: {err}")

    return 1 if report.has_drift else 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
