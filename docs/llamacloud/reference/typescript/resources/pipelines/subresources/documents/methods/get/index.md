## Get Pipeline Document

`client.pipelines.documents.get(stringdocumentID, DocumentGetParamsparams, RequestOptionsoptions?): CloudDocument`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Parameters

- `documentID: string`

- `params: DocumentGetParams`

  - `pipeline_id: string`

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

const cloudDocument = await client.pipelines.documents.get('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(cloudDocument.id);
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
