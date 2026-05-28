## Delete Pipeline File

`client.pipelines.files.delete(stringfileID, FileDeleteParamsparams, RequestOptionsoptions?): void`

**delete** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Delete a file from a pipeline.

### Parameters

- `fileID: string`

- `params: FileDeleteParams`

  - `pipeline_id: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.pipelines.files.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});
```
