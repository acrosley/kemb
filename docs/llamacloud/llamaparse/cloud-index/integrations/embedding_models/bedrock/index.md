---
title: Bedrock Embedding | Developer Documentation
---

Embed data using AWS Bedrock’s API.

## Configure via UI

1. Select `Bedrock Embedding` from the `Embedding Model` dropdown.
2. Enter your AWS Region, AWS access key ID and AWS secret access key.
3. Select your preferred model:

- `Titan Embedding` (Default)
- `Titan Embedding G1 Text 02`
- `Cohere Embed English V3`
- `Cohere Embed Multilingual V3`

![bedrock](/_astro/bedrock.DHXnXKFT_lJ1uj.png)

## Configure via API / Client

For API / Client, use the model IDs:

- `amazon.titan-embed-text-v1`
- `amazon.titan-embed-g1-text-02`
- `cohere.embed-english-v3`
- `cohere.embed-multilingual-v3`

* [Python](#tab-panel-327)
* [TypeScript](#tab-panel-328)
* [Python (legacy)](#tab-panel-329)
* [TypeScript (legacy)](#tab-panel-330)

```
pipeline = client.pipelines.upsert(
    name="test-pipeline",
    project_id="my-project-id",
    data_sink_id=None, # optional
    embedding_config={
        'type': 'BEDROCK_EMBEDDING',
        'component': {
            'region_name': 'us-east-1',
            'aws_access_key_id': '<aws_access_key_id>',
            'aws_secret_access_key': '<aws_secret_access_key>',
            'model': 'amazon.titan-embed-text-v1',
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
    'type': 'BEDROCK_EMBEDDING',
    'component': {
      'region_name': 'us-east-1',
      'aws_access_key_id': '<aws_access_key_id>',
      'aws_secret_access_key': '<aws_secret_access_key>',
      'model': 'amazon.titan-embed-text-v1',
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
        'type': 'BEDROCK_EMBEDDING',
        'component': {
            'region_name': 'us-east-1',
            'aws_access_key_id': '<aws_access_key_id>',
            'aws_secret_access_key': '<aws_secret_access_key>',
            'model': 'amazon.titan-embed-text-v1',
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
        'type': 'BEDROCK_EMBEDDING',
        'component': {
            'region_name': 'us-east-1',
            'aws_access_key_id': '<aws_access_key_id>',
            'aws_secret_access_key': '<aws_secret_access_key>',
            'model': 'amazon.titan-embed-text-v1',
        },
    }
  'dataSinkId': data_sink.id
}


await client.pipelines.upsertPipeline({
projectId: projectId,
body: pipeline
})
```
