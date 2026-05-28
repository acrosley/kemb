## Delete Data Sink

**delete** `/api/v1/data-sinks/{data_sink_id}`

Delete a data sink by ID.

### Path Parameters

- `data_sink_id: string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/data-sinks/$DATA_SINK_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```
