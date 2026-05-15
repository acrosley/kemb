# Files

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

## Get Pipeline File Status

`client.Pipelines.Files.GetStatus(ctx, fileID, query) (*ManagedIngestionStatusResponse, error)`

**get** `/api/v1/pipelines/{pipeline_id}/files/{file_id}/status`

Get status of a file for a pipeline.

### Parameters

- `fileID string`

- `query PipelineFileGetStatusParams`

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
  managedIngestionStatusResponse, err := client.Pipelines.Files.GetStatus(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineFileGetStatusParams{
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

## Add Files To Pipeline Api

`client.Pipelines.Files.New(ctx, pipelineID, body) (*[]PipelineFile, error)`

**put** `/api/v1/pipelines/{pipeline_id}/files`

Add files to a pipeline.

### Parameters

- `pipelineID string`

- `body PipelineFileNewParams`

  - `Body param.Field[[]PipelineFileNewParamsBody]`

    - `FileID string`

      The ID of the file

    - `CustomMetadata map[string, PipelineFileNewParamsBodyCustomMetadataUnion]`

      Custom metadata for the file

      - `type PipelineFileNewParamsBodyCustomMetadataMap map[string, any]`

      - `type PipelineFileNewParamsBodyCustomMetadataArray []any`

      - `string`

      - `float64`

      - `bool`

### Returns

- `type PipelineFileNewResponse []PipelineFile`

  - `ID string`

    Unique identifier for the pipeline file.

  - `PipelineID string`

    The ID of the pipeline that the file is associated with.

  - `ConfigHash map[string, PipelineFileConfigHashUnion]`

    Hashes for the configuration of the pipeline.

    - `type PipelineFileConfigHashMap map[string, any]`

    - `type PipelineFileConfigHashArray []any`

    - `string`

    - `float64`

    - `bool`

  - `CreatedAt Time`

    When the pipeline file was created.

  - `CustomMetadata map[string, PipelineFileCustomMetadataUnion]`

    Custom metadata for the file.

    - `type PipelineFileCustomMetadataMap map[string, any]`

    - `type PipelineFileCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `DataSourceID string`

    The ID of the data source that the file belongs to.

  - `ExternalFileID string`

    The ID of the file in the external system.

  - `FileID string`

    The ID of the file.

  - `FileSize int64`

    Size of the file in bytes.

  - `FileType string`

    File type (e.g. pdf, docx, etc.).

  - `IndexedPageCount int64`

    The number of pages that have been indexed for this file.

  - `LastModifiedAt Time`

    The last modified time of the file.

  - `Name string`

    Name of the file.

  - `PermissionInfo map[string, PipelineFilePermissionInfoUnion]`

    Permission information for the file.

    - `type PipelineFilePermissionInfoMap map[string, any]`

    - `type PipelineFilePermissionInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `ProjectID string`

    The ID of the project that the file belongs to.

  - `ResourceInfo map[string, PipelineFileResourceInfoUnion]`

    Resource information for the file.

    - `type PipelineFileResourceInfoMap map[string, any]`

    - `type PipelineFileResourceInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Status PipelineFileStatus`

    Status of the pipeline file.

    - `const PipelineFileStatusNotStarted PipelineFileStatus = "NOT_STARTED"`

    - `const PipelineFileStatusInProgress PipelineFileStatus = "IN_PROGRESS"`

    - `const PipelineFileStatusSuccess PipelineFileStatus = "SUCCESS"`

    - `const PipelineFileStatusError PipelineFileStatus = "ERROR"`

    - `const PipelineFileStatusCancelled PipelineFileStatus = "CANCELLED"`

  - `StatusUpdatedAt Time`

    The last time the status was updated.

  - `UpdatedAt Time`

    When the pipeline file was last updated.

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
  pipelineFiles, err := client.Pipelines.Files.New(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineFileNewParams{
      Body: []llamacloudprod.PipelineFileNewParamsBody{llamacloudprod.PipelineFileNewParamsBody{
        FileID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", pipelineFiles)
}
```

#### Response

```json
[
  {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "config_hash": {
      "foo": {
        "foo": "bar"
      }
    },
    "created_at": "2019-12-27T18:11:19.117Z",
    "custom_metadata": {
      "foo": {
        "foo": "bar"
      }
    },
    "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "external_file_id": "external_file_id",
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "file_size": 0,
    "file_type": "file_type",
    "indexed_page_count": 0,
    "last_modified_at": "2019-12-27T18:11:19.117Z",
    "name": "name",
    "permission_info": {
      "foo": {
        "foo": "bar"
      }
    },
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "resource_info": {
      "foo": {
        "foo": "bar"
      }
    },
    "status": "NOT_STARTED",
    "status_updated_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  }
]
```

## Update Pipeline File

`client.Pipelines.Files.Update(ctx, fileID, params) (*PipelineFile, error)`

**put** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Update a file for a pipeline.

### Parameters

- `fileID string`

- `params PipelineFileUpdateParams`

  - `PipelineID param.Field[string]`

    Path param

  - `CustomMetadata param.Field[map[string, PipelineFileUpdateParamsCustomMetadataUnion]]`

    Body param: Custom metadata for the file

    - `type PipelineFileUpdateParamsCustomMetadataMap map[string, any]`

    - `type PipelineFileUpdateParamsCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

### Returns

- `type PipelineFile struct{…}`

  A file associated with a pipeline.

  - `ID string`

    Unique identifier for the pipeline file.

  - `PipelineID string`

    The ID of the pipeline that the file is associated with.

  - `ConfigHash map[string, PipelineFileConfigHashUnion]`

    Hashes for the configuration of the pipeline.

    - `type PipelineFileConfigHashMap map[string, any]`

    - `type PipelineFileConfigHashArray []any`

    - `string`

    - `float64`

    - `bool`

  - `CreatedAt Time`

    When the pipeline file was created.

  - `CustomMetadata map[string, PipelineFileCustomMetadataUnion]`

    Custom metadata for the file.

    - `type PipelineFileCustomMetadataMap map[string, any]`

    - `type PipelineFileCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `DataSourceID string`

    The ID of the data source that the file belongs to.

  - `ExternalFileID string`

    The ID of the file in the external system.

  - `FileID string`

    The ID of the file.

  - `FileSize int64`

    Size of the file in bytes.

  - `FileType string`

    File type (e.g. pdf, docx, etc.).

  - `IndexedPageCount int64`

    The number of pages that have been indexed for this file.

  - `LastModifiedAt Time`

    The last modified time of the file.

  - `Name string`

    Name of the file.

  - `PermissionInfo map[string, PipelineFilePermissionInfoUnion]`

    Permission information for the file.

    - `type PipelineFilePermissionInfoMap map[string, any]`

    - `type PipelineFilePermissionInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `ProjectID string`

    The ID of the project that the file belongs to.

  - `ResourceInfo map[string, PipelineFileResourceInfoUnion]`

    Resource information for the file.

    - `type PipelineFileResourceInfoMap map[string, any]`

    - `type PipelineFileResourceInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Status PipelineFileStatus`

    Status of the pipeline file.

    - `const PipelineFileStatusNotStarted PipelineFileStatus = "NOT_STARTED"`

    - `const PipelineFileStatusInProgress PipelineFileStatus = "IN_PROGRESS"`

    - `const PipelineFileStatusSuccess PipelineFileStatus = "SUCCESS"`

    - `const PipelineFileStatusError PipelineFileStatus = "ERROR"`

    - `const PipelineFileStatusCancelled PipelineFileStatus = "CANCELLED"`

  - `StatusUpdatedAt Time`

    The last time the status was updated.

  - `UpdatedAt Time`

    When the pipeline file was last updated.

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
  pipelineFile, err := client.Pipelines.Files.Update(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineFileUpdateParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", pipelineFile.ID)
}
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "foo": {
      "foo": "bar"
    }
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "custom_metadata": {
    "foo": {
      "foo": "bar"
    }
  },
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "external_file_id": "external_file_id",
  "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "file_size": 0,
  "file_type": "file_type",
  "indexed_page_count": 0,
  "last_modified_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "permission_info": {
    "foo": {
      "foo": "bar"
    }
  },
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "resource_info": {
    "foo": {
      "foo": "bar"
    }
  },
  "status": "NOT_STARTED",
  "status_updated_at": "2019-12-27T18:11:19.117Z",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Pipeline File

`client.Pipelines.Files.Delete(ctx, fileID, body) error`

**delete** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Delete a file from a pipeline.

### Parameters

- `fileID string`

- `body PipelineFileDeleteParams`

  - `PipelineID param.Field[string]`

### Example

```go
package main

import (
  "context"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Pipelines.Files.Delete(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineFileDeleteParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

## List Pipeline Files2

`client.Pipelines.Files.List(ctx, pipelineID, query) (*PaginatedPipelineFiles[PipelineFile], error)`

**get** `/api/v1/pipelines/{pipeline_id}/files2`

List files for a pipeline with optional filtering, sorting, and pagination.

### Parameters

- `pipelineID string`

- `query PipelineFileListParams`

  - `DataSourceID param.Field[string]`

  - `FileNameContains param.Field[string]`

  - `Limit param.Field[int64]`

  - `Offset param.Field[int64]`

  - `OnlyManuallyUploaded param.Field[bool]`

  - `OrderBy param.Field[string]`

  - `Statuses param.Field[[]string]`

    Filter by file statuses

    - `const PipelineFileListParamsStatusNotStarted PipelineFileListParamsStatus = "NOT_STARTED"`

    - `const PipelineFileListParamsStatusInProgress PipelineFileListParamsStatus = "IN_PROGRESS"`

    - `const PipelineFileListParamsStatusSuccess PipelineFileListParamsStatus = "SUCCESS"`

    - `const PipelineFileListParamsStatusError PipelineFileListParamsStatus = "ERROR"`

    - `const PipelineFileListParamsStatusCancelled PipelineFileListParamsStatus = "CANCELLED"`

### Returns

- `type PipelineFile struct{…}`

  A file associated with a pipeline.

  - `ID string`

    Unique identifier for the pipeline file.

  - `PipelineID string`

    The ID of the pipeline that the file is associated with.

  - `ConfigHash map[string, PipelineFileConfigHashUnion]`

    Hashes for the configuration of the pipeline.

    - `type PipelineFileConfigHashMap map[string, any]`

    - `type PipelineFileConfigHashArray []any`

    - `string`

    - `float64`

    - `bool`

  - `CreatedAt Time`

    When the pipeline file was created.

  - `CustomMetadata map[string, PipelineFileCustomMetadataUnion]`

    Custom metadata for the file.

    - `type PipelineFileCustomMetadataMap map[string, any]`

    - `type PipelineFileCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `DataSourceID string`

    The ID of the data source that the file belongs to.

  - `ExternalFileID string`

    The ID of the file in the external system.

  - `FileID string`

    The ID of the file.

  - `FileSize int64`

    Size of the file in bytes.

  - `FileType string`

    File type (e.g. pdf, docx, etc.).

  - `IndexedPageCount int64`

    The number of pages that have been indexed for this file.

  - `LastModifiedAt Time`

    The last modified time of the file.

  - `Name string`

    Name of the file.

  - `PermissionInfo map[string, PipelineFilePermissionInfoUnion]`

    Permission information for the file.

    - `type PipelineFilePermissionInfoMap map[string, any]`

    - `type PipelineFilePermissionInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `ProjectID string`

    The ID of the project that the file belongs to.

  - `ResourceInfo map[string, PipelineFileResourceInfoUnion]`

    Resource information for the file.

    - `type PipelineFileResourceInfoMap map[string, any]`

    - `type PipelineFileResourceInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Status PipelineFileStatus`

    Status of the pipeline file.

    - `const PipelineFileStatusNotStarted PipelineFileStatus = "NOT_STARTED"`

    - `const PipelineFileStatusInProgress PipelineFileStatus = "IN_PROGRESS"`

    - `const PipelineFileStatusSuccess PipelineFileStatus = "SUCCESS"`

    - `const PipelineFileStatusError PipelineFileStatus = "ERROR"`

    - `const PipelineFileStatusCancelled PipelineFileStatus = "CANCELLED"`

  - `StatusUpdatedAt Time`

    The last time the status was updated.

  - `UpdatedAt Time`

    When the pipeline file was last updated.

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
  page, err := client.Pipelines.Files.List(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineFileListParams{

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
  "files": [
    {
      "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "config_hash": {
        "foo": {
          "foo": "bar"
        }
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "custom_metadata": {
        "foo": {
          "foo": "bar"
        }
      },
      "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "external_file_id": "external_file_id",
      "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "file_size": 0,
      "file_type": "file_type",
      "indexed_page_count": 0,
      "last_modified_at": "2019-12-27T18:11:19.117Z",
      "name": "name",
      "permission_info": {
        "foo": {
          "foo": "bar"
        }
      },
      "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "resource_info": {
        "foo": {
          "foo": "bar"
        }
      },
      "status": "NOT_STARTED",
      "status_updated_at": "2019-12-27T18:11:19.117Z",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "limit": 0,
  "offset": 0,
  "total_count": 0
}
```

## Domain Types

### Pipeline File

- `type PipelineFile struct{…}`

  A file associated with a pipeline.

  - `ID string`

    Unique identifier for the pipeline file.

  - `PipelineID string`

    The ID of the pipeline that the file is associated with.

  - `ConfigHash map[string, PipelineFileConfigHashUnion]`

    Hashes for the configuration of the pipeline.

    - `type PipelineFileConfigHashMap map[string, any]`

    - `type PipelineFileConfigHashArray []any`

    - `string`

    - `float64`

    - `bool`

  - `CreatedAt Time`

    When the pipeline file was created.

  - `CustomMetadata map[string, PipelineFileCustomMetadataUnion]`

    Custom metadata for the file.

    - `type PipelineFileCustomMetadataMap map[string, any]`

    - `type PipelineFileCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `DataSourceID string`

    The ID of the data source that the file belongs to.

  - `ExternalFileID string`

    The ID of the file in the external system.

  - `FileID string`

    The ID of the file.

  - `FileSize int64`

    Size of the file in bytes.

  - `FileType string`

    File type (e.g. pdf, docx, etc.).

  - `IndexedPageCount int64`

    The number of pages that have been indexed for this file.

  - `LastModifiedAt Time`

    The last modified time of the file.

  - `Name string`

    Name of the file.

  - `PermissionInfo map[string, PipelineFilePermissionInfoUnion]`

    Permission information for the file.

    - `type PipelineFilePermissionInfoMap map[string, any]`

    - `type PipelineFilePermissionInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `ProjectID string`

    The ID of the project that the file belongs to.

  - `ResourceInfo map[string, PipelineFileResourceInfoUnion]`

    Resource information for the file.

    - `type PipelineFileResourceInfoMap map[string, any]`

    - `type PipelineFileResourceInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Status PipelineFileStatus`

    Status of the pipeline file.

    - `const PipelineFileStatusNotStarted PipelineFileStatus = "NOT_STARTED"`

    - `const PipelineFileStatusInProgress PipelineFileStatus = "IN_PROGRESS"`

    - `const PipelineFileStatusSuccess PipelineFileStatus = "SUCCESS"`

    - `const PipelineFileStatusError PipelineFileStatus = "ERROR"`

    - `const PipelineFileStatusCancelled PipelineFileStatus = "CANCELLED"`

  - `StatusUpdatedAt Time`

    The last time the status was updated.

  - `UpdatedAt Time`

    When the pipeline file was last updated.
