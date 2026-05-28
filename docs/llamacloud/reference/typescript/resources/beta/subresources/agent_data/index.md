# Agent Data

## Get Agent Data

`client.beta.agentData.get(stringitemID, AgentDataGetParamsquery?, RequestOptionsoptions?): AgentData`

**get** `/api/v1/beta/agent-data/{item_id}`

Get agent data by ID.

### Parameters

- `itemID: string`

- `query: AgentDataGetParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

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

const agentData = await client.beta.agentData.get('item_id');

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

## Create Agent Data

`client.beta.agentData.create(AgentDataCreateParamsparams, RequestOptionsoptions?): AgentData`

**post** `/api/v1/beta/agent-data`

Create new agent data.

### Parameters

- `params: AgentDataCreateParams`

  - `data: Record<string, unknown>`

    Body param

  - `deployment_name: string`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `collection?: string`

    Body param

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

const agentData = await client.beta.agentData.create({
  data: { foo: 'bar' },
  deployment_name: 'deployment_name',
});

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

## Domain Types

### Agent Data

- `AgentData`

  API Result for a single agent data item

  - `data: Record<string, unknown>`

  - `deployment_name: string`

  - `id?: string | null`

  - `collection?: string`

  - `created_at?: string | null`

  - `project_id?: string | null`

  - `updated_at?: string | null`

### Agent Data Delete Response

- `AgentDataDeleteResponse = Record<string, string>`

### Agent Data Aggregate Response

- `AgentDataAggregateResponse`

  API Result for a single group in the aggregate response

  - `group_key: Record<string, unknown>`

  - `count?: number | null`

  - `first_item?: Record<string, unknown> | null`

### Agent Data Delete By Query Response

- `AgentDataDeleteByQueryResponse`

  API response for bulk delete operation

  - `deleted_count: number`
