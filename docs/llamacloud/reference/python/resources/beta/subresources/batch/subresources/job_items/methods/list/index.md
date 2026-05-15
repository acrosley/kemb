## List Batch Job Items

`beta.batch.job_items.list(strjob_id, JobItemListParams**kwargs)  -> SyncPaginatedBatchItems[JobItemListResponse]`

**get** `/api/v1/beta/batch-processing/{job_id}/items`

List items in a batch job with optional status filtering.

Useful for finding failed items, viewing completed items,
or debugging processing issues.

### Parameters

- `job_id: str`

- `limit: Optional[int]`

  Maximum number of items to return

- `offset: Optional[int]`

  Number of items to skip

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `status: Optional[Literal["pending", "processing", "completed", 3 more]]`

  Filter items by status

  - `"pending"`

  - `"processing"`

  - `"completed"`

  - `"failed"`

  - `"skipped"`

  - `"cancelled"`

### Returns

- `class JobItemListResponse: …`

  Detailed information about an item in a batch job.

  - `item_id: str`

    ID of the item

  - `item_name: str`

    Name of the item

  - `status: Literal["pending", "processing", "completed", 3 more]`

    Processing status of this item

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

    - `"cancelled"`

  - `completed_at: Optional[datetime]`

    When processing completed for this item

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `job_id: Optional[str]`

    Job ID for the underlying processing job (links to parse/extract job results)

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `skip_reason: Optional[str]`

    Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

  - `started_at: Optional[datetime]`

    When processing started for this item

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.batch.job_items.list(
    job_id="job_id",
)
page = page.items[0]
print(page.item_id)
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
