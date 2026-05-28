# Extract

## Create Extract Job

`extract.create(ExtractCreateParams**kwargs)  -> ExtractV2Job`

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

- `file_input: str`

  File ID or parse job ID to extract from

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `configuration: Optional[ExtractConfigurationParam]`

  Extract configuration combining parse and extract settings.

  - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

    JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `cite_sources: Optional[bool]`

    Include citations in results

  - `confidence_scores: Optional[bool]`

    Include confidence scores in results

  - `extract_version: Optional[str]`

    Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

  - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

    Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

    - `"per_doc"`

    - `"per_page"`

    - `"per_table_row"`

  - `max_pages: Optional[int]`

    Maximum number of pages to process. Omit for no limit.

  - `parse_config_id: Optional[str]`

    Saved parse configuration ID to control how the document is parsed before extraction

  - `parse_tier: Optional[str]`

    Parse tier to use before extraction. Defaults to the extract tier if not specified.

  - `system_prompt: Optional[str]`

    Custom system prompt to guide extraction behavior

  - `target_pages: Optional[str]`

    Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `tier: Optional[Literal["cost_effective", "agentic"]]`

    Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

    - `"cost_effective"`

    - `"agentic"`

- `configuration_id: Optional[str]`

  Saved configuration ID

- `webhook_configurations: Optional[Iterable[WebhookConfiguration]]`

  Outbound webhook endpoints to notify on job status changes

  - `webhook_events: Optional[List[Literal["extract.pending", "extract.success", "extract.error", 14 more]]]`

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

  - `webhook_headers: Optional[Dict[str, str]]`

    Custom HTTP headers sent with each webhook request (e.g. auth tokens)

  - `webhook_output_format: Optional[str]`

    Response format sent to the webhook: 'string' (default) or 'json'

  - `webhook_url: Optional[str]`

    URL to receive webhook POST notifications

### Returns

- `class ExtractV2Job: …`

  An extraction job.

  - `id: str`

    Unique job identifier (job_id)

  - `created_at: datetime`

    Creation timestamp

  - `file_input: str`

    File ID or parse job ID that was extracted

  - `project_id: str`

    Project this job belongs to

  - `status: str`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `updated_at: datetime`

    Last update timestamp

  - `configuration: Optional[ExtractConfiguration]`

    Extract configuration combining parse and extract settings.

    - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `cite_sources: Optional[bool]`

      Include citations in results

    - `confidence_scores: Optional[bool]`

      Include confidence scores in results

    - `extract_version: Optional[str]`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: Optional[int]`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: Optional[str]`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: Optional[str]`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: Optional[str]`

      Custom system prompt to guide extraction behavior

    - `target_pages: Optional[str]`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: Optional[Literal["cost_effective", "agentic"]]`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: Optional[str]`

    Saved extract configuration ID used for this job, if any

  - `error_message: Optional[str]`

    Error details when status is FAILED

  - `extract_metadata: Optional[ExtractJobMetadata]`

    Extraction metadata.

    - `field_metadata: Optional[ExtractedFieldMetadata]`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

        Per-page metadata when extraction_target is per_page

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

        Per-row metadata when extraction_target is per_table_row

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

    - `parse_job_id: Optional[str]`

      Reference to the ParseJob ID used for parsing

    - `parse_tier: Optional[str]`

      Parse tier used for parsing the document

  - `extract_result: Optional[Union[Dict[str, Union[Dict[str, object], List[object], str, 3 more]], List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]], null]]`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

  - `metadata: Optional[Metadata]`

    Job-level metadata.

    - `usage: Optional[ExtractJobUsage]`

      Extraction usage metrics.

      - `num_document_tokens: Optional[int]`

        Number of document tokens

      - `num_output_tokens: Optional[int]`

        Number of output tokens

      - `num_pages_extracted: Optional[int]`

        Number of pages extracted

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
extract_v2_job = client.extract.create(
    file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
)
print(extract_v2_job.id)
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

`extract.list(ExtractListParams**kwargs)  -> SyncPaginatedCursor[ExtractV2Job]`

**get** `/api/v2/extract`

List extraction jobs with optional filtering and pagination.

Filter by `configuration_id`, `status`, `file_input`,
or creation date range. Results are returned newest-first.
Use `expand=configuration` to include the full configuration used,
and `expand=extract_metadata` for per-field metadata.

### Parameters

- `configuration_id: Optional[str]`

  Filter by configuration ID

- `created_at_on_or_after: Optional[Union[str, datetime, null]]`

  Include items created at or after this timestamp (inclusive)

- `created_at_on_or_before: Optional[Union[str, datetime, null]]`

  Include items created at or before this timestamp (inclusive)

- `document_input_type: Optional[str]`

  Filter by document input type (file_id or parse_job_id)

- `document_input_value: Optional[str]`

  Deprecated: use file_input instead

- `expand: Optional[SequenceNotStr[str]]`

  Additional fields to include: configuration, extract_metadata

- `file_input: Optional[str]`

  Filter by file input value

- `job_ids: Optional[SequenceNotStr[str]]`

  Filter by specific job IDs

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

  Number of items per page

- `page_token: Optional[str]`

  Token for pagination

- `project_id: Optional[str]`

- `status: Optional[Literal["PENDING", "THROTTLED", "RUNNING", 3 more]]`

  Filter by status

  - `"PENDING"`

  - `"THROTTLED"`

  - `"RUNNING"`

  - `"COMPLETED"`

  - `"FAILED"`

  - `"CANCELLED"`

### Returns

