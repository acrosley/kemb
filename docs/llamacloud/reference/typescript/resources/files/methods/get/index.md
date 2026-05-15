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
