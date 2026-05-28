## List File Pages Figures

`pipelines.images.list_page_figures(strid, ImageListPageFiguresParams**kwargs)  -> ImageListPageFiguresResponse`

**get** `/api/v1/files/{id}/page-figures`

List metadata for all figures from all pages of a file.

### Parameters

- `id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `List[ImageListPageFiguresResponseItem]`

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

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.pipelines.images.list_page_figures(
    id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response)
```

#### Response

```json
[
  {
    "confidence": 0,
    "figure_name": "figure_name",
    "figure_size": 0,
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "page_index": 0,
    "is_likely_noise": true,
    "metadata": {
      "foo": "bar"
    }
  }
]
```
