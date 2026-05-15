"""Backbone CLI: `backbone ingest|render|status`."""
from __future__ import annotations

import sqlite3
from pathlib import Path

import click

from doc_backbone import __version__
from doc_backbone import corpus as corpus_mod
from doc_backbone import db as db_mod
from doc_backbone import render as render_mod
from doc_backbone import sync as sync_mod
from doc_backbone.classify import default_doc_type
from doc_backbone.extractors.registry import (
    chain_for,
    get_extractor,
    load_doc_types_config,
)

DEFAULT_BACKBONE_ROOT = Path(__file__).resolve().parents[3]


def _backbone_root(option: str | None) -> Path:
    return Path(option).resolve() if option else DEFAULT_BACKBONE_ROOT


def _config_path(root: Path) -> Path:
    return root / "config" / "doc_types.yaml"


def _db_path(root: Path) -> Path:
    return root / "corpus.db"


def _write_artifacts(
    backbone_root: Path,
    source_hash: str,
    doc_type: str,
    source_path: str,
    cir,
) -> tuple[Path, Path, Path]:
    cache = sync_mod.cache_dir(backbone_root, source_hash)
    cache.mkdir(parents=True, exist_ok=True)
    cir_path = cache / "cir.json"
    md_path = cache / "doc.md"
    cir_path.write_bytes(render_mod.cir_json_bytes(cir))
    md_path.write_text(render_mod.render(cir), encoding="utf-8")
    mirror = sync_mod.mirror_path(backbone_root, source_hash, doc_type, source_path)
    sync_mod.publish_to_mirror(md_path, mirror)
    return cir_path, md_path, mirror


def _already_parsed(conn: sqlite3.Connection, source_hash: str, extractor: str) -> bool:
    row = conn.execute(
        "SELECT cir_path, md_path FROM parses WHERE hash = ? AND extractor = ?",
        (source_hash, extractor),
    ).fetchone()
    if row is None:
        return False
    cir_p = Path(row["cir_path"])
    md_p = Path(row["md_path"]) if row["md_path"] else None
    return cir_p.exists() and md_p is not None and md_p.exists()


@click.group()
@click.version_option(__version__, prog_name="backbone")
def main() -> None:
    """doc-backbone: PDF corpus -> deterministic markdown mirror."""


@main.command()
@click.argument("source", type=click.Path(exists=True, path_type=Path))
@click.option("--root", "root_opt", type=click.Path(path_type=Path), default=None,
              help="Backbone root (defaults to the installed backbone/ dir).")
def ingest(source: Path, root_opt: Path | None) -> None:
    """Ingest a PDF or directory of PDFs: hash, extract, render, publish."""
    root = _backbone_root(str(root_opt) if root_opt else None)
    config = load_doc_types_config(_config_path(root))
    conn = db_mod.connect(_db_path(root))

    pdfs = list(corpus_mod.iter_pdfs(source))
    if not pdfs:
        click.echo("No PDFs found.")
        return

    new_count = skip_count = 0
    for pdf in pdfs:
        entry = corpus_mod.register(conn, pdf, source if source.is_dir() else source.parent)
        doc_type = default_doc_type()
        chain = chain_for(doc_type, config)

        for extractor_name in chain:
            if _already_parsed(conn, entry.hash, extractor_name):
                skip_count += 1
                click.echo(f"  skip   {entry.hash[:8]} via {extractor_name} (cached)")
                break
            extractor = get_extractor(extractor_name)
            cir = extractor.extract(pdf, source_hash=entry.hash, doc_type=doc_type)
            cir_path, md_path, mirror = _write_artifacts(
                root, entry.hash, doc_type, entry.path, cir
            )
            now = sync_mod.utcnow_iso()
            conn.execute(
                "INSERT OR REPLACE INTO parses "
                "(hash, extractor, extractor_version, cir_path, md_path, parsed_utc) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (entry.hash, extractor.name, extractor.version,
                 str(cir_path), str(md_path), now),
            )
            conn.execute(
                "INSERT OR REPLACE INTO mirror_state "
                "(hash, md_path, rendered_utc, cir_hash) VALUES (?, ?, ?, ?)",
                (entry.hash, str(mirror), now, render_mod.cir_content_hash(cir)),
            )
            conn.execute(
                "UPDATE documents SET pages = ?, doc_type = ? WHERE hash = ?",
                (cir.pages, doc_type, entry.hash),
            )
            conn.commit()
            new_count += 1
            click.echo(f"  parse  {entry.hash[:8]} via {extractor_name} -> {mirror.name}")
            break  # v0: only first extractor in chain runs

    click.echo(f"\nDone. parsed={new_count} cached={skip_count} total_pdfs={len(pdfs)}")


