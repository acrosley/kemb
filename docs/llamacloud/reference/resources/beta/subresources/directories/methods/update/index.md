## Update Directory

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Path Parameters

- `directory_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `description: optional string`

  Updated description for the directory.

- `name: optional string`

  Updated name for the directory.

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
    -X PATCH \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{}'
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
