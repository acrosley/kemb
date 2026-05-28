## Retrieve

`client.Retrievers.Retriever.Search(ctx, retrieverID, params) (*CompositeRetrievalResult, error)`

**post** `/api/v1/retrievers/{retriever_id}/retrieve`

Retrieve data using a Retriever.

### Parameters

- `retrieverID string`

- `params RetrieverRetrieverSearchParams`

  - `Query param.Field[string]`

    Body param: The query to retrieve against.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Mode param.Field[CompositeRetrievalMode]`

    Body param: The mode of composite retrieval.

  - `RerankConfig param.Field[ReRankConfig]`

    Body param: The rerank configuration for composite retrieval.

  - `RerankTopN param.Field[int64]`

    Body param: (use rerank_config.top_n instead) The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

### Returns

- `type CompositeRetrievalResult struct{…}`

  - `ImageNodes []PageScreenshotNodeWithScore`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `Node PageScreenshotNodeWithScoreNode`

      - `FileID string`

        The ID of the file that the page screenshot was taken from

      - `ImageSize int64`

        The size of the image in bytes

      - `PageIndex int64`

        The index of the page for which the screenshot is taken (0-indexed)

      - `Metadata map[string, any]`

        Metadata for the screenshot

    - `Score float64`

      The score of the screenshot node

    - `ClassName string`

  - `Nodes []CompositeRetrievalResultNode`

    The retrieved nodes from the composite retrieval.

    - `Node CompositeRetrievalResultNodeNode`

      - `ID string`

        The ID of the retrieved node.

      - `EndCharIdx int64`

        The end character index of the retrieved node in the document

      - `PipelineID string`

        The ID of the pipeline this node was retrieved from.

      - `RetrieverID string`

        The ID of the retriever this node was retrieved from.

      - `RetrieverPipelineName string`

        The name of the retrieval pipeline this node was retrieved from.

      - `StartCharIdx int64`

        The start character index of the retrieved node in the document

      - `Text string`

        The text of the retrieved node.

      - `Metadata map[string, any]`

        Metadata associated with the retrieved node.

    - `ClassName string`

    - `Score float64`

  - `PageFigureNodes []PageFigureNodeWithScore`

    The page figure nodes retrieved by the pipeline for the given query.

    - `Node PageFigureNodeWithScoreNode`

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

    - `Score float64`

      The score of the figure node

    - `ClassName string`

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
  compositeRetrievalResult, err := client.Retrievers.Retriever.Search(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.RetrieverRetrieverSearchParams{
      Query: "x",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", compositeRetrievalResult.ImageNodes)
}
```

#### Response

```json
{
  "image_nodes": [
    {
      "node": {
        "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "image_size": 0,
        "page_index": 0,
        "metadata": {
          "foo": "bar"
        }
      },
      "score": 0,
      "class_name": "class_name"
    }
  ],
  "nodes": [
    {
      "node": {
        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "end_char_idx": 0,
        "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "retriever_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "retriever_pipeline_name": "retriever_pipeline_name",
        "start_char_idx": 0,
        "text": "text",
        "metadata": {
          "foo": "bar"
        }
      },
      "class_name": "class_name",
      "score": 0
    }
  ],
  "page_figure_nodes": [
    {
      "node": {
        "confidence": 0,
        "figure_name": "figure_name",
        "figure_size": 0,
        "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "page_index": 0,
        "is_likely_noise": true,
        "metadata": {
          "foo": "bar"
        }
      },
      "score": 0,
      "class_name": "class_name"
    }
  ]
}
```
