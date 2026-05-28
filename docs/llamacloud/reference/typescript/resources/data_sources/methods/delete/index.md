## Delete Data Source

`client.dataSources.delete(stringdataSourceID, RequestOptionsoptions?): void`

**delete** `/api/v1/data-sources/{data_source_id}`

Delete a data source by ID.

### Parameters

- `dataSourceID: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.dataSources.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```
