## Delete Extract Job

`client.extract.delete(stringjobID, ExtractDeleteParamsparams?, RequestOptionsoptions?): ExtractDeleteResponse`

**delete** `/api/v2/extract/{job_id}`

Delete an extraction job and its results.

### Parameters

- `jobID: string`

- `params: ExtractDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ExtractDeleteResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const extract = await client.extract.delete('job_id');

console.log(extract);
```

#### Response

```json
{}
```
