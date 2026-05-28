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
