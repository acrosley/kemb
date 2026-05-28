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
