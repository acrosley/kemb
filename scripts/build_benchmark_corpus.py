#!/usr/bin/env python3
"""Build a knowledge-work benchmark corpus for kemb.

Assembles a directory of documents spanning every format kemb's probe
recognizes — with deliberate variety inside the PDF bucket (text layers,
scans, tables, two-column layouts, encryption, corruption) — so `kemb probe`,
`kemb parse`, and `kemb classify` can be exercised against one predictable
tree. Content is themed after the routing categories in
``examples/rules/document_routing.json`` (contract, invoice, receipt,
correspondence, other) so the same corpus benchmarks classification.

Every file is synthesized locally and deterministically; no network is
required. When the network *is* open, a handful of well-known real-world
documents (an arXiv paper, an IRS fillable form, a Project Gutenberg EPUB…)
are downloaded on top, because hand-rolled fixtures can't reproduce
real-world layout complexity. Downloads that fail are skipped with a note —
the synthesized corpus is complete on its own.

Layout::

    <dest>/
      manifest.json        per-file category, description, sha256, and the
                           sample status `kemb probe --sample` should report
      corpus/
        pdf/               eleven PDF variants + optional real-world PDFs
        office/            docx / xlsx / pptx
        opendocument/      odt / ods / odp
        text/              txt / md / rst
        data/              csv / tsv
        markup/            html / htm / xml
        ebooks_richtext/   epub / rtf
        images/            png / jpg / gif / bmp / tiff (OCR-route formats)
        edge_cases/        empty, truncated, mislabeled, corrupt, hidden,
                           unsupported-extension, deep-nesting, unicode names

Usage::

    python scripts/build_benchmark_corpus.py                  # build ./kemb_benchmark_corpus
    python scripts/build_benchmark_corpus.py --dest /tmp/c    # custom destination
    python scripts/build_benchmark_corpus.py --offline        # skip downloads
    python scripts/build_benchmark_corpus.py --verify         # build, then run
                                                              # kemb probe --sample over the
                                                              # corpus and check every file's
                                                              # status against the manifest

Dependencies: stdlib + pypdf (already a kemb dependency). Pillow is optional —
when importable, image fixtures are rendered with real text (useful OCR
fodder); otherwise minimal hand-rolled images are written and jpg is skipped.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import shutil
import struct
import sys
import time
import urllib.error
import urllib.request
import zipfile
import zlib
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path

MANIFEST_SCHEMA_VERSION = 1
DEFAULT_DEST = "kemb_benchmark_corpus"
DOWNLOAD_TIMEOUT = 30

# Statuses kemb's sampler can report (mirrors src/kemb/_sample.py).
OK = "ok"
NO_TEXT = "no-text"
NO_EXTRACTOR = "no-extractor"
ERROR = "error"

# --------------------------------------------------------------------------- #
# Deterministic knowledge-work prose
# --------------------------------------------------------------------------- #

CONTRACT_CLAUSES = [
    "This Master Services Agreement is entered into by Meridian Analytics LLC "
    "and Cobalt Harbor Logistics Inc., effective as of the date of last signature.",
    "The Service Provider shall deliver the work described in each Statement of "
    "Work with reasonable skill and care, consistent with industry standards.",
    "Either party may terminate for material breach upon thirty days written "
    "notice if the breach remains uncured at the end of the notice period.",
    "All intellectual property created under a Statement of Work vests in the "
    "Client upon payment in full of the associated fees.",
    "Neither party shall be liable for indirect or consequential damages, and "
    "aggregate liability is capped at fees paid in the twelve months preceding "
    "the claim.",
    "Confidential information shall be protected with no less than the degree "
    "of care the receiving party applies to its own confidential material.",
    "This Agreement is governed by the laws of the State of Delaware, without "
    "regard to its conflict of laws principles.",
]

REPORT_PARAGRAPHS = [
    "Revenue for the quarter rose eleven percent year over year, driven by "
    "renewals in the enterprise segment and early traction in the new "
    "logistics vertical.",
    "Gross margin expanded ninety basis points as the platform migration "
    "completed and duplicate infrastructure was decommissioned ahead of "
    "schedule.",
    "Headcount grew by fourteen, concentrated in customer engineering and "
    "compliance, while attrition remained below the industry benchmark.",
    "The risk committee flagged vendor concentration in payment processing "
    "and recommended qualifying a second provider before the holiday peak.",
    "Operating cash flow remains positive for a sixth consecutive quarter, "
    "and the board approved continued investment in the document automation "
    "initiative.",
    "Customer satisfaction scores held steady at ninety two, with onboarding "
    "time falling from nine days to six after the playbook revision.",
]

CORRESPONDENCE_BODY = """From: Dana Whitfield <dana.whitfield@meridian-analytics.example>
To: Procurement Team <procurement@cobaltharbor.example>
Date: Tue, 14 Apr 2026 09:12:00 -0500
Subject: Re: Renewal terms and the outstanding invoice queue

Team,

Thanks for the call yesterday. Summarizing where we landed so nothing is
lost before the renewal deadline:

1. The renewal term moves to twenty four months with a four percent uplift.
2. Invoices 2031 through 2034 are approved and enter the payment run Friday.
3. Legal returns the redlined data processing addendum by end of week.

I have attached the revised order form. Please countersign by April 21 so
provisioning is not blocked.

