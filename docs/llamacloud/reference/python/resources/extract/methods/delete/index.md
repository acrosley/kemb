## Delete Extract Job

`extract.delete(strjob_id, ExtractDeleteParams**kwargs)  -> object`

**delete** `/api/v2/extract/{job_id}`

Delete an extraction job and its results.

### Parameters

- `job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `object`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
extract = client.extract.delete(
    job_id="job_id",
)
print(extract)
```

#### Response

```json
{}
```
