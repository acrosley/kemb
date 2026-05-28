## Delete Spreadsheet Job

`client.Beta.Sheets.DeleteJob(ctx, spreadsheetJobID, body) (*BetaSheetDeleteJobResponse, error)`

**delete** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Delete a spreadsheet parsing job and its associated data.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheetJobID string`

- `body BetaSheetDeleteJobParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type BetaSheetDeleteJobResponse interface{…}`

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
  response, err := client.Beta.Sheets.DeleteJob(
    context.TODO(),
    "spreadsheet_job_id",
    llamacloudprod.BetaSheetDeleteJobParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

#### Response

```json
{}
```
