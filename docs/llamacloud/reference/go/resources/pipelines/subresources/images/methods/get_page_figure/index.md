## Get File Page Figure

`client.Pipelines.Images.GetPageFigure(ctx, figureName, params) (*PipelineImageGetPageFigureResponse, error)`

**get** `/api/v1/files/{id}/page-figures/{page_index}/{figure_name}`

Get a specific figure from a page of a file.

### Parameters

- `figureName string`

- `params PipelineImageGetPageFigureParams`

  - `ID param.Field[string]`

    Path param

  - `PageIndex param.Field[int64]`

    Path param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

### Returns

- `type PipelineImageGetPageFigureResponse interface{…}`

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
  response, err := client.Pipelines.Images.GetPageFigure(
    context.TODO(),
    "figure_name",
    llamacloudprod.PipelineImageGetPageFigureParams{
      ID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      PageIndex: 0,
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
