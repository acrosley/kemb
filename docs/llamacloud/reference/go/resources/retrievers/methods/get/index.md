## Get Retriever

`client.Retrievers.Get(ctx, retrieverID, query) (*Retriever, error)`

**get** `/api/v1/retrievers/{retriever_id}`

Get a Retriever by ID.

### Parameters

- `retrieverID string`

- `query RetrieverGetParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type Retriever struct{…}`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `ID string`

    Unique identifier

  - `Name string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `ProjectID string`

    The ID of the project this retriever resides in.

  - `CreatedAt Time`

    Creation datetime

  - `Pipelines []RetrieverPipeline`

    The pipelines this retriever uses.

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

  - `UpdatedAt Time`

    Update datetime

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
  retriever, err := client.Retrievers.Get(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.RetrieverGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", retriever.ID)
}
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "name": "x",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "created_at": "2019-12-27T18:11:19.117Z",
  "pipelines": [
    {
      "description": "description",
      "name": "x",
      "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "preset_retrieval_parameters": {
        "alpha": 0,
        "class_name": "class_name",
        "dense_similarity_cutoff": 0,
        "dense_similarity_top_k": 1,
        "enable_reranking": true,
        "files_top_k": 1,
        "rerank_top_n": 1,
        "retrieval_mode": "chunks",
        "retrieve_image_nodes": true,
        "retrieve_page_figure_nodes": true,
        "retrieve_page_screenshot_nodes": true,
        "search_filters": {
          "filters": [
            {
              "key": "key",
              "value": 0,
              "operator": "=="
            }
          ],
          "condition": "and"
        },
        "search_filters_inference_schema": {
          "foo": {
            "foo": "bar"
          }
        },
        "sparse_similarity_top_k": 1
      }
    }
  ],
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
