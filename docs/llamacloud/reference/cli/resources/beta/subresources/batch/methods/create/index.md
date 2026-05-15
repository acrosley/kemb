## Create Batch Job

`$ llamacloud-prod beta:batch create`

**post** `/api/v1/beta/batch-processing`

Create a batch processing job.

Processes files from a directory or a specific list of item IDs.
Supports batch parsing and classification operations.

Provide either `directory_id` to process all files in a directory,
or `item_ids` for specific items. The job runs asynchronously —
poll `GET /batch/{job_id}` for progress.

### Parameters

- `--job-config: object { correlation_id, job_name, parameters, 6 more }  or ClassifyJob`

  Body param: Job configuration — either a parse or classify config

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--continue-as-new-threshold: optional number`

  Body param: Maximum files to process per execution cycle in directory mode. Defaults to page_size.

- `--directory-id: optional string`

  Body param: ID of the directory containing files to process

- `--item-id: optional array of string`

  Body param: List of specific item IDs to process. Either this or directory_id must be provided.

- `--page-size: optional number`

  Body param: Number of files to process per batch when using directory mode

- `--temporal-namespace: optional string`

  Header param

### Returns

- `BetaBatchNewResponse: object { id, job_type, project_id, 14 more }`

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

### Example

```cli
llamacloud-prod beta:batch create \
  --api-key 'My API Key' \
  --job-config '{}'
```

#### Response

```json
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
```
