## List Batch Job Items

`$ llamacloud-prod beta:batch:job-items list`

**get** `/api/v1/beta/batch-processing/{job_id}/items`

List items in a batch job with optional status filtering.

Useful for finding failed items, viewing completed items,
or debugging processing issues.

### Parameters

- `--job-id: string`

- `--limit: optional number`

  Maximum number of items to return

- `--offset: optional number`

  Number of items to skip

- `--organization-id: optional string`

- `--project-id: optional string`

- `--status: optional "pending" or "processing" or "completed" or 3 more`

  Filter items by status

### Returns

- `BatchItemListResponse: object { items, next_page_token, total_size }`

  Paginated response containing batch job item details.

  - `items: optional array of object { item_id, item_name, status, 7 more }`

    List of item details

    - `item_id: string`

      ID of the item

    - `item_name: string`

      Name of the item

    - `status: "pending" or "processing" or "completed" or 3 more`

      Processing status of this item

      - `"pending"`

      - `"processing"`

      - `"completed"`

      - `"failed"`

      - `"skipped"`

      - `"cancelled"`

    - `completed_at: optional string`

      When processing completed for this item

    - `effective_at: optional string`

    - `error_message: optional string`

      Error message for the latest job attempt, if any.

    - `job_id: optional string`

      Job ID for the underlying processing job (links to parse/extract job results)

    - `job_record_id: optional string`

      The job record ID associated with this status, if any.

    - `skip_reason: optional string`

      Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

    - `started_at: optional string`

      When processing started for this item

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:batch:job-items list \
  --api-key 'My API Key' \
  --job-id job_id
```

#### Response

```json
{
  "items": [
    {
      "item_id": "item_id",
      "item_name": "item_name",
      "status": "pending",
      "completed_at": "2019-12-27T18:11:19.117Z",
      "effective_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "job_id": "job_id",
      "job_record_id": "job_record_id",
      "skip_reason": "skip_reason",
      "started_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
