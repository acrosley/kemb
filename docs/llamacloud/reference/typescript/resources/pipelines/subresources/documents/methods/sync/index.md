## Sync Pipeline Document

`client.pipelines.documents.sync(stringdocumentID, DocumentSyncParamsparams, RequestOptionsoptions?): DocumentSyncResponse`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `documentID: string`

- `params: DocumentSyncParams`

  - `pipeline_id: string`

### Returns

- `DocumentSyncResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.documents.sync('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response);
```

#### Response

```json
{}
```
