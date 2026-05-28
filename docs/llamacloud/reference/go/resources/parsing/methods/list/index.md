## List Parse Jobs

`client.Parsing.List(ctx, query) (*PaginatedCursor[ParsingListResponse], error)`

**get** `/api/v2/parse`

List parse jobs for the current project.

Filter by `status` or creation date range. Results are
paginated — use `page_token` from the response to fetch
subsequent pages.

### Parameters

- `query ParsingListParams`

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

  - `Status param.Field[ParsingListParamsStatus]`

    Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

    - `const ParsingListParamsStatusPending ParsingListParamsStatus = "PENDING"`

    - `const ParsingListParamsStatusRunning ParsingListParamsStatus = "RUNNING"`

    - `const ParsingListParamsStatusCompleted ParsingListParamsStatus = "COMPLETED"`

    - `const ParsingListParamsStatusFailed ParsingListParamsStatus = "FAILED"`

    - `const ParsingListParamsStatusCancelled ParsingListParamsStatus = "CANCELLED"`

### Returns

- `type ParsingListResponse struct{…}`

  A parse job.

  - `ID string`

    Unique parse job identifier

  - `ProjectID string`

    Project this job belongs to

  - `Status ParsingListResponseStatus`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `const ParsingListResponseStatusPending ParsingListResponseStatus = "PENDING"`

    - `const ParsingListResponseStatusRunning ParsingListResponseStatus = "RUNNING"`

    - `const ParsingListResponseStatusCompleted ParsingListResponseStatus = "COMPLETED"`

    - `const ParsingListResponseStatusFailed ParsingListResponseStatus = "FAILED"`

    - `const ParsingListResponseStatusCancelled ParsingListResponseStatus = "CANCELLED"`

  - `CreatedAt Time`

    Creation datetime

  - `ErrorMessage string`

    Error details when status is FAILED

  - `Name string`

    Optional display name for this parse job

  - `Tier string`

    Parsing tier used for this job

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
  page, err := client.Parsing.List(context.TODO(), llamacloudprod.ParsingListParams{

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
      "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "status": "PENDING",
      "created_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "name": "Q4 Financial Report",
      "tier": "fast",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
