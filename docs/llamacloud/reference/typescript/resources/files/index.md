# Files

## Upload File

`client.files.create(FileCreateParamsparams, RequestOptionsoptions?): FileCreateResponse`

**post** `/api/v1/beta/files`

Upload a file using multipart/form-data.

Set `purpose` to indicate how the file will be used:
`user_data`, `parse`, `extract`, `classify`, `split`,
`sheet`, or `agent_app`.

Returns the created file metadata including its ID for use
in subsequent parse, extract, or classify operations.

### Parameters

- `params: FileCreateParams`

  - `file: Uploadable`

    Body param: The file to upload

  - `purpose: string`

    Body param: The intended purpose of the file. Valid values: 'user_data', 'parse', 'extract', 'split', 'classify', 'sheet', 'agent_app'. This determines the storage and retention policy for the file.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `external_file_id?: string | null`

    Body param: The ID of the file in the external system

### Returns

- `FileCreateResponse`

  An uploaded file.

  - `id: string`

    Unique file identifier

  - `name: string`

    File name including extension

  - `project_id: string`

    Project this file belongs to

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `expires_at?: string | null`

    When the file expires and may be automatically removed. Null means no expiration.

  - `external_file_id?: string | null`

    Optional ID for correlating with an external system

  - `file_type?: string | null`

    File extension (pdf, docx, png, etc.)

  - `last_modified_at?: string | null`

    When the file was last modified (ISO 8601)

  - `purpose?: string | null`

    How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const file = await client.files.create({
  file: fs.createReadStream('path/to/file'),
  purpose: 'purpose',
});

console.log(file.id);
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

`client.files.query(FileQueryParamsparams, RequestOptionsoptions?): FileQueryResponse`

**post** `/api/v1/beta/files/query`

Query files with flexible filtering and pagination.

**Deprecated**: Use GET /files instead for listing files with query parameters.

Args:
request: The query request with filters and pagination
project: Validated project from dependency

Returns:
Paginated response with files

### Parameters

