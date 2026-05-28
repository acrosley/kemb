# Files

## Get Pipeline File Status Counts

`client.pipelines.files.getStatusCounts(stringpipelineID, FileGetStatusCountsParamsquery?, RequestOptionsoptions?): FileGetStatusCountsResponse`

**get** `/api/v1/pipelines/{pipeline_id}/files/status-counts`

Get files for a pipeline.

### Parameters

- `pipelineID: string`

- `query: FileGetStatusCountsParams`

  - `data_source_id?: string | null`

  - `only_manually_uploaded?: boolean`

### Returns

- `FileGetStatusCountsResponse`

  - `counts: Record<string, number>`

    The counts of files by status

  - `total_count: number`

    The total number of files

  - `data_source_id?: string | null`

    The ID of the data source that the files belong to

  - `only_manually_uploaded?: boolean`

    Whether to only count manually uploaded files

  - `pipeline_id?: string | null`

    The ID of the pipeline that the files belong to

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.files.getStatusCounts(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response.data_source_id);
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

`client.pipelines.files.getStatus(stringfileID, FileGetStatusParamsparams, RequestOptionsoptions?): ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/files/{file_id}/status`

Get status of a file for a pipeline.

### Parameters

- `fileID: string`

- `params: FileGetStatusParams`

  - `pipeline_id: string`

### Returns

- `ManagedIngestionStatusResponse`

  - `status: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date?: string | null`

    Date of the deployment.

  - `effective_at?: string | null`

    When the status is effective

  - `error?: Array<Error> | null`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" | "DATA_SOURCE" | "FILE_UPDATER" | 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id?: string | null`

    ID of the latest job.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const managedIngestionStatusResponse = await client.pipelines.files.getStatus(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
);

console.log(managedIngestionStatusResponse.job_id);
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

`client.pipelines.files.create(stringpipelineID, FileCreateParamsparams, RequestOptionsoptions?): FileCreateResponse`

**put** `/api/v1/pipelines/{pipeline_id}/files`

Add files to a pipeline.

### Parameters

- `pipelineID: string`

- `params: FileCreateParams`

  - `body: Array<Body>`

    - `file_id: string`

      The ID of the file

    - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      Custom metadata for the file

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

### Returns

- `FileCreateResponse = Array<PipelineFile>`

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipelineFiles = await client.pipelines.files.create('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  body: [{ file_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' }],
});

console.log(pipelineFiles);
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

`client.pipelines.files.update(stringfileID, FileUpdateParamsparams, RequestOptionsoptions?): PipelineFile`

**put** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Update a file for a pipeline.

### Parameters

- `fileID: string`

- `params: FileUpdateParams`

  - `pipeline_id: string`

    Path param

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Body param: Custom metadata for the file

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Returns

- `PipelineFile`

  A file associated with a pipeline.

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipelineFile = await client.pipelines.files.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(pipelineFile.id);
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

`client.pipelines.files.delete(stringfileID, FileDeleteParamsparams, RequestOptionsoptions?): void`

**delete** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Delete a file from a pipeline.

### Parameters

- `fileID: string`

- `params: FileDeleteParams`

  - `pipeline_id: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.pipelines.files.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});
```

## List Pipeline Files2

`client.pipelines.files.list(stringpipelineID, FileListParamsquery?, RequestOptionsoptions?): PaginatedPipelineFiles<PipelineFile>`

**get** `/api/v1/pipelines/{pipeline_id}/files2`

List files for a pipeline with optional filtering, sorting, and pagination.

### Parameters

- `pipelineID: string`

- `query: FileListParams`

  - `data_source_id?: string | null`

  - `file_name_contains?: string | null`

  - `limit?: number | null`

  - `offset?: number | null`

  - `only_manually_uploaded?: boolean`

  - `order_by?: string | null`

  - `statuses?: Array<"NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more> | null`

    Filter by file statuses

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

### Returns

- `PipelineFile`

  A file associated with a pipeline.

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const pipelineFile of client.pipelines.files.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(pipelineFile.id);
}
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

- `PipelineFile`

  A file associated with a pipeline.

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

### File Get Status Counts Response

- `FileGetStatusCountsResponse`

  - `counts: Record<string, number>`

    The counts of files by status

  - `total_count: number`

    The total number of files

  - `data_source_id?: string | null`

    The ID of the data source that the files belong to

  - `only_manually_uploaded?: boolean`

    Whether to only count manually uploaded files

  - `pipeline_id?: string | null`

    The ID of the pipeline that the files belong to

### File Create Response

- `FileCreateResponse = Array<PipelineFile>`

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.
