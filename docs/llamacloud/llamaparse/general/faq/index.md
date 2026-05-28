---
title: FAQ | Developer Documentation
description: Frequently asked questions about LlamaParse products, covering Parse, Extract, Index, Classify, Split, Sheets, pricing, privacy, and more.
---

## General

How do credits work?

All features are priced using credits, which are billed per page (or minute for audio). Credits vary by product, mode, and whether files are cached. Check the [Credit Pricing & Usage](/llamaparse/general/pricing/index.md) page for full details.

What file formats are supported?

LlamaParse supports 130+ file formats across documents, images, spreadsheets, and audio. See [Supported Document Types](/llamaparse/general/supported_document_types/index.md) for the full list. Other products like Extract, Classify, and Split support subsets of these formats — refer to each product’s documentation for specifics.

What are the current limitations?

See the [Limitations](/llamaparse/general/limitations/index.md) page for service-specific limits on file size, page counts, schema constraints, timeouts, and more.

What are the API rate limits?

LlamaParse implements rate limiting on high-traffic endpoints to ensure fair usage. Free tier organizations have lower limits (20 requests per minute). See the [Rate Limits](/llamaparse/general/rate_limits/index.md) page for details.

What happens when I run out of credits?

On **paid plans** (Starter, Pro), pay-as-you-go usage is enabled by default — additional credits are billed at the standard rate ($1.25 per 1,000 credits). On the **Free plan**, API requests that consume credits will return a `402` error, and credits reset at the start of your next billing cycle. See [Billing and Usage](/llamaparse/general/billing/index.md) for plan details and upgrade options.

Which SDK package should I use?

Use the `llama-cloud` package (PyPI: `llama-cloud`, npm: `@llamaindex/llama-cloud`). This is the current SDK that supports all products including Parse, Extract, Classify, Split, Sheets, and Index. The older `llama-cloud-services` package is deprecated — if you’re currently using it, we recommend migrating to `llama-cloud`.

Is LlamaParse available in the EU?

Yes. LlamaParse is available in both North America and Europe. Both regions support the same core functionality. To use the EU region, set your API base URL to `api.cloud.eu.llamaindex.ai`. See [Regions](/llamaparse/general/regions/index.md) for details.

Can I self-host or deploy on-prem?

Yes. LlamaParse supports self-hosted and BYOC (Bring Your Own Cloud) deployments for enterprise customers. See the [Self-Hosting documentation](/llamaparse/self_hosting/index.md) for setup guides and configuration options, or contact <sales@runllama.ai> to discuss your deployment needs.

Do you support webhooks for async notifications?

Yes. LlamaParse supports webhooks for Parse, Extract, Classify, and Split jobs. Configure a webhook endpoint to receive real-time notifications when jobs complete, fail, or change state — no polling required. See the [Webhooks guide](/llamaparse/general/webhooks/index.md) for setup instructions and supported events.

How do I get help or report an issue?

