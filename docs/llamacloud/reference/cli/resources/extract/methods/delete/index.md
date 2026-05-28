## Delete Extract Job

`$ llamacloud-prod extract delete`

**delete** `/api/v2/extract/{job_id}`

Delete an extraction job and its results.

### Parameters

- `--job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `ExtractDeleteResponse: unknown`

### Example

```cli
llamacloud-prod extract delete \
  --api-key 'My API Key' \
  --job-id job_id
```

#### Response

```json
{}
```
