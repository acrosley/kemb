## Cancel Batch Job

`$ llamacloud-prod beta:batch cancel`

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Parameters

- `--job-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--reason: optional string`

  Body param: Optional reason for cancelling the job

- `--temporal-namespace: optional string`

  Header param

### Returns

- `BetaBatchCancelResponse: object { job_id, message, processed_items, status }`

  Response after cancelling a batch job.

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

```cli
llamacloud-prod beta:batch cancel \
  --api-key 'My API Key' \
  --job-id job_id
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
