## List Classify Jobs

`classify.list(ClassifyListParams**kwargs)  -> SyncPaginatedCursor[ClassifyListResponse]`

**get** `/api/v2/classify`

List classify jobs with optional filtering and pagination.

Filter by `status`, `configuration_id`, specific `job_ids`,
or creation date range.

### Parameters

- `configuration_id: Optional[str]`

  Filter by configuration ID

- `created_at_on_or_after: Optional[Union[str, datetime, null]]`

  Include items created at or after this timestamp (inclusive)

- `created_at_on_or_before: Optional[Union[str, datetime, null]]`

  Include items created at or before this timestamp (inclusive)

- `job_ids: Optional[SequenceNotStr[str]]`

  Filter by specific job IDs

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

  Number of items per page

- `page_token: Optional[str]`

  Token for pagination

- `project_id: Optional[str]`

- `status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]]`

  Filter by job status

  - `"PENDING"`

  - `"RUNNING"`

  - `"COMPLETED"`

  - `"FAILED"`

### Returns

- `class ClassifyListResponse: …`

  Response for a classify job.

  - `id: str`

    Unique identifier

  - `configuration: ClassifyConfiguration`

    Classify configuration used for this job

    - `rules: List[Rule]`

      Classify rules to evaluate against the document (at least one required)

      - `description: str`

        Natural language criteria for matching this rule

      - `type: str`

        Document type to assign when rule matches

    - `mode: Optional[Literal["FAST"]]`

      Classify execution mode

      - `"FAST"`

    - `parsing_configuration: Optional[ParsingConfiguration]`

      Parsing configuration for classify jobs.

      - `lang: Optional[str]`

        ISO 639-1 language code for the document

      - `max_pages: Optional[int]`

        Maximum number of pages to process. Omit for no limit.

      - `target_pages: Optional[str]`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `document_input_type: Literal["url", "file_id", "parse_job_id"]`

    Whether the input was a file or parse job (FILE or PARSE_JOB)

    - `"url"`

    - `"file_id"`

    - `"parse_job_id"`

  - `file_input: str`

    ID of the input file or parse job

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]`

    Current job status: PENDING, RUNNING, COMPLETED, or FAILED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

  - `user_id: str`

    User who created this job

  - `configuration_id: Optional[str]`

    Product configuration ID

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error message if job failed

  - `parse_job_id: Optional[str]`

    Associated parse job ID

  - `result: Optional[ClassifyResult]`

    Result of classifying a document.

    - `confidence: float`

      Confidence score between 0.0 and 1.0

    - `reasoning: str`

      Why the document matched (or didn't match) the returned rule

    - `type: Optional[str]`

      Matched rule type, or null if no rule matched

  - `transaction_id: Optional[str]`

    Idempotency key

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.classify.list()
page = page.items[0]
print(page.id)
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "configuration": {
        "rules": [
          {
            "description": "contains invoice number, line items, and total amount",
            "type": "invoice"
          }
        ],
        "mode": "FAST",
        "parsing_configuration": {
          "lang": "en",
          "max_pages": 10,
          "target_pages": "1,3,5-7"
        }
      },
      "document_input_type": "url",
      "file_input": "file_input",
      "project_id": "project_id",
      "status": "PENDING",
      "user_id": "user_id",
      "configuration_id": "configuration_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "parse_job_id": "parse_job_id",
      "result": {
        "confidence": 0,
        "reasoning": "reasoning",
        "type": "type"
      },
      "transaction_id": "transaction_id",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
