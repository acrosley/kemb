## Retrieve

`retrievers.retriever.search(strretriever_id, RetrieverSearchParams**kwargs)  -> CompositeRetrievalResult`

**post** `/api/v1/retrievers/{retriever_id}/retrieve`

Retrieve data using a Retriever.

### Parameters

- `retriever_id: str`

- `query: str`

  The query to retrieve against.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `mode: Optional[CompositeRetrievalMode]`

  The mode of composite retrieval.

  - `"routing"`

  - `"full"`

- `rerank_config: Optional[ReRankConfigParam]`

  The rerank configuration for composite retrieval.

  - `top_n: Optional[int]`

    The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

  - `type: Optional[Literal["system_default", "llm", "cohere", 3 more]]`

    The type of reranker to use.

    - `"system_default"`

    - `"llm"`

    - `"cohere"`

    - `"bedrock"`

    - `"score"`

    - `"disabled"`

- `rerank_top_n: Optional[int]`

  (use rerank_config.top_n instead) The number of nodes to retrieve after reranking over retrieved nodes from all retrieval tools.

### Returns

- `class CompositeRetrievalResult: …`

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

  - `nodes: Optional[List[Node]]`

    The retrieved nodes from the composite retrieval.

    - `node: NodeNode`

      - `id: str`

        The ID of the retrieved node.

      - `end_char_idx: Optional[int]`

        The end character index of the retrieved node in the document

      - `pipeline_id: str`

        The ID of the pipeline this node was retrieved from.

      - `retriever_id: str`

        The ID of the retriever this node was retrieved from.

      - `retriever_pipeline_name: str`

        The name of the retrieval pipeline this node was retrieved from.

      - `start_char_idx: Optional[int]`

        The start character index of the retrieved node in the document

      - `text: str`

        The text of the retrieved node.

      - `metadata: Optional[Dict[str, object]]`

        Metadata associated with the retrieved node.

    - `class_name: Optional[str]`

    - `score: Optional[float]`

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

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
composite_retrieval_result = client.retrievers.retriever.search(
    retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    query="x",
)
print(composite_retrieval_result.image_nodes)
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
