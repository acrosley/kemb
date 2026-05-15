# Extract

## Create Extract Job

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

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `file_input: string`

  File ID or parse job ID to extract from

- `configuration: optional ExtractConfiguration`

  Extract configuration combining parse and extract settings.

  - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

    JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

  - `cite_sources: optional boolean`

    Include citations in results

  - `confidence_scores: optional boolean`

    Include confidence scores in results

  - `extract_version: optional string`

    Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

  - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

    Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

    - `"per_doc"`

    - `"per_page"`

    - `"per_table_row"`

  - `max_pages: optional number`

    Maximum number of pages to process. Omit for no limit.

  - `parse_config_id: optional string`

    Saved parse configuration ID to control how the document is parsed before extraction

  - `parse_tier: optional string`

    Parse tier to use before extraction. Defaults to the extract tier if not specified.

  - `system_prompt: optional string`

    Custom system prompt to guide extraction behavior

  - `target_pages: optional string`

    Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `tier: optional "cost_effective" or "agentic"`

    Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

    - `"cost_effective"`

    - `"agentic"`

- `configuration_id: optional string`

  Saved configuration ID

- `webhook_configurations: optional array of object { webhook_events, webhook_headers, webhook_output_format, webhook_url }`

  Outbound webhook endpoints to notify on job status changes

  - `webhook_events: optional array of "extract.pending" or "extract.success" or "extract.error" or 14 more`

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

  - `webhook_headers: optional map[string]`

    Custom HTTP headers sent with each webhook request (e.g. auth tokens)

  - `webhook_output_format: optional string`

    Response format sent to the webhook: 'string' (default) or 'json'

  - `webhook_url: optional string`

    URL to receive webhook POST notifications

### Returns

- `ExtractV2Job = object { id, created_at, file_input, 9 more }`

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

  - `configuration: optional ExtractConfiguration`

    Extract configuration combining parse and extract settings.

    - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources: optional boolean`

      Include citations in results

    - `confidence_scores: optional boolean`

      Include confidence scores in results

    - `extract_version: optional string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: optional number`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: optional string`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: optional string`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: optional string`

      Custom system prompt to guide extraction behavior

    - `target_pages: optional string`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: optional "cost_effective" or "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: optional string`

    Saved extract configuration ID used for this job, if any

  - `error_message: optional string`

    Error details when status is FAILED

  - `extract_metadata: optional ExtractJobMetadata`

    Extraction metadata.

    - `field_metadata: optional ExtractedFieldMetadata`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `page_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

        Per-page metadata when extraction_target is per_page

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `row_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

        Per-row metadata when extraction_target is per_table_row

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

    - `parse_job_id: optional string`

      Reference to the ParseJob ID used for parsing

    - `parse_tier: optional string`

      Parse tier used for parsing the document

  - `extract_result: optional map[map[unknown] or array of unknown or string or 2 more] or array of map[map[unknown] or array of unknown or string or 2 more]`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `map[map[unknown] or array of unknown or string or 2 more]`

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `array of map[map[unknown] or array of unknown or string or 2 more]`

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

  - `metadata: optional object { usage }`

    Job-level metadata.

    - `usage: optional ExtractJobUsage`

      Extraction usage metrics.

      - `num_document_tokens: optional number`

        Number of document tokens

      - `num_output_tokens: optional number`

        Number of output tokens

      - `num_pages_extracted: optional number`

        Number of pages extracted

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v2/extract \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "file_input": "dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
        }'
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

**get** `/api/v2/extract`

List extraction jobs with optional filtering and pagination.

Filter by `configuration_id`, `status`, `file_input`,
or creation date range. Results are returned newest-first.
Use `expand=configuration` to include the full configuration used,
and `expand=extract_metadata` for per-field metadata.

### Query Parameters

- `configuration_id: optional string`

  Filter by configuration ID

- `created_at_on_or_after: optional string`

  Include items created at or after this timestamp (inclusive)

- `created_at_on_or_before: optional string`

  Include items created at or before this timestamp (inclusive)

- `document_input_type: optional string`

  Filter by document input type (file_id or parse_job_id)

- `document_input_value: optional string`

  Deprecated: use file_input instead

- `expand: optional array of string`

  Additional fields to include: configuration, extract_metadata

- `file_input: optional string`

  Filter by file input value

- `job_ids: optional array of string`

  Filter by specific job IDs

- `organization_id: optional string`

- `page_size: optional number`

  Number of items per page

- `page_token: optional string`

  Token for pagination

- `project_id: optional string`

- `status: optional "PENDING" or "THROTTLED" or "RUNNING" or 3 more`

  Filter by status

  - `"PENDING"`

  - `"THROTTLED"`

  - `"RUNNING"`

  - `"COMPLETED"`

  - `"FAILED"`

  - `"CANCELLED"`

### Cookie Parameters

- `session: optional string`

### Returns

