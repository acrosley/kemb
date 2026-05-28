## Get Directory File

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Path Parameters

- `directory_id: string`

- `directory_file_id: string`

### Query Parameters

- `expand: optional array of string`

  Fields to expand.

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

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

- `created_at: optional string`

  Creation datetime

- `deleted_at: optional string`

  Soft delete marker when the file is removed upstream or by user action.

- `download_url: optional PresignedURL`

  Schema for a presigned URL.

  - `expires_at: string`

    The time at which the presigned URL expires

  - `url: string`

    A presigned URL for IO operations against a private file

  - `form_fields: optional map[string]`

    Form fields for a presigned POST request

- `file_id: optional string`

  File ID for the storage location.

- `metadata: optional map[string or number or boolean]`

  Merged metadata from all sources. Higher-priority sources override lower.

  - `string`

  - `number`

  - `boolean`

- `updated_at: optional string`

  Update datetime

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID/files/$DIRECTORY_FILE_ID \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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
