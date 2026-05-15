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
