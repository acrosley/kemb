## Delete Pipeline Files Metadata

`$ llamacloud-prod pipelines:metadata delete-all`

**delete** `/api/v1/pipelines/{pipeline_id}/metadata`

Delete metadata for all files in a pipeline.

### Parameters

- `--pipeline-id: string`

### Example

```cli
llamacloud-prod pipelines:metadata delete-all \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```
