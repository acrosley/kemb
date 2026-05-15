## Create Split Job

`client.Beta.Split.New(ctx, params) (*BetaSplitNewResponse, error)`

**post** `/api/v1/beta/split/jobs`

Create a document split job.

### Parameters

- `params BetaSplitNewParams`

  - `DocumentInput param.Field[SplitDocumentInput]`

    Body param: Document to be split.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Configuration param.Field[BetaSplitNewParamsConfiguration]`

    Body param: Split configuration with categories and splitting strategy.

    - `Categories []SplitCategory`

      Categories to split documents into.

      - `Name string`

        Name of the category.

      - `Description string`

        Optional description of what content belongs in this category.

    - `SplittingStrategy BetaSplitNewParamsConfigurationSplittingStrategy`

      Strategy for splitting documents.

      - `AllowUncategorized string`

        Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

        - `const BetaSplitNewParamsConfigurationSplittingStrategyAllowUncategorizedInclude BetaSplitNewParamsConfigurationSplittingStrategyAllowUncategorized = "include"`

        - `const BetaSplitNewParamsConfigurationSplittingStrategyAllowUncategorizedForbid BetaSplitNewParamsConfigurationSplittingStrategyAllowUncategorized = "forbid"`

        - `const BetaSplitNewParamsConfigurationSplittingStrategyAllowUncategorizedOmit BetaSplitNewParamsConfigurationSplittingStrategyAllowUncategorized = "omit"`

  - `ConfigurationID param.Field[string]`

    Body param: Saved split configuration ID.

### Returns

- `type BetaSplitNewResponse struct{…}`

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
  split, err := client.Beta.Split.New(context.TODO(), llamacloudprod.BetaSplitNewParams{
    DocumentInput: llamacloudprod.SplitDocumentInputParam{
      Type: "type",
      Value: "value",
    },
  })
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