- `class ExtractV2Job: …`

  An extraction job.

  - `id: str`

    Unique job identifier (job_id)

  - `created_at: datetime`

    Creation timestamp

  - `file_input: str`

    File ID or parse job ID that was extracted

  - `project_id: str`

    Project this job belongs to

  - `status: str`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `updated_at: datetime`

    Last update timestamp

  - `configuration: Optional[ExtractConfiguration]`

    Extract configuration combining parse and extract settings.

    - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `cite_sources: Optional[bool]`

      Include citations in results

    - `confidence_scores: Optional[bool]`

      Include confidence scores in results

    - `extract_version: Optional[str]`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: Optional[int]`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: Optional[str]`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: Optional[str]`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: Optional[str]`

      Custom system prompt to guide extraction behavior

    - `target_pages: Optional[str]`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: Optional[Literal["cost_effective", "agentic"]]`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: Optional[str]`

    Saved extract configuration ID used for this job, if any

  - `error_message: Optional[str]`

    Error details when status is FAILED

  - `extract_metadata: Optional[ExtractJobMetadata]`

    Extraction metadata.

    - `field_metadata: Optional[ExtractedFieldMetadata]`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

        Per-page metadata when extraction_target is per_page

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

        Per-row metadata when extraction_target is per_table_row

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

    - `parse_job_id: Optional[str]`

      Reference to the ParseJob ID used for parsing

    - `parse_tier: Optional[str]`

      Parse tier used for parsing the document

  - `extract_result: Optional[Union[Dict[str, Union[Dict[str, object], List[object], str, 3 more]], List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]], null]]`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

  - `metadata: Optional[Metadata]`

    Job-level metadata.

    - `usage: Optional[ExtractJobUsage]`

      Extraction usage metrics.

      - `num_document_tokens: Optional[int]`

        Number of document tokens

      - `num_output_tokens: Optional[int]`

        Number of output tokens

      - `num_pages_extracted: Optional[int]`

        Number of pages extracted

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.extract.list()
page = page.items[0]
print(page.id)
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

`extract.get(strjob_id, ExtractGetParams**kwargs)  -> ExtractV2Job`

**get** `/api/v2/extract/{job_id}`

Get a single extraction job by ID.

Returns the job status and results when complete.
Use `expand=configuration` to include the full configuration used,
and `expand=extract_metadata` for per-field metadata.

### Parameters

- `job_id: str`

