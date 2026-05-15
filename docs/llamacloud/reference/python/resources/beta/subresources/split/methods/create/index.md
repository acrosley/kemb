## Create Split Job

`beta.split.create(SplitCreateParams**kwargs)  -> SplitCreateResponse`

**post** `/api/v1/beta/split/jobs`

Create a document split job.

### Parameters

- `document_input: SplitDocumentInputParam`

  Document to be split.

  - `type: str`

    Type of document input. Valid values are: file_id

  - `value: str`

    Document identifier.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `configuration: Optional[Configuration]`

  Split configuration with categories and splitting strategy.

  - `categories: Iterable[SplitCategoryParam]`

    Categories to split documents into.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `splitting_strategy: Optional[ConfigurationSplittingStrategy]`

    Strategy for splitting documents.

    - `allow_uncategorized: Optional[Literal["include", "forbid", "omit"]]`

      Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

      - `"include"`

      - `"forbid"`

      - `"omit"`

- `configuration_id: Optional[str]`

  Saved split configuration ID.

### Returns

- `class SplitCreateResponse: …`

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
split = client.beta.split.create(
    document_input={
        "type": "type",
        "value": "value",
    },
)
print(split.id)
```

#### Response

```json
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
```
