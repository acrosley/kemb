# Retrievers

## Create Retriever

`$ llamacloud-prod retrievers create`

**post** `/api/v1/retrievers`

Create a new Retriever.

### Parameters

- `--name: string`

  Body param: A name for the retriever tool. Will default to the pipeline name if not provided.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--pipeline: optional array of RetrieverPipeline`

  Body param: The pipelines this retriever uses.

### Returns

- `retriever: object { id, name, project_id, 3 more }`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at: optional string`

    Creation datetime

  - `pipelines: optional array of RetrieverPipeline`

    The pipelines this retriever uses.

    - `description: string`

      A description of the retriever tool.

    - `name: string`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

      Parameters for retrieval configuration.

      - `alpha: optional number`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name: optional string`

      - `dense_similarity_cutoff: optional number`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k: optional number`

        Number of nodes for dense retrieval.

      - `enable_reranking: optional boolean`

        Enable reranking for retrieval

      - `files_top_k: optional number`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n: optional number`

        Number of reranked nodes for returning.

      - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes: optional boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes: optional boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes: optional boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters: optional object { filters, condition }`

        Metadata filters for vector stores.

        - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `MetadataFilter: object { key, value, operator }`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number or string or array of string or 2 more`

              - `union_member_0: number`

              - `union_member_1: string`

              - `union_member_2: array of string`

              - `union_member_3: array of number`

              - `union_member_4: array of number`

            - `operator: optional "==" or ">" or "<" or 11 more`

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

          - `metadata_filters: object { filters, condition }`

            Metadata filters for vector stores.

            - `filters: array of object { key, value, operator }  or MetadataFilters`

            - `condition: optional "and" or "or" or "not"`

              Vector store filter conditions to combine different filters.

              - `"and"`

              - `"or"`

              - `"not"`

        - `condition: optional "and" or "or" or "not"`

          Vector store filter conditions to combine different filters.

      - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `sparse_similarity_top_k: optional number`

        Number of nodes for sparse retrieval.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod retrievers create \
  --api-key 'My API Key' \
  --name x
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

`$ llamacloud-prod retrievers upsert`

**put** `/api/v1/retrievers`

Upsert a new Retriever.

### Parameters

- `--name: string`

  Body param: A name for the retriever tool. Will default to the pipeline name if not provided.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--pipeline: optional array of RetrieverPipeline`

  Body param: The pipelines this retriever uses.

### Returns

- `retriever: object { id, name, project_id, 3 more }`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at: optional string`

    Creation datetime

  - `pipelines: optional array of RetrieverPipeline`

    The pipelines this retriever uses.

    - `description: string`

      A description of the retriever tool.

    - `name: string`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

      Parameters for retrieval configuration.

      - `alpha: optional number`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name: optional string`

      - `dense_similarity_cutoff: optional number`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k: optional number`

        Number of nodes for dense retrieval.

      - `enable_reranking: optional boolean`

        Enable reranking for retrieval

      - `files_top_k: optional number`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n: optional number`

        Number of reranked nodes for returning.

      - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes: optional boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes: optional boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes: optional boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters: optional object { filters, condition }`

        Metadata filters for vector stores.

        - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `MetadataFilter: object { key, value, operator }`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number or string or array of string or 2 more`

              - `union_member_0: number`

              - `union_member_1: string`

              - `union_member_2: array of string`

              - `union_member_3: array of number`

              - `union_member_4: array of number`

            - `operator: optional "==" or ">" or "<" or 11 more`

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

          - `metadata_filters: object { filters, condition }`

            Metadata filters for vector stores.

            - `filters: array of object { key, value, operator }  or MetadataFilters`

            - `condition: optional "and" or "or" or "not"`

              Vector store filter conditions to combine different filters.

              - `"and"`

              - `"or"`

              - `"not"`

        - `condition: optional "and" or "or" or "not"`

          Vector store filter conditions to combine different filters.

      - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `sparse_similarity_top_k: optional number`

        Number of nodes for sparse retrieval.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod retrievers upsert \
  --api-key 'My API Key' \
  --name x
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

`$ llamacloud-prod retrievers list`

**get** `/api/v1/retrievers`

List Retrievers for a project.

### Parameters

