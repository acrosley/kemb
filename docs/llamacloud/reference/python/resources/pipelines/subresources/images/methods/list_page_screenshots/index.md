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
