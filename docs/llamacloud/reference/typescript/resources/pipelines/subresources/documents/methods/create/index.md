## Create Batch Pipeline Documents

`client.pipelines.documents.create(stringpipelineID, DocumentCreateParamsparams, RequestOptionsoptions?): DocumentCreateResponse`

**post** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create documents for a pipeline.

### Parameters

- `pipelineID: string`

- `params: DocumentCreateParams`

  - `body: Array<CloudDocumentCreate>`

    - `metadata: Record<string, unknown>`

    - `text: string`

    - `id?: string | null`

    - `excluded_embed_metadata_keys?: Array<string>`

    - `excluded_llm_metadata_keys?: Array<string>`

    - `page_positions?: Array<number> | null`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `DocumentCreateResponse = Array<CloudDocument>`

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

const cloudDocuments = await client.pipelines.documents.create(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  {
    body: [
      {
        metadata: { foo: 'bar' },
        text: 'text',
      },
    ],
  },
);

console.log(cloudDocuments);
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
