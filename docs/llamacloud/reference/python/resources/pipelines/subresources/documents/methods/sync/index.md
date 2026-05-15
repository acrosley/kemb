## Sync Pipeline Document

`pipelines.documents.sync(strdocument_id, DocumentSyncParams**kwargs)  -> object`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `pipeline_id: str`

- `document_id: str`

### Returns

- `object`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.pipelines.documents.sync(
    document_id="document_id",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response)
```

#### Response

```json
{}
```
