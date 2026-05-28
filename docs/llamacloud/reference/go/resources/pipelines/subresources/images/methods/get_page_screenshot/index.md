## Get File Page Screenshot

`client.Pipelines.Images.GetPageScreenshot(ctx, pageIndex, params) (*PipelineImageGetPageScreenshotResponse, error)`

**get** `/api/v1/files/{id}/page_screenshots/{page_index}`

Get screenshot of a page from a file.

### Parameters

- `pageIndex int64`

- `params PipelineImageGetPageScreenshotParams`

  - `ID param.Field[string]`

    Path param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

### Returns

- `type PipelineImageGetPageScreenshotResponse interface{…}`

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
  response, err := client.Pipelines.Images.GetPageScreenshot(
    context.TODO(),
    0,
    llamacloudprod.PipelineImageGetPageScreenshotParams{
      ID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
