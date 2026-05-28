## Get Classification Job Results

`$ llamacloud-prod classifier:jobs get-results`

**get** `/api/v1/classifier/jobs/{classify_job_id}/results`

Get the results of a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--classify-job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `ClassifierJobGetResultsResponse: object { items, next_page_token, total_size }`

  Response model for the classify endpoint following AIP-132 pagination standard.

  - `items: array of object { id, classify_job_id, created_at, 3 more }`

    The list of items.

    - `id: string`

      Unique identifier

    - `classify_job_id: string`

      The ID of the classify job

    - `created_at: optional string`

      Creation datetime

    - `file_id: optional string`

      The ID of the classified file

    - `result: optional object { confidence, reasoning, type }`

      Result of classifying a single file.

      - `confidence: number`

        Confidence score of the classification (0.0-1.0)

      - `reasoning: string`

        Step-by-step explanation of why this classification was chosen and the confidence score assigned

      - `type: string`

        The document type that best matches, or null if no match.

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod classifier:jobs get-results \
  --api-key 'My API Key' \
  --classify-job-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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
