## List Directories

`$ llamacloud-prod beta:directories list`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `--include-deleted: optional boolean`

- `--name: optional string`

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--type: optional "user" or "index"`

### Returns

- `DirectoryQueryResponse: object { items, next_page_token, total_size }`

  API query response schema for directories.

  - `items: array of object { id, name, project_id, 4 more }`

    The list of items.

    - `id: string`

      Unique identifier for the directory.

    - `name: string`

      Human-readable name for the directory.

    - `project_id: string`

      Project the directory belongs to.

    - `created_at: optional string`

      Creation datetime

    - `deleted_at: optional string`

      Optional timestamp of when the directory was deleted. Null if not deleted.

    - `description: optional string`

      Optional description shown to users.

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:directories list \
  --api-key 'My API Key'
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "name": "x",
      "project_id": "project_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "deleted_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
