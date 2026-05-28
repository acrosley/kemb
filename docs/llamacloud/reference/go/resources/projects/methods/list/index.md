## List Projects

`client.Projects.List(ctx, query) (*[]Project, error)`

**get** `/api/v1/projects`

List projects or get one by name

### Parameters

- `query ProjectListParams`

  - `OrganizationID param.Field[string]`

  - `ProjectName param.Field[string]`

### Returns

- `type ProjectListResponse []Project`

  - `ID string`

    Unique identifier

  - `Name string`

  - `OrganizationID string`

    The Organization ID the project is under.

  - `CreatedAt Time`

    Creation datetime

  - `IsDefault bool`

    Whether this project is the default project for the user.

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
  projects, err := client.Projects.List(context.TODO(), llamacloudprod.ProjectListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", projects)
}
```

#### Response

```json
[
  {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "name": "x",
    "organization_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "is_default": true,
    "updated_at": "2019-12-27T18:11:19.117Z"
  }
]
```
