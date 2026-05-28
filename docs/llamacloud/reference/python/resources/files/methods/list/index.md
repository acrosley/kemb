## List Files

`files.list(FileListParams**kwargs)  -> SyncPaginatedCursor[FileListResponse]`

**get** `/api/v1/beta/files`

List files with optional filtering and pagination.

Filter by `file_name`, `file_ids`, or `external_file_id`.
Supports cursor-based pagination and custom ordering.

### Parameters

- `expand: Optional[SequenceNotStr[str]]`

  Fields to expand on each file.

- `external_file_id: Optional[str]`

  Filter by external file ID.

- `file_ids: Optional[SequenceNotStr[str]]`

  Filter by specific file IDs.

- `file_name: Optional[str]`

  Filter by file name (exact match).

- `order_by: Optional[str]`

  A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

  The maximum number of items to return. Defaults to 50, maximum is 1000.

- `page_token: Optional[str]`

  A page token received from a previous list call. Provide this to retrieve the subsequent page.

- `project_id: Optional[str]`

### Returns

- `class FileListResponse: …`

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
page = client.files.list()
page = page.items[0]
print(page.id)
```

#### Response

```json
{
  "items": [
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
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
