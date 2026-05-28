## Update Agent Data

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Path Parameters

- `item_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `data: map[unknown]`

### Returns

- `AgentData = object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/agent-data/$ITEM_ID \
    -X PUT \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "data": {
            "foo": "bar"
          }
        }'
```

#### Response

```json
{
  "data": {
    "foo": "bar"
  },
  "deployment_name": "deployment_name",
  "id": "id",
  "collection": "collection",
  "created_at": "2019-12-27T18:11:19.117Z",
  "project_id": "project_id",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
