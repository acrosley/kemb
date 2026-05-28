## Delete Retriever

`client.retrievers.delete(stringretrieverID, RetrieverDeleteParamsparams?, RequestOptionsoptions?): void`

**delete** `/api/v1/retrievers/{retriever_id}`

Delete a Retriever by ID.

### Parameters

- `retrieverID: string`

- `params: RetrieverDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.retrievers.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```
