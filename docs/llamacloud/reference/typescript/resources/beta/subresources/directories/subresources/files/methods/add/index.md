## Add Directory File

`client.beta.directories.files.add(stringdirectoryID, FileAddParamsparams, RequestOptionsoptions?): FileAddResponse`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `directoryID: string`

- `params: FileAddParams`

  - `file_id: string`

    Body param: File ID for the storage location (required).

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `display_name?: string | null`

    Body param: Display name for the file. If not provided, will use the file's name.

  - `metadata?: Record<string, string | number | boolean | null> | null`

    Body param: User-defined metadata key-value pairs to associate with the file.

    - `string`

    - `number`

    - `boolean`

  - `unique_id?: string | null`

    Body param: Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `FileAddResponse`

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

const response = await client.beta.directories.files.add('directory_id', { file_id: 'file_id' });

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
