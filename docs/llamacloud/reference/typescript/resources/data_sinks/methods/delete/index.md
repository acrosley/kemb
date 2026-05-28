## Delete Data Sink

`client.dataSinks.delete(stringdataSinkID, RequestOptionsoptions?): void`

**delete** `/api/v1/data-sinks/{data_sink_id}`

Delete a data sink by ID.

### Parameters

- `dataSinkID: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.dataSinks.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```
