## List Batch Jobs

`client.Beta.Batch.List(ctx, query) (*PaginatedBatchItems[BetaBatchListResponse], error)`

**get** `/api/v1/beta/batch-processing`

List batch processing jobs with optional filtering.

Filter by `directory_id`, `job_type`, or `status`. Results
are paginated with configurable `limit` and `offset`.

### Parameters

- `query BetaBatchListParams`

  - `DirectoryID param.Field[string]`

    Filter by directory ID

  - `JobType param.Field[BetaBatchListParamsJobType]`

    Filter by job type (PARSE, EXTRACT, CLASSIFY)

    - `const BetaBatchListParamsJobTypeParse BetaBatchListParamsJobType = "parse"`

    - `const BetaBatchListParamsJobTypeExtract BetaBatchListParamsJobType = "extract"`

    - `const BetaBatchListParamsJobTypeClassify BetaBatchListParamsJobType = "classify"`

  - `Limit param.Field[int64]`

    Maximum number of jobs to return

  - `Offset param.Field[int64]`

    Number of jobs to skip for pagination

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

  - `Status param.Field[BetaBatchListParamsStatus]`

    Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

    - `const BetaBatchListParamsStatusPending BetaBatchListParamsStatus = "pending"`

    - `const BetaBatchListParamsStatusRunning BetaBatchListParamsStatus = "running"`

    - `const BetaBatchListParamsStatusDispatched BetaBatchListParamsStatus = "dispatched"`

    - `const BetaBatchListParamsStatusCompleted BetaBatchListParamsStatus = "completed"`

    - `const BetaBatchListParamsStatusFailed BetaBatchListParamsStatus = "failed"`

    - `const BetaBatchListParamsStatusCancelled BetaBatchListParamsStatus = "cancelled"`

### Returns

- `type BetaBatchListResponse struct{…}`

  Response schema for a batch processing job.

  - `ID string`

    Unique identifier for the batch job

  - `JobType BetaBatchListResponseJobType`

    Type of processing operation (parse or classify)

    - `const BetaBatchListResponseJobTypeParse BetaBatchListResponseJobType = "parse"`

    - `const BetaBatchListResponseJobTypeExtract BetaBatchListResponseJobType = "extract"`

    - `const BetaBatchListResponseJobTypeClassify BetaBatchListResponseJobType = "classify"`

  - `ProjectID string`

    Project this job belongs to

  - `Status BetaBatchListResponseStatus`

    Current job status

    - `const BetaBatchListResponseStatusPending BetaBatchListResponseStatus = "pending"`

    - `const BetaBatchListResponseStatusRunning BetaBatchListResponseStatus = "running"`

    - `const BetaBatchListResponseStatusDispatched BetaBatchListResponseStatus = "dispatched"`

    - `const BetaBatchListResponseStatusCompleted BetaBatchListResponseStatus = "completed"`

    - `const BetaBatchListResponseStatusFailed BetaBatchListResponseStatus = "failed"`

    - `const BetaBatchListResponseStatusCancelled BetaBatchListResponseStatus = "cancelled"`

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
  page, err := client.Beta.Batch.List(context.TODO(), llamacloudprod.BetaBatchListParams{

  })
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
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
