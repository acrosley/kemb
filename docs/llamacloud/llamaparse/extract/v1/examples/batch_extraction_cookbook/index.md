---
title: Production Extraction: Batch Processing, Polling, and Latency Management | Developer Documentation
---

This cookbook covers production patterns for LlamaExtract V2: extracting from single files, processing batches concurrently, composing parse-then-extract workflows, handling latency, and managing schemas programmatically.

Every example uses the V2 Extract API (`client.extract`), which accepts a `document_input_value` — either a File ID or Parse Job ID.

- [python](#tab-panel-347)
- [typescript](#tab-panel-348)

```
pip install llama-cloud<2.0
```

```
npm install @llamaindex/llama-cloud
```

## Connect to Llama Cloud

- [python](#tab-panel-349)
- [typescript](#tab-panel-350)

```
import os
from llama_cloud import LlamaCloud, AsyncLlamaCloud


client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])
```

```
import LlamaCloud from "@llamaindex/llama-cloud";


const client = new LlamaCloud({
  apiKey: process.env.LLAMA_CLOUD_API_KEY!,
});
```

## 1. Quick Start: Single File Extraction

Upload a file, define a schema, and extract structured data.

- [python](#tab-panel-351)
- [typescript](#tab-panel-352)

```
from pydantic import BaseModel, Field
from typing import Optional
import time


# Define your schema
class InvoiceData(BaseModel):
    vendor_name: str = Field(description="Name of the vendor or supplier")
    invoice_number: str = Field(description="Unique invoice identifier")
    total_amount: float = Field(description="Total amount due")
    currency: str = Field(description="Currency code (e.g. USD, EUR)")
    due_date: Optional[str] = Field(None, description="Payment due date")


# Upload the file
file_obj = client.files.create(
    file="./invoices/invoice_001.pdf",
    purpose="extract",
)


# Create an extraction job
job = client.extract.create(
    document_input_value=file_obj.id,
    config={
        "extract_options": {
            "data_schema": InvoiceData.model_json_schema(),
            "extraction_target": "per_doc",
            "tier": "cost_effective",
        },
    },
)


# Poll until complete
while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    job = client.extract.get(job.id)
    print(f"Status: {job.status}")


if job.status == "COMPLETED":
    invoice = InvoiceData.model_validate(job.extract_result)
    print(f"Vendor: {invoice.vendor_name}")
    print(f"Total: {invoice.currency} {invoice.total_amount}")
else:
    print(f"Job failed: {job.error_message}")
```

```
// Upload the file
const fileObj = await client.files.create({
  file: fs.createReadStream("./invoices/invoice_001.pdf"),
  purpose: "extract",
});


// Create an extraction job
let job = await client.extract.create({
  document_input_value: fileObj.id,
  config: {
    extract_options: {
      data_schema: {
        type: "object",
        properties: {
          vendor_name: { type: "string", description: "Name of the vendor or supplier" },
          invoice_number: { type: "string", description: "Unique invoice identifier" },
          total_amount: { type: "number", description: "Total amount due" },
          currency: { type: "string", description: "Currency code (e.g. USD, EUR)" },
          due_date: { type: "string", description: "Payment due date", nullable: true },
        },
        required: ["vendor_name", "invoice_number", "total_amount", "currency"],
      },
      extraction_target: "per_doc",
      tier: "cost_effective",
    },
  },
});


// Poll until complete
while (!["COMPLETED", "FAILED", "CANCELLED"].includes(job.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.extract.get(job.id);
  console.log(`Status: ${job.status}`);
}


if (job.status === "COMPLETED") {
  console.log("Extracted:", job.extract_result);
}
```

## 2. Batch Extraction from Multiple Documents

When you need to extract from many files, upload them all first, then create extraction jobs concurrently and poll them in parallel.

- [python](#tab-panel-353)
- [typescript](#tab-panel-354)

```
import asyncio
import time
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Optional
from llama_cloud import AsyncLlamaCloud


async_client = AsyncLlamaCloud()


class InvoiceData(BaseModel):
    vendor_name: str = Field(description="Name of the vendor or supplier")
    invoice_number: str = Field(description="Unique invoice identifier")
    total_amount: float = Field(description="Total amount due")
    currency: str = Field(description="Currency code (e.g. USD, EUR)")
    due_date: Optional[str] = Field(None, description="Payment due date")


EXTRACT_CONFIG = {
    "extract_options": {
        "data_schema": InvoiceData.model_json_schema(),
        "extraction_target": "per_doc",
        "tier": "cost_effective",
    },
}


async def upload_files(file_paths: list[Path]) -> list[str]:
    """Upload files concurrently and return file IDs."""
    async def upload_one(path: Path) -> str:
        file_obj = await async_client.files.create(
            file=str(path), purpose="extract"
        )
        return file_obj.id


    file_ids = await asyncio.gather(*[upload_one(p) for p in file_paths])
    return list(file_ids)


async def extract_one(file_id: str) -> dict:
    """Create an extract job for a single file and poll until done."""
    job = await async_client.extract.create(
        document_input_value=file_id,
        config=EXTRACT_CONFIG,
    )


    while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
        await asyncio.sleep(2)
        job = await async_client.extract.get(job.id)


    if job.status == "COMPLETED":
        return {"file_id": file_id, "data": job.extract_result}
    else:
        return {"file_id": file_id, "error": job.error_message}


async def batch_extract(file_paths: list[Path], concurrency: int = 10) -> list[dict]:
    """Extract from multiple files with bounded concurrency."""
    file_ids = await upload_files(file_paths)
    semaphore = asyncio.Semaphore(concurrency)


    async def extract_with_limit(file_id: str) -> dict:
        async with semaphore:
            return await extract_one(file_id)


    results = await asyncio.gather(
        *[extract_with_limit(fid) for fid in file_ids]
    )
    return list(results)


# Usage
async def main():
    invoice_files = list(Path("./invoices").glob("*.pdf"))
    print(f"Processing {len(invoice_files)} files...")


    results = await batch_extract(invoice_files, concurrency=10)


    succeeded = [r for r in results if "data" in r]
    failed = [r for r in results if "error" in r]
    print(f"Completed: {len(succeeded)}, Failed: {len(failed)}")


    for result in succeeded:
        invoice = InvoiceData.model_validate(result["data"])
        print(f"  {invoice.vendor_name}: {invoice.currency} {invoice.total_amount}")


asyncio.run(main())
```

```
import * as fs from "fs";
import * as path from "path";


const EXTRACT_CONFIG = {
  extract_options: {
    data_schema: {
      type: "object",
      properties: {
        vendor_name: { type: "string", description: "Name of the vendor or supplier" },
        invoice_number: { type: "string", description: "Unique invoice identifier" },
        total_amount: { type: "number", description: "Total amount due" },
        currency: { type: "string", description: "Currency code" },
      },
      required: ["vendor_name", "invoice_number", "total_amount", "currency"],
    },
    extraction_target: "per_doc" as const,
    tier: "cost_effective" as const,
  },
};


async function extractOne(fileId: string) {
  let job = await client.extract.create({
    document_input_value: fileId,
    config: EXTRACT_CONFIG,
  });


  while (!["COMPLETED", "FAILED", "CANCELLED"].includes(job.status)) {
    await new Promise((r) => setTimeout(r, 2000));
    job = await client.extract.get(job.id);
  }


  return { fileId, status: job.status, data: job.extract_result, error: job.error_message };
}


async function batchExtract(filePaths: string[], concurrency = 10) {
  // Upload all files
  const fileIds = await Promise.all(
    filePaths.map(async (fp) => {
      const fileObj = await client.files.create({
        file: fs.createReadStream(fp),
        purpose: "extract",
      });
      return fileObj.id;
    })
  );


  // Extract with bounded concurrency
  const results: any[] = [];
  for (let i = 0; i < fileIds.length; i += concurrency) {
    const batch = fileIds.slice(i, i + concurrency);
    const batchResults = await Promise.all(batch.map(extractOne));
    results.push(...batchResults);
  }
  return results;
}
```

### Rate Limiting Considerations

- **Concurrency**: Start with 10 concurrent jobs and adjust based on your plan limits. If you see `THROTTLED` status, reduce concurrency.
- **Credits**: `cost_effective` tier costs 4 credits per page. `agentic` tier costs 15 credits per page. Plan your budget for large batches.
- **File upload**: The file upload endpoint has its own rate limits. Upload files before creating extract jobs to separate the two bottlenecks.

## 3. Parse-Then-Extract: Composable Workflow

When you need fine-grained control over parsing, or want to parse once and extract with different schemas, use the parse-then-extract pattern. Parse the document first, then pass the `parse_job_id` to extraction.

This avoids re-parsing the same document for each extraction configuration, saving both time and credits.

- [python](#tab-panel-355)
- [typescript](#tab-panel-356)

```
from pydantic import BaseModel, Field
from typing import Optional
import time


# Step 1: Parse the document
parse_job = client.parsing.create(
    tier="agentic",
    version="latest",
    upload_file="./contracts/master_agreement.pdf",
)


# Wait for parse to complete
parse_result = client.parsing.wait_for_completion(
    parse_job.id, verbose=True
)
print(f"Parse complete: {parse_result.status}")


# Step 2: Extract with the first schema (contract metadata)
class ContractMetadata(BaseModel):
    parties: list[str] = Field(description="Names of all contracting parties")
    effective_date: str = Field(description="Contract effective date")
    termination_date: Optional[str] = Field(None, description="Contract end date")
    governing_law: str = Field(description="Governing law jurisdiction")


metadata_job = client.extract.create(
    document_input_value=parse_job.id,
    config={
        "extract_options": {
            "data_schema": ContractMetadata.model_json_schema(),
            "extraction_target": "per_doc",
            "tier": "agentic",
            "cite_sources": True,
        },
    },
)


while metadata_job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    metadata_job = client.extract.get(metadata_job.id)


metadata = ContractMetadata.model_validate(metadata_job.extract_result)
print(f"Parties: {metadata.parties}")
print(f"Governing law: {metadata.governing_law}")


# Step 3: Extract with a second schema (financial terms) from the SAME parse
class FinancialTerms(BaseModel):
    total_value: Optional[float] = Field(None, description="Total contract value")
    payment_schedule: Optional[str] = Field(None, description="Payment frequency and terms")
    penalties: Optional[str] = Field(None, description="Late payment or breach penalties")


financial_job = client.extract.create(
    document_input_value=parse_job.id,  # Reuse the same parse result
    config={
        "extract_options": {
            "data_schema": FinancialTerms.model_json_schema(),
            "extraction_target": "per_doc",
            "tier": "agentic",
        },
    },
)


while financial_job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    financial_job = client.extract.get(financial_job.id)


terms = FinancialTerms.model_validate(financial_job.extract_result)
print(f"Contract value: {terms.total_value}")
print(f"Payment schedule: {terms.payment_schedule}")
```

```
// Step 1: Parse the document
let parseJob = await client.parsing.create({
  tier: "agentic",
  version: "latest",
  upload_file: fs.createReadStream("./contracts/master_agreement.pdf"),
});


// Wait for parse to complete
parseJob = await client.parsing.waitForCompletion(parseJob.id);
console.log(`Parse complete: ${parseJob.status}`);


// Step 2: Extract contract metadata from parse result
let metadataJob = await client.extract.create({
  document_input_value: parseJob.id,
  config: {
    extract_options: {
      data_schema: {
        type: "object",
        properties: {
          parties: { type: "array", items: { type: "string" }, description: "Names of all contracting parties" },
          effective_date: { type: "string", description: "Contract effective date" },
          governing_law: { type: "string", description: "Governing law jurisdiction" },
        },
        required: ["parties", "effective_date", "governing_law"],
      },
      extraction_target: "per_doc",
      tier: "agentic",
      cite_sources: true,
    },
  },
});


while (!["COMPLETED", "FAILED", "CANCELLED"].includes(metadataJob.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  metadataJob = await client.extract.get(metadataJob.id);
}
console.log("Contract metadata:", metadataJob.extract_result);


// Step 3: Extract financial terms from the SAME parse result
let financialJob = await client.extract.create({
  document_input_value: parseJob.id, // Reuse the same parse result
  config: {
    extract_options: {
      data_schema: {
        type: "object",
        properties: {
          total_value: { type: "number", description: "Total contract value", nullable: true },
          payment_schedule: { type: "string", description: "Payment frequency and terms", nullable: true },
        },
      },
      extraction_target: "per_doc",
      tier: "agentic",
    },
  },
});


while (!["COMPLETED", "FAILED", "CANCELLED"].includes(financialJob.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  financialJob = await client.extract.get(financialJob.id);
}
console.log("Financial terms:", financialJob.extract_result);
```

### Page Targeting

Extract from specific pages using `target_pages`. This is useful for long documents where you only need data from certain pages.

- [python](#tab-panel-357)
- [typescript](#tab-panel-358)

```
job = client.extract.create(
    document_input_value=file_obj.id,
    config={
        "extract_options": {
            "data_schema": InvoiceData.model_json_schema(),
            "extraction_target": "per_doc",
            "tier": "cost_effective",
            "target_pages": "1,3,5-7",  # Pages 1, 3, 5, 6, 7
        },
    },
)
```

```
const job = await client.extract.create({
  document_input_value: fileObj.id,
  config: {
    extract_options: {
      data_schema: invoiceSchema,
      extraction_target: "per_doc",
      tier: "cost_effective",
      target_pages: "1,3,5-7", // Pages 1, 3, 5, 6, 7
    },
  },
});
```

Pages are 1-indexed. Supported formats: `"1"`, `"1,3"`, `"1-5"`, `"1,3,5-7,9"`. You are only billed for pages extracted.

### Fetching Metadata with Expand

By default, `extract_metadata` (usage stats, citations, field-level confidence) is not included in the response. Use the `expand` query parameter to request it.

- [python](#tab-panel-359)
- [typescript](#tab-panel-360)

```
# Get job with metadata
job = client.extract.get(job.id, expand=["extract_metadata"])


if job.extract_metadata:
    usage = job.extract_metadata.usage
    print(f"Pages extracted: {usage.num_pages_extracted}")
    print(f"Output tokens: {usage.num_output_tokens}")
```

```
// Get job with metadata
const job = await client.extract.get(jobId, {
  expand: ["extract_metadata"],
});


if (job.extract_metadata?.usage) {
  console.log(`Pages extracted: ${job.extract_metadata.usage.num_pages_extracted}`);
}
```

### When to Use Parse-Then-Extract

| Scenario                                        | Approach                                                                               |
| ----------------------------------------------- | -------------------------------------------------------------------------------------- |
| One file, one schema                            | Use `document_input_value` with file ID directly                                       |
| One file, multiple schemas                      | Parse once, then extract with each schema via `document_input_value` with parse job ID |
| Need to inspect parse quality before extracting | Parse first, review, then extract                                                      |
| Batch of files with same schema                 | Use file ID with batch pattern from Section 2                                          |
| Only need specific pages                        | Add `target_pages` to `extract_options`                                                |

## 4. Handling Latency

### Expected Latency and Cost by Tier

| Tier             | Credits/Page | Typical Latency | Best For                           |
| ---------------- | ------------ | --------------- | ---------------------------------- |
| `cost_effective` | 4            | 5-30 seconds    | High-volume, simpler documents     |
| `agentic`        | 15           | 15-90 seconds   | Complex documents, higher accuracy |

Latency scales with document length. A 100-page PDF on the `agentic` tier will take longer than a 2-page invoice.

### Client-Side Timeout Pattern

Wrap your polling loop with a timeout to avoid waiting indefinitely.

- [python](#tab-panel-361)
- [typescript](#tab-panel-362)

```
import time


def extract_with_timeout(
    client,
    file_id: str,
    config: dict,
    timeout_seconds: float = 300,
    poll_interval: float = 2.0,
) -> dict:
    """Extract with a client-side timeout."""
    job = client.extract.create(
        document_input_value=file_id,
        config=config,
    )


    start = time.monotonic()
    while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
        elapsed = time.monotonic() - start
        if elapsed > timeout_seconds:
            raise TimeoutError(
                f"Extraction job {job.id} did not complete within "
                f"{timeout_seconds}s (last status: {job.status})"
            )
        time.sleep(poll_interval)
        job = client.extract.get(job.id)


    if job.status != "COMPLETED":
        raise RuntimeError(f"Job {job.id} ended with status: {job.status} - {job.error_message}")


    return job.extract_result


# Usage
try:
    result = extract_with_timeout(
        client,
        file_id=file_obj.id,
        config=EXTRACT_CONFIG,
        timeout_seconds=120,
    )
    print("Extracted:", result)
except TimeoutError as e:
    print(f"Timed out: {e}")
except RuntimeError as e:
    print(f"Failed: {e}")
```

```
async function extractWithTimeout(
  fileId: string,
  config: any,
  timeoutMs: number = 300_000,
  pollIntervalMs: number = 2_000
) {
  let job = await client.extract.create({
    document_input_value: fileId,
    config,
  });


  const start = Date.now();
  while (!["COMPLETED", "FAILED", "CANCELLED"].includes(job.status)) {
    if (Date.now() - start > timeoutMs) {
      throw new Error(
        `Job ${job.id} did not complete within ${timeoutMs}ms (last status: ${job.status})`
      );
    }
    await new Promise((r) => setTimeout(r, pollIntervalMs));
    job = await client.extract.get(job.id);
  }


  if (job.status !== "COMPLETED") {
    throw new Error(`Job ${job.id} failed: ${job.status} - ${job.error_message}`);
  }
  return job.extract_result;
}
```

### Understanding THROTTLED Status

When the system is under load, your job may enter `THROTTLED` status before transitioning to `RUNNING`. This is normal. The job will proceed once capacity is available. Do not cancel and retry throttled jobs. That creates more load and pushes your job to the back of the queue.

```
PENDING → THROTTLED → RUNNING → COMPLETED
```

### Webhook Integration (Alternative to Polling)

For production systems where you don’t want long-lived polling connections, configure webhooks to receive notifications when jobs complete.

- [python](#tab-panel-363)
- [typescript](#tab-panel-364)

```
job = client.extract.create(
    document_input_value=file_obj.id,
    config=EXTRACT_CONFIG,
    webhook_configurations=[
        {
            "webhook_url": "https://your-api.example.com/webhooks/extract",
            "webhook_events": ["extract.success", "extract.error"],
            "webhook_headers": {
                "Authorization": "Bearer your-webhook-secret",
            },
        }
    ],
)


# No polling needed. Your webhook endpoint receives:
# POST https://your-api.example.com/webhooks/extract
# {
#   "event": "extract.success",
#   "job_id": "...",
#   "status": "COMPLETED",
#   ...
# }
```

```
const job = await client.extract.create({
  document_input_value: fileObj.id,
  config: EXTRACT_CONFIG,
  webhook_configurations: [
    {
      webhook_url: "https://your-api.example.com/webhooks/extract",
      webhook_events: ["extract.success", "extract.error"],
      webhook_headers: {
        Authorization: "Bearer your-webhook-secret",
      },
    },
  ],
});


// Your webhook endpoint receives a POST when the job completes
```

## 5. Schema Management

### Generate a Schema from a Prompt

Don’t want to write JSON schema by hand? Describe what you need in plain English and let the API generate a schema.

- [python](#tab-panel-365)
- [typescript](#tab-panel-366)

```
generated = client.extract.generate_schema(
    prompt="Extract the company name, CEO name, founding year, and headquarters city from this annual report",
)


print("Generated schema:", generated.data_schema)
print("Suggested config name:", generated.name)


# Use the generated schema directly in an extraction job
job = client.extract.create(
    document_input_value=file_obj.id,
    config={
        "extract_options": {
            "data_schema": generated.data_schema,
            "extraction_target": "per_doc",
            "tier": "cost_effective",
        },
    },
)
```

```
const generated = await client.extract.generateSchema({
  prompt: "Extract the company name, CEO name, founding year, and headquarters city from this annual report",
});


console.log("Generated schema:", generated.data_schema);


const job = await client.extract.create({
  document_input_value: fileObj.id,
  config: {
    extract_options: {
      data_schema: generated.data_schema,
      extraction_target: "per_doc",
      tier: "cost_effective",
    },
  },
});
```

### Generate a Schema from a Sample File

Upload a representative file and let the API analyze it to suggest a schema.

- [python](#tab-panel-367)
- [typescript](#tab-panel-368)

```
sample_file = client.files.create(
    file="./invoices/sample_invoice.pdf",
    purpose="extract",
)


generated = client.extract.generate_schema(
    file_id=sample_file.id,
    prompt="Extract all invoice fields including line items",
)


print("Generated schema:", generated.data_schema)
```

```
const sampleFile = await client.files.create({
  file: fs.createReadStream("./invoices/sample_invoice.pdf"),
  purpose: "extract",
});


const generated = await client.extract.generateSchema({
  file_id: sampleFile.id,
  prompt: "Extract all invoice fields including line items",
});


console.log("Generated schema:", generated.data_schema);
```

### Validate a Schema Before Use

Catch schema errors before running extraction jobs.

- [python](#tab-panel-369)
- [typescript](#tab-panel-370)

```
from pydantic import BaseModel, Field


class MySchema(BaseModel):
    name: str = Field(description="Person's full name")
    age: int = Field(description="Person's age in years")


validation = client.extract.validate_schema(
    data_schema=MySchema.model_json_schema(),
)


if validation.valid:
    print("Schema is valid")
else:
    print(f"Schema errors: {validation.errors}")
```

```
const validation = await client.extract.validateSchema({
  data_schema: {
    type: "object",
    properties: {
      name: { type: "string", description: "Person's full name" },
      age: { type: "integer", description: "Person's age in years" },
    },
    required: ["name", "age"],
  },
});


if (validation.valid) {
  console.log("Schema is valid");
} else {
  console.log("Schema errors:", validation.errors);
}
```

## Putting It All Together

Here’s a complete production script that combines batch upload, parse-then-extract, timeout handling, and result collection.

- [python](#tab-panel-371)
- [typescript](#tab-panel-372)

```
import asyncio
import time
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Optional
from llama_cloud import AsyncLlamaCloud


async_client = AsyncLlamaCloud()


class ContractSummary(BaseModel):
    parties: list[str] = Field(description="Names of all contracting parties")
    effective_date: str = Field(description="Contract effective date")
    contract_type: str = Field(description="Type of contract (NDA, MSA, SOW, etc.)")
    total_value: Optional[float] = Field(None, description="Total contract value if specified")


EXTRACT_CONFIG = {
    "extract_options": {
        "data_schema": ContractSummary.model_json_schema(),
        "extraction_target": "per_doc",
        "tier": "agentic",
        "cite_sources": True,
    },
}


async def process_contract(file_path: Path, timeout: float = 300) -> dict:
    """Parse, then extract from a single contract with timeout."""
    # Upload
    file_obj = await async_client.files.create(
        file=str(file_path), purpose="extract"
    )


    # Parse first for higher quality
    parse_job = await async_client.parsing.create(
        tier="agentic",
        version="latest",
        file_id=file_obj.id,
    )
    parse_job = await async_client.parsing.wait_for_completion(
        parse_job.id, timeout=timeout
    )


    # Extract from parse result
    job = await async_client.extract.create(
        document_input_value=parse_job.id,
        config=EXTRACT_CONFIG,
    )


    start = time.monotonic()
    while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
        if time.monotonic() - start > timeout:
            return {"file": file_path.name, "error": f"Timeout after {timeout}s"}
        await asyncio.sleep(2)
        job = await async_client.extract.get(job.id)


    if job.status == "COMPLETED":
        return {
            "file": file_path.name,
            "data": job.extract_result,
            # Note: extract_metadata requires ?expand=extract_metadata on GET
        }
    return {"file": file_path.name, "error": job.error_message}


async def main():
    contracts = list(Path("./contracts").glob("*.pdf"))
    semaphore = asyncio.Semaphore(5)


    async def bounded(path):
        async with semaphore:
            return await process_contract(path)


    results = await asyncio.gather(*[bounded(p) for p in contracts])


    for r in results:
        if "data" in r:
            summary = ContractSummary.model_validate(r["data"])
            print(f"{r['file']}: {summary.contract_type} between {', '.join(summary.parties)}")
        else:
            print(f"{r['file']}: ERROR - {r['error']}")


asyncio.run(main())
```

```
import * as fs from "fs";
import * as path from "path";


const EXTRACT_CONFIG = {
  extract_options: {
    data_schema: {
      type: "object",
      properties: {
        parties: { type: "array", items: { type: "string" }, description: "Contracting parties" },
        effective_date: { type: "string", description: "Contract effective date" },
        contract_type: { type: "string", description: "Type of contract (NDA, MSA, SOW, etc.)" },
        total_value: { type: "number", description: "Total contract value", nullable: true },
      },
      required: ["parties", "effective_date", "contract_type"],
    },
    extraction_target: "per_doc" as const,
    tier: "agentic" as const,
    cite_sources: true,
  },
};


async function processContract(filePath: string, timeoutMs = 300_000) {
  const fileObj = await client.files.create({
    file: fs.createReadStream(filePath),
    purpose: "extract",
  });


  // Parse first
  let parseJob = await client.parsing.create({
    tier: "agentic",
    version: "latest",
    file_id: fileObj.id,
  });
  parseJob = await client.parsing.waitForCompletion(parseJob.id);


  // Extract from parse result
  let job = await client.extract.create({
    document_input_value: parseJob.id,
    config: EXTRACT_CONFIG,
  });


  const start = Date.now();
  while (!["COMPLETED", "FAILED", "CANCELLED"].includes(job.status)) {
    if (Date.now() - start > timeoutMs) {
      return { file: path.basename(filePath), error: "Timeout" };
    }
    await new Promise((r) => setTimeout(r, 2000));
    job = await client.extract.get(job.id);
  }


  if (job.status === "COMPLETED") {
    return { file: path.basename(filePath), data: job.extract_result };
  }
  return { file: path.basename(filePath), error: job.error_message };
}
```

## What’s Next?

- [Extract Data with Citations and Reasoning](../examples/extract_data_with_citations) for inspecting extraction provenance
- [Auto-Generate Schema for Extraction](../examples/auto_generate_schema_for_extraction) for more schema generation patterns
- [Extract Repeating Entities](../examples/extract_repeating_entities) for table row extraction
- [LlamaExtract Documentation](https://developers.llamaindex.ai/llamaparse/extract/getting_started) for the full API reference
