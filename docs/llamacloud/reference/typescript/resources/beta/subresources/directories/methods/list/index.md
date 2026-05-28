## List Directories

`client.beta.directories.list(DirectoryListParamsquery?, RequestOptionsoptions?): PaginatedCursor<DirectoryListResponse>`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `query: DirectoryListParams`

  - `include_deleted?: boolean`

  - `name?: string | null`

  - `organization_id?: string | null`

  - `page_size?: number | null`

  - `page_token?: string | null`

  - `project_id?: string | null`

  - `type?: "user" | "index" | null`

    - `"user"`

    - `"index"`

### Returns

- `DirectoryListResponse`

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

// Automatically fetches more pages as needed.
for await (const directoryListResponse of client.beta.directories.list()) {
  console.log(directoryListResponse.id);
}
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "name": "x",
      "project_id": "project_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "deleted_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
