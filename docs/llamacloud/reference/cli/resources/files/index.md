# Files

## Upload File

`$ llamacloud-prod files create`

**post** `/api/v1/beta/files`

Upload a file using multipart/form-data.

Set `purpose` to indicate how the file will be used:
`user_data`, `parse`, `extract`, `classify`, `split`,
`sheet`, or `agent_app`.

Returns the created file metadata including its ID for use
in subsequent parse, extract, or classify operations.

### Parameters

- `--file: string`

  Body param: The file to upload

- `--purpose: string`

  Body param: The intended purpose of the file. Valid values: 'user_data', 'parse', 'extract', 'split', 'classify', 'sheet', 'agent_app'. This determines the storage and retention policy for the file.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--external-file-id: optional string`

  Body param: The ID of the file in the external system

### Returns

- `FileNewResponse: object { id, name, project_id, 6 more }`

  An uploaded file.

  - `id: string`

    Unique file identifier

  - `name: string`

    File name including extension

  - `project_id: string`

    Project this file belongs to

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `expires_at: optional string`

    When the file expires and may be automatically removed. Null means no expiration.

  - `external_file_id: optional string`

    Optional ID for correlating with an external system

  - `file_type: optional string`

    File extension (pdf, docx, png, etc.)

  - `last_modified_at: optional string`

    When the file was last modified (ISO 8601)

  - `purpose: optional string`

    How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

### Example

```cli
llamacloud-prod files create \
  --api-key 'My API Key' \
  --file 'Example data' \
  --purpose purpose
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

`$ llamacloud-prod files query`

**post** `/api/v1/beta/files/query`

Query files with flexible filtering and pagination.

**Deprecated**: Use GET /files instead for listing files with query parameters.

Args:
request: The query request with filters and pagination
project: Validated project from dependency

Returns:
Paginated response with files

### Parameters

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--filter: optional object { data_source_id, external_file_id, file_ids, 3 more }`

  Body param: Filter parameters for file queries.

- `--order-by: optional string`

  Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `--page-size: optional number`

  Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `--page-token: optional string`

  Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `FileQueryResponse: object { items, next_page_token, total_size }`

  Paginated list of files.

  - `items: array of object { id, name, project_id, 6 more }`

    The list of items.

    - `id: string`

      Unique file identifier

    - `name: string`

      File name including extension

    - `project_id: string`

      Project this file belongs to

    - `download_url: optional object { expires_at, url, form_fields }`

      Schema for a presigned URL.

      - `expires_at: string`

        The time at which the presigned URL expires

      - `url: string`

        A presigned URL for IO operations against a private file

      - `form_fields: optional map[string]`

        Form fields for a presigned POST request

    - `expires_at: optional string`

      When the file expires and may be automatically removed. Null means no expiration.

    - `external_file_id: optional string`

      Optional ID for correlating with an external system

    - `file_type: optional string`

      File extension (pdf, docx, png, etc.)

    - `last_modified_at: optional string`

      When the file was last modified (ISO 8601)

    - `purpose: optional string`

      How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod files query \
  --api-key 'My API Key'
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

`$ llamacloud-prod files list`

**get** `/api/v1/beta/files`

List files with optional filtering and pagination.

Filter by `file_name`, `file_ids`, or `external_file_id`.
Supports cursor-based pagination and custom ordering.

### Parameters

- `--expand: optional array of string`

  Fields to expand on each file.

- `--external-file-id: optional string`

  Filter by external file ID.

- `--file-id: optional array of string`

  Filter by specific file IDs.

- `--file-name: optional string`

  Filter by file name (exact match).

- `--order-by: optional string`

  A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `--organization-id: optional string`

- `--page-size: optional number`

  The maximum number of items to return. Defaults to 50, maximum is 1000.

- `--page-token: optional string`

  A page token received from a previous list call. Provide this to retrieve the subsequent page.

- `--project-id: optional string`

### Returns

- `FileQueryResponseV2: object { items, next_page_token, total_size }`

  Paginated list of files.

  - `items: array of object { id, name, project_id, 6 more }`

    The list of items.

    - `id: string`

      Unique file identifier

    - `name: string`

      File name including extension

    - `project_id: string`

      Project this file belongs to

    - `download_url: optional object { expires_at, url, form_fields }`

      Schema for a presigned URL.

      - `expires_at: string`

        The time at which the presigned URL expires

      - `url: string`

        A presigned URL for IO operations against a private file

      - `form_fields: optional map[string]`

        Form fields for a presigned POST request

    - `expires_at: optional string`

      When the file expires and may be automatically removed. Null means no expiration.

    - `external_file_id: optional string`

      Optional ID for correlating with an external system

    - `file_type: optional string`

      File extension (pdf, docx, png, etc.)

    - `last_modified_at: optional string`

      When the file was last modified (ISO 8601)

    - `purpose: optional string`

      How the file will be used: user_data, parse, extract, classify, split, sheet, or agent_app

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod files list \
  --api-key 'My API Key'
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

`$ llamacloud-prod files delete`

**delete** `/api/v1/beta/files/{file_id}`

Delete a file from the project.

### Parameters

- `--file-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Example

```cli
llamacloud-prod files delete \
  --api-key 'My API Key' \
  --file-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```

## Read File Content

`$ llamacloud-prod files get`

**get** `/api/v1/beta/files/{file_id}/content`

Get a presigned URL to download the file content.

### Parameters

- `--file-id: string`

- `--expires-at-seconds: optional number`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `presigned_url: object { expires_at, url, form_fields }`

  Schema for a presigned URL.

  - `expires_at: string`

    The time at which the presigned URL expires

  - `url: string`

    A presigned URL for IO operations against a private file

  - `form_fields: optional map[string]`

    Form fields for a presigned POST request

### Example

```cli
llamacloud-prod files get \
  --api-key 'My API Key' \
  --file-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

- `file: object { id, name, project_id, 11 more }`

  Schema for a file.

  - `id: string`

    Unique identifier

  - `name: string`

  - `project_id: string`

    The ID of the project that the file belongs to

  - `created_at: optional string`

    Creation datetime

  - `data_source_id: optional string`

    The ID of the data source that the file belongs to

  - `expires_at: optional string`

    The expiration date for the file. Files past this date can be deleted.

  - `external_file_id: optional string`

    The ID of the file in the external system

  - `file_size: optional number`

    Size of the file in bytes

  - `file_type: optional string`

    File type (e.g. pdf, docx, etc.)

  - `last_modified_at: optional string`

    The last modified time of the file

  - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

    Permission information for the file

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `purpose: optional string`

    The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

  - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

    Resource information for the file

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `updated_at: optional string`

    Update datetime

### Presigned URL

- `presigned_url: object { expires_at, url, form_fields }`

  Schema for a presigned URL.

  - `expires_at: string`

    The time at which the presigned URL expires

  - `url: string`

    A presigned URL for IO operations against a private file

  - `form_fields: optional map[string]`

    Form fields for a presigned POST request
