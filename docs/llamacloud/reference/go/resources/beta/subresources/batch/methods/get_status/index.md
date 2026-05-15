## Get Batch Job Status

`client.Beta.Batch.GetStatus(ctx, jobID, query) (*BetaBatchGetStatusResponse, error)`

**get** `/api/v1/beta/batch-processing/{job_id}`

Get detailed status of a batch processing job.

Returns current progress percentage, file counts (total,
processed, failed, skipped), and timestamps.

### Parameters

- `jobID string`

- `query BetaBatchGetStatusParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type BetaBatchGetStatusResponse struct{…}`

  Detailed status response for a batch processing job.

  - `Job BetaBatchGetStatusResponseJob`

    Response schema for a batch processing job.

    - `ID string`

      Unique identifier for the batch job

    - `JobType string`

      Type of processing operation (parse or classify)

      - `const BetaBatchGetStatusResponseJobJobTypeParse BetaBatchGetStatusResponseJobJobType = "parse"`

      - `const BetaBatchGetStatusResponseJobJobTypeExtract BetaBatchGetStatusResponseJobJobType = "extract"`

      - `const BetaBatchGetStatusResponseJobJobTypeClassify BetaBatchGetStatusResponseJobJobType = "classify"`

    - `ProjectID string`

      Project this job belongs to

    - `Status string`

      Current job status

      - `const BetaBatchGetStatusResponseJobStatusPending BetaBatchGetStatusResponseJobStatus = "pending"`

      - `const BetaBatchGetStatusResponseJobStatusRunning BetaBatchGetStatusResponseJobStatus = "running"`

      - `const BetaBatchGetStatusResponseJobStatusDispatched BetaBatchGetStatusResponseJobStatus = "dispatched"`

      - `const BetaBatchGetStatusResponseJobStatusCompleted BetaBatchGetStatusResponseJobStatus = "completed"`

      - `const BetaBatchGetStatusResponseJobStatusFailed BetaBatchGetStatusResponseJobStatus = "failed"`

      - `const BetaBatchGetStatusResponseJobStatusCancelled BetaBatchGetStatusResponseJobStatus = "cancelled"`

    - `TotalItems int64`

      Total number of items in the job

    - `CompletedAt Time`

      Timestamp when job completed

    - `CreatedAt Time`

      Creation datetime

    - `DirectoryID string`

      Directory being processed

    - `EffectiveAt Time`

    - `ErrorMessage string`

      Error message for the latest job attempt, if any.

    - `FailedItems int64`

      Number of items that failed processing

    - `JobRecordID string`

      The job record ID associated with this status, if any.

    - `ProcessedItems int64`

      Number of items processed so far

    - `SkippedItems int64`

      Number of items skipped (already processed or size limit)

    - `StartedAt Time`

      Timestamp when job processing started

    - `UpdatedAt Time`

      Update datetime

    - `WorkflowID string`

      Async job tracking ID

  - `ProgressPercentage float64`

    Percentage of items processed (0-100)

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
  response, err := client.Beta.Batch.GetStatus(
    context.TODO(),
    "job_id",
    llamacloudprod.BetaBatchGetStatusParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Job)
}
```

#### Response

```json
{
  "job": {
    "id": "bjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "job_type": "parse",
    "project_id": "proj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "status": "pending",
    "total_items": 0,
    "completed_at": "2019-12-27T18:11:19.117Z",
    "created_at": "2019-12-27T18:11:19.117Z",
    "directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "effective_at": "2019-12-27T18:11:19.117Z",
    "error_message": "error_message",
    "failed_items": 0,
    "job_record_id": "job_record_id",
    "processed_items": 0,
    "skipped_items": 0,
    "started_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "workflow_id": "workflow_id"
  },
  "progress_percentage": 0
}
```
