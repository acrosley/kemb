# Images

## List File Page Screenshots

`pipelines.images.list_page_screenshots(strid, ImageListPageScreenshotsParams**kwargs)  -> ImageListPageScreenshotsResponse`

**get** `/api/v1/files/{id}/page_screenshots`

List metadata for all screenshots of pages from a file.

### Parameters

- `id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `List[ImageListPageScreenshotsResponseItem]`

  - `file_id: str`

    The ID of the file that the page screenshot was taken from

  - `image_size: int`

    The size of the image in bytes

  - `page_index: int`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata: Optional[Dict[str, object]]`

    Metadata for the screenshot

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.pipelines.images.list_page_screenshots(
    id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response)
```

#### Response

```json
[
  {
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "image_size": 0,
    "page_index": 0,
    "metadata": {
      "foo": "bar"
    }
  }
]
```

## Get File Page Screenshot

`pipelines.images.get_page_screenshot(intpage_index, ImageGetPageScreenshotParams**kwargs)  -> object`

**get** `/api/v1/files/{id}/page_screenshots/{page_index}`

Get screenshot of a page from a file.

### Parameters

- `id: str`

- `page_index: int`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `object`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.pipelines.images.get_page_screenshot(
    page_index=0,
    id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response)
```

#### Response

```json
{}
```

## Get File Page Figure

`pipelines.images.get_page_figure(strfigure_name, ImageGetPageFigureParams**kwargs)  -> object`

**get** `/api/v1/files/{id}/page-figures/{page_index}/{figure_name}`

Get a specific figure from a page of a file.

### Parameters

- `id: str`

- `page_index: int`

- `figure_name: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `object`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.pipelines.images.get_page_figure(
    figure_name="figure_name",
    id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    page_index=0,
)
print(response)
```

#### Response

```json
{}
```

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

## Domain Types

### Image List Page Screenshots Response

- `List[ImageListPageScreenshotsResponseItem]`

  - `file_id: str`

    The ID of the file that the page screenshot was taken from

  - `image_size: int`

    The size of the image in bytes

  - `page_index: int`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata: Optional[Dict[str, object]]`

    Metadata for the screenshot

### Image List Page Figures Response

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
