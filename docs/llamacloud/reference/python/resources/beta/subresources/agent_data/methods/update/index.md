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