- `--name: optional string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `Response List Retrievers Api V1 Retrievers Get: array of Retriever`

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at: optional string`

    Creation datetime

  - `pipelines: optional array of RetrieverPipeline`

    The pipelines this retriever uses.

    - `description: string`

      A description of the retriever tool.

    - `name: string`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

      Parameters for retrieval configuration.

      - `alpha: optional number`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name: optional string`

      - `dense_similarity_cutoff: optional number`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k: optional number`

        Number of nodes for dense retrieval.

      - `enable_reranking: optional boolean`

        Enable reranking for retrieval

      - `files_top_k: optional number`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n: optional number`

        Number of reranked nodes for returning.

      - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes: optional boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes: optional boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes: optional boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters: optional object { filters, condition }`

        Metadata filters for vector stores.

        - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `MetadataFilter: object { key, value, operator }`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number or string or array of string or 2 more`

              - `union_member_0: number`

              - `union_member_1: string`

              - `union_member_2: array of string`

              - `union_member_3: array of number`

              - `union_member_4: array of number`

            - `operator: optional "==" or ">" or "<" or 11 more`

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

          - `metadata_filters: object { filters, condition }`

            Metadata filters for vector stores.

            - `filters: array of object { key, value, operator }  or MetadataFilters`

            - `condition: optional "and" or "or" or "not"`

              Vector store filter conditions to combine different filters.

              - `"and"`

              - `"or"`

              - `"not"`

        - `condition: optional "and" or "or" or "not"`

          Vector store filter conditions to combine different filters.

      - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `sparse_similarity_top_k: optional number`

        Number of nodes for sparse retrieval.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod retrievers list \
  --api-key 'My API Key'
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

`$ llamacloud-prod retrievers get`

**get** `/api/v1/retrievers/{retriever_id}`

Get a Retriever by ID.

### Parameters

- `--retriever-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `retriever: object { id, name, project_id, 3 more }`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at: optional string`

    Creation datetime

  - `pipelines: optional array of RetrieverPipeline`

    The pipelines this retriever uses.

    - `description: string`

      A description of the retriever tool.

    - `name: string`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

      Parameters for retrieval configuration.

      - `alpha: optional number`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name: optional string`

      - `dense_similarity_cutoff: optional number`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k: optional number`

        Number of nodes for dense retrieval.

      - `enable_reranking: optional boolean`

        Enable reranking for retrieval

      - `files_top_k: optional number`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n: optional number`

        Number of reranked nodes for returning.

      - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes: optional boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes: optional boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes: optional boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters: optional object { filters, condition }`

        Metadata filters for vector stores.

        - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `MetadataFilter: object { key, value, operator }`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number or string or array of string or 2 more`

              - `union_member_0: number`

              - `union_member_1: string`

              - `union_member_2: array of string`

              - `union_member_3: array of number`

              - `union_member_4: array of number`

            - `operator: optional "==" or ">" or "<" or 11 more`

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

          - `metadata_filters: object { filters, condition }`

            Metadata filters for vector stores.

            - `filters: array of object { key, value, operator }  or MetadataFilters`

            - `condition: optional "and" or "or" or "not"`

              Vector store filter conditions to combine different filters.

              - `"and"`

              - `"or"`

              - `"not"`

        - `condition: optional "and" or "or" or "not"`

          Vector store filter conditions to combine different filters.

      - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `sparse_similarity_top_k: optional number`

        Number of nodes for sparse retrieval.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod retrievers get \
  --api-key 'My API Key' \
  --retriever-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

`$ llamacloud-prod retrievers update`

**put** `/api/v1/retrievers/{retriever_id}`

Update an existing Retriever.

### Parameters

- `--retriever-id: string`

  Path param

- `--pipeline: array of RetrieverPipeline`

  Body param: The pipelines this retriever uses.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--name: optional string`

  Body param: A name for the retriever.

### Returns

- `retriever: object { id, name, project_id, 3 more }`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at: optional string`

    Creation datetime

  - `pipelines: optional array of RetrieverPipeline`

    The pipelines this retriever uses.

    - `description: string`

      A description of the retriever tool.

    - `name: string`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

      Parameters for retrieval configuration.

      - `alpha: optional number`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name: optional string`

      - `dense_similarity_cutoff: optional number`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k: optional number`

        Number of nodes for dense retrieval.

      - `enable_reranking: optional boolean`

        Enable reranking for retrieval

      - `files_top_k: optional number`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n: optional number`

        Number of reranked nodes for returning.

      - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes: optional boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes: optional boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes: optional boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters: optional object { filters, condition }`

        Metadata filters for vector stores.

        - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `MetadataFilter: object { key, value, operator }`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number or string or array of string or 2 more`

              - `union_member_0: number`

              - `union_member_1: string`

              - `union_member_2: array of string`

              - `union_member_3: array of number`

              - `union_member_4: array of number`

            - `operator: optional "==" or ">" or "<" or 11 more`

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

          - `metadata_filters: object { filters, condition }`

            Metadata filters for vector stores.

            - `filters: array of object { key, value, operator }  or MetadataFilters`

            - `condition: optional "and" or "or" or "not"`

              Vector store filter conditions to combine different filters.

              - `"and"`

              - `"or"`

              - `"not"`

        - `condition: optional "and" or "or" or "not"`

          Vector store filter conditions to combine different filters.

      - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `sparse_similarity_top_k: optional number`

        Number of nodes for sparse retrieval.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod retrievers update \
  --api-key 'My API Key' \
  --retriever-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --pipeline '{description: description, name: x, pipeline_id: 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e}'
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

`$ llamacloud-prod retrievers delete`

**delete** `/api/v1/retrievers/{retriever_id}`

Delete a Retriever by ID.

### Parameters

- `--retriever-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Example

