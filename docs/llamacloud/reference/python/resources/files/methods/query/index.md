## Query Files

`files.query(FileQueryParams**kwargs)  -> FileQueryResponse`

**post** `/api/v1/beta/files/query`

Query files with flexible filtering and pagination.

**Deprecated**: Use GET /files instead for listing files with query parameters.

Args:
request: The query request with filters and pagination
project: Validated project from dependency

Returns:
Paginated response with files

### Parameters

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `filter: Optional[Filter]`

  Filter parameters for file queries.

  - `data_source_id: Optional[str]`

    Filter by data source ID

  - `external_file_id: Optional[str]`

    Filter by external file ID

  - `file_ids: Optional[SequenceNotStr[str]]`

    Filter by specific file IDs

  - `file_name: Optional[str]`

    Filter by file name

  - `only_manually_uploaded: Optional[bool]`

    Filter only manually uploaded files (data_source_id is null)

  - `project_id: Optional[str]`

    Filter by project ID

- `order_by: Optional[str]`

  A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `page_size: Optional[int]`

  The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `page_token: Optional[str]`

  A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `class FileQueryResponse: …`

  Paginated list of files.

  - `items: List[Item]`

    The list of items.

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

  - `next_page_token: Optional[str]`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: Optional[int]`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.files.query()
print(response.items)
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
