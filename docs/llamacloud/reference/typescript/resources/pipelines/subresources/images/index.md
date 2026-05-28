# Images

## List File Page Screenshots

`client.pipelines.images.listPageScreenshots(stringid, ImageListPageScreenshotsParamsquery?, RequestOptionsoptions?): ImageListPageScreenshotsResponse`

**get** `/api/v1/files/{id}/page_screenshots`

List metadata for all screenshots of pages from a file.

### Parameters

- `id: string`

- `query: ImageListPageScreenshotsParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ImageListPageScreenshotsResponse = Array<ImageListPageScreenshotsResponseItem>`

  - `file_id: string`

    The ID of the file that the page screenshot was taken from

  - `image_size: number`

    The size of the image in bytes

  - `page_index: number`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata?: Record<string, unknown> | null`

    Metadata for the screenshot

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.images.listPageScreenshots(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response);
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

`client.pipelines.images.getPageScreenshot(numberpageIndex, ImageGetPageScreenshotParamsparams, RequestOptionsoptions?): ImageGetPageScreenshotResponse`

**get** `/api/v1/files/{id}/page_screenshots/{page_index}`

Get screenshot of a page from a file.

### Parameters

- `pageIndex: number`

- `params: ImageGetPageScreenshotParams`

  - `id: string`

    Path param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `ImageGetPageScreenshotResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.images.getPageScreenshot(0, {
  id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response);
```

#### Response

```json
{}
```

## Get File Page Figure

`client.pipelines.images.getPageFigure(stringfigureName, ImageGetPageFigureParamsparams, RequestOptionsoptions?): ImageGetPageFigureResponse`

**get** `/api/v1/files/{id}/page-figures/{page_index}/{figure_name}`

Get a specific figure from a page of a file.

### Parameters

- `figureName: string`

- `params: ImageGetPageFigureParams`

  - `id: string`

    Path param

  - `page_index: number`

    Path param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `ImageGetPageFigureResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.images.getPageFigure('figure_name', {
  id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  page_index: 0,
});

console.log(response);
```

#### Response

```json
{}
```

## List File Pages Figures

`client.pipelines.images.listPageFigures(stringid, ImageListPageFiguresParamsquery?, RequestOptionsoptions?): ImageListPageFiguresResponse`

**get** `/api/v1/files/{id}/page-figures`

List metadata for all figures from all pages of a file.

### Parameters

- `id: string`

- `query: ImageListPageFiguresParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ImageListPageFiguresResponse = Array<ImageListPageFiguresResponseItem>`

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

  - `is_likely_noise?: boolean`

    Whether the figure is likely to be noise

  - `metadata?: Record<string, unknown> | null`

    Metadata for the figure

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.images.listPageFigures(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response);
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

- `ImageListPageScreenshotsResponse = Array<ImageListPageScreenshotsResponseItem>`

  - `file_id: string`

    The ID of the file that the page screenshot was taken from

  - `image_size: number`

    The size of the image in bytes

  - `page_index: number`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata?: Record<string, unknown> | null`

    Metadata for the screenshot

### Image Get Page Screenshot Response

- `ImageGetPageScreenshotResponse = unknown`

### Image Get Page Figure Response

- `ImageGetPageFigureResponse = unknown`

### Image List Page Figures Response

- `ImageListPageFiguresResponse = Array<ImageListPageFiguresResponseItem>`

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

  - `is_likely_noise?: boolean`

    Whether the figure is likely to be noise

  - `metadata?: Record<string, unknown> | null`

    Metadata for the figure
