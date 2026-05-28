## List Parse Jobs

`client.parsing.list(ParsingListParamsquery?, RequestOptionsoptions?): PaginatedCursor<ParsingListResponse>`

**get** `/api/v2/parse`

List parse jobs for the current project.

Filter by `status` or creation date range. Results are
paginated — use `page_token` from the response to fetch
subsequent pages.

### Parameters

- `query: ParsingListParams`

  - `created_at_on_or_after?: string | null`

    Include items created at or after this timestamp (inclusive)

  - `created_at_on_or_before?: string | null`

    Include items created at or before this timestamp (inclusive)

  - `job_ids?: Array<string> | null`

    Filter by specific job IDs

  - `organization_id?: string | null`

  - `page_size?: number | null`

    Number of items per page

  - `page_token?: string | null`

    Token for pagination

  - `project_id?: string | null`

  - `status?: "PENDING" | "RUNNING" | "COMPLETED" | 2 more | null`

    Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

### Returns

- `ParsingListResponse`

  A parse job.

  - `id: string`

    Unique parse job identifier

  - `project_id: string`

    Project this job belongs to

  - `status: "PENDING" | "RUNNING" | "COMPLETED" | 2 more`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error details when status is FAILED

  - `name?: string | null`

    Optional display name for this parse job

  - `tier?: string | null`

    Parsing tier used for this job

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const parsingListResponse of client.parsing.list()) {
  console.log(parsingListResponse.id);
}
```

#### Response

```json
{
  "items": [
    {
      "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "status": "PENDING",
      "created_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "name": "Q4 Financial Report",
      "tier": "fast",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
