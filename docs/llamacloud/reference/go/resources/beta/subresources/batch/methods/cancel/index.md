## Cancel Batch Job

`client.Beta.Batch.Cancel(ctx, jobID, params) (*BetaBatchCancelResponse, error)`

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Parameters

- `jobID string`

- `params BetaBatchCancelParams`

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Reason param.Field[string]`

    Body param: Optional reason for cancelling the job

  - `TemporalNamespace param.Field[string]`

    Header param

### Returns

- `type BetaBatchCancelResponse struct{…}`

  Response after cancelling a batch job.

  - `JobID string`

    ID of the cancelled job

  - `Message string`

    Confirmation message

  - `ProcessedItems int64`

    Number of items processed before cancellation

  - `Status BetaBatchCancelResponseStatus`

    New status (should be 'cancelled')

    - `const BetaBatchCancelResponseStatusPending BetaBatchCancelResponseStatus = "pending"`

    - `const BetaBatchCancelResponseStatusRunning BetaBatchCancelResponseStatus = "running"`

    - `const BetaBatchCancelResponseStatusDispatched BetaBatchCancelResponseStatus = "dispatched"`

    - `const BetaBatchCancelResponseStatusCompleted BetaBatchCancelResponseStatus = "completed"`

    - `const BetaBatchCancelResponseStatusFailed BetaBatchCancelResponseStatus = "failed"`

    - `const BetaBatchCancelResponseStatusCancelled BetaBatchCancelResponseStatus = "cancelled"`

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
  response, err := client.Beta.Batch.Cancel(
    context.TODO(),
    "job_id",
    llamacloudprod.BetaBatchCancelParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.JobID)
}
```

#### Response

```json
{
  "job_id": "job_id",
  "message": "message",
  "processed_items": 0,
  "status": "pending"
}
```
