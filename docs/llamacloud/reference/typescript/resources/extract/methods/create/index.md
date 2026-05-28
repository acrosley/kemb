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
