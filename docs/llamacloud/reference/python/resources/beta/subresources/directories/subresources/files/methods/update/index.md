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
