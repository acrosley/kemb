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
