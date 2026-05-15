## Delete Agent Data

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Path Parameters

- `item_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/agent-data/$ITEM_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{
  "foo": "string"
}
```
