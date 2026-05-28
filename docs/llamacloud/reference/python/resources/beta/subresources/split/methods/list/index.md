## List Split Jobs

`beta.split.list(SplitListParams**kwargs)  -> SyncPaginatedCursor[SplitListResponse]`

**get** `/api/v1/beta/split/jobs`

List document split jobs.

### Parameters

- `created_at_on_or_after: Optional[Union[str, datetime, null]]`

  Include items created at or after this timestamp (inclusive)

- `created_at_on_or_before: Optional[Union[str, datetime, null]]`

  Include items created at or before this timestamp (inclusive)

- `job_ids: Optional[SequenceNotStr[str]]`

  Filter by specific job IDs

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

- `page_token: Optional[str]`

- `project_id: Optional[str]`

- `status: Optional[Literal["pending", "processing", "completed", 2 more]]`

  Filter by job status (pending, processing, completed, failed, cancelled)

  - `"pending"`

  - `"processing"`

  - `"completed"`

  - `"failed"`

  - `"cancelled"`

### Returns

- `class SplitListResponse: …`

  Beta response — uses nested document_input object.

  - `id: str`

    Unique identifier for the split job.

  - `categories: List[SplitCategory]`

    Categories used for splitting.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

    Document that was split.

    - `type: str`

      Type of document input. Valid values are: file_id

    - `value: str`

      Document identifier.

  - `project_id: str`

    Project ID this job belongs to.

  - `status: str`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: str`

    User ID who created this job.

  - `configuration_id: Optional[str]`

    Split configuration ID used for this job.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error message if the job failed.

  - `result: Optional[SplitResultResponse]`

    Result of a completed split job.

    - `segments: List[SplitSegmentResponse]`

      List of document segments.

      - `category: str`

        Category name this split belongs to.

      - `confidence_category: str`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: List[int]`

        1-indexed page numbers in this split.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.split.list()
page = page.items[0]
print(page.id)
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "categories": [
        {
          "name": "x",
          "description": "x"
        }
      ],
      "document_input": {
        "type": "type",
        "value": "value"
      },
      "project_id": "project_id",
      "status": "status",
      "user_id": "user_id",
      "configuration_id": "configuration_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "result": {
        "segments": [
          {
            "category": "category",
            "confidence_category": "confidence_category",
            "pages": [
              0
            ]
          }
        ]
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
