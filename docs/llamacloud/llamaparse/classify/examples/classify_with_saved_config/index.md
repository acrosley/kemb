---
title: Classify with a Saved Configuration | Developer Documentation
---

In this example, we’ll save a reusable classify configuration and use it across multiple jobs. Instead of passing inline rules every time, you create a configuration once and reference it by ID.

This is useful when you have a standard set of classification rules that you want to reuse across multiple files or integrate into an automated pipeline.

## Install

- [Python](#tab-panel-110)
- [TypeScript](#tab-panel-111)

Terminal window

```
pip install llama-cloud>=1.6
```

Terminal window

```
npm install @llamaindex/llama-cloud
```

## Create a Saved Configuration

Use the REST API to create a classify configuration with your rules. This returns a configuration ID that you can reuse.

You’ll need a [project ID](https://cloud.llamaindex.ai) — find it in the URL when viewing a project in the UI.

Terminal window

```
curl -X POST 'https://api.cloud.llamaindex.ai/api/v1/beta/configurations?project_id=YOUR_PROJECT_ID' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Invoice vs Receipt Classifier",
    "parameters": {
      "product_type": "classify_v2",
      "rules": [
        {
          "type": "invoice",
          "description": "Documents that contain an invoice number, invoice date, bill-to section, and line items with totals."
        },
        {
          "type": "receipt",
          "description": "Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page."
        }
      ],
      "mode": "FAST"
    }
  }'
```

The response includes an `id` field — this is your `configuration_id`:

```
{
  "id": "cfg-11111111-2222-3333-4444-555555555555",
  "name": "Invoice vs Receipt Classifier",
  "product_type": "classify_v2",
  ...
}
```

## Classify Using the Configuration ID

Now use the saved configuration to classify files — no need to pass rules inline.

- [Python](#tab-panel-112)
- [TypeScript](#tab-panel-113)

```
import os
import time
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


# Upload a file
file_obj = client.files.create(file="/path/to/document.pdf", purpose="classify")


# Create a classify job using the saved configuration
job = client.classify.create(
    file_id=file_obj.id,
    configuration_id="cfg-11111111-2222-3333-4444-555555555555",
)


# Poll until complete
status = client.classify.get(job.id)
while status.status == "PENDING":
    time.sleep(2)
    status = client.classify.get(job.id)


# Print result
if status.result:
    print(f"Type: {status.result.type}")
    print(f"Confidence: {status.result.confidence}")
    print(f"Reasoning: {status.result.reasoning}")
else:
    print(f"Classification failed: {status.error_message}")
```

```
import LlamaCloud from "@llamaindex/llama-cloud";
import fs from "fs";


const client = new LlamaCloud({
  apiKey: process.env.LLAMA_CLOUD_API_KEY,
});


// Upload a file
const fileObj = await client.files.create({
  file: fs.createReadStream("/path/to/document.pdf"),
  purpose: "classify",
});


// Create a classify job using the saved configuration
let job = await client.classify.create({
  file_id: fileObj.id,
  configuration_id: "cfg-11111111-2222-3333-4444-555555555555",
});


// Poll until complete
while (job.status === "PENDING") {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.classify.get(job.id);
}


// Print result
if (job.result) {
  console.log(`Type: ${job.result.type}`);
  console.log(`Confidence: ${job.result.confidence}`);
  console.log(`Reasoning: ${job.result.reasoning}`);
} else {
  console.log(`Classification failed: ${job.error_message}`);
}
```

## Update a Configuration

You can update the rules or mode of an existing configuration at any time via the REST API:

Terminal window

```
curl -X PUT 'https://api.cloud.llamaindex.ai/api/v1/beta/configurations/cfg-11111111-2222-3333-4444-555555555555?project_id=YOUR_PROJECT_ID' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "parameters": {
      "product_type": "classify_v2",
      "rules": [
        {
          "type": "invoice",
          "description": "Documents containing invoice numbers, dates, and itemized totals."
        },
        {
          "type": "receipt",
          "description": "POS receipts with merchant name, items, and total."
        },
        {
          "type": "purchase_order",
          "description": "Purchase orders with PO numbers, vendor details, and requested items."
        }
      ],
      "mode": "FAST"
    }
  }'
```

Future classify jobs using this `configuration_id` will automatically use the updated rules.

## Notes

- Use `configuration_id` instead of inline `configuration` when you want to reuse the same rules across multiple jobs.
- Configurations are scoped to your project — they are not shared across projects.
- You can also create and manage configurations from the LlamaCloud UI.
