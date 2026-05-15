## Update Agent Data

`client.beta.agentData.update(stringitemID, AgentDataUpdateParamsparams, RequestOptionsoptions?): AgentData`

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Parameters

- `itemID: string`

- `params: AgentDataUpdateParams`

  - `data: Record<string, unknown>`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `AgentData`

  API Result for a single agent data item

  - `data: Record<string, unknown>`

  - `deployment_name: string`

  - `id?: string | null`

  - `collection?: string`

  - `created_at?: string | null`

  - `project_id?: string | null`

  - `updated_at?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const agentData = await client.beta.agentData.update('item_id', { data: { foo: 'bar' } });

console.log(agentData.id);
```

#### Response

```json
{
  "data": {
    "foo": "bar"
  },
  "deployment_name": "deployment_name",
  "id": "id",
  "collection": "collection",
  "created_at": "2019-12-27T18:11:19.117Z",
  "project_id": "project_id",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