```cli
llamacloud-prod retrievers delete \
  --api-key 'My API Key' \
  --retriever-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```

## Direct Retrieve

`$ llamacloud-prod retrievers search`

**post** `/api/v1/retrievers/retrieve`

Retrieve data using specified pipelines without creating a persistent retriever.

### Parameters

- `--query: string`

  Body param: The query to retrieve against.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--mode: optional "routing" or "full"`

  Body param: The mode of composite retrieval.

- `--pipeline: optional array of RetrieverPipeline`

  Body param: The pipelines to use for retrieval.

- `--rerank-config: optional object { top_n, type }`

  Body param: The rerank configuration for composite retrieval.

- `--rerank-top-n: optional number`

  Body param: (use rerank_config.top_n instead) The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

### Returns

- `composite_retrieval_result: object { image_nodes, nodes, page_figure_nodes }`

  - `image_nodes: optional array of PageScreenshotNodeWithScore`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: object { file_id, image_size, page_index, metadata }`

      - `file_id: string`

        The ID of the file that the page screenshot was taken from

      - `image_size: number`

        The size of the image in bytes

      - `page_index: number`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata: optional map[unknown]`

        Metadata for the screenshot

    - `score: number`

      The score of the screenshot node

    - `class_name: optional string`

  - `nodes: optional array of object { node, class_name, score }`

    The retrieved nodes from the composite retrieval.

    - `node: object { id, end_char_idx, pipeline_id, 5 more }`

      - `id: string`

        The ID of the retrieved node.

      - `end_char_idx: number`

        The end character index of the retrieved node in the document

      - `pipeline_id: string`

        The ID of the pipeline this node was retrieved from.

      - `retriever_id: string`

        The ID of the retriever this node was retrieved from.

      - `retriever_pipeline_name: string`

        The name of the retrieval pipeline this node was retrieved from.

      - `start_char_idx: number`

        The start character index of the retrieved node in the document

      - `text: string`

        The text of the retrieved node.

      - `metadata: optional map[unknown]`

        Metadata associated with the retrieved node.

    - `class_name: optional string`

    - `score: optional number`

  - `page_figure_nodes: optional array of PageFigureNodeWithScore`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: object { confidence, figure_name, figure_size, 4 more }`

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

      - `is_likely_noise: optional boolean`

        Whether the figure is likely to be noise

      - `metadata: optional map[unknown]`

        Metadata for the figure

    - `score: number`

      The score of the figure node

    - `class_name: optional string`

### Example

```cli
llamacloud-prod retrievers search \
  --api-key 'My API Key' \
  --query x
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

- `composite_retrieval_mode: "routing" or "full"`

  Enum for the mode of composite retrieval.

  - `"routing"`

  - `"full"`

### Composite Retrieval Result

- `composite_retrieval_result: object { image_nodes, nodes, page_figure_nodes }`

  - `image_nodes: optional array of PageScreenshotNodeWithScore`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: object { file_id, image_size, page_index, metadata }`

      - `file_id: string`

        The ID of the file that the page screenshot was taken from

      - `image_size: number`

        The size of the image in bytes

      - `page_index: number`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata: optional map[unknown]`

        Metadata for the screenshot

    - `score: number`

      The score of the screenshot node

    - `class_name: optional string`

  - `nodes: optional array of object { node, class_name, score }`

    The retrieved nodes from the composite retrieval.

    - `node: object { id, end_char_idx, pipeline_id, 5 more }`

      - `id: string`

        The ID of the retrieved node.

      - `end_char_idx: number`

        The end character index of the retrieved node in the document

      - `pipeline_id: string`

        The ID of the pipeline this node was retrieved from.

      - `retriever_id: string`

        The ID of the retriever this node was retrieved from.

      - `retriever_pipeline_name: string`

        The name of the retrieval pipeline this node was retrieved from.

      - `start_char_idx: number`

        The start character index of the retrieved node in the document

      - `text: string`

        The text of the retrieved node.

      - `metadata: optional map[unknown]`

        Metadata associated with the retrieved node.

    - `class_name: optional string`

    - `score: optional number`

  - `page_figure_nodes: optional array of PageFigureNodeWithScore`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: object { confidence, figure_name, figure_size, 4 more }`

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

      - `is_likely_noise: optional boolean`

        Whether the figure is likely to be noise

      - `metadata: optional map[unknown]`

        Metadata for the figure

    - `score: number`

      The score of the figure node

    - `class_name: optional string`

