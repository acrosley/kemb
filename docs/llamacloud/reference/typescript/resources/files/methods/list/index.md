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
