## Delete Retriever

`client.Retrievers.Delete(ctx, retrieverID, body) error`

**delete** `/api/v1/retrievers/{retriever_id}`

Delete a Retriever by ID.

### Parameters

- `retrieverID string`

- `body RetrieverDeleteParams`

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
  err := client.Retrievers.Delete(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.RetrieverDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```
