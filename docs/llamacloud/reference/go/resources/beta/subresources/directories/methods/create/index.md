## Create Directory

`client.Beta.Directories.New(ctx, params) (*BetaDirectoryNewResponse, error)`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `params BetaDirectoryNewParams`

  - `Name param.Field[string]`

    Body param: Human-readable name for the directory.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Description param.Field[string]`

    Body param: Optional description shown to users.

### Returns

- `type BetaDirectoryNewResponse struct{…}`

  API response schema for a directory.

  - `ID string`

    Unique identifier for the directory.

  - `Name string`

    Human-readable name for the directory.

  - `ProjectID string`

    Project the directory belongs to.

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `Description string`

    Optional description shown to users.

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
  directory, err := client.Beta.Directories.New(context.TODO(), llamacloudprod.BetaDirectoryNewParams{
    Name: "x",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", directory.ID)
}
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
