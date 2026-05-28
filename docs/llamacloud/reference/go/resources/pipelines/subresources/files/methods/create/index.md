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
