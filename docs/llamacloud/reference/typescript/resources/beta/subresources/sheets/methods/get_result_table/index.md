## Get Result Region

`client.beta.sheets.getResultTable("table" | "extra" | "cell_metadata"regionType, SheetGetResultTableParamsparams, RequestOptionsoptions?): PresignedURL`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}`

Generate a presigned URL to download a specific extracted region.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `regionType: "table" | "extra" | "cell_metadata"`

  - `"table"`

  - `"extra"`

  - `"cell_metadata"`

- `params: SheetGetResultTableParams`

  - `spreadsheet_job_id: string`

    Path param

  - `region_id: string`

    Path param

  - `expires_at_seconds?: number | null`

    Query param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

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

const presignedURL = await client.beta.sheets.getResultTable('table', {
  spreadsheet_job_id: 'spreadsheet_job_id',
  region_id: 'region_id',
});

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
