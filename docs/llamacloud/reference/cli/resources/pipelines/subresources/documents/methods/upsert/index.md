## Upsert Batch Pipeline Documents

`$ llamacloud-prod pipelines:documents upsert`

**put** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create or update a document for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--body: array of CloudDocumentCreate`

### Returns

- `Response Upsert Batch Pipeline Documents Api V1 Pipelines  Pipeline Id  Documents Put: array of CloudDocument`

  - `id: string`

  - `metadata: map[unknown]`

  - `text: string`

  - `excluded_embed_metadata_keys: optional array of string`

  - `excluded_llm_metadata_keys: optional array of string`

  - `page_positions: optional array of number`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: optional map[unknown]`

### Example

```cli
llamacloud-prod pipelines:documents upsert \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --body '{metadata: {foo: bar}, text: text}'
```

#### Response

```json
[
  {
    "id": "id",
    "metadata": {
      "foo": "bar"
    },
    "text": "text",
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ],
    "page_positions": [
      0
    ],
    "status_metadata": {
      "foo": "bar"
    }
  }
]
```
