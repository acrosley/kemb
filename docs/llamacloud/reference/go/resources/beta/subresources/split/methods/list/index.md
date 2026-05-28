## List Split Jobs

`client.Beta.Split.List(ctx, query) (*PaginatedCursor[BetaSplitListResponse], error)`

**get** `/api/v1/beta/split/jobs`

List document split jobs.

### Parameters

- `query BetaSplitListParams`

  - `CreatedAtOnOrAfter param.Field[Time]`

    Include items created at or after this timestamp (inclusive)

  - `CreatedAtOnOrBefore param.Field[Time]`

    Include items created at or before this timestamp (inclusive)

  - `JobIDs param.Field[[]string]`

    Filter by specific job IDs

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

  - `PageToken param.Field[string]`

  - `ProjectID param.Field[string]`

  - `Status param.Field[BetaSplitListParamsStatus]`

    Filter by job status (pending, processing, completed, failed, cancelled)

    - `const BetaSplitListParamsStatusPending BetaSplitListParamsStatus = "pending"`

    - `const BetaSplitListParamsStatusProcessing BetaSplitListParamsStatus = "processing"`

    - `const BetaSplitListParamsStatusCompleted BetaSplitListParamsStatus = "completed"`

    - `const BetaSplitListParamsStatusFailed BetaSplitListParamsStatus = "failed"`

    - `const BetaSplitListParamsStatusCancelled BetaSplitListParamsStatus = "cancelled"`

### Returns

- `type BetaSplitListResponse struct{…}`

  Beta response — uses nested document_input object.

  - `ID string`

    Unique identifier for the split job.

  - `Categories []SplitCategory`

    Categories used for splitting.

    - `Name string`

      Name of the category.

    - `Description string`

      Optional description of what content belongs in this category.

  - `DocumentInput SplitDocumentInput`

    Document that was split.

    - `Type string`

      Type of document input. Valid values are: file_id

    - `Value string`

      Document identifier.

  - `ProjectID string`

    Project ID this job belongs to.

  - `Status string`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `UserID string`

    User ID who created this job.

  - `ConfigurationID string`

    Split configuration ID used for this job.

  - `CreatedAt Time`

    Creation datetime

  - `ErrorMessage string`

    Error message if the job failed.

  - `Result SplitResultResponse`

    Result of a completed split job.

    - `Segments []SplitSegmentResponse`

      List of document segments.

      - `Category string`

        Category name this split belongs to.

      - `ConfidenceCategory string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `Pages []int64`

        1-indexed page numbers in this split.

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
  page, err := client.Beta.Split.List(context.TODO(), llamacloudprod.BetaSplitListParams{

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
