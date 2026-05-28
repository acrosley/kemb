## Delete Retriever

`$ llamacloud-prod retrievers delete`

**delete** `/api/v1/retrievers/{retriever_id}`

Delete a Retriever by ID.

### Parameters

- `--retriever-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Example

```cli
llamacloud-prod retrievers delete \
  --api-key 'My API Key' \
  --retriever-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```
