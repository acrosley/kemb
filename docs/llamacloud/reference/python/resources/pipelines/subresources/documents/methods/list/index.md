## Paginated List Pipeline Documents

`pipelines.documents.list(strpipeline_id, DocumentListParams**kwargs)  -> SyncPaginatedCloudDocuments[CloudDocument]`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `pipeline_id: str`

- `file_id: Optional[str]`

- `limit: Optional[int]`

- `only_api_data_source_documents: Optional[bool]`

- `only_direct_upload: Optional[bool]`

- `skip: Optional[int]`

- `status_refresh_policy: Optional[Literal["cached", "ttl"]]`

  - `"cached"`

  - `"ttl"`

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
page = client.pipelines.documents.list(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
page = page.documents[0]
print(page.id)
```

#### Response

```json
{
  "documents": [
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
  ],
  "limit": 0,
  "offset": 0,
  "total_count": 0
}
```
