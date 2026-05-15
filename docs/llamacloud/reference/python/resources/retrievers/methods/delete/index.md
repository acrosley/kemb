## Delete Retriever

`retrievers.delete(strretriever_id, RetrieverDeleteParams**kwargs)`

**delete** `/api/v1/retrievers/{retriever_id}`

Delete a Retriever by ID.

### Parameters

- `retriever_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.retrievers.delete(
    retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```
