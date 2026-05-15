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
