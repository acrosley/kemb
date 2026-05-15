## Get Pipeline File Status

`pipelines.files.get_status(strfile_id, FileGetStatusParams**kwargs)  -> ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/files/{file_id}/status`

Get status of a file for a pipeline.

### Parameters

- `pipeline_id: str`

- `file_id: str`

### Returns

- `class ManagedIngestionStatusResponse: …`

  - `status: Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", 3 more]`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date: Optional[datetime]`

    Date of the deployment.

  - `effective_at: Optional[datetime]`

    When the status is effective

  - `error: Optional[List[Error]]`

    List of errors that occurred during ingestion.

    - `job_id: str`

      ID of the job that failed.

    - `message: str`

      List of errors that occurred during ingestion.

    - `step: Literal["MANAGED_INGESTION", "DATA_SOURCE", "FILE_UPDATER", 4 more]`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id: Optional[str]`

    ID of the latest job.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
managed_ingestion_status_response = client.pipelines.files.get_status(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(managed_ingestion_status_response.job_id)
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
