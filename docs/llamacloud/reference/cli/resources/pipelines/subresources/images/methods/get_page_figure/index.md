## Get File Page Figure

`$ llamacloud-prod pipelines:images get-page-figure`

**get** `/api/v1/files/{id}/page-figures/{page_index}/{figure_name}`

Get a specific figure from a page of a file.

### Parameters

- `--id: string`

  Path param

- `--page-index: number`

  Path param

- `--figure-name: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Returns

- `PipelineImageGetPageFigureResponse: unknown`

### Example

```cli
llamacloud-prod pipelines:images get-page-figure \
  --api-key 'My API Key' \
  --id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --page-index 0 \
  --figure-name figure_name
```

#### Response

```json
{}
```
