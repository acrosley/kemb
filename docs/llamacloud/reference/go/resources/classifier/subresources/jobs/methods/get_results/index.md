## Get Classification Job Results

`client.Classifier.Jobs.GetResults(ctx, classifyJobID, query) (*ClassifierJobGetResultsResponse, error)`

**get** `/api/v1/classifier/jobs/{classify_job_id}/results`

Get the results of a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `classifyJobID string`

- `query ClassifierJobGetResultsParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type ClassifierJobGetResultsResponse struct{…}`

  Response model for the classify endpoint following AIP-132 pagination standard.

  - `Items []ClassifierJobGetResultsResponseItem`

    The list of items.

    - `ID string`

      Unique identifier

    - `ClassifyJobID string`

      The ID of the classify job

    - `CreatedAt Time`

      Creation datetime

    - `FileID string`

      The ID of the classified file

    - `Result ClassifierJobGetResultsResponseItemResult`

      Result of classifying a single file.

      - `Confidence float64`

        Confidence score of the classification (0.0-1.0)

      - `Reasoning string`

        Step-by-step explanation of why this classification was chosen and the confidence score assigned

      - `Type string`

        The document type that best matches, or null if no match.

    - `UpdatedAt Time`

      Update datetime

  - `NextPageToken string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `TotalSize int64`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  response, err := client.Classifier.Jobs.GetResults(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.ClassifierJobGetResultsParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Items)
}
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
