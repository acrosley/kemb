# Split

## Create Split Job

`$ llamacloud-prod beta:split create`

**post** `/api/v1/beta/split/jobs`

Create a document split job.

### Parameters

- `--document-input: object { type, value }`

  Body param: Document to be split.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--configuration: optional object { categories, splitting_strategy }`

  Body param: Split configuration with categories and splitting strategy.

- `--configuration-id: optional string`

  Body param: Saved split configuration ID.

### Returns

- `BetaSplitNewResponse: object { id, categories, document_input, 8 more }`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: array of SplitCategory`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description: optional string`

      Optional description of what content belongs in this category.

  - `document_input: object { type, value }`

    Document that was split.

    - `type: string`

      Type of document input. Valid values are: file_id

    - `value: string`

      Document identifier.

  - `project_id: string`

    Project ID this job belongs to.

  - `status: string`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: string`

    User ID who created this job.

  - `configuration_id: optional string`

    Split configuration ID used for this job.

  - `created_at: optional string`

    Creation datetime

  - `error_message: optional string`

    Error message if the job failed.

  - `result: optional object { segments }`

    Result of a completed split job.

    - `segments: array of SplitSegmentResponse`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: array of number`

        1-indexed page numbers in this split.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:split create \
  --api-key 'My API Key' \
  --document-input '{type: type, value: value}'
```

#### Response

```json
{
  "id": "id",
  "categories": [
    {
      "name": "x",
      "description": "x"
    }
  ],
  "document_input": {
    "type": "type",
    "value": "value"
  },
  "project_id": "project_id",
  "status": "status",
  "user_id": "user_id",
  "configuration_id": "configuration_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "error_message": "error_message",
  "result": {
    "segments": [
      {
        "category": "category",
        "confidence_category": "confidence_category",
        "pages": [
          0
        ]
      }
    ]
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Split Jobs

`$ llamacloud-prod beta:split list`

**get** `/api/v1/beta/split/jobs`

List document split jobs.

### Parameters

- `--created-at-on-or-after: optional string`

  Include items created at or after this timestamp (inclusive)

- `--created-at-on-or-before: optional string`

  Include items created at or before this timestamp (inclusive)

- `--job-id: optional array of string`

  Filter by specific job IDs

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--status: optional "pending" or "processing" or "completed" or 2 more`

  Filter by job status (pending, processing, completed, failed, cancelled)

### Returns

- `SplitJobQueryResponse: object { items, next_page_token, total_size }`

  Beta paginated list of split jobs.

  - `items: array of object { id, categories, document_input, 8 more }`

    The list of items.

    - `id: string`

      Unique identifier for the split job.

    - `categories: array of SplitCategory`

      Categories used for splitting.

      - `name: string`

        Name of the category.

      - `description: optional string`

        Optional description of what content belongs in this category.

    - `document_input: object { type, value }`

      Document that was split.

      - `type: string`

        Type of document input. Valid values are: file_id

      - `value: string`

        Document identifier.

    - `project_id: string`

      Project ID this job belongs to.

    - `status: string`

      Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

    - `user_id: string`

      User ID who created this job.

    - `configuration_id: optional string`

      Split configuration ID used for this job.

    - `created_at: optional string`

      Creation datetime

    - `error_message: optional string`

      Error message if the job failed.

    - `result: optional object { segments }`

      Result of a completed split job.

      - `segments: array of SplitSegmentResponse`

        List of document segments.

        - `category: string`

          Category name this split belongs to.

        - `confidence_category: string`

          Categorical confidence level. Valid values are: high, medium, low.

        - `pages: array of number`

          1-indexed page numbers in this split.

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:split list \
  --api-key 'My API Key'
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "categories": [
        {
          "name": "x",
          "description": "x"
        }
      ],
      "document_input": {
        "type": "type",
        "value": "value"
      },
      "project_id": "project_id",
      "status": "status",
      "user_id": "user_id",
      "configuration_id": "configuration_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "result": {
        "segments": [
          {
            "category": "category",
            "confidence_category": "confidence_category",
            "pages": [
              0
            ]
          }
        ]
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Split Job

`$ llamacloud-prod beta:split get`

**get** `/api/v1/beta/split/jobs/{split_job_id}`

Get a document split job.

### Parameters

- `--split-job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaSplitGetResponse: object { id, categories, document_input, 8 more }`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: array of SplitCategory`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description: optional string`

      Optional description of what content belongs in this category.

  - `document_input: object { type, value }`

    Document that was split.

    - `type: string`

      Type of document input. Valid values are: file_id

    - `value: string`

      Document identifier.

  - `project_id: string`

    Project ID this job belongs to.

  - `status: string`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: string`

    User ID who created this job.

  - `configuration_id: optional string`

    Split configuration ID used for this job.

  - `created_at: optional string`

    Creation datetime

  - `error_message: optional string`

    Error message if the job failed.

  - `result: optional object { segments }`

    Result of a completed split job.

    - `segments: array of SplitSegmentResponse`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: array of number`

        1-indexed page numbers in this split.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:split get \
  --api-key 'My API Key' \
  --split-job-id split_job_id
```

#### Response

```json
{
  "id": "id",
  "categories": [
    {
      "name": "x",
      "description": "x"
    }
  ],
  "document_input": {
    "type": "type",
    "value": "value"
  },
  "project_id": "project_id",
  "status": "status",
  "user_id": "user_id",
  "configuration_id": "configuration_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "error_message": "error_message",
  "result": {
    "segments": [
      {
        "category": "category",
        "confidence_category": "confidence_category",
        "pages": [
          0
        ]
      }
    ]
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Domain Types

### Split Category

- `split_category: object { name, description }`

  Category definition for document splitting.

  - `name: string`

    Name of the category.

  - `description: optional string`

    Optional description of what content belongs in this category.

### Split Document Input

- `split_document_input: object { type, value }`

  Document input specification for beta API.

  - `type: string`

    Type of document input. Valid values are: file_id

  - `value: string`

    Document identifier.

### Split Result Response

- `split_result_response: object { segments }`

  Result of a completed split job.

  - `segments: array of SplitSegmentResponse`

    List of document segments.

    - `category: string`

      Category name this split belongs to.

    - `confidence_category: string`

      Categorical confidence level. Valid values are: high, medium, low.

    - `pages: array of number`

      1-indexed page numbers in this split.

### Split Segment Response

- `split_segment_response: object { category, confidence_category, pages }`

  A segment of the split document.

  - `category: string`

    Category name this split belongs to.

  - `confidence_category: string`

    Categorical confidence level. Valid values are: high, medium, low.

  - `pages: array of number`

    1-indexed page numbers in this split.
