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