Best,
Dana
"""

INVOICE_ROWS = [
    ("2031", "Document parsing platform, annual license", 1, 48000.00),
    ("2031-a", "OCR add-on, agentic tier, 250k pages", 1, 9500.00),
    ("2032", "Implementation services, March", 86, 210.00),
    ("2033", "Premium support, Q2", 1, 6000.00),
    ("2034", "Training workshop, two day on-site", 2, 3400.00),
]


def _paragraphs(pool, count, start=0):
    return [pool[(start + i) % len(pool)] for i in range(count)]


# --------------------------------------------------------------------------- #
# PDF builders (pypdf — already a kemb dependency)
# --------------------------------------------------------------------------- #


def _pdf_escape(text: str) -> bytes:
    out = text.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")
    return out.encode("latin-1", "replace")


def _add_pdf_page(writer, content: bytes, fonts=None):
    """Add one US-Letter page with a raw content stream and Type1 fonts."""
    from pypdf.generic import (
        ArrayObject,
        DictionaryObject,
        NameObject,
        StreamObject,
    )

    fonts = fonts or {"F1": "Helvetica"}
    page = writer.add_blank_page(width=612, height=792)
    stream = StreamObject()
    stream.set_data(content)
    page[NameObject("/Contents")] = writer._add_object(stream)
    font_dir = DictionaryObject()
    for res_name, base_font in fonts.items():
        font = DictionaryObject({
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject(f"/{base_font}"),
        })
        font_dir[NameObject(f"/{res_name}")] = writer._add_object(font)
    page[NameObject("/Resources")] = DictionaryObject({
        NameObject("/Font"): font_dir,
        NameObject("/ProcSet"): ArrayObject(
            [NameObject("/PDF"), NameObject("/Text")]
        ),
    })
    return page


def _text_page_stream(lines, *, x=72, y=740, size=11, leading=14, font="F1"):
    parts = [b"BT", f"/{font} {size} Tf".encode(), f"{leading} TL".encode(),
             f"{x} {y} Td".encode()]
    for line in lines:
        parts.append(b"(" + _pdf_escape(line) + b") Tj T*")
    parts.append(b"ET")
    return b"\n".join(parts)


def _wrap(text: str, width=88):
    import textwrap

    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=width) or [""])
    return lines


def make_text_pdf(path: Path, pages_of_lines):
    from pypdf import PdfWriter

    writer = PdfWriter()
    for lines in pages_of_lines:
        _add_pdf_page(writer, _text_page_stream(lines))
    with open(path, "wb") as fh:
        writer.write(fh)


def build_contract_pdf(path: Path):
    lines = ["MASTER SERVICES AGREEMENT", ""]
    for i, clause in enumerate(CONTRACT_CLAUSES, 1):
        lines.extend(_wrap(f"{i}. {clause}"))
        lines.append("")
    lines.extend(["Signed:", "Meridian Analytics LLC          Cobalt Harbor Logistics Inc."])
    make_text_pdf(path, [lines])


def build_multipage_report_pdf(path: Path, pages=12):
    pages_of_lines = []
    for p in range(pages):
        lines = [f"QUARTERLY OPERATIONS REPORT — page {p + 1} of {pages}", ""]
        for para in _paragraphs(REPORT_PARAGRAPHS, 4, start=p):
            lines.extend(_wrap(para))
            lines.append("")
        pages_of_lines.append(lines)
    make_text_pdf(path, pages_of_lines)


def build_long_pdf(path: Path, pages=60):
    """Page-count stressor for probe's per-PDF page counting and parse cost
    estimation; sampling still only opens the first few pages."""
    pages_of_lines = []
    for p in range(pages):
        lines = [f"ANNUAL FILING — section {p + 1}", ""]
        for para in _paragraphs(REPORT_PARAGRAPHS + CONTRACT_CLAUSES, 3, start=p * 2):
            lines.extend(_wrap(para))
            lines.append("")
        pages_of_lines.append(lines)
    make_text_pdf(path, pages_of_lines)


def build_invoice_table_pdf(path: Path):
    """Fixed-width Courier table — exercises tabular text extraction."""
    from pypdf import PdfWriter

    rows = [f"{'INV':<8}{'DESCRIPTION':<46}{'QTY':>5}{'UNIT':>12}{'TOTAL':>12}"]
    rows.append("-" * 83)
    total = 0.0
    for inv, desc, qty, unit in INVOICE_ROWS:
        amount = qty * unit
        total += amount
        rows.append(f"{inv:<8}{desc:<46}{qty:>5}{unit:>12,.2f}{amount:>12,.2f}")
    rows.append("-" * 83)
    rows.append(f"{'':<59}{'AMOUNT DUE':>12}{total:>12,.2f}")
    lines = ["INVOICE  2031-CONSOLIDATED", "Bill to: Cobalt Harbor Logistics Inc.",
             "Terms: net 30", ""] + rows
    writer = PdfWriter()
    _add_pdf_page(
        writer,
        _text_page_stream(lines, size=8, leading=11, font="F2"),
        fonts={"F2": "Courier"},
    )
    with open(path, "wb") as fh:
        writer.write(fh)


def build_two_column_pdf(path: Path):
    """Academic-style two-column layout — column-order extraction stressor."""
    from pypdf import PdfWriter

    left = _wrap(" ".join(_paragraphs(REPORT_PARAGRAPHS, 3)), width=42)
    right = _wrap(" ".join(_paragraphs(REPORT_PARAGRAPHS, 3, start=3)), width=42)
    title = _text_page_stream(
        ["Document Triage at Corpus Scale: a Working Note", ""],
        x=72, y=750, size=13,
    )
    col_l = _text_page_stream(left, x=72, y=710, size=9, leading=12)
    col_r = _text_page_stream(right, x=320, y=710, size=9, leading=12)
    writer = PdfWriter()
    _add_pdf_page(writer, title + b"\n" + col_l + b"\n" + col_r)
    with open(path, "wb") as fh:
        writer.write(fh)


def build_accented_pdf(path: Path):
    lines = [
        "RÉSUMÉ DE LA RÉUNION — São Paulo büro",
        "",
        "Señora Ibáñez confirmed the naïve façade estimate was outdated;",
        "the revised cost is 12 400 € (déjà approved by the Zürich office).",
    ]
    make_text_pdf(path, [lines])


def build_blank_scan_pdf(path: Path, pages=3):
    """No text layer at all — probe should flag it as a scan (no-text)."""
    from pypdf import PdfWriter

    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=612, height=792)
    with open(path, "wb") as fh:
        writer.write(fh)


def build_image_only_pdf(path: Path):
    """A page whose only content is a raster image — the realistic scan case."""
    from pypdf import PdfWriter
    from pypdf.generic import (
        ArrayObject,
        DictionaryObject,
        NameObject,
        NumberObject,
        StreamObject,
    )

    width, height = 132, 96
    pixels = bytearray()
    for y in range(height):
        for x in range(width):
            pixels += bytes((
                (x * 2) % 256,
                (y * 2) % 256,
                ((x + y) * 2) % 256,
            ))
    writer = PdfWriter()
    page = writer.add_blank_page(width=612, height=792)
    image = StreamObject()
    image.set_data(bytes(pixels))
    image[NameObject("/Type")] = NameObject("/XObject")
    image[NameObject("/Subtype")] = NameObject("/Image")
    image[NameObject("/Width")] = NumberObject(width)
    image[NameObject("/Height")] = NumberObject(height)
    image[NameObject("/ColorSpace")] = NameObject("/DeviceRGB")
    image[NameObject("/BitsPerComponent")] = NumberObject(8)
    image_ref = writer._add_object(image)
    content = StreamObject()
    content.set_data(b"q 396 0 0 288 108 360 cm /Im0 Do Q")
    page[NameObject("/Contents")] = writer._add_object(content)
    page[NameObject("/Resources")] = DictionaryObject({
        NameObject("/XObject"): DictionaryObject({NameObject("/Im0"): image_ref}),
        NameObject("/ProcSet"): ArrayObject(
            [NameObject("/PDF"), NameObject("/ImageC")]
        ),
    })
    with open(path, "wb") as fh:
        writer.write(fh)


def encrypt_pdf(src: Path, dst: Path, *, user_password="", owner_password=None):
    """RC4-128 keeps this pure-python — no crypto extras needed to build or
    detect it (mirrors tests/test_sample.py)."""
    from pypdf import PdfWriter

    writer = PdfWriter(clone_from=str(src))
    writer.encrypt(
        user_password=user_password,
        owner_password=owner_password,
        algorithm="RC4-128",
    )
    with open(dst, "wb") as fh:
        writer.write(fh)


def build_sealed_pdf(path: Path, scratch: Path):
    plain = scratch / "_sealed_src.pdf"
    make_text_pdf(plain, [["SEALED SETTLEMENT TERMS — password required"]])
    encrypt_pdf(plain, path, user_password="hunter2")
    plain.unlink()


def build_restricted_pdf(path: Path, scratch: Path):
    plain = scratch / "_restricted_src.pdf"
    make_text_pdf(plain, [[
        "BOARD MINUTES — distribution restricted, reading permitted",
    ]])
    encrypt_pdf(plain, path, owner_password="s3cret")
    plain.unlink()


def build_truncated_pdf(path: Path, scratch: Path):
    plain = scratch / "_truncated_src.pdf"
    build_multipage_report_pdf(plain, pages=4)
    data = plain.read_bytes()
    path.write_bytes(data[: len(data) * 2 // 5])  # cut before the xref table
    plain.unlink()


# --------------------------------------------------------------------------- #
# Office / OpenDocument builders (stdlib zipfile)
# --------------------------------------------------------------------------- #

_OOXML_CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>{overrides}</Types>'
)


def _ooxml_zip(path: Path, members, main_override):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(
            "[Content_Types].xml",
            _OOXML_CONTENT_TYPES.format(overrides=main_override),
        )
        for name, payload in members.items():
            zf.writestr(name, payload)


def build_docx(path: Path):
    paragraphs = ["MEETING MINUTES — vendor review, April 14"] + _paragraphs(
        REPORT_PARAGRAPHS, 4
    )
    body = "".join(
        f"<w:p><w:r><w:t>{p}</w:t></w:r></w:p>" for p in paragraphs
    )
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{body}</w:body></w:document>"
    )
    _ooxml_zip(
        path,
        {"word/document.xml": document},
        '<Override PartName="/word/document.xml" ContentType='
        '"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>',
    )


def build_xlsx(path: Path):
    strings = ["Line item", "Quarter", "Amount"] + [
        desc for _, desc, _, _ in INVOICE_ROWS
    ]
    shared = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        f'count="{len(strings)}" uniqueCount="{len(strings)}">'
        + "".join(f"<si><t>{s}</t></si>" for s in strings)
        + "</sst>"
    )
    rows = "".join(
        f'<row r="{i + 1}"><c r="A{i + 1}" t="s"><v>{i}</v></c></row>'
        for i in range(len(strings))
    )
    sheet = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f"<sheetData>{rows}</sheetData></worksheet>"
    )
    workbook = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<sheets><sheet name="Budget" sheetId="1" r:id="rId1" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>'
        "</sheets></workbook>"
    )
    _ooxml_zip(
        path,
        {
            "xl/workbook.xml": workbook,
            "xl/sharedStrings.xml": shared,
            "xl/worksheets/sheet1.xml": sheet,
        },
        '<Override PartName="/xl/workbook.xml" ContentType='
        '"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
    )


def build_pptx(path: Path):
    titles = [
        "Document automation: pitch deck",
        "Problem: forty thousand unsorted files per quarter",
        "Approach: probe, plan, then comb the corpus",
    ]
    members = {}
    for i, (title, para) in enumerate(
        zip(titles, _paragraphs(REPORT_PARAGRAPHS, len(titles))), start=1
    ):
        members[f"ppt/slides/slide{i}.xml"] = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
            "<p:cSld><p:spTree>"
            f"<p:sp><p:txBody><a:p><a:r><a:t>{title}</a:t></a:r></a:p>"
            f"<a:p><a:r><a:t>{para}</a:t></a:r></a:p></p:txBody></p:sp>"
            "</p:spTree></p:cSld></p:sld>"
        )
    _ooxml_zip(
        path,
        members,
        '<Override PartName="/ppt/slides/slide1.xml" ContentType='
        '"application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>',
    )


_ODF_MIMETYPES = {
    ".odt": "application/vnd.oasis.opendocument.text",
    ".ods": "application/vnd.oasis.opendocument.spreadsheet",
    ".odp": "application/vnd.oasis.opendocument.presentation",
}


def build_odf(path: Path, paragraphs):
    body = "".join(f"<text:p>{p}</text:p>" for p in paragraphs)
    content = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<office:document-content '
        'xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" '
        'xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0">'
        f"<office:body>{body}</office:body></office:document-content>"
    )
    with zipfile.ZipFile(path, "w") as zf:
        info = zipfile.ZipInfo("mimetype")
        zf.writestr(info, _ODF_MIMETYPES[path.suffix], zipfile.ZIP_STORED)
        zf.writestr("content.xml", content)


# --------------------------------------------------------------------------- #
# EPUB / RTF builders
# --------------------------------------------------------------------------- #


def build_epub(path: Path):
    chapter = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<html xmlns="http://www.w3.org/1999/xhtml"><head>'
        "<title>Employee Handbook</title></head><body>"
        "<h1>Employee Handbook</h1>"
        + "".join(f"<p>{p}</p>" for p in _paragraphs(REPORT_PARAGRAPHS, 4))
        + "</body></html>"
    )
    opf = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
        'unique-identifier="uid">'
        '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
        '<dc:identifier id="uid">urn:uuid:kemb-benchmark-handbook</dc:identifier>'
        "<dc:title>Employee Handbook</dc:title><dc:language>en</dc:language>"
        '<meta property="dcterms:modified">2026-01-01T00:00:00Z</meta>'
        "</metadata><manifest>"
        '<item id="ch1" href="chapter1.xhtml" media-type="application/xhtml+xml"/>'
        '</manifest><spine><itemref idref="ch1"/></spine></package>'
    )
    container = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<container version="1.0" '
        'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
        '<rootfiles><rootfile full-path="OEBPS/content.opf" '
        'media-type="application/oebps-package+xml"/></rootfiles></container>'
    )
    with zipfile.ZipFile(path, "w") as zf:
        info = zipfile.ZipInfo("mimetype")
        zf.writestr(info, "application/epub+zip", zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", container)
        zf.writestr("OEBPS/content.opf", opf)
        zf.writestr("OEBPS/chapter1.xhtml", chapter)


def build_rtf(path: Path):
    body = r"\par ".join(_paragraphs(CONTRACT_CLAUSES, 3))
    path.write_text(
        r"{\rtf1\ansi\deff0 {\fonttbl{\f0 Times New Roman;}}"
        r"\f0\fs22 LEGACY MEMO — retention schedule\par " + body + "}",
        encoding="ascii",
        errors="replace",
    )


# --------------------------------------------------------------------------- #
# Image builders — Pillow-rendered text when available, hand-rolled minimal
# files otherwise (locally these only exercise inventory/routing; real OCR
# happens server-side in `kemb parse`)
# --------------------------------------------------------------------------- #


def _load_pillow():
    try:
        from PIL import Image, ImageDraw  # type: ignore

        return Image, ImageDraw
    except Exception:
        return None, None


def _pillow_text_image(text):
    Image, ImageDraw = _load_pillow()
    img = Image.new("RGB", (640, 200), "white")
    draw = ImageDraw.Draw(img)
    for i, line in enumerate(text.split("\n")):
        draw.text((16, 16 + 24 * i), line, fill="black")
    return img


def _png_chunk(tag: bytes, payload: bytes) -> bytes:
    return (
        struct.pack(">I", len(payload))
        + tag
        + payload
        + struct.pack(">I", zlib.crc32(tag + payload) & 0xFFFFFFFF)
    )


def build_png(path: Path):
    Image, _ = _load_pillow()
    if Image:
        _pillow_text_image(
            "RECEIPT — Harbor Cafe\nespresso 3.50\nsandwich 9.25\nTOTAL 12.75"
        ).save(path, "PNG")
        return
    width = height = 32
    raw = b"".join(
        b"\x00" + bytes(((x * 8) % 256, (y * 8) % 256, 128) for x in range(width))
        for y in range(height)
    )
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + _png_chunk(b"IHDR", ihdr)
        + _png_chunk(b"IDAT", zlib.compress(raw))
        + _png_chunk(b"IEND", b"")
    )


def build_jpg(path: Path) -> bool:
    """Returns False (entry skipped) when Pillow is unavailable — baseline
    JPEG can't be hand-rolled with the stdlib."""
    Image, _ = _load_pillow()
    if not Image:
        return False
    _pillow_text_image(
        "WHITEBOARD — Q3 planning\nprobe -> plan -> comb\nship manifest by Friday"
    ).save(path, "JPEG", quality=80)
    return True


