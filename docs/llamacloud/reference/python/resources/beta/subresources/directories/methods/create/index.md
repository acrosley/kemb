## Create Directory

`beta.directories.create(DirectoryCreateParams**kwargs)  -> DirectoryCreateResponse`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `name: str`

  Human-readable name for the directory.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `description: Optional[str]`

  Optional description shown to users.

### Returns

- `class DirectoryCreateResponse: …`

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
directory = client.beta.directories.create(
    name="x",
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
