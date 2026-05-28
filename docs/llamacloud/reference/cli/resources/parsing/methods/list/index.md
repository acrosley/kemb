## List Parse Jobs

`$ llamacloud-prod parsing list`

**get** `/api/v2/parse`

List parse jobs for the current project.

Filter by `status` or creation date range. Results are
paginated — use `page_token` from the response to fetch
subsequent pages.

### Parameters

- `--created-at-on-or-after: optional string`

  Include items created at or after this timestamp (inclusive)

- `--created-at-on-or-before: optional string`

  Include items created at or before this timestamp (inclusive)

- `--job-id: optional array of string`

  Filter by specific job IDs

- `--organization-id: optional string`

- `--page-size: optional number`

  Number of items per page

- `--page-token: optional string`

  Token for pagination

- `--project-id: optional string`

- `--status: optional "PENDING" or "RUNNING" or "COMPLETED" or 2 more`

  Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

### Returns

- `ParseJobQueryResponse: object { items, next_page_token, total_size }`

  Response schema for paginated parse job queries.

  - `items: array of object { id, project_id, status, 5 more }`

    The list of items.

    - `id: string`

      Unique parse job identifier

    - `project_id: string`

      Project this job belongs to

    - `status: "PENDING" or "RUNNING" or "COMPLETED" or 2 more`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `"PENDING"`

      - `"RUNNING"`

      - `"COMPLETED"`

      - `"FAILED"`

      - `"CANCELLED"`

    - `created_at: optional string`

      Creation datetime

    - `error_message: optional string`

      Error details when status is FAILED

    - `name: optional string`

      Optional display name for this parse job

    - `tier: optional string`

      Parsing tier used for this job

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod parsing list \
  --api-key 'My API Key'
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
