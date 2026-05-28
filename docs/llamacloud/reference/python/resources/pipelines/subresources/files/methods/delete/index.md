## Delete Pipeline File

`pipelines.files.delete(strfile_id, FileDeleteParams**kwargs)`

**delete** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Delete a file from a pipeline.

### Parameters

- `pipeline_id: str`

- `file_id: str`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.pipelines.files.delete(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```
