---
title: SDK Usage | Developer Documentation
description: Guide on how to use the LlamaExtract SDK for programmatic data extraction, including schema definition and batch processing.
---

For a more programmatic approach, the SDK is the recommended way to experiment with different schemas and run extractions at scale.

You can visit the Github repo for the [Python SDK](https://github.com/run-llama/llama-cloud-py) or the [Typescript SDK](https://github.com/run-llama/llama-cloud-ts).

First, [get an api key](../../../../general/api_key). You can export it as an environment variable for easy access or pass it directly to clients later.

Terminal window

```
export LLAMA_CLOUD_API_KEY=llx-xxxxxx
```

Then, install dependencies:

- [Python](#tab-panel-408)
- [TypeScript](#tab-panel-409)
- [Python (legacy)](#tab-panel-410)

Terminal window

```
pip install llama-cloud<2.0
```

Terminal window

```
npm install @llamaindex/llama-cloud zod
```

Terminal window

```
pip install llama-cloud-services python-dotenv
```

Now we have our libraries and our API key available, let’s create a script file and extract data from files. In this case, we’re using some sample [resumes](https://github.com/run-llama/llama_cloud_services/tree/main/examples/extract/data) from our example:

## Quick Start

- [Python](#tab-panel-411)
- [TypeScript](#tab-panel-412)
- [Python (legacy)](#tab-panel-413)

```
from pydantic import BaseModel, Field
from llama_cloud import LlamaCloud, AsyncLlamaCloud


# Define schema using Pydantic
class Resume(BaseModel):
    name: str = Field(description="Full name of candidate")
    email: str = Field(description="Email address")
    skills: list[str] = Field(description="Technical skills and technologies")


client = LlamaCloud(api_key="your_api_key")


# Create extraction agent
agent = client.extraction.extraction_agents.create(
    name="resume-parser",
    data_schema=Resume.model_json_schema(),
    config={}
)


# Upload a file to extract from
file_obj = client.files.create(file="resume.pdf", purpose="extract")
file_id = file_obj.id


# Extract data from document
result = await client.extraction.jobs.extract(
    extraction_agent_id=agent.id,
    file_id=file_id,
)
print(result.data)
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


// Create extraction agent
const agent = await client.extraction.extractionAgents.create({
  name: 'resume-parser',
  dataSchema: ResumeSchema,
  config: {},
});


// Upload a file to extract from
const fileObj = await client.files.create({
  file: fs.createReadStream('resume.pdf'),
  purpose: 'extract',
});
const fileId = fileObj.id;


// Extract data from document
const result = await client.extraction.jobs.extract({
  extraction_agent_id: agent.id,
  file_id: fileId,
});
console.log(result.data);
```

```
from llama_cloud_services import LlamaExtract
from pydantic import BaseModel, Field


# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv
load_dotenv()


# Initialize client
extractor = LlamaExtract()


# Define schema using Pydantic
class Resume(BaseModel):
    name: str = Field(description="Full name of candidate")
    email: str = Field(description="Email address")
    skills: list[str] = Field(description="Technical skills and technologies")


# Create extraction agent
agent = extractor.create_agent(name="resume-parser", data_schema=Resume)


# Extract data from document
result = agent.extract("resume.pdf")
print(result.data)
```

Run your script to see the extracted result!

- [Python](#tab-panel-414)
- [TypeScript](#tab-panel-415)
- [Python (legacy)](#tab-panel-416)

Terminal window

```
python your_script.py
```

Terminal window

```
ts-node your_script.ts
```

Terminal window

```
python your_script.py
```

## Defining Schemas

Schemas can be defined using either Pydantic/Zod models or JSON Schema. Refer to the [Schemas](../../features/schema_design) page for more details.

## Other Extraction APIs

### Extraction over bytes or text

You can also call extraction directly over raw text.

- [Python](#tab-panel-417)
- [TypeScript](#tab-panel-418)
- [Python (legacy)](#tab-panel-419)

```
import io
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="your_api_key")


source_text = "Candidate Name: Jane Doe\nEmail: jane.doe@example.com"
source_buffer = io.BytesIO(source_text.encode('utf-8'))


file_obj = client.files.create(file=source_buffer, purpose="extract", external_file_id="resume.txt")
file_id = file_obj.id


result = await client.extraction.jobs.extract(
    extraction_agent_id=agent.id,
    file_id=file_id,
)
```

```
import fs from 'fs';
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
const fileId = fileObj.id;


const result = await client.extraction.jobs.extract({
  extraction_agent_id: agent.id,
  file_id: fileId,
});
```

You can use the `SourceText` class to extract from bytes or text directly without using a file. If passing the file bytes, you will need to pass the filename to the `SourceText` class.

```
from llama_cloud_services import LlamaExtract, SourceText


extractor = LlamaExtract()
agent = extractor.get_agent(name="resume-parser")


with open("resume.pdf", "rb") as f:
    file_bytes = f.read()
result = agent.extract(SourceText(file=file_bytes, filename="resume.pdf"))
```

```
result = agent.extract(SourceText(text_content="Candidate Name: Jane Doe"))
```

### Batch Processing

Process multiple files asynchronously:

- [Python](#tab-panel-420)
- [TypeScript](#tab-panel-421)
- [Python (legacy)](#tab-panel-422)

We can submit multiple files for extraction using concurrency control with a semaphore:

```
import asyncio
from llama_cloud import LlamaCloud, AsyncLlamaCloud


client = AsyncLlamaCloud(api_key="your_api_key")
semaphore = asyncio.Semaphore(5)  # Limit concurrency


async def process_path(file_path: str):
    async with semaphore:
        file_obj = await client.files.create(file=file_path, purpose="extract")
        file_id = file_obj.id


        result = await client.extraction.jobs.extract(
            extraction_agent_id=agent.id,
            file_id=file_id,
        )


    return result


file_paths = ["resume1.pdf", "resume2.pdf", "resume3.pdf"]
results = await asyncio.gather(*(process_path(path) for path in file_paths))
```

We can submit multiple files for extraction using concurrency control with a semaphore:

```
import fs from 'fs';
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: 'your_api_key',
});


const semaphore = new Semaphore(5); // Limit concurrency


async function processPath(filePath: string) {
  await semaphore.acquire();
  try {
    const fileObj = await client.files.create({
      file: fs.createReadStream(filePath),
      purpose: 'extract',
    });
    const fileId = fileObj.id;
    const result = await client.extraction.jobs.extract({
      extraction_agent_id: agent.id,
      file_id: fileId,
    });
    return result;
  } finally {
    semaphore.release();
  }
}


const filePaths = ["resume1.pdf", "resume2.pdf", "resume3.pdf"];
const results = await Promise.all(filePaths.map(processPath));
```

```
# Queue multiple files for extraction
jobs = await agent.queue_extraction(["resume1.pdf", "resume2.pdf"])


# Check job status
for job in jobs:
    status = agent.get_extraction_job(job.id).status
    print(f"Job {job.id}: {status}")


# Get results when complete
results = [agent.get_extraction_run_for_job(job.id) for job in jobs]
```

### Updating Schemas

Schemas can be modified and updated after creation:

- [Python](#tab-panel-423)
- [TypeScript](#tab-panel-424)
- [Python (legacy)](#tab-panel-425)

```
client.extraction.extraction_agents.update(
    extraction_agent_id=agent.id,
    data_schema=new_schema,
    config={},
)
```

```
await client.extraction.extractionAgents.update({
  extraction_agent_id: agent.id,
  dataSchema: newSchema,
  config: {},
});
```

```
# Update schema
agent.data_schema = new_schema


# Save changes
agent.save()
```

### Managing Agents

- [Python](#tab-panel-426)
- [TypeScript](#tab-panel-427)
- [Python (legacy)](#tab-panel-428)

```
# List all agents
agents = client.extraction.extraction_agents.list()


# Get specific agent
agent = client.extraction.extraction_agents.get(extraction_agent_id="agent_id")


# Delete agent
client.extraction.extraction_agents.delete(extraction_agent_id="agent_id")
```

```
// List all agents
const agents = await client.extraction.extractionAgents.list();


// Get specific agent
const agent = await client.extraction.extractionAgents.get({
  extraction_agent_id: 'agent_id',
});


// Delete agent
await client.extraction.extractionAgents.delete({
  extraction_agent_id: 'agent_id',
});
```

```
# List all agents
agents = extractor.list_agents()


# Get specific agent
agent = extractor.get_agent(name="resume-parser")


# Delete agent
extractor.delete_agent(agent.id)
```
