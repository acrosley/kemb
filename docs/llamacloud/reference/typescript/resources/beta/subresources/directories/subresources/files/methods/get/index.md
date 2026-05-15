## Get Directory File

`client.beta.directories.files.get(stringdirectoryFileID, FileGetParamsparams, RequestOptionsoptions?): FileGetResponse`

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Parameters

- `directoryFileID: string`

- `params: FileGetParams`

  - `directory_id: string`

    Path param

  - `expand?: Array<string> | null`

    Query param: Fields to expand.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `FileGetResponse`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const file = await client.beta.directories.files.get('directory_file_id', {
  directory_id: 'directory_id',
});

console.log(file.id);
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
