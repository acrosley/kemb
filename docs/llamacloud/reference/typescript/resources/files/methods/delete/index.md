## Delete File

`client.files.delete(stringfileID, FileDeleteParamsparams?, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/files/{file_id}`

Delete a file from the project.

### Parameters

- `fileID: string`

- `params: FileDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.files.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```
