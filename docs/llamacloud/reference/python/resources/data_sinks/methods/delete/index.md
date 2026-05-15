## Delete Data Sink

`data_sinks.delete(strdata_sink_id)`

**delete** `/api/v1/data-sinks/{data_sink_id}`

Delete a data sink by ID.

### Parameters

- `data_sink_id: str`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.data_sinks.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```