- `ExtractV2JobQueryResponse = object { items, next_page_token, total_size }`

  Paginated list of extraction jobs.

  - `items: array of ExtractV2Job`

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

    - `configuration: optional ExtractConfiguration`

      Extract configuration combining parse and extract settings.

      - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `cite_sources: optional boolean`

        Include citations in results

      - `confidence_scores: optional boolean`

        Include confidence scores in results

      - `extract_version: optional string`

        Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

      - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

        Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

        - `"per_doc"`

        - `"per_page"`

        - `"per_table_row"`

      - `max_pages: optional number`

        Maximum number of pages to process. Omit for no limit.

      - `parse_config_id: optional string`

        Saved parse configuration ID to control how the document is parsed before extraction

      - `parse_tier: optional string`

        Parse tier to use before extraction. Defaults to the extract tier if not specified.

      - `system_prompt: optional string`

        Custom system prompt to guide extraction behavior

      - `target_pages: optional string`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

      - `tier: optional "cost_effective" or "agentic"`

        Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

        - `"cost_effective"`

        - `"agentic"`

    - `configuration_id: optional string`

      Saved extract configuration ID used for this job, if any

    - `error_message: optional string`

      Error details when status is FAILED

    - `extract_metadata: optional ExtractJobMetadata`

      Extraction metadata.

      - `field_metadata: optional ExtractedFieldMetadata`

        Metadata for extracted fields including document, page, and row level info.

        - `document_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

          Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

          - `map[unknown]`

          - `array of unknown`

          - `string`

          - `number`

          - `boolean`

        - `page_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

          Per-page metadata when extraction_target is per_page

          - `map[unknown]`

          - `array of unknown`

          - `string`

          - `number`

          - `boolean`

        - `row_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

          Per-row metadata when extraction_target is per_table_row

          - `map[unknown]`

          - `array of unknown`

          - `string`

          - `number`

          - `boolean`

      - `parse_job_id: optional string`

        Reference to the ParseJob ID used for parsing

      - `parse_tier: optional string`

        Parse tier used for parsing the document

    - `extract_result: optional map[map[unknown] or array of unknown or string or 2 more] or array of map[map[unknown] or array of unknown or string or 2 more]`

      Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

      - `map[map[unknown] or array of unknown or string or 2 more]`

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `array of map[map[unknown] or array of unknown or string or 2 more]`

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

    - `metadata: optional object { usage }`

      Job-level metadata.

      - `usage: optional ExtractJobUsage`

        Extraction usage metrics.

        - `num_document_tokens: optional number`

          Number of document tokens

        - `num_output_tokens: optional number`

          Number of output tokens

        - `num_pages_extracted: optional number`

          Number of pages extracted

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v2/extract \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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

**get** `/api/v2/extract/{job_id}`

Get a single extraction job by ID.

Returns the job status and results when complete.
Use `expand=configuration` to include the full configuration used,
and `expand=extract_metadata` for per-field metadata.

### Path Parameters

- `job_id: string`

### Query Parameters

- `expand: optional array of string`

  Additional fields to include: configuration, extract_metadata

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Returns

- `ExtractV2Job = object { id, created_at, file_input, 9 more }`

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

  - `configuration: optional ExtractConfiguration`

    Extract configuration combining parse and extract settings.

    - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources: optional boolean`

      Include citations in results

    - `confidence_scores: optional boolean`

      Include confidence scores in results

    - `extract_version: optional string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: optional number`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: optional string`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: optional string`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: optional string`

      Custom system prompt to guide extraction behavior

    - `target_pages: optional string`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: optional "cost_effective" or "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: optional string`

    Saved extract configuration ID used for this job, if any

  - `error_message: optional string`

    Error details when status is FAILED

  - `extract_metadata: optional ExtractJobMetadata`

    Extraction metadata.

    - `field_metadata: optional ExtractedFieldMetadata`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `page_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

        Per-page metadata when extraction_target is per_page

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `row_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

        Per-row metadata when extraction_target is per_table_row

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

    - `parse_job_id: optional string`

      Reference to the ParseJob ID used for parsing

    - `parse_tier: optional string`

      Parse tier used for parsing the document

  - `extract_result: optional map[map[unknown] or array of unknown or string or 2 more] or array of map[map[unknown] or array of unknown or string or 2 more]`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `map[map[unknown] or array of unknown or string or 2 more]`

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `array of map[map[unknown] or array of unknown or string or 2 more]`

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

  - `metadata: optional object { usage }`

    Job-level metadata.

    - `usage: optional ExtractJobUsage`

      Extraction usage metrics.

      - `num_document_tokens: optional number`

        Number of document tokens

      - `num_output_tokens: optional number`

        Number of output tokens

      - `num_pages_extracted: optional number`

        Number of pages extracted

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v2/extract/$JOB_ID \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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

**delete** `/api/v2/extract/{job_id}`

Delete an extraction job and its results.

### Path Parameters

- `job_id: string`

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v2/extract/$JOB_ID \
    -X DELETE \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

#### Response

```json
{}
```

## Validate Extraction Schema

**post** `/api/v2/extract/schema/validation`

Validate a JSON schema for extraction.

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

  JSON Schema to validate for use with extract jobs

  - `map[unknown]`

  - `array of unknown`

  - `string`

  - `number`

  - `boolean`

### Returns

- `ExtractV2SchemaValidateResponse = object { data_schema }`

  Response schema for schema validation.

  - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

    Validated JSON Schema, ready for use in extract jobs

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v2/extract/schema/validation \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "data_schema": {
            "foo": {
              "foo": "bar"
            }
          }
        }'
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

**post** `/api/v2/extract/schema/generate`

