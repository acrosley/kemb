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
