## Get Batch Job Status

`client.beta.batch.getStatus(stringjobID, BatchGetStatusParamsquery?, RequestOptionsoptions?): BatchGetStatusResponse`

**get** `/api/v1/beta/batch-processing/{job_id}`

Get detailed status of a batch processing job.

Returns current progress percentage, file counts (total,
processed, failed, skipped), and timestamps.

### Parameters

- `jobID: string`

- `query: BatchGetStatusParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `BatchGetStatusResponse`

  Detailed status response for a batch processing job.

  - `job: Job`

    Response schema for a batch processing job.

    - `id: string`

      Unique identifier for the batch job

    - `job_type: "parse" | "extract" | "classify"`

      Type of processing operation (parse or classify)

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `project_id: string`

      Project this job belongs to

    - `status: "pending" | "running" | "dispatched" | 3 more`

      Current job status

      - `"pending"`

      - `"running"`

      - `"dispatched"`

      - `"completed"`

      - `"failed"`

      - `"cancelled"`

    - `total_items: number`

      Total number of items in the job

    - `completed_at?: string | null`

      Timestamp when job completed

    - `created_at?: string | null`

      Creation datetime

    - `directory_id?: string | null`

      Directory being processed

    - `effective_at?: string`

    - `error_message?: string | null`

      Error message for the latest job attempt, if any.

    - `failed_items?: number`

      Number of items that failed processing

    - `job_record_id?: string | null`

      The job record ID associated with this status, if any.

    - `processed_items?: number`

      Number of items processed so far

    - `skipped_items?: number`

      Number of items skipped (already processed or size limit)

    - `started_at?: string | null`

      Timestamp when job processing started

    - `updated_at?: string | null`

      Update datetime

    - `workflow_id?: string | null`

      Async job tracking ID

  - `progress_percentage: number`

    Percentage of items processed (0-100)

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.batch.getStatus('job_id');

console.log(response.job);
```

#### Response

```json
{
  "job": {
    "id": "bjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "job_type": "parse",
    "project_id": "proj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "status": "pending",
    "total_items": 0,
    "completed_at": "2019-12-27T18:11:19.117Z",
    "created_at": "2019-12-27T18:11:19.117Z",
    "directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "effective_at": "2019-12-27T18:11:19.117Z",
    "error_message": "error_message",
    "failed_items": 0,
    "job_record_id": "job_record_id",
    "processed_items": 0,
    "skipped_items": 0,
    "started_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "workflow_id": "workflow_id"
  },
  "progress_percentage": 0
}
```
