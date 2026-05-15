# Retrievers

## Create Retriever

`client.Retrievers.New(ctx, params) (*Retriever, error)`

**post** `/api/v1/retrievers`

Create a new Retriever.

### Parameters

- `params RetrieverNewParams`

  - `RetrieverCreate param.Field[RetrieverCreate]`

    Body param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

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
  retriever, err := client.Retrievers.New(context.TODO(), llamacloudprod.RetrieverNewParams{
    RetrieverCreate: llamacloudprod.RetrieverCreateParam{
      Name: "x",
    },
  })
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

## Upsert Retriever

`client.Retrievers.Upsert(ctx, params) (*Retriever, error)`

**put** `/api/v1/retrievers`

Upsert a new Retriever.

### Parameters

- `params RetrieverUpsertParams`

  - `RetrieverCreate param.Field[RetrieverCreate]`

    Body param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

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
  retriever, err := client.Retrievers.Upsert(context.TODO(), llamacloudprod.RetrieverUpsertParams{
    RetrieverCreate: llamacloudprod.RetrieverCreateParam{
      Name: "x",
    },
  })
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

## List Retrievers

`client.Retrievers.List(ctx, query) (*[]Retriever, error)`

**get** `/api/v1/retrievers`

List Retrievers for a project.

### Parameters

- `query RetrieverListParams`

  - `Name param.Field[string]`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type RetrieverListResponse []Retriever`

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
  retrievers, err := client.Retrievers.List(context.TODO(), llamacloudprod.RetrieverListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", retrievers)
}
```

#### Response

```json
[
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
]
```

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

## Update Retriever

`client.Retrievers.Update(ctx, retrieverID, params) (*Retriever, error)`

**put** `/api/v1/retrievers/{retriever_id}`

Update an existing Retriever.

### Parameters

- `retrieverID string`

- `params RetrieverUpdateParams`

  - `Pipelines param.Field[[]RetrieverPipeline]`

    Body param: The pipelines this retriever uses.

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

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Name param.Field[string]`

    Body param: A name for the retriever.

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
  retriever, err := client.Retrievers.Update(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.RetrieverUpdateParams{
      Pipelines: []llamacloudprod.RetrieverPipelineParam{llamacloudprod.RetrieverPipelineParam{
        Description: llamacloudprod.String("description"),
        Name: llamacloudprod.String("x"),
        PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      }},
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

## Delete Retriever

`client.Retrievers.Delete(ctx, retrieverID, body) error`

**delete** `/api/v1/retrievers/{retriever_id}`

Delete a Retriever by ID.

### Parameters

- `retrieverID string`

- `body RetrieverDeleteParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Example

```go
package main

import (
  "context"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Retrievers.Delete(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.RetrieverDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

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

## Domain Types

### Composite Retrieval Mode

- `type CompositeRetrievalMode string`

  Enum for the mode of composite retrieval.

  - `const CompositeRetrievalModeRouting CompositeRetrievalMode = "routing"`

  - `const CompositeRetrievalModeFull CompositeRetrievalMode = "full"`

### Composite Retrieval Result

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

### Re Rank Config

- `type ReRankConfig struct{…}`

  - `TopN int64`

    The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

  - `Type ReRankConfigType`

    The type of reranker to use.

    - `const ReRankConfigTypeSystemDefault ReRankConfigType = "system_default"`

    - `const ReRankConfigTypeLlm ReRankConfigType = "llm"`

    - `const ReRankConfigTypeCohere ReRankConfigType = "cohere"`

    - `const ReRankConfigTypeBedrock ReRankConfigType = "bedrock"`

    - `const ReRankConfigTypeScore ReRankConfigType = "score"`

    - `const ReRankConfigTypeDisabled ReRankConfigType = "disabled"`

### Retriever

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

### Retriever Create

- `type RetrieverCreate struct{…}`

  - `Name string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

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

### Retriever Pipeline

- `type RetrieverPipeline struct{…}`

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

# Retriever

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
