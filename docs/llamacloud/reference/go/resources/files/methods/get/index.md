## Read File Content

`client.Files.Get(ctx, fileID, query) (*PresignedURL, error)`

**get** `/api/v1/beta/files/{file_id}/content`

Get a presigned URL to download the file content.

### Parameters

- `fileID string`

- `query FileGetParams`

  - `ExpiresAtSeconds param.Field[int64]`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type PresignedURL struct{…}`

  Schema for a presigned URL.

  - `ExpiresAt Time`

    The time at which the presigned URL expires

  - `URL string`

    A presigned URL for IO operations against a private file

  - `FormFields map[string, string]`

    Form fields for a presigned POST request

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
  presignedURL, err := client.Files.Get(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.FileGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", presignedURL.ExpiresAt)
}
```

#### Response

```json
{
  "expires_at": "2019-12-27T18:11:19.117Z",
  "url": "https://example.com",
  "form_fields": {
    "foo": "string"
  }
}
```
