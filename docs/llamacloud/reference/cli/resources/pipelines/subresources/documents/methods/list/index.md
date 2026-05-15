## Paginated List Pipeline Documents

`$ llamacloud-prod pipelines:documents list`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--file-id: optional string`

- `--limit: optional number`

- `--only-api-data-source-documents: optional boolean`

- `--only-direct-upload: optional boolean`

- `--skip: optional number`

- `--status-refresh-policy: optional "cached" or "ttl"`

### Returns

- `PaginatedListCloudDocumentsResponse: object { documents, limit, offset, total_count }`

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

```cli
llamacloud-prod pipelines:documents list \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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
