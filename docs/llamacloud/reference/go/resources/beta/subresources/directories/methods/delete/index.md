## Delete Directory

`client.Beta.Directories.Delete(ctx, directoryID, body) error`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `directoryID string`

- `body BetaDirectoryDeleteParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

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
  err := client.Beta.Directories.Delete(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```
