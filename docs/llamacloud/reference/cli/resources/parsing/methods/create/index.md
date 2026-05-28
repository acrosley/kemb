## Parse File

`$ llamacloud-prod parsing create`

**post** `/api/v2/parse`

Parse a file by file ID or URL.

Provide either `file_id` (a previously uploaded file) or
`source_url` (a publicly accessible URL). Configure parsing
with options like `tier`, `target_pages`, and `lang`.

## Tiers

- `fast` — rule-based, cheapest, no AI
- `cost_effective` — balanced speed and quality
- `agentic` — full AI-powered parsing
- `agentic_plus` — premium AI with specialized features

The job runs asynchronously. Poll `GET /parse/{job_id}` with
`expand=text` or `expand=markdown` to retrieve results.

### Parameters

- `--tier: "fast" or "cost_effective" or "agentic" or "agentic_plus"`

  Body param: Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced), 'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with highest accuracy)

- `--version: "latest" or "2026-05-13" or "2026-05-11" or 2 more or string`

  Body param: Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--agentic-options: optional object { custom_prompt }`

  Body param: Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

  These options customize how the AI processes and interprets document content.
  Only applicable when using non-fast tiers.

- `--client-name: optional string`

  Body param: Identifier for the client/application making the request. Used for analytics and debugging. Example: 'my-app-v2'

- `--crop-box: optional object { bottom, left, right, top }`

  Body param: Crop boundaries to process only a portion of each page. Values are ratios 0-1 from page edges

- `--disable-cache: optional boolean`

  Body param: Bypass result caching and force re-parsing. Use when document content may have changed or you need fresh results

- `--fast-options: optional unknown`

  Body param: Options for fast tier parsing (rule-based, no AI).

  Fast tier uses deterministic algorithms for text extraction without AI enhancement.
  It's the fastest and most cost-effective option, best suited for simple documents
  with standard layouts. Currently has no configurable options but reserved for
  future expansion.

- `--file-id: optional string`

  Body param: ID of an existing file in the project to parse. Mutually exclusive with source_url

- `--http-proxy: optional string`

  Body param: HTTP/HTTPS proxy for fetching source_url. Ignored if using file_id

- `--input-options: optional object { html, pdf, presentation, spreadsheet }`

  Body param: Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on detected input file type

- `--output-options: optional object { additional_outputs, extract_printed_page_number, images_to_save, 3 more }`

  Body param: Output formatting options for markdown, text, and extracted images

- `--page-ranges: optional object { max_pages, target_pages }`

  Body param: Page selection: limit total pages or specify exact pages to process

- `--processing-control: optional object { job_failure_conditions, timeouts }`

  Body param: Job execution controls including timeouts and failure thresholds

- `--processing-options: optional object { aggressive_table_extraction, auto_mode_configuration, cost_optimizer, 4 more }`

  Body param: Document processing options including OCR, table extraction, and chart parsing

- `--source-url: optional string`

  Body param: Public URL of the document to parse. Mutually exclusive with file_id

- `--webhook-configuration: optional array of object { webhook_events, webhook_headers, webhook_url }`

  Body param: Webhook endpoints for job status notifications. Multiple webhooks can be configured for different events or services

### Returns

- `ParsingNewResponse: object { id, project_id, status, 5 more }`

  A parse job.

  - `id: string`

    Unique parse job identifier

  - `project_id: string`

    Project this job belongs to

  - `status: "PENDING" or "RUNNING" or "COMPLETED" or 2 more`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at: optional string`

    Creation datetime

  - `error_message: optional string`

    Error details when status is FAILED

  - `name: optional string`

    Optional display name for this parse job

  - `tier: optional string`

    Parsing tier used for this job

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod parsing create \
  --api-key 'My API Key' \
  --tier fast \
  --version latest
```

#### Response

```json
{
  "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "status": "PENDING",
  "created_at": "2019-12-27T18:11:19.117Z",
  "error_message": "error_message",
  "name": "Q4 Financial Report",
  "tier": "fast",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
