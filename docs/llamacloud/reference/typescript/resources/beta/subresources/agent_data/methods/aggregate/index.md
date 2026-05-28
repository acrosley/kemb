## Aggregate Agent Data

`client.beta.agentData.aggregate(AgentDataAggregateParamsparams, RequestOptionsoptions?): PaginatedCursorPost<AgentDataAggregateResponse>`

**post** `/api/v1/beta/agent-data/:aggregate`

Aggregate agent data with grouping and optional counting/first item retrieval.

### Parameters

- `params: AgentDataAggregateParams`

  - `deployment_name: string`

    Body param: The agent deployment's name to aggregate data for

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `collection?: string`

    Body param: The logical agent data collection to aggregate data for

  - `count?: boolean | null`

    Body param: Whether to count the number of items in each group

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

  - `first?: boolean | null`

    Body param: Whether to return the first item in each group (Sorted by created_at)

  - `group_by?: Array<string> | null`

    Body param: The fields to group by. If empty, the entire dataset is grouped on. e.g. if left out, can be used for simple count operations

  - `offset?: number | null`

    Body param: The offset to start from. If not provided, the first page is returned

  - `order_by?: string | null`

    Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `page_size?: number | null`

    Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

  - `page_token?: string | null`

    Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `AgentDataAggregateResponse`

  API Result for a single group in the aggregate response

  - `group_key: Record<string, unknown>`

  - `count?: number | null`

  - `first_item?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentDataAggregateResponse of client.beta.agentData.aggregate({
  deployment_name: 'deployment_name',
})) {
  console.log(agentDataAggregateResponse.group_key);
}
```

#### Response

```json
{
  "items": [
    {
      "group_key": {
        "foo": "bar"
      },
      "count": 0,
      "first_item": {
        "foo": "bar"
      }
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
