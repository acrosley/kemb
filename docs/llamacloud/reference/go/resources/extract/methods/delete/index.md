## Delete Extract Job

`client.Extract.Delete(ctx, jobID, body) (*ExtractDeleteResponse, error)`

**delete** `/api/v2/extract/{job_id}`

Delete an extraction job and its results.

### Parameters

- `jobID string`

- `body ExtractDeleteParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type ExtractDeleteResponse interface{…}`

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
  extract, err := client.Extract.Delete(
    context.TODO(),
    "job_id",
    llamacloudprod.ExtractDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", extract)
}
```

#### Response

```json
{}
```
