# Files

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

## Delete File

`files.delete(strfile_id, FileDeleteParams**kwargs)`

**delete** `/api/v1/beta/files/{file_id}`

Delete a file from the project.

### Parameters

- `file_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.files.delete(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

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

## Domain Types

### File

- `class File: …`

  Schema for a file.

  - `id: str`

    Unique identifier

  - `name: str`

  - `project_id: str`

    The ID of the project that the file belongs to

  - `created_at: Optional[datetime]`

    Creation datetime

  - `data_source_id: Optional[str]`

    The ID of the data source that the file belongs to

  - `expires_at: Optional[datetime]`

    The expiration date for the file. Files past this date can be deleted.

  - `external_file_id: Optional[str]`

    The ID of the file in the external system

  - `file_size: Optional[int]`

    Size of the file in bytes

  - `file_type: Optional[str]`

    File type (e.g. pdf, docx, etc.)

  - `last_modified_at: Optional[datetime]`

    The last modified time of the file

  - `permission_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Permission information for the file

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `purpose: Optional[str]`

    The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

  - `resource_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Resource information for the file

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Presigned URL

- `class PresignedURL: …`

  Schema for a presigned URL.

  - `expires_at: datetime`

    The time at which the presigned URL expires

  - `url: str`

    A presigned URL for IO operations against a private file

  - `form_fields: Optional[Dict[str, str]]`

    Form fields for a presigned POST request

### File Create Response

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

### File Query Response

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

### File List Response

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
