## Delete File

`$ llamacloud-prod files delete`

**delete** `/api/v1/beta/files/{file_id}`

Delete a file from the project.

### Parameters

- `--file-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Example

```cli
llamacloud-prod files delete \
  --api-key 'My API Key' \
  --file-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```
