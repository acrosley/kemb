## Delete File

`client.Files.Delete(ctx, fileID, body) error`

**delete** `/api/v1/beta/files/{file_id}`

Delete a file from the project.

### Parameters

- `fileID string`

- `body FileDeleteParams`

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
  err := client.Files.Delete(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.FileDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```
