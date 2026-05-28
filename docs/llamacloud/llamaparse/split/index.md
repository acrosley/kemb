---
title: Overview of Split | Developer Documentation
description: Introduction to the Split API, a tool for automatically segmenting concatenated PDFs into logical document sections based on content categories.
---

Using a coding agent?

Give your AI agent access to these docs: `claude mcp add llama-index-docs --transport http https://developers.llamaindex.ai/mcp` — [More options](/python/shared/mcp/index.md)

## Overview

The Split API provides a simple way to automatically segment concatenated PDFs into logical document sections based on content categories. Using AI-powered classification, it analyzes each page’s content, classifies pages into user-defined categories, and groups consecutive pages of the same category into segments.

Split is currently in beta and is subject to breaking changes. SDK support is not yet available—all interactions use the REST API directly.

### Is Split right for me?

Split is a great fit when you need:

- **Document separation**: Automatically separate bundled documents (e.g., a collection of reports, research papers, or contracts) before further processing
- **Content organization**: Categorize and organize mixed document collections by type
- **Pre-processing for extraction**: Identify different document types within a single file before running targeted extraction with LlamaExtract
- **Flexible categorization**: Define any categories relevant to your use case with natural-language descriptions

### Key Features

- **AI-powered classification**: Uses LLMs to understand page content and assign categories
- **Flexible categories**: Define any categories relevant to your use case
- **Confidence scoring**: Each segment includes a confidence level (high, medium, low)
- **Page-level granularity**: Results include exact page numbers for each segment
- **Uncategorized handling**: Optionally capture pages that don’t match any defined category

## Quick Start

### Get an API key

First, [get an API key](../general/api_key) to use the Split API.

### API/SDK Usage

Check out the [Getting Started guide](./getting_started) for a complete walkthrough.

### Typical Flow

1. **Upload your PDF** to LlamaCloud using the Files API
2. **Define categories** with names and natural-language descriptions
3. **Create a split job** with your file and categories
4. **Poll for completion** until the job finishes
5. **Retrieve results** with segments, page ranges, and confidence scores

## Pricing

See [Pricing](../general/pricing/#split) for credit rates and billing details.

## API Reference

- **Create Split Job**: `POST /api/v1/beta/split/jobs`
- **Get Split Job**: `GET /api/v1/beta/split/jobs/{job_id}`
- **List Split Jobs**: `GET /api/v1/beta/split/jobs`

For the complete API reference, see our [API documentation](https://developers.llamaindex.ai/reference/resources/beta/subresources/split/).
