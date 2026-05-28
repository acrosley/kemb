## Sync Pipeline Document

`$ llamacloud-prod pipelines:documents sync`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--document-id: string`

### Returns

- `PipelineDocumentSyncResponse: unknown`

### Example

```cli
llamacloud-prod pipelines:documents sync \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --document-id document_id
```

#### Response

```json
{}
```
