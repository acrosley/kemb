# Extract

## Create Extract Job

`client.extract.create(ExtractCreateParamsparams, RequestOptionsoptions?): ExtractV2Job`

**post** `/api/v2/extract`

Create an extraction job.

Extracts structured data from a document using either a saved
configuration or an inline JSON Schema.

## Input

Provide exactly one of:

- `configuration_id` — reference a saved extraction config
- `configuration` — inline configuration with a `data_schema`

## Document input

Set `file_input` to a file ID (`dfl-...`) or a
completed parse job ID (`pjb-...`).

The job runs asynchronously. Poll `GET /extract/{job_id}` or
register a webhook to monitor completion.

### Parameters

- `params: ExtractCreateParams`

  - `file_input: string`

    Body param: File ID or parse job ID to extract from

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `configuration?: ExtractConfiguration | null`

    Body param: Extract configuration combining parse and extract settings.

    - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources?: boolean`

      Include citations in results

    - `confidence_scores?: boolean`

      Include confidence scores in results

    - `extract_version?: string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages?: number | null`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id?: string | null`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier?: string | null`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt?: string | null`

      Custom system prompt to guide extraction behavior

    - `target_pages?: string | null`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier?: "cost_effective" | "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id?: string | null`

    Body param: Saved configuration ID

  - `webhook_configurations?: Array<WebhookConfiguration> | null`

    Body param: Outbound webhook endpoints to notify on job status changes

    - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

      Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

      - `"extract.pending"`

      - `"extract.success"`

      - `"extract.error"`

      - `"extract.partial_success"`

      - `"extract.cancelled"`

      - `"parse.pending"`

      - `"parse.running"`

      - `"parse.success"`

      - `"parse.error"`

      - `"parse.partial_success"`

      - `"parse.cancelled"`

      - `"classify.pending"`

      - `"classify.success"`

      - `"classify.error"`

      - `"classify.partial_success"`

      - `"classify.cancelled"`

      - `"unmapped_event"`

    - `webhook_headers?: Record<string, string> | null`

      Custom HTTP headers sent with each webhook request (e.g. auth tokens)

    - `webhook_output_format?: string | null`

      Response format sent to the webhook: 'string' (default) or 'json'

    - `webhook_url?: string | null`

      URL to receive webhook POST notifications

### Returns

- `ExtractV2Job`

  An extraction job.

  - `id: string`

    Unique job identifier (job_id)

  - `created_at: string`

    Creation timestamp

  - `file_input: string`

    File ID or parse job ID that was extracted

  - `project_id: string`

    Project this job belongs to

  - `status: string`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `updated_at: string`

    Last update timestamp

  - `configuration?: ExtractConfiguration | null`

    Extract configuration combining parse and extract settings.

    - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources?: boolean`

      Include citations in results

    - `confidence_scores?: boolean`

      Include confidence scores in results

    - `extract_version?: string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages?: number | null`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id?: string | null`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier?: string | null`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt?: string | null`

      Custom system prompt to guide extraction behavior

    - `target_pages?: string | null`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier?: "cost_effective" | "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id?: string | null`

    Saved extract configuration ID used for this job, if any

  - `error_message?: string | null`

    Error details when status is FAILED

  - `extract_metadata?: ExtractJobMetadata | null`

    Extraction metadata.

    - `field_metadata?: ExtractedFieldMetadata | null`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `page_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

        Per-page metadata when extraction_target is per_page

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `row_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

        Per-row metadata when extraction_target is per_table_row

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

    - `parse_job_id?: string | null`

      Reference to the ParseJob ID used for parsing

    - `parse_tier?: string | null`

      Parse tier used for parsing the document

  - `extract_result?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>>`

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

  - `metadata?: Metadata | null`

    Job-level metadata.

    - `usage?: ExtractJobUsage | null`

      Extraction usage metrics.

      - `num_document_tokens?: number | null`

        Number of document tokens

      - `num_output_tokens?: number | null`

        Number of output tokens

      - `num_pages_extracted?: number | null`

        Number of pages extracted

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const extractV2Job = await client.extract.create({
  file_input: 'dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee',
});

console.log(extractV2Job.id);
```

#### Response

```json
{
  "id": "ext-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "created_at": "2019-12-27T18:11:19.117Z",
  "file_input": "dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "status": "COMPLETED",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "configuration": {
    "data_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "cite_sources": true,
    "confidence_scores": true,
    "extract_version": "latest",
    "extraction_target": "per_doc",
    "max_pages": 10,
    "parse_config_id": "cfg-11111111-2222-3333-4444-555555555555",
    "parse_tier": "fast",
    "system_prompt": "Extract all monetary values in USD. If a currency is not specified, assume USD.",
    "target_pages": "1,3,5-7",
    "tier": "cost_effective"
  },
  "configuration_id": "cfg-11111111-2222-3333-4444-555555555555",
  "error_message": "error_message",
  "extract_metadata": {
    "field_metadata": {
      "document_metadata": {
        "items": [
          {
            "amount": {
              "citation": [
                {
                  "matching_text": "$10.00",
                  "page": 1
                }
              ],
              "confidence": 1
            },
            "description": {
              "citation": [
                {
                  "matching_text": "$10/month",
                  "page": 1
                }
              ],
              "confidence": 0.998
            }
          }
        ],
        "total": {
          "citation": "bar",
          "confidence": "bar"
        },
        "vendor": {
          "citation": "bar",
          "confidence": "bar",
          "extraction_confidence": "bar",
          "parsing_confidence": "bar"
        }
      },
      "page_metadata": [
        {
          "foo": {
            "foo": "bar"
          }
        }
      ],
      "row_metadata": [
        {
          "foo": {
            "foo": "bar"
          }
        }
      ]
    },
    "parse_job_id": "parse_job_id",
    "parse_tier": "parse_tier"
  },
  "extract_result": {
    "foo": {
      "foo": "bar"
    }
  },
  "metadata": {
    "usage": {
      "num_document_tokens": 0,
      "num_output_tokens": 0,
      "num_pages_extracted": 0
    }
  }
}
```

## List Extract Jobs

`client.extract.list(ExtractListParamsquery?, RequestOptionsoptions?): PaginatedCursor<ExtractV2Job>`

**get** `/api/v2/extract`

List extraction jobs with optional filtering and pagination.

Filter by `configuration_id`, `status`, `file_input`,
or creation date range. Results are returned newest-first.
Use `expand=configuration` to include the full configuration used,
and `expand=extract_metadata` for per-field metadata.

### Parameters

- `query: ExtractListParams`

  - `configuration_id?: string | null`

    Filter by configuration ID

  - `created_at_on_or_after?: string | null`

    Include items created at or after this timestamp (inclusive)

  - `created_at_on_or_before?: string | null`

    Include items created at or before this timestamp (inclusive)

  - `document_input_type?: string | null`

    Filter by document input type (file_id or parse_job_id)

  - `document_input_value?: string | null`

    Deprecated: use file_input instead

  - `expand?: Array<string>`

    Additional fields to include: configuration, extract_metadata

  - `file_input?: string | null`

    Filter by file input value

  - `job_ids?: Array<string> | null`

    Filter by specific job IDs

  - `organization_id?: string | null`

  - `page_size?: number | null`

    Number of items per page

  - `page_token?: string | null`

    Token for pagination

  - `project_id?: string | null`

  - `status?: "PENDING" | "THROTTLED" | "RUNNING" | 3 more | null`

    Filter by status

    - `"PENDING"`

    - `"THROTTLED"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

