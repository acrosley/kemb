## Delete File

`files.delete(strfile_id, FileDeleteParams**kwargs)`

**delete** `/api/v1/beta/files/{file_id}`

Delete a file from the project.

### Parameters

- `file_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.files.delete(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```
