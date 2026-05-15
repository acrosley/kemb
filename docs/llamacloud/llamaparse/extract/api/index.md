---
title: Using the REST API | Developer Documentation
description: Guide on how to use the LlamaExtract v2 REST API for programmatic data extraction, including uploading documents, running extraction jobs, and retrieving results.
---

Tip

For most use cases, we recommend using the [Python or TypeScript SDK](../sdk) instead of the REST API directly.

## Quickstart

### 1. Upload a document

Upload a document using the [Upload API](https://developers.llamaindex.ai/reference/resources/files/methods/create/).

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/files' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -F 'file=@/path/to/file' \
  -F purpose='extract'
```

Save the returned `id` (e.g. `dfl-xxxxxxxx-...`) — you’ll use it as `file_input` below.

Tip

The `file_input` field also accepts a LlamaParse job ID (`pjb-xxxxxxxx-...`). If you’ve already parsed a document with LlamaParse, you can pass the parse job ID directly to skip re-parsing and save time and credits. See the [SDK guide](../sdk#extraction-from-a-parse-job-id) or [Batch Extraction Cookbook](../examples/batch_extraction_cookbook#parse-then-extract) for examples.

### 2. Run an extraction job

Submit an extraction job with your schema and configuration inline. No agent creation needed — just provide your `data_schema` and options directly.

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v2/extract?project_id={PROJECT_ID}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -d '{
    "file_input": "{FILE_ID}",
    "configuration": {
        "tier": "agentic",
        "extraction_target": "per_doc",
        "data_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "Name of the company"
                },
                "revenue": {
                    "type": "number",
                    "description": "Annual revenue in USD"
                },
                "fiscal_year": {
                    "type": "integer",
                    "description": "Fiscal year of the report"
                }
            }
        },
        "cite_sources": true,
        "confidence_scores": false,
        "system_prompt": "Focus on the most recent fiscal year if multiple are present"
    }
}'
```

> **Tip**: The `tier` field maps to UI tiers — `cost_effective` = Cost Effective, `agentic` = Agentic. See [Tiers and versions](../#tiers-and-versions) for details.

### 3. Poll for job status

Jobs are processed asynchronously. Poll for the status using the job `id` from the response.

Terminal window

```
curl -X 'GET' \
  'https://api.cloud.llamaindex.ai/api/v2/extract/{JOB_ID}?project_id={PROJECT_ID}' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

When `status` is `COMPLETED`, the `extract_result` field contains your extracted data.

### 4. Get results with metadata

To include extraction metadata (citations, confidence scores) and usage stats, use the `expand` parameter:

Terminal window

```
curl -X 'GET' \
  'https://api.cloud.llamaindex.ai/api/v2/extract/{JOB_ID}?project_id={PROJECT_ID}&expand=extract_metadata&expand=metadata' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

## Configuration options

The `configuration` object supports many options, see the full [API reference for all configuration parameters](https://developers.llamaindex.ai/reference/resources/extract/#\(resource\)%20extract%20%3E%20\(model\)%20extract_configuration%20%3E%20\(schema\)).

## Legacy v1 API

If you need to use the v1 agent-based API, select the v1 toggle at the top of the sidebar to switch to Extract v1 documentation.

## Full API documentation

See all available endpoints in the [full API documentation](https://developers.llamaindex.ai/reference/resources/extract/).
