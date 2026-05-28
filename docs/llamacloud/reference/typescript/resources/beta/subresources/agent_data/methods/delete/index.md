## Delete Agent Data

`client.beta.agentData.delete(stringitemID, AgentDataDeleteParamsparams?, RequestOptionsoptions?): AgentDataDeleteResponse`

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Parameters

- `itemID: string`

- `params: AgentDataDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `AgentDataDeleteResponse = Record<string, string>`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const agentData = await client.beta.agentData.delete('item_id');

console.log(agentData);
```

#### Response

```json
{
  "foo": "string"
}
```
