# Images

## List File Page Screenshots

`client.Pipelines.Images.ListPageScreenshots(ctx, id, query) (*[]PipelineImageListPageScreenshotsResponse, error)`

**get** `/api/v1/files/{id}/page_screenshots`

List metadata for all screenshots of pages from a file.

### Parameters

- `id string`

- `query PipelineImageListPageScreenshotsParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type PipelineImageListPageScreenshotsResponse []PipelineImageListPageScreenshotsResponse`

  - `FileID string`

    The ID of the file that the page screenshot was taken from

  - `ImageSize int64`

    The size of the image in bytes

  - `PageIndex int64`

    The index of the page for which the screenshot is taken (0-indexed)

  - `Metadata map[string, any]`

    Metadata for the screenshot

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
  response, err := client.Pipelines.Images.ListPageScreenshots(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineImageListPageScreenshotsParams{

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
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "image_size": 0,
    "page_index": 0,
    "metadata": {
      "foo": "bar"
    }
  }
]
```

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
