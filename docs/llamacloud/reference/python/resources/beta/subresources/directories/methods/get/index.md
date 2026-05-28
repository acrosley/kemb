## Get Directory

`beta.directories.get(strdirectory_id, DirectoryGetParams**kwargs)  -> DirectoryGetResponse`

**get** `/api/v1/beta/directories/{directory_id}`

Retrieve a directory by its identifier.

### Parameters

- `directory_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class DirectoryGetResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
directory = client.beta.directories.get(
    directory_id="directory_id",
)
print(directory.id)
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
