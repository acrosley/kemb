## Get Pipeline File Status Counts

`client.pipelines.files.getStatusCounts(stringpipelineID, FileGetStatusCountsParamsquery?, RequestOptionsoptions?): FileGetStatusCountsResponse`

**get** `/api/v1/pipelines/{pipeline_id}/files/status-counts`

Get files for a pipeline.

### Parameters

- `pipelineID: string`

- `query: FileGetStatusCountsParams`

  - `data_source_id?: string | null`

  - `only_manually_uploaded?: boolean`

### Returns

- `FileGetStatusCountsResponse`

  - `counts: Record<string, number>`

    The counts of files by status

  - `total_count: number`

    The total number of files

  - `data_source_id?: string | null`

    The ID of the data source that the files belong to

  - `only_manually_uploaded?: boolean`

    Whether to only count manually uploaded files

  - `pipeline_id?: string | null`

    The ID of the pipeline that the files belong to

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.files.getStatusCounts(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response.data_source_id);
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
