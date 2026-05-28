## Delete Data Source

`data_sources.delete(strdata_source_id)`

**delete** `/api/v1/data-sources/{data_source_id}`

Delete a data source by ID.

### Parameters

- `data_source_id: str`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.data_sources.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```
