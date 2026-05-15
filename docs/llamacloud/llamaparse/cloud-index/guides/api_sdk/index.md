---
title: Index API & Clients Guide | Developer Documentation
description: Comprehensive guide to using the Index API and SDK clients for Python and TypeScript, including setup, file upload, data source/sink configuration, and index management.
---

This guide highlights the core workflow for working with Index programmatically.

Tip

See full API reference [here](/cloud-api-reference/llama-platform/index.md).

### App setup

- [Python](#tab-panel-75)
- [TypeScript](#tab-panel-76)

Install API client package

```
pip install llama-cloud>=1.0
```

Import and configure the client (you can use either the sync or async client):

```
from llama_cloud import LlamaCloud, AsyncLlamaCloud


client = LlamaCloud(api_key='<llama-cloud-api-key>')
```

Install API client package

```
npm install @llamaindex/llama-cloud
```

Import and configure the client:

```
import { LlamaCloud } from "@llamaindex/llama-cloud";


const client = new LlamaCloud({
  apiKey: "<llama-cloud-api-key>",
});
```

## Create new index

### Upload files

- [Python](#tab-panel-77)
- [TypeScript](#tab-panel-78)

```
file_obj = client.files.create(file="/path/to/doc1.pdf", purpose="user_data")
print(file_obj.id)
```

```
import { LlamaCloud } from "@llamaindex/llama-cloud";
import fs from 'fs';


const client = new LlamaCloud();


// Upload a file
const fileObj = await client.files.create({
    file: fs.createReadStream('/path/to/doc1.pdf'),
    purpose: "user_data",
});
const fileId = fileObj.id;


console.log(fileId);
```

Tip

See [Files API](/cloud-api-reference/category/files/index.md) for full details on file management.

### Configure data sources

- [Python](#tab-panel-79)
- [TypeScript Client](#tab-panel-80)

```
from llama_cloud.types.data_source_create_params import ComponentCloudS3DataSource


data_source = await client.data_sources.create(
    name="my-s3-data-source",
    component=ComponentCloudS3DataSource(
        bucket="my-bucket",
        aws_access_id="my-access-id",
        prefix="documents/",
    ),
    source_type="S3",
    project_id="my-project-id",
)
```

```
const dataSource = await client.dataSources.create({
  name: 'my-s3-data-source',
  component: {
    bucket: 'my-bucket',
    aws_access_id: 'my-access-id',
    prefix: 'documents/',
  },
  source_type: 'S3',
  project_id: 'my-project-id',
});


console.log(dataSource.id);
```

Tip

See [Data Sources API](/cloud-api-reference/category/data-sources/index.md) for full details on data source management.

See [full list of data sources and specifications](../../integrations/data_sources/).

### Configure data sinks

- [Python](#tab-panel-81)
- [TypeScript](#tab-panel-82)

```
from llama_cloud.types.data_sink_create_params import ComponentCloudPineconeVectorStore


data_sink = client.data_sinks.create(
    name="my-pinecone-data-sink",
    component=ComponentCloudPineconeVectorStore(
        api_key="my-pinecone-api-key",
        index_name="my-pinecone-index",
    ),
    sink_type="PINECONE",
)


print(data_sink.id)
```

```
const dataSink = await client.dataSinks.create({
  name: 'my-pinecone-data-sink',
  component: {
    api_key: 'my-pinecone-api-key',
    index_name: 'my-pinecone-index',
  },
  sink_type: 'PINECONE',
});


console.log(dataSink.id);
```

Tip

See [Data Sinks API](/cloud-api-reference/category/data-sinks/index.md) for full details on data sink management.

See [full list of data sinks and specifications](../../integrations/data_sinks/).

### Setup transformation and embedding config

Tip

See [Parsing & Transformation](../../parsing_transformation/) for full details on transformation guide.

```
# Embedding config
embedding_config = {
    'type': 'OPENAI_EMBEDDING',
    'component': {
        'api_key': '<YOUR_API_KEY_HERE>', # editable
        'model_name': 'text-embedding-ada-002' # editable
    }
}


# Transformation auto config
transform_config = {
    'mode': 'auto',
    'config': {
        'chunk_size': 1024, # editable
        'chunk_overlap': 20 # editable
    }
}
```

### Create index (i.e. pipeline)

- [Python](#tab-panel-83)
- [TypeScript](#tab-panel-84)

```
pipeline = client.pipelines.upsert({
  name: 'my-first-index',
  project_id: 'my-project-id',
  data_sink_id: data_sink.id,
  embedding_config: {
    "type": 'OPENAI_EMBEDDING',
    "component": {
      "api_key": 'sk-1234',
      "model_name": 'text-embedding-3-small',
    },
  },
  llama_parse_parameters: {
    "tier": "agentic",
    "version": "latest",
  },
  transform_config: {
    "mode": 'auto',
    "chunk_overlap": 128,
    "chunk_size": 1028,
  },
});


print(pipeline.id);
```

```
const pipeline = await client.pipelines.upsert({
  name: 'my-first-index',
  project_id: 'my-project-id',
  data_sink_id: dataSink.id,
  embedding_config: {
    type: 'OPENAI_EMBEDDING',
    component: {
      api_key: 'sk-1234',
      model_name: 'text-embedding-3-small',
    },
  },
  llama_parse_parameters: {
    tier: 'agentic',
    version: 'latest',
  },
  transform_config: {
    mode: 'auto',
    chunk_overlap: 128,
    chunk_size: 1028,
  },
});


console.log(pipeline.id);
```

Tip

See [Pipeline API](/cloud-api-reference/category/pipelines/index.md) and [Pipeline Files API](/cloud-api-reference/category/pipeline-files/index.md) for full details on index (i.e. pipeline) management.

### Add files to index

- [Python](#tab-panel-85)
- [TypeScript](#tab-panel-86)

```
files = client.pipelines.files.create(
    pipeline_id="some-id",
    body=[
        {
            "file_id": file_obj.id,
            "custom_metadata": {"category": "invoices"},
        }
    ]
)
```

```
const files = await client.pipelines.files.create(pipeline.id, {
  body: [
    {
      file_id: "1234",
      custom_metadata: { source: 'generated' },
    }
  ]
})


console.log(files.length);
```

Additive Semantics

This endpoint uses **additive/upsert semantics**, not standard REST PUT replacement:

- Files **not included** in the request remain unchanged in the index
- Files **included** in the request are added, or if already present, their status is reset and they will be re-indexed

**To add new files without re-indexing existing files**, only include the new file IDs in your request. Do not include existing file IDs unless you want them to be re-processed.

### Add data sources to index

- [Python](#tab-panel-87)
- [TypeScript](#tab-panel-88)

```
await client.pipelines.data_sources.update_data_sources(
    pipeline_id=pipeline.id,
    body=[
        {
            "data_source_id": data_source.id,
            "sync_interval": 43200.0 # Optional, scheduled sync frequency in seconds. In this case, every 12 hours.
        },
    ]
)
```

```
const dataSources = await client.pipelines.dataSources.updateDataSources(pipeline.id, {
  body: [
    {
      data_source_id: dataSourceId,
      sync_interval: 43200.0 // Optional, scheduled sync frequency in seconds. In this case, every 12 hours.
    },
  ],
});
```

Tip

For more details on scheduled sync, including how the sync timing works, and available sync frequencies, refer to [Scheduled sync](../ui#scheduled-sync).

### Add documents to index

- [Python](#tab-panel-89)
- [TypeScript](#tab-panel-90)

```
documents = await client.pipelines.documents.create(
    pipeline_id=pipeline.id,
    body=[
        {
            "text": "This is my first document to be indexed.",
            "metadata": {"source": "generated"},
        }
    ],
)
print(f"Uploaded {len(documents)} documents to the index.")
```

```
const documents = await client.pipelines.documents.create(pipeline.id, {
  body: [
    {
      text: 'This is my first document to be indexed.',
      metadata: { source: 'generated' },
    },
  ],
});
console.log(`Uploaded ${documents.length} documents to the index.`);
```

## Observe ingestion status & history

### Get index status

- [Python Sync Client](#tab-panel-91)
- [TypeScript Client](#tab-panel-92)

```
# Wait for indexing to complete
status_resp = client.pipelines.get_status(pipeline_id=pipeline.id)
while status_resp.status not in ("NOT_STARTED", "IN_PROGRESS"):
    time.sleep(5)
    status_resp = client.pipelines.get_status(pipeline_id=pipeline.id)


print(f"Indexing completed with status: {status_resp.status}")
```

```
// Wait for indexing to complete
let statusResp = await client.pipelines.getStatus(pipeline.id, {});
while (statusResp.status === 'NOT_STARTED' || statusResp.status === 'IN_PROGRESS') {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  statusResp = await client.pipelines.getStatus(pipeline.id, {});
}
```

## Run search (i.e. retrieval endpoint)

- [Python](#tab-panel-93)
- [TypeScript](#tab-panel-94)

```
results = await client.pipelines.retrieve(
    pipeline_id=pipeline.id,
    query="Some query",
    dense_similarity_top_k=20,
    sparse_similarity_top_k=20,
    alpha=0.5,
    enable_reranking=True,
    rerank_top_n=5,
)


for n in results.retrieval_nodes:
    print(f"Score: {n.score}, Text: {n.node.text}")
```

```
const results = await client.pipelines.retrieve('your-existing-pipeline-id', {
  query: 'Some query',
  dense_similarity_top_k: 20,
  sparse_similarity_top_k: 20,
  alpha: 0.5,
  enable_reranking: true,
  rerank_top_n: 5,
});


for (const n of results.retrieval_nodes || []) {
  console.log(`Score: ${n.score}, Text: ${n.node?.text}`);
}
```
