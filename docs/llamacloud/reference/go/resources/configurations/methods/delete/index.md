## Delete Configuration

`client.Configurations.Delete(ctx, configID, body) error`

**delete** `/api/v1/beta/configurations/{config_id}`

Delete a product configuration.

### Parameters

- `configID string`

- `body ConfigurationDeleteParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Example

```go
package main

import (
  "context"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Configurations.Delete(
    context.TODO(),
    "config_id",
    llamacloudprod.ConfigurationDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```
