---
title: Parse a Financial Report and Extract Every Table | Developer Documentation
---

This tutorial walks through one of the most common Parse use cases: **pulling every table out of a financial report and loading it into pandas**. We use the same [2024 Executive Summary by the Bureau of the Fiscal Service](https://fiscal.treasury.gov/files/reports-statements/financial-report/2024/executive-summary-2024.pdf) as the [Quick Start tutorial](/llamaparse/parse/examples/parse_pdf_outputs/index.md), so you can compare the two end-to-end.

The pattern in this tutorial generalizes to any financial document with mixed prose and tables — 10-Ks, earnings reports, investor decks, audit reports.

## When to use this pattern

- Your document has **multiple tables across multiple pages** and you want all of them, not just one
- You need the table data as **structured rows**, not just markdown text
- You want to **load tables directly into pandas** for downstream analysis or RAG indexing

If you only need a single table from a known page, see [Parse Charts in PDFs and Analyze with Pandas](/llamaparse/parse/examples/parse_charts_pandas/index.md) — it shows the simpler “one specific table” version. If you only need text or markdown, [Quick Start: Parse a PDF & Interpret Outputs](/llamaparse/parse/examples/parse_pdf_outputs/index.md) is enough.

## 1. Setup

Install the Parse SDK and pandas:

Terminal window

```
pip install llama-cloud pandas
```

Set your API key (this is a notebook tutorial — `getpass` works in Jupyter or Colab):

```
import os
from getpass import getpass


os.environ["LLAMA_CLOUD_API_KEY"] = getpass("Llama Cloud API Key: ")
```

Initialize an async client (this tutorial uses async because we’ll request a richer set of `expand` values and want to keep the example consistent with the rest of the tutorials):

```
from llama_cloud import AsyncLlamaCloud


client = AsyncLlamaCloud()
```

## 2. Parse the document

Upload the PDF and run a parse job. We pick `agentic` for solid table accuracy and request the `items` view so we get a structured tree we can walk for tables.

For a long mixed-complexity report, **enable [Cost Optimizer](/llamaparse/parse/guides/configuring-parse/#cost-optimizer/index.md)**. The Treasury document has many text-heavy narrative pages and a handful of table-heavy summary pages — Cost Optimizer will route the simple pages to `cost_effective` automatically and only spend premium credits on the table pages. We also request `metadata` so we can see which pages got cost-optimized.

```
file_obj = await client.files.create(
    file="executive-summary-2024.pdf",  # use /content/executive-summary-2024.pdf in Colab
    purpose="parse",
)


result = await client.parsing.parse(
    file_id=file_obj.id,
    tier="agentic",
    version="latest",
    processing_options={
        "cost_optimizer": {"enable": True},
    },
    expand=["markdown", "items", "metadata"],
)


print(f"Job status: {result.job.status}")
print(f"Total pages: {len(result.items.pages)}")
```

Where each option lives in the request shape: `tier` and `version` are top-level required fields, `processing_options.cost_optimizer.enable` enables per-page tier routing, and `expand` is a top-level array that controls what comes back. See [Configuration Model](/llamaparse/parse/guides/configuring-parse/index.md) for the full picture.

## 3. See which pages were cost-optimized

Cost Optimizer adds a `cost_optimized` flag to the per-page metadata. Inspect it to confirm the routing landed where you’d expect — text-heavy narrative pages should be `True` (processed on `cost_effective`) and table-heavy pages should be `False` (processed on `agentic`).

```
for page in result.metadata.pages:
    flag = "cost-optimized" if page.cost_optimized else "premium tier"
    print(f"page {page.page_number}: {flag}")
```

If you see a page with a clear table but `cost_optimized: True`, something’s off — the classifier is supposed to route table pages to the premium tier. File a support ticket with the document so the team can tune the heuristic. For more on how routing works, see [Cost Optimizer → How it works](/llamaparse/parse/guides/configuring-parse/#processing-options#how-it-works/index.md).

## 4. Find every table in the items tree

The `items` view returns a structured tree of typed elements per page: headings, paragraphs, tables, figures. Tables are `item.type == "table"` and carry a `rows` field (a list of lists), plus `csv`, `html`, and `md` representations of the same data.

Walk every page, collect every table, and tag each with its source page so you can trace back later:

```
all_tables = []


for page in result.items.pages:
    for item in page.items:
        if getattr(item, "type", None) == "table":
            all_tables.append({
                "page_number": page.page_number,
                "rows": item.rows,
                "csv": item.csv,
            })


print(f"Found {len(all_tables)} tables across {len(result.items.pages)} pages.")
for t in all_tables:
    n_rows = len(t["rows"])
    n_cols = len(t["rows"][0]) if t["rows"] else 0
    print(f"  page {t['page_number']}: {n_rows} rows × {n_cols} cols")
```

For our Treasury PDF, the first page contains the marquee “Financial Position & Condition” summary table — the same one shown in detail in the [Quick Start tutorial](/llamaparse/parse/examples/parse_pdf_outputs/#markdown-view-resultmarkdown/index.md). Subsequent pages contain narrative prose mixed with smaller summary tables.

## 5. Load each table into pandas

`item.csv` is the easiest path into pandas. Parse generates a clean CSV string for every table, which `pandas.read_csv` can ingest directly via a `StringIO` wrapper:

```
import io
import pandas as pd


dataframes = []
for t in all_tables:
    df = pd.read_csv(io.StringIO(t["csv"]))
    df["_source_page"] = t["page_number"]  # keep the source page for traceability
    dataframes.append(df)


# Quick look at the first table
if dataframes:
    print(dataframes[0].head())
    print(f"\nColumns: {list(dataframes[0].columns)}")
```

Each DataFrame keeps a `_source_page` column so you can group by source, write back to your data warehouse with provenance, or build a citation-aware RAG index where every row knows which page it came from.

## 6. Filter to specific tables you care about

Most financial reports have a few “summary” tables you actually care about and a long tail of supplementary tables you’d skip. Filter the list by content or shape:

```
# Tables with at least 5 rows (skip tiny one-line summaries)
substantial_tables = [df for df in dataframes if len(df) >= 5]


# Or filter by column header contents
financial_tables = [
    df for df in dataframes
    if any("$" in str(c) or "Dollar" in str(c) for c in df.columns)
]


print(f"Substantial tables: {len(substantial_tables)}")
print(f"Financial tables (with $ in column headers): {len(financial_tables)}")
```

You can also filter by source page if you already know which sections of the report matter:

```
# Only tables from the executive summary section (e.g. pages 1-3)
exec_summary_tables = [
    pd.read_csv(io.StringIO(t["csv"]))
    for t in all_tables
    if t["page_number"] in (1, 2, 3)
]
```

## 7. Save the tables for downstream use

Once you have the DataFrames, the rest is standard pandas. A few common patterns:

```
# Save each table as a separate CSV with a deterministic filename
for i, t in enumerate(all_tables):
    filename = f"table_p{t['page_number']:03d}_{i}.csv"
    pd.read_csv(io.StringIO(t["csv"])).to_csv(filename, index=False)


# Or write them all into a single Excel workbook, one sheet per table
with pd.ExcelWriter("financial_tables.xlsx") as writer:
    for i, t in enumerate(all_tables):
        df = pd.read_csv(io.StringIO(t["csv"]))
        sheet_name = f"page{t['page_number']}_{i}"[:31]  # Excel limit
        df.to_excel(writer, sheet_name=sheet_name, index=False)
```

If you’d rather have Parse export the tables as a real `.xlsx` file in one shot (instead of looping in Python), enable [tables-as-spreadsheet output](/llamaparse/parse/guides/configuring-parse/#tables-as-spreadsheet/index.md) and retrieve via `expand=["xlsx_content_metadata"]` — it returns a presigned URL for the Excel file.

## What to do with the tables next

A few high-leverage patterns that build on what you have now:

- **Citation-aware RAG.** Each row knows its source page from the `_source_page` column. When you embed and index the rows, store the page number in metadata. Your retriever can cite specific pages back in answers.
- **Schema validation.** Use [LlamaExtract](/llamaparse/extract/getting_started/index.md) on the same document with a Pydantic schema if you need guaranteed-shape JSON instead of tables — Extract is purpose-built for that.
- **Cross-document comparison.** Run this same pattern across multiple years’ worth of 10-Ks, then concatenate the DataFrames with a `_year` column to track metric changes over time.

## See also

- [Parse Charts in PDFs and Analyze with Pandas](/llamaparse/parse/examples/parse_charts_pandas/index.md) — the chart-focused version of this tutorial
- [Quick Start: Parse a PDF & Interpret Outputs](/llamaparse/parse/examples/parse_pdf_outputs/index.md) — what each `expand` view returns, in detail
- [Cost Optimizer](/llamaparse/parse/guides/configuring-parse/#cost-optimizer/index.md) — per-page tier routing
- [Tiers](/llamaparse/parse/guides/tiers/index.md) — pick the right tier for your document
- [Retrieving Results](/llamaparse/parse/guides/retrieving-results/index.md) — every legal `expand` value
- [LlamaExtract](/llamaparse/extract/getting_started/index.md) — schema-driven extraction for when you need guaranteed JSON shape
