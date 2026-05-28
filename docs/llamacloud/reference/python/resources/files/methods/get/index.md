## Read File Content

`files.get(strfile_id, FileGetParams**kwargs)  -> PresignedURL`

**get** `/api/v1/beta/files/{file_id}/content`

Get a presigned URL to download the file content.

### Parameters

- `file_id: str`

- `expires_at_seconds: Optional[int]`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class PresignedURL: …`

  Schema for a presigned URL.

  - `expires_at: datetime`

    The time at which the presigned URL expires

  - `url: str`

    A presigned URL for IO operations against a private file

  - `form_fields: Optional[Dict[str, str]]`

    Form fields for a presigned POST request

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
presigned_url = client.files.get(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(presigned_url.expires_at)
```

#### Response

```json
{
  "expires_at": "2019-12-27T18:11:19.117Z",
  "url": "https://example.com",
  "form_fields": {
    "foo": "string"
  }
}
```
