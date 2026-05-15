## Get Pipeline Document

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Path Parameters

- `pipeline_id: string`

- `document_id: string`

### Cookie Parameters

- `session: optional string`

### Returns

- `CloudDocument = object { id, metadata, text, 4 more }`

  Cloud document stored in S3.

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
curl https://api.cloud.llamaindex.ai/api/v1/pipelines/$PIPELINE_ID/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
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
```