- `expand: Optional[SequenceNotStr[str]]`

  Additional fields to include: configuration, extract_metadata

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class ExtractV2Job: …`

  An extraction job.

  - `id: str`

    Unique job identifier (job_id)

  - `created_at: datetime`

    Creation timestamp

  - `file_input: str`

    File ID or parse job ID that was extracted

  - `project_id: str`

    Project this job belongs to

  - `status: str`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `updated_at: datetime`

    Last update timestamp

  - `configuration: Optional[ExtractConfiguration]`

    Extract configuration combining parse and extract settings.

    - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `cite_sources: Optional[bool]`

      Include citations in results

    - `confidence_scores: Optional[bool]`

      Include confidence scores in results

    - `extract_version: Optional[str]`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: Optional[int]`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: Optional[str]`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: Optional[str]`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: Optional[str]`

      Custom system prompt to guide extraction behavior

    - `target_pages: Optional[str]`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: Optional[Literal["cost_effective", "agentic"]]`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: Optional[str]`

    Saved extract configuration ID used for this job, if any

  - `error_message: Optional[str]`

    Error details when status is FAILED

  - `extract_metadata: Optional[ExtractJobMetadata]`

    Extraction metadata.

    - `field_metadata: Optional[ExtractedFieldMetadata]`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

        Per-page metadata when extraction_target is per_page

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

        Per-row metadata when extraction_target is per_table_row

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

    - `parse_job_id: Optional[str]`

      Reference to the ParseJob ID used for parsing

    - `parse_tier: Optional[str]`

      Parse tier used for parsing the document

  - `extract_result: Optional[Union[Dict[str, Union[Dict[str, object], List[object], str, 3 more]], List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]], null]]`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

  - `metadata: Optional[Metadata]`

    Job-level metadata.

    - `usage: Optional[ExtractJobUsage]`

      Extraction usage metrics.

      - `num_document_tokens: Optional[int]`

        Number of document tokens

      - `num_output_tokens: Optional[int]`

        Number of output tokens

      - `num_pages_extracted: Optional[int]`

        Number of pages extracted

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
extract_v2_job = client.extract.get(
    job_id="job_id",
)
print(extract_v2_job.id)
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

`extract.delete(strjob_id, ExtractDeleteParams**kwargs)  -> object`

**delete** `/api/v2/extract/{job_id}`

Delete an extraction job and its results.

### Parameters

- `job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `object`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
extract = client.extract.delete(
    job_id="job_id",
)
print(extract)
```

#### Response

```json
{}
```

## Validate Extraction Schema

`extract.validate_schema(ExtractValidateSchemaParams**kwargs)  -> ExtractV2SchemaValidateResponse`

**post** `/api/v2/extract/schema/validation`

Validate a JSON schema for extraction.

### Parameters

- `data_schema: Dict[str, Union[Dict[str, object], Iterable[object], str, 3 more]]`

  JSON Schema to validate for use with extract jobs

  - `Dict[str, object]`

  - `Iterable[object]`

  - `str`

  - `float`

  - `bool`

### Returns

- `class ExtractV2SchemaValidateResponse: …`

  Response schema for schema validation.

  - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

    Validated JSON Schema, ready for use in extract jobs

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
extract_v2_schema_validate_response = client.extract.validate_schema(
    data_schema={
        "foo": {
            "foo": "bar"
        }
    },
)
print(extract_v2_schema_validate_response.data_schema)
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

`extract.generate_schema(ExtractGenerateSchemaParams**kwargs)  -> ConfigurationCreate`

**post** `/api/v2/extract/schema/generate`

Generate a JSON schema and return a product configuration request.

### Parameters

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `data_schema: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, 3 more]]]`

  Optional schema to validate, refine, or extend

  - `Dict[str, object]`

  - `Iterable[object]`

  - `str`

  - `float`

  - `bool`

- `file_id: Optional[str]`

  Optional file ID to analyze for schema generation

- `name: Optional[str]`

  Name for the generated configuration (auto-generated if omitted)

- `prompt: Optional[str]`

  Natural language description of the data structure to extract

### Returns

- `class ConfigurationCreate: …`

  Request body for creating a product configuration.

  - `name: str`

    Human-readable name for this configuration.

  - `parameters: Parameters`

    Product-specific configuration parameters.

    - `class SplitV1Parameters: …`

      Typed parameters for a *split v1* product configuration.

      - `categories: List[SplitCategory]`

        Categories to split documents into.

        - `name: str`

          Name of the category.

        - `description: Optional[str]`

          Optional description of what content belongs in this category.

      - `product_type: Literal["split_v1"]`

        Product type.

        - `"split_v1"`

      - `splitting_strategy: Optional[SplittingStrategy]`

        Strategy for splitting documents.

        - `allow_uncategorized: Optional[Literal["include", "forbid", "omit"]]`

          Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

          - `"include"`

          - `"forbid"`

          - `"omit"`

    - `class ExtractV2Parameters: …`

      Typed parameters for an *extract v2* product configuration.

      - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

        JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `product_type: Literal["extract_v2"]`

        Product type.

        - `"extract_v2"`

      - `cite_sources: Optional[bool]`

        Include citations in results

      - `confidence_scores: Optional[bool]`

        Include confidence scores in results

      - `extract_version: Optional[str]`

        Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

      - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

        Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

        - `"per_doc"`

        - `"per_page"`

        - `"per_table_row"`

      - `max_pages: Optional[int]`

        Maximum number of pages to process. Omit for no limit.

      - `parse_config_id: Optional[str]`

        Saved parse configuration ID to control how the document is parsed before extraction

      - `parse_tier: Optional[str]`

        Parse tier to use before extraction. Defaults to the extract tier if not specified.

      - `system_prompt: Optional[str]`

        Custom system prompt to guide extraction behavior

      - `target_pages: Optional[str]`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

      - `tier: Optional[Literal["cost_effective", "agentic"]]`

        Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

        - `"cost_effective"`

        - `"agentic"`

    - `class ClassifyV2Parameters: …`

      Typed parameters for a *classify v2* product configuration.

      - `product_type: Literal["classify_v2"]`

        Product type.

        - `"classify_v2"`

      - `rules: List[Rule]`

        Classify rules to evaluate against the document (at least one required)

        - `description: str`

          Natural language criteria for matching this rule

        - `type: str`

          Document type to assign when rule matches

      - `mode: Optional[Literal["FAST"]]`

        Classify execution mode

        - `"FAST"`

      - `parsing_configuration: Optional[ParsingConfiguration]`

        Parsing configuration for classify jobs.

        - `lang: Optional[str]`

          ISO 639-1 language code for the document

        - `max_pages: Optional[int]`

          Maximum number of pages to process. Omit for no limit.

        - `target_pages: Optional[str]`

          Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `class ParseV2Parameters: …`

      Configuration for LlamaParse v2 document parsing.

      Includes tier selection, processing options, output formatting,
      page targeting, and webhook delivery. Refer to the LlamaParse
      documentation for details on each field.

      - `product_type: Literal["parse_v2"]`

        Product type.

        - `"parse_v2"`

      - `tier: Literal["fast", "cost_effective", "agentic", "agentic_plus"]`

        Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced), 'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with highest accuracy)

        - `"fast"`

        - `"cost_effective"`

        - `"agentic"`

        - `"agentic_plus"`

      - `version: Union[Literal["latest", "2026-05-13", "2026-05-11", 2 more], str]`

        Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

        - `Literal["latest", "2026-05-13", "2026-05-11", 2 more]`

          Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

          - `"latest"`

          - `"2026-05-13"`

          - `"2026-05-11"`

          - `"2026-04-09"`

          - `"2025-12-11"`

        - `str`

      - `agentic_options: Optional[AgenticOptions]`

        Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

        These options customize how the AI processes and interprets document content.
        Only applicable when using non-fast tiers.

        - `custom_prompt: Optional[str]`

          Custom instructions for the AI parser. Use to guide extraction behavior, specify output formatting, or provide domain-specific context. Example: 'Extract financial tables with currency symbols. Format dates as YYYY-MM-DD.'

      - `client_name: Optional[str]`

        Identifier for the client/application making the request. Used for analytics and debugging. Example: 'my-app-v2'

      - `crop_box: Optional[CropBox]`

        Crop boundaries to process only a portion of each page. Values are ratios 0-1 from page edges

        - `bottom: Optional[float]`

          Bottom boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content below this line is excluded

        - `left: Optional[float]`

          Left boundary as ratio (0-1). 0=left edge, 1=right edge. Content left of this line is excluded

        - `right: Optional[float]`

          Right boundary as ratio (0-1). 0=left edge, 1=right edge. Content right of this line is excluded

        - `top: Optional[float]`

          Top boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content above this line is excluded

      - `disable_cache: Optional[bool]`

        Bypass result caching and force re-parsing. Use when document content may have changed or you need fresh results

      - `fast_options: Optional[object]`

        Options for fast tier parsing (rule-based, no AI).

        Fast tier uses deterministic algorithms for text extraction without AI enhancement.
        It's the fastest and most cost-effective option, best suited for simple documents
        with standard layouts. Currently has no configurable options but reserved for
        future expansion.

      - `input_options: Optional[InputOptions]`

        Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on detected input file type

        - `html: Optional[InputOptionsHTML]`

          HTML/web page parsing options (applies to .html, .htm files)

          - `make_all_elements_visible: Optional[bool]`

            Force all HTML elements to be visible by overriding CSS display/visibility properties. Useful for parsing pages with hidden content or collapsed sections

          - `remove_fixed_elements: Optional[bool]`

            Remove fixed-position elements (headers, footers, floating buttons) that appear on every page render

          - `remove_navigation_elements: Optional[bool]`

            Remove navigation elements (nav bars, sidebars, menus) to focus on main content

        - `pdf: Optional[object]`

          PDF-specific parsing options (applies to .pdf files)

        - `presentation: Optional[InputOptionsPresentation]`

          Presentation parsing options (applies to .pptx, .ppt, .odp, .key files)

          - `out_of_bounds_content: Optional[bool]`

            Extract content positioned outside the visible slide area. Some presentations have hidden notes or content that extends beyond slide boundaries

          - `skip_embedded_data: Optional[bool]`

            Skip extraction of embedded chart data tables. When true, only the visual representation of charts is captured, not the underlying data

        - `spreadsheet: Optional[InputOptionsSpreadsheet]`

          Spreadsheet parsing options (applies to .xlsx, .xls, .csv, .ods files)

          - `detect_sub_tables_in_sheets: Optional[bool]`

            Detect and extract multiple tables within a single sheet. Useful when spreadsheets contain several data regions separated by blank rows/columns

          - `force_formula_computation_in_sheets: Optional[bool]`

            Compute formula results instead of extracting formula text. Use when you need calculated values rather than formula definitions

          - `include_hidden_sheets: Optional[bool]`

            Parse hidden sheets in addition to visible ones. By default, hidden sheets are skipped

      - `output_options: Optional[OutputOptions]`

        Output formatting options for markdown, text, and extracted images

        - `additional_outputs: Optional[List[str]]`

          Optional additional output artifacts to save alongside the primary parse output. Each value opts in to generating and persisting one extra file; the empty list (default) saves none. The three accepted values are: 'stripped_md' — per-page markdown stripped of formatting (links, bold/italic, images, HTML), saved as JSON for full-text-search indexing; fetch via `expand=stripped_markdown_content_metadata`. 'concatenated_stripped_txt' — all stripped pages concatenated into a single plain-text file with `\n\n---\n\n` between pages, useful for feeding the document into search or embedding pipelines as one blob; fetch via `expand=concatenated_stripped_markdown_content_metadata`. 'word_bbox' — raw word-level bounding boxes (one JSON object per word, with page number and x/y/w/h coordinates) saved as JSONL, useful for highlighting or grounding extracted answers back to the source document; fetch via `expand=raw_words_content_metadata`.

        - `extract_printed_page_number: Optional[bool]`

          Extract the printed page number as it appears in the document (e.g., 'Page 5 of 10', 'v', 'A-3'). Useful for referencing original page numbers

        - `images_to_save: Optional[List[Literal["screenshot", "embedded", "layout"]]]`

          Image categories to extract and save. Options: 'screenshot' (full page renders useful for visual QA), 'embedded' (images found within the document), 'layout' (cropped regions from layout detection like figures and diagrams). Empty list saves no images

          - `"screenshot"`

          - `"embedded"`

          - `"layout"`

        - `markdown: Optional[OutputOptionsMarkdown]`

          Markdown formatting options including table styles and link annotations

          - `annotate_links: Optional[bool]`

            Add link annotations to markdown output in the format [text](url). When false, only the link text is included

          - `inline_images: Optional[bool]`

            Embed images directly in markdown as base64 data URIs instead of extracting them as separate files. Useful for self-contained markdown output

          - `tables: Optional[OutputOptionsMarkdownTables]`

            Table formatting options including markdown vs HTML format and merging behavior

            - `compact_markdown_tables: Optional[bool]`

              Remove extra whitespace padding in markdown table cells for more compact output

            - `markdown_table_multiline_separator: Optional[str]`

              Separator string for multiline cell content in markdown tables. Example: '<br>' to preserve line breaks, ' ' to join with spaces

            - `merge_continued_tables: Optional[bool]`

              Automatically merge tables that span multiple pages into a single table. The merged table appears on the first page with merged_from_pages metadata

            - `output_tables_as_markdown: Optional[bool]`

              Output tables as markdown pipe tables instead of HTML <table> tags. Markdown tables are simpler but cannot represent complex structures like merged cells

        - `spatial_text: Optional[OutputOptionsSpatialText]`

          Spatial text output options for preserving document layout structure

          - `do_not_unroll_columns: Optional[bool]`

            Keep multi-column layouts intact instead of linearizing columns into sequential text. Automatically enabled for non-fast tiers

          - `preserve_layout_alignment_across_pages: Optional[bool]`

            Maintain consistent text column alignment across page boundaries. Automatically enabled for document-level parsing modes

          - `preserve_very_small_text: Optional[bool]`

            Include text below the normal size threshold. Useful for footnotes, watermarks, or fine print that might otherwise be filtered out

        - `tables_as_spreadsheet: Optional[OutputOptionsTablesAsSpreadsheet]`

          Options for exporting tables as XLSX spreadsheets

          - `enable: Optional[bool]`

            Whether this option is enabled

          - `guess_sheet_name: Optional[bool]`

            Automatically generate descriptive sheet names from table context (headers, surrounding text) instead of using generic names like 'Table_1'

      - `page_ranges: Optional[PageRanges]`

        Page selection: limit total pages or specify exact pages to process

        - `max_pages: Optional[int]`

          Maximum number of pages to process. Pages are processed in order starting from page 1. If both max_pages and target_pages are set, target_pages takes precedence

        - `target_pages: Optional[str]`

          Comma-separated list of specific pages to process using 1-based indexing. Supports individual pages and ranges. Examples: '1,3,5' (pages 1, 3, 5), '1-5' (pages 1 through 5 inclusive), '1,3,5-8,10' (pages 1, 3, 5-8, and 10). Pages are sorted and deduplicated automatically. Duplicate pages cause an error

      - `processing_control: Optional[ProcessingControl]`

        Job execution controls including timeouts and failure thresholds

        - `job_failure_conditions: Optional[ProcessingControlJobFailureConditions]`

          Quality thresholds that determine when a job should fail vs complete with partial results

          - `allowed_page_failure_ratio: Optional[float]`

            Maximum ratio of pages allowed to fail before the job fails (0-1). Example: 0.1 means job fails if more than 10% of pages fail. Default is 0.05 (5%)

          - `fail_on_buggy_font: Optional[bool]`

            Fail the job if a problematic font is detected that may cause incorrect text extraction. Buggy fonts can produce garbled or missing characters

          - `fail_on_image_extraction_error: Optional[bool]`

            Fail the entire job if any embedded image cannot be extracted. By default, image extraction errors are logged but don't fail the job

          - `fail_on_image_ocr_error: Optional[bool]`

            Fail the entire job if OCR fails on any image. By default, OCR errors result in empty text for that image

          - `fail_on_markdown_reconstruction_error: Optional[bool]`

            Fail the entire job if markdown cannot be reconstructed for any page. By default, failed pages use fallback text extraction

        - `timeouts: Optional[ProcessingControlTimeouts]`

          Timeout settings for job execution. Increase for large or complex documents

          - `base_in_seconds: Optional[int]`

            Base timeout for the job in seconds (max 1800 = 30 minutes). This is the minimum time allowed regardless of document size

          - `extra_time_per_page_in_seconds: Optional[int]`

            Additional timeout per page in seconds (max 300 = 5 minutes). Total timeout = base + (this value × page count)

      - `processing_options: Optional[ProcessingOptions]`

        Document processing options including OCR, table extraction, and chart parsing

        - `aggressive_table_extraction: Optional[bool]`

          Use aggressive heuristics to detect table boundaries, even without visible borders. Useful for documents with borderless or complex tables

        - `auto_mode_configuration: Optional[List[ProcessingOptionsAutoModeConfiguration]]`

          Conditional processing rules that apply different parsing options based on page content, document structure, or filename patterns. Each entry defines trigger conditions and the parsing configuration to apply when triggered

          - `parsing_conf: ProcessingOptionsAutoModeConfigurationParsingConf`

            Parsing configuration to apply when trigger conditions are met

            - `adaptive_long_table: Optional[bool]`

              Whether to use adaptive long table handling

            - `aggressive_table_extraction: Optional[bool]`

              Whether to use aggressive table extraction

            - `crop_box: Optional[ProcessingOptionsAutoModeConfigurationParsingConfCropBox]`

              Crop box options for auto mode parsing configuration.

              - `bottom: Optional[float]`

                Bottom boundary of crop box as ratio (0-1)

              - `left: Optional[float]`

                Left boundary of crop box as ratio (0-1)

              - `right: Optional[float]`

                Right boundary of crop box as ratio (0-1)

              - `top: Optional[float]`

                Top boundary of crop box as ratio (0-1)

            - `custom_prompt: Optional[str]`

              Custom AI instructions for matched pages. Overrides the base custom_prompt

            - `extract_layout: Optional[bool]`

              Whether to extract layout information

            - `high_res_ocr: Optional[bool]`

              Whether to use high resolution OCR

            - `ignore: Optional[ProcessingOptionsAutoModeConfigurationParsingConfIgnore]`

              Ignore options for auto mode parsing configuration.

              - `ignore_diagonal_text: Optional[bool]`

                Whether to ignore diagonal text in the document

              - `ignore_hidden_text: Optional[bool]`

                Whether to ignore hidden text in the document

            - `language: Optional[str]`

              Primary language of the document

            - `outlined_table_extraction: Optional[bool]`

              Whether to use outlined table extraction

            - `presentation: Optional[ProcessingOptionsAutoModeConfigurationParsingConfPresentation]`

              Presentation-specific options for auto mode parsing configuration.

              - `out_of_bounds_content: Optional[bool]`

                Extract out of bounds content in presentation slides

              - `skip_embedded_data: Optional[bool]`

                Skip extraction of embedded data for charts in presentation slides

            - `spatial_text: Optional[ProcessingOptionsAutoModeConfigurationParsingConfSpatialText]`

              Spatial text options for auto mode parsing configuration.

              - `do_not_unroll_columns: Optional[bool]`

                Keep column structure intact without unrolling

              - `preserve_layout_alignment_across_pages: Optional[bool]`

                Preserve text alignment across page boundaries

              - `preserve_very_small_text: Optional[bool]`

                Include very small text in spatial output

            - `specialized_chart_parsing: Optional[Literal["agentic_plus", "agentic", "efficient"]]`

              Enable specialized chart parsing with the specified mode

              - `"agentic_plus"`

              - `"agentic"`

              - `"efficient"`

            - `tier: Optional[Literal["fast", "cost_effective", "agentic", "agentic_plus"]]`

              Override the parsing tier for matched pages. Must be paired with version

              - `"fast"`

              - `"cost_effective"`

              - `"agentic"`

              - `"agentic_plus"`

            - `version: Optional[Union[Literal["latest", "2026-05-13", "2026-05-11", 2 more], str, null]]`

              Tier version when overriding tier. Required when tier is specified

              - `Literal["latest", "2026-05-13", "2026-05-11", 2 more]`

                Tier version when overriding tier. Required when tier is specified

                - `"latest"`

                - `"2026-05-13"`

                - `"2026-05-11"`

                - `"2026-04-09"`

                - `"2025-12-11"`

              - `str`

          - `filename_match_glob: Optional[str]`

            Single glob pattern to match against filename

          - `filename_match_glob_list: Optional[List[str]]`

            List of glob patterns to match against filename

          - `filename_regexp: Optional[str]`

            Regex pattern to match against filename

          - `filename_regexp_mode: Optional[str]`

            Regex mode flags (e.g., 'i' for case-insensitive)

          - `full_page_image_in_page: Optional[bool]`

            Trigger if page contains a full-page image (scanned page detection)

          - `full_page_image_in_page_threshold: Optional[Union[float, str, null]]`

            Threshold for full page image detection (0.0-1.0, default 0.8)

            - `float`

            - `str`

          - `image_in_page: Optional[bool]`

            Trigger if page contains non-screenshot images

          - `layout_element_in_page: Optional[str]`

            Trigger if page contains this layout element type

          - `layout_element_in_page_confidence_threshold: Optional[Union[float, str, null]]`

            Confidence threshold for layout element detection

            - `float`

            - `str`

          - `page_contains_at_least_n_charts: Optional[Union[int, str, null]]`

            Trigger if page has more than N charts

            - `int`

            - `str`

          - `page_contains_at_least_n_images: Optional[Union[int, str, null]]`

            Trigger if page has more than N images

            - `int`

            - `str`

          - `page_contains_at_least_n_layout_elements: Optional[Union[int, str, null]]`

            Trigger if page has more than N layout elements

            - `int`

            - `str`

          - `page_contains_at_least_n_lines: Optional[Union[int, str, null]]`

            Trigger if page has more than N lines

            - `int`

            - `str`

          - `page_contains_at_least_n_links: Optional[Union[int, str, null]]`

            Trigger if page has more than N links

            - `int`

            - `str`

          - `page_contains_at_least_n_numbers: Optional[Union[int, str, null]]`

            Trigger if page has more than N numeric words

            - `int`

            - `str`

          - `page_contains_at_least_n_percent_numbers: Optional[Union[int, str, null]]`

            Trigger if page has more than N% numeric words

            - `int`

            - `str`

          - `page_contains_at_least_n_tables: Optional[Union[int, str, null]]`

            Trigger if page has more than N tables

            - `int`

            - `str`

          - `page_contains_at_least_n_words: Optional[Union[int, str, null]]`

            Trigger if page has more than N words

            - `int`

            - `str`

          - `page_contains_at_most_n_charts: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N charts

            - `int`

            - `str`

          - `page_contains_at_most_n_images: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N images

            - `int`

            - `str`

          - `page_contains_at_most_n_layout_elements: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N layout elements

            - `int`

            - `str`

          - `page_contains_at_most_n_lines: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N lines

            - `int`

            - `str`

          - `page_contains_at_most_n_links: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N links

            - `int`

            - `str`

          - `page_contains_at_most_n_numbers: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N numeric words

            - `int`

            - `str`

          - `page_contains_at_most_n_percent_numbers: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N% numeric words

            - `int`

            - `str`

          - `page_contains_at_most_n_tables: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N tables

            - `int`

            - `str`

          - `page_contains_at_most_n_words: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N words

            - `int`

            - `str`

          - `page_longer_than_n_chars: Optional[Union[int, str, null]]`

            Trigger if page has more than N characters

            - `int`

            - `str`

          - `page_md_error: Optional[bool]`

            Trigger on pages with markdown extraction errors

          - `page_shorter_than_n_chars: Optional[Union[int, str, null]]`

            Trigger if page has fewer than N characters

            - `int`

            - `str`

          - `regexp_in_page: Optional[str]`

            Regex pattern to match in page content

          - `regexp_in_page_mode: Optional[str]`

            Regex mode flags for regexp_in_page

          - `table_in_page: Optional[bool]`

            Trigger if page contains a table

          - `text_in_page: Optional[str]`

            Trigger if page text/markdown contains this string

          - `trigger_mode: Optional[str]`

            How to combine multiple trigger conditions: 'and' (all conditions must match, this is the default) or 'or' (any single condition can trigger)

        - `cost_optimizer: Optional[ProcessingOptionsCostOptimizer]`

          Cost optimizer configuration for reducing parsing costs on simpler pages.

          When enabled, the parser analyzes each page and routes simpler pages to faster,
          cheaper processing while preserving quality for complex pages. Only works with
          'agentic' or 'agentic_plus' tiers.

          - `enable: Optional[bool]`

            Enable cost-optimized parsing. Routes simpler pages to faster processing while complex pages use full AI analysis. May reduce speed on some documents. IMPORTANT: Only available with 'agentic' or 'agentic_plus' tiers

        - `disable_heuristics: Optional[bool]`

          Disable automatic heuristics including outlined table extraction and adaptive long table handling. Use when heuristics produce incorrect results

        - `ignore: Optional[ProcessingOptionsIgnore]`

          Options for ignoring specific text types (diagonal, hidden, text in images)

          - `ignore_diagonal_text: Optional[bool]`

            Skip text rotated at an angle (not horizontal/vertical). Useful for ignoring watermarks or decorative angled text

          - `ignore_hidden_text: Optional[bool]`

            Skip text marked as hidden in the document structure. Some PDFs contain invisible text layers used for accessibility or search indexing

          - `ignore_text_in_image: Optional[bool]`

            Skip OCR text extraction from embedded images. Use when images contain irrelevant text (watermarks, logos) that shouldn't be in the output

        - `ocr_parameters: Optional[ProcessingOptionsOcrParameters]`

          OCR configuration including language detection settings

          - `languages: Optional[List[ParsingLanguages]]`

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

        - `specialized_chart_parsing: Optional[Literal["agentic_plus", "agentic", "efficient"]]`

          Enable AI-powered chart analysis. Modes: 'efficient' (fast, lower cost), 'agentic' (balanced), 'agentic_plus' (highest accuracy). Automatically enables extract_layout and precise_bounding_box when set

          - `"agentic_plus"`

          - `"agentic"`

          - `"efficient"`

      - `webhook_configurations: Optional[List[WebhookConfiguration]]`

        Webhook endpoints for job status notifications. Multiple webhooks can be configured for different events or services

        - `webhook_events: Optional[List[str]]`

          Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

        - `webhook_headers: Optional[Dict[str, object]]`

          Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

        - `webhook_url: Optional[str]`

          HTTPS URL to receive webhook POST requests. Must be publicly accessible

    - `class ParametersSpreadsheetV1Parameters: …`

      Typed parameters for a *spreadsheet v1* product configuration.

      - `product_type: Literal["spreadsheet_v1"]`

        Product type.

        - `"spreadsheet_v1"`

      - `extraction_range: Optional[str]`

        A1 notation of the range to extract a single region from. If None, the entire sheet is used.

      - `flatten_hierarchical_tables: Optional[bool]`

        Return a flattened dataframe when a detected table is recognized as hierarchical.

      - `generate_additional_metadata: Optional[bool]`

        Whether to generate additional metadata (title, description) for each extracted region.

      - `include_hidden_cells: Optional[bool]`

        Whether to include hidden cells when extracting regions from the spreadsheet.

      - `sheet_names: Optional[List[str]]`

        The names of the sheets to extract regions from. If empty, all sheets will be processed.

      - `specialization: Optional[str]`

        Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

      - `table_merge_sensitivity: Optional[Literal["strong", "weak"]]`

        Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

        - `"strong"`

        - `"weak"`

      - `use_experimental_processing: Optional[bool]`

        Enables experimental processing. Accuracy may be impacted.

    - `class UntypedParameters: …`

      Catch-all for configurations without a dedicated typed schema.

      Accepts arbitrary JSON fields alongside `product_type`.

      - `product_type: Literal["unknown"]`

        Product type.

        - `"unknown"`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
