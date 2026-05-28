## List Projects

`client.projects.list(ProjectListParamsquery?, RequestOptionsoptions?): ProjectListResponse`

**get** `/api/v1/projects`

List projects or get one by name

### Parameters

- `query: ProjectListParams`

  - `organization_id?: string | null`

  - `project_name?: string | null`

### Returns

- `ProjectListResponse = Array<Project>`

  - `id: string`

    Unique identifier

  - `name: string`

  - `organization_id: string`

    The Organization ID the project is under.

  - `created_at?: string | null`

    Creation datetime

  - `is_default?: boolean`

    Whether this project is the default project for the user.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const projects = await client.projects.list();

console.log(projects);
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
