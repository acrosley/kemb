## Delete Spreadsheet Job

`beta.sheets.delete_job(strspreadsheet_job_id, SheetDeleteJobParams**kwargs)  -> object`

**delete** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Delete a spreadsheet parsing job and its associated data.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheet_job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `object`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.sheets.delete_job(
    spreadsheet_job_id="spreadsheet_job_id",
)
print(response)
```

#### Response

```json
{}
```
