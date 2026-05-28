# Agent Data

## Get Agent Data

`$ llamacloud-prod beta:agent-data get`

**get** `/api/v1/beta/agent-data/{item_id}`

Get agent data by ID.

### Parameters

- `--item-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

### Example

```cli
llamacloud-prod beta:agent-data get \
  --api-key 'My API Key' \
  --item-id item_id
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

`$ llamacloud-prod beta:agent-data update`

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Parameters

- `--item-id: string`

  Path param

- `--data: map[unknown]`

  Body param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Returns

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

### Example

```cli
llamacloud-prod beta:agent-data update \
  --api-key 'My API Key' \
  --item-id item_id \
  --data '{foo: bar}'
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

`$ llamacloud-prod beta:agent-data delete`

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Parameters

- `--item-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaAgentDataDeleteResponse: map[string]`

### Example

```cli
llamacloud-prod beta:agent-data delete \
  --api-key 'My API Key' \
  --item-id item_id
```

#### Response

```json
{
  "foo": "string"
}
```

## Create Agent Data

`$ llamacloud-prod beta:agent-data create`

**post** `/api/v1/beta/agent-data`

Create new agent data.

### Parameters

- `--data: map[unknown]`

  Body param

- `--deployment-name: string`

  Body param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param

### Returns

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

### Example

```cli
llamacloud-prod beta:agent-data create \
  --api-key 'My API Key' \
  --data '{foo: bar}' \
  --deployment-name deployment_name
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

`$ llamacloud-prod beta:agent-data search`

**post** `/api/v1/beta/agent-data/:search`

Search agent data with filtering, sorting, and pagination.

### Parameters

- `--deployment-name: string`

  Body param: The agent deployment's name to search within

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param: The logical agent data collection to search within

- `--filter: optional map[object { eq, excludes, gt, 5 more } ]`

  Body param: A filter object or expression that filters resources listed in the response.

- `--include-total: optional boolean`

  Body param: Whether to include the total number of items in the response

- `--offset: optional number`

  Body param: The offset to start from. If not provided, the first page is returned

- `--order-by: optional string`

  Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `--page-size: optional number`

  Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `--page-token: optional string`

  Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `PaginatedResponse_AgentData_: object { items, next_page_token, total_size }`

  - `items: array of AgentData`

    The list of items.

    - `data: map[unknown]`

    - `deployment_name: string`

    - `id: optional string`

    - `collection: optional string`

    - `created_at: optional string`

    - `project_id: optional string`

    - `updated_at: optional string`

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:agent-data search \
  --api-key 'My API Key' \
  --deployment-name deployment_name
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

`$ llamacloud-prod beta:agent-data aggregate`

**post** `/api/v1/beta/agent-data/:aggregate`

Aggregate agent data with grouping and optional counting/first item retrieval.

### Parameters

- `--deployment-name: string`

  Body param: The agent deployment's name to aggregate data for

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param: The logical agent data collection to aggregate data for

- `--count: optional boolean`

  Body param: Whether to count the number of items in each group

- `--filter: optional map[object { eq, excludes, gt, 5 more } ]`

  Body param: A filter object or expression that filters resources listed in the response.

- `--first: optional boolean`

  Body param: Whether to return the first item in each group (Sorted by created_at)

- `--group-by: optional array of string`

  Body param: The fields to group by. If empty, the entire dataset is grouped on. e.g. if left out, can be used for simple count operations

- `--offset: optional number`

  Body param: The offset to start from. If not provided, the first page is returned

- `--order-by: optional string`

  Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `--page-size: optional number`

  Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `--page-token: optional string`

  Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `PaginatedResponse_AggregateGroup_: object { items, next_page_token, total_size }`

  - `items: array of object { group_key, count, first_item }`

    The list of items.

    - `group_key: map[unknown]`

    - `count: optional number`

    - `first_item: optional map[unknown]`

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:agent-data aggregate \
  --api-key 'My API Key' \
  --deployment-name deployment_name
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

`$ llamacloud-prod beta:agent-data delete-by-query`

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Parameters

- `--deployment-name: string`

  Body param: The agent deployment's name to delete data for

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param: The logical agent data collection to delete from

- `--filter: optional map[object { eq, excludes, gt, 5 more } ]`

  Body param: Optional filters to select which items to delete

### Returns

- `BetaAgentDataDeleteByQueryResponse: object { deleted_count }`

  API response for bulk delete operation

  - `deleted_count: number`

### Example

```cli
llamacloud-prod beta:agent-data delete-by-query \
  --api-key 'My API Key' \
  --deployment-name deployment_name
```

#### Response

```json
{
  "deleted_count": 0
}
```

## Domain Types

### Agent Data

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`
