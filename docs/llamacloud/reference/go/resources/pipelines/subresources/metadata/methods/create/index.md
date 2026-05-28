## Import Pipeline Metadata

`client.Pipelines.Metadata.New(ctx, pipelineID, body) (*PipelineMetadataNewResponse, error)`

**put** `/api/v1/pipelines/{pipeline_id}/metadata`

Import metadata for a pipeline.

### Parameters

- `pipelineID string`

- `body PipelineMetadataNewParams`

  - `UploadFile param.Field[Reader]`

### Returns

- `type PipelineMetadataNewResponse map[string, string]`

### Example

```go
package main

import (
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  metadata, err := client.Pipelines.Metadata.New(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineMetadataNewParams{
      UploadFile: io.Reader(bytes.NewBuffer([]byte("Example data"))),
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", metadata)
}
```

#### Response

```json
{
  "foo": "string"
}
```