Generate a JSON schema and return a product configuration request.

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `data_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

  Optional schema to validate, refine, or extend

  - `map[unknown]`

  - `array of unknown`

  - `string`

  - `number`

  - `boolean`

- `file_id: optional string`

  Optional file ID to analyze for schema generation

- `name: optional string`

  Name for the generated configuration (auto-generated if omitted)

- `prompt: optional string`

  Natural language description of the data structure to extract

### Returns

- `ConfigurationCreate = object { name, parameters }`

  Request body for creating a product configuration.

  - `name: string`

    Human-readable name for this configuration.

  - `parameters: SplitV1Parameters or ExtractV2Parameters or ClassifyV2Parameters or 3 more`

    Product-specific configuration parameters.

    - `SplitV1Parameters = object { categories, product_type, splitting_strategy }`

      Typed parameters for a *split v1* product configuration.

      - `categories: array of SplitCategory`

        Categories to split documents into.

        - `name: string`

          Name of the category.

        - `description: optional string`

          Optional description of what content belongs in this category.

      - `product_type: "split_v1"`

        Product type.

        - `"split_v1"`

      - `splitting_strategy: optional object { allow_uncategorized }`

        Strategy for splitting documents.

        - `allow_uncategorized: optional "include" or "forbid" or "omit"`

          Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

          - `"include"`

          - `"forbid"`

          - `"omit"`

    - `ExtractV2Parameters = object { data_schema, product_type, cite_sources, 9 more }`

      Typed parameters for an *extract v2* product configuration.

      - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `product_type: "extract_v2"`

        Product type.

        - `"extract_v2"`

      - `cite_sources: optional boolean`

        Include citations in results

      - `confidence_scores: optional boolean`

        Include confidence scores in results

      - `extract_version: optional string`

        Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

      - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

        Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

        - `"per_doc"`

        - `"per_page"`

        - `"per_table_row"`

      - `max_pages: optional number`

        Maximum number of pages to process. Omit for no limit.

      - `parse_config_id: optional string`

        Saved parse configuration ID to control how the document is parsed before extraction

      - `parse_tier: optional string`

        Parse tier to use before extraction. Defaults to the extract tier if not specified.

      - `system_prompt: optional string`

        Custom system prompt to guide extraction behavior

      - `target_pages: optional string`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

      - `tier: optional "cost_effective" or "agentic"`

        Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

        - `"cost_effective"`

        - `"agentic"`

    - `ClassifyV2Parameters = object { product_type, rules, mode, parsing_configuration }`

      Typed parameters for a *classify v2* product configuration.

      - `product_type: "classify_v2"`

        Product type.

        - `"classify_v2"`

      - `rules: array of object { description, type }`

        Classify rules to evaluate against the document (at least one required)

        - `description: string`

          Natural language criteria for matching this rule

        - `type: string`

          Document type to assign when rule matches

      - `mode: optional "FAST"`

        Classify execution mode

        - `"FAST"`

      - `parsing_configuration: optional object { lang, max_pages, target_pages }`

        Parsing configuration for classify jobs.

        - `lang: optional string`

          ISO 639-1 language code for the document

        - `max_pages: optional number`

          Maximum number of pages to process. Omit for no limit.

        - `target_pages: optional string`

          Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `ParseV2Parameters = object { product_type, tier, version, 11 more }`

      Configuration for LlamaParse v2 document parsing.

      Includes tier selection, processing options, output formatting,
      page targeting, and webhook delivery. Refer to the LlamaParse
      documentation for details on each field.

      - `product_type: "parse_v2"`

        Product type.

        - `"parse_v2"`

      - `tier: "fast" or "cost_effective" or "agentic" or "agentic_plus"`

        Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced), 'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with highest accuracy)

        - `"fast"`

        - `"cost_effective"`

        - `"agentic"`

        - `"agentic_plus"`

      - `version: "latest" or "2026-05-13" or "2026-05-11" or 2 more or string`

        Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

        - `"latest" or "2026-05-13" or "2026-05-11" or 2 more`

          Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

          - `"latest"`

          - `"2026-05-13"`

          - `"2026-05-11"`

          - `"2026-04-09"`

          - `"2025-12-11"`

        - `string`

      - `agentic_options: optional object { custom_prompt }`

        Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

        These options customize how the AI processes and interprets document content.
        Only applicable when using non-fast tiers.

        - `custom_prompt: optional string`

          Custom instructions for the AI parser. Use to guide extraction behavior, specify output formatting, or provide domain-specific context. Example: 'Extract financial tables with currency symbols. Format dates as YYYY-MM-DD.'

      - `client_name: optional string`

        Identifier for the client/application making the request. Used for analytics and debugging. Example: 'my-app-v2'

      - `crop_box: optional object { bottom, left, right, top }`

        Crop boundaries to process only a portion of each page. Values are ratios 0-1 from page edges

        - `bottom: optional number`

          Bottom boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content below this line is excluded

        - `left: optional number`

          Left boundary as ratio (0-1). 0=left edge, 1=right edge. Content left of this line is excluded

        - `right: optional number`

          Right boundary as ratio (0-1). 0=left edge, 1=right edge. Content right of this line is excluded

        - `top: optional number`

          Top boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content above this line is excluded

      - `disable_cache: optional boolean`

        Bypass result caching and force re-parsing. Use when document content may have changed or you need fresh results

      - `fast_options: optional unknown`

        Options for fast tier parsing (rule-based, no AI).

        Fast tier uses deterministic algorithms for text extraction without AI enhancement.
        It's the fastest and most cost-effective option, best suited for simple documents
        with standard layouts. Currently has no configurable options but reserved for
        future expansion.

      - `input_options: optional object { html, pdf, presentation, spreadsheet }`

        Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on detected input file type

        - `html: optional object { make_all_elements_visible, remove_fixed_elements, remove_navigation_elements }`

          HTML/web page parsing options (applies to .html, .htm files)

          - `make_all_elements_visible: optional boolean`

            Force all HTML elements to be visible by overriding CSS display/visibility properties. Useful for parsing pages with hidden content or collapsed sections

          - `remove_fixed_elements: optional boolean`

            Remove fixed-position elements (headers, footers, floating buttons) that appear on every page render

          - `remove_navigation_elements: optional boolean`

            Remove navigation elements (nav bars, sidebars, menus) to focus on main content

        - `pdf: optional unknown`

          PDF-specific parsing options (applies to .pdf files)

        - `presentation: optional object { out_of_bounds_content, skip_embedded_data }`

          Presentation parsing options (applies to .pptx, .ppt, .odp, .key files)

          - `out_of_bounds_content: optional boolean`

            Extract content positioned outside the visible slide area. Some presentations have hidden notes or content that extends beyond slide boundaries

          - `skip_embedded_data: optional boolean`

            Skip extraction of embedded chart data tables. When true, only the visual representation of charts is captured, not the underlying data

        - `spreadsheet: optional object { detect_sub_tables_in_sheets, force_formula_computation_in_sheets, include_hidden_sheets }`

          Spreadsheet parsing options (applies to .xlsx, .xls, .csv, .ods files)

          - `detect_sub_tables_in_sheets: optional boolean`

            Detect and extract multiple tables within a single sheet. Useful when spreadsheets contain several data regions separated by blank rows/columns

          - `force_formula_computation_in_sheets: optional boolean`

            Compute formula results instead of extracting formula text. Use when you need calculated values rather than formula definitions

          - `include_hidden_sheets: optional boolean`

            Parse hidden sheets in addition to visible ones. By default, hidden sheets are skipped

      - `output_options: optional object { additional_outputs, extract_printed_page_number, images_to_save, 3 more }`

        Output formatting options for markdown, text, and extracted images

        - `additional_outputs: optional array of string`

          Optional additional output artifacts to save alongside the primary parse output. Each value opts in to generating and persisting one extra file; the empty list (default) saves none. The three accepted values are: 'stripped_md' — per-page markdown stripped of formatting (links, bold/italic, images, HTML), saved as JSON for full-text-search indexing; fetch via `expand=stripped_markdown_content_metadata`. 'concatenated_stripped_txt' — all stripped pages concatenated into a single plain-text file with `\n\n---\n\n` between pages, useful for feeding the document into search or embedding pipelines as one blob; fetch via `expand=concatenated_stripped_markdown_content_metadata`. 'word_bbox' — raw word-level bounding boxes (one JSON object per word, with page number and x/y/w/h coordinates) saved as JSONL, useful for highlighting or grounding extracted answers back to the source document; fetch via `expand=raw_words_content_metadata`.

        - `extract_printed_page_number: optional boolean`

          Extract the printed page number as it appears in the document (e.g., 'Page 5 of 10', 'v', 'A-3'). Useful for referencing original page numbers

        - `images_to_save: optional array of "screenshot" or "embedded" or "layout"`

          Image categories to extract and save. Options: 'screenshot' (full page renders useful for visual QA), 'embedded' (images found within the document), 'layout' (cropped regions from layout detection like figures and diagrams). Empty list saves no images

          - `"screenshot"`

          - `"embedded"`

          - `"layout"`

        - `markdown: optional object { annotate_links, inline_images, tables }`

          Markdown formatting options including table styles and link annotations

          - `annotate_links: optional boolean`

            Add link annotations to markdown output in the format [text](url). When false, only the link text is included

          - `inline_images: optional boolean`

            Embed images directly in markdown as base64 data URIs instead of extracting them as separate files. Useful for self-contained markdown output

          - `tables: optional object { compact_markdown_tables, markdown_table_multiline_separator, merge_continued_tables, output_tables_as_markdown }`

            Table formatting options including markdown vs HTML format and merging behavior

            - `compact_markdown_tables: optional boolean`

              Remove extra whitespace padding in markdown table cells for more compact output

            - `markdown_table_multiline_separator: optional string`

              Separator string for multiline cell content in markdown tables. Example: '<br>' to preserve line breaks, ' ' to join with spaces

            - `merge_continued_tables: optional boolean`

              Automatically merge tables that span multiple pages into a single table. The merged table appears on the first page with merged_from_pages metadata

            - `output_tables_as_markdown: optional boolean`

              Output tables as markdown pipe tables instead of HTML <table> tags. Markdown tables are simpler but cannot represent complex structures like merged cells

        - `spatial_text: optional object { do_not_unroll_columns, preserve_layout_alignment_across_pages, preserve_very_small_text }`

          Spatial text output options for preserving document layout structure

          - `do_not_unroll_columns: optional boolean`

            Keep multi-column layouts intact instead of linearizing columns into sequential text. Automatically enabled for non-fast tiers

          - `preserve_layout_alignment_across_pages: optional boolean`

            Maintain consistent text column alignment across page boundaries. Automatically enabled for document-level parsing modes

          - `preserve_very_small_text: optional boolean`

            Include text below the normal size threshold. Useful for footnotes, watermarks, or fine print that might otherwise be filtered out

        - `tables_as_spreadsheet: optional object { enable, guess_sheet_name }`

          Options for exporting tables as XLSX spreadsheets

          - `enable: optional boolean`

            Whether this option is enabled

          - `guess_sheet_name: optional boolean`

            Automatically generate descriptive sheet names from table context (headers, surrounding text) instead of using generic names like 'Table_1'

      - `page_ranges: optional object { max_pages, target_pages }`

        Page selection: limit total pages or specify exact pages to process

        - `max_pages: optional number`

          Maximum number of pages to process. Pages are processed in order starting from page 1. If both max_pages and target_pages are set, target_pages takes precedence

        - `target_pages: optional string`

          Comma-separated list of specific pages to process using 1-based indexing. Supports individual pages and ranges. Examples: '1,3,5' (pages 1, 3, 5), '1-5' (pages 1 through 5 inclusive), '1,3,5-8,10' (pages 1, 3, 5-8, and 10). Pages are sorted and deduplicated automatically. Duplicate pages cause an error

      - `processing_control: optional object { job_failure_conditions, timeouts }`

        Job execution controls including timeouts and failure thresholds

        - `job_failure_conditions: optional object { allowed_page_failure_ratio, fail_on_buggy_font, fail_on_image_extraction_error, 2 more }`

          Quality thresholds that determine when a job should fail vs complete with partial results

          - `allowed_page_failure_ratio: optional number`

            Maximum ratio of pages allowed to fail before the job fails (0-1). Example: 0.1 means job fails if more than 10% of pages fail. Default is 0.05 (5%)

          - `fail_on_buggy_font: optional boolean`

            Fail the job if a problematic font is detected that may cause incorrect text extraction. Buggy fonts can produce garbled or missing characters

          - `fail_on_image_extraction_error: optional boolean`

            Fail the entire job if any embedded image cannot be extracted. By default, image extraction errors are logged but don't fail the job

          - `fail_on_image_ocr_error: optional boolean`

            Fail the entire job if OCR fails on any image. By default, OCR errors result in empty text for that image

          - `fail_on_markdown_reconstruction_error: optional boolean`

            Fail the entire job if markdown cannot be reconstructed for any page. By default, failed pages use fallback text extraction

        - `timeouts: optional object { base_in_seconds, extra_time_per_page_in_seconds }`

          Timeout settings for job execution. Increase for large or complex documents

          - `base_in_seconds: optional number`

            Base timeout for the job in seconds (max 1800 = 30 minutes). This is the minimum time allowed regardless of document size

          - `extra_time_per_page_in_seconds: optional number`

            Additional timeout per page in seconds (max 300 = 5 minutes). Total timeout = base + (this value × page count)

      - `processing_options: optional object { aggressive_table_extraction, auto_mode_configuration, cost_optimizer, 4 more }`

        Document processing options including OCR, table extraction, and chart parsing

        - `aggressive_table_extraction: optional boolean`

          Use aggressive heuristics to detect table boundaries, even without visible borders. Useful for documents with borderless or complex tables

        - `auto_mode_configuration: optional array of object { parsing_conf, filename_match_glob, filename_match_glob_list, 33 more }`

          Conditional processing rules that apply different parsing options based on page content, document structure, or filename patterns. Each entry defines trigger conditions and the parsing configuration to apply when triggered

          - `parsing_conf: object { adaptive_long_table, aggressive_table_extraction, crop_box, 11 more }`

            Parsing configuration to apply when trigger conditions are met

            - `adaptive_long_table: optional boolean`

              Whether to use adaptive long table handling

            - `aggressive_table_extraction: optional boolean`

              Whether to use aggressive table extraction

            - `crop_box: optional object { bottom, left, right, top }`

              Crop box options for auto mode parsing configuration.

              - `bottom: optional number`

                Bottom boundary of crop box as ratio (0-1)

              - `left: optional number`

                Left boundary of crop box as ratio (0-1)

              - `right: optional number`

                Right boundary of crop box as ratio (0-1)

              - `top: optional number`

                Top boundary of crop box as ratio (0-1)

            - `custom_prompt: optional string`

              Custom AI instructions for matched pages. Overrides the base custom_prompt

            - `extract_layout: optional boolean`

              Whether to extract layout information

            - `high_res_ocr: optional boolean`

              Whether to use high resolution OCR

            - `ignore: optional object { ignore_diagonal_text, ignore_hidden_text }`

              Ignore options for auto mode parsing configuration.

              - `ignore_diagonal_text: optional boolean`

                Whether to ignore diagonal text in the document

              - `ignore_hidden_text: optional boolean`

                Whether to ignore hidden text in the document

            - `language: optional string`

              Primary language of the document

            - `outlined_table_extraction: optional boolean`

              Whether to use outlined table extraction

            - `presentation: optional object { out_of_bounds_content, skip_embedded_data }`

              Presentation-specific options for auto mode parsing configuration.

              - `out_of_bounds_content: optional boolean`

                Extract out of bounds content in presentation slides

              - `skip_embedded_data: optional boolean`

                Skip extraction of embedded data for charts in presentation slides

            - `spatial_text: optional object { do_not_unroll_columns, preserve_layout_alignment_across_pages, preserve_very_small_text }`

              Spatial text options for auto mode parsing configuration.

              - `do_not_unroll_columns: optional boolean`

                Keep column structure intact without unrolling

              - `preserve_layout_alignment_across_pages: optional boolean`

                Preserve text alignment across page boundaries

              - `preserve_very_small_text: optional boolean`

                Include very small text in spatial output

            - `specialized_chart_parsing: optional "agentic_plus" or "agentic" or "efficient"`

              Enable specialized chart parsing with the specified mode

              - `"agentic_plus"`

              - `"agentic"`

              - `"efficient"`

            - `tier: optional "fast" or "cost_effective" or "agentic" or "agentic_plus"`

              Override the parsing tier for matched pages. Must be paired with version

              - `"fast"`

              - `"cost_effective"`

              - `"agentic"`

              - `"agentic_plus"`

            - `version: optional "latest" or "2026-05-13" or "2026-05-11" or 2 more or string`

              Tier version when overriding tier. Required when tier is specified

              - `"latest" or "2026-05-13" or "2026-05-11" or 2 more`

                Tier version when overriding tier. Required when tier is specified

                - `"latest"`

                - `"2026-05-13"`

                - `"2026-05-11"`

                - `"2026-04-09"`

                - `"2025-12-11"`

              - `string`

          - `filename_match_glob: optional string`

            Single glob pattern to match against filename

          - `filename_match_glob_list: optional array of string`

            List of glob patterns to match against filename

          - `filename_regexp: optional string`

            Regex pattern to match against filename

          - `filename_regexp_mode: optional string`

            Regex mode flags (e.g., 'i' for case-insensitive)

          - `full_page_image_in_page: optional boolean`

            Trigger if page contains a full-page image (scanned page detection)

          - `full_page_image_in_page_threshold: optional number or string`

            Threshold for full page image detection (0.0-1.0, default 0.8)

            - `number`

            - `string`

          - `image_in_page: optional boolean`

            Trigger if page contains non-screenshot images

          - `layout_element_in_page: optional string`

            Trigger if page contains this layout element type

          - `layout_element_in_page_confidence_threshold: optional number or string`

            Confidence threshold for layout element detection

            - `number`

            - `string`

          - `page_contains_at_least_n_charts: optional number or string`

            Trigger if page has more than N charts

            - `number`

            - `string`

          - `page_contains_at_least_n_images: optional number or string`

            Trigger if page has more than N images

            - `number`

            - `string`

          - `page_contains_at_least_n_layout_elements: optional number or string`

            Trigger if page has more than N layout elements

            - `number`

            - `string`

          - `page_contains_at_least_n_lines: optional number or string`

            Trigger if page has more than N lines

            - `number`

            - `string`

          - `page_contains_at_least_n_links: optional number or string`

            Trigger if page has more than N links

            - `number`

            - `string`

          - `page_contains_at_least_n_numbers: optional number or string`

            Trigger if page has more than N numeric words

            - `number`

            - `string`

          - `page_contains_at_least_n_percent_numbers: optional number or string`

            Trigger if page has more than N% numeric words

            - `number`

            - `string`

          - `page_contains_at_least_n_tables: optional number or string`

            Trigger if page has more than N tables

            - `number`

            - `string`

          - `page_contains_at_least_n_words: optional number or string`

            Trigger if page has more than N words

            - `number`

            - `string`

          - `page_contains_at_most_n_charts: optional number or string`

            Trigger if page has fewer than N charts

            - `number`

            - `string`

          - `page_contains_at_most_n_images: optional number or string`

            Trigger if page has fewer than N images

            - `number`

            - `string`

          - `page_contains_at_most_n_layout_elements: optional number or string`

            Trigger if page has fewer than N layout elements

            - `number`

            - `string`

          - `page_contains_at_most_n_lines: optional number or string`

            Trigger if page has fewer than N lines

            - `number`

            - `string`

          - `page_contains_at_most_n_links: optional number or string`

            Trigger if page has fewer than N links

            - `number`

            - `string`

          - `page_contains_at_most_n_numbers: optional number or string`

            Trigger if page has fewer than N numeric words

            - `number`

            - `string`

          - `page_contains_at_most_n_percent_numbers: optional number or string`

            Trigger if page has fewer than N% numeric words

            - `number`

            - `string`

          - `page_contains_at_most_n_tables: optional number or string`

            Trigger if page has fewer than N tables

            - `number`

            - `string`

          - `page_contains_at_most_n_words: optional number or string`

            Trigger if page has fewer than N words

            - `number`

            - `string`

          - `page_longer_than_n_chars: optional number or string`

            Trigger if page has more than N characters

            - `number`

            - `string`

          - `page_md_error: optional boolean`

            Trigger on pages with markdown extraction errors

          - `page_shorter_than_n_chars: optional number or string`

            Trigger if page has fewer than N characters

            - `number`

            - `string`

          - `regexp_in_page: optional string`

            Regex pattern to match in page content

          - `regexp_in_page_mode: optional string`

            Regex mode flags for regexp_in_page

          - `table_in_page: optional boolean`

            Trigger if page contains a table

          - `text_in_page: optional string`

            Trigger if page text/markdown contains this string

          - `trigger_mode: optional string`

            How to combine multiple trigger conditions: 'and' (all conditions must match, this is the default) or 'or' (any single condition can trigger)

        - `cost_optimizer: optional object { enable }`

          Cost optimizer configuration for reducing parsing costs on simpler pages.

          When enabled, the parser analyzes each page and routes simpler pages to faster,
          cheaper processing while preserving quality for complex pages. Only works with
          'agentic' or 'agentic_plus' tiers.

          - `enable: optional boolean`

            Enable cost-optimized parsing. Routes simpler pages to faster processing while complex pages use full AI analysis. May reduce speed on some documents. IMPORTANT: Only available with 'agentic' or 'agentic_plus' tiers

        - `disable_heuristics: optional boolean`

          Disable automatic heuristics including outlined table extraction and adaptive long table handling. Use when heuristics produce incorrect results

        - `ignore: optional object { ignore_diagonal_text, ignore_hidden_text, ignore_text_in_image }`

          Options for ignoring specific text types (diagonal, hidden, text in images)

          - `ignore_diagonal_text: optional boolean`

            Skip text rotated at an angle (not horizontal/vertical). Useful for ignoring watermarks or decorative angled text

          - `ignore_hidden_text: optional boolean`

            Skip text marked as hidden in the document structure. Some PDFs contain invisible text layers used for accessibility or search indexing

          - `ignore_text_in_image: optional boolean`

            Skip OCR text extraction from embedded images. Use when images contain irrelevant text (watermarks, logos) that shouldn't be in the output

        - `ocr_parameters: optional object { languages }`

          OCR configuration including language detection settings

          - `languages: optional array of ParsingLanguages`

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

        - `specialized_chart_parsing: optional "agentic_plus" or "agentic" or "efficient"`

          Enable AI-powered chart analysis. Modes: 'efficient' (fast, lower cost), 'agentic' (balanced), 'agentic_plus' (highest accuracy). Automatically enables extract_layout and precise_bounding_box when set

          - `"agentic_plus"`

          - `"agentic"`

          - `"efficient"`

      - `webhook_configurations: optional array of object { webhook_events, webhook_headers, webhook_url }`

        Webhook endpoints for job status notifications. Multiple webhooks can be configured for different events or services

        - `webhook_events: optional array of string`

          Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

        - `webhook_headers: optional map[unknown]`

          Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

        - `webhook_url: optional string`

          HTTPS URL to receive webhook POST requests. Must be publicly accessible

    - `SpreadsheetV1 = object { product_type, extraction_range, flatten_hierarchical_tables, 6 more }`

      Typed parameters for a *spreadsheet v1* product configuration.

      - `product_type: "spreadsheet_v1"`

        Product type.

        - `"spreadsheet_v1"`

      - `extraction_range: optional string`

        A1 notation of the range to extract a single region from. If None, the entire sheet is used.

      - `flatten_hierarchical_tables: optional boolean`

        Return a flattened dataframe when a detected table is recognized as hierarchical.

      - `generate_additional_metadata: optional boolean`

        Whether to generate additional metadata (title, description) for each extracted region.

      - `include_hidden_cells: optional boolean`

        Whether to include hidden cells when extracting regions from the spreadsheet.

      - `sheet_names: optional array of string`

        The names of the sheets to extract regions from. If empty, all sheets will be processed.

      - `specialization: optional string`

        Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

      - `table_merge_sensitivity: optional "strong" or "weak"`

        Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

        - `"strong"`

        - `"weak"`

      - `use_experimental_processing: optional boolean`

        Enables experimental processing. Accuracy may be impacted.

    - `UntypedParameters = object { product_type }`

      Catch-all for configurations without a dedicated typed schema.

      Accepts arbitrary JSON fields alongside `product_type`.

      - `product_type: "unknown"`

        Product type.

        - `"unknown"`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v2/extract/schema/generate \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{}'
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

- `ExtractConfiguration = object { data_schema, cite_sources, confidence_scores, 8 more }`

  Extract configuration combining parse and extract settings.

  - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

    JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

  - `cite_sources: optional boolean`

    Include citations in results

  - `confidence_scores: optional boolean`

    Include confidence scores in results

  - `extract_version: optional string`

    Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

  - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

    Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

    - `"per_doc"`

    - `"per_page"`

    - `"per_table_row"`

  - `max_pages: optional number`

    Maximum number of pages to process. Omit for no limit.

  - `parse_config_id: optional string`

    Saved parse configuration ID to control how the document is parsed before extraction

  - `parse_tier: optional string`

    Parse tier to use before extraction. Defaults to the extract tier if not specified.

  - `system_prompt: optional string`

    Custom system prompt to guide extraction behavior

  - `target_pages: optional string`

    Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `tier: optional "cost_effective" or "agentic"`

    Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

    - `"cost_effective"`

    - `"agentic"`

### Extract Job Metadata

- `ExtractJobMetadata = object { field_metadata, parse_job_id, parse_tier }`

  Extraction metadata.

  - `field_metadata: optional ExtractedFieldMetadata`

    Metadata for extracted fields including document, page, and row level info.

    - `document_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

      Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `page_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

      Per-page metadata when extraction_target is per_page

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `row_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

      Per-row metadata when extraction_target is per_table_row

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

  - `parse_job_id: optional string`

    Reference to the ParseJob ID used for parsing

  - `parse_tier: optional string`

    Parse tier used for parsing the document

