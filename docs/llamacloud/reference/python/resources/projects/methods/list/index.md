## List Projects

`projects.list(ProjectListParams**kwargs)  -> ProjectListResponse`

**get** `/api/v1/projects`

List projects or get one by name

### Parameters

- `organization_id: Optional[str]`

- `project_name: Optional[str]`

### Returns

- `List[Project]`

  - `id: str`

    Unique identifier

  - `name: str`

  - `organization_id: str`

    The Organization ID the project is under.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `is_default: Optional[bool]`

    Whether this project is the default project for the user.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
projects = client.projects.list()
print(projects)
```

#### Response

```json
[
  {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "name": "x",
    "organization_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "is_default": true,
    "updated_at": "2019-12-27T18:11:19.117Z"
  }
]
```
