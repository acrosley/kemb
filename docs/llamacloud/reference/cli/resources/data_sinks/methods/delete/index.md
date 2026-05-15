## Delete Data Sink

`$ llamacloud-prod data-sinks delete`

**delete** `/api/v1/data-sinks/{data_sink_id}`

Delete a data sink by ID.

### Parameters

- `--data-sink-id: string`

### Example

```cli
llamacloud-prod data-sinks delete \
  --api-key 'My API Key' \
  --data-sink-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```
