## Get Result Region

`beta.sheets.get_result_table(Literal["table", "extra", "cell_metadata"]region_type, SheetGetResultTableParams**kwargs)  -> PresignedURL`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}`

Generate a presigned URL to download a specific extracted region.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheet_job_id: str`

- `region_id: str`

- `region_type: Literal["table", "extra", "cell_metadata"]`

  - `"table"`

  - `"extra"`

  - `"cell_metadata"`

- `expires_at_seconds: Optional[int]`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class PresignedURL: …`

  Schema for a presigned URL.

  - `expires_at: datetime`

    The time at which the presigned URL expires

  - `url: str`

    A presigned URL for IO operations against a private file

  - `form_fields: Optional[Dict[str, str]]`

    Form fields for a presigned POST request

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
presigned_url = client.beta.sheets.get_result_table(
    region_type="table",
    spreadsheet_job_id="spreadsheet_job_id",
    region_id="region_id",
)
print(presigned_url.expires_at)
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