def build_gif(path: Path):
    Image, _ = _load_pillow()
    if Image:
        _pillow_text_image("FLOW DIAGRAM\ninbox -> triage -> parsed mirror").save(
            path, "GIF"
        )
        return
    # canonical minimal 1x1 GIF89a
    path.write_bytes(
        b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff"
        b"\x21\xf9\x04\x01\x00\x00\x00\x00"
        b"\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b"
    )


def build_bmp(path: Path):
    Image, _ = _load_pillow()
    if Image:
        _pillow_text_image("FAX COVER PAGE\nto: records dept\npages: 3").save(
            path, "BMP"
        )
        return
    width, height = 8, 8
    row = bytes(b for x in range(width) for b in (x * 30 % 256, 80, 160))
    padding = b"\x00" * ((4 - len(row) % 4) % 4)
    pixels = (row + padding) * height
    header = struct.pack(
        "<2sIHHI", b"BM", 14 + 40 + len(pixels), 0, 0, 14 + 40
    ) + struct.pack("<IiiHHIIiiII", 40, width, height, 1, 24, 0, len(pixels), 2835, 2835, 0, 0)
    path.write_bytes(header + pixels)


def build_tiff(path: Path):
    Image, _ = _load_pillow()
    if Image:
        _pillow_text_image("BLUEPRINT SCAN\nfloor 2 — east wing").save(path, "TIFF")
        return
    width = height = 16
    pixels = bytes((x * y) % 256 for y in range(height) for x in range(width))
    # little-endian TIFF: header, one strip of 8-bit grayscale, then the IFD
    pixel_offset = 8
    ifd_offset = pixel_offset + len(pixels)
    entries = [
        (256, 3, 1, width),         # ImageWidth
        (257, 3, 1, height),        # ImageLength
        (258, 3, 1, 8),             # BitsPerSample
        (259, 3, 1, 1),             # Compression: none
        (262, 3, 1, 1),             # Photometric: BlackIsZero
        (273, 4, 1, pixel_offset),  # StripOffsets
        (278, 3, 1, height),        # RowsPerStrip
        (279, 4, 1, len(pixels)),   # StripByteCounts
    ]
    ifd = struct.pack("<H", len(entries))
    for tag, typ, count, value in entries:
        ifd += struct.pack("<HHII", tag, typ, count, value)
    ifd += struct.pack("<I", 0)
    path.write_bytes(
        struct.pack("<2sHI", b"II", 42, ifd_offset) + pixels + ifd
    )


