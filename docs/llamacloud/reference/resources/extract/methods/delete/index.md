## Delete Extract Job

**delete** `/api/v2/extract/{job_id}`

Delete an extraction job and its results.

### Path Parameters

- `job_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v2/extract/$JOB_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{}
```
