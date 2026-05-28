# Agent Data

## Get Agent Data

`beta.agent_data.get(stritem_id, AgentDataGetParams**kwargs)  -> AgentData`

**get** `/api/v1/beta/agent-data/{item_id}`

Get agent data by ID.

### Parameters

- `item_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

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
agent_data = client.beta.agent_data.get(
    item_id="item_id",
)
print(agent_data.id)
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

`beta.agent_data.update(stritem_id, AgentDataUpdateParams**kwargs)  -> AgentData`

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Parameters

- `item_id: str`

- `data: Dict[str, object]`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

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
agent_data = client.beta.agent_data.update(
    item_id="item_id",
    data={
        "foo": "bar"
    },
)
print(agent_data.id)
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

`beta.agent_data.delete(stritem_id, AgentDataDeleteParams**kwargs)  -> AgentDataDeleteResponse`

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Parameters

- `item_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `Dict[str, str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
agent_data = client.beta.agent_data.delete(
    item_id="item_id",
)
print(agent_data)
```

#### Response

```json
{
  "foo": "string"
}
```

## Create Agent Data

`beta.agent_data.create(AgentDataCreateParams**kwargs)  -> AgentData`

**post** `/api/v1/beta/agent-data`

Create new agent data.

### Parameters

- `data: Dict[str, object]`

- `deployment_name: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `collection: Optional[str]`

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
agent_data = client.beta.agent_data.create(
    data={
        "foo": "bar"
    },
    deployment_name="deployment_name",
)
print(agent_data.id)
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

## Delete Agent Data By Query

`beta.agent_data.delete_by_query(AgentDataDeleteByQueryParams**kwargs)  -> AgentDataDeleteByQueryResponse`

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Parameters

- `deployment_name: str`

  The agent deployment's name to delete data for

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `collection: Optional[str]`

  The logical agent data collection to delete from

- `filter: Optional[Dict[str, Filter]]`

  Optional filters to select which items to delete

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

### Returns

- `class AgentDataDeleteByQueryResponse: …`

  API response for bulk delete operation

  - `deleted_count: int`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.agent_data.delete_by_query(
    deployment_name="deployment_name",
)
print(response.deleted_count)
```

#### Response

```json
{
  "deleted_count": 0
}
```

## Domain Types

### Agent Data

- `class AgentData: …`

  API Result for a single agent data item

  - `data: Dict[str, object]`

  - `deployment_name: str`

  - `id: Optional[str]`

  - `collection: Optional[str]`

  - `created_at: Optional[datetime]`

  - `project_id: Optional[str]`

  - `updated_at: Optional[datetime]`

### Agent Data Delete Response

- `Dict[str, str]`

### Agent Data Aggregate Response

- `class AgentDataAggregateResponse: …`

  API Result for a single group in the aggregate response

  - `group_key: Dict[str, object]`

  - `count: Optional[int]`

  - `first_item: Optional[Dict[str, object]]`

### Agent Data Delete By Query Response

- `class AgentDataDeleteByQueryResponse: …`

  API response for bulk delete operation

  - `deleted_count: int`