- `params: FileQueryParams`

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `filter?: Filter | null`

    Body param: Filter parameters for file queries.

    - `data_source_id?: string | null`

      Filter by data source ID

    - `external_file_id?: string | null`

      Filter by external file ID

    - `file_ids?: Array<string> | null`

      Filter by specific file IDs

    - `file_name?: string | null`

      Filter by file name

    - `only_manually_uploaded?: boolean | null`

      Filter only manually uploaded files (data_source_id is null)

    - `project_id?: string | null`

      Filter by project ID

  - `order_by?: string | null`

    Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `page_size?: number | null`

    Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

  - `page_token?: string | null`

    Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `FileQueryResponse`

  Paginated list of files.

  - `items: Array<Item>`

    The list of items.

    - `id: string`

      Unique file identifier

    - `name: string`

      File name including extension

    - `project_id: string`

      Project this file belongs to

    - `download_url?: PresignedURL | null`

      Schema for a presigned URL.

      - `expires_at: string`

        The time at which the presigned URL expires

      - `url: string`

        A presigned URL for IO operations against a private file

      - `form_fields?: Record<string, string> | null`

        Form fields for a presigned POST request

    - `expires_at?: string | null`

      When the file expires and may be automatically removed. Null means no expiration.

    - `external_file_id?: string | null`

      Optional ID for correlating with an external system

    - `file_type?: string | null`

      File extension (pdf, docx, png, etc.)

    - `last_modified_at?: string | null`

      When the file was last modified (ISO 8601)

    - `purpose?: string | null`

      How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

  - `next_page_token?: string | null`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size?: number | null`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.files.query();

console.log(response.items);
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

`client.files.list(FileListParamsquery?, RequestOptionsoptions?): PaginatedCursor<FileListResponse>`

**get** `/api/v1/beta/files`

List files with optional filtering and pagination.

Filter by `file_name`, `file_ids`, or `external_file_id`.
Supports cursor-based pagination and custom ordering.

### Parameters

- `query: FileListParams`

  - `expand?: Array<string> | null`

    Fields to expand on each file.

  - `external_file_id?: string | null`

    Filter by external file ID.

  - `file_ids?: Array<string> | null`

    Filter by specific file IDs.

  - `file_name?: string | null`

    Filter by file name (exact match).

  - `order_by?: string | null`

    A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `organization_id?: string | null`

  - `page_size?: number | null`

    The maximum number of items to return. Defaults to 50, maximum is 1000.

  - `page_token?: string | null`

    A page token received from a previous list call. Provide this to retrieve the subsequent page.

  - `project_id?: string | null`

### Returns

- `FileListResponse`

  An uploaded file.

  - `id: string`

    Unique file identifier

  - `name: string`

    File name including extension

  - `project_id: string`

    Project this file belongs to

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `expires_at?: string | null`

    When the file expires and may be automatically removed. Null means no expiration.

  - `external_file_id?: string | null`

    Optional ID for correlating with an external system

  - `file_type?: string | null`

    File extension (pdf, docx, png, etc.)

  - `last_modified_at?: string | null`

    When the file was last modified (ISO 8601)

  - `purpose?: string | null`

    How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const fileListResponse of client.files.list()) {
  console.log(fileListResponse.id);
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

`client.files.delete(stringfileID, FileDeleteParamsparams?, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/files/{file_id}`

Delete a file from the project.

### Parameters

- `fileID: string`

- `params: FileDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.files.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```

## Read File Content

`client.files.get(stringfileID, FileGetParamsquery?, RequestOptionsoptions?): PresignedURL`

**get** `/api/v1/beta/files/{file_id}/content`

Get a presigned URL to download the file content.

### Parameters

- `fileID: string`

- `query: FileGetParams`

  - `expires_at_seconds?: number | null`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `PresignedURL`

  Schema for a presigned URL.

  - `expires_at: string`

    The time at which the presigned URL expires

  - `url: string`

    A presigned URL for IO operations against a private file

  - `form_fields?: Record<string, string> | null`

    Form fields for a presigned POST request

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const presignedURL = await client.files.get('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(presignedURL.expires_at);
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

- `File`

  Schema for a file.

  - `id: string`

    Unique identifier

  - `name: string`

  - `project_id: string`

    The ID of the project that the file belongs to

  - `created_at?: string | null`

    Creation datetime

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to

  - `expires_at?: string | null`

    The expiration date for the file. Files past this date can be deleted.

  - `external_file_id?: string | null`

    The ID of the file in the external system

  - `file_size?: number | null`

    Size of the file in bytes

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.)

  - `last_modified_at?: string | null`

    The last modified time of the file

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `purpose?: string | null`

    The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Presigned URL

- `PresignedURL`

  Schema for a presigned URL.

  - `expires_at: string`

    The time at which the presigned URL expires

  - `url: string`

    A presigned URL for IO operations against a private file

  - `form_fields?: Record<string, string> | null`

    Form fields for a presigned POST request

### File Create Response

- `FileCreateResponse`

  An uploaded file.

  - `id: string`

    Unique file identifier

  - `name: string`

    File name including extension

  - `project_id: string`

    Project this file belongs to

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `expires_at?: string | null`

    When the file expires and may be automatically removed. Null means no expiration.

  - `external_file_id?: string | null`

    Optional ID for correlating with an external system

  - `file_type?: string | null`

    File extension (pdf, docx, png, etc.)

  - `last_modified_at?: string | null`

    When the file was last modified (ISO 8601)

  - `purpose?: string | null`

    How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

### File Query Response

- `FileQueryResponse`

  Paginated list of files.

  - `items: Array<Item>`

    The list of items.

    - `id: string`

      Unique file identifier

    - `name: string`

      File name including extension

    - `project_id: string`

      Project this file belongs to

    - `download_url?: PresignedURL | null`

      Schema for a presigned URL.

      - `expires_at: string`

        The time at which the presigned URL expires

      - `url: string`

        A presigned URL for IO operations against a private file

      - `form_fields?: Record<string, string> | null`

        Form fields for a presigned POST request

    - `expires_at?: string | null`

      When the file expires and may be automatically removed. Null means no expiration.

    - `external_file_id?: string | null`

      Optional ID for correlating with an external system

    - `file_type?: string | null`

      File extension (pdf, docx, png, etc.)

    - `last_modified_at?: string | null`

      When the file was last modified (ISO 8601)

    - `purpose?: string | null`

      How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

  - `next_page_token?: string | null`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size?: number | null`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### File List Response

- `FileListResponse`

  An uploaded file.

  - `id: string`

    Unique file identifier

  - `name: string`

    File name including extension

  - `project_id: string`

    Project this file belongs to

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `expires_at?: string | null`

    When the file expires and may be automatically removed. Null means no expiration.

  - `external_file_id?: string | null`

    Optional ID for correlating with an external system

  - `file_type?: string | null`

    File extension (pdf, docx, png, etc.)

  - `last_modified_at?: string | null`

    When the file was last modified (ISO 8601)

  - `purpose?: string | null`

    How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app
