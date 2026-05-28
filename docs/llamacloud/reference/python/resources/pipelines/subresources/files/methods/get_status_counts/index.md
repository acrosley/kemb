## Get Pipeline File Status Counts

`pipelines.files.get_status_counts(strpipeline_id, FileGetStatusCountsParams**kwargs)  -> FileGetStatusCountsResponse`

**get** `/api/v1/pipelines/{pipeline_id}/files/status-counts`

Get files for a pipeline.

### Parameters

- `pipeline_id: str`

- `data_source_id: Optional[str]`

- `only_manually_uploaded: Optional[bool]`

### Returns

- `class FileGetStatusCountsResponse: …`

  - `counts: Dict[str, int]`

    The counts of files by status

  - `total_count: int`

    The total number of files

  - `data_source_id: Optional[str]`

    The ID of the data source that the files belong to

  - `only_manually_uploaded: Optional[bool]`

    Whether to only count manually uploaded files

  - `pipeline_id: Optional[str]`

    The ID of the pipeline that the files belong to

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.pipelines.files.get_status_counts(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response.data_source_id)
```

#### Response

```json
{
  "counts": {
    "foo": 0
  },
  "total_count": 0,
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "only_manually_uploaded": true,
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```
