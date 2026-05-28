## Create Batch Pipeline Documents

**post** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create documents for a pipeline.

### Path Parameters

- `pipeline_id: string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `body: array of CloudDocumentCreate`

  - `metadata: map[unknown]`

  - `text: string`

  - `id: optional string`

  - `excluded_embed_metadata_keys: optional array of string`

  - `excluded_llm_metadata_keys: optional array of string`

  - `page_positions: optional array of number`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `id: string`

- `metadata: map[unknown]`

- `text: string`

- `excluded_embed_metadata_keys: optional array of string`

- `excluded_llm_metadata_keys: optional array of string`

- `page_positions: optional array of number`

  indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

- `status_metadata: optional map[unknown]`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/pipelines/$PIPELINE_ID/documents \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '[
          {
            "metadata": {
              "foo": "bar"
            },
            "text": "text",
            "id": "id",
            "excluded_embed_metadata_keys": [
              "string"
            ],
            "excluded_llm_metadata_keys": [
              "string"
            ],
            "page_positions": [
              0
            ]
          }
        ]'
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
