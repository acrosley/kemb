---
title: Pricing | Developer Documentation
description: Detailed information about LlamaParse credit pricing and usage rates for parsing, indexing, extraction, classification, and split services.
---

All features are priced using **credits**, which are billed per page (or minute for audio). Credits vary by parsing mode, model, and whether files are cached.

---

## Credit Rates

| Region        | Price per 1,000 Credits |
| ------------- | ----------------------- |
| North America | $1.25                   |
| Europe        | $1.25                   |

## Parsing

- [v2 (Tiers)](#tab-panel-28)
- [v1 (Modes)](#tab-panel-29)

In the v2 API, parsing uses a simplified **tier-based** system. Choose a tier and the platform handles model selection automatically.

| Tier           | Credits per Page |
| -------------- | ---------------- |
| Fast           | 1                |
| Cost-effective | 3                |
| Agentic        | 10               |
| Agentic Plus   | 45               |

**Additional Configs:**

- **Layout extraction:** +3 credits per page (can be added to any tier)
- **Spreadsheet:** 1 credit per sheet
- **Audio:** 3 credits per minute

In the v1 API, you select a parse mode and model directly.

| Category                 | Mode                         | Model                             | Credits per Page |
| ------------------------ | ---------------------------- | --------------------------------- | ---------------- |
| **Recommended Settings** | Cost-effective               | -                                 | 3                |
|                          | Agentic                      | -                                 | 10               |
|                          | Agentic Plus                 | -                                 | 45               |
| **Presets**              | Invoice                      | -                                 | 90               |
|                          | Scientific papers            | -                                 | 90               |
|                          | Technical documentation      | -                                 | 90               |
|                          | Forms                        | -                                 | 90               |
| **Modes**                | Parse without AI             | -                                 | 1                |
|                          | Parse page with LLM          | -                                 | 3                |
|                          | Parse page with LVM          | anthropic-sonnet-3.5 (deprecated) | 60               |
|                          |                              | anthropic-sonnet-3.7              | 60               |
|                          |                              | anthropic-sonnet-4.0              | 60               |
|                          |                              | anthropic-sonnet-4.5              | 60               |
|                          |                              | anthropic-haiku-4.5 (preview)     | 30               |
|                          |                              | openai-gpt-4o-mini                | 15               |
|                          |                              | openai-gpt-4o                     | 30               |
|                          |                              | openai-gpt-4-1-nano               | 15               |
|                          |                              | openai-gpt-4-1-mini               | 20               |
|                          |                              | openai-gpt-4-1                    | 30               |
|                          |                              | openai-gpt-5-nano                 | 10               |
|                          |                              | openai-gpt-5-mini                 | 30               |
|                          |                              | openai-gpt-5                      | 150              |
|                          |                              | gemini-2.0-flash                  | 6                |
|                          |                              | gemini-2.5-flash                  | 25               |
|                          |                              | gemini-2.5-pro                    | 60               |
|                          |                              | Custom Azure Model                | 1                |
|                          |                              | Use your own API key              | 1                |
|                          | Parse page with Layout Agent | -                                 | 45               |
|                          | Parse page with Agent        | anthropic-sonnet-3.5 (deprecated) | 45               |
|                          |                              | anthropic-sonnet-3.7              | 90               |
|                          |                              | anthropic-sonnet-4.0              | 90               |
|                          |                              | anthropic-sonnet-4.5              | 90               |
|                          |                              | anthropic-haiku-4.5 (preview)     | 45               |
|                          |                              | openai-gpt-4-1-mini               | 10               |
|                          |                              | openai-gpt-4-1                    | 45               |
|                          |                              | openai-gpt-5-nano                 | 10               |
|                          |                              | openai-gpt-5-mini                 | 45               |
|                          |                              | openai-gpt-5                      | 90               |
|                          |                              | gemini-2.0-flash                  | 10               |
|                          |                              | gemini-2.5-flash                  | 10               |
|                          |                              | gemini-2.5-pro                    | 45               |
|                          | Auto Mode                    | -                                 | 3–45             |
|                          | Parse document with LLM      | -                                 | 30               |
|                          | Parse document with Agent    | anthropic-sonnet-3.7              | 90               |
|                          |                              | anthropic-sonnet-4.0              | 90               |
|                          |                              | anthropic-sonnet-4.5              | 90               |
| **Other Options**        | Structure Output             | -                                 | 3                |
| **File Type Modes**      | Spreadsheet                  | -                                 | 1 per sheet      |
|                          | Audio                        | -                                 | 3 per minute     |
| **Legacy Modes**         | Continuous Mode              | -                                 | 30               |

**Additional Configs:**

- **Layout extraction:** +3 credits per page (can be added to any mode)

---

## Indexing

| Mode        | Credits per Page (or Sheet) |
| ----------- | --------------------------- |
| Standard    | 1                           |
| Spreadsheet | 2                           |
| Multi-modal | 2                           |

---

## Extraction

- [v2 (Tiers)](#tab-panel-30)
- [v1 (Modes)](#tab-panel-31)

In the v2 API, extraction uses a simplified **tier-based** system. **Total credits per page = extract tier + parse tier.** Pick an extract tier for the structured-data step, and a parse tier for how the document is interpreted before extraction.

**Extract tier** — quality of structured-data extraction:

| Extract Tier   | Credits per Page (extract only)\* |
| -------------- | --------------------------------- |
| Cost-effective | 5                                 |
| Agentic        | 15                                |

**Parse tier** — how the document is interpreted before extraction (configurable under Advanced Options; defaults to match the extract tier):

| Parse Tier     | Credits per Page |
| -------------- | ---------------- |
| Fast           | 1                |
| Cost-effective | 3                |
| Agentic        | 10               |
| Agentic Plus   | 45               |

**Range:** 6 credits/page (Cost-effective extract + Fast parse) to 60 credits/page (Agentic extract + Agentic Plus parse).

*\*For text files or pre-cached parsed files, only the extract-tier cost applies.*

- For text files (md, txt, csv, html), a page is defined as the equivalent of 600 tokens.
- For text files or if the file has previously been parsed by LlamaParse, only the extract-tier cost applies.

| Mode       | Credits per Page | Credits per Page (extract only)\* |
| ---------- | ---------------- | --------------------------------- |
| Fast       | 5                | 4                                 |
| Balanced   | 10               | 7                                 |
| Multimodal | 20               | 14                                |
| Premium    | 60               | 15                                |

*\*For text files or pre-cached parsed files.*

- For text files (md, txt, csv, html), a page is defined as the equivalent of 600 tokens.
- For text files or if the file has previously been parsed by LlamaParse, only extraction costs apply.
- For Multimodal mode, 6 additional credits will be charged for docx/pptx format.

---

## Split

| Mode    | Credits per Page       |
| ------- | ---------------------- |
| Default | 4 (3 for cached files) |

> If the file is already present in the LlamaParse cache, only split costs apply.

---

## Classification

| Mode       | Credits per Page |
| ---------- | ---------------- |
| Fast       | 1                |
| Multimodal | 2                |

---

## Sheets

Sheets is currently in beta and **free to use**.

---

## Agents

Agents is currently in beta and **free to use**. When agents make use of Parse, Extract, or Index, the pricing of the underlying module applies.

---

## Cost Optimization Strategies

### Parse

1. **Use caching** — Parsed files are cached for 48 hours. Re-parsing the same file within that window is free.
2. **Choose the right tier** — Start with Cost-effective (3 credits) for initial testing. Only move to Agentic (10) or Agentic Plus (45) when document complexity requires it. Fast (1 credit) outputs spatial text only — no markdown.
3. **Use page ranges** — Parse only the pages you need instead of entire documents. Specify `target_pages` to avoid processing irrelevant content.

### Cross-product

4. **Leverage extract-only pricing** — If a file was previously parsed, subsequent extractions cost less (extract-only rates apply). Parse once, extract many times.
5. **Pre-filter with Classify** — Use Classify (1-2 credits/page) to filter documents before running more expensive Parse or Extract jobs.
6. **Batch strategically** — Group similar documents in a single job when possible rather than submitting many small requests.