# --------------------------------------------------------------------------- #
# Plain text / markup / data builders
# --------------------------------------------------------------------------- #


def build_txt(path: Path):
    path.write_text(CORRESPONDENCE_BODY, encoding="utf-8")


def build_md(path: Path):
    paras = _paragraphs(REPORT_PARAGRAPHS, 2)
    path.write_text(
        "# Incident runbook: parse queue backlog\n\n"
        "## Symptoms\n\n"
        f"{paras[0]}\n\n"
        "## Mitigation\n\n"
        "1. Pause the intake webhook.\n"
        "2. Re-run `kemb probe ./inbox --sample` and triage scans separately.\n"
        "3. Resume with the cost_effective tier for text-layer PDFs.\n\n"
        "```bash\nkemb parse ./inbox/contract.pdf --tier cost_effective\n```\n\n"
        f"## Postmortem notes\n\n{paras[1]}\n",
        encoding="utf-8",
    )


def build_rst(path: Path):
    path.write_text(
        "Document pipeline architecture\n"
        "==============================\n\n"
        "Overview\n--------\n\n"
        + _paragraphs(REPORT_PARAGRAPHS, 1, start=2)[0]
        + "\n\n.. note:: probe is local-only and spends no credits.\n",
        encoding="utf-8",
    )


