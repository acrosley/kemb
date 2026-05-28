# Files

## Add Directory File

`beta.directories.files.add(strdirectory_id, FileAddParams**kwargs)  -> FileAddResponse`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `directory_id: str`

- `file_id: str`

  File ID for the storage location (required).

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `display_name: Optional[str]`

  Display name for the file. If not provided, will use the file's name.

- `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

  User-defined metadata key-value pairs to associate with the file.

  - `str`

  - `float`

  - `bool`

- `unique_id: Optional[str]`

  Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `class FileAddResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.directories.files.add(
    directory_id="directory_id",
    file_id="file_id",
)
print(response.id)
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Directory Files

`beta.directories.files.list(strdirectory_id, FileListParams**kwargs)  -> SyncPaginatedCursor[FileListResponse]`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `directory_id: str`

- `display_name: Optional[str]`

- `display_name_contains: Optional[str]`

- `expand: Optional[SequenceNotStr[str]]`

  Fields to expand on each directory file.

- `file_id: Optional[str]`

- `include_deleted: Optional[bool]`

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

- `page_token: Optional[str]`

- `project_id: Optional[str]`

- `unique_id: Optional[str]`

- `updated_at_on_or_after: Optional[Union[str, datetime, null]]`

  Include items updated at or after this timestamp (inclusive)

- `updated_at_on_or_before: Optional[Union[str, datetime, null]]`

  Include items updated at or before this timestamp (inclusive)

### Returns

- `class FileListResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.directories.files.list(
    directory_id="directory_id",
)
page = page.items[0]
print(page.id)
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "directory_id": "directory_id",
      "display_name": "x",
      "project_id": "project_id",
      "unique_id": "x",
      "created_at": "2019-12-27T18:11:19.117Z",
      "deleted_at": "2019-12-27T18:11:19.117Z",
      "download_url": {
        "expires_at": "2019-12-27T18:11:19.117Z",
        "url": "https://example.com",
        "form_fields": {
          "foo": "string"
        }
      },
      "file_id": "file_id",
      "metadata": {
        "foo": "string"
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Directory File

`beta.directories.files.get(strdirectory_file_id, FileGetParams**kwargs)  -> FileGetResponse`

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Parameters

- `directory_id: str`

- `directory_file_id: str`

- `expand: Optional[SequenceNotStr[str]]`

  Fields to expand.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class FileGetResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
file = client.beta.directories.files.get(
    directory_file_id="directory_file_id",
    directory_id="directory_id",
)
print(file.id)
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Directory File

`beta.directories.files.update(strdirectory_file_id, FileUpdateParams**kwargs)  -> FileUpdateResponse`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directory_id: str`

- `directory_file_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `directory_id: str`

- `display_name: Optional[str]`

  Updated display name.

- `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

  User-defined metadata key-value pairs. Replaces the user metadata layer.

  - `str`

  - `float`

  - `bool`

- `unique_id: Optional[str]`

  Updated unique identifier.

### Returns

- `class FileUpdateResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
file = client.beta.directories.files.update(
    directory_file_id="directory_file_id",
    path_directory_id="directory_id",
)
print(file.id)
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Directory File

`beta.directories.files.delete(strdirectory_file_id, FileDeleteParams**kwargs)`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directory_id: str`

- `directory_file_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.beta.directories.files.delete(
    directory_file_id="directory_file_id",
    directory_id="directory_id",
)
```

## Upload File To Directory

`beta.directories.files.upload(strdirectory_id, FileUploadParams**kwargs)  -> FileUploadResponse`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `directory_id: str`

- `upload_file: FileTypes`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `display_name: Optional[str]`

- `external_file_id: Optional[str]`

- `metadata: Optional[str]`

  User metadata as a JSON object string.

- `unique_id: Optional[str]`

### Returns

- `class FileUploadResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.directories.files.upload(
    directory_id="directory_id",
    upload_file=b"Example data",
)
print(response.id)
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Domain Types

### File Add Response

- `class FileAddResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### File List Response

- `class FileListResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### File Get Response

- `class FileGetResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### File Update Response

- `class FileUpdateResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### File Upload Response

- `class FileUploadResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime
