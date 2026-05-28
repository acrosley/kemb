# Parsing

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

## Get Parse Job

`$ llamacloud-prod parsing get`

**get** `/api/v2/parse/{job_id}`

Retrieve a parse job with optional expanded content.

By default returns job metadata only. Use `expand` to include
parsed content:

- `text` — plain text output
- `markdown` — markdown output
- `items` — structured page-by-page output
- `job_metadata` — usage and processing details

Content metadata fields (e.g. `text_content_metadata`) return
presigned URLs for downloading large results.

### Parameters

- `--job-id: string`

- `--expand: optional array of string`

  Fields to include: text, markdown, items, metadata, job_metadata, text_content_metadata, markdown_content_metadata, items_content_metadata, metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata, output_pdf_content_metadata, images_content_metadata. Metadata fields include presigned URLs.

- `--image-filenames: optional string`

  Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `ParsingGetResponse: object { job, images_content_metadata, items, 8 more }`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `job: object { id, project_id, status, 5 more }`

    Parse job status and metadata

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

  - `images_content_metadata: optional object { images, total_count }`

    Metadata for all extracted images.

    - `images: array of object { filename, index, bbox, 4 more }`

      List of image metadata with presigned URLs

      - `filename: string`

        Image filename (e.g., 'image_0.png')

      - `index: number`

        Index of the image in the extraction order

      - `bbox: optional object { h, w, x, y }`

        Bounding box for an image on its page.

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

      - `category: optional "screenshot" or "embedded" or "layout"`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `content_type: optional string`

        MIME type of the image

      - `presigned_url: optional string`

        Presigned URL to download the image

      - `size_bytes: optional number`

        Deprecated: always returns None. Will be removed in a future release.

    - `total_count: number`

      Total number of extracted images

  - `items: optional object { pages }`

    Structured JSON result (if requested)

    - `pages: array of object { items, page_height, page_number, 2 more }  or object { error, page_number, success }`

      List of structured pages or failed page entries

      - `StructuredResultPage: object { items, page_height, page_number, 2 more }`

        - `items: array of TextItem or HeadingItem or ListItem or 6 more`

          List of structured items on the page

          - `text_item: object { md, value, bbox, type }`

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Text content

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `type: optional "text"`

              Text item type

              - `"text"`

          - `heading_item: object { level, md, value, 2 more }`

            - `level: number`

              Heading level (1-6)

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Heading text content

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `type: optional "heading"`

              Heading item type

              - `"heading"`

          - `list_item: object { items, md, ordered, 2 more }`

            - `items: array of TextItem or ListItem`

              List of nested text or list items

              - `text_item: object { md, value, bbox, type }`

              - `list_item: object { items, md, ordered, 2 more }`

            - `md: string`

              Markdown representation preserving formatting

            - `ordered: boolean`

              Whether the list is ordered or unordered

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `type: optional "list"`

              List item type

              - `"list"`

          - `code_item: object { md, value, bbox, 2 more }`

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Code content

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `language: optional string`

              Programming language identifier

            - `type: optional "code"`

              Code block item type

              - `"code"`

          - `table_item: object { csv, html, md, 6 more }`

            - `csv: string`

              CSV representation of the table

            - `html: string`

              HTML representation of the table

            - `md: string`

              Markdown representation preserving formatting

            - `rows: array of array of string or number`

              Table data as array of arrays (string, number, or null)

              - `union_member_0: string`

              - `union_member_1: number`

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `merged_from_pages: optional array of number`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `merged_into_page: optional number`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `parse_concerns: optional array of object { details, type }`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `details: string`

                Human-readable details about the concern

              - `type: string`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `type: optional "table"`

              Table item type

              - `"table"`

          - `image_item: object { caption, md, url, 2 more }`

            - `caption: string`

              Image caption

            - `md: string`

              Markdown representation preserving formatting

            - `url: string`

              URL to the image

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `type: optional "image"`

              Image item type

              - `"image"`

          - `link_item: object { md, text, url, 2 more }`

            - `md: string`

              Markdown representation preserving formatting

            - `text: string`

              Display text of the link

            - `url: string`

              URL of the link

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `type: optional "link"`

              Link item type

              - `"link"`

          - `header_item: object { items, md, bbox, type }`

            - `items: array of TextItem or HeadingItem or ListItem or 4 more`

              List of items within the header

              - `text_item: object { md, value, bbox, type }`

              - `heading_item: object { level, md, value, 2 more }`

              - `list_item: object { items, md, ordered, 2 more }`

              - `code_item: object { md, value, bbox, 2 more }`

              - `table_item: object { csv, html, md, 6 more }`

              - `image_item: object { caption, md, url, 2 more }`

              - `link_item: object { md, text, url, 2 more }`

            - `md: string`

              Markdown representation preserving formatting

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `type: optional "header"`

              Page header container

              - `"header"`

          - `footer_item: object { items, md, bbox, type }`

            - `items: array of TextItem or HeadingItem or ListItem or 4 more`

              List of items within the footer

              - `text_item: object { md, value, bbox, type }`

              - `heading_item: object { level, md, value, 2 more }`

              - `list_item: object { items, md, ordered, 2 more }`

              - `code_item: object { md, value, bbox, 2 more }`

              - `table_item: object { csv, html, md, 6 more }`

              - `image_item: object { caption, md, url, 2 more }`

              - `link_item: object { md, text, url, 2 more }`

            - `md: string`

              Markdown representation preserving formatting

            - `bbox: optional array of BBox`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence: optional number`

                Confidence score

              - `end_index: optional number`

                End index in the text

              - `label: optional string`

                Label for the bounding box

              - `start_index: optional number`

                Start index in the text

            - `type: optional "footer"`

              Page footer container

              - `"footer"`

        - `page_height: number`

          Height of the page in points

        - `page_number: number`

          Page number of the document

        - `page_width: number`

          Width of the page in points

        - `success: true`

          Success indicator

      - `FailedStructuredPage: object { error, page_number, success }`

        - `error: string`

          Error message describing the failure

        - `page_number: number`

          Page number of the document

        - `success: false`

          Failure indicator

  - `job_metadata: optional map[unknown]`

    Job execution metadata (if requested)

  - `markdown: optional object { pages }`

    Markdown result (if requested)

    - `pages: array of object { markdown, page_number, success, 2 more }  or object { error, page_number, success }`

      List of markdown pages or failed page entries

      - `MarkdownResultPage: object { markdown, page_number, success, 2 more }`

        - `markdown: string`

          Markdown content of the page

        - `page_number: number`

          Page number of the document

        - `success: true`

          Success indicator

        - `footer: optional string`

          Footer of the page in markdown

        - `header: optional string`

          Header of the page in markdown

      - `FailedMarkdownPage: object { error, page_number, success }`

        - `error: string`

          Error message describing the failure

        - `page_number: number`

          Page number of the document

        - `success: false`

          Failure indicator

  - `markdown_full: optional string`

    Full raw markdown content (if requested)

  - `metadata: optional object { pages }`

    Result containing metadata (page level and general) for the parsed document.

    - `pages: array of object { page_number, confidence, cost_optimized, 5 more }`

      List of page metadata entries

      - `page_number: number`

        Page number of the document

      - `confidence: optional number`

        Confidence score for the page parsing (0-1)

      - `cost_optimized: optional boolean`

        Whether cost-optimized parsing was used for the page

      - `original_orientation_angle: optional number`

        Original orientation angle of the page in degrees

      - `printed_page_number: optional string`

        Printed page number as it appears in the document

      - `slide_section_name: optional string`

        Section name from presentation slides

      - `speaker_notes: optional string`

        Speaker notes from presentation slides

      - `triggered_auto_mode: optional boolean`

        Whether auto mode was triggered for the page

  - `raw_parameters: optional map[unknown]`

  - `result_content_metadata: optional map[object { size_bytes, exists, presigned_url } ]`

    Metadata including size, existence, and presigned URLs for result files

    - `size_bytes: number`

      Size of the result file in bytes

    - `exists: optional boolean`

      Whether the result file exists in S3

    - `presigned_url: optional string`

      Presigned URL to download the result file

  - `text: optional object { pages }`

    Plain text result (if requested)

    - `pages: array of object { page_number, text }`

      List of text pages

      - `page_number: number`

        Page number of the document

      - `text: string`

        Plain text content of the page

  - `text_full: optional string`

    Full raw text content (if requested)

### Example

```cli
llamacloud-prod parsing get \
  --api-key 'My API Key' \
  --job-id job_id
