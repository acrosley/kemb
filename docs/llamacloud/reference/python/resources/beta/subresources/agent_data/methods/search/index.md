## Search Agent Data

`beta.agent_data.search(AgentDataSearchParams**kwargs)  -> SyncPaginatedCursorPost[AgentData]`

**post** `/api/v1/beta/agent-data/:search`

Search agent data with filtering, sorting, and pagination.

### Parameters

- `deployment_name: str`

  The agent deployment's name to search within

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `collection: Optional[str]`

  The logical agent data collection to search within

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

- `include_total: Optional[bool]`

  Whether to include the total number of items in the response

- `offset: Optional[int]`

  The offset to start from. If not provided, the first page is returned

- `order_by: Optional[str]`

  A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `page_size: Optional[int]`

  The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `page_token: Optional[str]`

  A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `class AgentData: …`

  API Result for a single agent data item

  - `data: Dict[str, object]`

  - `deployment_name: str`

  - `id: Optional[str]`

  - `collection: Optional[str]`

  - `created_at: Optional[datetime]`

  - `project_id: Optional[str]`

  - `updated_at: Optional[datetime]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agent_data.search(
    deployment_name="deployment_name",
)
page = page.items[0]
print(page.id)
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
