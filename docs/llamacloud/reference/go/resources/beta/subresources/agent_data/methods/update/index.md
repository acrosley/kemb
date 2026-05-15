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
