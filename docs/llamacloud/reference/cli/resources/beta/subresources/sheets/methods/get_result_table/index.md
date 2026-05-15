## Get Result Region

`$ llamacloud-prod beta:sheets get-result-table`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}`

Generate a presigned URL to download a specific extracted region.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--spreadsheet-job-id: string`

  Path param

- `--region-id: string`

  Path param

- `--region-type: "table" or "extra" or "cell_metadata"`

  Path param

- `--expires-at-seconds: optional number`

  Query param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

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
llamacloud-prod beta:sheets get-result-table \
  --api-key 'My API Key' \
  --spreadsheet-job-id spreadsheet_job_id \
  --region-id region_id \
  --region-type table
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
