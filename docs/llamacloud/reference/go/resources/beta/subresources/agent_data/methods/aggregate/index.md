## Aggregate Agent Data

`client.Beta.AgentData.Aggregate(ctx, params) (*PaginatedCursorPost[BetaAgentDataAggregateResponse], error)`

**post** `/api/v1/beta/agent-data/:aggregate`

Aggregate agent data with grouping and optional counting/first item retrieval.

### Parameters

- `params BetaAgentDataAggregateParams`

  - `DeploymentName param.Field[string]`

    Body param: The agent deployment's name to aggregate data for

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Collection param.Field[string]`

    Body param: The logical agent data collection to aggregate data for

  - `Count param.Field[bool]`

    Body param: Whether to count the number of items in each group

  - `Filter param.Field[map[string, BetaAgentDataAggregateParamsFilter]]`

    Body param: A filter object or expression that filters resources listed in the response.

    - `Eq BetaAgentDataAggregateParamsFilterEqUnion`

      - `float64`

      - `string`

      - `Time`

    - `Excludes []BetaAgentDataAggregateParamsFilterExcludeUnion`

      - `float64`

      - `string`

      - `Time`

    - `Gt BetaAgentDataAggregateParamsFilterGtUnion`

      - `float64`

      - `string`

      - `Time`

    - `Gte BetaAgentDataAggregateParamsFilterGteUnion`

      - `float64`

      - `string`

      - `Time`

    - `Includes []BetaAgentDataAggregateParamsFilterIncludeUnion`

      - `float64`

      - `string`

      - `Time`

    - `Lt BetaAgentDataAggregateParamsFilterLtUnion`

      - `float64`

      - `string`

      - `Time`

    - `Lte BetaAgentDataAggregateParamsFilterLteUnion`

      - `float64`

      - `string`

      - `Time`

    - `Ne BetaAgentDataAggregateParamsFilterNeUnion`

      - `float64`

      - `string`

      - `Time`

  - `First param.Field[bool]`

    Body param: Whether to return the first item in each group (Sorted by created_at)

  - `GroupBy param.Field[[]string]`

    Body param: The fields to group by. If empty, the entire dataset is grouped on. e.g. if left out, can be used for simple count operations

  - `Offset param.Field[int64]`

    Body param: The offset to start from. If not provided, the first page is returned

  - `OrderBy param.Field[string]`

    Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `PageSize param.Field[int64]`

    Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

  - `PageToken param.Field[string]`

    Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `type BetaAgentDataAggregateResponse struct{…}`

  API Result for a single group in the aggregate response

  - `GroupKey map[string, any]`

  - `Count int64`

  - `FirstItem map[string, any]`

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
  page, err := client.Beta.AgentData.Aggregate(context.TODO(), llamacloudprod.BetaAgentDataAggregateParams{
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
      "group_key": {
        "foo": "bar"
      },
      "count": 0,
      "first_item": {
        "foo": "bar"
      }
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
