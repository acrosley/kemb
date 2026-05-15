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
