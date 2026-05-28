## Get Pipeline File Status Counts

`$ llamacloud-prod pipelines:files get-status-counts`

**get** `/api/v1/pipelines/{pipeline_id}/files/status-counts`

Get files for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--data-source-id: optional string`

- `--only-manually-uploaded: optional boolean`

### Returns

- `PipelineFileGetStatusCountsResponse: object { counts, total_count, data_source_id, 2 more }`

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

```cli
llamacloud-prod pipelines:files get-status-counts \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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
