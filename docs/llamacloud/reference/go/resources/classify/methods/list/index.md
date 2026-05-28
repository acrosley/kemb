## List Classify Jobs

`client.Classify.List(ctx, query) (*PaginatedCursor[ClassifyListResponse], error)`

**get** `/api/v2/classify`

List classify jobs with optional filtering and pagination.

Filter by `status`, `configuration_id`, specific `job_ids`,
or creation date range.

### Parameters

- `query ClassifyListParams`

  - `ConfigurationID param.Field[string]`

    Filter by configuration ID

  - `CreatedAtOnOrAfter param.Field[Time]`

    Include items created at or after this timestamp (inclusive)

  - `CreatedAtOnOrBefore param.Field[Time]`

    Include items created at or before this timestamp (inclusive)

  - `JobIDs param.Field[[]string]`

    Filter by specific job IDs

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

    Number of items per page

  - `PageToken param.Field[string]`

    Token for pagination

  - `ProjectID param.Field[string]`

  - `Status param.Field[ClassifyListParamsStatus]`

    Filter by job status

    - `const ClassifyListParamsStatusPending ClassifyListParamsStatus = "PENDING"`

    - `const ClassifyListParamsStatusRunning ClassifyListParamsStatus = "RUNNING"`

    - `const ClassifyListParamsStatusCompleted ClassifyListParamsStatus = "COMPLETED"`

    - `const ClassifyListParamsStatusFailed ClassifyListParamsStatus = "FAILED"`

### Returns

- `type ClassifyListResponse struct{…}`

  Response for a classify job.

  - `ID string`

    Unique identifier

  - `Configuration ClassifyConfiguration`

    Classify configuration used for this job

    - `Rules []ClassifyConfigurationRule`

      Classify rules to evaluate against the document (at least one required)

      - `Description string`

        Natural language criteria for matching this rule

      - `Type string`

        Document type to assign when rule matches

    - `Mode ClassifyConfigurationMode`

      Classify execution mode

      - `const ClassifyConfigurationModeFast ClassifyConfigurationMode = "FAST"`

    - `ParsingConfiguration ClassifyConfigurationParsingConfiguration`

      Parsing configuration for classify jobs.

      - `Lang string`

        ISO 639-1 language code for the document

      - `MaxPages int64`

        Maximum number of pages to process. Omit for no limit.

      - `TargetPages string`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `DocumentInputType ClassifyListResponseDocumentInputType`

    Whether the input was a file or parse job (FILE or PARSE_JOB)

    - `const ClassifyListResponseDocumentInputTypeURL ClassifyListResponseDocumentInputType = "url"`

    - `const ClassifyListResponseDocumentInputTypeFileID ClassifyListResponseDocumentInputType = "file_id"`

    - `const ClassifyListResponseDocumentInputTypeParseJobID ClassifyListResponseDocumentInputType = "parse_job_id"`

  - `FileInput string`

    ID of the input file or parse job

  - `ProjectID string`

    Project this job belongs to

  - `Status ClassifyListResponseStatus`

    Current job status: PENDING, RUNNING, COMPLETED, or FAILED

    - `const ClassifyListResponseStatusPending ClassifyListResponseStatus = "PENDING"`

    - `const ClassifyListResponseStatusRunning ClassifyListResponseStatus = "RUNNING"`

    - `const ClassifyListResponseStatusCompleted ClassifyListResponseStatus = "COMPLETED"`

    - `const ClassifyListResponseStatusFailed ClassifyListResponseStatus = "FAILED"`

  - `UserID string`

    User who created this job

  - `ConfigurationID string`

    Product configuration ID

  - `CreatedAt Time`

    Creation datetime

  - `ErrorMessage string`

    Error message if job failed

  - `ParseJobID string`

    Associated parse job ID

  - `Result ClassifyResult`

    Result of classifying a document.

    - `Confidence float64`

      Confidence score between 0.0 and 1.0

    - `Reasoning string`

      Why the document matched (or didn't match) the returned rule

    - `Type string`

      Matched rule type, or null if no rule matched

  - `TransactionID string`

    Idempotency key

  - `UpdatedAt Time`

    Update datetime

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Classify.List(context.TODO(), llamacloudprod.ClassifyListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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
