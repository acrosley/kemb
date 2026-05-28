## Create Agent Data

`$ llamacloud-prod beta:agent-data create`

**post** `/api/v1/beta/agent-data`

Create new agent data.

### Parameters

- `--data: map[unknown]`

  Body param

- `--deployment-name: string`

  Body param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param

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
llamacloud-prod beta:agent-data create \
  --api-key 'My API Key' \
  --data '{foo: bar}' \
  --deployment-name deployment_name
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
