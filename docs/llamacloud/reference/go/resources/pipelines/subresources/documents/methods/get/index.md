## Get Pipeline Document

`client.Pipelines.Documents.Get(ctx, documentID, query) (*CloudDocument, error)`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Parameters

- `documentID string`

- `query PipelineDocumentGetParams`

  - `PipelineID param.Field[string]`

### Returns

- `type CloudDocument struct{…}`

  Cloud document stored in S3.

  - `ID string`

  - `Metadata map[string, any]`

  - `Text string`

  - `ExcludedEmbedMetadataKeys []string`

  - `ExcludedLlmMetadataKeys []string`

  - `PagePositions []int64`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `StatusMetadata map[string, any]`

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
  cloudDocument, err := client.Pipelines.Documents.Get(
    context.TODO(),
    "document_id",
    llamacloudprod.PipelineDocumentGetParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", cloudDocument.ID)
}
```

#### Response

```json
{
  "id": "id",
  "metadata": {
    "foo": "bar"
  },
  "text": "text",
  "excluded_embed_metadata_keys": [
    "string"
  ],
  "excluded_llm_metadata_keys": [
    "string"
  ],
  "page_positions": [
    0
  ],
  "status_metadata": {
    "foo": "bar"
  }
}
```
