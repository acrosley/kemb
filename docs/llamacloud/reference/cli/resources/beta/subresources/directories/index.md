# Directories

## Create Directory

`$ llamacloud-prod beta:directories create`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `--name: string`

  Body param: Human-readable name for the directory.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--description: optional string`

  Body param: Optional description shown to users.

### Returns

- `BetaDirectoryNewResponse: object { id, name, project_id, 4 more }`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: optional string`

    Optional description shown to users.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories create \
  --api-key 'My API Key' \
  --name x
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

`$ llamacloud-prod beta:directories list`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `--include-deleted: optional boolean`

- `--name: optional string`

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--type: optional "user" or "index"`

### Returns

- `DirectoryQueryResponse: object { items, next_page_token, total_size }`

  API query response schema for directories.

  - `items: array of object { id, name, project_id, 4 more }`

    The list of items.

    - `id: string`

      Unique identifier for the directory.

    - `name: string`

      Human-readable name for the directory.

    - `project_id: string`

      Project the directory belongs to.

    - `created_at: optional string`

      Creation datetime

    - `deleted_at: optional string`

      Optional timestamp of when the directory was deleted. Null if not deleted.

    - `description: optional string`

      Optional description shown to users.

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:directories list \
  --api-key 'My API Key'
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

`$ llamacloud-prod beta:directories get`

**get** `/api/v1/beta/directories/{directory_id}`

Retrieve a directory by its identifier.

### Parameters

- `--directory-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaDirectoryGetResponse: object { id, name, project_id, 4 more }`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: optional string`

    Optional description shown to users.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories get \
  --api-key 'My API Key' \
  --directory-id directory_id
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

`$ llamacloud-prod beta:directories update`

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Parameters

- `--directory-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--description: optional string`

  Body param: Updated description for the directory.

- `--name: optional string`

  Body param: Updated name for the directory.

### Returns

- `BetaDirectoryUpdateResponse: object { id, name, project_id, 4 more }`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: optional string`

    Optional description shown to users.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories update \
  --api-key 'My API Key' \
  --directory-id directory_id
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

`$ llamacloud-prod beta:directories delete`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `--directory-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Example

```cli
llamacloud-prod beta:directories delete \
  --api-key 'My API Key' \
  --directory-id directory_id
```

# Files

## Add Directory File

`$ llamacloud-prod beta:directories:files add`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `--directory-id: string`

  Path param

- `--file-id: string`

  Body param: File ID for the storage location (required).

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--display-name: optional string`

  Body param: Display name for the file. If not provided, will use the file's name.

- `--metadata: optional map[string or number or boolean]`

  Body param: User-defined metadata key-value pairs to associate with the file.

- `--unique-id: optional string`

  Body param: Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `BetaDirectoryFileAddResponse: object { id, directory_id, display_name, 8 more }`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `file_id: optional string`

    File ID for the storage location.

  - `metadata: optional map[string or number or boolean]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files add \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --file-id file_id
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

`$ llamacloud-prod beta:directories:files list`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `--directory-id: string`

- `--display-name: optional string`

- `--display-name-contains: optional string`

- `--expand: optional array of string`

  Fields to expand on each directory file.

- `--file-id: optional string`

- `--include-deleted: optional boolean`

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--unique-id: optional string`

- `--updated-at-on-or-after: optional string`

  Include items updated at or after this timestamp (inclusive)

- `--updated-at-on-or-before: optional string`

  Include items updated at or before this timestamp (inclusive)

### Returns

- `DirectoryFileQueryResponse: object { items, next_page_token, total_size }`

  API query response schema for directory files.

  - `items: array of object { id, directory_id, display_name, 8 more }`

    The list of items.

    - `id: string`

      Unique identifier for the directory file.

    - `directory_id: string`

      Directory the file belongs to.

    - `display_name: string`

      Display name for the file.

    - `project_id: string`

      Project the directory file belongs to.

    - `unique_id: string`

      Unique identifier for the file in the directory

    - `created_at: optional string`

      Creation datetime

    - `deleted_at: optional string`

      Soft delete marker when the file is removed upstream or by user action.

    - `download_url: optional object { expires_at, url, form_fields }`

      Schema for a presigned URL.

      - `expires_at: string`

        The time at which the presigned URL expires

      - `url: string`

        A presigned URL for IO operations against a private file

      - `form_fields: optional map[string]`

        Form fields for a presigned POST request

    - `file_id: optional string`

      File ID for the storage location.

    - `metadata: optional map[string or number or boolean]`

      Merged metadata from all sources. Higher-priority sources override lower.

      - `union_member_0: string`

      - `union_member_1: number`

      - `union_member_2: boolean`

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:directories:files list \
  --api-key 'My API Key' \
  --directory-id directory_id
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

`$ llamacloud-prod beta:directories:files get`

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Parameters

- `--directory-id: string`

  Path param

- `--directory-file-id: string`

  Path param

- `--expand: optional array of string`

  Query param: Fields to expand.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Returns

- `BetaDirectoryFileGetResponse: object { id, directory_id, display_name, 8 more }`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `file_id: optional string`

    File ID for the storage location.

  - `metadata: optional map[string or number or boolean]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files get \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --directory-file-id directory_file_id
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

`$ llamacloud-prod beta:directories:files update`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `--directory-id: string`

  Path param

- `--directory-file-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--directory-id: string`

  Path param

- `--display-name: optional string`

  Body param: Updated display name.

- `--metadata: optional map[string or number or boolean]`

  Body param: User-defined metadata key-value pairs. Replaces the user metadata layer.

- `--unique-id: optional string`

  Body param: Updated unique identifier.

### Returns

- `BetaDirectoryFileUpdateResponse: object { id, directory_id, display_name, 8 more }`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `file_id: optional string`

    File ID for the storage location.

  - `metadata: optional map[string or number or boolean]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files update \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --directory-file-id directory_file_id
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

`$ llamacloud-prod beta:directories:files delete`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `--directory-id: string`

  Path param

- `--directory-file-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Example

```cli
llamacloud-prod beta:directories:files delete \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --directory-file-id directory_file_id
```

## Upload File To Directory

`$ llamacloud-prod beta:directories:files upload`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `--directory-id: string`

  Path param

- `--upload-file: string`

  Body param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--display-name: optional string`

  Body param

- `--external-file-id: optional string`

  Body param

- `--metadata: optional string`

  Body param: User metadata as a JSON object string.

- `--unique-id: optional string`

  Body param

### Returns

- `BetaDirectoryFileUploadResponse: object { id, directory_id, display_name, 8 more }`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `file_id: optional string`

    File ID for the storage location.

  - `metadata: optional map[string or number or boolean]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files upload \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --upload-file 'Example data'
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
