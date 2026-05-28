## Add Directory File

`client.Beta.Directories.Files.Add(ctx, directoryID, params) (*BetaDirectoryFileAddResponse, error)`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `directoryID string`

- `params BetaDirectoryFileAddParams`

  - `FileID param.Field[string]`

    Body param: File ID for the storage location (required).

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `DisplayName param.Field[string]`

    Body param: Display name for the file. If not provided, will use the file's name.

  - `Metadata param.Field[map[string, BetaDirectoryFileAddParamsMetadataUnion]]`

    Body param: User-defined metadata key-value pairs to associate with the file.

    - `string`

    - `float64`

    - `bool`

  - `UniqueID param.Field[string]`

    Body param: Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `type BetaDirectoryFileAddResponse struct{…}`

  API response schema for a directory file.

  - `ID string`

    Unique identifier for the directory file.

  - `DirectoryID string`

    Directory the file belongs to.

  - `DisplayName string`

    Display name for the file.

  - `ProjectID string`

    Project the directory file belongs to.

  - `UniqueID string`

    Unique identifier for the file in the directory

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Soft delete marker when the file is removed upstream or by user action.

  - `DownloadURL PresignedURL`

    Schema for a presigned URL.

    - `ExpiresAt Time`

      The time at which the presigned URL expires

    - `URL string`

      A presigned URL for IO operations against a private file

    - `FormFields map[string, string]`

      Form fields for a presigned POST request

  - `FileID string`

    File ID for the storage location.

  - `Metadata map[string, BetaDirectoryFileAddResponseMetadataUnion]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

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
  response, err := client.Beta.Directories.Files.Add(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryFileAddParams{
      FileID: "file_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.ID)
}
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
