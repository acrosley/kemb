## List Files

`client.Files.List(ctx, query) (*PaginatedCursor[FileListResponse], error)`

**get** `/api/v1/beta/files`

List files with optional filtering and pagination.

Filter by `file_name`, `file_ids`, or `external_file_id`.
Supports cursor-based pagination and custom ordering.

### Parameters

- `query FileListParams`

  - `Expand param.Field[[]string]`

    Fields to expand on each file.

  - `ExternalFileID param.Field[string]`

    Filter by external file ID.

  - `FileIDs param.Field[[]string]`

    Filter by specific file IDs.

  - `FileName param.Field[string]`

    Filter by file name (exact match).

  - `OrderBy param.Field[string]`

    A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

    The maximum number of items to return. Defaults to 50, maximum is 1000.

  - `PageToken param.Field[string]`

    A page token received from a previous list call. Provide this to retrieve the subsequent page.

  - `ProjectID param.Field[string]`

### Returns

- `type FileListResponse struct{…}`

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
  "context"
  "fmt"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Files.List(context.TODO(), llamacloudprod.FileListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "items": [
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
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
