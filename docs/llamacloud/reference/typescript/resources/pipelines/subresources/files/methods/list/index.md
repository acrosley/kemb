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
