---
title: Cohere Embedding | Developer Documentation
---

Embed data using Cohere’s API.

## Configure via UI

1. Select `Cohere Embedding` from the `Embedding Model` dropdown.
2. Enter your Cohere API key.

![cohere](/_astro/cohere.Aoej4bwr_1GHHKN.png)

## Configure via API / Client

- [Python](#tab-panel-331)
- [TypeScript](#tab-panel-332)
- [Python (legacy)](#tab-panel-333)
- [TypeScript (legacy)](#tab-panel-334)

```
pipeline = client.pipelines.upsert(
    name="test-pipeline",
    project_id="my-project-id",
    data_sink_id=None, # optional
    embedding_config={
        'type': 'COHERE_EMBEDDING',
        'component': {
            'api_key': '<YOUR_COHERE_API_KEY>', # editable
        },
    },
    llama_parse_parameters={},
    transform_config={"mode": "auto", "chunk_overlap": 128, "chunk_size": 1028},
)
```

```
const pipeline = await client.pipelines.upsert({
  name: 'my-first-index',
  project_id: 'my-project-id',
  data_sink_id: null, // optional
  embedding_config: {
    'type': 'COHERE_EMBEDDING',
    'component': {
      'api_key': '<YOUR_COHERE_API_KEY>', // editable
    },
  },
  llama_parse_parameters: {},
  transform_config: {
    mode: 'auto',
    chunk_overlap: 128,
    chunk_size: 1028,
  },
});
```

```
pipeline = {
    'name': 'test-pipeline',
    'transform_config': {...},
    'embedding_config': {
        'type': 'COHERE_EMBEDDING',
        'component': {
            'api_key': '<YOUR_COHERE_API_KEY>', # editable
        },
    },
    'data_sink_id': data_sink.id
}


pipeline = client.pipelines.upsert_pipeline(request=pipeline)
```

```
const pipeline = {
    'name': 'test-pipeline',
    'transform_config': {...},
    'embedding_config': {
        'type': 'COHERE_EMBEDDING',
        'component': {
            'api_key': '<YOUR_COHERE_API_KEY>', # editable
        },
    }
  'dataSinkId': data_sink.id
}


await client.pipelines.upsertPipeline({
projectId: projectId,
body: pipeline
})
```
