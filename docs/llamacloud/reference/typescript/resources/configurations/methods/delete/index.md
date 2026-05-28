## Delete Configuration

`client.configurations.delete(stringconfigID, ConfigurationDeleteParamsparams?, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/configurations/{config_id}`

Delete a product configuration.

### Parameters

- `configID: string`

- `params: ConfigurationDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.configurations.delete('config_id');
```
