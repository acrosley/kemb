## Delete Pipeline Document

`pipelines.documents.delete(strdocument_id, DocumentDeleteParams**kwargs)`

**delete** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Delete a document from a pipeline.
Initiates an async job that will:

1. Delete vectors from the vector store
1. Delete the document from MongoDB after vectors are successfully deleted

### Parameters

- `pipeline_id: str`

- `document_id: str`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.pipelines.documents.delete(
    document_id="document_id",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```
