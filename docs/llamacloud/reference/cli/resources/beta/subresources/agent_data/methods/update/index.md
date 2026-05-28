## Update Agent Data

`$ llamacloud-prod beta:agent-data update`

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Parameters

- `--item-id: string`

  Path param

- `--data: map[unknown]`

  Body param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Returns

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

### Example

```cli
llamacloud-prod beta:agent-data update \
  --api-key 'My API Key' \
  --item-id item_id \
  --data '{foo: bar}'
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
