## Update Directory File

`client.Beta.Directories.Files.Update(ctx, directoryFileID, params) (*BetaDirectoryFileUpdateResponse, error)`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID string`

- `params BetaDirectoryFileUpdateParams`

  - `PathDirectoryID param.Field[string]`

    Path param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `PathDirectoryID param.Field[string]`

    Path param

  - `DisplayName param.Field[string]`

    Body param: Updated display name.

  - `Metadata param.Field[map[string, BetaDirectoryFileUpdateParamsMetadataUnion]]`

    Body param: User-defined metadata key-value pairs. Replaces the user metadata layer.

    - `string`

    - `float64`

    - `bool`

  - `UniqueID param.Field[string]`

    Body param: Updated unique identifier.

### Returns

- `type BetaDirectoryFileUpdateResponse struct{…}`

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

  - `Metadata map[string, BetaDirectoryFileUpdateResponseMetadataUnion]`

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
  file, err := client.Beta.Directories.Files.Update(
    context.TODO(),
    "directory_file_id",
    llamacloudprod.BetaDirectoryFileUpdateParams{
      PathDirectoryID: "directory_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", file.ID)
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
