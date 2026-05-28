## Update Directory

`$ llamacloud-prod beta:directories update`

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Parameters

- `--directory-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--description: optional string`

  Body param: Updated description for the directory.

- `--name: optional string`

  Body param: Updated name for the directory.

### Returns

- `BetaDirectoryUpdateResponse: object { id, name, project_id, 4 more }`

  API response schema for a directory.

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

### Example

```cli
llamacloud-prod beta:directories update \
  --api-key 'My API Key' \
  --directory-id directory_id
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
