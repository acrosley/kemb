## Delete Configuration

**delete** `/api/v1/beta/configurations/{config_id}`

Delete a product configuration.

### Path Parameters

- `config_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/configurations/$CONFIG_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```
