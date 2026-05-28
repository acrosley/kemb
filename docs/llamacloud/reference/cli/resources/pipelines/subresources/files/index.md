# Files

## Get Pipeline File Status Counts

`$ llamacloud-prod pipelines:files get-status-counts`

**get** `/api/v1/pipelines/{pipeline_id}/files/status-counts`

Get files for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--data-source-id: optional string`

- `--only-manually-uploaded: optional boolean`

### Returns

- `PipelineFileGetStatusCountsResponse: object { counts, total_count, data_source_id, 2 more }`

  - `counts: map[number]`

    The counts of files by status

  - `total_count: number`

    The total number of files

  - `data_source_id: optional string`

    The ID of the data source that the files belong to

  - `only_manually_uploaded: optional boolean`

    Whether to only count manually uploaded files

  - `pipeline_id: optional string`

    The ID of the pipeline that the files belong to

### Example

```cli
llamacloud-prod pipelines:files get-status-counts \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

`$ llamacloud-prod pipelines:files get-status`

**get** `/api/v1/pipelines/{pipeline_id}/files/{file_id}/status`

Get status of a file for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--file-id: string`

### Returns

- `managed_ingestion_status_response: object { status, deployment_date, effective_at, 2 more }`

  - `status: "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date: optional string`

    Date of the deployment.

  - `effective_at: optional string`

    When the status is effective

  - `error: optional array of object { job_id, message, step }`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" or "DATA_SOURCE" or "FILE_UPDATER" or 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id: optional string`

    ID of the latest job.

### Example

```cli
llamacloud-prod pipelines:files get-status \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --file-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

`$ llamacloud-prod pipelines:files create`

**put** `/api/v1/pipelines/{pipeline_id}/files`

Add files to a pipeline.

### Parameters

- `--pipeline-id: string`

- `--body: array of object { file_id, custom_metadata }`

### Returns

- `Response Add Files To Pipeline Api Api V1 Pipelines  Pipeline Id  Files Put: array of PipelineFile`

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash: optional map[map[unknown] or array of unknown or string or 2 more]`

    Hashes for the configuration of the pipeline.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `created_at: optional string`

    When the pipeline file was created.

  - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Custom metadata for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `data_source_id: optional string`

    The ID of the data source that the file belongs to.

  - `external_file_id: optional string`

    The ID of the file in the external system.

  - `file_id: optional string`

    The ID of the file.

  - `file_size: optional number`

    Size of the file in bytes.

  - `file_type: optional string`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count: optional number`

    The number of pages that have been indexed for this file.

  - `last_modified_at: optional string`

    The last modified time of the file.

  - `name: optional string`

    Name of the file.

  - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

    Permission information for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `project_id: optional string`

    The ID of the project that the file belongs to.

  - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

    Resource information for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `status: optional "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: optional string`

    The last time the status was updated.

  - `updated_at: optional string`

    When the pipeline file was last updated.

### Example

```cli
llamacloud-prod pipelines:files create \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --body '{file_id: 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e}'
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

`$ llamacloud-prod pipelines:files update`

**put** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Update a file for a pipeline.

### Parameters

- `--pipeline-id: string`

  Path param

- `--file-id: string`

  Path param

- `--custom-metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

  Body param: Custom metadata for the file

### Returns

- `pipeline_file: object { id, pipeline_id, config_hash, 16 more }`

  A file associated with a pipeline.

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash: optional map[map[unknown] or array of unknown or string or 2 more]`

    Hashes for the configuration of the pipeline.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `created_at: optional string`

    When the pipeline file was created.

  - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Custom metadata for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `data_source_id: optional string`

    The ID of the data source that the file belongs to.

  - `external_file_id: optional string`

    The ID of the file in the external system.

  - `file_id: optional string`

    The ID of the file.

  - `file_size: optional number`

    Size of the file in bytes.

  - `file_type: optional string`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count: optional number`

    The number of pages that have been indexed for this file.

  - `last_modified_at: optional string`

    The last modified time of the file.

  - `name: optional string`

    Name of the file.

  - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

    Permission information for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `project_id: optional string`

    The ID of the project that the file belongs to.

  - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

    Resource information for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `status: optional "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: optional string`

    The last time the status was updated.

  - `updated_at: optional string`

    When the pipeline file was last updated.

