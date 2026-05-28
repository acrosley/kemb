# Retrievers

## Create Retriever

`client.retrievers.create(RetrieverCreateParamsparams, RequestOptionsoptions?): Retriever`

**post** `/api/v1/retrievers`

Create a new Retriever.

### Parameters

- `params: RetrieverCreateParams`

  - `name: string`

    Body param: A name for the retriever tool. Will default to the pipeline name if not provided.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `pipelines?: Array<RetrieverPipeline>`

    Body param: The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

### Returns

- `Retriever`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at?: string | null`

    Creation datetime

  - `pipelines?: Array<RetrieverPipeline>`

    The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const retriever = await client.retrievers.create({ name: 'x' });

console.log(retriever.id);
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

`client.retrievers.upsert(RetrieverUpsertParamsparams, RequestOptionsoptions?): Retriever`

**put** `/api/v1/retrievers`

Upsert a new Retriever.

### Parameters

- `params: RetrieverUpsertParams`

  - `name: string`

    Body param: A name for the retriever tool. Will default to the pipeline name if not provided.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `pipelines?: Array<RetrieverPipeline>`

    Body param: The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

### Returns

- `Retriever`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at?: string | null`

    Creation datetime

  - `pipelines?: Array<RetrieverPipeline>`

    The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const retriever = await client.retrievers.upsert({ name: 'x' });

console.log(retriever.id);
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

`client.retrievers.list(RetrieverListParamsquery?, RequestOptionsoptions?): RetrieverListResponse`

**get** `/api/v1/retrievers`

List Retrievers for a project.

### Parameters

- `query: RetrieverListParams`

  - `name?: string | null`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `RetrieverListResponse = Array<Retriever>`

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at?: string | null`

    Creation datetime

  - `pipelines?: Array<RetrieverPipeline>`

    The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const retrievers = await client.retrievers.list();

console.log(retrievers);
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

`client.retrievers.get(stringretrieverID, RetrieverGetParamsquery?, RequestOptionsoptions?): Retriever`

**get** `/api/v1/retrievers/{retriever_id}`

Get a Retriever by ID.

### Parameters

- `retrieverID: string`

- `query: RetrieverGetParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `Retriever`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at?: string | null`

    Creation datetime

  - `pipelines?: Array<RetrieverPipeline>`

    The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const retriever = await client.retrievers.get('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(retriever.id);
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

`client.retrievers.update(stringretrieverID, RetrieverUpdateParamsparams, RequestOptionsoptions?): Retriever`

**put** `/api/v1/retrievers/{retriever_id}`

Update an existing Retriever.

### Parameters

- `retrieverID: string`

- `params: RetrieverUpdateParams`

  - `pipelines: Array<RetrieverPipeline> | null`

    Body param: The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `name?: string | null`

    Body param: A name for the retriever.

### Returns

- `Retriever`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at?: string | null`

    Creation datetime

  - `pipelines?: Array<RetrieverPipeline>`

    The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const retriever = await client.retrievers.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  pipelines: [
    {
      description: 'description',
      name: 'x',
      pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
    },
  ],
});

console.log(retriever.id);
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

`client.retrievers.delete(stringretrieverID, RetrieverDeleteParamsparams?, RequestOptionsoptions?): void`

**delete** `/api/v1/retrievers/{retriever_id}`

Delete a Retriever by ID.

### Parameters

- `retrieverID: string`

- `params: RetrieverDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.retrievers.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```

## Direct Retrieve

`client.retrievers.search(RetrieverSearchParamsparams, RequestOptionsoptions?): CompositeRetrievalResult`

**post** `/api/v1/retrievers/retrieve`

Retrieve data using specified pipelines without creating a persistent retriever.

### Parameters

- `params: RetrieverSearchParams`

  - `query: string`

    Body param: The query to retrieve against.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `mode?: CompositeRetrievalMode`

    Body param: The mode of composite retrieval.

    - `"routing"`

    - `"full"`

  - `pipelines?: Array<RetrieverPipeline>`

    Body param: The pipelines to use for retrieval.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `rerank_config?: ReRankConfig`

    Body param: The rerank configuration for composite retrieval.

    - `top_n?: number`

      The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

    - `type?: "system_default" | "llm" | "cohere" | 3 more`

      The type of reranker to use.

      - `"system_default"`

      - `"llm"`

      - `"cohere"`

      - `"bedrock"`

      - `"score"`

      - `"disabled"`

  - `rerank_top_n?: number | null`

    Body param: (use rerank_config.top_n instead) The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

### Returns

