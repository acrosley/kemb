## Run Search

`client.pipelines.retrieve(stringpipelineID, PipelineRetrieveParamsparams, RequestOptionsoptions?): PipelineRetrieveResponse`

**post** `/api/v1/pipelines/{pipeline_id}/retrieve`

Run a retrieval query against a managed pipeline.

Searches the pipeline's vector store using the provided query
and retrieval parameters. Supports dense, sparse, and hybrid
search modes with configurable top-k and reranking.

### Parameters

- `pipelineID: string`

- `params: PipelineRetrieveParams`

  - `query: string`

    Body param: The query to retrieve against.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `alpha?: number | null`

    Body param: Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

  - `class_name?: string`

    Body param

  - `dense_similarity_cutoff?: number | null`

    Body param: Minimum similarity score wrt query for retrieval

  - `dense_similarity_top_k?: number | null`

    Body param: Number of nodes for dense retrieval.

  - `enable_reranking?: boolean | null`

    Body param: Enable reranking for retrieval

  - `files_top_k?: number | null`

    Body param: Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

  - `rerank_top_n?: number | null`

    Body param: Number of reranked nodes for returning.

  - `retrieval_mode?: RetrievalMode`

    Body param: The retrieval mode for the query.

    - `"chunks"`

    - `"files_via_metadata"`

    - `"files_via_content"`

    - `"auto_routed"`

  - `retrieve_image_nodes?: boolean`

    Body param: Whether to retrieve image nodes.

  - `retrieve_page_figure_nodes?: boolean`

    Body param: Whether to retrieve page figure nodes.

  - `retrieve_page_screenshot_nodes?: boolean`

    Body param: Whether to retrieve page screenshot nodes.

  - `search_filters?: MetadataFilters | null`

    Body param: Metadata filters for vector stores.

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

    Body param: JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `sparse_similarity_top_k?: number | null`

    Body param: Number of nodes for sparse retrieval.

### Returns

- `PipelineRetrieveResponse`

  Schema for the result of an retrieval execution.

  - `pipeline_id: string`

    The ID of the pipeline that the query was retrieved against.

  - `retrieval_nodes: Array<RetrievalNode>`

    The nodes retrieved by the pipeline for the given query.

    - `node: TextNode`

      Provided for backward compatibility.

      - `class_name?: string`

      - `embedding?: Array<number> | null`

        Embedding of the node.

      - `end_char_idx?: number | null`

        End char index of the node.

      - `excluded_embed_metadata_keys?: Array<string>`

        Metadata keys that are excluded from text for the embed model.

      - `excluded_llm_metadata_keys?: Array<string>`

        Metadata keys that are excluded from text for the LLM.

      - `extra_info?: Record<string, unknown>`

        A flat dictionary of metadata fields

      - `id_?: string`

        Unique ID of the node.

      - `metadata_seperator?: string`

        Separator between metadata fields when converting to string.

      - `metadata_template?: string`

        Template for how metadata is formatted, with {key} and {value} placeholders.

      - `mimetype?: string`

        MIME type of the node content.

      - `relationships?: Record<string, RelatedNodeInfo | Array<UnionMember1>>`

        A mapping of relationships to other node information.

        - `RelatedNodeInfo`

          - `node_id: string`

          - `class_name?: string`

          - `hash?: string | null`

          - `metadata?: Record<string, unknown>`

          - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

            - `"1" | "2" | "3" | 2 more`

              - `"1"`

              - `"2"`

              - `"3"`

              - `"4"`

              - `"5"`

            - `(string & {})`

        - `Array<UnionMember1>`

          - `node_id: string`

          - `class_name?: string`

          - `hash?: string | null`

          - `metadata?: Record<string, unknown>`

          - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

            - `"1" | "2" | "3" | 2 more`

              - `"1"`

              - `"2"`

              - `"3"`

              - `"4"`

              - `"5"`

            - `(string & {})`

      - `start_char_idx?: number | null`

        Start char index of the node.

      - `text?: string`

        Text content of the node.

      - `text_template?: string`

        Template for how text is formatted, with {content} and {metadata_str} placeholders.

    - `class_name?: string`

    - `score?: number | null`

  - `class_name?: string`

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

  - `inferred_search_filters?: MetadataFilters | null`

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

  - `metadata?: Record<string, string>`

    Metadata associated with the retrieval execution

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

  - `retrieval_latency?: Record<string, number>`

    The end-to-end latency for retrieval and reranking.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  query: 'x',
});

console.log(pipeline.pipeline_id);
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
