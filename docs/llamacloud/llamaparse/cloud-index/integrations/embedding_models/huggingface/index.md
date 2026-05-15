---
title: HuggingFace Embedding | Developer Documentation
---

Embed data using HuggingFace’s Inference API.

## Configure via UI

1. Select `HuggingFace Embedding` from the `Embedding Model` dropdown.
2. Enter your HuggingFace API key.
3. Enter your HuggingFace model name or URL, e.g. `BAAI/bge-small-en-v1.5`.

![huggingface](/_astro/huggingface.BVlLJSgO_ZKYKYg.png)

## Configure via API / Client

- [Python](#tab-panel-339)
- [TypeScript](#tab-panel-340)
- [Python (legacy)](#tab-panel-341)
- [TypeScript (legacy)](#tab-panel-342)

```
pipeline = client.pipelines.upsert(
    name="test-pipeline",
    project_id="my-project-id",
    data_sink_id=None, # optional
    embedding_config={
        'type': 'HUGGINGFACE_API_EMBEDDING',
        'component': {
            'token': 'hf_...',
            'model_name': 'BAAI/bge-small-en-v1.5',
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
    'type': 'HUGGINGFACE_API_EMBEDDING',
    'component': {
      'token': 'hf_...',
      'model_name': 'BAAI/bge-small-en-v1.5',
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
        'type': 'HUGGINGFACE_API_EMBEDDING',
        'component': {
            'token': 'hf_...',
            'model_name': 'BAAI/bge-small-en-v1.5',
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
      'type': 'HUGGINGFACE_API_EMBEDDING',
      'component': {
          'token': 'hf_...',
          'model_name': 'BAAI/bge-small-en-v1.5',
      },
  },
  'dataSinkId': data_sink.id
}


await client.pipelines.upsertPipeline({
projectId: projectId,
body: pipeline
})
```
