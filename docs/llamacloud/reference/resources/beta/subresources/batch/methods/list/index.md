## List Batch Jobs

**get** `/api/v1/beta/batch-processing`

List batch processing jobs with optional filtering.

Filter by `directory_id`, `job_type`, or `status`. Results
are paginated with configurable `limit` and `offset`.

### Query Parameters

- `directory_id: optional string`

  Filter by directory ID

- `job_type: optional "parse" or "extract" or "classify"`

  Filter by job type (PARSE, EXTRACT, CLASSIFY)

  - `"parse"`

  - `"extract"`

  - `"classify"`

- `limit: optional number`

  Maximum number of jobs to return

- `offset: optional number`

  Number of jobs to skip for pagination

- `organization_id: optional string`

- `project_id: optional string`

- `status: optional "pending" or "running" or "dispatched" or 3 more`

  Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

  - `"pending"`

  - `"running"`

  - `"dispatched"`

  - `"completed"`

  - `"failed"`

  - `"cancelled"`

### Cookie Parameters

- `session: optional string`

### Returns

- `items: array of object { id, job_type, project_id, 14 more }`

  The list of items.

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

- `next_page_token: optional string`

  A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

- `total_size: optional number`

  The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/batch-processing \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{
  "items": [
    {
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
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
