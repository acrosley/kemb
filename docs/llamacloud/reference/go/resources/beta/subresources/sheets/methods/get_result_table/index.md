## Get Result Region

`client.Beta.Sheets.GetResultTable(ctx, regionType, params) (*PresignedURL, error)`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}`

Generate a presigned URL to download a specific extracted region.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `regionType BetaSheetGetResultTableParamsRegionType`

  - `const BetaSheetGetResultTableParamsRegionTypeTable BetaSheetGetResultTableParamsRegionType = "table"`

  - `const BetaSheetGetResultTableParamsRegionTypeExtra BetaSheetGetResultTableParamsRegionType = "extra"`

  - `const BetaSheetGetResultTableParamsRegionTypeCellMetadata BetaSheetGetResultTableParamsRegionType = "cell_metadata"`

- `params BetaSheetGetResultTableParams`

  - `SpreadsheetJobID param.Field[string]`

    Path param

  - `RegionID param.Field[string]`

    Path param

  - `ExpiresAtSeconds param.Field[int64]`

    Query param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

### Returns

- `type PresignedURL struct{…}`

  Schema for a presigned URL.

  - `ExpiresAt Time`

    The time at which the presigned URL expires

  - `URL string`

    A presigned URL for IO operations against a private file

  - `FormFields map[string, string]`

    Form fields for a presigned POST request

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
  presignedURL, err := client.Beta.Sheets.GetResultTable(
    context.TODO(),
    llamacloudprod.BetaSheetGetResultTableParamsRegionTypeTable,
    llamacloudprod.BetaSheetGetResultTableParams{
      SpreadsheetJobID: "spreadsheet_job_id",
      RegionID: "region_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", presignedURL.ExpiresAt)
}
```

#### Response

```json
{
  "expires_at": "2019-12-27T18:11:19.117Z",
  "url": "https://example.com",
  "form_fields": {
    "foo": "string"
  }
}
```
