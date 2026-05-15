## List File Pages Figures

`client.Pipelines.Images.ListPageFigures(ctx, id, query) (*[]PipelineImageListPageFiguresResponse, error)`

**get** `/api/v1/files/{id}/page-figures`

List metadata for all figures from all pages of a file.

### Parameters

- `id string`

- `query PipelineImageListPageFiguresParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type PipelineImageListPageFiguresResponse []PipelineImageListPageFiguresResponse`

  - `Confidence float64`

    The confidence of the figure

  - `FigureName string`

    The name of the figure

  - `FigureSize int64`

    The size of the figure in bytes

  - `FileID string`

    The ID of the file that the figure was taken from

  - `PageIndex int64`

    The index of the page for which the figure is taken (0-indexed)

  - `IsLikelyNoise bool`

    Whether the figure is likely to be noise

  - `Metadata map[string, any]`

    Metadata for the figure

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
  response, err := client.Pipelines.Images.ListPageFigures(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineImageListPageFiguresParams{

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
[
  {
    "confidence": 0,
    "figure_name": "figure_name",
    "figure_size": 0,
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "page_index": 0,
    "is_likely_noise": true,
    "metadata": {
      "foo": "bar"
    }
  }
]
```
