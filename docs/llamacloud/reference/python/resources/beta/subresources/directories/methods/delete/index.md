## Delete Directory

`beta.directories.delete(strdirectory_id, DirectoryDeleteParams**kwargs)`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `directory_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.beta.directories.delete(
    directory_id="directory_id",
)
```
