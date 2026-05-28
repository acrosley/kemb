# Directories

## Create Directory

`client.Beta.Directories.New(ctx, params) (*BetaDirectoryNewResponse, error)`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `params BetaDirectoryNewParams`

  - `Name param.Field[string]`

    Body param: Human-readable name for the directory.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Description param.Field[string]`

    Body param: Optional description shown to users.

### Returns

- `type BetaDirectoryNewResponse struct{…}`

  API response schema for a directory.

  - `ID string`

    Unique identifier for the directory.

  - `Name string`

    Human-readable name for the directory.

  - `ProjectID string`

    Project the directory belongs to.

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `Description string`

    Optional description shown to users.

  - `UpdatedAt Time`

    Update datetime

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
  directory, err := client.Beta.Directories.New(context.TODO(), llamacloudprod.BetaDirectoryNewParams{
    Name: "x",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", directory.ID)
}
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Directories

`client.Beta.Directories.List(ctx, query) (*PaginatedCursor[BetaDirectoryListResponse], error)`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `query BetaDirectoryListParams`

  - `IncludeDeleted param.Field[bool]`

  - `Name param.Field[string]`

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

  - `PageToken param.Field[string]`

  - `ProjectID param.Field[string]`

  - `Type param.Field[BetaDirectoryListParamsType]`

    - `const BetaDirectoryListParamsTypeUser BetaDirectoryListParamsType = "user"`

    - `const BetaDirectoryListParamsTypeIndex BetaDirectoryListParamsType = "index"`

### Returns

- `type BetaDirectoryListResponse struct{…}`

  API response schema for a directory.

  - `ID string`

    Unique identifier for the directory.

  - `Name string`

    Human-readable name for the directory.

  - `ProjectID string`

    Project the directory belongs to.

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `Description string`

    Optional description shown to users.

  - `UpdatedAt Time`

    Update datetime

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
  page, err := client.Beta.Directories.List(context.TODO(), llamacloudprod.BetaDirectoryListParams{

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
      "id": "id",
      "name": "x",
      "project_id": "project_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "deleted_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Directory

`client.Beta.Directories.Get(ctx, directoryID, query) (*BetaDirectoryGetResponse, error)`

**get** `/api/v1/beta/directories/{directory_id}`

Retrieve a directory by its identifier.

### Parameters

- `directoryID string`

- `query BetaDirectoryGetParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type BetaDirectoryGetResponse struct{…}`

  API response schema for a directory.

  - `ID string`

    Unique identifier for the directory.

  - `Name string`

    Human-readable name for the directory.

  - `ProjectID string`

    Project the directory belongs to.

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `Description string`

    Optional description shown to users.

  - `UpdatedAt Time`

    Update datetime

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
  directory, err := client.Beta.Directories.Get(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", directory.ID)
}
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Directory

`client.Beta.Directories.Update(ctx, directoryID, params) (*BetaDirectoryUpdateResponse, error)`

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Parameters

- `directoryID string`

- `params BetaDirectoryUpdateParams`

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Description param.Field[string]`

    Body param: Updated description for the directory.

  - `Name param.Field[string]`

    Body param: Updated name for the directory.

### Returns

- `type BetaDirectoryUpdateResponse struct{…}`

  API response schema for a directory.

  - `ID string`

    Unique identifier for the directory.

  - `Name string`

    Human-readable name for the directory.

  - `ProjectID string`

    Project the directory belongs to.

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `Description string`

    Optional description shown to users.

  - `UpdatedAt Time`

    Update datetime

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
  directory, err := client.Beta.Directories.Update(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", directory.ID)
}
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Directory

`client.Beta.Directories.Delete(ctx, directoryID, body) error`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `directoryID string`

