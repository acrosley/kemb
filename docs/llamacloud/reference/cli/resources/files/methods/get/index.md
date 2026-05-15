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
