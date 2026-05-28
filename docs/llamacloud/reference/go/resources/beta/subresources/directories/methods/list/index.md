## List Directories

`client.Beta.Directories.List(ctx, query) (*PaginatedCursor[BetaDirectoryListResponse], error)`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `query BetaDirectoryListParams`

  - `IncludeDeleted param.Field[bool]`

  - `Name param.Field[string]`

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

  - `PageToken param.Field[string]`

  - `ProjectID param.Field[string]`

  - `Type param.Field[BetaDirectoryListParamsType]`

    - `const BetaDirectoryListParamsTypeUser BetaDirectoryListParamsType = "user"`

    - `const BetaDirectoryListParamsTypeIndex BetaDirectoryListParamsType = "index"`

### Returns

- `type BetaDirectoryListResponse struct{…}`

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
  page, err := client.Beta.Directories.List(context.TODO(), llamacloudprod.BetaDirectoryListParams{

  })
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
      "name": "x",
      "project_id": "project_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "deleted_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
