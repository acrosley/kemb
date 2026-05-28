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
