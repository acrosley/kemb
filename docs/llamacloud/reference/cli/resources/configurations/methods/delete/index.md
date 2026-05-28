## Delete Configuration

`$ llamacloud-prod configurations delete`

**delete** `/api/v1/beta/configurations/{config_id}`

Delete a product configuration.

### Parameters

- `--config-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Example

```cli
llamacloud-prod configurations delete \
  --api-key 'My API Key' \
  --config-id config_id
```