### Returns

- `ExtractV2Job`

  An extraction job.

  - `id: string`

    Unique job identifier (job_id)

  - `created_at: string`

    Creation timestamp

  - `file_input: string`

    File ID or parse job ID that was extracted

  - `project_id: string`

    Project this job belongs to

  - `status: string`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `updated_at: string`

    Last update timestamp

  - `configuration?: ExtractConfiguration | null`

    Extract configuration combining parse and extract settings.

    - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources?: boolean`

      Include citations in results

    - `confidence_scores?: boolean`

      Include confidence scores in results

    - `extract_version?: string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages?: number | null`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id?: string | null`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier?: string | null`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt?: string | null`

      Custom system prompt to guide extraction behavior

    - `target_pages?: string | null`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier?: "cost_effective" | "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id?: string | null`

    Saved extract configuration ID used for this job, if any

  - `error_message?: string | null`

    Error details when status is FAILED

  - `extract_metadata?: ExtractJobMetadata | null`

    Extraction metadata.

    - `field_metadata?: ExtractedFieldMetadata | null`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `page_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

        Per-page metadata when extraction_target is per_page

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `row_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

        Per-row metadata when extraction_target is per_table_row

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

    - `parse_job_id?: string | null`

      Reference to the ParseJob ID used for parsing

    - `parse_tier?: string | null`

      Parse tier used for parsing the document

  - `extract_result?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>>`

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

  - `metadata?: Metadata | null`

    Job-level metadata.

    - `usage?: ExtractJobUsage | null`

      Extraction usage metrics.

      - `num_document_tokens?: number | null`

        Number of document tokens

      - `num_output_tokens?: number | null`

        Number of output tokens

      - `num_pages_extracted?: number | null`

        Number of pages extracted

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const extractV2Job of client.extract.list()) {
  console.log(extractV2Job.id);
}
```

#### Response

```json
{
  "items": [
    {
      "id": "ext-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "created_at": "2019-12-27T18:11:19.117Z",
      "file_input": "dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "status": "COMPLETED",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "configuration": {
        "data_schema": {
          "foo": {
            "foo": "bar"
          }
        },
        "cite_sources": true,
        "confidence_scores": true,
        "extract_version": "latest",
        "extraction_target": "per_doc",
        "max_pages": 10,
        "parse_config_id": "cfg-11111111-2222-3333-4444-555555555555",
        "parse_tier": "fast",
        "system_prompt": "Extract all monetary values in USD. If a currency is not specified, assume USD.",
        "target_pages": "1,3,5-7",
        "tier": "cost_effective"
      },
      "configuration_id": "cfg-11111111-2222-3333-4444-555555555555",
      "error_message": "error_message",
      "extract_metadata": {
        "field_metadata": {
          "document_metadata": {
            "items": [
              {
                "amount": {
                  "citation": [
                    {
                      "matching_text": "$10.00",
                      "page": 1
                    }
                  ],
                  "confidence": 1
                },
                "description": {
                  "citation": [
                    {
                      "matching_text": "$10/month",
                      "page": 1
                    }
                  ],
                  "confidence": 0.998
                }
              }
            ],
            "total": {
              "citation": "bar",
              "confidence": "bar"
            },
            "vendor": {
              "citation": "bar",
              "confidence": "bar",
              "extraction_confidence": "bar",
              "parsing_confidence": "bar"
            }
          },
          "page_metadata": [
            {
              "foo": {
                "foo": "bar"
              }
            }
          ],
          "row_metadata": [
            {
              "foo": {
                "foo": "bar"
              }
            }
          ]
        },
        "parse_job_id": "parse_job_id",
        "parse_tier": "parse_tier"
      },
      "extract_result": {
        "foo": {
          "foo": "bar"
        }
      },
      "metadata": {
        "usage": {
          "num_document_tokens": 0,
          "num_output_tokens": 0,
          "num_pages_extracted": 0
        }
      }
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Extract Job

`client.extract.get(stringjobID, ExtractGetParamsquery?, RequestOptionsoptions?): ExtractV2Job`

**get** `/api/v2/extract/{job_id}`

Get a single extraction job by ID.

Returns the job status and results when complete.
Use `expand=configuration` to include the full configuration used,
and `expand=extract_metadata` for per-field metadata.

### Parameters

- `jobID: string`

- `query: ExtractGetParams`

  - `expand?: Array<string>`

    Additional fields to include: configuration, extract_metadata

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ExtractV2Job`

  An extraction job.

  - `id: string`

    Unique job identifier (job_id)

  - `created_at: string`

    Creation timestamp

  - `file_input: string`

    File ID or parse job ID that was extracted

  - `project_id: string`

    Project this job belongs to

  - `status: string`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `updated_at: string`

    Last update timestamp

  - `configuration?: ExtractConfiguration | null`

    Extract configuration combining parse and extract settings.

    - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources?: boolean`

      Include citations in results

    - `confidence_scores?: boolean`

      Include confidence scores in results

    - `extract_version?: string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages?: number | null`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id?: string | null`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier?: string | null`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt?: string | null`

      Custom system prompt to guide extraction behavior

    - `target_pages?: string | null`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier?: "cost_effective" | "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id?: string | null`

    Saved extract configuration ID used for this job, if any

  - `error_message?: string | null`

    Error details when status is FAILED

  - `extract_metadata?: ExtractJobMetadata | null`

    Extraction metadata.

    - `field_metadata?: ExtractedFieldMetadata | null`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `page_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

        Per-page metadata when extraction_target is per_page

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `row_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

        Per-row metadata when extraction_target is per_table_row

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

    - `parse_job_id?: string | null`

      Reference to the ParseJob ID used for parsing

    - `parse_tier?: string | null`

      Parse tier used for parsing the document

  - `extract_result?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>>`

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

  - `metadata?: Metadata | null`

    Job-level metadata.

    - `usage?: ExtractJobUsage | null`

      Extraction usage metrics.

      - `num_document_tokens?: number | null`

        Number of document tokens

      - `num_output_tokens?: number | null`

        Number of output tokens

      - `num_pages_extracted?: number | null`

        Number of pages extracted

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const extractV2Job = await client.extract.get('job_id');

console.log(extractV2Job.id);
```

#### Response

```json
{
  "id": "ext-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "created_at": "2019-12-27T18:11:19.117Z",
  "file_input": "dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "status": "COMPLETED",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "configuration": {
    "data_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "cite_sources": true,
    "confidence_scores": true,
    "extract_version": "latest",
    "extraction_target": "per_doc",
    "max_pages": 10,
    "parse_config_id": "cfg-11111111-2222-3333-4444-555555555555",
    "parse_tier": "fast",
    "system_prompt": "Extract all monetary values in USD. If a currency is not specified, assume USD.",
    "target_pages": "1,3,5-7",
    "tier": "cost_effective"
  },
  "configuration_id": "cfg-11111111-2222-3333-4444-555555555555",
  "error_message": "error_message",
  "extract_metadata": {
    "field_metadata": {
      "document_metadata": {
        "items": [
          {
            "amount": {
              "citation": [
                {
                  "matching_text": "$10.00",
                  "page": 1
                }
              ],
              "confidence": 1
            },
            "description": {
              "citation": [
                {
                  "matching_text": "$10/month",
                  "page": 1
                }
              ],
              "confidence": 0.998
            }
          }
        ],
        "total": {
          "citation": "bar",
          "confidence": "bar"
        },
        "vendor": {
          "citation": "bar",
          "confidence": "bar",
          "extraction_confidence": "bar",
          "parsing_confidence": "bar"
        }
      },
      "page_metadata": [
        {
          "foo": {
            "foo": "bar"
          }
        }
      ],
      "row_metadata": [
        {
          "foo": {
            "foo": "bar"
          }
        }
      ]
    },
    "parse_job_id": "parse_job_id",
    "parse_tier": "parse_tier"
  },
  "extract_result": {
    "foo": {
      "foo": "bar"
    }
  },
  "metadata": {
    "usage": {
      "num_document_tokens": 0,
      "num_output_tokens": 0,
      "num_pages_extracted": 0
    }
  }
}
```

## Delete Extract Job

`client.extract.delete(stringjobID, ExtractDeleteParamsparams?, RequestOptionsoptions?): ExtractDeleteResponse`

**delete** `/api/v2/extract/{job_id}`

Delete an extraction job and its results.

### Parameters

- `jobID: string`

- `params: ExtractDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ExtractDeleteResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const extract = await client.extract.delete('job_id');

console.log(extract);
```

#### Response

```json
{}
```

## Validate Extraction Schema

`client.extract.validateSchema(ExtractValidateSchemaParamsbody, RequestOptionsoptions?): ExtractV2SchemaValidateResponse`

**post** `/api/v2/extract/schema/validation`

Validate a JSON schema for extraction.

### Parameters

- `body: ExtractValidateSchemaParams`

  - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

    JSON Schema to validate for use with extract jobs

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Returns

- `ExtractV2SchemaValidateResponse`

  Response schema for schema validation.

  - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

    Validated JSON Schema, ready for use in extract jobs

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const extractV2SchemaValidateResponse = await client.extract.validateSchema({
  data_schema: { foo: { foo: 'bar' } },
});

console.log(extractV2SchemaValidateResponse.data_schema);
```

#### Response

```json
{
  "data_schema": {
    "foo": {
      "foo": "bar"
    }
  }
}
```

## Generate Extraction Schema

`client.extract.generateSchema(ExtractGenerateSchemaParamsparams, RequestOptionsoptions?): ConfigurationCreate`

**post** `/api/v2/extract/schema/generate`

Generate a JSON schema and return a product configuration request.

### Parameters

- `params: ExtractGenerateSchemaParams`

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `data_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Body param: Optional schema to validate, refine, or extend

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `file_id?: string | null`

    Body param: Optional file ID to analyze for schema generation

  - `name?: string | null`

    Body param: Name for the generated configuration (auto-generated if omitted)

  - `prompt?: string | null`

    Body param: Natural language description of the data structure to extract

### Returns

- `ConfigurationCreate`

  Request body for creating a product configuration.

  - `name: string`

    Human-readable name for this configuration.

  - `parameters: SplitV1Parameters | ExtractV2Parameters | ClassifyV2Parameters | 3 more`

    Product-specific configuration parameters.

    - `SplitV1Parameters`

      Typed parameters for a *split v1* product configuration.

      - `categories: Array<SplitCategory>`

        Categories to split documents into.

        - `name: string`

          Name of the category.

        - `description?: string | null`

          Optional description of what content belongs in this category.

      - `product_type: "split_v1"`

        Product type.

        - `"split_v1"`

      - `splitting_strategy?: SplittingStrategy`

        Strategy for splitting documents.

        - `allow_uncategorized?: "include" | "forbid" | "omit"`

          Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

          - `"include"`

          - `"forbid"`

          - `"omit"`

    - `ExtractV2Parameters`

      Typed parameters for an *extract v2* product configuration.

      - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

        JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `product_type: "extract_v2"`

        Product type.

        - `"extract_v2"`

      - `cite_sources?: boolean`

        Include citations in results

      - `confidence_scores?: boolean`

        Include confidence scores in results

      - `extract_version?: string`

        Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

      - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

        Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

        - `"per_doc"`

        - `"per_page"`

        - `"per_table_row"`

      - `max_pages?: number | null`

        Maximum number of pages to process. Omit for no limit.

      - `parse_config_id?: string | null`

        Saved parse configuration ID to control how the document is parsed before extraction

      - `parse_tier?: string | null`

        Parse tier to use before extraction. Defaults to the extract tier if not specified.

      - `system_prompt?: string | null`

        Custom system prompt to guide extraction behavior

      - `target_pages?: string | null`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

      - `tier?: "cost_effective" | "agentic"`

        Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

        - `"cost_effective"`

        - `"agentic"`

    - `ClassifyV2Parameters`

      Typed parameters for a *classify v2* product configuration.

      - `product_type: "classify_v2"`

        Product type.

        - `"classify_v2"`

      - `rules: Array<Rule>`

        Classify rules to evaluate against the document (at least one required)

        - `description: string`

          Natural language criteria for matching this rule

        - `type: string`

          Document type to assign when rule matches

      - `mode?: "FAST"`

        Classify execution mode

        - `"FAST"`

      - `parsing_configuration?: ParsingConfiguration | null`

        Parsing configuration for classify jobs.

        - `lang?: string`

          ISO 639-1 language code for the document

        - `max_pages?: number | null`

          Maximum number of pages to process. Omit for no limit.

        - `target_pages?: string | null`

          Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `ParseV2Parameters`

      Configuration for LlamaParse v2 document parsing.

      Includes tier selection, processing options, output formatting,
      page targeting, and webhook delivery. Refer to the LlamaParse
      documentation for details on each field.

      - `product_type: "parse_v2"`

        Product type.

        - `"parse_v2"`

      - `tier: "fast" | "cost_effective" | "agentic" | "agentic_plus"`

        Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced), 'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with highest accuracy)

        - `"fast"`

        - `"cost_effective"`

        - `"agentic"`

        - `"agentic_plus"`

      - `version: "latest" | "2026-05-13" | "2026-05-11" | 2 more | (string & {})`

        Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

        - `"latest" | "2026-05-13" | "2026-05-11" | 2 more`

          - `"latest"`

          - `"2026-05-13"`

          - `"2026-05-11"`

          - `"2026-04-09"`

          - `"2025-12-11"`

        - `(string & {})`

      - `agentic_options?: AgenticOptions | null`

        Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

        These options customize how the AI processes and interprets document content.
        Only applicable when using non-fast tiers.

        - `custom_prompt?: string | null`

          Custom instructions for the AI parser. Use to guide extraction behavior, specify output formatting, or provide domain-specific context. Example: 'Extract financial tables with currency symbols. Format dates as YYYY-MM-DD.'

      - `client_name?: string | null`

        Identifier for the client/application making the request. Used for analytics and debugging. Example: 'my-app-v2'

      - `crop_box?: CropBox`

        Crop boundaries to process only a portion of each page. Values are ratios 0-1 from page edges

        - `bottom?: number | null`

          Bottom boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content below this line is excluded

        - `left?: number | null`

          Left boundary as ratio (0-1). 0=left edge, 1=right edge. Content left of this line is excluded

        - `right?: number | null`

          Right boundary as ratio (0-1). 0=left edge, 1=right edge. Content right of this line is excluded

        - `top?: number | null`

          Top boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content above this line is excluded

      - `disable_cache?: boolean | null`

        Bypass result caching and force re-parsing. Use when document content may have changed or you need fresh results

      - `fast_options?: unknown`

        Options for fast tier parsing (rule-based, no AI).

        Fast tier uses deterministic algorithms for text extraction without AI enhancement.
        It's the fastest and most cost-effective option, best suited for simple documents
        with standard layouts. Currently has no configurable options but reserved for
        future expansion.

      - `input_options?: InputOptions`

        Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on detected input file type

        - `html?: HTML`

          HTML/web page parsing options (applies to .html, .htm files)

          - `make_all_elements_visible?: boolean | null`

            Force all HTML elements to be visible by overriding CSS display/visibility properties. Useful for parsing pages with hidden content or collapsed sections

          - `remove_fixed_elements?: boolean | null`

            Remove fixed-position elements (headers, footers, floating buttons) that appear on every page render

          - `remove_navigation_elements?: boolean | null`

            Remove navigation elements (nav bars, sidebars, menus) to focus on main content

        - `pdf?: unknown`

          PDF-specific parsing options (applies to .pdf files)

        - `presentation?: Presentation`

          Presentation parsing options (applies to .pptx, .ppt, .odp, .key files)

          - `out_of_bounds_content?: boolean | null`

            Extract content positioned outside the visible slide area. Some presentations have hidden notes or content that extends beyond slide boundaries

          - `skip_embedded_data?: boolean | null`

            Skip extraction of embedded chart data tables. When true, only the visual representation of charts is captured, not the underlying data

        - `spreadsheet?: Spreadsheet`

          Spreadsheet parsing options (applies to .xlsx, .xls, .csv, .ods files)

          - `detect_sub_tables_in_sheets?: boolean | null`

            Detect and extract multiple tables within a single sheet. Useful when spreadsheets contain several data regions separated by blank rows/columns

          - `force_formula_computation_in_sheets?: boolean | null`

            Compute formula results instead of extracting formula text. Use when you need calculated values rather than formula definitions

          - `include_hidden_sheets?: boolean | null`

            Parse hidden sheets in addition to visible ones. By default, hidden sheets are skipped

      - `output_options?: OutputOptions`

        Output formatting options for markdown, text, and extracted images

        - `additional_outputs?: Array<string>`

          Optional additional output artifacts to save alongside the primary parse output. Each value opts in to generating and persisting one extra file; the empty list (default) saves none. The three accepted values are: 'stripped_md' — per-page markdown stripped of formatting (links, bold/italic, images, HTML), saved as JSON for full-text-search indexing; fetch via `expand=stripped_markdown_content_metadata`. 'concatenated_stripped_txt' — all stripped pages concatenated into a single plain-text file with `\n\n---\n\n` between pages, useful for feeding the document into search or embedding pipelines as one blob; fetch via `expand=concatenated_stripped_markdown_content_metadata`. 'word_bbox' — raw word-level bounding boxes (one JSON object per word, with page number and x/y/w/h coordinates) saved as JSONL, useful for highlighting or grounding extracted answers back to the source document; fetch via `expand=raw_words_content_metadata`.

        - `extract_printed_page_number?: boolean | null`

          Extract the printed page number as it appears in the document (e.g., 'Page 5 of 10', 'v', 'A-3'). Useful for referencing original page numbers

        - `images_to_save?: Array<"screenshot" | "embedded" | "layout">`

          Image categories to extract and save. Options: 'screenshot' (full page renders useful for visual QA), 'embedded' (images found within the document), 'layout' (cropped regions from layout detection like figures and diagrams). Empty list saves no images

          - `"screenshot"`

          - `"embedded"`

          - `"layout"`

        - `markdown?: Markdown`

          Markdown formatting options including table styles and link annotations

          - `annotate_links?: boolean | null`

            Add link annotations to markdown output in the format [text](url). When false, only the link text is included

          - `inline_images?: boolean | null`

            Embed images directly in markdown as base64 data URIs instead of extracting them as separate files. Useful for self-contained markdown output

          - `tables?: Tables`

            Table formatting options including markdown vs HTML format and merging behavior

            - `compact_markdown_tables?: boolean | null`

              Remove extra whitespace padding in markdown table cells for more compact output

            - `markdown_table_multiline_separator?: string | null`

              Separator string for multiline cell content in markdown tables. Example: '<br>' to preserve line breaks, ' ' to join with spaces

            - `merge_continued_tables?: boolean | null`

              Automatically merge tables that span multiple pages into a single table. The merged table appears on the first page with merged_from_pages metadata

            - `output_tables_as_markdown?: boolean | null`

              Output tables as markdown pipe tables instead of HTML <table> tags. Markdown tables are simpler but cannot represent complex structures like merged cells

        - `spatial_text?: SpatialText`

          Spatial text output options for preserving document layout structure

          - `do_not_unroll_columns?: boolean | null`

            Keep multi-column layouts intact instead of linearizing columns into sequential text. Automatically enabled for non-fast tiers

          - `preserve_layout_alignment_across_pages?: boolean | null`

            Maintain consistent text column alignment across page boundaries. Automatically enabled for document-level parsing modes

          - `preserve_very_small_text?: boolean | null`

            Include text below the normal size threshold. Useful for footnotes, watermarks, or fine print that might otherwise be filtered out

        - `tables_as_spreadsheet?: TablesAsSpreadsheet`

          Options for exporting tables as XLSX spreadsheets

          - `enable?: boolean | null`

            Whether this option is enabled

          - `guess_sheet_name?: boolean`

            Automatically generate descriptive sheet names from table context (headers, surrounding text) instead of using generic names like 'Table_1'

      - `page_ranges?: PageRanges`

        Page selection: limit total pages or specify exact pages to process

        - `max_pages?: number | null`

          Maximum number of pages to process. Pages are processed in order starting from page 1. If both max_pages and target_pages are set, target_pages takes precedence

        - `target_pages?: string | null`

          Comma-separated list of specific pages to process using 1-based indexing. Supports individual pages and ranges. Examples: '1,3,5' (pages 1, 3, 5), '1-5' (pages 1 through 5 inclusive), '1,3,5-8,10' (pages 1, 3, 5-8, and 10). Pages are sorted and deduplicated automatically. Duplicate pages cause an error

      - `processing_control?: ProcessingControl`

        Job execution controls including timeouts and failure thresholds

        - `job_failure_conditions?: JobFailureConditions`

          Quality thresholds that determine when a job should fail vs complete with partial results

          - `allowed_page_failure_ratio?: number | null`

            Maximum ratio of pages allowed to fail before the job fails (0-1). Example: 0.1 means job fails if more than 10% of pages fail. Default is 0.05 (5%)

          - `fail_on_buggy_font?: boolean | null`

            Fail the job if a problematic font is detected that may cause incorrect text extraction. Buggy fonts can produce garbled or missing characters

          - `fail_on_image_extraction_error?: boolean | null`

            Fail the entire job if any embedded image cannot be extracted. By default, image extraction errors are logged but don't fail the job

          - `fail_on_image_ocr_error?: boolean | null`

            Fail the entire job if OCR fails on any image. By default, OCR errors result in empty text for that image

          - `fail_on_markdown_reconstruction_error?: boolean | null`

            Fail the entire job if markdown cannot be reconstructed for any page. By default, failed pages use fallback text extraction

        - `timeouts?: Timeouts`

          Timeout settings for job execution. Increase for large or complex documents

          - `base_in_seconds?: number | null`

            Base timeout for the job in seconds (max 1800 = 30 minutes). This is the minimum time allowed regardless of document size

          - `extra_time_per_page_in_seconds?: number | null`

            Additional timeout per page in seconds (max 300 = 5 minutes). Total timeout = base + (this value × page count)

      - `processing_options?: ProcessingOptions`

        Document processing options including OCR, table extraction, and chart parsing

        - `aggressive_table_extraction?: boolean | null`

          Use aggressive heuristics to detect table boundaries, even without visible borders. Useful for documents with borderless or complex tables

        - `auto_mode_configuration?: Array<AutoModeConfiguration> | null`

          Conditional processing rules that apply different parsing options based on page content, document structure, or filename patterns. Each entry defines trigger conditions and the parsing configuration to apply when triggered

          - `parsing_conf: ParsingConf`

            Parsing configuration to apply when trigger conditions are met

            - `adaptive_long_table?: boolean | null`

              Whether to use adaptive long table handling

            - `aggressive_table_extraction?: boolean | null`

              Whether to use aggressive table extraction

            - `crop_box?: CropBox | null`

              Crop box options for auto mode parsing configuration.

              - `bottom?: number | null`

                Bottom boundary of crop box as ratio (0-1)

              - `left?: number | null`

                Left boundary of crop box as ratio (0-1)

              - `right?: number | null`

                Right boundary of crop box as ratio (0-1)

              - `top?: number | null`

                Top boundary of crop box as ratio (0-1)

            - `custom_prompt?: string | null`

              Custom AI instructions for matched pages. Overrides the base custom_prompt

            - `extract_layout?: boolean | null`

              Whether to extract layout information

            - `high_res_ocr?: boolean | null`

              Whether to use high resolution OCR

            - `ignore?: Ignore | null`

              Ignore options for auto mode parsing configuration.

              - `ignore_diagonal_text?: boolean | null`

                Whether to ignore diagonal text in the document

              - `ignore_hidden_text?: boolean | null`

                Whether to ignore hidden text in the document

            - `language?: string | null`

              Primary language of the document

            - `outlined_table_extraction?: boolean | null`

              Whether to use outlined table extraction

            - `presentation?: Presentation | null`

              Presentation-specific options for auto mode parsing configuration.

              - `out_of_bounds_content?: boolean | null`

                Extract out of bounds content in presentation slides

              - `skip_embedded_data?: boolean | null`

                Skip extraction of embedded data for charts in presentation slides

            - `spatial_text?: SpatialText | null`

              Spatial text options for auto mode parsing configuration.

              - `do_not_unroll_columns?: boolean | null`

                Keep column structure intact without unrolling

              - `preserve_layout_alignment_across_pages?: boolean | null`

                Preserve text alignment across page boundaries

              - `preserve_very_small_text?: boolean | null`

                Include very small text in spatial output

            - `specialized_chart_parsing?: "agentic_plus" | "agentic" | "efficient" | null`

              Enable specialized chart parsing with the specified mode

              - `"agentic_plus"`

              - `"agentic"`

              - `"efficient"`

            - `tier?: "fast" | "cost_effective" | "agentic" | "agentic_plus" | null`

              Override the parsing tier for matched pages. Must be paired with version

              - `"fast"`

              - `"cost_effective"`

              - `"agentic"`

              - `"agentic_plus"`

            - `version?: "latest" | "2026-05-13" | "2026-05-11" | 2 more | (string & {}) | null`

              Tier version when overriding tier. Required when tier is specified

              - `"latest" | "2026-05-13" | "2026-05-11" | 2 more`

                - `"latest"`

                - `"2026-05-13"`

                - `"2026-05-11"`

                - `"2026-04-09"`

                - `"2025-12-11"`

              - `(string & {})`

          - `filename_match_glob?: string | null`

            Single glob pattern to match against filename

          - `filename_match_glob_list?: Array<string> | null`

            List of glob patterns to match against filename

          - `filename_regexp?: string | null`

            Regex pattern to match against filename

          - `filename_regexp_mode?: string | null`

            Regex mode flags (e.g., 'i' for case-insensitive)

          - `full_page_image_in_page?: boolean | null`

            Trigger if page contains a full-page image (scanned page detection)

          - `full_page_image_in_page_threshold?: number | string | null`

            Threshold for full page image detection (0.0-1.0, default 0.8)

            - `number`

            - `string`

          - `image_in_page?: boolean | null`

            Trigger if page contains non-screenshot images

          - `layout_element_in_page?: string | null`

            Trigger if page contains this layout element type

          - `layout_element_in_page_confidence_threshold?: number | string | null`

            Confidence threshold for layout element detection

            - `number`

            - `string`

          - `page_contains_at_least_n_charts?: number | string | null`

            Trigger if page has more than N charts

            - `number`

            - `string`

          - `page_contains_at_least_n_images?: number | string | null`

            Trigger if page has more than N images

            - `number`

            - `string`

          - `page_contains_at_least_n_layout_elements?: number | string | null`

            Trigger if page has more than N layout elements

            - `number`

            - `string`

          - `page_contains_at_least_n_lines?: number | string | null`

            Trigger if page has more than N lines

            - `number`

            - `string`

          - `page_contains_at_least_n_links?: number | string | null`

            Trigger if page has more than N links

            - `number`

            - `string`

          - `page_contains_at_least_n_numbers?: number | string | null`

            Trigger if page has more than N numeric words

            - `number`

            - `string`

          - `page_contains_at_least_n_percent_numbers?: number | string | null`

            Trigger if page has more than N% numeric words

            - `number`

            - `string`

          - `page_contains_at_least_n_tables?: number | string | null`

            Trigger if page has more than N tables

            - `number`

            - `string`

          - `page_contains_at_least_n_words?: number | string | null`

            Trigger if page has more than N words

            - `number`

            - `string`

          - `page_contains_at_most_n_charts?: number | string | null`

            Trigger if page has fewer than N charts

            - `number`

            - `string`

          - `page_contains_at_most_n_images?: number | string | null`

            Trigger if page has fewer than N images

            - `number`

            - `string`

          - `page_contains_at_most_n_layout_elements?: number | string | null`

            Trigger if page has fewer than N layout elements

            - `number`

            - `string`

          - `page_contains_at_most_n_lines?: number | string | null`

            Trigger if page has fewer than N lines

            - `number`

            - `string`

          - `page_contains_at_most_n_links?: number | string | null`

            Trigger if page has fewer than N links

            - `number`

            - `string`

          - `page_contains_at_most_n_numbers?: number | string | null`

            Trigger if page has fewer than N numeric words

            - `number`

            - `string`

          - `page_contains_at_most_n_percent_numbers?: number | string | null`

            Trigger if page has fewer than N% numeric words

            - `number`

            - `string`

          - `page_contains_at_most_n_tables?: number | string | null`

            Trigger if page has fewer than N tables

            - `number`

            - `string`

          - `page_contains_at_most_n_words?: number | string | null`

            Trigger if page has fewer than N words

            - `number`

            - `string`

          - `page_longer_than_n_chars?: number | string | null`

            Trigger if page has more than N characters

            - `number`

            - `string`

          - `page_md_error?: boolean | null`

            Trigger on pages with markdown extraction errors

          - `page_shorter_than_n_chars?: number | string | null`

            Trigger if page has fewer than N characters

            - `number`

            - `string`

          - `regexp_in_page?: string | null`

            Regex pattern to match in page content

          - `regexp_in_page_mode?: string | null`

            Regex mode flags for regexp_in_page

          - `table_in_page?: boolean | null`

            Trigger if page contains a table

          - `text_in_page?: string | null`

            Trigger if page text/markdown contains this string

          - `trigger_mode?: string | null`

            How to combine multiple trigger conditions: 'and' (all conditions must match, this is the default) or 'or' (any single condition can trigger)

        - `cost_optimizer?: CostOptimizer | null`

          Cost optimizer configuration for reducing parsing costs on simpler pages.

          When enabled, the parser analyzes each page and routes simpler pages to faster,
          cheaper processing while preserving quality for complex pages. Only works with
          'agentic' or 'agentic_plus' tiers.

          - `enable?: boolean | null`

            Enable cost-optimized parsing. Routes simpler pages to faster processing while complex pages use full AI analysis. May reduce speed on some documents. IMPORTANT: Only available with 'agentic' or 'agentic_plus' tiers

        - `disable_heuristics?: boolean | null`

          Disable automatic heuristics including outlined table extraction and adaptive long table handling. Use when heuristics produce incorrect results

        - `ignore?: Ignore`

          Options for ignoring specific text types (diagonal, hidden, text in images)

          - `ignore_diagonal_text?: boolean | null`

            Skip text rotated at an angle (not horizontal/vertical). Useful for ignoring watermarks or decorative angled text

          - `ignore_hidden_text?: boolean | null`

            Skip text marked as hidden in the document structure. Some PDFs contain invisible text layers used for accessibility or search indexing

          - `ignore_text_in_image?: boolean | null`

            Skip OCR text extraction from embedded images. Use when images contain irrelevant text (watermarks, logos) that shouldn't be in the output

        - `ocr_parameters?: OcrParameters`

          OCR configuration including language detection settings

          - `languages?: Array<ParsingLanguages> | null`

            Languages to use for OCR text recognition. Specify multiple languages if document contains mixed-language content. Order matters - put primary language first. Example: ['en', 'es'] for English with Spanish

            - `"af"`

            - `"az"`

            - `"bs"`

            - `"cs"`

            - `"cy"`

            - `"da"`

            - `"de"`

            - `"en"`

            - `"es"`

            - `"et"`

            - `"fr"`

            - `"ga"`

            - `"hr"`

            - `"hu"`

            - `"id"`

            - `"is"`

            - `"it"`

            - `"ku"`

            - `"la"`

            - `"lt"`

            - `"lv"`

            - `"mi"`

            - `"ms"`

            - `"mt"`

            - `"nl"`

            - `"no"`

            - `"oc"`

            - `"pi"`

            - `"pl"`

            - `"pt"`

            - `"ro"`

            - `"rs_latin"`

            - `"sk"`

            - `"sl"`

            - `"sq"`

            - `"sv"`

            - `"sw"`

            - `"tl"`

            - `"tr"`

            - `"uz"`

            - `"vi"`

            - `"ar"`

            - `"fa"`

            - `"ug"`

            - `"ur"`

            - `"bn"`

            - `"as"`

            - `"mni"`

            - `"ru"`

            - `"rs_cyrillic"`

            - `"be"`

            - `"bg"`

            - `"uk"`

            - `"mn"`

            - `"abq"`

            - `"ady"`

            - `"kbd"`

            - `"ava"`

            - `"dar"`

            - `"inh"`

            - `"che"`

            - `"lbe"`

            - `"lez"`

            - `"tab"`

            - `"tjk"`

            - `"hi"`

            - `"mr"`

            - `"ne"`

            - `"bh"`

            - `"mai"`

            - `"ang"`

            - `"bho"`

            - `"mah"`

            - `"sck"`

            - `"new"`

            - `"gom"`

            - `"sa"`

            - `"bgc"`

            - `"th"`

            - `"ch_sim"`

            - `"ch_tra"`

            - `"ja"`

            - `"ko"`

            - `"ta"`

            - `"te"`

            - `"kn"`

        - `specialized_chart_parsing?: "agentic_plus" | "agentic" | "efficient" | null`

          Enable AI-powered chart analysis. Modes: 'efficient' (fast, lower cost), 'agentic' (balanced), 'agentic_plus' (highest accuracy). Automatically enables extract_layout and precise_bounding_box when set

          - `"agentic_plus"`

          - `"agentic"`

          - `"efficient"`

      - `webhook_configurations?: Array<WebhookConfiguration>`

        Webhook endpoints for job status notifications. Multiple webhooks can be configured for different events or services

        - `webhook_events?: Array<string> | null`

          Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

        - `webhook_headers?: Record<string, unknown> | null`

          Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

        - `webhook_url?: string | null`

          HTTPS URL to receive webhook POST requests. Must be publicly accessible

    - `SpreadsheetV1Parameters`

      Typed parameters for a *spreadsheet v1* product configuration.

      - `product_type: "spreadsheet_v1"`

        Product type.

        - `"spreadsheet_v1"`

      - `extraction_range?: string | null`

        A1 notation of the range to extract a single region from. If None, the entire sheet is used.

      - `flatten_hierarchical_tables?: boolean`

        Return a flattened dataframe when a detected table is recognized as hierarchical.

      - `generate_additional_metadata?: boolean`

        Whether to generate additional metadata (title, description) for each extracted region.

      - `include_hidden_cells?: boolean`

        Whether to include hidden cells when extracting regions from the spreadsheet.

      - `sheet_names?: Array<string> | null`

        The names of the sheets to extract regions from. If empty, all sheets will be processed.

      - `specialization?: string | null`

        Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

      - `table_merge_sensitivity?: "strong" | "weak"`

        Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

        - `"strong"`

        - `"weak"`

      - `use_experimental_processing?: boolean`

        Enables experimental processing. Accuracy may be impacted.

    - `UntypedParameters`

      Catch-all for configurations without a dedicated typed schema.

      Accepts arbitrary JSON fields alongside `product_type`.

      - `product_type: "unknown"`

        Product type.

        - `"unknown"`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const configurationCreate = await client.extract.generateSchema();

console.log(configurationCreate.name);
```

#### Response

```json
{
  "name": "x",
  "parameters": {
    "categories": [
      {
        "name": "x",
        "description": "x"
      }
    ],
    "product_type": "split_v1",
    "splitting_strategy": {
      "allow_uncategorized": "include"
    }
  }
}
```

## Domain Types

### Extract Configuration

- `ExtractConfiguration`

  Extract configuration combining parse and extract settings.

  - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

    JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `cite_sources?: boolean`

    Include citations in results

  - `confidence_scores?: boolean`

    Include confidence scores in results

  - `extract_version?: string`

    Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

  - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

    Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

    - `"per_doc"`

    - `"per_page"`

    - `"per_table_row"`

  - `max_pages?: number | null`

    Maximum number of pages to process. Omit for no limit.

  - `parse_config_id?: string | null`

    Saved parse configuration ID to control how the document is parsed before extraction

  - `parse_tier?: string | null`

    Parse tier to use before extraction. Defaults to the extract tier if not specified.

  - `system_prompt?: string | null`

    Custom system prompt to guide extraction behavior

  - `target_pages?: string | null`

    Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `tier?: "cost_effective" | "agentic"`

    Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

    - `"cost_effective"`

    - `"agentic"`

### Extract Job Metadata

- `ExtractJobMetadata`

  Extraction metadata.

  - `field_metadata?: ExtractedFieldMetadata | null`

    Metadata for extracted fields including document, page, and row level info.

    - `document_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `page_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

      Per-page metadata when extraction_target is per_page

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `row_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

      Per-row metadata when extraction_target is per_table_row

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

  - `parse_job_id?: string | null`

    Reference to the ParseJob ID used for parsing

  - `parse_tier?: string | null`

    Parse tier used for parsing the document

### Extract Job Usage

- `ExtractJobUsage`

  Extraction usage metrics.

  - `num_document_tokens?: number | null`

    Number of document tokens

  - `num_output_tokens?: number | null`

    Number of output tokens

  - `num_pages_extracted?: number | null`

    Number of pages extracted

### Extract V2 Job

- `ExtractV2Job`

  An extraction job.

  - `id: string`

    Unique job identifier (job_id)

  - `created_at: string`

    Creation timestamp

  - `file_input: string`

    File ID or parse job ID that was extracted

  - `project_id: string`

    Project this job belongs to

  - `status: string`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `updated_at: string`

    Last update timestamp

  - `configuration?: ExtractConfiguration | null`

    Extract configuration combining parse and extract settings.

    - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources?: boolean`

      Include citations in results

    - `confidence_scores?: boolean`

      Include confidence scores in results

    - `extract_version?: string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages?: number | null`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id?: string | null`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier?: string | null`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt?: string | null`

      Custom system prompt to guide extraction behavior

    - `target_pages?: string | null`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier?: "cost_effective" | "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id?: string | null`

    Saved extract configuration ID used for this job, if any

  - `error_message?: string | null`

    Error details when status is FAILED

  - `extract_metadata?: ExtractJobMetadata | null`

    Extraction metadata.

    - `field_metadata?: ExtractedFieldMetadata | null`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `page_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

        Per-page metadata when extraction_target is per_page

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `row_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

        Per-row metadata when extraction_target is per_table_row

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

    - `parse_job_id?: string | null`

      Reference to the ParseJob ID used for parsing

    - `parse_tier?: string | null`

      Parse tier used for parsing the document

  - `extract_result?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>>`

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

  - `metadata?: Metadata | null`

    Job-level metadata.

    - `usage?: ExtractJobUsage | null`

      Extraction usage metrics.

      - `num_document_tokens?: number | null`

        Number of document tokens

      - `num_output_tokens?: number | null`

        Number of output tokens

      - `num_pages_extracted?: number | null`

        Number of pages extracted

### Extract V2 Job Create

- `ExtractV2JobCreate`

  Request to create an extraction job. Provide configuration_id or inline configuration.

  - `file_input: string`

    File ID or parse job ID to extract from

  - `configuration?: ExtractConfiguration | null`

    Extract configuration combining parse and extract settings.

    - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources?: boolean`

      Include citations in results

    - `confidence_scores?: boolean`

      Include confidence scores in results

    - `extract_version?: string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages?: number | null`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id?: string | null`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier?: string | null`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt?: string | null`

      Custom system prompt to guide extraction behavior

    - `target_pages?: string | null`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier?: "cost_effective" | "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id?: string | null`

    Saved configuration ID

  - `webhook_configurations?: Array<WebhookConfiguration> | null`

    Outbound webhook endpoints to notify on job status changes

    - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

      Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

      - `"extract.pending"`

      - `"extract.success"`

      - `"extract.error"`

      - `"extract.partial_success"`

      - `"extract.cancelled"`

      - `"parse.pending"`

      - `"parse.running"`

      - `"parse.success"`

      - `"parse.error"`

      - `"parse.partial_success"`

      - `"parse.cancelled"`

      - `"classify.pending"`

      - `"classify.success"`

      - `"classify.error"`

      - `"classify.partial_success"`

      - `"classify.cancelled"`

      - `"unmapped_event"`

    - `webhook_headers?: Record<string, string> | null`

      Custom HTTP headers sent with each webhook request (e.g. auth tokens)

    - `webhook_output_format?: string | null`

      Response format sent to the webhook: 'string' (default) or 'json'

    - `webhook_url?: string | null`

      URL to receive webhook POST notifications

### Extract V2 Job Query Response

- `ExtractV2JobQueryResponse`

  Paginated list of extraction jobs.

  - `items: Array<ExtractV2Job>`

    The list of items.

    - `id: string`

      Unique job identifier (job_id)

    - `created_at: string`

      Creation timestamp

    - `file_input: string`

      File ID or parse job ID that was extracted

    - `project_id: string`

      Project this job belongs to

    - `status: string`

      Current job status.

      - `PENDING` — queued, not yet started
      - `RUNNING` — actively processing
      - `COMPLETED` — finished successfully
      - `FAILED` — terminated with an error
      - `CANCELLED` — cancelled by user

    - `updated_at: string`

      Last update timestamp

    - `configuration?: ExtractConfiguration | null`

      Extract configuration combining parse and extract settings.

      - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

        JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `cite_sources?: boolean`

        Include citations in results

      - `confidence_scores?: boolean`

        Include confidence scores in results

      - `extract_version?: string`

        Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

      - `extraction_target?: "per_doc" | "per_page" | "per_table_row"`

        Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

        - `"per_doc"`

        - `"per_page"`

        - `"per_table_row"`

      - `max_pages?: number | null`

        Maximum number of pages to process. Omit for no limit.

      - `parse_config_id?: string | null`

        Saved parse configuration ID to control how the document is parsed before extraction

      - `parse_tier?: string | null`

        Parse tier to use before extraction. Defaults to the extract tier if not specified.

      - `system_prompt?: string | null`

        Custom system prompt to guide extraction behavior

      - `target_pages?: string | null`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

      - `tier?: "cost_effective" | "agentic"`

        Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

        - `"cost_effective"`

        - `"agentic"`

    - `configuration_id?: string | null`

      Saved extract configuration ID used for this job, if any

    - `error_message?: string | null`

      Error details when status is FAILED

    - `extract_metadata?: ExtractJobMetadata | null`

      Extraction metadata.

      - `field_metadata?: ExtractedFieldMetadata | null`

        Metadata for extracted fields including document, page, and row level info.

        - `document_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

          Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

          - `Record<string, unknown>`

          - `Array<unknown>`

          - `string`

          - `number`

          - `boolean`

        - `page_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

          Per-page metadata when extraction_target is per_page

          - `Record<string, unknown>`

          - `Array<unknown>`

          - `string`

          - `number`

          - `boolean`

        - `row_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

          Per-row metadata when extraction_target is per_table_row

          - `Record<string, unknown>`

          - `Array<unknown>`

          - `string`

          - `number`

          - `boolean`

      - `parse_job_id?: string | null`

        Reference to the ParseJob ID used for parsing

      - `parse_tier?: string | null`

        Parse tier used for parsing the document

    - `extract_result?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

      Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

      - `Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

      - `Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>>`

        - `Record<string, unknown>`

        - `Array<unknown>`

        - `string`

        - `number`

        - `boolean`

    - `metadata?: Metadata | null`

      Job-level metadata.

      - `usage?: ExtractJobUsage | null`

        Extraction usage metrics.

        - `num_document_tokens?: number | null`

          Number of document tokens

        - `num_output_tokens?: number | null`

          Number of output tokens

        - `num_pages_extracted?: number | null`

          Number of pages extracted

  - `next_page_token?: string | null`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size?: number | null`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Extract V2 Schema Generate Request

- `ExtractV2SchemaGenerateRequest`

  Request schema for generating an extraction schema.

  - `data_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Optional schema to validate, refine, or extend

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `file_id?: string | null`

    Optional file ID to analyze for schema generation

  - `name?: string | null`

    Name for the generated configuration (auto-generated if omitted)

  - `prompt?: string | null`

    Natural language description of the data structure to extract

### Extract V2 Schema Validate Request

- `ExtractV2SchemaValidateRequest`

  Request schema for validating an extraction schema.

  - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

    JSON Schema to validate for use with extract jobs

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Extract V2 Schema Validate Response

- `ExtractV2SchemaValidateResponse`

  Response schema for schema validation.

  - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

    Validated JSON Schema, ready for use in extract jobs

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Extracted Field Metadata

- `ExtractedFieldMetadata`

  Metadata for extracted fields including document, page, and row level info.

  - `document_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `page_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

    Per-page metadata when extraction_target is per_page

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `row_metadata?: Array<Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>> | null`

    Per-row metadata when extraction_target is per_table_row

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Extract Delete Response

- `ExtractDeleteResponse = unknown`
