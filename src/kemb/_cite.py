"""Cite — resolve a verbatim quote back to its source via a stemma manifest.

The other half of the provenance slice: ``kemb stemma`` writes the manifest,
``kemb cite`` reads it. Given a quote an agent emitted, return the source
document, page, character span, and bounding box (when present) it came from —
the "cite verbatim → source link" step, done locally with zero credits.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ._common import err
from ._stemma import resolve_quote


def add_subparser(subparsers):
    p = subparsers.add_parser(
        "cite",
        help="Resolve a verbatim quote to its source page via a stemma manifest.",
        description=(
            "Look up a verbatim quote in a stemma manifest (written by "
            "`kemb stemma`) and print where it came from: source, page, "
            "character span, and bounding box when available."
        ),
    )
    p.add_argument("quote", help="The verbatim text to locate.")
    p.add_argument("--manifest", type=Path, required=True,
                   help="Path to a <doc>.stemma.json manifest.")
    p.add_argument("--json", action="store_true",
                   help="Emit matches as JSON instead of a human-readable list.")
    p.set_defaults(func=run)
    return p


def _format_bbox(bbox) -> str:
    if not bbox:
        return ""
    return (f"  bbox x={bbox['x']:.0f} y={bbox['y']:.0f} "
            f"w={bbox['w']:.0f} h={bbox['h']:.0f}")


def run(args):
    if not args.manifest.exists():
        err(f"manifest not found: {args.manifest}")
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        err(f"could not read manifest {args.manifest}: {e}")

    matches = resolve_quote(args.quote, manifest)

    if args.json:
        print(json.dumps(matches, indent=2))
        return 0 if matches else 1

    if not matches:
        print("no source found for that quote.", file=sys.stderr)
        return 1

    for m in matches:
        loc = f"{m['source']} p.{m['page']}"
        span = f"chars {m['char_start']}-{m['char_end']}"
        print(f"{loc}  [{m['strand_id']}]  {span}{_format_bbox(m.get('bbox'))}")
    return 0