### Re Rank Config

- `re_rank_config: object { top_n, type }`

  - `top_n: optional number`

    The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

  - `type: optional "system_default" or "llm" or "cohere" or 3 more`

    The type of reranker to use.

    - `"system_default"`

    - `"llm"`

    - `"cohere"`

    - `"bedrock"`

    - `"score"`

    - `"disabled"`

### Retriever

- `retriever: object { id, name, project_id, 3 more }`

  An entity that retrieves context nodes from several sub RetrieverTools.

  - `id: string`

    Unique identifier

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `project_id: string`

    The ID of the project this retriever resides in.

  - `created_at: optional string`

    Creation datetime

  - `pipelines: optional array of RetrieverPipeline`

    The pipelines this retriever uses.

    - `description: string`

      A description of the retriever tool.

    - `name: string`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

      Parameters for retrieval configuration.

      - `alpha: optional number`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name: optional string`

      - `dense_similarity_cutoff: optional number`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k: optional number`

        Number of nodes for dense retrieval.

      - `enable_reranking: optional boolean`

        Enable reranking for retrieval

      - `files_top_k: optional number`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n: optional number`

        Number of reranked nodes for returning.

      - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes: optional boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes: optional boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes: optional boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters: optional object { filters, condition }`

        Metadata filters for vector stores.

        - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `MetadataFilter: object { key, value, operator }`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number or string or array of string or 2 more`

              - `union_member_0: number`

              - `union_member_1: string`

              - `union_member_2: array of string`

              - `union_member_3: array of number`

              - `union_member_4: array of number`

            - `operator: optional "==" or ">" or "<" or 11 more`

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

          - `metadata_filters: object { filters, condition }`

            Metadata filters for vector stores.

            - `filters: array of object { key, value, operator }  or MetadataFilters`

            - `condition: optional "and" or "or" or "not"`

              Vector store filter conditions to combine different filters.

              - `"and"`

              - `"or"`

              - `"not"`

        - `condition: optional "and" or "or" or "not"`

          Vector store filter conditions to combine different filters.

      - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `sparse_similarity_top_k: optional number`

        Number of nodes for sparse retrieval.

  - `updated_at: optional string`

    Update datetime

### Retriever Create

- `retriever_create: object { name, pipelines }`

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `pipelines: optional array of RetrieverPipeline`

    The pipelines this retriever uses.

    - `description: string`

      A description of the retriever tool.

    - `name: string`

      A name for the retriever tool. Will default to the pipeline name if not provided.

    - `pipeline_id: string`

      The ID of the pipeline this tool uses.

    - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

      Parameters for retrieval configuration.

      - `alpha: optional number`

        Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

      - `class_name: optional string`

      - `dense_similarity_cutoff: optional number`

        Minimum similarity score wrt query for retrieval

      - `dense_similarity_top_k: optional number`

        Number of nodes for dense retrieval.

      - `enable_reranking: optional boolean`

        Enable reranking for retrieval

      - `files_top_k: optional number`

        Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

      - `rerank_top_n: optional number`

        Number of reranked nodes for returning.

      - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

        The retrieval mode for the query.

        - `"chunks"`

        - `"files_via_metadata"`

        - `"files_via_content"`

        - `"auto_routed"`

      - `retrieve_image_nodes: optional boolean`

        Whether to retrieve image nodes.

      - `retrieve_page_figure_nodes: optional boolean`

        Whether to retrieve page figure nodes.

      - `retrieve_page_screenshot_nodes: optional boolean`

        Whether to retrieve page screenshot nodes.

      - `search_filters: optional object { filters, condition }`

        Metadata filters for vector stores.

        - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `MetadataFilter: object { key, value, operator }`

            Comprehensive metadata filter for vector stores to support more operators.

            Value uses Strict types, as int, float and str are compatible types and were all
            converted to string before.

            See: https://docs.pydantic.dev/latest/usage/types/#strict-types

            - `key: string`

            - `value: number or string or array of string or 2 more`

              - `union_member_0: number`

              - `union_member_1: string`

              - `union_member_2: array of string`

              - `union_member_3: array of number`

              - `union_member_4: array of number`

            - `operator: optional "==" or ">" or "<" or 11 more`

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

          - `metadata_filters: object { filters, condition }`

            Metadata filters for vector stores.

            - `filters: array of object { key, value, operator }  or MetadataFilters`

            - `condition: optional "and" or "or" or "not"`

              Vector store filter conditions to combine different filters.

              - `"and"`

              - `"or"`

              - `"not"`

        - `condition: optional "and" or "or" or "not"`

          Vector store filter conditions to combine different filters.

      - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `sparse_similarity_top_k: optional number`

        Number of nodes for sparse retrieval.

### Retriever Pipeline

- `retriever_pipeline: object { description, name, pipeline_id, preset_retrieval_parameters }`

  - `description: string`

    A description of the retriever tool.

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `pipeline_id: string`

    The ID of the pipeline this tool uses.

  - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

    Parameters for retrieval configuration.

    - `alpha: optional number`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name: optional string`

    - `dense_similarity_cutoff: optional number`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k: optional number`

      Number of nodes for dense retrieval.

    - `enable_reranking: optional boolean`

      Enable reranking for retrieval

    - `files_top_k: optional number`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n: optional number`

      Number of reranked nodes for returning.

    - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes: optional boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes: optional boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes: optional boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters: optional object { filters, condition }`

      Metadata filters for vector stores.

      - `filters: array of object { key, value, operator }  or MetadataFilters`

        - `MetadataFilter: object { key, value, operator }`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number or string or array of string or 2 more`

            - `union_member_0: number`

            - `union_member_1: string`

            - `union_member_2: array of string`

            - `union_member_3: array of number`

            - `union_member_4: array of number`

          - `operator: optional "==" or ">" or "<" or 11 more`

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

        - `metadata_filters: object { filters, condition }`

          Metadata filters for vector stores.

          - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `condition: optional "and" or "or" or "not"`

            Vector store filter conditions to combine different filters.

            - `"and"`

            - `"or"`

            - `"not"`

      - `condition: optional "and" or "or" or "not"`

        Vector store filter conditions to combine different filters.

    - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `sparse_similarity_top_k: optional number`

      Number of nodes for sparse retrieval.

