## Search Agent Data

**post** `/api/v1/beta/agent-data/:search`

Search agent data with filtering, sorting, and pagination.

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `deployment_name: string`

  The agent deployment's name to search within

- `collection: optional string`

  The logical agent data collection to search within

- `filter: optional map[object { eq, excludes, gt, 5 more } ]`

  A filter object or expression that filters resources listed in the response.

  - `eq: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `excludes: optional array of number or string or string`

    - `number`

    - `string`

    - `string`

  - `gt: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `gte: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `includes: optional array of number or string or string`

    - `number`

    - `string`

    - `string`

  - `lt: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `lte: optional number or string or string`

    - `number`

    - `string`

    - `string`

  - `ne: optional number or string or string`

    - `number`

    - `string`

    - `string`

- `include_total: optional boolean`

  Whether to include the total number of items in the response

- `offset: optional number`

  The offset to start from. If not provided, the first page is returned

- `order_by: optional string`

  A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `page_size: optional number`

  The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `page_token: optional string`

  A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

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

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/agent-data/:search \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "deployment_name": "deployment_name"
        }'
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
