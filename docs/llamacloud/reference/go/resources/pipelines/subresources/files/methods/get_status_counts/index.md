## Get Pipeline File Status Counts

`client.Pipelines.Files.GetStatusCounts(ctx, pipelineID, query) (*PipelineFileGetStatusCountsResponse, error)`

**get** `/api/v1/pipelines/{pipeline_id}/files/status-counts`

Get files for a pipeline.

### Parameters

- `pipelineID string`

- `query PipelineFileGetStatusCountsParams`

  - `DataSourceID param.Field[string]`

  - `OnlyManuallyUploaded param.Field[bool]`

### Returns

- `type PipelineFileGetStatusCountsResponse struct{…}`

  - `Counts map[string, int64]`

    The counts of files by status

  - `TotalCount int64`

    The total number of files

  - `DataSourceID string`

    The ID of the data source that the files belong to

  - `OnlyManuallyUploaded bool`

    Whether to only count manually uploaded files

  - `PipelineID string`

    The ID of the pipeline that the files belong to

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
  response, err := client.Pipelines.Files.GetStatusCounts(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineFileGetStatusCountsParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.DataSourceID)
}
```

#### Response

```json
{
  "counts": {
    "foo": 0
  },
  "total_count": 0,
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "only_manually_uploaded": true,
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```
