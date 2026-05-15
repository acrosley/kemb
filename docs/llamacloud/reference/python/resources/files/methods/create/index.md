## Upload File

`files.create(FileCreateParams**kwargs)  -> FileCreateResponse`

**post** `/api/v1/beta/files`

Upload a file using multipart/form-data.

Set `purpose` to indicate how the file will be used:
`user_data`, `parse`, `extract`, `classify`, `split`,
`sheet`, or `agent_app`.

Returns the created file metadata including its ID for use
in subsequent parse, extract, or classify operations.

### Parameters

- `file: FileTypes`

  The file to upload

- `purpose: str`

  The intended purpose of the file. Valid values: 'user_data', 'parse', 'extract', 'split', 'classify', 'sheet', 'agent_app'. This determines the storage and retention policy for the file.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `external_file_id: Optional[str]`

  The ID of the file in the external system

### Returns

- `class FileCreateResponse: …`

  An uploaded file.

  - `id: str`

    Unique file identifier

  - `name: str`

    File name including extension

  - `project_id: str`

    Project this file belongs to

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `expires_at: Optional[datetime]`

    When the file expires and may be automatically removed. Null means no expiration.

  - `external_file_id: Optional[str]`

    Optional ID for correlating with an external system

  - `file_type: Optional[str]`

    File extension (pdf, docx, png, etc.)

  - `last_modified_at: Optional[datetime]`

    When the file was last modified (ISO 8601)

  - `purpose: Optional[str]`

    How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
file = client.files.create(
    file=b"Example data",
    purpose="purpose",
)
print(file.id)
```

#### Response

```json
{
  "id": "dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "name": "invoice.pdf",
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "expires_at": "2019-12-27T18:11:19.117Z",
  "external_file_id": "ext-12345",
  "file_type": "pdf",
  "last_modified_at": "2019-12-27T18:11:19.117Z",
  "purpose": "parse"
}
```
