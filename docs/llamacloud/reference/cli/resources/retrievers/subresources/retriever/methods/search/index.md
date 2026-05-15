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
