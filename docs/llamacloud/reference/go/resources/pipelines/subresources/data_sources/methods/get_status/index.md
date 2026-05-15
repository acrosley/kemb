## Get Pipeline Data Source Status

`client.Pipelines.DataSources.GetStatus(ctx, dataSourceID, query) (*ManagedIngestionStatusResponse, error)`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status`

Get the status of a data source for a pipeline.

### Parameters

- `dataSourceID string`

- `query PipelineDataSourceGetStatusParams`

  - `PipelineID param.Field[string]`

### Returns

- `type ManagedIngestionStatusResponse struct{…}`

  - `Status ManagedIngestionStatusResponseStatus`

    Status of the ingestion.

    - `const ManagedIngestionStatusResponseStatusNotStarted ManagedIngestionStatusResponseStatus = "NOT_STARTED"`

    - `const ManagedIngestionStatusResponseStatusInProgress ManagedIngestionStatusResponseStatus = "IN_PROGRESS"`

    - `const ManagedIngestionStatusResponseStatusSuccess ManagedIngestionStatusResponseStatus = "SUCCESS"`

    - `const ManagedIngestionStatusResponseStatusError ManagedIngestionStatusResponseStatus = "ERROR"`

    - `const ManagedIngestionStatusResponseStatusPartialSuccess ManagedIngestionStatusResponseStatus = "PARTIAL_SUCCESS"`

    - `const ManagedIngestionStatusResponseStatusCancelled ManagedIngestionStatusResponseStatus = "CANCELLED"`

  - `DeploymentDate Time`

    Date of the deployment.

  - `EffectiveAt Time`

    When the status is effective

  - `Error []ManagedIngestionStatusResponseError`

    List of errors that occurred during ingestion.

    - `JobID string`

      ID of the job that failed.

    - `Message string`

      List of errors that occurred during ingestion.

    - `Step string`

      Name of the job that failed.

      - `const ManagedIngestionStatusResponseErrorStepManagedIngestion ManagedIngestionStatusResponseErrorStep = "MANAGED_INGESTION"`

      - `const ManagedIngestionStatusResponseErrorStepDataSource ManagedIngestionStatusResponseErrorStep = "DATA_SOURCE"`

      - `const ManagedIngestionStatusResponseErrorStepFileUpdater ManagedIngestionStatusResponseErrorStep = "FILE_UPDATER"`

      - `const ManagedIngestionStatusResponseErrorStepParse ManagedIngestionStatusResponseErrorStep = "PARSE"`

      - `const ManagedIngestionStatusResponseErrorStepTransform ManagedIngestionStatusResponseErrorStep = "TRANSFORM"`

      - `const ManagedIngestionStatusResponseErrorStepIngestion ManagedIngestionStatusResponseErrorStep = "INGESTION"`

      - `const ManagedIngestionStatusResponseErrorStepMetadataUpdate ManagedIngestionStatusResponseErrorStep = "METADATA_UPDATE"`

  - `JobID string`

    ID of the latest job.

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
  managedIngestionStatusResponse, err := client.Pipelines.DataSources.GetStatus(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDataSourceGetStatusParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", managedIngestionStatusResponse.JobID)
}
```

#### Response

```json
{
  "status": "NOT_STARTED",
  "deployment_date": "2019-12-27T18:11:19.117Z",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error": [
    {
      "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "message": "message",
      "step": "MANAGED_INGESTION"
    }
  ],
  "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```
