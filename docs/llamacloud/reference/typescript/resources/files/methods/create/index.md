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
