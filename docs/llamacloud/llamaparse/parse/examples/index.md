---
title: Parse Examples | Developer Documentation
description: Runnable example tutorials demonstrating Parse for common document workflows — first parse, chart extraction, financial table extraction, custom prompts, batch processing, spreadsheets, and TypeScript/Node.js integration.
---

A collection of runnable tutorials for the most common Parse workflows. Each one walks through a real document end-to-end and shows the SDK calls in context. Most tutorials are Python notebooks (Jupyter, Colab); the TypeScript tutorial shows the same patterns from Node.js. If you’re new to Parse, the [Getting Started](/llamaparse/parse/getting_started/index.md) page will give you the bare-bones first parse in 60 seconds.

## Start here

[Quick Start: Parse a PDF & Interpret Outputs ](/llamaparse/parse/examples/parse_pdf_outputs/index.md)Python · Parse a real US Treasury financial report and interpret the four most common output views — text, markdown, items, and metadata. The best place to start if you're new to the Parse SDK.

[Parse a PDF in TypeScript ](/llamaparse/parse/examples/parse_pdf_typescript/index.md)TypeScript · Parse a PDF from a Node.js script — install, set the API key, run the parse, walk the markdown output, and save it to disk. The TypeScript counterpart to the Python Quick Start.

## By use case

### Structured extraction

[Parse a Financial Report and Extract Every Table ](/llamaparse/parse/examples/parse_financial_tables/index.md)Walk every page of a real Treasury financial report, pull every table out into pandas DataFrames with source-page provenance, and turn on Cost Optimizer to keep costs down on long mixed-complexity documents.

[Parse Embedded Charts and Analyze with Pandas ](/llamaparse/parse/examples/parse_charts_pandas/index.md)Use specialized chart parsing to extract chart data from a financial report, then load the resulting tables into pandas for summaries, plots, and value counts.

[Parse and Analyze Excel Spreadsheets ](/llamaparse/parse/examples/parse_excel_sheets/index.md)Parse a multi-sheet XLSX template and (optionally) build a small RAG app over the rows with the LlamaIndex framework.

### Prompt engineering

[Parse with Additional Prompts ](/llamaparse/parse/examples/parse_with_prompts/index.md)Steer Parse with a custom prompt to focus on the parts of a document you care about. Walks through extracting just the prices from a McDonald's receipt.

### Bulk processing

[Parse All PDFs in a Folder (Async) ](/llamaparse/parse/examples/async_parse_folder/index.md)Batch-parse every PDF in a directory with controlled concurrency using asyncio and a semaphore. The pattern to use when you have hundreds or thousands of files.

## More resources

- **Browse the SDK examples on GitHub** — for more detailed Python SDK examples, see [`run-llama/llama-cloud-py/tree/main/examples/parse`](https://github.com/run-llama/llama-cloud-py/tree/main/examples/parse).
- **Look up an option** — see the [Input Options](/llamaparse/parse/guides/configuring-parse/#input-options/index.md), [Output Options](/llamaparse/parse/guides/configuring-parse/#output-options/index.md), and [Processing Options](/llamaparse/parse/guides/configuring-parse/#processing-options/index.md) groups for prose explanations of every knob.
- **Pick the right tier** — see the [Tiers](/llamaparse/parse/guides/tiers/index.md) page for guidance on `fast` vs `cost_effective` vs `agentic` vs `agentic_plus`.
- **Understand the configuration model** — see the [Configuration Model](/llamaparse/parse/guides/configuring-parse/index.md) page for where every option lives in the request shape.
