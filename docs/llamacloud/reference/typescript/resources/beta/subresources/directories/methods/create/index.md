## Create Directory

`client.beta.directories.create(DirectoryCreateParamsparams, RequestOptionsoptions?): DirectoryCreateResponse`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `params: DirectoryCreateParams`

  - `name: string`

    Body param: Human-readable name for the directory.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `description?: string | null`

    Body param: Optional description shown to users.

### Returns

- `DirectoryCreateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const directory = await client.beta.directories.create({ name: 'x' });

console.log(directory.id);
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