@main.command()
@click.option("--root", "root_opt", type=click.Path(path_type=Path), default=None)
@click.option("--all", "render_all", is_flag=True, help="Re-render every cached CIR.")
@click.argument("source_hash", required=False)
def render(root_opt: Path | None, render_all: bool, source_hash: str | None) -> None:
    """Re-render markdown from cached CIRs without re-extracting."""
    if not render_all and not source_hash:
        raise click.UsageError("provide --all or a source_hash")
    root = _backbone_root(str(root_opt) if root_opt else None)
    conn = db_mod.connect(_db_path(root))

    if render_all:
        rows = conn.execute("SELECT hash FROM mirror_state").fetchall()
        hashes = [r["hash"] for r in rows]
    else:
        hashes = [source_hash]

    import json
    from doc_backbone.cir import CIR
    rendered = 0
    for h in hashes:
        parse = conn.execute(
            "SELECT cir_path, md_path FROM parses WHERE hash = ? LIMIT 1", (h,)
        ).fetchone()
        if parse is None:
            click.echo(f"  miss   {h[:8]} (no parse)")
            continue
        cir = CIR.from_dict(json.loads(Path(parse["cir_path"]).read_text(encoding="utf-8")))
        Path(parse["md_path"]).write_text(render_mod.render(cir), encoding="utf-8")
        doc = conn.execute(
            "SELECT path, doc_type FROM documents WHERE hash = ?", (h,)
        ).fetchone()
        if doc is not None:
            mirror = sync_mod.mirror_path(root, h, doc["doc_type"] or "unknown", doc["path"])
            sync_mod.publish_to_mirror(Path(parse["md_path"]), mirror)
        rendered += 1
        click.echo(f"  render {h[:8]}")
    click.echo(f"\nRendered {rendered} document(s).")


@main.command()
@click.option("--root", "root_opt", type=click.Path(path_type=Path), default=None)
def status(root_opt: Path | None) -> None:
    """Summarize the corpus."""
    root = _backbone_root(str(root_opt) if root_opt else None)
    if not _db_path(root).exists():
        click.echo("No corpus.db yet. Run `backbone ingest <path>` first.")
        return
    conn = db_mod.connect(_db_path(root))
    total = conn.execute("SELECT COUNT(*) AS n FROM documents").fetchone()["n"]
    by_type = conn.execute(
        "SELECT COALESCE(doc_type, 'unclassified') AS t, COUNT(*) AS n "
        "FROM documents GROUP BY doc_type ORDER BY n DESC"
    ).fetchall()
    by_extractor = conn.execute(
        "SELECT extractor, COUNT(*) AS n FROM parses GROUP BY extractor ORDER BY n DESC"
    ).fetchall()
    click.echo(f"Backbone root : {root}")
    click.echo(f"Total docs    : {total}")
    click.echo("By doc_type   :")
    for r in by_type:
        click.echo(f"  {r['t']:<20} {r['n']}")
    click.echo("By extractor  :")
    for r in by_extractor:
        click.echo(f"  {r['extractor']:<20} {r['n']}")


if __name__ == "__main__":
    main()
