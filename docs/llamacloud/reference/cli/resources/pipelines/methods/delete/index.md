## Delete Pipeline

`$ llamacloud-prod pipelines delete`

**delete** `/api/v1/pipelines/{pipeline_id}`

Delete a pipeline and all associated resources.

Removes pipeline files, data sources, and vector store data.
This operation is irreversible.

### Parameters

- `--pipeline-id: string`

### Example

```cli
llamacloud-prod pipelines delete \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```
