## List Directory Files

`$ llamacloud-prod beta:directories:files list`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `--directory-id: string`

- `--display-name: optional string`

- `--display-name-contains: optional string`

- `--expand: optional array of string`

  Fields to expand on each directory file.

- `--file-id: optional string`

- `--include-deleted: optional boolean`

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--unique-id: optional string`

- `--updated-at-on-or-after: optional string`

  Include items updated at or after this timestamp (inclusive)

- `--updated-at-on-or-before: optional string`

  Include items updated at or before this timestamp (inclusive)

### Returns

- `DirectoryFileQueryResponse: object { items, next_page_token, total_size }`

  API query response schema for directory files.

  - `items: array of object { id, directory_id, display_name, 8 more }`

    The list of items.

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

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:directories:files list \
  --api-key 'My API Key' \
  --directory-id directory_id
```

#### Response

```json
{
  "items": [
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
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
