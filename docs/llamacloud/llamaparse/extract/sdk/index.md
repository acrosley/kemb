---
title: Getting Started | Developer Documentation
description: Guide on how to use the LlamaExtract SDK for programmatic data extraction, including schema definition and batch processing.
---

For a more programmatic approach, the SDK is the recommended way to experiment with different schemas and run extractions at scale.

Note

The examples below use the **v2** Extract SDK (`llama-cloud`). If you need to use **Extract v1**, switch to the v1 documentation using the toggle at the top of the left sidebar.

You can visit the Github repo for the [Python SDK](https://github.com/run-llama/llama-cloud-py) or the [Typescript SDK](https://github.com/run-llama/llama-cloud-ts).

First, [get an api key](../../general/api_key). You can export it as an environment variable for easy access or pass it directly to clients later.

Terminal window

```
export LLAMA_CLOUD_API_KEY=llx-xxxxxx
```

Then, install dependencies:

- [Python](#tab-panel-16)
- [TypeScript](#tab-panel-17)

Terminal window

```
pip install llama-cloud>=2.1
```

Terminal window

```
npm install @llamaindex/llama-cloud zod
```

Now we have our libraries and our API key available, let’s create a script file and extract data from files. In this case, we’re using some sample [resumes](https://github.com/run-llama/llama_cloud_services/tree/main/examples/extract/data) from our example:

## Quick Start

- [Python](#tab-panel-18)
- [TypeScript](#tab-panel-19)

```
import time
from pydantic import BaseModel, Field
from llama_cloud import LlamaCloud


# Define schema using Pydantic
class Resume(BaseModel):
    name: str = Field(description="Full name of candidate")
    email: str = Field(description="Email address")
    skills: list[str] = Field(description="Technical skills and technologies")


client = LlamaCloud(api_key="your_api_key")


# Upload a file to extract from
file_obj = client.files.create(file="resume.pdf", purpose="extract")


# Extract data from document
job = client.extract.create(
    file_input=file_obj.id,
    configuration={
        "data_schema": Resume.model_json_schema(),
        "extraction_target": "per_doc",
        "tier": "agentic",
    },
)


# Poll for completion
while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    job = client.extract.get(job.id)


print(job.extract_result)
```

```
import fs from 'fs';
import { z } from 'zod';
import LlamaCloud from '@llamaindex/llama-cloud';


// Define schema using Zod
const ResumeSchema = z.object({
    name: z.string().describe("Full name of candidate"),
    email: z.string().describe("Email address"),
    skills: z.array(z.string()).describe("Technical skills and technologies"),
});


const client = new LlamaCloud({
  apiKey: 'your_api_key',
});


// Upload a file to extract from
const fileObj = await client.files.create({
  file: fs.createReadStream('resume.pdf'),
  purpose: 'extract',
});


// Extract data from document
let job = await client.extract.create({
  file_input: fileObj.id,
  configuration: {
      data_schema: z.toJSONSchema(ResumeSchema),
      extraction_target: 'per_doc',
      tier: 'agentic',
  },
});


// Poll for completion
while (!['COMPLETED', 'FAILED', 'CANCELLED'].includes(job.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.extract.get(job.id);
}


console.log(job.extract_result);
```

Run your script to see the extracted result!

## Defining Schemas

Schemas can be defined using either Pydantic/Zod models or JSON Schema. Refer to the [Schemas](../guides/schema_design) page for more details.

## Other Extraction APIs

### Extraction over bytes or text

You can also call extraction directly over raw text.

- [Python](#tab-panel-20)
- [TypeScript](#tab-panel-21)

```
import io
import time
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="your_api_key")


source_text = "Candidate Name: Jane Doe\nEmail: jane.doe@example.com"
source_buffer = io.BytesIO(source_text.encode('utf-8'))


file_obj = client.files.create(file=source_buffer, purpose="extract", external_file_id="resume.txt")


job = client.extract.create(
    file_input=file_obj.id,
    configuration={
        "data_schema": Resume.model_json_schema(),
        "extraction_target": "per_doc",
        "tier": "agentic",
    },
)


while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    job = client.extract.get(job.id)
```

```
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: 'your_api_key',
});


const sourceText = 'Candidate Name: Jane Doe\nEmail: jane.doe@example.com';


const fileObj = await client.files.create({
  file: Buffer.from(sourceText, 'utf-8'),
  purpose: 'extract',
  external_file_id: 'resume.txt',
});


let job = await client.extract.create({
  file_input: fileObj.id,
  configuration: {
      data_schema: z.toJSONSchema(ResumeSchema),
      extraction_target: 'per_doc',
      tier: 'agentic',
  },
});


while (!['COMPLETED', 'FAILED', 'CANCELLED'].includes(job.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.extract.get(job.id);
}
```

### Extraction from a Parse Job ID

If you’ve already parsed a document with LlamaParse, you can pass the parse job ID directly to extraction instead of uploading the file again. This skips re-parsing, saving both time and credits. It’s especially useful when you want to extract with multiple schemas from the same document.

- [Python](#tab-panel-22)
- [TypeScript](#tab-panel-23)

```
import time
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="your_api_key")


# Step 1: Parse the document once
parse_job = client.parsing.create(
    tier="agentic",
    version="latest",
    upload_file="./document.pdf",
)
parse_result = client.parsing.wait_for_completion(parse_job.id, verbose=True)


# Step 2: Extract using the parse job ID (no re-upload needed)
job = client.extract.create(
    file_input=parse_job.id,  # e.g. "pjb-xxxxxxxx-..."
    configuration={
        "data_schema": Resume.model_json_schema(),
        "extraction_target": "per_doc",
        "tier": "agentic",
    },
)


# Poll for completion
while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    job = client.extract.get(job.id)


print(job.extract_result)
```

```
import fs from 'fs';
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({ apiKey: 'your_api_key' });


// Step 1: Parse the document once
let parseJob = await client.parsing.create({
  tier: 'agentic',
  version: 'latest',
  upload_file: fs.createReadStream('./document.pdf'),
});
parseJob = await client.parsing.waitForCompletion(parseJob.id);


// Step 2: Extract using the parse job ID (no re-upload needed)
let job = await client.extract.create({
  file_input: parseJob.id,  // e.g. "pjb-xxxxxxxx-..."
  configuration: {
      data_schema: z.toJSONSchema(ResumeSchema),
      extraction_target: 'per_doc',
      tier: 'agentic',
  },
});


// Poll for completion
while (!['COMPLETED', 'FAILED', 'CANCELLED'].includes(job.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.extract.get(job.id);
}


console.log(job.extract_result);
```

The `file_input` field accepts either a file ID (`dfl-...`) or a parse job ID (`pjb-...`). For a more detailed example including extracting with multiple schemas from the same parse result, see the [Batch Extraction Cookbook](../examples/batch_extraction_cookbook#parse-then-extract).

### Batch Processing

Process multiple files asynchronously:

- [Python](#tab-panel-24)
- [TypeScript](#tab-panel-25)

We can submit multiple files for extraction using concurrency control with a semaphore:

```
import asyncio
from llama_cloud import AsyncLlamaCloud


client = AsyncLlamaCloud(api_key="your_api_key")
semaphore = asyncio.Semaphore(5)  # Limit concurrency


EXTRACT_CONFIG = {
    "data_schema": Resume.model_json_schema(),
    "extraction_target": "per_doc",
    "tier": "agentic",
}


async def process_path(file_path: str):
    async with semaphore:
        file_obj = await client.files.create(file=file_path, purpose="extract")


        job = await client.extract.create(
            file_input=file_obj.id,
            configuration=EXTRACT_CONFIG,
        )


        while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
            await asyncio.sleep(2)
            job = await client.extract.get(job.id)


    return job.extract_result


async def main():
    file_paths = ["resume1.pdf", "resume2.pdf", "resume3.pdf"]
    results = await asyncio.gather(*(process_path(path) for path in file_paths))
    return results


asyncio.run(main())
```

We can submit multiple files for extraction using concurrency control with a semaphore:

```
import fs from 'fs';
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: 'your_api_key',
});


const extractConfig = {
    data_schema: z.toJSONSchema(ResumeSchema),
    extraction_target: 'per_doc',
    tier: 'agentic',
};


// npm install async-mutex for Semaphore, or use p-limit
const semaphore = new Semaphore(5);


async function processPath(filePath: string) {
  await semaphore.acquire();
  try {
    const fileObj = await client.files.create({
      file: fs.createReadStream(filePath),
      purpose: 'extract',
    });


    let job = await client.extract.create({
      file_input: fileObj.id,
      configuration: extractConfig,
    });


    while (!['COMPLETED', 'FAILED', 'CANCELLED'].includes(job.status)) {
      await new Promise((r) => setTimeout(r, 2000));
      job = await client.extract.get(job.id);
    }


    return job.extract_result;
  } finally {
    semaphore.release();
  }
}


const filePaths = ["resume1.pdf", "resume2.pdf", "resume3.pdf"];
const results = await Promise.all(filePaths.map(processPath));
```

### Schema Generation

You can use the SDK to auto-generate a JSON schema from a prompt or a sample file:

- [Python](#tab-panel-26)
- [TypeScript](#tab-panel-27)

```
# Generate schema from a prompt
generated = client.extract.generate_schema(
    prompt="Extract company financials including revenue, net income, and fiscal year",
)


# Generate schema from a sample file
file_obj = client.files.create(file="sample_report.pdf", purpose="extract")
generated = client.extract.generate_schema(
    file_id=file_obj.id,
    prompt="Extract key financial data",
)


# Use the generated schema in an extraction
job = client.extract.create(
    file_input=file_obj.id,
    configuration={
        "data_schema": generated.parameters.data_schema,
        "tier": "agentic",
    },
)
```

```
// Generate schema from a prompt
const schema = await client.extract.generateSchema({
  prompt: 'Extract company financials including revenue, net income, and fiscal year',
});


// Generate schema from a sample file
const fileObj = await client.files.create({
  file: fs.createReadStream('sample_report.pdf'),
  purpose: 'extract',
});
const schemaFromFile = await client.extract.generateSchema({
  file_id: fileObj.id,
  prompt: 'Extract key financial data',
});


// Use the generated schema in an extraction
let job = await client.extract.create({
  file_input: fileObj.id,
  configuration: {
      data_schema: schema,
      tier: 'agentic',
  },
});
```
