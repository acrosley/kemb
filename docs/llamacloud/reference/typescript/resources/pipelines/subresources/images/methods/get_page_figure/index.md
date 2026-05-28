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