configuration_create = client.extract.generate_schema()
print(configuration_create.name)
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

- `class ExtractConfiguration: …`

  Extract configuration combining parse and extract settings.

  - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

    JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `cite_sources: Optional[bool]`

    Include citations in results

  - `confidence_scores: Optional[bool]`

    Include confidence scores in results

  - `extract_version: Optional[str]`

    Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

  - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

    Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

    - `"per_doc"`

    - `"per_page"`

    - `"per_table_row"`

  - `max_pages: Optional[int]`

    Maximum number of pages to process. Omit for no limit.

  - `parse_config_id: Optional[str]`

    Saved parse configuration ID to control how the document is parsed before extraction

  - `parse_tier: Optional[str]`

    Parse tier to use before extraction. Defaults to the extract tier if not specified.

  - `system_prompt: Optional[str]`

    Custom system prompt to guide extraction behavior

  - `target_pages: Optional[str]`

    Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

  - `tier: Optional[Literal["cost_effective", "agentic"]]`

    Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

    - `"cost_effective"`

    - `"agentic"`

### Extract Job Metadata

- `class ExtractJobMetadata: …`

  Extraction metadata.

  - `field_metadata: Optional[ExtractedFieldMetadata]`

    Metadata for extracted fields including document, page, and row level info.

    - `document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

      Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

      Per-page metadata when extraction_target is per_page

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

      Per-row metadata when extraction_target is per_table_row

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

  - `parse_job_id: Optional[str]`

    Reference to the ParseJob ID used for parsing

  - `parse_tier: Optional[str]`

    Parse tier used for parsing the document

### Extract Job Usage

- `class ExtractJobUsage: …`

  Extraction usage metrics.

  - `num_document_tokens: Optional[int]`

    Number of document tokens

  - `num_output_tokens: Optional[int]`

    Number of output tokens

  - `num_pages_extracted: Optional[int]`

    Number of pages extracted

### Extract V2 Job

- `class ExtractV2Job: …`

  An extraction job.

  - `id: str`

    Unique job identifier (job_id)

  - `created_at: datetime`

    Creation timestamp

  - `file_input: str`

    File ID or parse job ID that was extracted

  - `project_id: str`

    Project this job belongs to

  - `status: str`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `updated_at: datetime`

    Last update timestamp

  - `configuration: Optional[ExtractConfiguration]`

    Extract configuration combining parse and extract settings.

    - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `cite_sources: Optional[bool]`

      Include citations in results

    - `confidence_scores: Optional[bool]`

      Include confidence scores in results

    - `extract_version: Optional[str]`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: Optional[int]`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: Optional[str]`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: Optional[str]`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: Optional[str]`

      Custom system prompt to guide extraction behavior

    - `target_pages: Optional[str]`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: Optional[Literal["cost_effective", "agentic"]]`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: Optional[str]`

    Saved extract configuration ID used for this job, if any

  - `error_message: Optional[str]`

    Error details when status is FAILED

  - `extract_metadata: Optional[ExtractJobMetadata]`

    Extraction metadata.

    - `field_metadata: Optional[ExtractedFieldMetadata]`

      Metadata for extracted fields including document, page, and row level info.

      - `document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

        Per-page metadata when extraction_target is per_page

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

        Per-row metadata when extraction_target is per_table_row

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

    - `parse_job_id: Optional[str]`

      Reference to the ParseJob ID used for parsing

    - `parse_tier: Optional[str]`

      Parse tier used for parsing the document

  - `extract_result: Optional[Union[Dict[str, Union[Dict[str, object], List[object], str, 3 more]], List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]], null]]`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

  - `metadata: Optional[Metadata]`

    Job-level metadata.

    - `usage: Optional[ExtractJobUsage]`

      Extraction usage metrics.

      - `num_document_tokens: Optional[int]`

        Number of document tokens

      - `num_output_tokens: Optional[int]`

        Number of output tokens

      - `num_pages_extracted: Optional[int]`

        Number of pages extracted

