## Delete Pipeline

`pipelines.delete(strpipeline_id)`

**delete** `/api/v1/pipelines/{pipeline_id}`

Delete a pipeline and all associated resources.

Removes pipeline files, data sources, and vector store data.
This operation is irreversible.

### Parameters

- `pipeline_id: str`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.pipelines.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```
