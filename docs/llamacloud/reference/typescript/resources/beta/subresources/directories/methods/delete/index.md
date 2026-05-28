## Delete Directory

`client.beta.directories.delete(stringdirectoryID, DirectoryDeleteParamsparams?, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `directoryID: string`

- `params: DirectoryDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.beta.directories.delete('directory_id');
```