- `CompositeRetrievalResult`

  - `image_nodes?: Array<PageScreenshotNodeWithScore>`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: Node`

      - `file_id: string`

        The ID of the file that the page screenshot was taken from

      - `image_size: number`

        The size of the image in bytes

      - `page_index: number`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata?: Record<string, unknown> | null`

        Metadata for the screenshot

    - `score: number`

      The score of the screenshot node

    - `class_name?: string`

  - `nodes?: Array<Node>`

    The retrieved nodes from the composite retrieval.

    - `node: Node`

      - `id: string`

        The ID of the retrieved node.

      - `end_char_idx: number | null`

        The end character index of the retrieved node in the document

      - `pipeline_id: string`

        The ID of the pipeline this node was retrieved from.

      - `retriever_id: string`

        The ID of the retriever this node was retrieved from.

      - `retriever_pipeline_name: string`

        The name of the retrieval pipeline this node was retrieved from.

      - `start_char_idx: number | null`

        The start character index of the retrieved node in the document

      - `text: string`

        The text of the retrieved node.

      - `metadata?: Record<string, unknown>`

        Metadata associated with the retrieved node.

    - `class_name?: string`

    - `score?: number | null`

  - `page_figure_nodes?: Array<PageFigureNodeWithScore>`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: Node`

      - `confidence: number`

        The confidence of the figure

      - `figure_name: string`

        The name of the figure

      - `figure_size: number`

        The size of the figure in bytes

      - `file_id: string`

        The ID of the file that the figure was taken from

      - `page_index: number`

        The index of the page for which the figure is taken (0-indexed)

      - `is_likely_noise?: boolean`

        Whether the figure is likely to be noise

      - `metadata?: Record<string, unknown> | null`

        Metadata for the figure

    - `score: number`

      The score of the figure node

    - `class_name?: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const compositeRetrievalResult = await client.retrievers.search({ query: 'x' });

console.log(compositeRetrievalResult.image_nodes);
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

- `CompositeRetrievalMode = "routing" | "full"`

  Enum for the mode of composite retrieval.

  - `"routing"`

  - `"full"`

### Composite Retrieval Result

- `CompositeRetrievalResult`

  - `image_nodes?: Array<PageScreenshotNodeWithScore>`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: Node`

      - `file_id: string`

        The ID of the file that the page screenshot was taken from

      - `image_size: number`

        The size of the image in bytes

      - `page_index: number`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata?: Record<string, unknown> | null`

        Metadata for the screenshot

    - `score: number`

      The score of the screenshot node

    - `class_name?: string`

  - `nodes?: Array<Node>`

    The retrieved nodes from the composite retrieval.

    - `node: Node`

      - `id: string`

        The ID of the retrieved node.

      - `end_char_idx: number | null`

        The end character index of the retrieved node in the document

      - `pipeline_id: string`

        The ID of the pipeline this node was retrieved from.

      - `retriever_id: string`

        The ID of the retriever this node was retrieved from.

      - `retriever_pipeline_name: string`

        The name of the retrieval pipeline this node was retrieved from.

      - `start_char_idx: number | null`

        The start character index of the retrieved node in the document

      - `text: string`

        The text of the retrieved node.

      - `metadata?: Record<string, unknown>`

        Metadata associated with the retrieved node.

    - `class_name?: string`

    - `score?: number | null`

  - `page_figure_nodes?: Array<PageFigureNodeWithScore>`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: Node`

      - `confidence: number`

        The confidence of the figure

      - `figure_name: string`

        The name of the figure

      - `figure_size: number`

        The size of the figure in bytes

      - `file_id: string`

        The ID of the file that the figure was taken from

      - `page_index: number`

        The index of the page for which the figure is taken (0-indexed)

      - `is_likely_noise?: boolean`

        Whether the figure is likely to be noise

      - `metadata?: Record<string, unknown> | null`

        Metadata for the figure

    - `score: number`

      The score of the figure node

    - `class_name?: string`

### Re Rank Config

- `ReRankConfig`

  - `top_n?: number`

    The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

  - `type?: "system_default" | "llm" | "cohere" | 3 more`

    The type of reranker to use.

    - `"system_default"`

    - `"llm"`

    - `"cohere"`

    - `"bedrock"`

    - `"score"`

    - `"disabled"`

### Retriever

- `Retriever`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at?: string | null`

    Creation datetime

  - `pipelines?: Array<RetrieverPipeline>`

    The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `updated_at?: string | null`

    Update datetime

### Retriever Create

- `RetrieverCreate`

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `pipelines?: Array<RetrieverPipeline>`

    The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

### Retriever Pipeline

- `RetrieverPipeline`

  - `description: string | null`

    A description of the retriever tool.

  - `name: string | null`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `pipeline_id: string`

    The ID of the pipeline this tool uses.

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Parameters for retrieval configuration.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

### Retriever List Response