### Extract Job Usage

- `ExtractJobUsage = object { num_document_tokens, num_output_tokens, num_pages_extracted }`

  Extraction usage metrics.

  - `num_document_tokens: optional number`

    Number of document tokens

  - `num_output_tokens: optional number`

    Number of output tokens

  - `num_pages_extracted: optional number`

    Number of pages extracted

### Extract V2 Job

- `ExtractV2Job = object { id, created_at, file_input, 9 more }`

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

  - `configuration: optional ExtractConfiguration`

    Extract configuration combining parse and extract settings.

    - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources: optional boolean`

      Include citations in results

    - `confidence_scores: optional boolean`

      Include confidence scores in results

    - `extract_version: optional string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: optional number`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: optional string`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: optional string`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: optional string`

      Custom system prompt to guide extraction behavior

    - `target_pages: optional string`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: optional "cost_effective" or "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: optional string`

    Saved extract configuration ID used for this job, if any

  - `error_message: optional string`

    Error details when status is FAILED

  - `extract_metadata: optional ExtractJobMetadata`

    Extraction metadata.

    - `field_metadata: optional ExtractedFieldMetadata`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `page_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

        Per-page metadata when extraction_target is per_page

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `row_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

        Per-row metadata when extraction_target is per_table_row

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

    - `parse_job_id: optional string`

      Reference to the ParseJob ID used for parsing

    - `parse_tier: optional string`

      Parse tier used for parsing the document

  - `extract_result: optional map[map[unknown] or array of unknown or string or 2 more] or array of map[map[unknown] or array of unknown or string or 2 more]`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `map[map[unknown] or array of unknown or string or 2 more]`

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `array of map[map[unknown] or array of unknown or string or 2 more]`

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

  - `metadata: optional object { usage }`

    Job-level metadata.

    - `usage: optional ExtractJobUsage`

      Extraction usage metrics.

      - `num_document_tokens: optional number`

        Number of document tokens

      - `num_output_tokens: optional number`

        Number of output tokens

      - `num_pages_extracted: optional number`

        Number of pages extracted

