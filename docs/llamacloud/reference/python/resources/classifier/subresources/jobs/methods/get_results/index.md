## Get Classification Job Results

`classifier.jobs.get_results(strclassify_job_id, JobGetResultsParams**kwargs)  -> JobGetResultsResponse`

**get** `/api/v1/classifier/jobs/{classify_job_id}/results`

Get the results of a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `classify_job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class JobGetResultsResponse: …`

  Response model for the classify endpoint following AIP-132 pagination standard.

  - `items: List[Item]`

    The list of items.

    - `id: str`

      Unique identifier

    - `classify_job_id: str`

      The ID of the classify job

    - `created_at: Optional[datetime]`

      Creation datetime

    - `file_id: Optional[str]`

      The ID of the classified file

    - `result: Optional[ItemResult]`

      Result of classifying a single file.

      - `confidence: float`

        Confidence score of the classification (0.0-1.0)

      - `reasoning: str`

        Step-by-step explanation of why this classification was chosen and the confidence score assigned

      - `type: Optional[str]`

        The document type that best matches, or null if no match.

    - `updated_at: Optional[datetime]`

      Update datetime

  - `next_page_token: Optional[str]`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: Optional[int]`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.classifier.jobs.get_results(
    classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response.items)
```

#### Response

```json
{
  "items": [
    {
      "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "classify_job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "created_at": "2019-12-27T18:11:19.117Z",
      "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "result": {
        "confidence": 0,
        "reasoning": "reasoning",
        "type": "type"
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