def build_csv(path: Path):
    lines = ["invoice,description,quantity,unit_price,total"]
    for inv, desc, qty, unit in INVOICE_ROWS:
        lines.append(f'{inv},"{desc}",{qty},{unit:.2f},{qty * unit:.2f}')
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_tsv(path: Path):
    lines = ["account\towner\tregion\trenewal_date\tarr"]
    rows = [
        ("Cobalt Harbor", "D. Whitfield", "NA-East", "2026-07-01", "63500"),
        ("Juniper Freight", "M. Osei", "EU-West", "2026-09-15", "41200"),
        ("Halcyon Mutual", "R. Tanaka", "APAC", "2027-01-30", "88000"),
    ]
    lines += ["\t".join(r) for r in rows]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_html(path: Path):
    path.write_text(
        "<!DOCTYPE html><html><head><title>Records retention policy</title>"
        "<style>body{font-family:sans-serif;color:#222}</style>"
        "<script>console.log('nav');</script></head><body>"
        "<h1>Records retention policy</h1>"
        + "".join(f"<p>{p}</p>" for p in _paragraphs(CONTRACT_CLAUSES, 3, start=4))
        + "</body></html>",
        encoding="utf-8",
    )


def build_htm(path: Path):
    path.write_text(
        "<html><body><h2>Archived intranet notice (2019)</h2>"
        "<p>The shared drive migrates to the document mirror this weekend. "
        "File new contracts under /corpus/contracts.</p></body></html>",
        encoding="utf-8",
    )


