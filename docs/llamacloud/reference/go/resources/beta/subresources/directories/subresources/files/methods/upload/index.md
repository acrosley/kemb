## Upload File To Directory

`client.Beta.Directories.Files.Upload(ctx, directoryID, params) (*BetaDirectoryFileUploadResponse, error)`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `directoryID string`

- `params BetaDirectoryFileUploadParams`

  - `UploadFile param.Field[Reader]`

    Body param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `DisplayName param.Field[string]`

    Body param

  - `ExternalFileID param.Field[string]`

    Body param

  - `Metadata param.Field[string]`

    Body param: User metadata as a JSON object string.

  - `UniqueID param.Field[string]`

    Body param

### Returns

- `type BetaDirectoryFileUploadResponse struct{…}`

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

  - `Metadata map[string, BetaDirectoryFileUploadResponseMetadataUnion]`

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
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  response, err := client.Beta.Directories.Files.Upload(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryFileUploadParams{
      UploadFile: io.Reader(bytes.NewBuffer([]byte("Example data"))),
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
