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
