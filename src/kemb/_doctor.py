"""Doctor — preflight checks for a kemb install.

Reports Python and package versions, dependency availability, API key
presence, and a non-billable auth probe against LlamaCloud. Spends zero
credits — never uploads a document or starts a job.

Exit codes:
    0 — every required check passed (SDK missing is a warning, not a failure)
    1 — at least one required check failed
"""
from __future__ import annotations

import argparse
import os
import platform
import sys
from typing import Optional

from ._common import API_HOST

REQUIRED_PYTHON = (3, 9)

# Status tokens. Width is chosen so the bracketed label is 6 chars wide
# and the lines align in a terminal.
_OK = "[ ok ]"
_WARN = "[warn]"
_FAIL = "[fail]"
_SKIP = "[skip]"


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "doctor",
        help="Diagnose your kemb install (Python, deps, API key, reachability).",
        description=(
            "Run preflight checks against the local install: Python version, "
            "package version, `requests` and `llama-cloud` availability, "
            "LLAMA_CLOUD_API_KEY presence, and a non-billable HEAD probe to "
            "confirm the key authenticates against LlamaCloud."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  kemb doctor             # full check incl. one auth probe\n"
            "  kemb doctor --offline   # skip the network probe\n"
        ),
    )
    p.add_argument(
        "--offline",
        action="store_true",
        help="Skip the LlamaCloud reachability/auth probe.",
    )
    p.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Seconds to wait for the auth probe (default: 10).",
    )
    p.add_argument(
        "--auto-install",
        action="store_true",
        help="No-op for doctor; accepted so the bundled skill shim can pass "
             "--auto-install on every facet (the shim uses it to bootstrap "
             "kemb itself when relocated).",
    )
    p.set_defaults(func=run)
    return p


# --------------------------------------------------------------------------- #
# Individual checks. Each returns (status_token, headline, detail_or_None).
# The orchestrator below prints them and decides the exit code.
# --------------------------------------------------------------------------- #


def check_python_version() -> tuple[str, str, Optional[str]]:
    major, minor = sys.version_info[:2]
    label = f"Python {platform.python_version()} ({platform.system()} {platform.machine()})"
    if (major, minor) < REQUIRED_PYTHON:
        return _FAIL, label, f"requires Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}+"
    return _OK, label, None


def check_package_version() -> tuple[str, str, Optional[str]]:
    try:
        from importlib.metadata import PackageNotFoundError, version

        v = version("kemb")
        return _OK, f"kemb {v}", None
    except PackageNotFoundError:
        return (
            _WARN,
            "kemb (version unknown)",
            "package metadata missing — running from a source tree?",
        )
    except Exception as e:
        return _WARN, "kemb (version unknown)", repr(e)


def check_requests() -> tuple[str, str, Optional[str]]:
    try:
        import requests  # noqa: F401

        return _OK, f"requests {requests.__version__}", None
    except ImportError as e:
        return _FAIL, "requests not importable", str(e)


def check_sdk() -> tuple[str, str, Optional[str]]:
    """`llama-cloud` is preferred but not required — REST fallback covers it."""
    try:
        import llama_cloud  # noqa: F401

        # Some SDK builds omit __version__; that's not a real problem.
        v = getattr(llama_cloud, "__version__", "version unknown")
        return _OK, f"llama-cloud SDK ({v})", None
    except ImportError:
        return (
            _WARN,
            "llama-cloud SDK not installed",
            "REST fallback still works; `pip install llama-cloud` for the SDK path",
        )


def check_api_key() -> tuple[str, str, Optional[str]]:
    key = os.environ.get("LLAMA_CLOUD_API_KEY")
    if not key:
        return (
            _FAIL,
            "LLAMA_CLOUD_API_KEY not set",
            "get a key at https://cloud.llamaindex.ai/api-key and export it",
        )
    return _OK, f"LLAMA_CLOUD_API_KEY set ({mask_key(key)})", None


def check_api_reachable(timeout: float) -> tuple[str, str, Optional[str]]:
    """Probe LlamaCloud with the user's key. Spends no credits.

    Uses a HEAD against the upload endpoint:
      - 2xx / 405 / 404 / most 4xx → auth header was accepted; key works
      - 401                        → key was rejected
      - 403                        → forbidden (host allowlist? plan tier?)
      - connection / timeout error → network unreachable
    """
    key = os.environ.get("LLAMA_CLOUD_API_KEY")
    if not key:
        return _SKIP, "auth probe skipped", "no API key in env"

    try:
        import requests
    except ImportError as e:
        return _SKIP, "auth probe skipped", f"requests not importable: {e}"

    url = f"{API_HOST}/api/v1/beta/files"
    try:
        resp = requests.head(
            url,
            headers={"Authorization": f"Bearer {key}"},
            timeout=timeout,
            allow_redirects=False,
        )
    except requests.exceptions.ConnectTimeout:
        return _FAIL, f"could not reach {API_HOST}", f"connect timeout after {timeout:.0f}s"
    except requests.exceptions.ReadTimeout:
        return _FAIL, f"could not reach {API_HOST}", f"read timeout after {timeout:.0f}s"
    except requests.exceptions.ConnectionError as e:
        return _FAIL, f"could not reach {API_HOST}", f"connection error: {e}"
    except Exception as e:
        return _FAIL, f"auth probe errored", f"{type(e).__name__}: {e}"

    code = resp.status_code
    if code == 401:
        return _FAIL, f"API key rejected ({code} from {API_HOST})", "rotate the key or fix typos"
    if code == 403:
        return (
            _FAIL,
            f"forbidden ({code} from {API_HOST})",
            "key authenticated but lacks permission — check plan tier, project scope, "
            "or (Cowork) the network allowlist for api.cloud.llamaindex.ai",
        )
    # Everything else: we got past auth (2xx, 404, 405, even 5xx).
    # Use ASCII-only "->" so the line prints on Windows cp1252 consoles too.
    return _OK, f"LlamaCloud reachable (HEAD {url} -> {code})", None


# --------------------------------------------------------------------------- #
# Output / orchestration
# --------------------------------------------------------------------------- #


def mask_key(key: str) -> str:
    """Render a key as `llx-...XXXX` so it's safe to print."""
    key = key.strip()
    if len(key) <= 4:
        return "****"
    return f"{key[:4]}...{key[-4:]}"


def _print_line(status: str, headline: str, detail: Optional[str]) -> None:
    print(f"  {status}  {headline}")
    if detail:
        print(f"         {detail}")


def run(args) -> int:
    print("kemb doctor")
    print("-----------------")

    results: list[tuple[str, str, Optional[str]]] = [
        check_python_version(),
        check_package_version(),
        check_requests(),
        check_sdk(),
        check_api_key(),
    ]
    if args.offline:
        results.append((_SKIP, "auth probe skipped", "--offline passed"))
    else:
        results.append(check_api_reachable(args.timeout))

    for status, headline, detail in results:
        _print_line(status, headline, detail)

    print()
    failed = sum(1 for s, _, _ in results if s == _FAIL)
    warned = sum(1 for s, _, _ in results if s == _WARN)
    if failed:
        print(f"{failed} check(s) failed, {warned} warning(s). See messages above.")
        return 1
    if warned:
        print(f"all required checks passed ({warned} warning(s)).")
    else:
        print("all checks passed.")
    return 0
