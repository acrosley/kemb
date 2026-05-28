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
