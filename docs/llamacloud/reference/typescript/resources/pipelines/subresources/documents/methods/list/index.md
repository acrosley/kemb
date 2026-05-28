## Paginated List Pipeline Documents

`client.pipelines.documents.list(stringpipelineID, DocumentListParamsquery?, RequestOptionsoptions?): PaginatedCloudDocuments<CloudDocument>`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `pipelineID: string`

- `query: DocumentListParams`

  - `file_id?: string | null`

  - `limit?: number`

  - `only_api_data_source_documents?: boolean | null`

  - `only_direct_upload?: boolean | null`

  - `skip?: number`

  - `status_refresh_policy?: "cached" | "ttl"`

    - `"cached"`

    - `"ttl"`

### Returns

- `CloudDocument`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const cloudDocument of client.pipelines.documents.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(cloudDocument.id);
}
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