def build_xml(path: Path):
    items = "".join(
        f"<doc id='{inv}'><title>{desc}</title><amount>{qty * unit:.2f}</amount></doc>"
        for inv, desc, qty, unit in INVOICE_ROWS[:3]
    )
    path.write_text(
        f"<?xml version='1.0' encoding='UTF-8'?><export generated='2026-04-14'>{items}</export>",
        encoding="utf-8",
    )


# --------------------------------------------------------------------------- #
# Corpus specification
# --------------------------------------------------------------------------- #


class Entry:
    """One corpus file: how to build it and what probe should say about it."""

    def __init__(self, relpath, category, description, builder,
                 expected_status, *, supported=True, in_probe=True):
        self.relpath = relpath
        self.category = category
        self.description = description
        self.builder = builder
        self.expected_status = expected_status
        self.supported = supported
        self.in_probe = in_probe  # hidden files are excluded by default probe


def corpus_spec(scratch: Path):
    e = Entry
    return [
        # ---- PDF variety -------------------------------------------------
        e("pdf/contract_simple.pdf", "pdf",
          "single-page contract with a clean text layer",
          build_contract_pdf, OK),
        e("pdf/quarterly_report_12pp.pdf", "pdf",
          "12-page narrative report, text layer on every page",
          build_multipage_report_pdf, OK),
        e("pdf/annual_filing_60pp.pdf", "pdf",
          "60-page filing — page-count and throughput stressor",
          build_long_pdf, OK),
        e("pdf/invoice_table.pdf", "pdf",
          "fixed-width invoice table (Courier) — tabular extraction",
          build_invoice_table_pdf, OK),
        e("pdf/research_two_column.pdf", "pdf",
          "two-column academic-style layout — column-order stressor",
          build_two_column_pdf, OK),
        e("pdf/meeting_notes_accented.pdf", "pdf",
          "Latin-1 accented text (résumé/São Paulo/€) — encoding check",
          build_accented_pdf, OK),
        e("pdf/scan_blank_pages.pdf", "pdf",
          "3 pages, no text layer — probe should flag as scan needing OCR",
          build_blank_scan_pdf, NO_TEXT),
        e("pdf/scan_image_only.pdf", "pdf",
          "raster image as sole page content — realistic scanned page",
          build_image_only_pdf, NO_TEXT),
        e("pdf/sealed_user_password.pdf", "pdf",
          "user-password encrypted (RC4-128) — probe reports encrypted",
          lambda p: build_sealed_pdf(p, scratch), ERROR),
        e("pdf/restricted_owner_password.pdf", "pdf",
          "owner-password only — restricted but still readable",
          lambda p: build_restricted_pdf(p, scratch), OK),
        # ---- Office ------------------------------------------------------
        e("office/meeting_minutes.docx", "office",
          "Word document with multi-paragraph body",
          build_docx, OK),
        e("office/budget_forecast.xlsx", "office",
          "Excel workbook with shared strings + one sheet",
          build_xlsx, OK),
        e("office/pitch_deck.pptx", "office",
          "PowerPoint with three text slides",
          build_pptx, OK),
        # ---- OpenDocument ------------------------------------------------
        e("opendocument/project_charter.odt", "opendocument",
          "OpenDocument text", lambda p: build_odf(
              p, ["PROJECT CHARTER — corpus mirror"] + _paragraphs(REPORT_PARAGRAPHS, 3)), OK),
        e("opendocument/headcount_plan.ods", "opendocument",
          "OpenDocument spreadsheet", lambda p: build_odf(
              p, ["Headcount plan FY26", "Engineering 41", "Compliance 9", "Sales 17"]), OK),
        e("opendocument/roadmap_slides.odp", "opendocument",
          "OpenDocument presentation", lambda p: build_odf(
              p, ["Roadmap H2", "Probe everywhere", "Mirror with provenance"]), OK),
        # ---- Plain text --------------------------------------------------
        e("text/correspondence_email.txt", "text",
          "exported email thread (correspondence category)",
          build_txt, OK),
        e("text/incident_runbook.md", "text",
          "markdown with headers, lists, and a code fence",
          build_md, OK),
        e("text/architecture_note.rst", "text",
          "reStructuredText with directives",
          build_rst, OK),
        # ---- Data --------------------------------------------------------
        e("data/expense_lines.csv", "data",
          "comma-separated invoice lines with quoted fields",
          build_csv, OK),
        e("data/crm_accounts.tsv", "data",
          "tab-separated account export",
          build_tsv, OK),
        # ---- Markup ------------------------------------------------------
        e("markup/retention_policy.html", "markup",
          "HTML with <style> and <script> that sampling must strip",
          build_html, OK),
        e("markup/archived_notice.htm", "markup",
          "legacy .htm page",
          build_htm, OK),
        e("markup/document_export.xml", "markup",
          "structured XML export",
          build_xml, OK),
        # ---- E-books / rich text ------------------------------------------
        e("ebooks_richtext/employee_handbook.epub", "ebooks_richtext",
          "valid EPUB3 (no local extractor; parse handles it server-side)",
          build_epub, NO_EXTRACTOR),
        e("ebooks_richtext/legacy_memo.rtf", "ebooks_richtext",
          "RTF memo (no local extractor)",
          build_rtf, NO_EXTRACTOR),
        # ---- Images (OCR-route formats) ------------------------------------
        e("images/receipt_scan.png", "images",
          "receipt image — OCR route", build_png, NO_EXTRACTOR),
        e("images/flow_diagram.gif", "images",
          "diagram image", build_gif, NO_EXTRACTOR),
        e("images/fax_cover.bmp", "images",
          "fax-style bitmap", build_bmp, NO_EXTRACTOR),
        e("images/blueprint_scan.tiff", "images",
          "TIFF scan", build_tiff, NO_EXTRACTOR),
        # ---- Edge cases ----------------------------------------------------
        e("edge_cases/empty_file.txt", "edge_cases",
          "zero-byte text file — sampled as no-text",
          lambda p: p.write_bytes(b""), NO_TEXT),
        e("edge_cases/truncated_report.pdf", "edge_cases",
          "PDF cut off mid-stream (no xref) — error path",
          lambda p: build_truncated_pdf(p, scratch), ERROR),
        e("edge_cases/misnamed_notes.pdf", "edge_cases",
          "plain text saved with a .pdf extension — error path",
          lambda p: p.write_text("these are just notes, not a PDF\n"), ERROR),
        e("edge_cases/corrupt_archive.docx", "edge_cases",
          "random bytes with a .docx extension — BadZipFile path",
          lambda p: p.write_bytes(b"\x00\x01not a zip archive\x02" * 16), ERROR),
        e("edge_cases/notes with spaces éü.txt", "edge_cases",
          "spaces + unicode in the filename",
          lambda p: p.write_text("Walkthrough notes from the München office visit.\n",
                                 encoding="utf-8"), OK),
        e("edge_cases/exports/raw_dump.json", "edge_cases",
          "extension outside the supported set — flagged unsupported",
          lambda p: p.write_text(json.dumps({"rows": INVOICE_ROWS[:2]}, indent=1)),
          NO_EXTRACTOR, supported=False),
        e("edge_cases/archive/2019/q3/old_notes.txt", "edge_cases",
          "three directories deep — recursion check",
          lambda p: p.write_text("Q3 2019: migrated the shared drive to the mirror.\n"), OK),
        e("edge_cases/.hidden_draft.txt", "edge_cases",
          "hidden dotfile — excluded by probe unless --include-hidden",
          lambda p: p.write_text("draft: do not circulate\n"), OK, in_probe=False),
    ]