If you are experiencing issues, check the [Status Page](https://llamaindex.statuspage.io/) for ongoing incidents. You can also review the [Troubleshooting & Error Codes](/llamaparse/general/troubleshooting/index.md) guide. For unresolved issues, contact <support@runllama.ai>.

## Privacy & Caching

Are documents stored or cached? If so, for how long?

Your data is kept private to you only and is used only to return your results, never for model training. To avoid charging multiple times for processing the same document, your files are cached for 48 hours and then permanently deleted from our servers.

How do I avoid caching sensitive documents?

If you wish to avoid caching sensitive documents, you may set `do_not_cache=True` when submitting a parse or extract job.

Is my data private when using Extract?

Yes. Your data is kept private and is used only to return your results, never for model training. See the [LlamaExtract Privacy](/llamaparse/extract/privacy/index.md) page for more information.

## Parse

How long does parsing typically take?

It depends on the length and complexity of the document, in particular:

- The number of pages
- The number of images
  - And whether text must be extracted from those images
- The density of text on each page

On average, parsing a block of pages takes 45 seconds. However, this is a rough estimate and the actual time may vary. For example, a document with many images may take longer to parse than a text-only document with the same number of pages.

What parsing tiers are available?

In the v2 API, parsing uses a tier-based system: **Fast** (1 credit/page), **Cost-effective** (3), **Agentic** (10), and **Agentic Plus** (45). The platform selects the best model automatically for each tier. Layout extraction is always enabled and free in v2. See [Pricing](/llamaparse/general/pricing/index.md) for full details.

Can I parse only specific pages of a document?

Yes. Use the `target_pages` parameter to parse only the pages you need. This is a great way to reduce costs and processing time for large documents.

My parse job is timing out on a large document. What can I do?

Parse jobs have a configurable timeout composed of a base timeout (up to 30 minutes) plus a per-page timeout (up to 5 minutes per page). For very large or image-heavy documents, try:

1. **Use `target_pages`** to parse only the pages you need
2. **Choose a faster tier** — Fast (1 credit) extracts text only, without LLM processing
3. **Split the document** — use the [Split API](/llamaparse/split/getting_started/index.md) to segment large PDFs before parsing

See [Limitations](/llamaparse/general/limitations/index.md) for timeout details, and [Troubleshooting](/llamaparse/general/troubleshooting/index.md) for error codes.

What is the difference between the v1 and v2 Parse API?

The v2 API uses a simplified **tier-based** system (Fast, Cost-effective, Agentic, Agentic Plus) where the platform automatically selects the best model for each tier. The v1 API requires you to select a parse mode and model directly. We recommend the v2 API for new projects. See the [v1 to v2 migration guide](/llamaparse/parse/guides/migration-v1-to-v2/index.md) for details on switching.

My parse job failed. How do I find out why?

Check the job status via the API or web UI — error codes and messages are returned with the job result. For common error types and solutions, see the [Troubleshooting & Error Codes](/llamaparse/general/troubleshooting/index.md) guide. If you need to investigate a specific job, the job ID can be shared with <support@runllama.ai> for further diagnosis.

## Extract

What is LlamaExtract?

LlamaExtract provides a simple API for extracting structured data from unstructured documents like PDFs, text files, and images. You define a JSON schema describing the fields you want, and LlamaExtract returns well-typed, schema-compliant data. It’s available as a [web UI](/llamaparse/extract/getting_started/web_ui/index.md), [Python SDK](/llamaparse/extract/getting_started/sdk/index.md), and [REST API](/llamaparse/extract/getting_started/api/index.md).

Are there limits on extraction schema size?

Yes. Schemas are limited to 5,000 total properties, 7 levels of nesting depth, 120,000 characters of combined string content, and 150,000 characters of raw JSON schema. For large documents, consider splitting into smaller extraction jobs. See [Schema Design and Restrictions](/llamaparse/extract/guides/schema_design/index.md) and [Limitations](/llamaparse/general/limitations/index.md) for details.

Can I parse a document once and then extract from it multiple times?

Yes. If a file was previously parsed by LlamaParse, subsequent extractions use **extract-only pricing** (lower cost). You can parse a document once and then run multiple extraction jobs with different schemas against the cached result. This composable parse-then-extract workflow is available via the SDK and REST API.

## Classify

What is LlamaClassify?

Classify lets you automatically categorize documents into types you define (e.g., invoice, receipt, contract) using natural-language rules. It’s useful as a pre-processing step before extraction, parsing, or indexing to improve accuracy and reduce cost.

What classification modes are available?

LlamaClassify offers two modes: **Fast** (1 credit/page) for text-heavy documents, and **Multimodal** (2 credits/page) for documents where layout and visual elements matter. Results include a predicted type, confidence score (0.0-1.0), and step-by-step reasoning.

Is Classify stable?

Classify is stable and generally available.

How do I use Classify with other products?

Classify is designed as a pre-processing step. Common patterns include:

- **Before Extract**: Classify documents by type (invoice vs. contract), then run different extraction schemas per type
- **Before Parse**: Classify first, then apply different parse settings per document category
- **Before Index**: Classify and route documents to appropriate indices with tailored chunking and metadata

At 1-2 credits/page, Classify is a cost-effective way to improve downstream accuracy.

## Split

What is Split?

The Split API automatically segments concatenated PDFs into logical document sections based on content categories you define. It uses AI-powered classification to analyze each page and group consecutive pages of the same category into segments.

What file formats does Split support?

Split supports PDF, DOC, DOCX, PPT, and PPTX formats. You can define up to 50 categories per job.

Is Split stable?

Split is currently in beta and is subject to breaking changes. SDK support is not yet available — all interactions use the REST API directly.

## Sheets

What is Sheets?

Sheets is a beta API for extracting regions and tables from messy spreadsheets. It intelligently identifies regions, isolates and extracts each one, and outputs them as [Parquet files](https://parquet.apache.org/docs/overview/) — a portable format that retains type information and can be loaded directly as dataframes.

How much does Sheets cost?

Sheets is currently in beta and **free to use**.

What are the limits for Sheets?

Sheets supports up to 100 columns, 10,000 rows, and 1,000,000 cells per sheet. See [Limitations](/llamaparse/general/limitations/index.md) for details.

## Index

What is Index?

Index is LlamaParse’s managed data ingestion pipeline for RAG (Retrieval Augmented Generation). Connect your [data sources](/llamaparse/cloud-index/integrations/data_sources/index.md), set your parse parameters and embedding model, and the index automatically handles syncing your data into your [vector databases](/llamaparse/cloud-index/integrations/data_sinks/index.md). It’s available through a no-code UI, REST API, and integrates with the LlamaIndex Python and TypeScript frameworks.

How much does indexing cost?

Standard indexing costs 1 credit per page (or sheet). Spreadsheet and multi-modal indexing cost 2 credits per page. See [Pricing](/llamaparse/general/pricing/index.md) for details.

What embedding models does Index support?

Index supports multiple embedding providers. You provide credentials for your preferred embedding model service (e.g. OpenAI) during index creation, and the platform handles the rest.

How long does an index sync take?

Sync time depends on the number of files and pages, image density, and text complexity. There is no fixed duration. You can monitor file processing status (SUCCESS, ERROR, PENDING) via the UI or API. For large syncs, consider using [webhooks](/llamaparse/general/webhooks/index.md) to get notified when processing completes rather than polling.
