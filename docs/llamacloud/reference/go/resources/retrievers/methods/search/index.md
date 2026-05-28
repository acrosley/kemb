## Direct Retrieve

`client.Retrievers.Search(ctx, params) (*CompositeRetrievalResult, error)`

**post** `/api/v1/retrievers/retrieve`

Retrieve data using specified pipelines without creating a persistent retriever.

### Parameters

- `params RetrieverSearchParams`

  - `Query param.Field[string]`

    Body param: The query to retrieve against.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Mode param.Field[CompositeRetrievalMode]`

    Body param: The mode of composite retrieval.

  - `Pipelines param.Field[[]RetrieverPipeline]`

    Body param: The pipelines to use for retrieval.

    - `Description string`

      A description of the retriever tool.

    - `Name string`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `PipelineID string`

      The ID of the pipeline this tool uses.

    - `PresetRetrievalParameters PresetRetrievalParamsResp`

      Parameters for retrieval configuration.

      - `Alpha float64`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `ClassName string`

      - `DenseSimilarityCutoff float64`

        Minimum similarity score wrt query for retrieval

      - `DenseSimilarityTopK int64`

        Number of nodes for dense retrieval.

      - `EnableReranking bool`

        Enable reranking for retrieval

      - `FilesTopK int64`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `RerankTopN int64`

        Number of reranked nodes for returning.

      - `RetrievalMode RetrievalMode`

        The retrieval mode for the query.

        - `const RetrievalModeChunks RetrievalMode = "chunks"`

        - `const RetrievalModeFilesViaMetadata RetrievalMode = "files_via_metadata"`

        - `const RetrievalModeFilesViaContent RetrievalMode = "files_via_content"`

        - `const RetrievalModeAutoRouted RetrievalMode = "auto_routed"`

      - `RetrieveImageNodes bool`

        Whether to retrieve image nodes.

      - `RetrievePageFigureNodes bool`

        Whether to retrieve page figure nodes.

      - `RetrievePageScreenshotNodes bool`

        Whether to retrieve page screenshot nodes.

      - `SearchFilters MetadataFilters`

        Metadata filters for vector stores.

        - `Filters []MetadataFiltersFilterUnion`

          - `type MetadataFiltersFilterMetadataFilter struct{…}`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `Key string`

            - `Value MetadataFiltersFilterMetadataFilterValueUnion`

              - `float64`

              - `string`

              - `type MetadataFiltersFilterMetadataFilterValueArray []string`

              - `type MetadataFiltersFilterMetadataFilterValueArray []float64`

              - `type MetadataFiltersFilterMetadataFilterValueArray []int64`

            - `Operator string`

              Vector store filter operator.

              - `const MetadataFiltersFilterMetadataFilterOperatorEquals MetadataFiltersFilterMetadataFilterOperator = "=="`

              - `const MetadataFiltersFilterMetadataFilterOperatorGreater MetadataFiltersFilterMetadataFilterOperator = ">"`

              - `const MetadataFiltersFilterMetadataFilterOperatorLess MetadataFiltersFilterMetadataFilterOperator = "<"`

              - `const MetadataFiltersFilterMetadataFilterOperatorNotEquals MetadataFiltersFilterMetadataFilterOperator = "!="`

              - `const MetadataFiltersFilterMetadataFilterOperatorGreaterOrEquals MetadataFiltersFilterMetadataFilterOperator = ">="`

              - `const MetadataFiltersFilterMetadataFilterOperatorLessOrEquals MetadataFiltersFilterMetadataFilterOperator = "<="`

              - `const MetadataFiltersFilterMetadataFilterOperatorIn MetadataFiltersFilterMetadataFilterOperator = "in"`

              - `const MetadataFiltersFilterMetadataFilterOperatorNin MetadataFiltersFilterMetadataFilterOperator = "nin"`

              - `const MetadataFiltersFilterMetadataFilterOperatorAny MetadataFiltersFilterMetadataFilterOperator = "any"`

              - `const MetadataFiltersFilterMetadataFilterOperatorAll MetadataFiltersFilterMetadataFilterOperator = "all"`

              - `const MetadataFiltersFilterMetadataFilterOperatorTextMatch MetadataFiltersFilterMetadataFilterOperator = "text_match"`

              - `const MetadataFiltersFilterMetadataFilterOperatorTextMatchInsensitive MetadataFiltersFilterMetadataFilterOperator = "text_match_insensitive"`

              - `const MetadataFiltersFilterMetadataFilterOperatorContains MetadataFiltersFilterMetadataFilterOperator = "contains"`

              - `const MetadataFiltersFilterMetadataFilterOperatorIsEmpty MetadataFiltersFilterMetadataFilterOperator = "is_empty"`

          - `type MetadataFilters struct{…}`

            Metadata filters for vector stores.

        - `Condition MetadataFiltersCondition`

          Vector store filter conditions to combine different filters.

          - `const MetadataFiltersConditionAnd MetadataFiltersCondition = "and"`

          - `const MetadataFiltersConditionOr MetadataFiltersCondition = "or"`

          - `const MetadataFiltersConditionNot MetadataFiltersCondition = "not"`

      - `SearchFiltersInferenceSchema map[string, PresetRetrievalParamsSearchFiltersInferenceSchemaUnionResp]`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `type PresetRetrievalParamsSearchFiltersInferenceSchemaMap map[string, any]`

        - `type PresetRetrievalParamsSearchFiltersInferenceSchemaArray []any`

        - `string`

        - `float64`

        - `bool`

      - `SparseSimilarityTopK int64`

        Number of nodes for sparse retrieval.

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
  compositeRetrievalResult, err := client.Retrievers.Search(context.TODO(), llamacloudprod.RetrieverSearchParams{
    Query: "x",
  })
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
