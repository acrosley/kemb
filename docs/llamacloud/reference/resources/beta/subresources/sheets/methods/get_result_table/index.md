## Get Result Region

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}`

Generate a presigned URL to download a specific extracted region.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Path Parameters

- `spreadsheet_job_id: string`

- `region_id: string`

- `region_type: "table" or "extra" or "cell_metadata"`

  - `"table"`

  - `"extra"`

  - `"cell_metadata"`

### Query Parameters

- `expires_at_seconds: optional number`

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

- `PresignedURL = object { expires_at, url, form_fields }`

  Schema for a presigned URL.

  - `expires_at: string`

    The time at which the presigned URL expires

  - `url: string`

    A presigned URL for IO operations against a private file

  - `form_fields: optional map[string]`

    Form fields for a presigned POST request

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/sheets/jobs/$SPREADSHEET_JOB_ID/regions/$REGION_ID/result/$REGION_TYPE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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
