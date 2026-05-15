# Images

## List File Page Screenshots

`$ llamacloud-prod pipelines:images list-page-screenshots`

**get** `/api/v1/files/{id}/page_screenshots`

List metadata for all screenshots of pages from a file.

### Parameters

- `--id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `Response List File Page Screenshots Api V1 Files  Id  Page Screenshots Get: array of object { file_id, image_size, page_index, metadata }`

  - `file_id: string`

    The ID of the file that the page screenshot was taken from

  - `image_size: number`

    The size of the image in bytes

  - `page_index: number`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata: optional map[unknown]`

    Metadata for the screenshot

### Example

```cli
llamacloud-prod pipelines:images list-page-screenshots \
  --api-key 'My API Key' \
  --id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```

#### Response

```json
[
  {
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "image_size": 0,
    "page_index": 0,
    "metadata": {
      "foo": "bar"
    }
  }
]
```

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

## List File Pages Figures

`$ llamacloud-prod pipelines:images list-page-figures`

**get** `/api/v1/files/{id}/page-figures`

List metadata for all figures from all pages of a file.

### Parameters

- `--id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `Response List File Pages Figures Api V1 Files  Id  Page Figures Get: array of object { confidence, figure_name, figure_size, 4 more }`

  - `confidence: number`

    The confidence of the figure

  - `figure_name: string`

    The name of the figure

  - `figure_size: number`

    The size of the figure in bytes

  - `file_id: string`

    The ID of the file that the figure was taken from

  - `page_index: number`

    The index of the page for which the figure is taken (0-indexed)

  - `is_likely_noise: optional boolean`

    Whether the figure is likely to be noise

  - `metadata: optional map[unknown]`

    Metadata for the figure

### Example

```cli
llamacloud-prod pipelines:images list-page-figures \
  --api-key 'My API Key' \
  --id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```

#### Response

```json
[
  {
    "confidence": 0,
    "figure_name": "figure_name",
    "figure_size": 0,
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "page_index": 0,
    "is_likely_noise": true,
    "metadata": {
      "foo": "bar"
    }
  }
]
```
