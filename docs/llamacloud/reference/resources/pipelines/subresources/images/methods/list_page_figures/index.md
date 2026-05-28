## List File Pages Figures

**get** `/api/v1/files/{id}/page-figures`

List metadata for all figures from all pages of a file.

### Path Parameters

- `id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

- `confidence: number`

  The confidence of the figure

- `figure_name: string`

  The name of the figure

- `figure_size: number`

  The size of the figure in bytes

- `file_id: string`

  The ID of the file that the figure was taken from

- `page_index: number`

  The index of the page for which the figure is taken (0-indexed)

- `is_likely_noise: optional boolean`

  Whether the figure is likely to be noise

- `metadata: optional map[unknown]`

  Metadata for the figure

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/files/$ID/page-figures \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
[
  {
    "confidence": 0,
    "figure_name": "figure_name",
    "figure_size": 0,
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "page_index": 0,
    "is_likely_noise": true,
    "metadata": {
      "foo": "bar"
    }
  }
]
```
