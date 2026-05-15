## Create Classify Job

`$ llamacloud-prod classify create`

**post** `/api/v2/classify`

Create a classify job.

Classifies a document against a set of rules. Set `file_input`
to a file ID (`dfl-...`) or parse job ID (`pjb-...`), and provide
either inline `configuration` with rules or a `configuration_id`
referencing a saved preset.

Each rule has a `type` (the label to assign) and a `description`
(natural language criteria). The classifier returns the best
matching rule with a confidence score.

The job runs asynchronously. Poll `GET /classify/{job_id}` to
check status and retrieve results.

### Parameters

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--configuration: optional object { rules, mode, parsing_configuration }`

  Body param: Configuration for a classify job.

- `--configuration-id: optional string`

  Body param: Saved configuration ID

- `--file-id: optional string`

  Body param: Deprecated: use file_input instead

- `--file-input: optional string`

  Body param: File ID or parse job ID to classify

- `--parse-job-id: optional string`

  Body param: Deprecated: use file_input instead

- `--transaction-id: optional string`

  Body param: Idempotency key scoped to the project

### Returns

- `ClassifyNewResponse: object { id, configuration, document_input_type, 11 more }`

  Response for a classify job.

  - `id: string`

    Unique identifier

  - `configuration: object { rules, mode, parsing_configuration }`

    Classify configuration used for this job

    - `rules: array of object { description, type }`

      Classify rules to evaluate against the document (at least one required)

      - `description: string`

        Natural language criteria for matching this rule

      - `type: string`

        Document type to assign when rule matches

    - `mode: optional "FAST"`

      Classify execution mode

      - `"FAST"`

    - `parsing_configuration: optional object { lang, max_pages, target_pages }`

      Parsing configuration for classify jobs.

      - `lang: optional string`

        ISO 639-1 language code for the document

      - `max_pages: optional number`

        Maximum number of pages to process. Omit for no limit.

      - `target_pages: optional string`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `document_input_type: "url" or "file_id" or "parse_job_id"`

    Whether the input was a file or parse job (FILE or PARSE_JOB)

    - `"url"`

    - `"file_id"`

    - `"parse_job_id"`

  - `file_input: string`

    ID of the input file or parse job

  - `project_id: string`

    Project this job belongs to

  - `status: "PENDING" or "RUNNING" or "COMPLETED" or "FAILED"`

    Current job status: PENDING, RUNNING, COMPLETED, or FAILED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

  - `user_id: string`

    User who created this job

  - `configuration_id: optional string`

    Product configuration ID

  - `created_at: optional string`

    Creation datetime

  - `error_message: optional string`

    Error message if job failed

  - `parse_job_id: optional string`

    Associated parse job ID

  - `result: optional object { confidence, reasoning, type }`

    Result of classifying a document.

    - `confidence: number`

      Confidence score between 0.0 and 1.0

    - `reasoning: string`

      Why the document matched (or didn't match) the returned rule

    - `type: string`

      Matched rule type, or null if no rule matched

  - `transaction_id: optional string`

    Idempotency key

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod classify create \
  --api-key 'My API Key'
```

#### Response

```json
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
```
