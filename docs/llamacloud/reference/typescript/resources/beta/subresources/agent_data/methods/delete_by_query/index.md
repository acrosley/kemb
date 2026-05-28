## Delete Agent Data By Query

`client.beta.agentData.deleteByQuery(AgentDataDeleteByQueryParamsparams, RequestOptionsoptions?): AgentDataDeleteByQueryResponse`

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Parameters

- `params: AgentDataDeleteByQueryParams`

  - `deployment_name: string`

    Body param: The agent deployment's name to delete data for

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `collection?: string`

    Body param: The logical agent data collection to delete from

  - `filter?: Record<string, Filter> | null`

    Body param: Optional filters to select which items to delete

    - `eq?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `excludes?: Array<number | string | (string & {}) | null>`

      - `number`

      - `string`

      - `(string & {})`

    - `gt?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `gte?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `includes?: Array<number | string | (string & {}) | null>`

      - `number`

      - `string`

      - `(string & {})`

    - `lt?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `lte?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `ne?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

### Returns

- `AgentDataDeleteByQueryResponse`

  API response for bulk delete operation

  - `deleted_count: number`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.agentData.deleteByQuery({ deployment_name: 'deployment_name' });

console.log(response.deleted_count);
```

#### Response

```json
{
  "deleted_count": 0
}
```
