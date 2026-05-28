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
