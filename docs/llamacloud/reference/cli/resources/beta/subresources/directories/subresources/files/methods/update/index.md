## Update Directory File

`$ llamacloud-prod beta:directories:files update`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `--directory-id: string`

  Path param

- `--directory-file-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--directory-id: string`

  Path param

- `--display-name: optional string`

  Body param: Updated display name.

- `--metadata: optional map[string or number or boolean]`

  Body param: User-defined metadata key-value pairs. Replaces the user metadata layer.

- `--unique-id: optional string`

  Body param: Updated unique identifier.

### Returns

- `BetaDirectoryFileUpdateResponse: object { id, directory_id, display_name, 8 more }`

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

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

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

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files update \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --directory-file-id directory_file_id
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
