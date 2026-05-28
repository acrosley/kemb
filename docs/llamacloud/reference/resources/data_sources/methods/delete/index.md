## Delete Data Source

**delete** `/api/v1/data-sources/{data_source_id}`

Delete a data source by ID.

### Path Parameters

- `data_source_id: string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/data-sources/$DATA_SOURCE_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```
