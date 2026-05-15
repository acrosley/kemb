## List Split Jobs

**get** `/api/v1/beta/split/jobs`

List document split jobs.

### Query Parameters

- `created_at_on_or_after: optional string`

  Include items created at or after this timestamp (inclusive)

- `created_at_on_or_before: optional string`

  Include items created at or before this timestamp (inclusive)

- `job_ids: optional array of string`

  Filter by specific job IDs

- `organization_id: optional string`

- `page_size: optional number`

- `page_token: optional string`

- `project_id: optional string`

- `status: optional "pending" or "processing" or "completed" or 2 more`

  Filter by job status (pending, processing, completed, failed, cancelled)

  - `"pending"`

  - `"processing"`

  - `"completed"`

  - `"failed"`

  - `"cancelled"`

### Cookie Parameters

- `session: optional string`

### Returns

- `items: array of object { id, categories, document_input, 8 more }`

  The list of items.

  - `id: string`

    Unique identifier for the split job.

  - `categories: array of SplitCategory`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description: optional string`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

    Document that was split.

    - `type: string`

      Type of document input. Valid values are: file_id

    - `value: string`

      Document identifier.

  - `project_id: string`

    Project ID this job belongs to.

  - `status: string`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: string`

    User ID who created this job.

  - `configuration_id: optional string`

    Split configuration ID used for this job.

  - `created_at: optional string`

    Creation datetime

  - `error_message: optional string`

    Error message if the job failed.

  - `result: optional SplitResultResponse`

    Result of a completed split job.

    - `segments: array of SplitSegmentResponse`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: array of number`

        1-indexed page numbers in this split.

  - `updated_at: optional string`

    Update datetime

- `next_page_token: optional string`

  A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

- `total_size: optional number`

  The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "categories": [
        {
          "name": "x",
          "description": "x"
        }
      ],
      "document_input": {
        "type": "type",
        "value": "value"
      },
      "project_id": "project_id",
      "status": "status",
      "user_id": "user_id",
      "configuration_id": "configuration_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "result": {
        "segments": [
          {
            "category": "category",
            "confidence_category": "confidence_category",
            "pages": [
              0
            ]
          }
        ]
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
