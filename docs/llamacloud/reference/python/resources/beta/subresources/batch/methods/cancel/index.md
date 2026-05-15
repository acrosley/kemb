## Cancel Batch Job

`beta.batch.cancel(strjob_id, BatchCancelParams**kwargs)  -> BatchCancelResponse`

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Parameters

- `job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `reason: Optional[str]`

  Optional reason for cancelling the job

- `temporal_namespace: Optional[str]`

### Returns

- `class BatchCancelResponse: …`

  Response after cancelling a batch job.

  - `job_id: str`

    ID of the cancelled job

  - `message: str`

    Confirmation message

  - `processed_items: int`

    Number of items processed before cancellation

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    New status (should be 'cancelled')

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.batch.cancel(
    job_id="job_id",
)
print(response.job_id)
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
