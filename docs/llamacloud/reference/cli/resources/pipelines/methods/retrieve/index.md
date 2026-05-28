## Run Search

`$ llamacloud-prod pipelines retrieve`

**post** `/api/v1/pipelines/{pipeline_id}/retrieve`

Run a retrieval query against a managed pipeline.

Searches the pipeline's vector store using the provided query
and retrieval parameters. Supports dense, sparse, and hybrid
search modes with configurable top-k and reranking.

### Parameters

- `--pipeline-id: string`

  Path param

- `--query: string`

  Body param: The query to retrieve against.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--alpha: optional number`

  Body param: Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

- `--class-name: optional string`

  Body param

- `--dense-similarity-cutoff: optional number`

  Body param: Minimum similarity score wrt query for retrieval

- `--dense-similarity-top-k: optional number`

  Body param: Number of nodes for dense retrieval.

- `--enable-reranking: optional boolean`

  Body param: Enable reranking for retrieval

- `--files-top-k: optional number`

  Body param: Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

- `--rerank-top-n: optional number`

  Body param: Number of reranked nodes for returning.

- `--retrieval-mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

  Body param: The retrieval mode for the query.

- `--retrieve-image-nodes: optional boolean`

  Body param: Whether to retrieve image nodes.

- `--retrieve-page-figure-nodes: optional boolean`

  Body param: Whether to retrieve page figure nodes.

- `--retrieve-page-screenshot-nodes: optional boolean`

  Body param: Whether to retrieve page screenshot nodes.

- `--search-filters: optional object { filters, condition }`

  Body param: Metadata filters for vector stores.

- `--search-filters-inference-schema: optional map[map[unknown] or array of unknown or string or 2 more]`

  Body param: JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

- `--sparse-similarity-top-k: optional number`

  Body param: Number of nodes for sparse retrieval.

### Returns

- `PipelineGetResponse: object { pipeline_id, retrieval_nodes, class_name, 5 more }`

  Schema for the result of an retrieval execution.

  - `pipeline_id: string`

    The ID of the pipeline that the query was retrieved against.

  - `retrieval_nodes: array of object { node, class_name, score }`

    The nodes retrieved by the pipeline for the given query.

    - `node: object { class_name, embedding, end_char_idx, 11 more }`

      Provided for backward compatibility.

      - `class_name: optional string`

      - `embedding: optional array of number`

        Embedding of the node.

      - `end_char_idx: optional number`

        End char index of the node.

      - `excluded_embed_metadata_keys: optional array of string`

        Metadata keys that are excluded from text for the embed model.

      - `excluded_llm_metadata_keys: optional array of string`

        Metadata keys that are excluded from text for the LLM.

      - `extra_info: optional map[unknown]`

        A flat dictionary of metadata fields

      - `id_: optional string`

        Unique ID of the node.

      - `metadata_seperator: optional string`

        Separator between metadata fields when converting to string.

      - `metadata_template: optional string`

        Template for how metadata is formatted, with {key} and {value} placeholders.

      - `mimetype: optional string`

        MIME type of the node content.

      - `relationships: optional map[object { node_id, class_name, hash, 2 more }  or array of object { node_id, class_name, hash, 2 more } ]`

        A mapping of relationships to other node information.

        - `RelatedNodeInfo: object { node_id, class_name, hash, 2 more }`

          - `node_id: string`

          - `class_name: optional string`

          - `hash: optional string`

          - `metadata: optional map[unknown]`

          - `node_type: optional "1" or "2" or "3" or 2 more or string`

            - `"1"`

            - `"2"`

            - `"3"`

            - `"4"`

            - `"5"`

        - `union_member_1: array of object { node_id, class_name, hash, 2 more }`

          - `node_id: string`

          - `class_name: optional string`

          - `hash: optional string`

          - `metadata: optional map[unknown]`

          - `node_type: optional "1" or "2" or "3" or 2 more or string`

            - `"1"`

            - `"2"`

            - `"3"`

            - `"4"`

            - `"5"`

      - `start_char_idx: optional number`

        Start char index of the node.

      - `text: optional string`

        Text content of the node.

      - `text_template: optional string`

        Template for how text is formatted, with {content} and {metadata_str} placeholders.

    - `class_name: optional string`

    - `score: optional number`

  - `class_name: optional string`

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

  - `inferred_search_filters: optional object { filters, condition }`

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

  - `metadata: optional map[string]`

    Metadata associated with the retrieval execution

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

  - `retrieval_latency: optional map[number]`

    The end-to-end latency for retrieval and reranking.

### Example

```cli
llamacloud-prod pipelines retrieve \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --query x
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