# jpg needs Pillow; added conditionally in build_corpus.
JPG_ENTRY = (
    "images/whiteboard_photo.jpg", "images",
    "whiteboard photo (rendered with Pillow)", build_jpg, NO_EXTRACTOR,
)

# --------------------------------------------------------------------------- #
# Optional real-world downloads — layered on top when the network allows.
# Synthetic fixtures can't reproduce real layout complexity; these can.
# (url, relpath, category, description, expected_status, magic_prefixes)
# --------------------------------------------------------------------------- #

DOWNLOADS = [
    ("https://arxiv.org/pdf/1706.03762",
     "pdf/real_arxiv_attention_paper.pdf", "pdf",
     "real two-column academic paper with tables and math (arXiv 1706.03762)",
     OK, (b"%PDF",)),
    ("https://www.irs.gov/pub/irs-pdf/fw9.pdf",
     "pdf/real_irs_form_w9.pdf", "pdf",
     "real fillable AcroForm (IRS Form W-9)",
     OK, (b"%PDF",)),
    ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
     "pdf/real_w3c_dummy.pdf", "pdf",
     "minimal real-world single-page PDF (W3C test file)",
     OK, (b"%PDF",)),
    ("https://www.rfc-editor.org/rfc/rfc9110.txt",
     "text/real_rfc9110_http_semantics.txt", "text",
     "large real plain-text document (RFC 9110)",
     OK, None),
    ("https://www.gutenberg.org/ebooks/1342.epub.noimages",
     "ebooks_richtext/real_gutenberg_pride_and_prejudice.epub", "ebooks_richtext",
     "real EPUB (Project Gutenberg #1342)",
     NO_EXTRACTOR, (b"PK",)),
]


