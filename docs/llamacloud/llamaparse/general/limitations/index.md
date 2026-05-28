---
title: Limitations | Developer Documentation
description: Current limitations for LlamaParse services including file size limits, page limits, processing timeouts, schema constraints, and concurrency limits.
---

This page documents the current service limitations across LlamaParse products. See also [Rate Limits](/llamaparse/general/rate_limits/index.md) for API rate limiting details.

## General

These limits apply across all LlamaParse services:

| Limit             | Value | Notes                                                                    |
| ----------------- | ----- | ------------------------------------------------------------------------ |
| Maximum file size | 512MB | Platform-wide upload limit; individual services may enforce lower limits |

## Parse

| Limit                             | Value        | Notes                                                                                 |
| --------------------------------- | ------------ | ------------------------------------------------------------------------------------- |
| Supported file formats            | 130+ formats | See [Supported Document Types](/llamaparse/general/supported_document_types/index.md) |
| Maximum images extracted per page | 35           | Only the 35 largest images are extracted/OCR processed                                |
| Maximum text extracted per page   | 64KB         | Content beyond 64KB is ignored                                                        |

### Timeout Behavior

Parse jobs have a configurable timeout composed of:

- **Base timeout**: up to 30 minutes (1,800 seconds)
- **Per-page timeout**: up to 5 minutes (300 seconds) additional time per page

The total timeout is calculated as: `base timeout + (per-page timeout × page count)`.

## Extract

| Limit                         | Value              | Notes                                                             |
| ----------------------------- | ------------------ | ----------------------------------------------------------------- |
| Maximum file size             | 100MB              |                                                                   |
| Maximum pages per extraction  | 500                | Enforced for files larger than 5MB                                |
| Maximum schema properties     | 5,000              | Total properties across the entire schema                         |
| Maximum schema nesting depth  | 7 levels           |                                                                   |
| Maximum schema string content | 120,000 characters | Combined total for all field names, descriptions, and enum values |
| Maximum raw JSON schema size  | 150,000 characters |                                                                   |

For workflows that exceed these limits, we recommend splitting the job into smaller, targeted extraction jobs. See the [Split and Extract](/llamaparse/extract/examples/split_and_extract_resume_book/index.md) example for a walkthrough. For more details on schema constraints, see [Schema Design and Restrictions](/llamaparse/extract/guides/schema_design/index.md).

## Classify

| Limit                                | Value             | Notes                                                     |
| ------------------------------------ | ----------------- | --------------------------------------------------------- |
| Minimum classification rules per job | 1                 | All rule types must be unique                             |
| Rule type length                     | 1–50 characters   | Alphanumeric characters, spaces, hyphens, and underscores |
| Rule description length              | 10–500 characters |                                                           |

## Split

| Limit                       | Value                     | Notes |
| --------------------------- | ------------------------- | ----- |
| Maximum file size           | 512MB                     |       |
| Supported file formats      | PDF, DOC, DOCX, PPT, PPTX |       |
| Categories per job          | 1–50                      |       |
| Category name length        | 1–200 characters          |       |
| Category description length | up to 2,000 characters    |       |
| Custom instructions length  | up to 5,000 characters    |       |

## Sheets

Sheets is currently in beta and subject to change.

| Limit                     | Value     | Notes |
| ------------------------- | --------- | ----- |
| Maximum columns per sheet | 100       |       |
| Maximum rows per sheet    | 10,000    |       |
| Maximum cells per sheet   | 1,000,000 |       |

## Index

| Limit                                     | Value | Notes           |
| ----------------------------------------- | ----- | --------------- |
| Maximum concurrent parse jobs per project | 30    | During indexing |

Index-specific limits for pages, files, data sources, and embedding models may vary by plan. Contact support for details on your plan’s limits.
