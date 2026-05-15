## Direct Retrieve

**post** `/api/v1/retrievers/retrieve`

Retrieve data using specified pipelines without creating a persistent retriever.

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `query: string`

  The query to retrieve against.

- `mode: optional CompositeRetrievalMode`

  The mode of composite retrieval.

  - `"routing"`

  - `"full"`

- `pipelines: optional array of RetrieverPipeline`

  The pipelines to use for retrieval.

  - `description: string`

    A description of the retriever tool.

  - `name: string`

    A name for the retriever tool. Will default to the pipeline name if not provided.

  - `pipeline_id: string`

    The ID of the pipeline this tool uses.

  - `preset_retrieval_parameters: optional PresetRetrievalParams`

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

    - `retrieval_mode: optional RetrievalMode`

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

    - `search_filters: optional MetadataFilters`

      Metadata filters for vector stores.

      - `filters: array of object { key, value, operator }  or MetadataFilters`

        - `MetadataFilter = object { key, value, operator }`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number or string or array of string or 2 more`

            - `number`

            - `string`

            - `array of string`

            - `array of number`

            - `array of number`

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

        - `MetadataFilters = object { filters, condition }`

          Metadata filters for vector stores.

      - `condition: optional "and" or "or" or "not"`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k: optional number`

      Number of nodes for sparse retrieval.

- `rerank_config: optional ReRankConfig`

  The rerank configuration for composite retrieval.

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

- `rerank_top_n: optional number`

  (use rerank_config.top_n instead) The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

### Returns

- `CompositeRetrievalResult = object { image_nodes, nodes, page_figure_nodes }`

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

```http
curl https://api.cloud.llamaindex.ai/api/v1/retrievers/retrieve \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "query": "x"
        }'
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