def fetch(url: str, dest: Path, magic) -> str | None:
    """Download url to dest; return an error string instead of raising."""
    req = urllib.request.Request(url, headers={"User-Agent": "kemb-benchmark/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT) as resp:
            data = resp.read()
    except (urllib.error.URLError, OSError, ValueError) as exc:
        return f"{type(exc).__name__}: {exc}"
    if not data:
        return "empty response"
    if magic and not any(data.startswith(m) for m in magic):
        return f"unexpected content (first bytes {data[:8]!r})"
    dest.write_bytes(data)
    return None


# --------------------------------------------------------------------------- #
# Build + verify
# --------------------------------------------------------------------------- #


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_corpus(dest: Path, *, offline: bool) -> dict:
    corpus = dest / "corpus"
    if corpus.exists():
        shutil.rmtree(corpus)
    corpus.mkdir(parents=True)

    manifest_files = []
    spec = corpus_spec(scratch=corpus)
    if _load_pillow()[0]:
        rel, cat, desc, builder, status = JPG_ENTRY
        spec.append(Entry(rel, cat, desc, builder, status))
    else:
        print("note: Pillow not installed — images are minimal stubs, .jpg skipped")

    for entry in spec:
        target = corpus / entry.relpath
        target.parent.mkdir(parents=True, exist_ok=True)
        entry.builder(target)
        manifest_files.append({
            "path": entry.relpath,
            "category": entry.category,
            "source": "generated",
            "description": entry.description,
            "bytes": target.stat().st_size,
            "sha256": _sha256(target),
            "expected_sample_status": entry.expected_status,
            "expected_supported": entry.supported,
            "expected_in_default_probe": entry.in_probe,
        })
    print(f"generated {len(manifest_files)} files")

    skipped_downloads = []
    if offline:
        print("offline mode: skipping real-world downloads")
        skipped_downloads = [{"url": u, "path": p, "reason": "offline"}
                             for u, p, *_ in DOWNLOADS]
    else:
        for url, relpath, category, description, status, magic in DOWNLOADS:
            target = corpus / relpath
            error = fetch(url, target, magic)
            if error:
                print(f"  download skipped ({relpath}): {error}")
                skipped_downloads.append({"url": url, "path": relpath, "reason": error})
                continue
            print(f"  downloaded {relpath} ({target.stat().st_size:,} bytes)")
            manifest_files.append({
                "path": relpath,
                "category": category,
                "source": url,
                "description": description,
                "bytes": target.stat().st_size,
                "sha256": _sha256(target),
                "expected_sample_status": status,
                "expected_supported": True,
                "expected_in_default_probe": True,
            })

    manifest = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "scripts/build_benchmark_corpus.py",
        "corpus_dir": "corpus",
        "total_files": len(manifest_files),
        "total_bytes": sum(f["bytes"] for f in manifest_files),
        "skipped_downloads": skipped_downloads,
        "files": sorted(manifest_files, key=lambda f: f["path"]),
    }
    (dest / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"corpus ready: {dest} ({manifest['total_files']} files, "
          f"{manifest['total_bytes']:,} bytes)")
    return manifest


def verify_corpus(dest: Path, manifest: dict) -> int:
    """Run `kemb probe --sample --json` over the corpus and check every
    file's sample status against the manifest. Returns a process exit code."""
    repo_src = Path(__file__).resolve().parent.parent / "src"
    if (repo_src / "kemb").is_dir():
        sys.path.insert(0, str(repo_src))
    try:
        from kemb import _core
    except ImportError as exc:
        print(f"verify: cannot import kemb ({exc}) — install it or run from the repo")
        return 2

    corpus = dest / "corpus"
    buf = io.StringIO()
    started = time.perf_counter()
    with redirect_stdout(buf):
        rc = _core.main(["probe", str(corpus), "--sample", "--json"])
    elapsed = time.perf_counter() - started
    if rc != 0:
        print(f"verify: probe exited {rc}")
        return rc
    report = json.loads(buf.getvalue())
    probed = {f["relative"]: f for f in report["files"]}

    failures = []
    for spec in manifest["files"]:
        path = spec["path"]
        entry = probed.get(path)
        if not spec["expected_in_default_probe"]:
            if entry is not None:
                failures.append(f"{path}: expected probe to exclude this hidden file")
            continue
        if entry is None:
            failures.append(f"{path}: missing from probe output")
            continue
        if entry["sample_status"] != spec["expected_sample_status"]:
            failures.append(
                f"{path}: sample_status {entry['sample_status']!r} "
                f"(detail: {entry.get('sample_detail')}) "
                f"!= expected {spec['expected_sample_status']!r}"
            )
        if entry["supported"] != spec["expected_supported"]:
            failures.append(
                f"{path}: supported={entry['supported']} "
                f"!= expected {spec['expected_supported']}"
            )

    checked = sum(1 for f in manifest["files"] if f["expected_in_default_probe"])
    by_status = {}
    for f in report["files"]:
        by_status[f["sample_status"]] = by_status.get(f["sample_status"], 0) + 1
    print(f"\nverify: probed {len(report['files'])} files in {elapsed:.2f}s "
          f"({len(report['files']) / elapsed:.0f} files/s)")
    print("verify: sample statuses " + ", ".join(
        f"{k}={v}" for k, v in sorted(by_status.items())))
    if failures:
        print(f"verify: {len(failures)} mismatch(es):")
        for line in failures:
            print(f"  FAIL {line}")
        return 1
    print(f"verify: all {checked} expectations met "
          f"(+{len(manifest['files']) - checked} hidden-file exclusion check)")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dest", default=DEFAULT_DEST, type=Path,
        help=f"output directory (default: ./{DEFAULT_DEST})",
    )
    parser.add_argument(
        "--offline", action="store_true",
        help="skip real-world downloads; build the fully synthetic corpus only",
    )
    parser.add_argument(
        "--verify", action="store_true",
        help="after building, run `kemb probe --sample` over the corpus and "
             "check each file's status against the manifest",
    )
    args = parser.parse_args(argv)

    # Like kemb's own loader, catch more than ImportError: a broken system
    # `cryptography` can make `import pypdf` raise arbitrary exceptions.
    try:
        import pypdf  # noqa: F401
    except BaseException as exc:
        parser.error(
            "pypdf is required and failed to import "
            f"({type(exc).__name__}: {exc}) — try `pip install -U pypdf cffi cryptography`"
        )

    manifest = build_corpus(args.dest, offline=args.offline)
    if args.verify:
        return verify_corpus(args.dest, manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