# Retriever

## Retrieve

`$ llamacloud-prod retrievers:retriever search`

**post** `/api/v1/retrievers/{retriever_id}/retrieve`

Retrieve data using a Retriever.

### Parameters

- `--retriever-id: string`

  Path param

- `--query: string`

  Body param: The query to retrieve against.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--mode: optional "routing" or "full"`

  Body param: The mode of composite retrieval.

- `--rerank-config: optional object { top_n, type }`

  Body param: The rerank configuration for composite retrieval.

- `--rerank-top-n: optional number`

  Body param: (use rerank_config.top_n instead) The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

### Returns

- `composite_retrieval_result: object { image_nodes, nodes, page_figure_nodes }`

  - `image_nodes: optional array of PageScreenshotNodeWithScore`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: object { file_id, image_size, page_index, metadata }`

      - `file_id: string`

        The ID of the file that the page screenshot was taken from

      - `image_size: number`

        The size of the image in bytes

      - `page_index: number`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata: optional map[unknown]`

        Metadata for the screenshot

    - `score: number`

      The score of the screenshot node

    - `class_name: optional string`

  - `nodes: optional array of object { node, class_name, score }`

    The retrieved nodes from the composite retrieval.

    - `node: object { id, end_char_idx, pipeline_id, 5 more }`

      - `id: string`

        The ID of the retrieved node.

      - `end_char_idx: number`

        The end character index of the retrieved node in the document

      - `pipeline_id: string`

        The ID of the pipeline this node was retrieved from.

      - `retriever_id: string`

        The ID of the retriever this node was retrieved from.

      - `retriever_pipeline_name: string`

        The name of the retrieval pipeline this node was retrieved from.

      - `start_char_idx: number`

        The start character index of the retrieved node in the document

      - `text: string`

        The text of the retrieved node.

      - `metadata: optional map[unknown]`

        Metadata associated with the retrieved node.

    - `class_name: optional string`

    - `score: optional number`

  - `page_figure_nodes: optional array of PageFigureNodeWithScore`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: object { confidence, figure_name, figure_size, 4 more }`

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

      - `is_likely_noise: optional boolean`

        Whether the figure is likely to be noise

      - `metadata: optional map[unknown]`

        Metadata for the figure

    - `score: number`

      The score of the figure node

    - `class_name: optional string`

### Example

```cli
llamacloud-prod retrievers:retriever search \
  --api-key 'My API Key' \
  --retriever-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --query x
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
