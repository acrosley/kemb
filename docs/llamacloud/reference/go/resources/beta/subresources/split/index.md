# Split

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

## Domain Types

### Split Category

- `type SplitCategory struct{…}`

  Category definition for document splitting.

  - `Name string`

    Name of the category.

  - `Description string`

    Optional description of what content belongs in this category.

### Split Document Input

- `type SplitDocumentInput struct{…}`

  Document input specification for beta API.

  - `Type string`

    Type of document input. Valid values are: file_id

  - `Value string`

    Document identifier.

### Split Result Response

- `type SplitResultResponse struct{…}`

  Result of a completed split job.

  - `Segments []SplitSegmentResponse`

    List of document segments.

    - `Category string`

      Category name this split belongs to.

    - `ConfidenceCategory string`

      Categorical confidence level. Valid values are: high, medium, low.

    - `Pages []int64`

      1-indexed page numbers in this split.

### Split Segment Response

- `type SplitSegmentResponse struct{…}`

  A segment of the split document.

  - `Category string`

    Category name this split belongs to.

  - `ConfidenceCategory string`

    Categorical confidence level. Valid values are: high, medium, low.

  - `Pages []int64`

    1-indexed page numbers in this split.
