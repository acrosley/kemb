## Delete Pipeline Files Metadata

`client.pipelines.metadata.deleteAll(stringpipelineID, RequestOptionsoptions?): void`

**delete** `/api/v1/pipelines/{pipeline_id}/metadata`

Delete metadata for all files in a pipeline.

### Parameters

- `pipelineID: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.pipelines.metadata.deleteAll('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```
