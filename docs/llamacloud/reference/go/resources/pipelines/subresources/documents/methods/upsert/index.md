## Upsert Batch Pipeline Documents

`client.Pipelines.Documents.Upsert(ctx, pipelineID, body) (*[]CloudDocument, error)`

**put** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create or update a document for a pipeline.

### Parameters

- `pipelineID string`

- `body PipelineDocumentUpsertParams`

  - `Body param.Field[[]CloudDocumentCreate]`

    - `Metadata map[string, any]`

    - `Text string`

    - `ID string`

    - `ExcludedEmbedMetadataKeys []string`

    - `ExcludedLlmMetadataKeys []string`

    - `PagePositions []int64`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `type PipelineDocumentUpsertResponse []CloudDocument`

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
  cloudDocuments, err := client.Pipelines.Documents.Upsert(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDocumentUpsertParams{
      Body: []llamacloudprod.CloudDocumentCreateParam{llamacloudprod.CloudDocumentCreateParam{
        Metadata: map[string]any{
        "foo": "bar",
        },
        Text: "text",
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", cloudDocuments)
}
```

#### Response

```json
[
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
]
```
