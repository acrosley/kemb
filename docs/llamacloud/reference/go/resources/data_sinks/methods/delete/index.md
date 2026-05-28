## Delete Data Sink

`client.DataSinks.Delete(ctx, dataSinkID) error`

**delete** `/api/v1/data-sinks/{data_sink_id}`

Delete a data sink by ID.

### Parameters

- `dataSinkID string`

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
  err := client.DataSinks.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
  if err != nil {
    panic(err.Error())
  }
}
```
