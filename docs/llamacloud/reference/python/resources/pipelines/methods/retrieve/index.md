## Run Search

`pipelines.retrieve(strpipeline_id, PipelineRetrieveParams**kwargs)  -> PipelineRetrieveResponse`

**post** `/api/v1/pipelines/{pipeline_id}/retrieve`

Run a retrieval query against a managed pipeline.

Searches the pipeline's vector store using the provided query
and retrieval parameters. Supports dense, sparse, and hybrid
search modes with configurable top-k and reranking.

### Parameters

- `pipeline_id: str`

- `query: str`

  The query to retrieve against.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `alpha: Optional[float]`

  Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

- `class_name: Optional[str]`

- `dense_similarity_cutoff: Optional[float]`

  Minimum similarity score wrt query for retrieval

- `dense_similarity_top_k: Optional[int]`

  Number of nodes for dense retrieval.

- `enable_reranking: Optional[bool]`

  Enable reranking for retrieval

- `files_top_k: Optional[int]`

  Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

- `rerank_top_n: Optional[int]`

  Number of reranked nodes for returning.

- `retrieval_mode: Optional[RetrievalMode]`

  The retrieval mode for the query.

  - `"chunks"`

  - `"files_via_metadata"`

  - `"files_via_content"`

  - `"auto_routed"`

- `retrieve_image_nodes: Optional[bool]`

  Whether to retrieve image nodes.

- `retrieve_page_figure_nodes: Optional[bool]`

  Whether to retrieve page figure nodes.

- `retrieve_page_screenshot_nodes: Optional[bool]`

  Whether to retrieve page screenshot nodes.

- `search_filters: Optional[MetadataFiltersParam]`

  Metadata filters for vector stores.

  - `filters: List[Filter]`

    - `class FilterMetadataFilter: …`

      Comprehensive metadata filter for vector stores to support more operators.

      Value uses Strict types, as int, float and str are compatible types and were all
      converted to string before.

      See: https://docs.pydantic.dev/latest/usage/types/#strict-types

      - `key: str`

      - `value: Union[float, str, List[str], 3 more]`

        - `float`

        - `str`

        - `List[str]`

        - `List[float]`

        - `List[int]`

      - `operator: Optional[Literal["==", ">", "<", 11 more]]`

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

    - `class MetadataFilters: …`

      Metadata filters for vector stores.

  - `condition: Optional[Literal["and", "or", "not"]]`

    Vector store filter conditions to combine different filters.

    - `"and"`

    - `"or"`

    - `"not"`

- `search_filters_inference_schema: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, 3 more]]]`

  JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

  - `Dict[str, object]`

  - `Iterable[object]`

  - `str`

  - `float`

  - `bool`

- `sparse_similarity_top_k: Optional[int]`

  Number of nodes for sparse retrieval.

### Returns

- `class PipelineRetrieveResponse: …`

  Schema for the result of an retrieval execution.

  - `pipeline_id: str`

    The ID of the pipeline that the query was retrieved against.

  - `retrieval_nodes: List[RetrievalNode]`

    The nodes retrieved by the pipeline for the given query.

    - `node: TextNode`

      Provided for backward compatibility.

      - `class_name: Optional[str]`

      - `embedding: Optional[List[float]]`

        Embedding of the node.

      - `end_char_idx: Optional[int]`

        End char index of the node.

      - `excluded_embed_metadata_keys: Optional[List[str]]`

        Metadata keys that are excluded from text for the embed model.

      - `excluded_llm_metadata_keys: Optional[List[str]]`

        Metadata keys that are excluded from text for the LLM.

      - `extra_info: Optional[Dict[str, object]]`

        A flat dictionary of metadata fields

      - `id: Optional[str]`

        Unique ID of the node.

      - `metadata_seperator: Optional[str]`

        Separator between metadata fields when converting to string.

      - `metadata_template: Optional[str]`

        Template for how metadata is formatted, with {key} and {value} placeholders.

      - `mimetype: Optional[str]`

        MIME type of the node content.

      - `relationships: Optional[Dict[str, Relationships]]`

        A mapping of relationships to other node information.

        - `class RelationshipsRelatedNodeInfo: …`

          - `node_id: str`

          - `class_name: Optional[str]`

          - `hash: Optional[str]`

          - `metadata: Optional[Dict[str, object]]`

          - `node_type: Optional[Union[Literal["1", "2", "3", 2 more], str, null]]`

            - `Literal["1", "2", "3", 2 more]`

              - `"1"`

              - `"2"`

              - `"3"`

              - `"4"`

              - `"5"`

            - `str`

        - `List[RelationshipsUnionMember1]`

          - `node_id: str`

          - `class_name: Optional[str]`

          - `hash: Optional[str]`

          - `metadata: Optional[Dict[str, object]]`

          - `node_type: Optional[Union[Literal["1", "2", "3", 2 more], str, null]]`

            - `Literal["1", "2", "3", 2 more]`

              - `"1"`

              - `"2"`

              - `"3"`

              - `"4"`

              - `"5"`

            - `str`

      - `start_char_idx: Optional[int]`

        Start char index of the node.

      - `text: Optional[str]`

        Text content of the node.

      - `text_template: Optional[str]`

        Template for how text is formatted, with {content} and {metadata_str} placeholders.

    - `class_name: Optional[str]`

    - `score: Optional[float]`

  - `class_name: Optional[str]`

  - `image_nodes: Optional[List[PageScreenshotNodeWithScore]]`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: Node`

      - `file_id: str`

        The ID of the file that the page screenshot was taken from

      - `image_size: int`

        The size of the image in bytes

      - `page_index: int`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata: Optional[Dict[str, object]]`

        Metadata for the screenshot

    - `score: float`

      The score of the screenshot node

    - `class_name: Optional[str]`

  - `inferred_search_filters: Optional[MetadataFilters]`

    Metadata filters for vector stores.

    - `filters: List[Filter]`

      - `class FilterMetadataFilter: …`

        Comprehensive metadata filter for vector stores to support more operators.

        Value uses Strict types, as int, float and str are compatible types and were all
        converted to string before.

        See: https://docs.pydantic.dev/latest/usage/types/#strict-types

        - `key: str`

        - `value: Union[float, str, List[str], 3 more]`

          - `float`

          - `str`

          - `List[str]`

          - `List[float]`

          - `List[int]`

        - `operator: Optional[Literal["==", ">", "<", 11 more]]`

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

      - `class MetadataFilters: …`

        Metadata filters for vector stores.

    - `condition: Optional[Literal["and", "or", "not"]]`

      Vector store filter conditions to combine different filters.

      - `"and"`

      - `"or"`

      - `"not"`

  - `metadata: Optional[Dict[str, str]]`

    Metadata associated with the retrieval execution

  - `page_figure_nodes: Optional[List[PageFigureNodeWithScore]]`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: Node`

      - `confidence: float`

        The confidence of the figure

      - `figure_name: str`

        The name of the figure

      - `figure_size: int`

        The size of the figure in bytes

      - `file_id: str`

        The ID of the file that the figure was taken from

      - `page_index: int`

        The index of the page for which the figure is taken (0-indexed)

      - `is_likely_noise: Optional[bool]`

        Whether the figure is likely to be noise

      - `metadata: Optional[Dict[str, object]]`

        Metadata for the figure

    - `score: float`

      The score of the figure node

    - `class_name: Optional[str]`

  - `retrieval_latency: Optional[Dict[str, float]]`

    The end-to-end latency for retrieval and reranking.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
pipeline = client.pipelines.retrieve(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    query="x",
)
print(pipeline.pipeline_id)
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
