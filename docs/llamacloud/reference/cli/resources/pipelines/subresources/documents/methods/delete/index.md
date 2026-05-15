## Delete Pipeline Document

`$ llamacloud-prod pipelines:documents delete`

**delete** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Delete a document from a pipeline.
Initiates an async job that will:

1. Delete vectors from the vector store
1. Delete the document from MongoDB after vectors are successfully deleted

### Parameters

- `--pipeline-id: string`

- `--document-id: string`

### Example

```cli
llamacloud-prod pipelines:documents delete \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --document-id document_id
```
