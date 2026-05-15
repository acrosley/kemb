## Get Pipeline Status

`client.pipelines.getStatus(stringpipelineID, PipelineGetStatusParamsquery?, RequestOptionsoptions?): ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/status`

Get the ingestion status of a managed pipeline.

Returns document counts, sync progress, and the last
effective timestamp. Only available for managed pipelines.

### Parameters

- `pipelineID: string`

- `query: PipelineGetStatusParams`

  - `full_details?: boolean | null`

### Returns

- `ManagedIngestionStatusResponse`

  - `status: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date?: string | null`

    Date of the deployment.

  - `effective_at?: string | null`

    When the status is effective

  - `error?: Array<Error> | null`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" | "DATA_SOURCE" | "FILE_UPDATER" | 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id?: string | null`

    ID of the latest job.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const managedIngestionStatusResponse = await client.pipelines.getStatus(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(managedIngestionStatusResponse.job_id);
```

#### Response

```json
{
  "status": "NOT_STARTED",
  "deployment_date": "2019-12-27T18:11:19.117Z",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error": [
    {
      "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "message": "message",
      "step": "MANAGED_INGESTION"
    }
  ],
  "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```
