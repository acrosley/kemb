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
