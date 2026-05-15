## Search Agent Data

`client.beta.agentData.search(AgentDataSearchParamsparams, RequestOptionsoptions?): PaginatedCursorPost<AgentData>`

**post** `/api/v1/beta/agent-data/:search`

Search agent data with filtering, sorting, and pagination.

### Parameters

- `params: AgentDataSearchParams`

  - `deployment_name: string`

    Body param: The agent deployment's name to search within

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `collection?: string`

    Body param: The logical agent data collection to search within

  - `filter?: Record<string, Filter> | null`

    Body param: A filter object or expression that filters resources listed in the response.

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

  - `include_total?: boolean`

    Body param: Whether to include the total number of items in the response

  - `offset?: number | null`

    Body param: The offset to start from. If not provided, the first page is returned

  - `order_by?: string | null`

    Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `page_size?: number | null`

    Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

  - `page_token?: string | null`

    Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

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

// Automatically fetches more pages as needed.
for await (const agentData of client.beta.agentData.search({
  deployment_name: 'deployment_name',
})) {
  console.log(agentData.id);
}
```

#### Response

```json
{
  "items": [
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
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
