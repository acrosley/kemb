---
title: Getting Started | Developer Documentation
description: Guide on how to use the Split REST API/SDK for automatically segmenting PDFs into logical document sections.
---

## Quickstart

### Upload a document

First, upload a PDF using the [Files API](https://developers.llamaindex.ai/reference/resources/files/).

- [Python](#tab-panel-54)
- [TypeScript](#tab-panel-55)
- [cURL](#tab-panel-56)

Install the Python SDK if you haven’t already:

Terminal window

```
pip install llama-cloud>=1.0
```

Then upload your file:

```
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")


file_obj = client.files.create(file="path/to/your/file.pdf", purpose="split")
print(file_obj.id)
```

Install the TypeScript SDK if you haven’t already:

Terminal window

```
npm install @llamaindex/llama-cloud
```

Then upload your file:

```
import fs from "fs";
import { LlamaCloud } from "@llamaindex/llama-cloud";


const client = new LlamaCloud({
  apiKey: "LLAMA_CLOUD_API_KEY",
});


const fileObj = await client.files.create({
  file: fs.createReadStream('path/to/your/file.pdf'),
  purpose: 'split',
});
console.log(fileObj.id);
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/files' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -F 'upload_file=@/path/to/your/file.pdf;type=application/pdf'
```

Save the returned `id` as your `FILE_ID`.

### Create a split job

Create a split job with your file ID and category definitions:

- [Python](#tab-panel-57)
- [TypeScript](#tab-panel-58)
- [cURL](#tab-panel-59)

```
job = await client.beta.split.create(
  categories=[
    {
      "name": "invoice",
      "description": "A commercial document requesting payment for goods or services, typically containing line items, totals, and payment terms"
    },
    {
      "name": "contract",
      "description": "A legal agreement between parties outlining terms, conditions, obligations, and signatures"
    }
  ],
  document_input={"type": "file_id", "value": file_id},
)
```

```
const job = await client.beta.split.create({
  categories: [
    {
      name: "invoice",
      description: "A commercial document requesting payment for goods or services, typically containing line items, totals, and payment terms"
    },
    {
      name: "contract",
      description: "A legal agreement between parties outlining terms, conditions, obligations, and signatures"
    }
  ],
  document_input: { type: "file_id", value: fileId },
});
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -d '{
    "document_input": {
      "type": "file_id",
      "value": "YOUR_FILE_ID"
    },
    "categories": [
      {
        "name": "invoice",
        "description": "A commercial document requesting payment for goods or services, typically containing line items, totals, and payment terms"
      },
      {
        "name": "contract",
        "description": "A legal agreement between parties outlining terms, conditions, obligations, and signatures"
      }
    ]
  }'
```

The response includes the job ID and initial status:

```
{
  "id": "spl-abc123...",
  "status": "pending"
}
```

### Poll for job completion

Jobs are processed asynchronously. Poll the status until it reaches `completed` or `failed`:

- [Python](#tab-panel-60)
- [TypeScript](#tab-panel-61)
- [cURL](#tab-panel-62)

```
completed_job = await client.beta.split.wait_for_completion(
    job.id,
    polling_interval=1.0,
    verbose=True,
)
```

```
const completedJob = await client.beta.split.waitForCompletion(
  job.id,
  { pollingInterval: 1.0, verbose: true, }
);
```

Terminal window

```
curl -X 'GET' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs/YOUR_JOB_ID' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

### Get the results

When the job completes successfully, the response includes the segmentation results:

```
{
  "id": "spl-abc123...",
  "status": "completed",
  "result": {
    "segments": [
      {
        "category": "invoice",
        "pages": [1, 2, 3],
        "confidence_category": "high"
      },
      {
        "category": "contract",
        "pages": [4, 5, 6, 7, 8],
        "confidence_category": "high"
      }
    ]
  }
}
```

Each segment contains:

- `category`: The assigned category name
- `pages`: Array of page numbers (1-indexed) belonging to this segment
- `confidence_category`: Confidence level (`high`, `medium`, or `low`)

## Advanced Options

### Uncategorized pages

By default, pages that don’t match any defined category are grouped as `uncategorized` and included in the results. You can control this behavior with the `allow_uncategorized` option in `splitting_strategy`:

| Value                 | Behavior                                                                                       |
| --------------------- | ---------------------------------------------------------------------------------------------- |
| `"include"` (default) | Pages that don’t match any category will be grouped as `uncategorized` and included in results |
| `"forbid"`            | All pages must be assigned to a defined category                                               |
| `"omit"`              | Pages that don’t match any category will not appear in results                                 |

For example, to exclude uncategorized pages from results:

- [Python](#tab-panel-63)
- [TypeScript](#tab-panel-64)
- [cURL](#tab-panel-65)

```
job = await client.beta.split.create(
  categories=[
    {
      "name": "invoice",
      "description": "A commercial document requesting payment for goods or services"
    }
  ],
  document_input={"type": "file_id", "value": file_id},
  splitting_strategy={"allow_uncategorized": "omit"}
)
```

```
const job = await client.beta.split.create({
  categories: [
    {
      name: "invoice",
      description: "A commercial document requesting payment for goods or services"
    }
  ],
  document_input: { type: "file_id", value: fileId },
  splitting_strategy: { allow_uncategorized: "omit" }
});
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -d '{
    "document_input": {
      "type": "file_id",
      "value": "YOUR_FILE_ID"
    },
    "categories": [
      {
        "name": "invoice",
        "description": "A commercial document requesting payment for goods or services"
      }
    ],
    "splitting_strategy": {
      "allow_uncategorized": "omit"
    }
  }'
```

With `"omit"`, pages that don’t match `invoice` will not appear in the response. To force all pages into defined categories instead, set `allow_uncategorized` to `"forbid"`.

### Using project IDs

If you’re working within a specific project, include the `project_id` query parameter:

- [Python](#tab-panel-66)
- [TypeScript](#tab-panel-67)
- [cURL](#tab-panel-68)

```
job = await client.beta.split.create(
  ...,
  project_id="YOUR_PROJECT_ID"
)
```

```
const job = await client.beta.split.create({
  ...,
  project_id: "YOUR_PROJECT_ID"
});
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs?project_id=YOUR_PROJECT_ID' \
  ...
```

## Full API Documentation

This is a subset of the available endpoints to help you get started.

You can see all available endpoints in our [full API documentation](https://developers.llamaindex.ai/reference/resources/beta/subresources/split/).
