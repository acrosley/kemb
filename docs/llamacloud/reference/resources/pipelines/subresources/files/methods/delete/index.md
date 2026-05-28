## Delete Pipeline File

**delete** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Delete a file from a pipeline.

### Path Parameters

- `pipeline_id: string`

- `file_id: string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/pipelines/$PIPELINE_ID/files/$FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```
