## Update Pipeline File

`pipelines.files.update(strfile_id, FileUpdateParams**kwargs)  -> PipelineFile`

**put** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Update a file for a pipeline.

### Parameters

- `pipeline_id: str`

- `file_id: str`

- `custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, 3 more]]]`

  Custom metadata for the file

  - `Dict[str, object]`

  - `Iterable[object]`

  - `str`

  - `float`

  - `bool`

### Returns

- `class PipelineFile: …`

  A file associated with a pipeline.

  - `id: str`

    Unique identifier for the pipeline file.

  - `pipeline_id: str`

    The ID of the pipeline that the file is associated with.

  - `config_hash: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Hashes for the configuration of the pipeline.

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `created_at: Optional[datetime]`

    When the pipeline file was created.

  - `custom_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Custom metadata for the file.

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `data_source_id: Optional[str]`

    The ID of the data source that the file belongs to.

  - `external_file_id: Optional[str]`

    The ID of the file in the external system.

  - `file_id: Optional[str]`

    The ID of the file.

  - `file_size: Optional[int]`

    Size of the file in bytes.

  - `file_type: Optional[str]`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count: Optional[int]`

    The number of pages that have been indexed for this file.

  - `last_modified_at: Optional[datetime]`

    The last modified time of the file.

  - `name: Optional[str]`

    Name of the file.

  - `permission_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Permission information for the file.

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `project_id: Optional[str]`

    The ID of the project that the file belongs to.

  - `resource_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Resource information for the file.

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `status: Optional[Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", 2 more]]`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: Optional[datetime]`

    The last time the status was updated.

  - `updated_at: Optional[datetime]`

    When the pipeline file was last updated.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
pipeline_file = client.pipelines.files.update(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(pipeline_file.id)
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "foo": {
      "foo": "bar"
    }
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "custom_metadata": {
    "foo": {
      "foo": "bar"
    }
  },
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "external_file_id": "external_file_id",
  "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "file_size": 0,
  "file_type": "file_type",
  "indexed_page_count": 0,
  "last_modified_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "permission_info": {
    "foo": {
      "foo": "bar"
    }
  },
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "resource_info": {
    "foo": {
      "foo": "bar"
    }
  },
  "status": "NOT_STARTED",
  "status_updated_at": "2019-12-27T18:11:19.117Z",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