### Extract V2 Job Create

- `ExtractV2JobCreate = object { file_input, configuration, configuration_id, webhook_configurations }`

  Request to create an extraction job. Provide configuration_id or inline configuration.

  - `file_input: string`

    File ID or parse job ID to extract from

  - `configuration: optional ExtractConfiguration`

    Extract configuration combining parse and extract settings.

    - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `map[unknown]`

      - `array of unknown`

      - `string`

      - `number`

      - `boolean`

    - `cite_sources: optional boolean`

      Include citations in results

    - `confidence_scores: optional boolean`

      Include confidence scores in results

    - `extract_version: optional string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: optional number`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: optional string`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: optional string`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: optional string`

      Custom system prompt to guide extraction behavior

    - `target_pages: optional string`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: optional "cost_effective" or "agentic"`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: optional string`

    Saved configuration ID

  - `webhook_configurations: optional array of object { webhook_events, webhook_headers, webhook_output_format, webhook_url }`

    Outbound webhook endpoints to notify on job status changes

    - `webhook_events: optional array of "extract.pending" or "extract.success" or "extract.error" or 14 more`

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

    - `webhook_headers: optional map[string]`

      Custom HTTP headers sent with each webhook request (e.g. auth tokens)

    - `webhook_output_format: optional string`

      Response format sent to the webhook: 'string' (default) or 'json'

    - `webhook_url: optional string`

      URL to receive webhook POST notifications

### Extract V2 Job Query Response

- `ExtractV2JobQueryResponse = object { items, next_page_token, total_size }`

  Paginated list of extraction jobs.

  - `items: array of ExtractV2Job`

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

    - `configuration: optional ExtractConfiguration`

      Extract configuration combining parse and extract settings.

      - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

        JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `cite_sources: optional boolean`

        Include citations in results

      - `confidence_scores: optional boolean`

        Include confidence scores in results

      - `extract_version: optional string`

        Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

      - `extraction_target: optional "per_doc" or "per_page" or "per_table_row"`

        Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

        - `"per_doc"`

        - `"per_page"`

        - `"per_table_row"`

      - `max_pages: optional number`

        Maximum number of pages to process. Omit for no limit.

      - `parse_config_id: optional string`

        Saved parse configuration ID to control how the document is parsed before extraction

      - `parse_tier: optional string`

        Parse tier to use before extraction. Defaults to the extract tier if not specified.

      - `system_prompt: optional string`

        Custom system prompt to guide extraction behavior

      - `target_pages: optional string`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

      - `tier: optional "cost_effective" or "agentic"`

        Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

        - `"cost_effective"`

        - `"agentic"`

    - `configuration_id: optional string`

      Saved extract configuration ID used for this job, if any

    - `error_message: optional string`

      Error details when status is FAILED

    - `extract_metadata: optional ExtractJobMetadata`

      Extraction metadata.

      - `field_metadata: optional ExtractedFieldMetadata`

        Metadata for extracted fields including document, page, and row level info.

        - `document_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

          Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

          - `map[unknown]`

          - `array of unknown`

          - `string`

          - `number`

          - `boolean`

        - `page_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

          Per-page metadata when extraction_target is per_page

          - `map[unknown]`

          - `array of unknown`

          - `string`

          - `number`

          - `boolean`

        - `row_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

          Per-row metadata when extraction_target is per_table_row

          - `map[unknown]`

          - `array of unknown`

          - `string`

          - `number`

          - `boolean`

      - `parse_job_id: optional string`

        Reference to the ParseJob ID used for parsing

      - `parse_tier: optional string`

        Parse tier used for parsing the document

    - `extract_result: optional map[map[unknown] or array of unknown or string or 2 more] or array of map[map[unknown] or array of unknown or string or 2 more]`

      Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

      - `map[map[unknown] or array of unknown or string or 2 more]`

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

      - `array of map[map[unknown] or array of unknown or string or 2 more]`

        - `map[unknown]`

        - `array of unknown`

        - `string`

        - `number`

        - `boolean`

    - `metadata: optional object { usage }`

      Job-level metadata.

      - `usage: optional ExtractJobUsage`

        Extraction usage metrics.

        - `num_document_tokens: optional number`

          Number of document tokens

        - `num_output_tokens: optional number`

          Number of output tokens

        - `num_pages_extracted: optional number`

          Number of pages extracted

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Extract V2 Schema Generate Request

