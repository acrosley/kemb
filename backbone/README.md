# doc-backbone

A layered, deterministic parsing backbone that turns a PDF corpus (medical records, expert testimony, CVs, fee schedules, exhibits, designations, etc.) into a living markdown mirror.

**PDFs are the source of truth; markdown is a pure projection.** Wipe `mirror/` and `cache/` at any time — both are regenerable from the PDFs plus the parse config.

## The seven layers

```
L0  Corpus index      walk PDF tree, sha256, register in corpus.db
L1  Triage            cheap probe per PDF: text vs scan, page count, form fields
L2  Classify          doc-type classifier (medical / CV / testimony / fee_schedule / ...)
L3  Extract (routed)  per-type extractor chain, all producing one CIR
L4  Score + arbitrate quality signals -> auto-escalate to next tier
L5  Render            CIR -> markdown, deterministic, hash-stamped frontmatter
L6  Sync              reconcile mirror/ against corpus.db; re-render only what changed
```

## What v0 implements vs. stubs

| Layer | v0 |
|-------|----|
| L0 corpus index | implemented (walk, hash, SQLite registry) |
| L1 triage | stub (`NotImplementedError`) |
| L2 classify | stub; everything is `doc_type = "unknown"` |
| L3 extract | one extractor: `native_pdf` via pypdf |
| L4 score | stub |
| L5 render | implemented (deterministic, hash-stamped) |
| L6 sync | partial: schema migrations + mirror reconcile during `ingest` |

The point of the v0 spine is to prove the architecture end-to-end: PDF in, markdown out, re-running is a no-op. The stubs exist so the layer boundaries are visible on disk — adding a classifier or OCR tier later is a known-shape change, not an architectural rewrite.

## The load-bearing abstraction: CIR

Every extractor — present and future — emits a `CIR` (Canonical Intermediate Representation) of typed blocks. The renderer never knows which extractor produced a CIR. Add a new extractor by implementing `Extractor.extract(path) -> CIR` and registering it in `config/doc_types.yaml`; nothing downstream changes.

```python
@dataclass(slots=True)
class Block:
    kind: BlockKind                  # heading / paragraph / list / table / figure / footnote / page_break
    page: int
    text: str | None = None
    level: int | None = None
    table: list[list[str]] | None = None
    bbox: tuple[float, float, float, float] | None = None
    confidence: float = 1.0
    source_extractor: str = ""

@dataclass(slots=True)
class CIR:
    source_hash: str
    source_path: str
    doc_type: str
    pages: int
    extractor: str
    extractor_version: str
    blocks: list[Block]
    metadata: dict
```

## Layout

```
backbone/
  corpus.db                 SQLite: documents, parses, mirror_state
  cache/<ab>/<cdef.../>     content-hashed cir.json + doc.md
  mirror/                   the living markdown, organized by doc_type
  config/doc_types.yaml     doc_type -> extractor chain
  src/doc_backbone/         the package
  tests/                    spine tests
```

## Running the v0 demo

```
pip install -e backbone[test]
backbone ingest path/to/some.pdf
backbone status
backbone render --all
```

`ingest` is idempotent: a second run on the same PDF is a no-op.
