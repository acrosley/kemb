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
