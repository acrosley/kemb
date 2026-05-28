# Files

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

## Delete File

`client.Files.Delete(ctx, fileID, body) error`

**delete** `/api/v1/beta/files/{file_id}`

Delete a file from the project.

### Parameters

- `fileID string`

- `body FileDeleteParams`

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
  err := client.Files.Delete(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.FileDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

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

## Domain Types

### File

- `type File struct{…}`

  Schema for a file.

  - `ID string`

    Unique identifier

  - `Name string`

  - `ProjectID string`

    The ID of the project that the file belongs to

  - `CreatedAt Time`

    Creation datetime

  - `DataSourceID string`

    The ID of the data source that the file belongs to

  - `ExpiresAt Time`

    The expiration date for the file. Files past this date can be deleted.

  - `ExternalFileID string`

    The ID of the file in the external system

  - `FileSize int64`

    Size of the file in bytes

  - `FileType string`

    File type (e.g. pdf, docx, etc.)

  - `LastModifiedAt Time`

    The last modified time of the file

  - `PermissionInfo map[string, FilePermissionInfoUnion]`

    Permission information for the file

    - `type FilePermissionInfoMap map[string, any]`

    - `type FilePermissionInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Purpose string`

    The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

  - `ResourceInfo map[string, FileResourceInfoUnion]`

    Resource information for the file

    - `type FileResourceInfoMap map[string, any]`

    - `type FileResourceInfoArray []any`

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

### Presigned URL

- `type PresignedURL struct{…}`

  Schema for a presigned URL.

  - `ExpiresAt Time`

    The time at which the presigned URL expires

  - `URL string`

    A presigned URL for IO operations against a private file

  - `FormFields map[string, string]`

    Form fields for a presigned POST request
