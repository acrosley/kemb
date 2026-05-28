## Aggregate Agent Data

`beta.agent_data.aggregate(AgentDataAggregateParams**kwargs)  -> SyncPaginatedCursorPost[AgentDataAggregateResponse]`

**post** `/api/v1/beta/agent-data/:aggregate`

Aggregate agent data with grouping and optional counting/first item retrieval.

### Parameters

- `deployment_name: str`

  The agent deployment's name to aggregate data for

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `collection: Optional[str]`

  The logical agent data collection to aggregate data for

- `count: Optional[bool]`

  Whether to count the number of items in each group

- `filter: Optional[Dict[str, Filter]]`

  A filter object or expression that filters resources listed in the response.

  - `eq: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `excludes: Optional[SequenceNotStr[Union[float, str, Union[str, datetime], null]]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `gt: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `gte: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `includes: Optional[SequenceNotStr[Union[float, str, Union[str, datetime], null]]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `lt: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `lte: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `ne: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

- `first: Optional[bool]`

  Whether to return the first item in each group (Sorted by created_at)

- `group_by: Optional[SequenceNotStr[str]]`

  The fields to group by. If empty, the entire dataset is grouped on. e.g. if left out, can be used for simple count operations

- `offset: Optional[int]`

  The offset to start from. If not provided, the first page is returned

- `order_by: Optional[str]`

  A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `page_size: Optional[int]`

  The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `page_token: Optional[str]`

  A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `class AgentDataAggregateResponse: …`

  API Result for a single group in the aggregate response

  - `group_key: Dict[str, object]`

  - `count: Optional[int]`

  - `first_item: Optional[Dict[str, object]]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agent_data.aggregate(
    deployment_name="deployment_name",
)
page = page.items[0]
print(page.group_key)
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