- `ExtractV2SchemaGenerateRequest = object { data_schema, file_id, name, prompt }`

  Request schema for generating an extraction schema.

  - `data_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

    Optional schema to validate, refine, or extend

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

  - `file_id: optional string`

    Optional file ID to analyze for schema generation

  - `name: optional string`

    Name for the generated configuration (auto-generated if omitted)

  - `prompt: optional string`

    Natural language description of the data structure to extract

### Extract V2 Schema Validate Request

- `ExtractV2SchemaValidateRequest = object { data_schema }`

  Request schema for validating an extraction schema.

  - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

    JSON Schema to validate for use with extract jobs

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

### Extract V2 Schema Validate Response

- `ExtractV2SchemaValidateResponse = object { data_schema }`

  Response schema for schema validation.

  - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

    Validated JSON Schema, ready for use in extract jobs

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

### Extracted Field Metadata

- `ExtractedFieldMetadata = object { document_metadata, page_metadata, row_metadata }`

  Metadata for extracted fields including document, page, and row level info.

  - `document_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

  - `page_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

    Per-page metadata when extraction_target is per_page

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

  - `row_metadata: optional array of map[map[unknown] or array of unknown or string or 2 more]`

    Per-row metadata when extraction_target is per_table_row

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

### Extract Delete Response

- `ExtractDeleteResponse = unknown`
