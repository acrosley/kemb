# Images

## List File Page Screenshots

**get** `/api/v1/files/{id}/page_screenshots`

List metadata for all screenshots of pages from a file.

### Path Parameters

- `id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

- `file_id: string`

  The ID of the file that the page screenshot was taken from

- `image_size: number`

  The size of the image in bytes

- `page_index: number`

  The index of the page for which the screenshot is taken (0-indexed)

- `metadata: optional map[unknown]`

  Metadata for the screenshot

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/files/$ID/page_screenshots \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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

**get** `/api/v1/files/{id}/page_screenshots/{page_index}`

Get screenshot of a page from a file.

### Path Parameters

- `id: string`

- `page_index: number`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/files/$ID/page_screenshots/$PAGE_INDEX \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{}
```

## Get File Page Figure

**get** `/api/v1/files/{id}/page-figures/{page_index}/{figure_name}`

Get a specific figure from a page of a file.

### Path Parameters

- `id: string`

- `page_index: number`

- `figure_name: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/files/$ID/page-figures/$PAGE_INDEX/$FIGURE_NAME \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{}
```

## List File Pages Figures

**get** `/api/v1/files/{id}/page-figures`

List metadata for all figures from all pages of a file.

### Path Parameters

- `id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

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

```http
curl https://api.cloud.llamaindex.ai/api/v1/files/$ID/page-figures \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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

## Domain Types

### Image List Page Screenshots Response

- `ImageListPageScreenshotsResponse = array of object { file_id, image_size, page_index, metadata }`

  - `file_id: string`

    The ID of the file that the page screenshot was taken from

  - `image_size: number`

    The size of the image in bytes

  - `page_index: number`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata: optional map[unknown]`

    Metadata for the screenshot

### Image Get Page Screenshot Response

- `ImageGetPageScreenshotResponse = unknown`

### Image Get Page Figure Response

- `ImageGetPageFigureResponse = unknown`

### Image List Page Figures Response

- `ImageListPageFiguresResponse = array of object { confidence, figure_name, figure_size, 4 more }`

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
