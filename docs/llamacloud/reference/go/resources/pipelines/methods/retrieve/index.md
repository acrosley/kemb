## Run Search

`client.Pipelines.Get(ctx, pipelineID, params) (*PipelineGetResponse, error)`

**post** `/api/v1/pipelines/{pipeline_id}/retrieve`

Run a retrieval query against a managed pipeline.

Searches the pipeline's vector store using the provided query
and retrieval parameters. Supports dense, sparse, and hybrid
search modes with configurable top-k and reranking.

### Parameters

- `pipelineID string`

- `params PipelineGetParams`

  - `Query param.Field[string]`

    Body param: The query to retrieve against.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Alpha param.Field[float64]`

    Body param: Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

  - `ClassName param.Field[string]`

    Body param

  - `DenseSimilarityCutoff param.Field[float64]`

    Body param: Minimum similarity score wrt query for retrieval

  - `DenseSimilarityTopK param.Field[int64]`

    Body param: Number of nodes for dense retrieval.

  - `EnableReranking param.Field[bool]`

    Body param: Enable reranking for retrieval

  - `FilesTopK param.Field[int64]`

    Body param: Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

  - `RerankTopN param.Field[int64]`

    Body param: Number of reranked nodes for returning.

  - `RetrievalMode param.Field[RetrievalMode]`

    Body param: The retrieval mode for the query.

  - `RetrieveImageNodes param.Field[bool]`

    Body param: Whether to retrieve image nodes.

  - `RetrievePageFigureNodes param.Field[bool]`

    Body param: Whether to retrieve page figure nodes.

  - `RetrievePageScreenshotNodes param.Field[bool]`

    Body param: Whether to retrieve page screenshot nodes.

  - `SearchFilters param.Field[MetadataFilters]`

    Body param: Metadata filters for vector stores.

  - `SearchFiltersInferenceSchema param.Field[map[string, PipelineGetParamsSearchFiltersInferenceSchemaUnion]]`

    Body param: JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

    - `type PipelineGetParamsSearchFiltersInferenceSchemaMap map[string, any]`

    - `type PipelineGetParamsSearchFiltersInferenceSchemaArray []any`

    - `string`

    - `float64`

    - `bool`

  - `SparseSimilarityTopK param.Field[int64]`

    Body param: Number of nodes for sparse retrieval.

### Returns

- `type PipelineGetResponse struct{…}`

  Schema for the result of an retrieval execution.

  - `PipelineID string`

    The ID of the pipeline that the query was retrieved against.

  - `RetrievalNodes []PipelineGetResponseRetrievalNode`

    The nodes retrieved by the pipeline for the given query.

    - `Node TextNode`

      Provided for backward compatibility.

      - `ClassName string`

      - `Embedding []float64`

        Embedding of the node.

      - `EndCharIdx int64`

        End char index of the node.

      - `ExcludedEmbedMetadataKeys []string`

        Metadata keys that are excluded from text for the embed model.

      - `ExcludedLlmMetadataKeys []string`

        Metadata keys that are excluded from text for the LLM.

      - `ExtraInfo map[string, any]`

        A flat dictionary of metadata fields

      - `ID string`

        Unique ID of the node.

      - `MetadataSeperator string`

        Separator between metadata fields when converting to string.

      - `MetadataTemplate string`

        Template for how metadata is formatted, with {key} and {value} placeholders.

      - `Mimetype string`

        MIME type of the node content.

      - `Relationships map[string, TextNodeRelationshipUnion]`

        A mapping of relationships to other node information.

        - `type TextNodeRelationshipRelatedNodeInfo struct{…}`

          - `NodeID string`

          - `ClassName string`

          - `Hash string`

          - `Metadata map[string, any]`

          - `NodeType string`

            - `string`

              - `const TextNodeRelationshipRelatedNodeInfoNodeType1 TextNodeRelationshipRelatedNodeInfoNodeType = "1"`

              - `const TextNodeRelationshipRelatedNodeInfoNodeType2 TextNodeRelationshipRelatedNodeInfoNodeType = "2"`

              - `const TextNodeRelationshipRelatedNodeInfoNodeType3 TextNodeRelationshipRelatedNodeInfoNodeType = "3"`

              - `const TextNodeRelationshipRelatedNodeInfoNodeType4 TextNodeRelationshipRelatedNodeInfoNodeType = "4"`

              - `const TextNodeRelationshipRelatedNodeInfoNodeType5 TextNodeRelationshipRelatedNodeInfoNodeType = "5"`

            - `string`

        - `type TextNodeRelationshipArray []TextNodeRelationshipArrayItem`

          - `NodeID string`

          - `ClassName string`

          - `Hash string`

          - `Metadata map[string, any]`

          - `NodeType string`

            - `string`

              - `const TextNodeRelationshipArrayItemNodeType1 TextNodeRelationshipArrayItemNodeType = "1"`

              - `const TextNodeRelationshipArrayItemNodeType2 TextNodeRelationshipArrayItemNodeType = "2"`

              - `const TextNodeRelationshipArrayItemNodeType3 TextNodeRelationshipArrayItemNodeType = "3"`

              - `const TextNodeRelationshipArrayItemNodeType4 TextNodeRelationshipArrayItemNodeType = "4"`

              - `const TextNodeRelationshipArrayItemNodeType5 TextNodeRelationshipArrayItemNodeType = "5"`

            - `string`

      - `StartCharIdx int64`

        Start char index of the node.

      - `Text string`

        Text content of the node.

      - `TextTemplate string`

        Template for how text is formatted, with {content} and {metadata_str} placeholders.

    - `ClassName string`

    - `Score float64`

  - `ClassName string`

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

  - `InferredSearchFilters MetadataFilters`

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

  - `Metadata map[string, string]`

    Metadata associated with the retrieval execution

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

  - `RetrievalLatency map[string, float64]`

    The end-to-end latency for retrieval and reranking.

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
  pipeline, err := client.Pipelines.Get(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineGetParams{
      Query: "x",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", pipeline.PipelineID)
}
```

#### Response

```json
{
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "retrieval_nodes": [
    {
      "node": {
        "class_name": "class_name",
        "embedding": [
          0
        ],
        "end_char_idx": 0,
        "excluded_embed_metadata_keys": [
          "string"
        ],
        "excluded_llm_metadata_keys": [
          "string"
        ],
        "extra_info": {
          "foo": "bar"
        },
        "id_": "id_",
        "metadata_seperator": "metadata_seperator",
        "metadata_template": "metadata_template",
        "mimetype": "mimetype",
        "relationships": {
          "foo": {
            "node_id": "node_id",
            "class_name": "class_name",
            "hash": "hash",
            "metadata": {
              "foo": "bar"
            },
            "node_type": "1"
          }
        },
        "start_char_idx": 0,
        "text": "text",
        "text_template": "text_template"
      },
      "class_name": "class_name",
      "score": 0
    }
  ],
  "class_name": "class_name",
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
  "inferred_search_filters": {
    "filters": [
      {
        "key": "key",
        "value": 0,
        "operator": "=="
      }
    ],
    "condition": "and"
  },
  "metadata": {
    "foo": "string"
  },
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
  ],
  "retrieval_latency": {
    "foo": 0
  }
}
```
