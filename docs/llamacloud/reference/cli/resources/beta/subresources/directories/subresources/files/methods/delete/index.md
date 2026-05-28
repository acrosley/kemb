## Delete Directory File

`$ llamacloud-prod beta:directories:files delete`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `--directory-id: string`

  Path param

- `--directory-file-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Example

```cli
llamacloud-prod beta:directories:files delete \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --directory-file-id directory_file_id
```
