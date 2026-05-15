## Delete Configuration

`configurations.delete(strconfig_id, ConfigurationDeleteParams**kwargs)`

**delete** `/api/v1/beta/configurations/{config_id}`

Delete a product configuration.

### Parameters

- `config_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.configurations.delete(
    config_id="config_id",
)
```
