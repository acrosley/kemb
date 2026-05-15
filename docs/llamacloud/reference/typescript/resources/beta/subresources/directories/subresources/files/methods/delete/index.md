## Delete Directory File

`client.beta.directories.files.delete(stringdirectoryFileID, FileDeleteParamsparams, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID: string`

- `params: FileDeleteParams`

  - `directory_id: string`

    Path param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.beta.directories.files.delete('directory_file_id', { directory_id: 'directory_id' });
```
