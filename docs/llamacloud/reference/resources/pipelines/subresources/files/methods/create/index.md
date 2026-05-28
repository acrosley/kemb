## Add Files To Pipeline Api

**put** `/api/v1/pipelines/{pipeline_id}/files`

Add files to a pipeline.

### Path Parameters

- `pipeline_id: string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `body: array of object { file_id, custom_metadata }`

  - `file_id: string`

    The ID of the file

  - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Custom metadata for the file

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

### Returns

- `id: string`

  Unique identifier for the pipeline file.

- `pipeline_id: string`

  The ID of the pipeline that the file is associated with.

- `config_hash: optional map[map[unknown] or array of unknown or string or 2 more]`

  Hashes for the configuration of the pipeline.

  - `map[unknown]`

  - `array of unknown`

  - `string`

  - `number`

  - `boolean`

- `created_at: optional string`

  When the pipeline file was created.

- `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

  Custom metadata for the file.

  - `map[unknown]`

  - `array of unknown`

  - `string`

  - `number`

  - `boolean`

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

  - `map[unknown]`

  - `array of unknown`

  - `string`

  - `number`

  - `boolean`

- `project_id: optional string`

  The ID of the project that the file belongs to.

- `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

  Resource information for the file.

  - `map[unknown]`

  - `array of unknown`

  - `string`

  - `number`

  - `boolean`

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

```http
curl https://api.cloud.llamaindex.ai/api/v1/pipelines/$PIPELINE_ID/files \
    -X PUT \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '[
          {
            "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            "custom_metadata": {
              "foo": {
                "foo": "bar"
              }
            }
          }
        ]'
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
