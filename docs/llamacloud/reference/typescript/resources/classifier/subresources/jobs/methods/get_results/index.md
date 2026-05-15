## Get Classification Job Results

`client.classifier.jobs.getResults(stringclassifyJobID, JobGetResultsParamsquery?, RequestOptionsoptions?): JobGetResultsResponse`

**get** `/api/v1/classifier/jobs/{classify_job_id}/results`

Get the results of a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `classifyJobID: string`

- `query: JobGetResultsParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `JobGetResultsResponse`

  Response model for the classify endpoint following AIP-132 pagination standard.

  - `items: Array<Item>`

    The list of items.

    - `id: string`

      Unique identifier

    - `classify_job_id: string`

      The ID of the classify job

    - `created_at?: string | null`

      Creation datetime

    - `file_id?: string | null`

      The ID of the classified file

    - `result?: Result | null`

      Result of classifying a single file.

      - `confidence: number`

        Confidence score of the classification (0.0-1.0)

      - `reasoning: string`

        Step-by-step explanation of why this classification was chosen and the confidence score assigned

      - `type: string | null`

        The document type that best matches, or null if no match.

    - `updated_at?: string | null`

      Update datetime

  - `next_page_token?: string | null`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size?: number | null`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.classifier.jobs.getResults('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(response.items);
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
