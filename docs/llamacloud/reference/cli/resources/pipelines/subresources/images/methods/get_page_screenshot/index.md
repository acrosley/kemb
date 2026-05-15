## Get File Page Screenshot

`$ llamacloud-prod pipelines:images get-page-screenshot`

**get** `/api/v1/files/{id}/page_screenshots/{page_index}`

Get screenshot of a page from a file.

### Parameters

- `--id: string`

  Path param

- `--page-index: number`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Returns

- `PipelineImageGetPageScreenshotResponse: unknown`

### Example

```cli
llamacloud-prod pipelines:images get-page-screenshot \
  --api-key 'My API Key' \
  --id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --page-index 0
```

#### Response

```json
{}
```
