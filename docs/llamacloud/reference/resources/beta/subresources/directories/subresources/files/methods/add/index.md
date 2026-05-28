## Add Directory File

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Path Parameters

- `directory_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `file_id: string`

  File ID for the storage location (required).

- `display_name: optional string`

  Display name for the file. If not provided, will use the file's name.

- `metadata: optional map[string or number or boolean]`

  User-defined metadata key-value pairs to associate with the file.

  - `string`

  - `number`

  - `boolean`

- `unique_id: optional string`

  Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

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
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID/files \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "file_id": "file_id"
        }'
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