### Extract V2 Job Create

- `class ExtractV2JobCreate: …`

  Request to create an extraction job. Provide configuration_id or inline configuration.

  - `file_input: str`

    File ID or parse job ID to extract from

  - `configuration: Optional[ExtractConfiguration]`

    Extract configuration combining parse and extract settings.

    - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `cite_sources: Optional[bool]`

      Include citations in results

    - `confidence_scores: Optional[bool]`

      Include confidence scores in results

    - `extract_version: Optional[str]`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `"per_doc"`

      - `"per_page"`

      - `"per_table_row"`

    - `max_pages: Optional[int]`

      Maximum number of pages to process. Omit for no limit.

    - `parse_config_id: Optional[str]`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `parse_tier: Optional[str]`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `system_prompt: Optional[str]`

      Custom system prompt to guide extraction behavior

    - `target_pages: Optional[str]`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `tier: Optional[Literal["cost_effective", "agentic"]]`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `"cost_effective"`

      - `"agentic"`

  - `configuration_id: Optional[str]`

    Saved configuration ID

  - `webhook_configurations: Optional[List[WebhookConfiguration]]`

    Outbound webhook endpoints to notify on job status changes

    - `webhook_events: Optional[List[Literal["extract.pending", "extract.success", "extract.error", 14 more]]]`

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

    - `webhook_headers: Optional[Dict[str, str]]`

      Custom HTTP headers sent with each webhook request (e.g. auth tokens)

    - `webhook_output_format: Optional[str]`

      Response format sent to the webhook: 'string' (default) or 'json'

    - `webhook_url: Optional[str]`

      URL to receive webhook POST notifications

