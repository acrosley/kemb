---
title: Using Saved Configurations | Developer Documentation
description: Save and reuse parse and extract configurations for consistent, repeatable extraction workflows.
---

Saved configurations let you define your parse and extract settings once — either in the [LlamaCloud UI](https://cloud.llamaindex.ai) or via the API — and then reference them by ID when creating extraction jobs. This is useful when you want to:

- **Standardize** extraction across your team with a shared configuration
- **Simplify** job creation by replacing inline config with a single ID
- **Decouple** parse settings from extract settings so you can mix and match
- **Iterate** on configuration in the UI playground, then use the same settings programmatically

## Concepts

There are two types of saved configurations relevant to extraction:

| Configuration Type        | Product Type | What It Controls                                                                                               |
| ------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------- |
| **Parse configuration**   | `parse_v2`   | How documents are parsed (tier, options) before extraction                                                     |
| **Extract configuration** | `extract_v2` | Full extraction settings: schema, tier, extraction target, and optionally a reference to a parse configuration |

Both are managed through the **Product Configurations API** (`/api/v1/beta/configurations`).

Tip

The easiest way to create configurations is through the LlamaCloud UI. Open the [Extract](https://cloud.llamaindex.ai/extract) or [Parse](https://cloud.llamaindex.ai/parse) playground, configure your settings, and click **Save Configuration**. Then use the configuration ID programmatically as shown below.

## Creating Configurations via the API

### Create a Parse Configuration

A parse configuration saves your LlamaParse settings so they can be reused across multiple extraction jobs.

- [Python](#tab-panel-156)
- [cURL](#tab-panel-157)

```
import os
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


# Create a saved parse configuration
# Note: configurations API is in beta and not yet available as a typed SDK resource.
# Use the raw HTTP method on the client.
parse_config = client.post(
    "/api/v1/beta/configurations",
    body={
        "name": "High Quality Parse",
        "parameters": {
            "product_type": "parse_v2",
            "version": "latest",
            "tier": "agentic",
        },
    },
    cast_to=dict,
)


print(f"Parse config ID: {parse_config['id']}")
# e.g. "cfg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/configurations?project_id={PROJECT_ID}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -d '{
    "name": "High Quality Parse",
    "parameters": {
      "product_type": "parse_v2",
      "version": "latest",
      "tier": "agentic"
    }
  }'
```

### Create an Extract Configuration

An extract configuration saves your schema, extraction tier, and other settings. You can optionally reference a saved parse configuration inside it.

- [Python](#tab-panel-158)
- [cURL](#tab-panel-159)

```
from pydantic import BaseModel, Field
from typing import Optional


# Define your extraction schema
class InvoiceData(BaseModel):
    vendor_name: str = Field(description="Name of the vendor or supplier")
    invoice_number: str = Field(description="Unique invoice identifier")
    total_amount: float = Field(description="Total amount due")
    currency: str = Field(description="Currency code (e.g. USD, EUR)")
    due_date: Optional[str] = Field(None, description="Payment due date")


# Create a saved extract configuration that references the parse config
extract_config = client.post(
    "/api/v1/beta/configurations",
    body={
        "name": "Invoice Extraction",
        "parameters": {
            "product_type": "extract_v2",
            "parse_config_id": parse_config["id"],   # Reference the parse config
            "data_schema": InvoiceData.model_json_schema(),
            "extraction_target": "per_doc",
            "tier": "agentic",
            "cite_sources": True,
        },
    },
    cast_to=dict,
)


print(f"Extract config ID: {extract_config['id']}")
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/configurations?project_id={PROJECT_ID}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -d '{
    "name": "Invoice Extraction",
    "parameters": {
      "product_type": "extract_v2",
      "parse_config_id": "{PARSE_CONFIG_ID}",
        "data_schema": {
          "type": "object",
          "properties": {
            "vendor_name": {"type": "string", "description": "Name of the vendor or supplier"},
            "invoice_number": {"type": "string", "description": "Unique invoice identifier"},
            "total_amount": {"type": "number", "description": "Total amount due"},
            "currency": {"type": "string", "description": "Currency code (e.g. USD, EUR)"},
            "due_date": {"type": "string", "description": "Payment due date", "nullable": true}
          },
          "required": ["vendor_name", "invoice_number", "total_amount", "currency"]
        },
        "extraction_target": "per_doc",
        "tier": "agentic",
        "cite_sources": true
      }
    }
  }'
```

## Running Extraction with a Saved Configuration

Once you have a saved extract configuration, you can create extraction jobs by passing just the `configuration_id` — no inline config needed.

- [Python](#tab-panel-160)
- [TypeScript](#tab-panel-161)
- [cURL](#tab-panel-162)

```
import time


# Upload a file
file_obj = client.files.create(file="./invoices/invoice_001.pdf", purpose="extract")


# Extract using the saved configuration — no inline config needed
job = client.extract.create(
    file_input=file_obj.id,
    configuration_id=extract_config["id"],
)


# Poll for completion
while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    job = client.extract.get(job.id)


if job.status == "COMPLETED":
    invoice = InvoiceData.model_validate(job.extract_result)
    print(f"Vendor: {invoice.vendor_name}")
    print(f"Total: {invoice.currency} {invoice.total_amount}")
```

```
import fs from 'fs';
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: process.env.LLAMA_CLOUD_API_KEY!,
});


// Upload a file
const fileObj = await client.files.create({
  file: fs.createReadStream('./invoices/invoice_001.pdf'),
  purpose: 'extract',
});


// Extract using the saved configuration — no inline config needed
let job = await client.extract.create({
  file_input: fileObj.id,
  configuration_id: 'cfg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', // your saved config ID
});


// Poll for completion
while (!['COMPLETED', 'FAILED', 'CANCELLED'].includes(job.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.extract.get(job.id);
}


if (job.status === 'COMPLETED') {
  console.log('Extracted:', job.extract_result);
}
```

Terminal window

```
# Extract using a saved configuration ID
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v2/extract?project_id={PROJECT_ID}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -d '{
    "file_input": "{FILE_ID}",
    "configuration_id": "{EXTRACT_CONFIG_ID}"
  }'
```

Note

`configuration_id` and `configuration` are mutually exclusive. You must provide exactly one — either a saved configuration ID or an inline configuration object, not both.

## Using parse\_config\_id with Inline Config

You don’t need a saved extract configuration to use a saved parse configuration. You can reference a `parse_config_id` directly inside an inline `configuration` block:

- [Python](#tab-panel-163)
- [TypeScript](#tab-panel-164)
- [cURL](#tab-panel-165)

```
# Use a saved parse config with an inline extract config
job = client.extract.create(
    file_input=file_obj.id,
    configuration={
        "parse_config_id": parse_config["id"],
        "data_schema": InvoiceData.model_json_schema(),
        "extraction_target": "per_doc",
        "tier": "agentic",
    },
)
```

```
// invoiceSchema defined earlier (see Create an Extract Configuration above)
let job = await client.extract.create({
  file_input: fileObj.id,
  configuration: {
    parse_config_id: 'cfg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    data_schema: invoiceSchema,
    extraction_target: 'per_doc',
    tier: 'agentic',
  },
});
```

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
      "parse_config_id": "{PARSE_CONFIG_ID}",
        "data_schema": {
          "type": "object",
          "properties": {
            "vendor_name": {"type": "string", "description": "Name of the vendor"},
            "total_amount": {"type": "number", "description": "Total amount due"}
          },
          "required": ["vendor_name", "total_amount"]
        },
        "extraction_target": "per_doc",
        "tier": "agentic"
      }
    }
  }'
```

This is useful when you want consistent parsing across jobs but need different extraction schemas for different use cases.

## Batch Processing with Saved Configurations

Saved configurations simplify batch workflows — just pass the same `configuration_id` for every file:

- [Python](#tab-panel-166)
- [TypeScript](#tab-panel-167)

```
import os
import asyncio
from pathlib import Path
from llama_cloud import AsyncLlamaCloud


async_client = AsyncLlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])
EXTRACT_CONFIG_ID = extract_config["id"]  # Your saved config ID


async def process_file(file_path: Path) -> dict:
    file_obj = await async_client.files.create(
        file=str(file_path), purpose="extract"
    )


    job = await async_client.extract.create(
        file_input=file_obj.id,
        configuration_id=EXTRACT_CONFIG_ID,
    )


    while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
        await asyncio.sleep(2)
        job = await async_client.extract.get(job.id)


    if job.status == "COMPLETED":
        return {"file": file_path.name, "data": job.extract_result}
    return {"file": file_path.name, "error": job.error_message}


async def main():
    files = list(Path("./invoices").glob("*.pdf"))
    semaphore = asyncio.Semaphore(10)


    async def bounded(path):
        async with semaphore:
            return await process_file(path)


    results = await asyncio.gather(*[bounded(f) for f in files])


    for r in results:
        if "data" in r:
            print(f"  {r['file']}: {r['data']}")
        else:
            print(f"  {r['file']}: ERROR - {r['error']}")


asyncio.run(main())
```

```
import * as fs from 'fs';
import * as path from 'path';
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: process.env.LLAMA_CLOUD_API_KEY!,
});


const EXTRACT_CONFIG_ID = 'cfg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx';


async function processFile(filePath: string) {
  const fileObj = await client.files.create({
    file: fs.createReadStream(filePath),
    purpose: 'extract',
  });


  let job = await client.extract.create({
    file_input: fileObj.id,
    configuration_id: EXTRACT_CONFIG_ID,
  });


  while (!['COMPLETED', 'FAILED', 'CANCELLED'].includes(job.status)) {
    await new Promise((r) => setTimeout(r, 2000));
    job = await client.extract.get(job.id);
  }


  return {
    file: path.basename(filePath),
    status: job.status,
    data: job.extract_result,
    error: job.error_message,
  };
}


// Process files with bounded concurrency
const filePaths = ['invoice_001.pdf', 'invoice_002.pdf', 'invoice_003.pdf'];
const concurrency = 10;


for (let i = 0; i < filePaths.length; i += concurrency) {
  const batch = filePaths.slice(i, i + concurrency);
  const results = await Promise.all(batch.map(processFile));
  results.forEach((r) => console.log(`${r.file}: ${r.status}`));
}
```

## Listing Saved Configurations

You can list your saved configurations filtered by product type:

- [Python](#tab-panel-168)
- [cURL](#tab-panel-169)

```
# List all extract configurations
extract_configs = client.get(
    "/api/v1/beta/configurations",
    cast_to=dict,
    options={"params": {"product_type": "extract_v2"}},
)
for cfg in extract_configs.get("data", []):
    print(f"  {cfg['name']} ({cfg['id']})")


# List all parse configurations
parse_configs = client.get(
    "/api/v1/beta/configurations",
    cast_to=dict,
    options={"params": {"product_type": "parse_v2"}},
)
for cfg in parse_configs.get("data", []):
    print(f"  {cfg['name']} ({cfg['id']})")
```

Terminal window

```
# List extract configurations
curl -X 'GET' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/configurations?project_id={PROJECT_ID}&product_type=extract_v2' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"


# List parse configurations
curl -X 'GET' \
  'https://api.cloud.llamaindex.ai/api/v1/beta/configurations?project_id={PROJECT_ID}&product_type=parse_v2' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

## When to Use Saved Configurations

| Scenario                                       | Approach                                                 |
| ---------------------------------------------- | -------------------------------------------------------- |
| Quick prototyping, one-off jobs                | Inline `configuration` — fastest to get started          |
| Consistent settings across many jobs           | Saved `configuration_id` — define once, use everywhere   |
| Same parse settings, different extract schemas | Saved `parse_config_id` in inline config                 |
| Team sharing a standard pipeline               | Saved `configuration_id` — everyone uses the same config |
| UI-to-code workflow                            | Configure in UI playground → save → use config ID in SDK |
