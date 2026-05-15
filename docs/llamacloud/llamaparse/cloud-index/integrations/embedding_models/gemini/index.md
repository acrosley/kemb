---
title: Gemini Embedding | Developer Documentation
---

Embed data using Gemini’s API.

## Configure via UI

1. Select `Gemini Embedding` from the `Embedding Model` dropdown.
2. Enter your Gemini API key.

![gemini](/_astro/gemini.CX1MbTJq_1BIb4q.png)

## Configure via API / Client

- [Python](#tab-panel-335)
- [TypeScript](#tab-panel-336)
- [Python (legacy)](#tab-panel-337)
- [TypeScript (legacy)](#tab-panel-338)

```
pipeline = client.pipelines.upsert(
    name="test-pipeline",
    project_id="my-project-id",
    data_sink_id=None, # optional
    embedding_config={
        'type': 'GEMINI_EMBEDDING',
        'component': {
            'api_key': '<YOUR_GEMINI_API_KEY>', # editable
            'model_name': 'models/gemini-embedding-001', # editable
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
    'type': 'GEMINI_EMBEDDING',
    'component': {
      'api_key': '<YOUR_GEMINI_API_KEY>', // editable
      'model_name': 'models/gemini-embedding-001', // editable
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
        'type': 'GEMINI_EMBEDDING',
        'component': {
            'api_key': '<YOUR_GEMINI_API_KEY>', # editable
            'model_name': 'models/gemini-embedding-001', # editable
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
        'type': 'GEMINI_EMBEDDING',
        'component': {
            'api_key': '<YOUR_GEMINI_API_KEY>', # editable
            'model_name': 'models/gemini-embedding-001', # editable
        },
    }
  'dataSinkId': data_sink.id
}


await client.pipelines.upsertPipeline({
projectId: projectId,
body: pipeline
})
```
