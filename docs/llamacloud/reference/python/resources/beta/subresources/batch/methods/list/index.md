## List Batch Jobs

`beta.batch.list(BatchListParams**kwargs)  -> SyncPaginatedBatchItems[BatchListResponse]`

**get** `/api/v1/beta/batch-processing`

List batch processing jobs with optional filtering.

Filter by `directory_id`, `job_type`, or `status`. Results
are paginated with configurable `limit` and `offset`.

### Parameters

- `directory_id: Optional[str]`

  Filter by directory ID

- `job_type: Optional[Literal["parse", "extract", "classify"]]`

  Filter by job type (PARSE, EXTRACT, CLASSIFY)

  - `"parse"`

  - `"extract"`

  - `"classify"`

- `limit: Optional[int]`

  Maximum number of jobs to return

- `offset: Optional[int]`

  Number of jobs to skip for pagination

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `status: Optional[Literal["pending", "running", "dispatched", 3 more]]`

  Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

  - `"pending"`

  - `"running"`

  - `"dispatched"`

  - `"completed"`

  - `"failed"`

  - `"cancelled"`

### Returns

- `class BatchListResponse: …`

  Response schema for a batch processing job.

  - `id: str`

    Unique identifier for the batch job

  - `job_type: Literal["parse", "extract", "classify"]`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: int`

    Total number of items in the job

  - `completed_at: Optional[datetime]`

    Timestamp when job completed

  - `created_at: Optional[datetime]`

    Creation datetime

  - `directory_id: Optional[str]`

    Directory being processed

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `failed_items: Optional[int]`

    Number of items that failed processing

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `processed_items: Optional[int]`

    Number of items processed so far

  - `skipped_items: Optional[int]`

    Number of items skipped (already processed or size limit)

  - `started_at: Optional[datetime]`

    Timestamp when job processing started

  - `updated_at: Optional[datetime]`

    Update datetime

  - `workflow_id: Optional[str]`

    Async job tracking ID

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.batch.list()
page = page.items[0]
print(page.id)
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
