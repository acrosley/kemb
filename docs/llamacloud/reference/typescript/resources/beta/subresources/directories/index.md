# Directories

## Create Directory

`client.beta.directories.create(DirectoryCreateParamsparams, RequestOptionsoptions?): DirectoryCreateResponse`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `params: DirectoryCreateParams`

  - `name: string`

    Body param: Human-readable name for the directory.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `description?: string | null`

    Body param: Optional description shown to users.

### Returns

- `DirectoryCreateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const directory = await client.beta.directories.create({ name: 'x' });

console.log(directory.id);
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

`client.beta.directories.list(DirectoryListParamsquery?, RequestOptionsoptions?): PaginatedCursor<DirectoryListResponse>`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `query: DirectoryListParams`

  - `include_deleted?: boolean`

  - `name?: string | null`

  - `organization_id?: string | null`

  - `page_size?: number | null`

  - `page_token?: string | null`

  - `project_id?: string | null`

  - `type?: "user" | "index" | null`

    - `"user"`

    - `"index"`

### Returns

- `DirectoryListResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const directoryListResponse of client.beta.directories.list()) {
  console.log(directoryListResponse.id);
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

`client.beta.directories.get(stringdirectoryID, DirectoryGetParamsquery?, RequestOptionsoptions?): DirectoryGetResponse`

**get** `/api/v1/beta/directories/{directory_id}`

Retrieve a directory by its identifier.

### Parameters

- `directoryID: string`

- `query: DirectoryGetParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `DirectoryGetResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const directory = await client.beta.directories.get('directory_id');

console.log(directory.id);
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

`client.beta.directories.update(stringdirectoryID, DirectoryUpdateParamsparams, RequestOptionsoptions?): DirectoryUpdateResponse`

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Parameters

- `directoryID: string`

- `params: DirectoryUpdateParams`

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `description?: string | null`

    Body param: Updated description for the directory.

  - `name?: string | null`

    Body param: Updated name for the directory.

### Returns

- `DirectoryUpdateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const directory = await client.beta.directories.update('directory_id');

console.log(directory.id);
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

`client.beta.directories.delete(stringdirectoryID, DirectoryDeleteParamsparams?, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `directoryID: string`

- `params: DirectoryDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.beta.directories.delete('directory_id');
```

## Domain Types

### Directory Create Response

- `DirectoryCreateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Directory List Response

- `DirectoryListResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Directory Get Response

- `DirectoryGetResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Directory Update Response

- `DirectoryUpdateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

# Files

## Add Directory File

`client.beta.directories.files.add(stringdirectoryID, FileAddParamsparams, RequestOptionsoptions?): FileAddResponse`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `directoryID: string`

- `params: FileAddParams`

  - `file_id: string`

    Body param: File ID for the storage location (required).

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `display_name?: string | null`

    Body param: Display name for the file. If not provided, will use the file's name.

  - `metadata?: Record<string, string | number | boolean | null> | null`

    Body param: User-defined metadata key-value pairs to associate with the file.

    - `string`

    - `number`

    - `boolean`

  - `unique_id?: string | null`

    Body param: Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `FileAddResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.directories.files.add('directory_id', { file_id: 'file_id' });

console.log(response.id);
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

`client.beta.directories.files.list(stringdirectoryID, FileListParamsquery?, RequestOptionsoptions?): PaginatedCursor<FileListResponse>`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `directoryID: string`

- `query: FileListParams`

  - `display_name?: string | null`

  - `display_name_contains?: string | null`

  - `expand?: Array<string> | null`

    Fields to expand on each directory file.

  - `file_id?: string | null`

  - `include_deleted?: boolean`

  - `organization_id?: string | null`

  - `page_size?: number | null`

  - `page_token?: string | null`

  - `project_id?: string | null`

  - `unique_id?: string | null`

  - `updated_at_on_or_after?: string | null`

    Include items updated at or after this timestamp (inclusive)

  - `updated_at_on_or_before?: string | null`

    Include items updated at or before this timestamp (inclusive)

### Returns

- `FileListResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const fileListResponse of client.beta.directories.files.list('directory_id')) {
  console.log(fileListResponse.id);
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

`client.beta.directories.files.get(stringdirectoryFileID, FileGetParamsparams, RequestOptionsoptions?): FileGetResponse`

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Parameters

- `directoryFileID: string`

- `params: FileGetParams`

  - `directory_id: string`

    Path param

  - `expand?: Array<string> | null`

    Query param: Fields to expand.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `FileGetResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const file = await client.beta.directories.files.get('directory_file_id', {
  directory_id: 'directory_id',
});

console.log(file.id);
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

`client.beta.directories.files.update(stringdirectoryFileID, FileUpdateParamsparams, RequestOptionsoptions?): FileUpdateResponse`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID: string`

- `params: FileUpdateParams`

  - `body_directory_id?: string | null`

    Body param: Move file to a different directory.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `display_name?: string | null`

    Body param: Updated display name.

  - `metadata?: Record<string, string | number | boolean | null> | null`

    Body param: User-defined metadata key-value pairs. Replaces the user metadata layer.

    - `string`

    - `number`

    - `boolean`

  - `unique_id?: string | null`

    Body param: Updated unique identifier.

### Returns

- `FileUpdateResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const file = await client.beta.directories.files.update('directory_file_id', {
  path_directory_id: 'directory_id',
});

console.log(file.id);
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

`client.beta.directories.files.delete(stringdirectoryFileID, FileDeleteParamsparams, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID: string`

- `params: FileDeleteParams`

  - `directory_id: string`

    Path param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.beta.directories.files.delete('directory_file_id', { directory_id: 'directory_id' });
```

## Upload File To Directory

`client.beta.directories.files.upload(stringdirectoryID, FileUploadParamsparams, RequestOptionsoptions?): FileUploadResponse`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `directoryID: string`

- `params: FileUploadParams`

  - `upload_file: Uploadable`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `display_name?: string | null`

    Body param

  - `external_file_id?: string | null`

    Body param

  - `metadata?: string | null`

    Body param: User metadata as a JSON object string.

  - `unique_id?: string | null`

    Body param

### Returns

- `FileUploadResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.directories.files.upload('directory_id', {
  upload_file: fs.createReadStream('path/to/file'),
});

console.log(response.id);
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

- `FileAddResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### File List Response

- `FileListResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### File Get Response

- `FileGetResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### File Update Response

- `FileUpdateResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### File Upload Response

- `FileUploadResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime
