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
