## Create Split Job

**post** `/api/v1/beta/split/jobs`

Create a document split job.

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `document_input: SplitDocumentInput`

  Document to be split.

  - `type: string`

    Type of document input. Valid values are: file_id

  - `value: string`

    Document identifier.

- `configuration: optional object { categories, splitting_strategy }`

  Split configuration with categories and splitting strategy.

  - `categories: array of SplitCategory`

    Categories to split documents into.

    - `name: string`

      Name of the category.

    - `description: optional string`

      Optional description of what content belongs in this category.

  - `splitting_strategy: optional object { allow_uncategorized }`

    Strategy for splitting documents.

    - `allow_uncategorized: optional "include" or "forbid" or "omit"`

      Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

      - `"include"`

      - `"forbid"`

      - `"omit"`

- `configuration_id: optional string`

  Saved split configuration ID.

### Returns

- `id: string`

  Unique identifier for the split job.

- `categories: array of SplitCategory`

  Categories used for splitting.

  - `name: string`

    Name of the category.

  - `description: optional string`

    Optional description of what content belongs in this category.

- `document_input: SplitDocumentInput`

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

- `result: optional SplitResultResponse`

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

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "document_input": {
            "type": "type",
            "value": "value"
          }
        }'
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
