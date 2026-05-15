## Create Directory

`$ llamacloud-prod beta:directories create`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `--name: string`

  Body param: Human-readable name for the directory.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--description: optional string`

  Body param: Optional description shown to users.

### Returns

- `BetaDirectoryNewResponse: object { id, name, project_id, 4 more }`

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
llamacloud-prod beta:directories create \
  --api-key 'My API Key' \
  --name x
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