### Extract V2 Job Query Response

- `class ExtractV2JobQueryResponse: …`

  Paginated list of extraction jobs.

  - `items: List[ExtractV2Job]`

    The list of items.

    - `id: str`

      Unique job identifier (job_id)

    - `created_at: datetime`

      Creation timestamp

    - `file_input: str`

      File ID or parse job ID that was extracted

    - `project_id: str`

      Project this job belongs to

    - `status: str`

      Current job status.

      - `PENDING` — queued, not yet started
      - `RUNNING` — actively processing
      - `COMPLETED` — finished successfully
      - `FAILED` — terminated with an error
      - `CANCELLED` — cancelled by user

    - `updated_at: datetime`

      Last update timestamp

    - `configuration: Optional[ExtractConfiguration]`

      Extract configuration combining parse and extract settings.

      - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

        JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `cite_sources: Optional[bool]`

        Include citations in results

      - `confidence_scores: Optional[bool]`

        Include confidence scores in results

      - `extract_version: Optional[str]`

        Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

      - `extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]]`

        Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

        - `"per_doc"`

        - `"per_page"`

        - `"per_table_row"`

      - `max_pages: Optional[int]`

        Maximum number of pages to process. Omit for no limit.

      - `parse_config_id: Optional[str]`

        Saved parse configuration ID to control how the document is parsed before extraction

      - `parse_tier: Optional[str]`

        Parse tier to use before extraction. Defaults to the extract tier if not specified.

      - `system_prompt: Optional[str]`

        Custom system prompt to guide extraction behavior

      - `target_pages: Optional[str]`

        Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

      - `tier: Optional[Literal["cost_effective", "agentic"]]`

        Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

        - `"cost_effective"`

        - `"agentic"`

    - `configuration_id: Optional[str]`

      Saved extract configuration ID used for this job, if any

    - `error_message: Optional[str]`

      Error details when status is FAILED

    - `extract_metadata: Optional[ExtractJobMetadata]`

      Extraction metadata.

      - `field_metadata: Optional[ExtractedFieldMetadata]`

        Metadata for extracted fields including document, page, and row level info.

        - `document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

          Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

          - `Dict[str, object]`

          - `List[object]`

          - `str`

          - `float`

          - `bool`

        - `page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

          Per-page metadata when extraction_target is per_page

          - `Dict[str, object]`

          - `List[object]`

          - `str`

          - `float`

          - `bool`

        - `row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

          Per-row metadata when extraction_target is per_table_row

          - `Dict[str, object]`

          - `List[object]`

          - `str`

          - `float`

          - `bool`

      - `parse_job_id: Optional[str]`

        Reference to the ParseJob ID used for parsing

      - `parse_tier: Optional[str]`

        Parse tier used for parsing the document

    - `extract_result: Optional[Union[Dict[str, Union[Dict[str, object], List[object], str, 3 more]], List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]], null]]`

      Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

      - `Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

      - `List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

        - `Dict[str, object]`

        - `List[object]`

        - `str`

        - `float`

        - `bool`

    - `metadata: Optional[Metadata]`

      Job-level metadata.

      - `usage: Optional[ExtractJobUsage]`

        Extraction usage metrics.

        - `num_document_tokens: Optional[int]`

          Number of document tokens

        - `num_output_tokens: Optional[int]`

          Number of output tokens

        - `num_pages_extracted: Optional[int]`

          Number of pages extracted

  - `next_page_token: Optional[str]`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: Optional[int]`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Extract V2 Schema Generate Request

- `class ExtractV2SchemaGenerateRequest: …`

  Request schema for generating an extraction schema.

  - `data_schema: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Optional schema to validate, refine, or extend

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `file_id: Optional[str]`

    Optional file ID to analyze for schema generation

  - `name: Optional[str]`

    Name for the generated configuration (auto-generated if omitted)

  - `prompt: Optional[str]`

    Natural language description of the data structure to extract

### Extract V2 Schema Validate Request

- `class ExtractV2SchemaValidateRequest: …`

  Request schema for validating an extraction schema.

  - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

    JSON Schema to validate for use with extract jobs

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

### Extract V2 Schema Validate Response

- `class ExtractV2SchemaValidateResponse: …`

  Response schema for schema validation.

  - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

    Validated JSON Schema, ready for use in extract jobs

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

### Extracted Field Metadata

- `class ExtractedFieldMetadata: …`

  Metadata for extracted fields including document, page, and row level info.

  - `document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

    Per-page metadata when extraction_target is per_page

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]]`

    Per-row metadata when extraction_target is per_table_row

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`
