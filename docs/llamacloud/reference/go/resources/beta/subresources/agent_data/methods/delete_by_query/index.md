## Delete Agent Data By Query

`client.Beta.AgentData.DeleteByQuery(ctx, params) (*BetaAgentDataDeleteByQueryResponse, error)`

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Parameters

- `params BetaAgentDataDeleteByQueryParams`

  - `DeploymentName param.Field[string]`

    Body param: The agent deployment's name to delete data for

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Collection param.Field[string]`

    Body param: The logical agent data collection to delete from

  - `Filter param.Field[map[string, BetaAgentDataDeleteByQueryParamsFilter]]`

    Body param: Optional filters to select which items to delete

    - `Eq BetaAgentDataDeleteByQueryParamsFilterEqUnion`

      - `float64`

      - `string`

      - `Time`

    - `Excludes []BetaAgentDataDeleteByQueryParamsFilterExcludeUnion`

      - `float64`

      - `string`

      - `Time`

    - `Gt BetaAgentDataDeleteByQueryParamsFilterGtUnion`

      - `float64`

      - `string`

      - `Time`

    - `Gte BetaAgentDataDeleteByQueryParamsFilterGteUnion`

      - `float64`

      - `string`

      - `Time`

    - `Includes []BetaAgentDataDeleteByQueryParamsFilterIncludeUnion`

      - `float64`

      - `string`

      - `Time`

    - `Lt BetaAgentDataDeleteByQueryParamsFilterLtUnion`

      - `float64`

      - `string`

      - `Time`

    - `Lte BetaAgentDataDeleteByQueryParamsFilterLteUnion`

      - `float64`

      - `string`

      - `Time`

    - `Ne BetaAgentDataDeleteByQueryParamsFilterNeUnion`

      - `float64`

      - `string`

      - `Time`

### Returns

- `type BetaAgentDataDeleteByQueryResponse struct{…}`

  API response for bulk delete operation

  - `DeletedCount int64`

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
  response, err := client.Beta.AgentData.DeleteByQuery(context.TODO(), llamacloudprod.BetaAgentDataDeleteByQueryParams{
    DeploymentName: "deployment_name",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.DeletedCount)
}
```

#### Response

```json
{
  "deleted_count": 0
}
```
