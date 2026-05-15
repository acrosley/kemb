## List Batch Job Items

`client.Beta.Batch.JobItems.List(ctx, jobID, query) (*PaginatedBatchItems[BetaBatchJobItemListResponse], error)`

**get** `/api/v1/beta/batch-processing/{job_id}/items`

List items in a batch job with optional status filtering.

Useful for finding failed items, viewing completed items,
or debugging processing issues.

### Parameters

- `jobID string`

- `query BetaBatchJobItemListParams`

  - `Limit param.Field[int64]`

    Maximum number of items to return

  - `Offset param.Field[int64]`

    Number of items to skip

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

  - `Status param.Field[BetaBatchJobItemListParamsStatus]`

    Filter items by status

    - `const BetaBatchJobItemListParamsStatusPending BetaBatchJobItemListParamsStatus = "pending"`

    - `const BetaBatchJobItemListParamsStatusProcessing BetaBatchJobItemListParamsStatus = "processing"`

    - `const BetaBatchJobItemListParamsStatusCompleted BetaBatchJobItemListParamsStatus = "completed"`

    - `const BetaBatchJobItemListParamsStatusFailed BetaBatchJobItemListParamsStatus = "failed"`

    - `const BetaBatchJobItemListParamsStatusSkipped BetaBatchJobItemListParamsStatus = "skipped"`

    - `const BetaBatchJobItemListParamsStatusCancelled BetaBatchJobItemListParamsStatus = "cancelled"`

### Returns

- `type BetaBatchJobItemListResponse struct{…}`

  Detailed information about an item in a batch job.

  - `ItemID string`

    ID of the item

  - `ItemName string`

    Name of the item

  - `Status BetaBatchJobItemListResponseStatus`

    Processing status of this item

    - `const BetaBatchJobItemListResponseStatusPending BetaBatchJobItemListResponseStatus = "pending"`

    - `const BetaBatchJobItemListResponseStatusProcessing BetaBatchJobItemListResponseStatus = "processing"`

    - `const BetaBatchJobItemListResponseStatusCompleted BetaBatchJobItemListResponseStatus = "completed"`

    - `const BetaBatchJobItemListResponseStatusFailed BetaBatchJobItemListResponseStatus = "failed"`

    - `const BetaBatchJobItemListResponseStatusSkipped BetaBatchJobItemListResponseStatus = "skipped"`

    - `const BetaBatchJobItemListResponseStatusCancelled BetaBatchJobItemListResponseStatus = "cancelled"`

  - `CompletedAt Time`

    When processing completed for this item

  - `EffectiveAt Time`

  - `ErrorMessage string`

    Error message for the latest job attempt, if any.

  - `JobID string`

    Job ID for the underlying processing job (links to parse/extract job results)

  - `JobRecordID string`

    The job record ID associated with this status, if any.

  - `SkipReason string`

    Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

  - `StartedAt Time`

    When processing started for this item

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Batch.JobItems.List(
    context.TODO(),
    "job_id",
    llamacloudprod.BetaBatchJobItemListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
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
