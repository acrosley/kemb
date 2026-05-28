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
