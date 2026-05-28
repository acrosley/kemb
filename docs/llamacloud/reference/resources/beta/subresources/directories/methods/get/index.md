## Get Directory

**get** `/api/v1/beta/directories/{directory_id}`

Retrieve a directory by its identifier.

### Path Parameters

- `directory_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

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

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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
