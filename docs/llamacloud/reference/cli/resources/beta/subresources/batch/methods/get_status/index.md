## Get Batch Job Status

`$ llamacloud-prod beta:batch get-status`

**get** `/api/v1/beta/batch-processing/{job_id}`

Get detailed status of a batch processing job.

Returns current progress percentage, file counts (total,
processed, failed, skipped), and timestamps.

### Parameters

- `--job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaBatchGetStatusResponse: object { job, progress_percentage }`

  Detailed status response for a batch processing job.

  - `job: object { id, job_type, project_id, 14 more }`

    Response schema for a batch processing job.

    - `id: string`

      Unique identifier for the batch job

    - `job_type: "parse" or "extract" or "classify"`

      Type of processing operation (parse or classify)

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `project_id: string`

      Project this job belongs to

    - `status: "pending" or "running" or "dispatched" or 3 more`

      Current job status

      - `"pending"`

      - `"running"`

      - `"dispatched"`

      - `"completed"`

      - `"failed"`

      - `"cancelled"`

    - `total_items: number`

      Total number of items in the job

    - `completed_at: optional string`

      Timestamp when job completed

    - `created_at: optional string`

      Creation datetime

    - `directory_id: optional string`

      Directory being processed

    - `effective_at: optional string`

    - `error_message: optional string`

      Error message for the latest job attempt, if any.

    - `failed_items: optional number`

      Number of items that failed processing

    - `job_record_id: optional string`

      The job record ID associated with this status, if any.

    - `processed_items: optional number`

      Number of items processed so far

    - `skipped_items: optional number`

      Number of items skipped (already processed or size limit)

    - `started_at: optional string`

      Timestamp when job processing started

    - `updated_at: optional string`

      Update datetime

    - `workflow_id: optional string`

      Async job tracking ID

  - `progress_percentage: number`

    Percentage of items processed (0-100)

### Example

```cli
llamacloud-prod beta:batch get-status \
  --api-key 'My API Key' \
  --job-id job_id
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
