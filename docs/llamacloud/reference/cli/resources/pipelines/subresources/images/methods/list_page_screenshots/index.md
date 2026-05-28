## List File Page Screenshots

`$ llamacloud-prod pipelines:images list-page-screenshots`

**get** `/api/v1/files/{id}/page_screenshots`

List metadata for all screenshots of pages from a file.

### Parameters

- `--id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `Response List File Page Screenshots Api V1 Files  Id  Page Screenshots Get: array of object { file_id, image_size, page_index, metadata }`

  - `file_id: string`

    The ID of the file that the page screenshot was taken from

  - `image_size: number`

    The size of the image in bytes

  - `page_index: number`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata: optional map[unknown]`

    Metadata for the screenshot

### Example

```cli
llamacloud-prod pipelines:images list-page-screenshots \
  --api-key 'My API Key' \
  --id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```

#### Response

```json
[
  {
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "image_size": 0,
    "page_index": 0,
    "metadata": {
      "foo": "bar"
    }
  }
]
```
