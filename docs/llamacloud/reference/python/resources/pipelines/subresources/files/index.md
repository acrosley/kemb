# Files

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

## Get Pipeline File Status

`pipelines.files.get_status(strfile_id, FileGetStatusParams**kwargs)  -> ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/files/{file_id}/status`

Get status of a file for a pipeline.

### Parameters

- `pipeline_id: str`

- `file_id: str`

### Returns

- `class ManagedIngestionStatusResponse: …`

  - `status: Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", 3 more]`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date: Optional[datetime]`

    Date of the deployment.

  - `effective_at: Optional[datetime]`

    When the status is effective

  - `error: Optional[List[Error]]`

    List of errors that occurred during ingestion.

    - `job_id: str`

      ID of the job that failed.

    - `message: str`

      List of errors that occurred during ingestion.

    - `step: Literal["MANAGED_INGESTION", "DATA_SOURCE", "FILE_UPDATER", 4 more]`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id: Optional[str]`

    ID of the latest job.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
managed_ingestion_status_response = client.pipelines.files.get_status(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(managed_ingestion_status_response.job_id)
```

#### Response

```json
{
  "status": "NOT_STARTED",
  "deployment_date": "2019-12-27T18:11:19.117Z",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error": [
    {
      "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "message": "message",
      "step": "MANAGED_INGESTION"
    }
  ],
  "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```

## Add Files To Pipeline Api

`pipelines.files.create(strpipeline_id, FileCreateParams**kwargs)  -> FileCreateResponse`

**put** `/api/v1/pipelines/{pipeline_id}/files`

Add files to a pipeline.

### Parameters

- `pipeline_id: str`

- `body: Iterable[Body]`

  - `file_id: str`

    The ID of the file

  - `custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, 3 more]]]`

    Custom metadata for the file

    - `Dict[str, object]`

    - `Iterable[object]`

    - `str`

    - `float`

    - `bool`

### Returns

- `List[PipelineFile]`

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
pipeline_files = client.pipelines.files.create(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    body=[{
        "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
    }],
)
print(pipeline_files)
```

#### Response

```json
[
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
]
```

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

## Delete Pipeline File

`pipelines.files.delete(strfile_id, FileDeleteParams**kwargs)`

**delete** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Delete a file from a pipeline.

### Parameters

- `pipeline_id: str`

- `file_id: str`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.pipelines.files.delete(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

## List Pipeline Files2

`pipelines.files.list(strpipeline_id, FileListParams**kwargs)  -> SyncPaginatedPipelineFiles[PipelineFile]`

**get** `/api/v1/pipelines/{pipeline_id}/files2`

List files for a pipeline with optional filtering, sorting, and pagination.

### Parameters

- `pipeline_id: str`

- `data_source_id: Optional[str]`

- `file_name_contains: Optional[str]`

- `limit: Optional[int]`

- `offset: Optional[int]`

- `only_manually_uploaded: Optional[bool]`

- `order_by: Optional[str]`

- `statuses: Optional[List[Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", 2 more]]]`

  Filter by file statuses

  - `"NOT_STARTED"`

  - `"IN_PROGRESS"`

  - `"SUCCESS"`

  - `"ERROR"`

  - `"CANCELLED"`

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
page = client.pipelines.files.list(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
page = page.files[0]
print(page.id)
```

#### Response

```json
{
  "files": [
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
  ],
  "limit": 0,
  "offset": 0,
  "total_count": 0
}
```

## Domain Types

### Pipeline File

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

### File Get Status Counts Response

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

### File Create Response

- `List[PipelineFile]`

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
