## Cancel Batch Job

`client.beta.batch.cancel(stringjobID, BatchCancelParamsparams, RequestOptionsoptions?): BatchCancelResponse`

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Parameters

- `jobID: string`

- `params: BatchCancelParams`

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `reason?: string | null`

    Body param: Optional reason for cancelling the job

  - `temporalNamespace?: string`

    Header param

### Returns

- `BatchCancelResponse`

  Response after cancelling a batch job.

  - `job_id: string`

    ID of the cancelled job

  - `message: string`

    Confirmation message

  - `processed_items: number`

    Number of items processed before cancellation

  - `status: "pending" | "running" | "dispatched" | 3 more`

    New status (should be 'cancelled')

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.batch.cancel('job_id');

console.log(response.job_id);
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
