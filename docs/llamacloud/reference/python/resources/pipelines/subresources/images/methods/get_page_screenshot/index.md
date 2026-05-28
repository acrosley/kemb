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
