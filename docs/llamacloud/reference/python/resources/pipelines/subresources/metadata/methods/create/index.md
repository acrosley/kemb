## Import Pipeline Metadata

`pipelines.metadata.create(strpipeline_id, MetadataCreateParams**kwargs)  -> MetadataCreateResponse`

**put** `/api/v1/pipelines/{pipeline_id}/metadata`

Import metadata for a pipeline.

### Parameters

- `pipeline_id: str`

- `upload_file: FileTypes`

### Returns

- `Dict[str, str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
metadata = client.pipelines.metadata.create(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    upload_file=b"Example data",
)
print(metadata)
```

#### Response

```json
{
  "foo": "string"
}
```