```

#### Response

```json
{
  "job": {
    "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "status": "PENDING",
    "created_at": "2019-12-27T18:11:19.117Z",
    "error_message": "error_message",
    "name": "Q4 Financial Report",
    "tier": "fast",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "images_content_metadata": {
    "images": [
      {
        "filename": "filename",
        "index": 0,
        "bbox": {
          "h": 0,
          "w": 0,
          "x": 0,
          "y": 0
        },
        "category": "screenshot",
        "content_type": "content_type",
        "presigned_url": "presigned_url",
        "size_bytes": 0
      }
    ],
    "total_count": 0
  },
  "items": {
    "pages": [
      {
        "items": [
          {
            "md": "md",
            "value": "value",
            "bbox": [
              {
                "h": 0,
                "w": 0,
                "x": 0,
                "y": 0,
                "confidence": 0,
                "end_index": 0,
                "label": "label",
                "start_index": 0
              }
            ],
            "type": "text"
          }
        ],
        "page_height": 0,
        "page_number": 0,
        "page_width": 0,
        "success": true
      }
    ]
  },
  "job_metadata": {
    "foo": "bar"
  },
  "markdown": {
    "pages": [
      {
        "markdown": "markdown",
        "page_number": 0,
        "success": true,
        "footer": "footer",
        "header": "header"
      }
    ]
  },
  "markdown_full": "markdown_full",
  "metadata": {
    "pages": [
      {
        "page_number": 0,
        "confidence": 0,
        "cost_optimized": true,
        "original_orientation_angle": 0,
        "printed_page_number": "printed_page_number",
        "slide_section_name": "slide_section_name",
        "speaker_notes": "speaker_notes",
        "triggered_auto_mode": true
      }
    ]
  },
  "raw_parameters": {
    "foo": "bar"
  },
  "result_content_metadata": {
    "foo": {
      "size_bytes": 0,
      "exists": true,
      "presigned_url": "presigned_url"
    }
  },
  "text": {
    "pages": [
      {
        "page_number": 0,
        "text": "text"
      }
    ]
  },
  "text_full": "text_full"
}
```

## List Parse Jobs

`$ llamacloud-prod parsing list`

**get** `/api/v2/parse`

List parse jobs for the current project.

Filter by `status` or creation date range. Results are
paginated — use `page_token` from the response to fetch
subsequent pages.

### Parameters

- `--created-at-on-or-after: optional string`

  Include items created at or after this timestamp (inclusive)

- `--created-at-on-or-before: optional string`

  Include items created at or before this timestamp (inclusive)

- `--job-id: optional array of string`

  Filter by specific job IDs

- `--organization-id: optional string`

- `--page-size: optional number`

  Number of items per page

- `--page-token: optional string`

  Token for pagination

- `--project-id: optional string`

- `--status: optional "PENDING" or "RUNNING" or "COMPLETED" or 2 more`

  Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

### Returns

- `ParseJobQueryResponse: object { items, next_page_token, total_size }`

  Response schema for paginated parse job queries.

  - `items: array of object { id, project_id, status, 5 more }`

    The list of items.

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

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod parsing list \
  --api-key 'My API Key'
```

#### Response

```json
{
  "items": [
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
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Domain Types

### B Box

- `b_box: object { h, w, x, 5 more }`

  Bounding box with coordinates and optional metadata.

  - `h: number`

    Height of the bounding box

  - `w: number`

    Width of the bounding box

  - `x: number`

    X coordinate of the bounding box

  - `y: number`

    Y coordinate of the bounding box

  - `confidence: optional number`

    Confidence score

  - `end_index: optional number`

    End index in the text

  - `label: optional string`

    Label for the bounding box

  - `start_index: optional number`

    Start index in the text

### Code Item

- `code_item: object { md, value, bbox, 2 more }`

  - `md: string`

    Markdown representation preserving formatting

  - `value: string`

    Code content

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `language: optional string`

    Programming language identifier

  - `type: optional "code"`

    Code block item type

    - `"code"`

### Fail Page Mode

- `fail_page_mode: "raw_text" or "blank_page" or "error_message"`

  Enum for representing the different available page error handling modes.

  - `"raw_text"`

  - `"blank_page"`

  - `"error_message"`

### Footer Item

- `footer_item: object { items, md, bbox, type }`

  - `items: array of TextItem or HeadingItem or ListItem or 4 more`

    List of items within the footer

    - `text_item: object { md, value, bbox, type }`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Text content

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "text"`

        Text item type

        - `"text"`

    - `heading_item: object { level, md, value, 2 more }`

      - `level: number`

        Heading level (1-6)

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Heading text content

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "heading"`

        Heading item type

        - `"heading"`

    - `list_item: object { items, md, ordered, 2 more }`

      - `items: array of TextItem or ListItem`

        List of nested text or list items

        - `text_item: object { md, value, bbox, type }`

        - `list_item: object { items, md, ordered, 2 more }`

      - `md: string`

        Markdown representation preserving formatting

      - `ordered: boolean`

        Whether the list is ordered or unordered

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "list"`

        List item type

        - `"list"`

    - `code_item: object { md, value, bbox, 2 more }`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Code content

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `language: optional string`

        Programming language identifier

      - `type: optional "code"`

        Code block item type

        - `"code"`

    - `table_item: object { csv, html, md, 6 more }`

      - `csv: string`

        CSV representation of the table

      - `html: string`

        HTML representation of the table

      - `md: string`

        Markdown representation preserving formatting

      - `rows: array of array of string or number`

        Table data as array of arrays (string, number, or null)

        - `union_member_0: string`

        - `union_member_1: number`

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `merged_from_pages: optional array of number`

        List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

      - `merged_into_page: optional number`

        Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

      - `parse_concerns: optional array of object { details, type }`

        Quality concerns detected during table extraction, indicating the table may have issues

        - `details: string`

          Human-readable details about the concern

        - `type: string`

          Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

      - `type: optional "table"`

        Table item type

        - `"table"`

    - `image_item: object { caption, md, url, 2 more }`

      - `caption: string`

        Image caption

      - `md: string`

        Markdown representation preserving formatting

      - `url: string`

        URL to the image

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "image"`

        Image item type

        - `"image"`

    - `link_item: object { md, text, url, 2 more }`

      - `md: string`

        Markdown representation preserving formatting

      - `text: string`

        Display text of the link

      - `url: string`

        URL of the link

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "link"`

        Link item type

        - `"link"`

  - `md: string`

    Markdown representation preserving formatting

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `type: optional "footer"`

    Page footer container

    - `"footer"`

### Header Item

- `header_item: object { items, md, bbox, type }`

  - `items: array of TextItem or HeadingItem or ListItem or 4 more`

    List of items within the header

    - `text_item: object { md, value, bbox, type }`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Text content

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "text"`

        Text item type

        - `"text"`

    - `heading_item: object { level, md, value, 2 more }`

      - `level: number`

        Heading level (1-6)

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Heading text content

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "heading"`

        Heading item type

        - `"heading"`

    - `list_item: object { items, md, ordered, 2 more }`

      - `items: array of TextItem or ListItem`

        List of nested text or list items

        - `text_item: object { md, value, bbox, type }`

        - `list_item: object { items, md, ordered, 2 more }`

      - `md: string`

        Markdown representation preserving formatting

      - `ordered: boolean`

        Whether the list is ordered or unordered

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "list"`

        List item type

        - `"list"`

    - `code_item: object { md, value, bbox, 2 more }`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Code content

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `language: optional string`

        Programming language identifier

      - `type: optional "code"`

        Code block item type

        - `"code"`

    - `table_item: object { csv, html, md, 6 more }`

      - `csv: string`

        CSV representation of the table

      - `html: string`

        HTML representation of the table

      - `md: string`

        Markdown representation preserving formatting

      - `rows: array of array of string or number`

        Table data as array of arrays (string, number, or null)

        - `union_member_0: string`

        - `union_member_1: number`

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `merged_from_pages: optional array of number`

        List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

      - `merged_into_page: optional number`

        Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

      - `parse_concerns: optional array of object { details, type }`

        Quality concerns detected during table extraction, indicating the table may have issues

        - `details: string`

          Human-readable details about the concern

        - `type: string`

          Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

      - `type: optional "table"`

        Table item type

        - `"table"`

    - `image_item: object { caption, md, url, 2 more }`

      - `caption: string`

        Image caption

      - `md: string`

        Markdown representation preserving formatting

      - `url: string`

        URL to the image

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "image"`

        Image item type

        - `"image"`

    - `link_item: object { md, text, url, 2 more }`

      - `md: string`

        Markdown representation preserving formatting

      - `text: string`

        Display text of the link

      - `url: string`

        URL of the link

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "link"`

        Link item type

        - `"link"`

  - `md: string`

    Markdown representation preserving formatting

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `type: optional "header"`

    Page header container

    - `"header"`

### Heading Item

- `heading_item: object { level, md, value, 2 more }`

  - `level: number`

    Heading level (1-6)

  - `md: string`

    Markdown representation preserving formatting

  - `value: string`

    Heading text content

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `type: optional "heading"`

    Heading item type

    - `"heading"`

### Image Item

- `image_item: object { caption, md, url, 2 more }`

  - `caption: string`

    Image caption

  - `md: string`

    Markdown representation preserving formatting

  - `url: string`

    URL to the image

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `type: optional "image"`

    Image item type

    - `"image"`

### Link Item

- `link_item: object { md, text, url, 2 more }`

  - `md: string`

    Markdown representation preserving formatting

  - `text: string`

    Display text of the link

  - `url: string`

    URL of the link

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `type: optional "link"`

    Link item type

    - `"link"`

### List Item

- `list_item: object { items, md, ordered, 2 more }`

  - `items: array of TextItem or ListItem`

    List of nested text or list items

    - `text_item: object { md, value, bbox, type }`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Text content

      - `bbox: optional array of BBox`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence: optional number`

          Confidence score

        - `end_index: optional number`

          End index in the text

        - `label: optional string`

          Label for the bounding box

        - `start_index: optional number`

          Start index in the text

      - `type: optional "text"`

        Text item type

        - `"text"`

    - `list_item: object { items, md, ordered, 2 more }`

  - `md: string`

    Markdown representation preserving formatting

  - `ordered: boolean`

    Whether the list is ordered or unordered

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `type: optional "list"`

    List item type

    - `"list"`

### Llama Parse Supported File Extensions

- `llama_parse_supported_file_extensions: ".pdf" or ".abw" or ".awt" or 144 more`

  Enum for supported file extensions.

  - `".pdf"`

  - `".abw"`

  - `".awt"`

  - `".cgm"`

  - `".cwk"`

  - `".doc"`

  - `".docm"`

  - `".docx"`

  - `".dot"`

  - `".dotm"`

  - `".dotx"`

  - `".fodg"`

  - `".fodp"`

  - `".fopd"`

  - `".fodt"`

  - `".fb2"`

  - `".hwp"`

  - `".lwp"`

  - `".mcw"`

  - `".mw"`

  - `".mwd"`

  - `".odf"`

  - `".odt"`

  - `".otg"`

  - `".ott"`

  - `".pages"`

  - `".pbd"`

  - `".psw"`

  - `".rtf"`

  - `".sda"`

  - `".sdd"`

  - `".sdp"`

  - `".sdw"`

  - `".sgl"`

  - `".std"`

  - `".stw"`

  - `".sxd"`

  - `".sxg"`

  - `".sxm"`

  - `".sxw"`

  - `".uof"`

  - `".uop"`

  - `".uot"`

  - `".vor"`

  - `".wpd"`

  - `".wps"`

  - `".wpt"`

  - `".wri"`

  - `".wn"`

  - `".xml"`

  - `".zabw"`

  - `".key"`

  - `".odp"`

  - `".odg"`

  - `".otp"`

  - `".pot"`

  - `".potm"`

  - `".potx"`

  - `".ppt"`

  - `".pptm"`

  - `".pptx"`

  - `".sti"`

  - `".sxi"`

  - `".vsd"`

  - `".vsdm"`

  - `".vsdx"`

  - `".vdx"`

  - `".bmp"`

  - `".gif"`

  - `".heic"`

  - `".heif"`

  - `".jpg"`

  - `".jpeg"`

  - `".png"`

  - `".svg"`

  - `".tif"`

  - `".tiff"`

  - `".webp"`

  - `".htm"`

  - `".html"`

  - `".xhtm"`

  - `".csv"`

  - `".dbf"`

  - `".dif"`

  - `".et"`

  - `".eth"`

  - `".fods"`

  - `".numbers"`

  - `".ods"`

  - `".ots"`

  - `".prn"`

  - `".qpw"`

  - `".slk"`

  - `".stc"`

  - `".sxc"`

  - `".sylk"`

  - `".tsv"`

  - `".uos1"`

  - `".uos2"`

  - `".uos"`

  - `".wb1"`

  - `".wb2"`

  - `".wb3"`

  - `".wk1"`

  - `".wk2"`

  - `".wk3"`

  - `".wk4"`

  - `".wks"`

  - `".wq1"`

  - `".wq2"`

  - `".xlr"`

  - `".xls"`

  - `".xlsb"`

  - `".xlsm"`

  - `".xlsx"`

  - `".xlw"`

  - `".azw"`

  - `".azw3"`

  - `".azw4"`

  - `".cb7"`

  - `".cbc"`

  - `".cbr"`

  - `".cbz"`

  - `".chm"`

  - `".djvu"`

  - `".epub"`

  - `".fbz"`

  - `".htmlz"`

  - `".lit"`

  - `".lrf"`

  - `".md"`

  - `".mobi"`

  - `".pdb"`

  - `".pml"`

  - `".prc"`

  - `".rb"`

  - `".snb"`

  - `".tcr"`

  - `".txtz"`

  - `".m4a"`

  - `".mp3"`

  - `".mp4"`

  - `".mpeg"`

  - `".mpga"`

  - `".wav"`

  - `".webm"`

  - `".yxmd"`

### Parsing Job

- `parsing_job: object { id, status, error_code, error_message }`

  A parse job (v1).

  - `id: string`

    Unique parse job identifier

  - `status: "PENDING" or "SUCCESS" or "ERROR" or 2 more`

    Current job status

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `error_code: optional string`

    Machine-readable error code when failed

  - `error_message: optional string`

    Human-readable error details when failed

### Parsing Languages

- `parsing_languages: "af" or "az" or "bs" or 83 more`

  Enum for representing the languages supported by the parser.

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

### Parsing Mode

- `parsing_mode: "parse_page_without_llm" or "parse_page_with_llm" or "parse_page_with_lvm" or 5 more`

  Enum for representing the mode of parsing to be used.

  - `"parse_page_without_llm"`

  - `"parse_page_with_llm"`

  - `"parse_page_with_lvm"`

  - `"parse_page_with_agent"`

  - `"parse_page_with_layout_agent"`

  - `"parse_document_with_llm"`

  - `"parse_document_with_lvm"`

  - `"parse_document_with_agent"`

### Status Enum

- `status_enum: "PENDING" or "SUCCESS" or "ERROR" or 2 more`

  Enum for representing the status of a job

  - `"PENDING"`

  - `"SUCCESS"`

  - `"ERROR"`

  - `"PARTIAL_SUCCESS"`

  - `"CANCELLED"`

### Table Item

- `table_item: object { csv, html, md, 6 more }`

  - `csv: string`

    CSV representation of the table

  - `html: string`

    HTML representation of the table

  - `md: string`

    Markdown representation preserving formatting

  - `rows: array of array of string or number`

    Table data as array of arrays (string, number, or null)

    - `union_member_0: string`

    - `union_member_1: number`

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `merged_from_pages: optional array of number`

    List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

  - `merged_into_page: optional number`

    Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

  - `parse_concerns: optional array of object { details, type }`

    Quality concerns detected during table extraction, indicating the table may have issues

    - `details: string`

      Human-readable details about the concern

    - `type: string`

      Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

  - `type: optional "table"`

    Table item type

    - `"table"`

### Text Item

- `text_item: object { md, value, bbox, type }`

  - `md: string`

    Markdown representation preserving formatting

  - `value: string`

    Text content

  - `bbox: optional array of BBox`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence: optional number`

      Confidence score

    - `end_index: optional number`

      End index in the text

    - `label: optional string`

      Label for the bounding box

    - `start_index: optional number`

      Start index in the text

  - `type: optional "text"`

    Text item type

    - `"text"`
