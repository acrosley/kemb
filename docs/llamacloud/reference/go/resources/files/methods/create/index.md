## Upload File

`client.Files.New(ctx, params) (*FileNewResponse, error)`

**post** `/api/v1/beta/files`

Upload a file using multipart/form-data.

Set `purpose` to indicate how the file will be used:
`user_data`, `parse`, `extract`, `classify`, `split`,
`sheet`, or `agent_app`.

Returns the created file metadata including its ID for use
in subsequent parse, extract, or classify operations.

### Parameters

- `params FileNewParams`

  - `File param.Field[Reader]`

    Body param: The file to upload

  - `Purpose param.Field[string]`

    Body param: The intended purpose of the file. Valid values: 'user_data', 'parse', 'extract', 'split', 'classify', 'sheet', 'agent_app'. This determines the storage and retention policy for the file.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `ExternalFileID param.Field[string]`

    Body param: The ID of the file in the external system

### Returns

- `type FileNewResponse struct{…}`

  An uploaded file.

  - `ID string`

    Unique file identifier

  - `Name string`

    File name including extension

  - `ProjectID string`

    Project this file belongs to

  - `DownloadURL PresignedURL`

    Schema for a presigned URL.

    - `ExpiresAt Time`

      The time at which the presigned URL expires

    - `URL string`

      A presigned URL for IO operations against a private file

    - `FormFields map[string, string]`

      Form fields for a presigned POST request

  - `ExpiresAt Time`

    When the file expires and may be automatically removed. Null means no expiration.

  - `ExternalFileID string`

    Optional ID for correlating with an external system

  - `FileType string`

    File extension (pdf, docx, png, etc.)

  - `LastModifiedAt Time`

    When the file was last modified (ISO 8601)

  - `Purpose string`

    How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

### Example

```go
package main

import (
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  file, err := client.Files.New(context.TODO(), llamacloudprod.FileNewParams{
    File: io.Reader(bytes.NewBuffer([]byte("Example data"))),
    Purpose: "purpose",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", file.ID)
}
```

#### Response

```json
{
  "id": "dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "name": "invoice.pdf",
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "expires_at": "2019-12-27T18:11:19.117Z",
  "external_file_id": "ext-12345",
  "file_type": "pdf",
  "last_modified_at": "2019-12-27T18:11:19.117Z",
  "purpose": "parse"
}
```