### Example

```cli
llamacloud-prod pipelines:files update \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --file-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

`$ llamacloud-prod pipelines:files delete`

**delete** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Delete a file from a pipeline.

### Parameters

- `--pipeline-id: string`

- `--file-id: string`

### Example

```cli
llamacloud-prod pipelines:files delete \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --file-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```

## List Pipeline Files2

`$ llamacloud-prod pipelines:files list`

**get** `/api/v1/pipelines/{pipeline_id}/files2`

List files for a pipeline with optional filtering, sorting, and pagination.

### Parameters

- `--pipeline-id: string`

- `--data-source-id: optional string`

- `--file-name-contains: optional string`

- `--limit: optional number`

- `--offset: optional number`

- `--only-manually-uploaded: optional boolean`

- `--order-by: optional string`

- `--status: optional array of "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

  Filter by file statuses

### Returns

- `PaginatedListPipelineFilesResponse: object { files, limit, offset, total_count }`

  Paginated list of pipeline files.

  - `files: array of PipelineFile`

    The files to list

    - `id: string`

      Unique identifier for the pipeline file.

    - `pipeline_id: string`

      The ID of the pipeline that the file is associated with.

    - `config_hash: optional map[map[unknown] or array of unknown or string or 2 more]`

      Hashes for the configuration of the pipeline.

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `created_at: optional string`

      When the pipeline file was created.

    - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

      Custom metadata for the file.

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `data_source_id: optional string`

      The ID of the data source that the file belongs to.

    - `external_file_id: optional string`

      The ID of the file in the external system.

    - `file_id: optional string`

      The ID of the file.

    - `file_size: optional number`

      Size of the file in bytes.

    - `file_type: optional string`

      File type (e.g. pdf, docx, etc.).

    - `indexed_page_count: optional number`

      The number of pages that have been indexed for this file.

    - `last_modified_at: optional string`

      The last modified time of the file.

    - `name: optional string`

      Name of the file.

    - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

      Permission information for the file.

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `project_id: optional string`

      The ID of the project that the file belongs to.

    - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

      Resource information for the file.

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `status: optional "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

      Status of the pipeline file.

      - `"NOT_STARTED"`

      - `"IN_PROGRESS"`

      - `"SUCCESS"`

      - `"ERROR"`

      - `"CANCELLED"`

    - `status_updated_at: optional string`

      The last time the status was updated.

    - `updated_at: optional string`

      When the pipeline file was last updated.

  - `limit: number`

    The limit of the files

  - `offset: number`

    The offset of the files

  - `total_count: number`

    The total number of files

### Example

```cli
llamacloud-prod pipelines:files list \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

- `pipeline_file: object { id, pipeline_id, config_hash, 16 more }`

  A file associated with a pipeline.

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash: optional map[map[unknown] or array of unknown or string or 2 more]`

    Hashes for the configuration of the pipeline.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `created_at: optional string`

    When the pipeline file was created.

  - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Custom metadata for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `data_source_id: optional string`

    The ID of the data source that the file belongs to.

  - `external_file_id: optional string`

    The ID of the file in the external system.

  - `file_id: optional string`

    The ID of the file.

  - `file_size: optional number`

    Size of the file in bytes.

  - `file_type: optional string`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count: optional number`

    The number of pages that have been indexed for this file.

  - `last_modified_at: optional string`

    The last modified time of the file.

  - `name: optional string`

    Name of the file.

  - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

    Permission information for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `project_id: optional string`

    The ID of the project that the file belongs to.

  - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

    Resource information for the file.

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `status: optional "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: optional string`

    The last time the status was updated.

  - `updated_at: optional string`

    When the pipeline file was last updated.
