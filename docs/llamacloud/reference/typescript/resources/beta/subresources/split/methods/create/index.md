## Create Split Job

`client.beta.split.create(SplitCreateParamsparams, RequestOptionsoptions?): SplitCreateResponse`

**post** `/api/v1/beta/split/jobs`

Create a document split job.

### Parameters

- `params: SplitCreateParams`

  - `document_input: SplitDocumentInput`

    Body param: Document to be split.

    - `type: string`

      Type of document input. Valid values are: file_id

    - `value: string`

      Document identifier.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `configuration?: Configuration | null`

    Body param: Split configuration with categories and splitting strategy.

    - `categories: Array<SplitCategory>`

      Categories to split documents into.

      - `name: string`

        Name of the category.

      - `description?: string | null`

        Optional description of what content belongs in this category.

    - `splitting_strategy?: SplittingStrategy`

      Strategy for splitting documents.

      - `allow_uncategorized?: "include" | "forbid" | "omit"`

        Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

        - `"include"`

        - `"forbid"`

        - `"omit"`

  - `configuration_id?: string | null`

    Body param: Saved split configuration ID.

### Returns

- `SplitCreateResponse`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: Array<SplitCategory>`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description?: string | null`

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

  - `configuration_id?: string | null`

    Split configuration ID used for this job.

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error message if the job failed.

  - `result?: SplitResultResponse | null`

    Result of a completed split job.

    - `segments: Array<SplitSegmentResponse>`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: Array<number>`

        1-indexed page numbers in this split.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const split = await client.beta.split.create({ document_input: { type: 'type', value: 'value' } });

console.log(split.id);
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
