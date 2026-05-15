## Get Split Job

`client.Beta.Split.Get(ctx, splitJobID, query) (*BetaSplitGetResponse, error)`

**get** `/api/v1/beta/split/jobs/{split_job_id}`

Get a document split job.

### Parameters

- `splitJobID string`

- `query BetaSplitGetParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type BetaSplitGetResponse struct{…}`

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
  split, err := client.Beta.Split.Get(
    context.TODO(),
    "split_job_id",
    llamacloudprod.BetaSplitGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", split.ID)
}
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
