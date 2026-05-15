## Cancel Batch Job

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Path Parameters

- `job_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Header Parameters

- `"temporal-namespace": optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `reason: optional string`

  Optional reason for cancelling the job

### Returns

- `job_id: string`

  ID of the cancelled job

- `message: string`

  Confirmation message

- `processed_items: number`

  Number of items processed before cancellation

- `status: "pending" or "running" or "dispatched" or 3 more`

  New status (should be 'cancelled')

  - `"pending"`

  - `"running"`

  - `"dispatched"`

  - `"completed"`

  - `"failed"`

  - `"cancelled"`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/batch-processing/$JOB_ID/cancel \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{}'
```

#### Response

```json
{
  "job_id": "job_id",
  "message": "message",
  "processed_items": 0,
  "status": "pending"
}
```
