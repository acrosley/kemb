## Get Project

`$ llamacloud-prod projects get`

**get** `/api/v1/projects/{project_id}`

Get a project by ID.

### Parameters

- `--project-id: string`

- `--organization-id: optional string`

### Returns

- `project: object { id, name, organization_id, 3 more }`

  Schema for a project.

  - `id: string`

    Unique identifier

  - `name: string`

  - `organization_id: string`

    The Organization ID the project is under.

  - `created_at: optional string`

    Creation datetime

  - `is_default: optional boolean`

    Whether this project is the default project for the user.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod projects get \
  --api-key 'My API Key' \
  --project-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "name": "x",
  "organization_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "created_at": "2019-12-27T18:11:19.117Z",
  "is_default": true,
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
