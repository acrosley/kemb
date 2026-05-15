## Paginated List Pipeline Documents

`client.Pipelines.Documents.List(ctx, pipelineID, query) (*PaginatedCloudDocuments[CloudDocument], error)`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `pipelineID string`

- `query PipelineDocumentListParams`

  - `FileID param.Field[string]`

  - `Limit param.Field[int64]`

  - `OnlyAPIDataSourceDocuments param.Field[bool]`

  - `OnlyDirectUpload param.Field[bool]`

  - `Skip param.Field[int64]`

  - `StatusRefreshPolicy param.Field[PipelineDocumentListParamsStatusRefreshPolicy]`

    - `const PipelineDocumentListParamsStatusRefreshPolicyCached PipelineDocumentListParamsStatusRefreshPolicy = "cached"`

    - `const PipelineDocumentListParamsStatusRefreshPolicyTtl PipelineDocumentListParamsStatusRefreshPolicy = "ttl"`

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
  page, err := client.Pipelines.Documents.List(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDocumentListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "documents": [
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
  ],
  "limit": 0,
  "offset": 0,
  "total_count": 0
}
```