- `body BetaDirectoryDeleteParams`

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
  err := client.Beta.Directories.Delete(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

# Files

## Add Directory File

`client.Beta.Directories.Files.Add(ctx, directoryID, params) (*BetaDirectoryFileAddResponse, error)`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `directoryID string`

- `params BetaDirectoryFileAddParams`

  - `FileID param.Field[string]`

    Body param: File ID for the storage location (required).

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `DisplayName param.Field[string]`

    Body param: Display name for the file. If not provided, will use the file's name.

  - `Metadata param.Field[map[string, BetaDirectoryFileAddParamsMetadataUnion]]`

    Body param: User-defined metadata key-value pairs to associate with the file.

    - `string`

    - `float64`

    - `bool`

  - `UniqueID param.Field[string]`

    Body param: Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `type BetaDirectoryFileAddResponse struct{…}`

  API response schema for a directory file.

  - `ID string`

    Unique identifier for the directory file.

  - `DirectoryID string`

    Directory the file belongs to.

  - `DisplayName string`

    Display name for the file.

  - `ProjectID string`

    Project the directory file belongs to.

  - `UniqueID string`

    Unique identifier for the file in the directory

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Soft delete marker when the file is removed upstream or by user action.

  - `DownloadURL PresignedURL`

    Schema for a presigned URL.

    - `ExpiresAt Time`

      The time at which the presigned URL expires

    - `URL string`

      A presigned URL for IO operations against a private file

    - `FormFields map[string, string]`

      Form fields for a presigned POST request

  - `FileID string`

    File ID for the storage location.

  - `Metadata map[string, BetaDirectoryFileAddResponseMetadataUnion]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

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
  response, err := client.Beta.Directories.Files.Add(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryFileAddParams{
      FileID: "file_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.ID)
}
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Directory Files

`client.Beta.Directories.Files.List(ctx, directoryID, query) (*PaginatedCursor[BetaDirectoryFileListResponse], error)`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `directoryID string`

- `query BetaDirectoryFileListParams`

  - `DisplayName param.Field[string]`

  - `DisplayNameContains param.Field[string]`

  - `Expand param.Field[[]string]`

    Fields to expand on each directory file.

  - `FileID param.Field[string]`

  - `IncludeDeleted param.Field[bool]`

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

  - `PageToken param.Field[string]`

  - `ProjectID param.Field[string]`

  - `UniqueID param.Field[string]`

  - `UpdatedAtOnOrAfter param.Field[Time]`

    Include items updated at or after this timestamp (inclusive)

  - `UpdatedAtOnOrBefore param.Field[Time]`

    Include items updated at or before this timestamp (inclusive)

### Returns

- `type BetaDirectoryFileListResponse struct{…}`

  API response schema for a directory file.

  - `ID string`

    Unique identifier for the directory file.

  - `DirectoryID string`

    Directory the file belongs to.

  - `DisplayName string`

    Display name for the file.

  - `ProjectID string`

    Project the directory file belongs to.

  - `UniqueID string`

    Unique identifier for the file in the directory

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Soft delete marker when the file is removed upstream or by user action.

  - `DownloadURL PresignedURL`

    Schema for a presigned URL.

    - `ExpiresAt Time`

      The time at which the presigned URL expires

    - `URL string`

      A presigned URL for IO operations against a private file

    - `FormFields map[string, string]`

      Form fields for a presigned POST request

  - `FileID string`

    File ID for the storage location.

  - `Metadata map[string, BetaDirectoryFileListResponseMetadataUnion]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

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
  page, err := client.Beta.Directories.Files.List(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryFileListParams{

    },
  )
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
      "id": "id",
      "directory_id": "directory_id",
      "display_name": "x",
      "project_id": "project_id",
      "unique_id": "x",
      "created_at": "2019-12-27T18:11:19.117Z",
      "deleted_at": "2019-12-27T18:11:19.117Z",
      "download_url": {
        "expires_at": "2019-12-27T18:11:19.117Z",
        "url": "https://example.com",
        "form_fields": {
          "foo": "string"
        }
      },
      "file_id": "file_id",
      "metadata": {
        "foo": "string"
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Directory File

`client.Beta.Directories.Files.Get(ctx, directoryFileID, params) (*BetaDirectoryFileGetResponse, error)`

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Parameters

- `directoryFileID string`

- `params BetaDirectoryFileGetParams`

  - `DirectoryID param.Field[string]`

    Path param

  - `Expand param.Field[[]string]`

    Query param: Fields to expand.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

### Returns

- `type BetaDirectoryFileGetResponse struct{…}`

  API response schema for a directory file.

  - `ID string`

    Unique identifier for the directory file.

  - `DirectoryID string`

    Directory the file belongs to.

  - `DisplayName string`

    Display name for the file.

  - `ProjectID string`

    Project the directory file belongs to.

  - `UniqueID string`

    Unique identifier for the file in the directory

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Soft delete marker when the file is removed upstream or by user action.

  - `DownloadURL PresignedURL`

    Schema for a presigned URL.

    - `ExpiresAt Time`

      The time at which the presigned URL expires

    - `URL string`

      A presigned URL for IO operations against a private file

    - `FormFields map[string, string]`

      Form fields for a presigned POST request

  - `FileID string`

    File ID for the storage location.

  - `Metadata map[string, BetaDirectoryFileGetResponseMetadataUnion]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

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
  file, err := client.Beta.Directories.Files.Get(
    context.TODO(),
    "directory_file_id",
    llamacloudprod.BetaDirectoryFileGetParams{
      DirectoryID: "directory_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", file.ID)
}
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Directory File

`client.Beta.Directories.Files.Update(ctx, directoryFileID, params) (*BetaDirectoryFileUpdateResponse, error)`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID string`

- `params BetaDirectoryFileUpdateParams`

  - `PathDirectoryID param.Field[string]`

    Path param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `PathDirectoryID param.Field[string]`

    Path param

  - `DisplayName param.Field[string]`

    Body param: Updated display name.

  - `Metadata param.Field[map[string, BetaDirectoryFileUpdateParamsMetadataUnion]]`

    Body param: User-defined metadata key-value pairs. Replaces the user metadata layer.

    - `string`

    - `float64`

    - `bool`

  - `UniqueID param.Field[string]`

    Body param: Updated unique identifier.

### Returns

- `type BetaDirectoryFileUpdateResponse struct{…}`

  API response schema for a directory file.

  - `ID string`

    Unique identifier for the directory file.

  - `DirectoryID string`

    Directory the file belongs to.

  - `DisplayName string`

    Display name for the file.

  - `ProjectID string`

    Project the directory file belongs to.

  - `UniqueID string`

    Unique identifier for the file in the directory

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Soft delete marker when the file is removed upstream or by user action.

  - `DownloadURL PresignedURL`

    Schema for a presigned URL.

    - `ExpiresAt Time`

      The time at which the presigned URL expires

    - `URL string`

      A presigned URL for IO operations against a private file

    - `FormFields map[string, string]`

      Form fields for a presigned POST request

  - `FileID string`

    File ID for the storage location.

  - `Metadata map[string, BetaDirectoryFileUpdateResponseMetadataUnion]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

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
  file, err := client.Beta.Directories.Files.Update(
    context.TODO(),
    "directory_file_id",
    llamacloudprod.BetaDirectoryFileUpdateParams{
      PathDirectoryID: "directory_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", file.ID)
}
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Directory File

`client.Beta.Directories.Files.Delete(ctx, directoryFileID, params) error`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID string`

- `params BetaDirectoryFileDeleteParams`

  - `DirectoryID param.Field[string]`

    Path param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

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
  err := client.Beta.Directories.Files.Delete(
    context.TODO(),
    "directory_file_id",
    llamacloudprod.BetaDirectoryFileDeleteParams{
      DirectoryID: "directory_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

## Upload File To Directory

`client.Beta.Directories.Files.Upload(ctx, directoryID, params) (*BetaDirectoryFileUploadResponse, error)`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `directoryID string`

- `params BetaDirectoryFileUploadParams`

  - `UploadFile param.Field[Reader]`

    Body param

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `DisplayName param.Field[string]`

    Body param

  - `ExternalFileID param.Field[string]`

    Body param

  - `Metadata param.Field[string]`

    Body param: User metadata as a JSON object string.

  - `UniqueID param.Field[string]`

    Body param

### Returns

- `type BetaDirectoryFileUploadResponse struct{…}`

  API response schema for a directory file.

  - `ID string`

    Unique identifier for the directory file.

  - `DirectoryID string`

    Directory the file belongs to.

  - `DisplayName string`

    Display name for the file.

  - `ProjectID string`

    Project the directory file belongs to.

  - `UniqueID string`

    Unique identifier for the file in the directory

  - `CreatedAt Time`

    Creation datetime

  - `DeletedAt Time`

    Soft delete marker when the file is removed upstream or by user action.

  - `DownloadURL PresignedURL`

    Schema for a presigned URL.

    - `ExpiresAt Time`

      The time at which the presigned URL expires

    - `URL string`

      A presigned URL for IO operations against a private file

    - `FormFields map[string, string]`

      Form fields for a presigned POST request

  - `FileID string`

    File ID for the storage location.

  - `Metadata map[string, BetaDirectoryFileUploadResponseMetadataUnion]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

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
  response, err := client.Beta.Directories.Files.Upload(
    context.TODO(),
    "directory_id",
    llamacloudprod.BetaDirectoryFileUploadParams{
      UploadFile: io.Reader(bytes.NewBuffer([]byte("Example data"))),
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.ID)
}
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
