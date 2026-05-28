## Paginated List Pipeline Documents

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Path Parameters

- `pipeline_id: string`

### Query Parameters

- `file_id: optional string`

- `limit: optional number`

- `only_api_data_source_documents: optional boolean`

- `only_direct_upload: optional boolean`

- `skip: optional number`

- `status_refresh_policy: optional "cached" or "ttl"`

  - `"cached"`

  - `"ttl"`

### Cookie Parameters

- `session: optional string`

### Returns

- `documents: array of CloudDocument`

  The documents to list

  - `id: string`

  - `metadata: map[unknown]`

  - `text: string`

  - `excluded_embed_metadata_keys: optional array of string`

  - `excluded_llm_metadata_keys: optional array of string`

  - `page_positions: optional array of number`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: optional map[unknown]`

- `limit: number`

  The limit of the documents

- `offset: number`

  The offset of the documents

- `total_count: number`

  The total number of documents

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/pipelines/$PIPELINE_ID/documents/paginated \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{
  "documents": [
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
  ],
  "limit": 0,
  "offset": 0,
  "total_count": 0
}
```
