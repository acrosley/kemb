## Delete Directory File

`client.Beta.Directories.Files.Delete(ctx, directoryFileID, params) error`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID string`

- `params BetaDirectoryFileDeleteParams`

  - `DirectoryID param.Field[string]`

    Path param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

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
  err := client.Beta.Directories.Files.Delete(
    context.TODO(),
    "directory_file_id",
    llamacloudprod.BetaDirectoryFileDeleteParams{
      DirectoryID: "directory_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```
