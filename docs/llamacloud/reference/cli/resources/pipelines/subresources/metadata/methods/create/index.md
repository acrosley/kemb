## Import Pipeline Metadata

`$ llamacloud-prod pipelines:metadata create`

**put** `/api/v1/pipelines/{pipeline_id}/metadata`

Import metadata for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--upload-file: string`

### Returns

- `PipelineMetadataNewResponse: map[string]`

### Example

```cli
llamacloud-prod pipelines:metadata create \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --upload-file 'Example data'
```

#### Response

```json
{
  "foo": "string"
}
```
