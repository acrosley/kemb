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
