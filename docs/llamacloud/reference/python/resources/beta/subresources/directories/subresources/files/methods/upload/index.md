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
