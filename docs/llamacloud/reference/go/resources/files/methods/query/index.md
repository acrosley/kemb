## Query Files

`client.Files.Query(ctx, params) (*FileQueryResponse, error)`

**post** `/api/v1/beta/files/query`

Query files with flexible filtering and pagination.

**Deprecated**: Use GET /files instead for listing files with query parameters.

Args:
request: The query request with filters and pagination
project: Validated project from dependency

Returns:
Paginated response with files

### Parameters

- `params FileQueryParams`

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Filter param.Field[FileQueryParamsFilter]`

    Body param: Filter parameters for file queries.

    - `DataSourceID string`

      Filter by data source ID

    - `ExternalFileID string`

      Filter by external file ID

    - `FileIDs []string`

      Filter by specific file IDs

    - `FileName string`

      Filter by file name

    - `OnlyManuallyUploaded bool`

      Filter only manually uploaded files (data_source_id is null)

    - `ProjectID string`

      Filter by project ID

  - `OrderBy param.Field[string]`

    Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `PageSize param.Field[int64]`

    Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

  - `PageToken param.Field[string]`

    Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `type FileQueryResponse struct{…}`

  Paginated list of files.

  - `Items []FileQueryResponseItem`

    The list of items.

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

  - `NextPageToken string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `TotalSize int64`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

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
  response, err := client.Files.Query(context.TODO(), llamacloudprod.FileQueryParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Items)
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
