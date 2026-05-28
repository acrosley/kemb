## Get Pipeline File Status Counts

**get** `/api/v1/pipelines/{pipeline_id}/files/status-counts`

Get files for a pipeline.

### Path Parameters

- `pipeline_id: string`

### Query Parameters

- `data_source_id: optional string`

- `only_manually_uploaded: optional boolean`

### Cookie Parameters

- `session: optional string`

### Returns

- `counts: map[number]`

  The counts of files by status

- `total_count: number`

  The total number of files

- `data_source_id: optional string`

  The ID of the data source that the files belong to

- `only_manually_uploaded: optional boolean`

  Whether to only count manually uploaded files

- `pipeline_id: optional string`

  The ID of the pipeline that the files belong to

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/pipelines/$PIPELINE_ID/files/status-counts \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{
  "counts": {
    "foo": 0
  },
  "total_count": 0,
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "only_manually_uploaded": true,
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```
