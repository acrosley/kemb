"""Local text sampling for probe — no network, no credits.

Extracts the first N words from each document so an agent can weigh a large
multi-directory corpus (doc types, parse tiers, priorities) directly from one
text file, without uploading anything or running a per-file model pass.

Extractors are deliberately cheap and best-effort:
  - PDF        — pypdf, first few pages only (also yields a page count and
                 detects missing text layers, i.e. scans that need OCR)
  - DOCX/PPTX/XLSX/ODT/ODS/ODP — stdlib zipfile + tag stripping
  - TXT/MD/RST/CSV/TSV          — direct read of the head of the file
  - HTML/HTM/XML                — head of the file with tags stripped
  - everything else             — no local extraction; reported as such

A failed or empty extraction is a signal, not an error: "no-text" on a PDF
usually means a scan that needs an OCR-capable parse tier.
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path
from typing import List, Optional, TypedDict

# How much raw data to read from plain-text-ish files before word-capping.
# Keeps probe fast on multi-GB logs that happen to end in .txt.
_TEXT_READ_CAP = 262_144  # 256 KB

# Statuses an extraction can land in. "ok" and "no-text" are the interesting
# ones for triage; the rest explain why no sample text is present.
STATUS_OK = "ok"
STATUS_NO_TEXT = "no-text"
STATUS_UNSUPPORTED = "no-extractor"
STATUS_SKIPPED = "skipped-budget"
STATUS_ERROR = "error"

_TAG_RE = re.compile(r"<[^>]+>")
_SCRIPT_STYLE_RE = re.compile(
    r"<(script|style)\b[^>]*>.*?</\1>", re.IGNORECASE | re.DOTALL
)


class SampleResult(TypedDict):
    """Outcome of sampling one file."""

    status: str
    text: str
    words: int
    pages: Optional[int]
    detail: Optional[str]


def _result(status, text="", pages=None, detail=None) -> SampleResult:
    return {
        "status": status,
        "text": text,
        "words": len(text.split()) if text else 0,
        "pages": pages,
        "detail": detail,
    }


def _cap_words(text: str, max_words: int) -> str:
    """Normalize whitespace and keep the first ``max_words`` words."""
    words = text.split()
    return " ".join(words[:max_words])


def _strip_tags(markup: str) -> str:
    markup = _SCRIPT_STYLE_RE.sub(" ", markup)
    return _TAG_RE.sub(" ", markup)


# --------------------------------------------------------------------------- #
# Per-format extractors
# --------------------------------------------------------------------------- #


def _load_pypdf():
    """Import pypdf defensively.

    A broken transitive dependency (e.g. a system `cryptography` without its
    cffi backend) can make `import pypdf` raise something other than
    ImportError, so catch everything and degrade to a status string.
    """
    try:
        from pypdf import PdfReader  # type: ignore
        return PdfReader
    except Exception:
        return None


def _sample_pdf(path: Path, max_words: int, max_pages: int) -> SampleResult:
    PdfReader = _load_pypdf()
    if PdfReader is None:
        return _result(
            STATUS_ERROR,
            detail="pypdf unavailable — `pip install pypdf` to sample PDFs",
        )
    try:
        reader = PdfReader(str(path))
        if reader.is_encrypted:
            try:
                reader.decrypt("")  # PDFs with an owner password but no user password
            except Exception:
                return _result(STATUS_ERROR, detail="encrypted PDF")
        page_count = len(reader.pages)
        chunks: List[str] = []
        words_seen = 0
        for page in reader.pages[:max_pages]:
            try:
                text = page.extract_text() or ""
            except Exception:
                text = ""
            if text.strip():
                chunks.append(text)
                words_seen += len(text.split())
            if words_seen >= max_words:
                break
    except Exception as e:
        return _result(STATUS_ERROR, detail=f"{type(e).__name__}: {e}")

    text = _cap_words(" ".join(chunks), max_words)
    if not text:
        return _result(
            STATUS_NO_TEXT,
            pages=page_count,
            detail="no text layer — likely a scan; needs an OCR-capable parse tier",
        )
    return _result(STATUS_OK, text=text, pages=page_count)


# Office/OpenDocument files are zip archives; the members holding body text.
# pptx slides are matched by prefix since they're numbered.
_ZIP_TEXT_MEMBERS = {
    ".docx": ["word/document.xml"],
    ".xlsx": ["xl/sharedStrings.xml"],
    ".odt": ["content.xml"],
    ".ods": ["content.xml"],
    ".odp": ["content.xml"],
}
_PPTX_SLIDE_RE = re.compile(r"^ppt/slides/slide(\d+)\.xml$")


def _sample_zip_xml(path: Path, ext: str, max_words: int) -> SampleResult:
    try:
        with zipfile.ZipFile(path) as zf:
            if ext == ".pptx":
                slides = sorted(
                    (m for m in zf.namelist() if _PPTX_SLIDE_RE.match(m)),
                    key=lambda m: int(_PPTX_SLIDE_RE.match(m).group(1)),
                )
                members = slides[:5]
            else:
                members = [m for m in _ZIP_TEXT_MEMBERS[ext] if m in zf.namelist()]
            chunks = []
            words_seen = 0
            for member in members:
                xml = zf.read(member).decode("utf-8", errors="replace")
                chunk = _strip_tags(xml)
                chunks.append(chunk)
                words_seen += len(chunk.split())
                if words_seen >= max_words:
                    break
    except (zipfile.BadZipFile, KeyError, OSError) as e:
        return _result(STATUS_ERROR, detail=f"{type(e).__name__}: {e}")

    text = _cap_words(" ".join(chunks), max_words)
    if not text:
        return _result(STATUS_NO_TEXT, detail="document body is empty")
    return _result(STATUS_OK, text=text)


def _sample_plain_text(path: Path, max_words: int, *, strip_markup=False) -> SampleResult:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read(_TEXT_READ_CAP)
    except OSError as e:
        return _result(STATUS_ERROR, detail=f"{type(e).__name__}: {e}")
    if strip_markup:
        raw = _strip_tags(raw)
    text = _cap_words(raw, max_words)
    if not text:
        return _result(STATUS_NO_TEXT, detail="file is empty")
    return _result(STATUS_OK, text=text)


_PLAIN_TEXT_EXTENSIONS = frozenset({".txt", ".md", ".rst", ".csv", ".tsv"})
_MARKUP_EXTENSIONS = frozenset({".html", ".htm", ".xml"})


def sample_file(path, extension, *, max_words=120, pdf_pages=3) -> SampleResult:
    """Extract up to ``max_words`` words of text from one file, locally.

    Returns a SampleResult; never raises. ``pages`` is populated for PDFs
    only (page counts feed the corpus plan's pages-x-tier cost estimate).
    """
    path = Path(path)
    ext = (extension or "").lower()
    if ext == ".pdf":
        return _sample_pdf(path, max_words, pdf_pages)
    if ext == ".pptx" or ext in _ZIP_TEXT_MEMBERS:
        return _sample_zip_xml(path, ext, max_words)
    if ext in _PLAIN_TEXT_EXTENSIONS:
        return _sample_plain_text(path, max_words)
    if ext in _MARKUP_EXTENSIONS:
        return _sample_plain_text(path, max_words, strip_markup=True)
    return _result(
        STATUS_UNSUPPORTED,
        detail="no local text extractor for this format",
    )
