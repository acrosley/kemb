# Files

## Add Directory File

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Path Parameters

- `directory_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `file_id: string`

  File ID for the storage location (required).

- `display_name: optional string`

  Display name for the file. If not provided, will use the file's name.

- `metadata: optional map[string or number or boolean]`

  User-defined metadata key-value pairs to associate with the file.

  - `string`

  - `number`

  - `boolean`

- `unique_id: optional string`

  Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

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

- `download_url: optional PresignedURL`

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

  - `string`

  - `number`

  - `boolean`

- `updated_at: optional string`

  Update datetime

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID/files \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "file_id": "file_id"
        }'
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

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Path Parameters

- `directory_id: string`

### Query Parameters

- `display_name: optional string`

- `display_name_contains: optional string`

- `expand: optional array of string`

  Fields to expand on each directory file.

- `file_id: optional string`

- `include_deleted: optional boolean`

- `organization_id: optional string`

- `page_size: optional number`

- `page_token: optional string`

- `project_id: optional string`

- `unique_id: optional string`

- `updated_at_on_or_after: optional string`

  Include items updated at or after this timestamp (inclusive)

- `updated_at_on_or_before: optional string`

  Include items updated at or before this timestamp (inclusive)

### Cookie Parameters

- `session: optional string`

### Returns

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

  - `download_url: optional PresignedURL`

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

    - `string`

    - `number`

    - `boolean`

  - `updated_at: optional string`

    Update datetime

- `next_page_token: optional string`

  A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

- `total_size: optional number`

  The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID/files \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Path Parameters

- `directory_id: string`

- `directory_file_id: string`

### Query Parameters

- `expand: optional array of string`

  Fields to expand.

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

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

- `download_url: optional PresignedURL`

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

  - `string`

  - `number`

  - `boolean`

- `updated_at: optional string`

  Update datetime

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID/files/$DIRECTORY_FILE_ID \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Path Parameters

- `directory_id: string`

- `directory_file_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `directory_id: optional string`

  Move file to a different directory.

- `display_name: optional string`

  Updated display name.

- `metadata: optional map[string or number or boolean]`

  User-defined metadata key-value pairs. Replaces the user metadata layer.

  - `string`

  - `number`

  - `boolean`

- `unique_id: optional string`

  Updated unique identifier.

### Returns

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

- `download_url: optional PresignedURL`

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

  - `string`

  - `number`

  - `boolean`

- `updated_at: optional string`

  Update datetime

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID/files/$DIRECTORY_FILE_ID \
    -X PATCH \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{}'
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

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Path Parameters

- `directory_id: string`

- `directory_file_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID/files/$DIRECTORY_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

## Upload File To Directory

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Path Parameters

- `directory_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

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

- `download_url: optional PresignedURL`

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

  - `string`

  - `number`

  - `boolean`

- `updated_at: optional string`

  Update datetime

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/directories/$DIRECTORY_ID/files/upload \
    -H 'Content-Type: multipart/form-data' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -F 'upload_file=@/path/to/upload_file'
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

## Domain Types

### File Add Response

- `FileAddResponse = object { id, directory_id, display_name, 8 more }`

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

  - `download_url: optional PresignedURL`

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

    - `string`

    - `number`

    - `boolean`

  - `updated_at: optional string`

    Update datetime

### File List Response

- `FileListResponse = object { id, directory_id, display_name, 8 more }`

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

  - `download_url: optional PresignedURL`

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

    - `string`

    - `number`

    - `boolean`

  - `updated_at: optional string`

    Update datetime

### File Get Response

- `FileGetResponse = object { id, directory_id, display_name, 8 more }`

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

  - `download_url: optional PresignedURL`

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

    - `string`

    - `number`

    - `boolean`

  - `updated_at: optional string`

    Update datetime

### File Update Response

- `FileUpdateResponse = object { id, directory_id, display_name, 8 more }`

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

  - `download_url: optional PresignedURL`

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

    - `string`

    - `number`

    - `boolean`

  - `updated_at: optional string`

    Update datetime

### File Upload Response

- `FileUploadResponse = object { id, directory_id, display_name, 8 more }`

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

  - `download_url: optional PresignedURL`

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

    - `string`

    - `number`

    - `boolean`

  - `updated_at: optional string`

    Update datetime
