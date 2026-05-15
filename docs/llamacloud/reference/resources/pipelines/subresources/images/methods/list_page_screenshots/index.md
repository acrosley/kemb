## List File Page Screenshots

**get** `/api/v1/files/{id}/page_screenshots`

List metadata for all screenshots of pages from a file.

### Path Parameters

- `id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

- `file_id: string`

  The ID of the file that the page screenshot was taken from

- `image_size: number`

  The size of the image in bytes

- `page_index: number`

  The index of the page for which the screenshot is taken (0-indexed)

- `metadata: optional map[unknown]`

  Metadata for the screenshot

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/files/$ID/page_screenshots \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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
