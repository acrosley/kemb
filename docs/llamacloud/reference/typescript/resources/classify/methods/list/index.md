## List Classify Jobs

`client.classify.list(ClassifyListParamsquery?, RequestOptionsoptions?): PaginatedCursor<ClassifyListResponse>`

**get** `/api/v2/classify`

List classify jobs with optional filtering and pagination.

Filter by `status`, `configuration_id`, specific `job_ids`,
or creation date range.

### Parameters

- `query: ClassifyListParams`

  - `configuration_id?: string | null`

    Filter by configuration ID

  - `created_at_on_or_after?: string | null`

    Include items created at or after this timestamp (inclusive)

  - `created_at_on_or_before?: string | null`

    Include items created at or before this timestamp (inclusive)

  - `job_ids?: Array<string> | null`

    Filter by specific job IDs

  - `organization_id?: string | null`

  - `page_size?: number | null`

    Number of items per page

  - `page_token?: string | null`

    Token for pagination

  - `project_id?: string | null`

  - `status?: "PENDING" | "RUNNING" | "COMPLETED" | "FAILED" | null`

    Filter by job status

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

### Returns

- `ClassifyListResponse`

  Response for a classify job.

  - `id: string`

    Unique identifier

  - `configuration: ClassifyConfiguration`

    Classify configuration used for this job

    - `rules: Array<Rule>`

      Classify rules to evaluate against the document (at least one required)

      - `description: string`

        Natural language criteria for matching this rule

      - `type: string`

        Document type to assign when rule matches

    - `mode?: "FAST"`

      Classify execution mode

      - `"FAST"`

    - `parsing_configuration?: ParsingConfiguration | null`

      Parsing configuration for classify jobs.

      - `lang?: string`

        ISO 639-1 language code for the document

      - `max_pages?: number | null`

        Maximum number of pages to process. Omit for no limit.

      - `target_pages?: string | null`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `document_input_type: "url" | "file_id" | "parse_job_id"`

    Whether the input was a file or parse job (FILE or PARSE_JOB)

    - `"url"`

    - `"file_id"`

    - `"parse_job_id"`

  - `file_input: string`

    ID of the input file or parse job

  - `project_id: string`

    Project this job belongs to

  - `status: "PENDING" | "RUNNING" | "COMPLETED" | "FAILED"`

    Current job status: PENDING, RUNNING, COMPLETED, or FAILED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

  - `user_id: string`

    User who created this job

  - `configuration_id?: string | null`

    Product configuration ID

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error message if job failed

  - `parse_job_id?: string | null`

    Associated parse job ID

  - `result?: ClassifyResult | null`

    Result of classifying a document.

    - `confidence: number`

      Confidence score between 0.0 and 1.0

    - `reasoning: string`

      Why the document matched (or didn't match) the returned rule

    - `type: string | null`

      Matched rule type, or null if no rule matched

  - `transaction_id?: string | null`

    Idempotency key

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const classifyListResponse of client.classify.list()) {
  console.log(classifyListResponse.id);
}
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
