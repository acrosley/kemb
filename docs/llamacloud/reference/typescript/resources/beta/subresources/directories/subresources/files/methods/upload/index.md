## Upload File To Directory

`client.beta.directories.files.upload(stringdirectoryID, FileUploadParamsparams, RequestOptionsoptions?): FileUploadResponse`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `directoryID: string`

- `params: FileUploadParams`

  - `upload_file: Uploadable`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `display_name?: string | null`

    Body param

  - `external_file_id?: string | null`

    Body param

  - `metadata?: string | null`

    Body param: User metadata as a JSON object string.

  - `unique_id?: string | null`

    Body param

### Returns

- `FileUploadResponse`

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

const response = await client.beta.directories.files.upload('directory_id', {
  upload_file: fs.createReadStream('path/to/file'),
});

console.log(response.id);
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
