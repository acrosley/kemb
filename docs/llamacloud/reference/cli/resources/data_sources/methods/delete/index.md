## Delete Data Source

`$ llamacloud-prod data-sources delete`

**delete** `/api/v1/data-sources/{data_source_id}`

Delete a data source by ID.

### Parameters

- `--data-source-id: string`

### Example

```cli
llamacloud-prod data-sources delete \
  --api-key 'My API Key' \
  --data-source-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```
