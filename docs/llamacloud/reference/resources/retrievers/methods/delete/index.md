## Delete Retriever

**delete** `/api/v1/retrievers/{retriever_id}`

Delete a Retriever by ID.

### Path Parameters

- `retriever_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/retrievers/$RETRIEVER_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```
