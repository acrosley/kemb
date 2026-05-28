## List Batch Job Items

`client.beta.batch.jobItems.list(stringjobID, JobItemListParamsquery?, RequestOptionsoptions?): PaginatedBatchItems<JobItemListResponse>`

**get** `/api/v1/beta/batch-processing/{job_id}/items`

List items in a batch job with optional status filtering.

Useful for finding failed items, viewing completed items,
or debugging processing issues.

### Parameters

- `jobID: string`

- `query: JobItemListParams`

  - `limit?: number`

    Maximum number of items to return

  - `offset?: number`

    Number of items to skip

  - `organization_id?: string | null`

  - `project_id?: string | null`

  - `status?: "pending" | "processing" | "completed" | 3 more | null`

    Filter items by status

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

    - `"cancelled"`

### Returns

- `JobItemListResponse`

  Detailed information about an item in a batch job.

  - `item_id: string`

    ID of the item

  - `item_name: string`

    Name of the item

  - `status: "pending" | "processing" | "completed" | 3 more`

    Processing status of this item

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

    - `"cancelled"`

  - `completed_at?: string | null`

    When processing completed for this item

  - `effective_at?: string`

  - `error_message?: string | null`

    Error message for the latest job attempt, if any.

  - `job_id?: string | null`

    Job ID for the underlying processing job (links to parse/extract job results)

  - `job_record_id?: string | null`

    The job record ID associated with this status, if any.

  - `skip_reason?: string | null`

    Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

  - `started_at?: string | null`

    When processing started for this item

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const jobItemListResponse of client.beta.batch.jobItems.list('job_id')) {
  console.log(jobItemListResponse.item_id);
}
```

#### Response

```json
{
  "items": [
    {
      "item_id": "item_id",
      "item_name": "item_name",
      "status": "pending",
      "completed_at": "2019-12-27T18:11:19.117Z",
      "effective_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "job_id": "job_id",
      "job_record_id": "job_record_id",
      "skip_reason": "skip_reason",
      "started_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
