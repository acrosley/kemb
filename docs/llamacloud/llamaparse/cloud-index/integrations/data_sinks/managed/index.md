---
title: Managed Data Sink | Developer Documentation
---

Use LlamaCloud managed index as data sink.

## Configure via UI

![managed](/_astro/managed.BQ5J7cYU_1VMvmM.png)

## Configure via API / Client

Simply set `data_sink_id` to None when creating a pipeline

- [Python](#tab-panel-251)
- [TypeScript](#tab-panel-252)

```
from llama_cloud import AsyncLlamaCloud, LlamaCloud
from llama_cloud.types.pipeline_create_params import (
  EmbeddingConfigOpenAIEmbeddingConfig,
  EmbeddingConfigOpenAIEmbeddingConfigComponent,
)
client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


pipeline = client.pipelines.create(
  name="my-first-index",
  project_id="my-project-id",
  data_sink_id=None, # Use managed data sink
  embedding_config=EmbeddingConfigOpenAIEmbeddingConfig(
    component=EmbeddingConfigOpenAIEmbeddingConfigComponent(
      api_key="sk-1234",
      model_name="text-embedding-3-small",
    ),
    type="OPENAI_EMBEDDING",
  ),
  llama_parse_parameters={"parse_mode": "parse_document_with_agent", "model": "openai-gpt-4-1-mini"},
  transform_config={"mode": "auto", "chunk_overlap": 128, "chunk_size": 1028},
)
```

```
const pipeline = await client.pipelines.upsert({
  name: 'my-first-index',
  project_id: 'my-project-id',
  data_sink_id: null, // Use managed data sink
  embedding_config: {
    type: 'OPENAI_EMBEDDING',
    component: {
      api_key: 'sk-1234',
      model_name: 'text-embedding-3-small',
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
