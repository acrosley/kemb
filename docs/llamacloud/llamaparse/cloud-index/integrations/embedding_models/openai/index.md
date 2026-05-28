---
title: OpenAI Embedding | Developer Documentation
---

Embed data using OpenAI’s API.

## Configure via UI

1. Select `OpenAI Embedding` from the `Embedding Model` dropdown.
2. Enter your OpenAI API key.
3. Select your preferred model:

- `text-embedding-3-small` (Default)
- `text-similarity-3-large`
- `text-embedding-ada-002`

![openai](/_astro/openai.C5wAtOen_ZWgQrd.png)

## Configure via API / Client

- [Python](#tab-panel-343)
- [TypeScript](#tab-panel-344)
- [Python (legacy)](#tab-panel-345)
- [TypeScript (legacy)](#tab-panel-346)

```
pipeline = client.pipelines.upsert(
    name="test-pipeline",
    project_id="my-project-id",
    data_sink_id=None, # optional
    embedding_config={
        'type': 'OPENAI_EMBEDDING',
        'component': {
            'api_key': '<YOUR_API_KEY_HERE>', # editable
            'model_name': 'text-embedding-3-small' # editable
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
    'type': 'OPENAI_EMBEDDING',
    'component': {
      'api_key': '<YOUR_API_KEY_HERE>', // editable
      'model_name': 'text-embedding-3-small' // editable
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
        'type': 'OPENAI_EMBEDDING',
        'component': {
            'api_key': '<YOUR_API_KEY_HERE>', # editable
            'model_name': 'text-embedding-3-small' # editable
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
        'type': 'OPENAI_EMBEDDING',
        'component': {
            'api_key': '<YOUR_API_KEY_HERE>', # editable
            'model_name': 'text-embedding-3-small' # editable
        },
    },
    'dataSinkId': data_sink.id
}


await client.pipelines.upsertPipeline({
projectId: projectId,
body: pipeline
})
```
