## Search Agent Data

`client.Beta.AgentData.Search(ctx, params) (*PaginatedCursorPost[AgentData], error)`

**post** `/api/v1/beta/agent-data/:search`

Search agent data with filtering, sorting, and pagination.

### Parameters

- `params BetaAgentDataSearchParams`

  - `DeploymentName param.Field[string]`

    Body param: The agent deployment's name to search within

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Collection param.Field[string]`

    Body param: The logical agent data collection to search within

  - `Filter param.Field[map[string, BetaAgentDataSearchParamsFilter]]`

    Body param: A filter object or expression that filters resources listed in the response.

    - `Eq BetaAgentDataSearchParamsFilterEqUnion`

      - `float64`

      - `string`

      - `Time`

    - `Excludes []BetaAgentDataSearchParamsFilterExcludeUnion`

      - `float64`

      - `string`

      - `Time`

    - `Gt BetaAgentDataSearchParamsFilterGtUnion`

      - `float64`

      - `string`

      - `Time`

    - `Gte BetaAgentDataSearchParamsFilterGteUnion`

      - `float64`

      - `string`

      - `Time`

    - `Includes []BetaAgentDataSearchParamsFilterIncludeUnion`

      - `float64`

      - `string`

      - `Time`

    - `Lt BetaAgentDataSearchParamsFilterLtUnion`

      - `float64`

      - `string`

      - `Time`

    - `Lte BetaAgentDataSearchParamsFilterLteUnion`

      - `float64`

      - `string`

      - `Time`

    - `Ne BetaAgentDataSearchParamsFilterNeUnion`

      - `float64`

      - `string`

      - `Time`

  - `IncludeTotal param.Field[bool]`

    Body param: Whether to include the total number of items in the response

  - `Offset param.Field[int64]`

    Body param: The offset to start from. If not provided, the first page is returned

  - `OrderBy param.Field[string]`

    Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `PageSize param.Field[int64]`

    Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

  - `PageToken param.Field[string]`

    Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `type AgentData struct{…}`

  API Result for a single agent data item

  - `Data map[string, any]`

  - `DeploymentName string`

  - `ID string`

  - `Collection string`

  - `CreatedAt Time`

  - `ProjectID string`

  - `UpdatedAt Time`

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
  page, err := client.Beta.AgentData.Search(context.TODO(), llamacloudprod.BetaAgentDataSearchParams{
    DeploymentName: "deployment_name",
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
      "data": {
        "foo": "bar"
      },
      "deployment_name": "deployment_name",
      "id": "id",
      "collection": "collection",
      "created_at": "2019-12-27T18:11:19.117Z",
      "project_id": "project_id",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
