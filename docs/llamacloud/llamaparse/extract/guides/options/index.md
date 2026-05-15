---
title: Configuration Options | Developer Documentation
description: Overview of configuration options for LlamaExtract, including extraction modes, system prompts, and extraction targets.
---

When creating a new extraction configuration, the *schema* is the most important part. However, there are a few other options that can significantly impact the extraction process.

## Schema Alignment and Extraction Target

These options determine how your schema is applied to the document:

- **Extraction Target**: Determines the scope and granularity of extraction. Available options:

  - `per_doc` (default): Schema is applied to the entire document, returns a single JSON object
  - `per_page`: Schema is applied to each page independently, returns an array of JSON objects (one per page)
  - `per_table_row`: Schema is applied to each entity in an ordered list (table rows, bulleted lists, etc.), returns an array of JSON objects (one per entity)

  See the [Core Concepts](../concepts/#extraction-target) page for detailed guidance on when to use each mode.

## Important Settings

### Tiers

In the LlamaExtract UI you choose between three tiers:

- **Cost Effective**: Lowest cost tier, optimized for speed and simpler documents where you don’t need the most advanced reasoning over layout.
- **Agentic**: Recommended default tier for most extractions. Uses stronger models and agentic reasoning for higher‑quality results on mixed‑complexity documents.
- **Agentic Plus (coming soon)**: Highest‑fidelity tier intended for very complex, high‑stakes extractions (dense tables, long reports, highly structured documents).

Under the hood these tier choices map to different extraction modes and model combinations; you usually don’t need to set those manually unless you are using the SDK or REST API directly.

### Advanced Settings

Under **Advanced Settings** in the UI you can fine-tune how extraction runs:

- **Parse tier**: Select the parsing tier used to interpret the input document before extraction. This uses the same v2 parse tiers as LlamaParse (for example, `cost_effective`, `agentic`, and `agentic_plus`). See [Tiers](/llamaparse/parse/guides/tiers/index.md) for details.
- **Cite sources**: Enable **cite sources** to attach citations to extracted fields so you can trace every value back to its origin in the document.
- **Confidence scores**: Enable **confidence scores** to get per-field confidence signals alongside extracted output.
- **System prompt**: Provide a **system prompt** to globally guide the extractor (for example, “Prefer the most recent fiscal year if multiple are present”, or “Return numbers as plain numerals without currency symbols”).

### System Prompt

- **System Prompt**: Any additional system level instructions for the extraction. Note that you should use the schema descriptions to pass field-level instructions, few-shot examples, formatting instructions, etc.

### Page Range and Context Window

- **Page Range**: Specify which pages to extract from by providing comma-separated page numbers or ranges (1-based indexing). For example, use `1,3,5-7,9` to extract pages 1, 3, pages 5 through 7, and page 9. You can also use ranges like `1-3,8-10` to extract the first three pages and pages 8 through 10. Page numbers are 1-based, meaning the first page is page 1. This option is useful when you only need to extract data from specific sections of large documents.

- **Context Window**: Number of pages to pass as context for long document extraction. This is useful when extracting from large documents where you need context from surrounding pages. This is configurable via the extraction tier and system prompt. Larger values keep more of the surrounding document intact, which helps when you need to see multi-page tables or invoices in one pass. Smaller values advance through the file more aggressively and are better when you need exhaustive coverage of dense lists.

## Metadata Extensions

For additional extraction features that provide enhanced metadata and insights, see the [**Metadata Extensions**](../extensions) page which covers:

- **Citations**: Source tracing for extracted fields
- **Reasoning**: Explanations for extraction decisions
- **Confidence Scores**: Quantitative confidence measures

These extensions return additional metadata in the `extract_metadata` field but may impact processing time.

## Setting Configuration Options

You can configure these options when creating an extraction job using either the REST API or Python SDK.

### SDKs

- [Python](#tab-panel-172)
- [TypeScript](#tab-panel-173)

First, install the Python SDK:

Terminal window

```
pip install llama-cloud>=2.1
```

Here’s how to set various configuration options:

```
import time
from llama_cloud import LlamaCloud, AsyncLlamaCloud


client = LlamaCloud(api_key="your_api_key")


schema = {
    "type": "object",
    "properties": {
        "company_name": {"type": "string", "description": "Name of the company"},
        "revenue": {"type": "number", "description": "Annual revenue in USD"}
    }
}


file_obj = client.files.create(file="path/to/your/document.pdf", purpose="extract")
file_id = file_obj.id


job = client.extract.create(
    file_input=file_id,
    configuration={
        "data_schema": schema,
        "extraction_target": "per_doc",          # per_doc, per_page, per_table_row
        "tier": "agentic",                       # cost_effective, agentic
        "system_prompt": "Focus on the most recent financial data",
        "target_pages": "1-5,10-15",             # Extract from specific pages
        "cite_sources": True,                    # Enable citations
        "confidence_scores": True,               # Enable confidence scores
    },
)


# Poll for completion
while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    job = client.extract.get(job.id)
```

First, install the TypeScript SDK:

Terminal window

```
npm install @llamaindex/llama-cloud zod
```

Here’s how to set various configuration options:

```
import fs from 'fs';
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: 'your_api_key',
});


const schema = {
  type: 'object',
  properties: {
    company_name: { type: 'string', description: 'Name of the company' },
    revenue: { type: 'number', description: 'Annual revenue in USD' },
  },
};


const fileObj = await client.files.create({
  file: fs.createReadStream('path/to/your/document.pdf'),
  purpose: 'extract',
});
const fileId = fileObj.id;


let job = await client.extract.create({
  file_input: fileId,
  configuration: {
      data_schema: schema,
      extraction_target: 'per_doc',           // per_doc, per_page, per_table_row
      tier: 'agentic',                       // cost_effective, agentic
      system_prompt: 'Focus on the most recent financial data',
      target_pages: '1-5,10-15',             // Extract from specific pages
      cite_sources: true,                    // Enable citations
      confidence_scores: true,               // Enable confidence scores
    },
});


// Poll for completion
while (!['COMPLETED', 'FAILED', 'CANCELLED'].includes(job.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.extract.get(job.id);
}
```

### REST API

You can configure these options using the REST API when creating an extraction job:

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v2/extract?project_id={PROJECT_ID}' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "file_input": "{FILE_ID}",
    "configuration": {
      "data_schema": {
        "type": "object",
        "properties": {
          "company_name": {"type": "string", "description": "Name of the company"},
          "revenue": {"type": "number", "description": "Annual revenue in USD"}
        }
      },
      "extraction_target": "per_doc",
      "tier": "agentic",
      "system_prompt": "Focus on the most recent financial data",
      "target_pages": "1-5,10-15",
      "cite_sources": true,
      "confidence_scores": true
    }
  }'
```

### Configuration Reference

| Option                     | Type    | Default     | Description                                                                  |
| -------------------------- | ------- | ----------- | ---------------------------------------------------------------------------- |
| **Schema Alignment**       |         |             |                                                                              |
| `extraction_target`        | string  | `”per_doc”` | Extraction scope: `per_doc`, `per_page`, `per_table_row`                     |
| **Tier**                   |         |             |                                                                              |
| `tier`                     | string  | `”agentic”` | Extraction tier: `cost_effective`, `agentic` (default)                       |
| **System Prompt**          |         |             |                                                                              |
| `system_prompt`            | string  | `null`      | Additional system-level instructions                                         |
| **Page Range and Context** |         |             |                                                                              |
| `target_pages`             | string  | `null`      | Comma-separated page numbers or ranges to process (1-based, e.g., “1,3,5-7”) |
| `max_pages`                | integer | `null`      | Maximum number of pages to process                                           |
| **Metadata Extensions**    |         |             |                                                                              |
| `cite_sources`             | boolean | `false`     | Enable source citations                                                      |
| `confidence_scores`        | boolean | `false`     | Enable confidence scores                                                     |
