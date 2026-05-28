## List Directory Files

`client.Beta.Directories.Files.List(ctx, directoryID, query) (*PaginatedCursor[BetaDirectoryFileListResponse], error)`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `directoryID string`

- `query BetaDirectoryFileListParams`

  - `DisplayName param.Field[string]`

  - `DisplayNameContains param.Field[string]`

  - `Expand param.Field[[]string]`

    Fields to expand on each directory file.

  - `FileID param.Field[string]`

  - `IncludeDeleted param.Field[bool]`

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

  - `PageToken param.Field[string]`

  - `ProjectID param.Field[string]`

  - `UniqueID param.Field[string]`

  - `UpdatedAtOnOrAfter param.Field[Time]`

    Include items updated at or after this timestamp (inclusive)

  - `UpdatedAtOnOrBefore param.Field[Time]`

    Include items updated at or before this timestamp (inclusive)

### Returns

- `type BetaDirectoryFileListResponse struct{…}`

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

  - `Metadata map[string, BetaDirectoryFileListResponseMetadataUnion]`

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
  page, err := client.Beta.Directories.Files.List(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryFileListParams{

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
  "items": [
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
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
