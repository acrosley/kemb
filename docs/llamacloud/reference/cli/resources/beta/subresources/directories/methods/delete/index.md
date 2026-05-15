## Delete Directory

`$ llamacloud-prod beta:directories delete`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `--directory-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Example

```cli
llamacloud-prod beta:directories delete \
  --api-key 'My API Key' \
  --directory-id directory_id
```
