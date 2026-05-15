## Sync Pipeline Document

`client.Pipelines.Documents.Sync(ctx, documentID, body) (*PipelineDocumentSyncResponse, error)`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `documentID string`

- `body PipelineDocumentSyncParams`

  - `PipelineID param.Field[string]`

### Returns

- `type PipelineDocumentSyncResponse interface{…}`

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
  response, err := client.Pipelines.Documents.Sync(
    context.TODO(),
    "document_id",
    llamacloudprod.PipelineDocumentSyncParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
