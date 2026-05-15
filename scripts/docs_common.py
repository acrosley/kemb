"""Shared helpers for the LlamaCloud docs mirror.

The mirror lives under `docs/llamacloud/` and tracks every page under
`/llamaparse/*` and `/reference/*` on developers.llamaindex.ai (LlamaCloud's
public docs host as of 2026-05). Each page is fetched as raw markdown via the
site's `<page>/index.md` source endpoint and stored at the mirrored path.

The companion `_manifest.json` is the source of truth for what is mirrored
and lets `check_docs_staleness.py` detect upstream drift by re-hashing.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs" / "llamacloud"
MANIFEST_PATH = DOCS_ROOT / "_manifest.json"

DOCS_HOST = "https://developers.llamaindex.ai"
SITEMAP_URL = f"{DOCS_HOST}/sitemap.xml"

# Top-level path prefixes that are part of LlamaCloud's docs (vs. the Python
# framework, the TS framework, LiteParse, etc.). Keep this list short and
# explicit — broadening it accidentally pulls in 1700+ unrelated pages.
INCLUDED_PREFIXES = ("/llamaparse/", "/reference/")

USER_AGENT = "llamaparse-plugin-docs-mirror/1.0 (+https://github.com/acrosley/llamaparse-plugin)"


@dataclass(frozen=True)
class DocEntry:
    """One mirrored page: where it lives upstream and on disk, with its hash."""

    url: str
    rel_path: str  # path under DOCS_ROOT (POSIX separators)
    sha256: str
    bytes: int
    fetched_at: str  # ISO-8601 UTC


def http_get(url: str, timeout: float = 30.0) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 - trusted host
        return resp.read()


def list_sitemap_urls() -> list[str]:
    body = http_get(SITEMAP_URL).decode("utf-8", errors="replace")
    return re.findall(r"<loc>([^<]+)</loc>", body)


def filter_llamacloud(urls: Iterable[str]) -> list[str]:
    keep: list[str] = []
    for u in urls:
        if not u.startswith(DOCS_HOST):
            continue
        path = u[len(DOCS_HOST):]
        if any(path.startswith(p) for p in INCLUDED_PREFIXES):
            keep.append(u)
    return sorted(set(keep))


def page_url_to_md_url(page_url: str) -> str:
    """Translate `https://.../llamaparse/parse/` to its raw markdown source URL."""
    if not page_url.endswith("/"):
        page_url += "/"
    return page_url + "index.md"


def page_url_to_rel_path(page_url: str) -> str:
    """Translate page URL to the mirror-relative path (POSIX separators)."""
    path = page_url[len(DOCS_HOST):].strip("/")
    # The site root (`/llamaparse/`) maps to `llamaparse/index.md`. Everything
    # else gets `<path>/index.md` to preserve directory structure.
    return f"{path}/index.md" if path else "index.md"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {"docs_host": DOCS_HOST, "entries": {}}
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def save_manifest(manifest: dict) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)
