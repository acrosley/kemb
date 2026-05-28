## Delete Pipeline

**delete** `/api/v1/pipelines/{pipeline_id}`

Delete a pipeline and all associated resources.

Removes pipeline files, data sources, and vector store data.
This operation is irreversible.

### Path Parameters

- `pipeline_id: string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/pipelines/$PIPELINE_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```
