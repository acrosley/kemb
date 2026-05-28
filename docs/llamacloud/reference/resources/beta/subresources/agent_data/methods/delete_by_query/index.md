## Delete Agent Data By Query

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `deployment_name: string`

  The agent deployment's name to delete data for

- `collection: optional string`

  The logical agent data collection to delete from

- `filter: optional map[object { eq, excludes, gt, 5 more } ]`

  Optional filters to select which items to delete

  - `eq: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `excludes: optional array of number or string or string`

    - `number`

    - `string`

    - `string`

  - `gt: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `gte: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `includes: optional array of number or string or string`

    - `number`

    - `string`

    - `string`

  - `lt: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `lte: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `ne: optional number or string or string`

    - `number`

    - `string`

    - `string`

### Returns

- `deleted_count: number`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/agent-data/:delete \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "deployment_name": "deployment_name"
        }'
```

#### Response

```json
{
  "deleted_count": 0
}
```
