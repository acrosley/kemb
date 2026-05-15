## Get Extract Job

`client.Extract.Get(ctx, jobID, query) (*ExtractV2Job, error)`

**get** `/api/v2/extract/{job_id}`

Get a single extraction job by ID.

Returns the job status and results when complete.
Use `expand=configuration` to include the full configuration used,
and `expand=extract_metadata` for per-field metadata.

### Parameters

- `jobID string`

- `query ExtractGetParams`

  - `Expand param.Field[[]string]`

    Additional fields to include: configuration, extract_metadata

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type ExtractV2Job struct{…}`

  An extraction job.

  - `ID string`

    Unique job identifier (job_id)

  - `CreatedAt Time`

    Creation timestamp

  - `FileInput string`

    File ID or parse job ID that was extracted

  - `ProjectID string`

    Project this job belongs to

  - `Status string`

    Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user

  - `UpdatedAt Time`

    Last update timestamp

  - `Configuration ExtractConfiguration`

    Extract configuration combining parse and extract settings.

    - `DataSchema map[string, ExtractConfigurationDataSchemaUnion]`

      JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

      - `type ExtractConfigurationDataSchemaMap map[string, any]`

      - `type ExtractConfigurationDataSchemaArray []any`

      - `string`

      - `float64`

      - `bool`

    - `CiteSources bool`

      Include citations in results

    - `ConfidenceScores bool`

      Include confidence scores in results

    - `ExtractVersion string`

      Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

    - `ExtractionTarget ExtractConfigurationExtractionTarget`

      Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

      - `const ExtractConfigurationExtractionTargetPerDoc ExtractConfigurationExtractionTarget = "per_doc"`

      - `const ExtractConfigurationExtractionTargetPerPage ExtractConfigurationExtractionTarget = "per_page"`

      - `const ExtractConfigurationExtractionTargetPerTableRow ExtractConfigurationExtractionTarget = "per_table_row"`

    - `MaxPages int64`

      Maximum number of pages to process. Omit for no limit.

    - `ParseConfigID string`

      Saved parse configuration ID to control how the document is parsed before extraction

    - `ParseTier string`

      Parse tier to use before extraction. Defaults to the extract tier if not specified.

    - `SystemPrompt string`

      Custom system prompt to guide extraction behavior

    - `TargetPages string`

      Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `Tier ExtractConfigurationTier`

      Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

      - `const ExtractConfigurationTierCostEffective ExtractConfigurationTier = "cost_effective"`

      - `const ExtractConfigurationTierAgentic ExtractConfigurationTier = "agentic"`

  - `ConfigurationID string`

    Saved extract configuration ID used for this job, if any

  - `ErrorMessage string`

    Error details when status is FAILED

  - `ExtractMetadata ExtractJobMetadata`

    Extraction metadata.

    - `FieldMetadata ExtractedFieldMetadata`

      Metadata for extracted fields including document, page, and row level info.

      - `DocumentMetadata map[string, ExtractedFieldMetadataDocumentMetadataUnion]`

        Per-field metadata keyed by field name from your schema. Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and confidence. Array fields (e.g. `items`) map to a list where each element contains per-sub-field FieldMetadataEntry objects, indexed by array position. Nested objects contain sub-field entries recursively.

        - `type ExtractedFieldMetadataDocumentMetadataMap map[string, any]`

        - `type ExtractedFieldMetadataDocumentMetadataArray []any`

        - `string`

        - `float64`

        - `bool`

      - `PageMetadata []map[string, ExtractedFieldMetadataPageMetadataUnion]`

        Per-page metadata when extraction_target is per_page

        - `type ExtractedFieldMetadataPageMetadataMap map[string, any]`

        - `type ExtractedFieldMetadataPageMetadataArray []any`

        - `string`

        - `float64`

        - `bool`

      - `RowMetadata []map[string, ExtractedFieldMetadataRowMetadataUnion]`

        Per-row metadata when extraction_target is per_table_row

        - `type ExtractedFieldMetadataRowMetadataMap map[string, any]`

        - `type ExtractedFieldMetadataRowMetadataArray []any`

        - `string`

        - `float64`

        - `bool`

    - `ParseJobID string`

      Reference to the ParseJob ID used for parsing

    - `ParseTier string`

      Parse tier used for parsing the document

  - `ExtractResult ExtractV2JobExtractResultUnion`

    Extracted data conforming to the data_schema. Returns a single object for per_doc, or an array for per_page / per_table_row.

    - `type ExtractV2JobExtractResultMap map[string, ExtractV2JobExtractResultMapItemUnion]`

      - `type ExtractV2JobExtractResultMapItemMap map[string, any]`

      - `type ExtractV2JobExtractResultMapItemArray []any`

      - `string`

      - `float64`

      - `bool`

    - `type ExtractV2JobExtractResultArray []map[string, ExtractV2JobExtractResultArrayItemUnion]`

      - `type ExtractV2JobExtractResultArrayItemMap map[string, any]`

      - `type ExtractV2JobExtractResultArrayItemArray []any`

      - `string`

      - `float64`

      - `bool`

  - `Metadata ExtractV2JobMetadata`

    Job-level metadata.

    - `Usage ExtractJobUsage`

      Extraction usage metrics.

      - `NumDocumentTokens int64`

        Number of document tokens

      - `NumOutputTokens int64`

        Number of output tokens

      - `NumPagesExtracted int64`

        Number of pages extracted

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
  extractV2Job, err := client.Extract.Get(
    context.TODO(),
    "job_id",
    llamacloudprod.ExtractGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", extractV2Job.ID)
}
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
