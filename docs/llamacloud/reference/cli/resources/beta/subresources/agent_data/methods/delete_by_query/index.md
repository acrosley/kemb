## Delete Agent Data By Query

`$ llamacloud-prod beta:agent-data delete-by-query`

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Parameters

- `--deployment-name: string`

  Body param: The agent deployment's name to delete data for

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param: The logical agent data collection to delete from

- `--filter: optional map[object { eq, excludes, gt, 5 more } ]`

  Body param: Optional filters to select which items to delete

### Returns

- `BetaAgentDataDeleteByQueryResponse: object { deleted_count }`

  API response for bulk delete operation

  - `deleted_count: number`

### Example

```cli
llamacloud-prod beta:agent-data delete-by-query \
  --api-key 'My API Key' \
  --deployment-name deployment_name
```

#### Response

```json
{
  "deleted_count": 0
}
```
