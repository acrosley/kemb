## Get Pipeline Document

`pipelines.documents.get(strdocument_id, DocumentGetParams**kwargs)  -> CloudDocument`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Parameters

- `pipeline_id: str`

- `document_id: str`

### Returns

- `class CloudDocument: …`

  Cloud document stored in S3.

  - `id: str`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: Optional[Dict[str, object]]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
cloud_document = client.pipelines.documents.get(
    document_id="document_id",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(cloud_document.id)
```

#### Response

```json
{
  "id": "id",
  "metadata": {
    "foo": "bar"
  },
  "text": "text",
  "excluded_embed_metadata_keys": [
    "string"
  ],
  "excluded_llm_metadata_keys": [
    "string"
  ],
  "page_positions": [
    0
  ],
  "status_metadata": {
    "foo": "bar"
  }
}
```
