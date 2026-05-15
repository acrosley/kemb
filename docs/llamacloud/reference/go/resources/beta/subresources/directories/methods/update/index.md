## Update Directory

`client.Beta.Directories.Update(ctx, directoryID, params) (*BetaDirectoryUpdateResponse, error)`

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Parameters

- `directoryID string`

- `params BetaDirectoryUpdateParams`

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Description param.Field[string]`

    Body param: Updated description for the directory.

  - `Name param.Field[string]`

    Body param: Updated name for the directory.

### Returns

- `type BetaDirectoryUpdateResponse struct{…}`

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
  directory, err := client.Beta.Directories.Update(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryUpdateParams{

    },
  )
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
