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