- `RetrieverListResponse = Array<Retriever>`

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at?: string | null`

    Creation datetime

  - `pipelines?: Array<RetrieverPipeline>`

    The pipelines this retriever uses.

    - `description: string | null`

      A description of the retriever tool.

    - `name: string | null`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters?: PresetRetrievalParams`

      Parameters for retrieval configuration.

      - `alpha?: number | null`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name?: string`

      - `dense_similarity_cutoff?: number | null`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k?: number | null`

        Number of nodes for dense retrieval.

      - `enable_reranking?: boolean | null`

        Enable reranking for retrieval

      - `files_top_k?: number | null`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n?: number | null`

        Number of reranked nodes for returning.

      - `retrieval_mode?: RetrievalMode`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes?: boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes?: boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes?: boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters?: MetadataFilters | null`

        Metadata filters for vector stores.

        - `filters: Array<MetadataFilter | MetadataFilters>`

          - `MetadataFilter`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number | string | Array<string> | 2 more | null`

              - `number`

              - `string`

              - `Array<string>`

              - `Array<number>`

              - `Array<number>`

            - `operator?: "==" | ">" | "<" | 11 more`

              Vector store filter operator.

              - `"=="`

              - `">"`

              - `"<"`

              - `"!="`

              - `">="`

              - `"<="`

              - `"in"`

              - `"nin"`

              - `"any"`

              - `"all"`

              - `"text_match"`

              - `"text_match_insensitive"`

              - `"contains"`

              - `"is_empty"`

          - `MetadataFilters`

            Metadata filters for vector stores.

        - `condition?: "and" | "or" | "not" | null`

          Vector store filter conditions to combine different filters.

          - `"and"`

          - `"or"`

          - `"not"`

      - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `sparse_similarity_top_k?: number | null`

        Number of nodes for sparse retrieval.

  - `updated_at?: string | null`

    Update datetime

# Retriever

## Retrieve

`client.retrievers.retriever.search(stringretrieverID, RetrieverSearchParamsparams, RequestOptionsoptions?): CompositeRetrievalResult`

**post** `/api/v1/retrievers/{retriever_id}/retrieve`

Retrieve data using a Retriever.

### Parameters

- `retrieverID: string`

- `params: RetrieverSearchParams`

  - `query: string`

    Body param: The query to retrieve against.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `mode?: CompositeRetrievalMode`

    Body param: The mode of composite retrieval.

    - `"routing"`

    - `"full"`

  - `rerank_config?: ReRankConfig`

    Body param: The rerank configuration for composite retrieval.

    - `top_n?: number`

      The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

    - `type?: "system_default" | "llm" | "cohere" | 3 more`

      The type of reranker to use.

      - `"system_default"`

      - `"llm"`

      - `"cohere"`

      - `"bedrock"`

      - `"score"`

      - `"disabled"`

  - `rerank_top_n?: number | null`

    Body param: (use rerank_config.top_n instead) The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

### Returns

- `CompositeRetrievalResult`

  - `image_nodes?: Array<PageScreenshotNodeWithScore>`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: Node`

      - `file_id: string`

        The ID of the file that the page screenshot was taken from

      - `image_size: number`

        The size of the image in bytes

      - `page_index: number`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata?: Record<string, unknown> | null`

        Metadata for the screenshot

    - `score: number`

      The score of the screenshot node

    - `class_name?: string`

  - `nodes?: Array<Node>`

    The retrieved nodes from the composite retrieval.

    - `node: Node`

      - `id: string`

        The ID of the retrieved node.

      - `end_char_idx: number | null`

        The end character index of the retrieved node in the document

      - `pipeline_id: string`

        The ID of the pipeline this node was retrieved from.

      - `retriever_id: string`

        The ID of the retriever this node was retrieved from.

      - `retriever_pipeline_name: string`

        The name of the retrieval pipeline this node was retrieved from.

      - `start_char_idx: number | null`

        The start character index of the retrieved node in the document

      - `text: string`

        The text of the retrieved node.

      - `metadata?: Record<string, unknown>`

        Metadata associated with the retrieved node.

    - `class_name?: string`

    - `score?: number | null`

  - `page_figure_nodes?: Array<PageFigureNodeWithScore>`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: Node`

      - `confidence: number`

        The confidence of the figure

      - `figure_name: string`

        The name of the figure

      - `figure_size: number`

        The size of the figure in bytes

      - `file_id: string`

        The ID of the file that the figure was taken from

      - `page_index: number`

        The index of the page for which the figure is taken (0-indexed)

      - `is_likely_noise?: boolean`

        Whether the figure is likely to be noise

      - `metadata?: Record<string, unknown> | null`

        Metadata for the figure

    - `score: number`

      The score of the figure node

    - `class_name?: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const compositeRetrievalResult = await client.retrievers.retriever.search(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { query: 'x' },
);

console.log(compositeRetrievalResult.image_nodes);
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
