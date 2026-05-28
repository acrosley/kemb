---
title: Getting Started | Developer Documentation
description: Use the client SDK to classify documents with natural-language rules, including file uploads, job polling, and reading results.
---

This guide shows how to classify documents using the SDK. You will:

- Create classification rules
- Upload files
- Submit a classify job
- Read predictions (type, confidence, reasoning)

The SDK is available in [llama-cloud-py](https://github.com/run-llama/llama-cloud-py) or [llama-cloud-ts](https://github.com/run-llama/llama-cloud-ts).

## Setup

First, [get an API key](../../general/api_key) and record it for safe keeping.

You can set this as an environment variable `LLAMA_CLOUD_API_KEY` or pass it directly to the SDK at runtime.

Then, install dependencies:

- [Python](#tab-panel-8)
- [TypeScript](#tab-panel-9)

Terminal window

```
pip install llama-cloud>=1.6
```

Terminal window

```
npm install @llamaindex/llama-cloud
```

## Quick start

Using the classify API consists of a few main steps:

1. Upload a file and get a `file_id`
2. Create a classify job with your rules
3. Wait for the job to finish
4. Read the results

The SDK provides a convenience method that handles all of these steps in one call:

- [Python](#tab-panel-10)
- [TypeScript](#tab-panel-11)

```
import os
from llama_cloud import LlamaCloud, AsyncLlamaCloud


# For async usage, use `AsyncLlamaCloud()`
client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


# Upload a file
file_obj = client.files.create(file="/path/to/doc1.pdf", purpose="classify")
file_id = file_obj.id


# Classify and wait for completion
result = client.classifier.classify(
    file_ids=[file_id],
    rules=[
        {
            "type": "invoice",
            "description": "Documents that contain an invoice number, invoice date, bill-to section, and line items with totals.",
        },
        {
            "type": "receipt",
            "description": "Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page.",
        },
    ],
    parsing_configuration={
        "lang": "en",
        "max_pages": 5,            # optional, parse at most 5 pages
        # "target_pages": "1,3",   # optional, parse only specific pages (1-based)
    },
    mode="FAST",  # or "MULTIMODAL"
)


# Print the classification results
for item in result.items:
    if item.result is None:
        print(f"Classification failed for file {item.file_id}")
        continue
    print(f"Classified type: {item.result.type}")
    print(f"Confidence: {item.result.confidence}")
    print(f"Reasoning: {item.result.reasoning}")
```

```
import LlamaCloud from '@llamaindex/llama-cloud';
import fs from 'fs';


const client = new LlamaCloud({ apiKey: process.env.LLAMA_CLOUD_API_KEY });


// Upload a file
const fileObj = await client.files.create({
    file: fs.createReadStream('/path/to/doc1.pdf'),
    purpose: "classify",
});
const fileId = fileObj.id;


// Classify and wait for completion
const result = await client.classifier.classify({
    file_ids: [fileId],
    rules: [
        {
            type: 'invoice',
            description: 'Documents that contain an invoice number, invoice date, bill-to section, and line items with totals.',
        },
        {
            type: 'receipt',
            description: 'Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page.',
        },
    ],
    parsing_configuration: {
        lang: 'en',
        max_pages: 5,
        // target_pages: "1,3",  // Optional: specific pages (1-based)
    },
    mode: 'FAST',  // or 'MULTIMODAL'
});


// Print the classification results
for (const item of result.items) {
    if (!item.result) {
        console.log(`Classification failed for file ${item.file_id}`);
        continue;
    }
    console.log(`Classified type: ${item.result.type}`);
    console.log(`Confidence: ${item.result.confidence}`);
    console.log(`Reasoning: ${item.result.reasoning}`);
}
```

## Step-by-step (manual polling)

You can also run each step individually if you need more control:

- [Python](#tab-panel-12)
- [TypeScript](#tab-panel-13)

```
import os
import time
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


# Upload a file
file_obj = client.files.create(file="/path/to/doc1.pdf", purpose="classify")
file_id = file_obj.id


# Create a classify job
job = client.classifier.jobs.create(
    file_ids=[file_id],
    rules=[
        {
            "type": "invoice",
            "description": "Documents that contain an invoice number, invoice date, bill-to section, and line items with totals.",
        },
        {
            "type": "receipt",
            "description": "Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page.",
        },
    ],
    mode="FAST",  # or "MULTIMODAL"
)


# Poll until complete
status = client.classifier.jobs.get(job.id)
while status.status == "PENDING":
    time.sleep(2)
    status = client.classifier.jobs.get(job.id)


# Fetch results
result = client.classifier.jobs.get_results(job.id)


for item in result.items:
    if item.result is None:
        print(f"Classification failed for file {item.file_id}")
        continue
    print(f"Classified type: {item.result.type}")
    print(f"Confidence: {item.result.confidence}")
    print(f"Reasoning: {item.result.reasoning}")
```

```
import LlamaCloud from '@llamaindex/llama-cloud';
import fs from 'fs';


const client = new LlamaCloud({ apiKey: process.env.LLAMA_CLOUD_API_KEY });


// Upload a file
const fileObj = await client.files.create({
    file: fs.createReadStream('/path/to/doc1.pdf'),
    purpose: "classify",
});
const fileId = fileObj.id;


// Create a classify job
const job = await client.classifier.jobs.create({
    file_ids: [fileId],
    rules: [
        {
            type: 'invoice',
            description: 'Documents that contain an invoice number, invoice date, bill-to section, and line items with totals.',
        },
        {
            type: 'receipt',
            description: 'Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page.',
        },
    ],
    mode: 'FAST',  // or 'MULTIMODAL'
});


// Wait for completion (built-in polling)
await client.classifier.jobs.waitForCompletion(job.id);


// Fetch results
const result = await client.classifier.jobs.getResults(job.id);


for (const item of result.items) {
    if (!item.result) {
        console.log(`Classification failed for file ${item.file_id}`);
        continue;
    }
    console.log(`Classified type: ${item.result.type}`);
    console.log(`Confidence: ${item.result.confidence}`);
    console.log(`Reasoning: ${item.result.reasoning}`);
}
```

## Classification modes

LlamaClassify supports two modes:

| Mode         | Credits per Page | Description                                      |
| ------------ | ---------------- | ------------------------------------------------ |
| `FAST`       | 1                | Text-based classification (default)              |
| `MULTIMODAL` | 2                | Vision-based classification for visual documents |

Use **Multimodal mode** when your documents contain images, charts, or complex layouts that are important for classification:

- [Python](#tab-panel-14)
- [TypeScript](#tab-panel-15)

```
file_obj = client.files.create(file="/path/to/visual-doc.pdf", purpose="classify")


result = client.classifier.classify(
    file_ids=[file_obj.id],
    rules=rules,
    mode="MULTIMODAL",
)
```

```
const fileObj = await client.files.create({
    file: fs.createReadStream('/path/to/visual-doc.pdf'),
    purpose: "classify",
});


const result = await client.classifier.classify({
    file_ids: [fileObj.id],
    rules,
    mode: 'MULTIMODAL',
});
```

## Notes

- Each rule requires a `type` (the label to assign) and a `description` (natural-language description of what content matches).
- `parsing_configuration` is optional. Use `lang`, `max_pages`, or `target_pages` to control how documents are parsed before classification.
- `target_pages` is a comma-separated string of 1-based page numbers or ranges (e.g., `"1,3,5-7"`).
- In cases of partial failure, some items may not have a result — always check `item.result` before accessing it.
- Job statuses: `PENDING`, `SUCCESS`, `ERROR`, `PARTIAL_SUCCESS`, `CANCELLED`.

## Tips for writing good rules

- Be specific about content features that distinguish the type.
- Include key fields the document usually contains (e.g., invoice number, total amount).
- Add multiple rules when needed to cover distinct patterns.
- Start simple, test on a small set, then refine.
