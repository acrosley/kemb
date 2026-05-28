## Delete Agent Data

`$ llamacloud-prod beta:agent-data delete`

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Parameters

- `--item-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaAgentDataDeleteResponse: map[string]`

### Example

```cli
llamacloud-prod beta:agent-data delete \
  --api-key 'My API Key' \
  --item-id item_id
```

#### Response

```json
{
  "foo": "string"
}
```
