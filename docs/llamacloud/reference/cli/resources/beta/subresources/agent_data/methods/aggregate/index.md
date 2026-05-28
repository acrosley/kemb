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
