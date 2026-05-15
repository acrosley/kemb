## Delete Spreadsheet Job

`client.beta.sheets.deleteJob(stringspreadsheetJobID, SheetDeleteJobParamsparams?, RequestOptionsoptions?): SheetDeleteJobResponse`

**delete** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Delete a spreadsheet parsing job and its associated data.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheetJobID: string`

- `params: SheetDeleteJobParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `SheetDeleteJobResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.sheets.deleteJob('spreadsheet_job_id');

console.log(response);
```

#### Response

```json
{}
```
