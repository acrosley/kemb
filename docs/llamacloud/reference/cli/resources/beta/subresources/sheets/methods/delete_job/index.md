## Delete Spreadsheet Job

`$ llamacloud-prod beta:sheets delete-job`

**delete** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Delete a spreadsheet parsing job and its associated data.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--spreadsheet-job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaSheetDeleteJobResponse: unknown`

### Example

```cli
llamacloud-prod beta:sheets delete-job \
  --api-key 'My API Key' \
  --spreadsheet-job-id spreadsheet_job_id
```

#### Response

```json
{}
```
