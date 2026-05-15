# Agent Data

## Get Agent Data

`client.Beta.AgentData.Get(ctx, itemID, query) (*AgentData, error)`

**get** `/api/v1/beta/agent-data/{item_id}`

Get agent data by ID.

### Parameters

- `itemID string`

- `query BetaAgentDataGetParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

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
  agentData, err := client.Beta.AgentData.Get(
    context.TODO(),
    "item_id",
    llamacloudprod.BetaAgentDataGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentData.ID)
}
```

#### Response

```json
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
```

## Update Agent Data

`client.Beta.AgentData.Update(ctx, itemID, params) (*AgentData, error)`

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Parameters

- `itemID string`

- `params BetaAgentDataUpdateParams`

  - `Data param.Field[map[string, any]]`

    Body param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

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
  agentData, err := client.Beta.AgentData.Update(
    context.TODO(),
    "item_id",
    llamacloudprod.BetaAgentDataUpdateParams{
      Data: map[string]any{
      "foo": "bar",
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentData.ID)
}
```

#### Response

```json
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
```

## Delete Agent Data

`client.Beta.AgentData.Delete(ctx, itemID, body) (*BetaAgentDataDeleteResponse, error)`

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Parameters

- `itemID string`

- `body BetaAgentDataDeleteParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type BetaAgentDataDeleteResponse map[string, string]`

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
  agentData, err := client.Beta.AgentData.Delete(
    context.TODO(),
    "item_id",
    llamacloudprod.BetaAgentDataDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentData)
}
```

#### Response

```json
{
  "foo": "string"
}
```

## Create Agent Data

`client.Beta.AgentData.New(ctx, params) (*AgentData, error)`

**post** `/api/v1/beta/agent-data`

Create new agent data.

### Parameters

- `params BetaAgentDataNewParams`

  - `Data param.Field[map[string, any]]`

    Body param

  - `DeploymentName param.Field[string]`

    Body param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Collection param.Field[string]`

    Body param

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
  agentData, err := client.Beta.AgentData.New(context.TODO(), llamacloudprod.BetaAgentDataNewParams{
    Data: map[string]any{
    "foo": "bar",
    },
    DeploymentName: "deployment_name",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentData.ID)
}
```

#### Response

```json
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
```

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

## Domain Types

### Agent Data

- `type AgentData struct{…}`

  API Result for a single agent data item

  - `Data map[string, any]`

  - `DeploymentName string`

  - `ID string`

  - `Collection string`

  - `CreatedAt Time`

  - `ProjectID string`

  - `UpdatedAt Time`
