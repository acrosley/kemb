# Parsing

## Parse File

`client.parsing.create(ParsingCreateParamsparams, RequestOptionsoptions?): ParsingCreateResponse`

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

- `params: ParsingCreateParams`

  - `tier: "fast" | "cost_effective" | "agentic" | "agentic_plus"`

    Body param: Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced), 'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with highest accuracy)

    - `"fast"`

    - `"cost_effective"`

    - `"agentic"`

    - `"agentic_plus"`

  - `version: "latest" | "2026-05-13" | "2026-05-11" | 2 more | (string & {})`

    Body param: Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

    - `"latest" | "2026-05-13" | "2026-05-11" | 2 more`

      - `"latest"`

      - `"2026-05-13"`

      - `"2026-05-11"`

      - `"2026-04-09"`

      - `"2025-12-11"`

    - `(string & {})`

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `agentic_options?: AgenticOptions | null`

    Body param: Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

    These options customize how the AI processes and interprets document content.
    Only applicable when using non-fast tiers.

    - `custom_prompt?: string | null`

      Custom instructions for the AI parser. Use to guide extraction behavior, specify output formatting, or provide domain-specific context. Example: 'Extract financial tables with currency symbols. Format dates as YYYY-MM-DD.'

  - `client_name?: string | null`

    Body param: Identifier for the client/application making the request. Used for analytics and debugging. Example: 'my-app-v2'

  - `crop_box?: CropBox`

    Body param: Crop boundaries to process only a portion of each page. Values are ratios 0-1 from page edges

    - `bottom?: number | null`

      Bottom boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content below this line is excluded

    - `left?: number | null`

      Left boundary as ratio (0-1). 0=left edge, 1=right edge. Content left of this line is excluded

    - `right?: number | null`

      Right boundary as ratio (0-1). 0=left edge, 1=right edge. Content right of this line is excluded

    - `top?: number | null`

      Top boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content above this line is excluded

  - `disable_cache?: boolean | null`

    Body param: Bypass result caching and force re-parsing. Use when document content may have changed or you need fresh results

  - `fast_options?: unknown`

    Body param: Options for fast tier parsing (rule-based, no AI).

    Fast tier uses deterministic algorithms for text extraction without AI enhancement.
    It's the fastest and most cost-effective option, best suited for simple documents
    with standard layouts. Currently has no configurable options but reserved for
    future expansion.

  - `file_id?: string | null`

    Body param: ID of an existing file in the project to parse. Mutually exclusive with source_url

  - `http_proxy?: string | null`

    Body param: HTTP/HTTPS proxy for fetching source_url. Ignored if using file_id

  - `input_options?: InputOptions`

    Body param: Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on detected input file type

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

    Body param: Output formatting options for markdown, text, and extracted images

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

    Body param: Page selection: limit total pages or specify exact pages to process

    - `max_pages?: number | null`

      Maximum number of pages to process. Pages are processed in order starting from page 1. If both max_pages and target_pages are set, target_pages takes precedence

    - `target_pages?: string | null`

      Comma-separated list of specific pages to process using 1-based indexing. Supports individual pages and ranges. Examples: '1,3,5' (pages 1, 3, 5), '1-5' (pages 1 through 5 inclusive), '1,3,5-8,10' (pages 1, 3, 5-8, and 10). Pages are sorted and deduplicated automatically. Duplicate pages cause an error

  - `processing_control?: ProcessingControl`

    Body param: Job execution controls including timeouts and failure thresholds

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

    Body param: Document processing options including OCR, table extraction, and chart parsing

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

  - `source_url?: string | null`

    Body param: Public URL of the document to parse. Mutually exclusive with file_id

  - `webhook_configurations?: Array<WebhookConfiguration>`

    Body param: Webhook endpoints for job status notifications. Multiple webhooks can be configured for different events or services

    - `webhook_events?: Array<string> | null`

      Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

    - `webhook_headers?: Record<string, unknown> | null`

      Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

    - `webhook_url?: string | null`

      HTTPS URL to receive webhook POST requests. Must be publicly accessible

### Returns

- `ParsingCreateResponse`

  A parse job.

  - `id: string`

    Unique parse job identifier

  - `project_id: string`

    Project this job belongs to

  - `status: "PENDING" | "RUNNING" | "COMPLETED" | 2 more`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error details when status is FAILED

  - `name?: string | null`

    Optional display name for this parse job

  - `tier?: string | null`

    Parsing tier used for this job

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const parsing = await client.parsing.create({ tier: 'fast', version: 'latest' });

console.log(parsing.id);
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

`client.parsing.get(stringjobID, ParsingGetParamsquery?, RequestOptionsoptions?): ParsingGetResponse`

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

- `jobID: string`

- `query: ParsingGetParams`

  - `expand?: Array<string>`

    Fields to include: text, markdown, items, metadata, job_metadata, text_content_metadata, markdown_content_metadata, items_content_metadata, metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata, output_pdf_content_metadata, images_content_metadata. Metadata fields include presigned URLs.

  - `image_filenames?: string | null`

    Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ParsingGetResponse`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `job: Job`

    Parse job status and metadata

    - `id: string`

      Unique parse job identifier

    - `project_id: string`

      Project this job belongs to

    - `status: "PENDING" | "RUNNING" | "COMPLETED" | 2 more`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `"PENDING"`

      - `"RUNNING"`

      - `"COMPLETED"`

      - `"FAILED"`

      - `"CANCELLED"`

    - `created_at?: string | null`

      Creation datetime

    - `error_message?: string | null`

      Error details when status is FAILED

    - `name?: string | null`

      Optional display name for this parse job

    - `tier?: string | null`

      Parsing tier used for this job

    - `updated_at?: string | null`

      Update datetime

  - `images_content_metadata?: ImagesContentMetadata | null`

    Metadata for all extracted images.

    - `images: Array<Image>`

      List of image metadata with presigned URLs

      - `filename: string`

        Image filename (e.g., 'image_0.png')

      - `index: number`

        Index of the image in the extraction order

      - `bbox?: Bbox | null`

        Bounding box for an image on its page.

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

      - `category?: "screenshot" | "embedded" | "layout" | null`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `content_type?: string | null`

        MIME type of the image

      - `presigned_url?: string | null`

        Presigned URL to download the image

      - `size_bytes?: number | null`

        Deprecated: always returns None. Will be removed in a future release.

    - `total_count: number`

      Total number of extracted images

  - `items?: Items | null`

    Structured JSON result (if requested)

    - `pages: Array<StructuredResultPage | FailedStructuredPage>`

      List of structured pages or failed page entries

      - `StructuredResultPage`

        - `items: Array<TextItem | HeadingItem | ListItem | 6 more>`

          List of structured items on the page

          - `TextItem`

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Text content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "text"`

              Text item type

              - `"text"`

          - `HeadingItem`

            - `level: number`

              Heading level (1-6)

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Heading text content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "heading"`

              Heading item type

              - `"heading"`

          - `ListItem`

            - `items: Array<TextItem | ListItem>`

              List of nested text or list items

              - `TextItem`

              - `ListItem`

            - `md: string`

              Markdown representation preserving formatting

            - `ordered: boolean`

              Whether the list is ordered or unordered

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "list"`

              List item type

              - `"list"`

          - `CodeItem`

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Code content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `language?: string | null`

              Programming language identifier

            - `type?: "code"`

              Code block item type

              - `"code"`

          - `TableItem`

            - `csv: string`

              CSV representation of the table

            - `html: string`

              HTML representation of the table

            - `md: string`

              Markdown representation preserving formatting

            - `rows: Array<Array<string | number | null>>`

              Table data as array of arrays (string, number, or null)

              - `string`

              - `number`

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `merged_from_pages?: Array<number> | null`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `merged_into_page?: number | null`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `parse_concerns?: Array<ParseConcern> | null`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `details: string`

                Human-readable details about the concern

              - `type: string`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `type?: "table"`

              Table item type

              - `"table"`

          - `ImageItem`

            - `caption: string`

              Image caption

            - `md: string`

              Markdown representation preserving formatting

            - `url: string`

              URL to the image

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "image"`

              Image item type

              - `"image"`

          - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `text: string`

              Display text of the link

            - `url: string`

              URL of the link

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "link"`

              Link item type

              - `"link"`

          - `HeaderItem`

            - `items: Array<TextItem | HeadingItem | ListItem | 4 more>`

              List of items within the header

              - `TextItem`

              - `HeadingItem`

              - `ListItem`

              - `CodeItem`

              - `TableItem`

              - `ImageItem`

              - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "header"`

              Page header container

              - `"header"`

          - `FooterItem`

            - `items: Array<TextItem | HeadingItem | ListItem | 4 more>`

              List of items within the footer

              - `TextItem`

              - `HeadingItem`

              - `ListItem`

              - `CodeItem`

              - `TableItem`

              - `ImageItem`

              - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "footer"`

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

          - `true`

      - `FailedStructuredPage`

        - `error: string`

          Error message describing the failure

        - `page_number: number`

          Page number of the document

        - `success: false`

          Failure indicator

          - `false`

  - `job_metadata?: Record<string, unknown> | null`

    Job execution metadata (if requested)

  - `markdown?: Markdown | null`

    Markdown result (if requested)

    - `pages: Array<MarkdownResultPage | FailedMarkdownPage>`

      List of markdown pages or failed page entries

      - `MarkdownResultPage`

        - `markdown: string`

          Markdown content of the page

        - `page_number: number`

          Page number of the document

        - `success: true`

          Success indicator

          - `true`

        - `footer?: string | null`

          Footer of the page in markdown

        - `header?: string | null`

          Header of the page in markdown

      - `FailedMarkdownPage`

        - `error: string`

          Error message describing the failure

        - `page_number: number`

          Page number of the document

        - `success: false`

          Failure indicator

          - `false`

  - `markdown_full?: string | null`

    Full raw markdown content (if requested)

  - `metadata?: Metadata | null`

    Result containing metadata (page level and general) for the parsed document.

    - `pages: Array<Page>`

      List of page metadata entries

      - `page_number: number`

        Page number of the document

      - `confidence?: number | null`

        Confidence score for the page parsing (0-1)

      - `cost_optimized?: boolean | null`

        Whether cost-optimized parsing was used for the page

      - `original_orientation_angle?: number | null`

        Original orientation angle of the page in degrees

      - `printed_page_number?: string | null`

        Printed page number as it appears in the document

      - `slide_section_name?: string | null`

        Section name from presentation slides

      - `speaker_notes?: string | null`

        Speaker notes from presentation slides

      - `triggered_auto_mode?: boolean | null`

        Whether auto mode was triggered for the page

  - `raw_parameters?: Record<string, unknown> | null`

  - `result_content_metadata?: Record<string, ResultContentMetadata> | null`

    Metadata including size, existence, and presigned URLs for result files

    - `size_bytes: number`

      Size of the result file in bytes

    - `exists?: boolean`

      Whether the result file exists in S3

    - `presigned_url?: string | null`

      Presigned URL to download the result file

  - `text?: Text | null`

    Plain text result (if requested)

    - `pages: Array<Page>`

      List of text pages

      - `page_number: number`

        Page number of the document

      - `text: string`

        Plain text content of the page

  - `text_full?: string | null`

    Full raw text content (if requested)

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const parsing = await client.parsing.get('job_id');

console.log(parsing.job);
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

`client.parsing.list(ParsingListParamsquery?, RequestOptionsoptions?): PaginatedCursor<ParsingListResponse>`

**get** `/api/v2/parse`

List parse jobs for the current project.

Filter by `status` or creation date range. Results are
paginated — use `page_token` from the response to fetch
subsequent pages.

### Parameters

- `query: ParsingListParams`

  - `created_at_on_or_after?: string | null`

    Include items created at or after this timestamp (inclusive)

  - `created_at_on_or_before?: string | null`

    Include items created at or before this timestamp (inclusive)

  - `job_ids?: Array<string> | null`

    Filter by specific job IDs

  - `organization_id?: string | null`

  - `page_size?: number | null`

    Number of items per page

  - `page_token?: string | null`

    Token for pagination

  - `project_id?: string | null`

  - `status?: "PENDING" | "RUNNING" | "COMPLETED" | 2 more | null`

    Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

### Returns

- `ParsingListResponse`

  A parse job.

  - `id: string`

    Unique parse job identifier

  - `project_id: string`

    Project this job belongs to

  - `status: "PENDING" | "RUNNING" | "COMPLETED" | 2 more`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error details when status is FAILED

  - `name?: string | null`

    Optional display name for this parse job

  - `tier?: string | null`

    Parsing tier used for this job

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const parsingListResponse of client.parsing.list()) {
  console.log(parsingListResponse.id);
}
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

- `BBox`

  Bounding box with coordinates and optional metadata.

  - `h: number`

    Height of the bounding box

  - `w: number`

    Width of the bounding box

  - `x: number`

    X coordinate of the bounding box

  - `y: number`

    Y coordinate of the bounding box

  - `confidence?: number | null`

    Confidence score

  - `end_index?: number | null`

    End index in the text

  - `label?: string | null`

    Label for the bounding box

  - `start_index?: number | null`

    Start index in the text

### Code Item

- `CodeItem`

  - `md: string`

    Markdown representation preserving formatting

  - `value: string`

    Code content

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `language?: string | null`

    Programming language identifier

  - `type?: "code"`

    Code block item type

    - `"code"`

### Fail Page Mode

- `FailPageMode = "raw_text" | "blank_page" | "error_message"`

  Enum for representing the different available page error handling modes.

  - `"raw_text"`

  - `"blank_page"`

  - `"error_message"`

### Footer Item

- `FooterItem`

  - `items: Array<TextItem | HeadingItem | ListItem | 4 more>`

    List of items within the footer

    - `TextItem`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Text content

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "text"`

        Text item type

        - `"text"`

    - `HeadingItem`

      - `level: number`

        Heading level (1-6)

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Heading text content

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "heading"`

        Heading item type

        - `"heading"`

    - `ListItem`

      - `items: Array<TextItem | ListItem>`

        List of nested text or list items

        - `TextItem`

        - `ListItem`

      - `md: string`

        Markdown representation preserving formatting

      - `ordered: boolean`

        Whether the list is ordered or unordered

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "list"`

        List item type

        - `"list"`

    - `CodeItem`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Code content

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `language?: string | null`

        Programming language identifier

      - `type?: "code"`

        Code block item type

        - `"code"`

    - `TableItem`

      - `csv: string`

        CSV representation of the table

      - `html: string`

        HTML representation of the table

      - `md: string`

        Markdown representation preserving formatting

      - `rows: Array<Array<string | number | null>>`

        Table data as array of arrays (string, number, or null)

        - `string`

        - `number`

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `merged_from_pages?: Array<number> | null`

        List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

      - `merged_into_page?: number | null`

        Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

      - `parse_concerns?: Array<ParseConcern> | null`

        Quality concerns detected during table extraction, indicating the table may have issues

        - `details: string`

          Human-readable details about the concern

        - `type: string`

          Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

      - `type?: "table"`

        Table item type

        - `"table"`

    - `ImageItem`

      - `caption: string`

        Image caption

      - `md: string`

        Markdown representation preserving formatting

      - `url: string`

        URL to the image

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "image"`

        Image item type

        - `"image"`

    - `LinkItem`

      - `md: string`

        Markdown representation preserving formatting

      - `text: string`

        Display text of the link

      - `url: string`

        URL of the link

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "link"`

        Link item type

        - `"link"`

  - `md: string`

    Markdown representation preserving formatting

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `type?: "footer"`

    Page footer container

    - `"footer"`

### Header Item

- `HeaderItem`

  - `items: Array<TextItem | HeadingItem | ListItem | 4 more>`

    List of items within the header

    - `TextItem`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Text content

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "text"`

        Text item type

        - `"text"`

    - `HeadingItem`

      - `level: number`

        Heading level (1-6)

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Heading text content

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "heading"`

        Heading item type

        - `"heading"`

    - `ListItem`

      - `items: Array<TextItem | ListItem>`

        List of nested text or list items

        - `TextItem`

        - `ListItem`

      - `md: string`

        Markdown representation preserving formatting

      - `ordered: boolean`

        Whether the list is ordered or unordered

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "list"`

        List item type

        - `"list"`

    - `CodeItem`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Code content

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `language?: string | null`

        Programming language identifier

      - `type?: "code"`

        Code block item type

        - `"code"`

    - `TableItem`

      - `csv: string`

        CSV representation of the table

      - `html: string`

        HTML representation of the table

      - `md: string`

        Markdown representation preserving formatting

      - `rows: Array<Array<string | number | null>>`

        Table data as array of arrays (string, number, or null)

        - `string`

        - `number`

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `merged_from_pages?: Array<number> | null`

        List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

      - `merged_into_page?: number | null`

        Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

      - `parse_concerns?: Array<ParseConcern> | null`

        Quality concerns detected during table extraction, indicating the table may have issues

        - `details: string`

          Human-readable details about the concern

        - `type: string`

          Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

      - `type?: "table"`

        Table item type

        - `"table"`

    - `ImageItem`

      - `caption: string`

        Image caption

      - `md: string`

        Markdown representation preserving formatting

      - `url: string`

        URL to the image

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "image"`

        Image item type

        - `"image"`

    - `LinkItem`

      - `md: string`

        Markdown representation preserving formatting

      - `text: string`

        Display text of the link

      - `url: string`

        URL of the link

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "link"`

        Link item type

        - `"link"`

  - `md: string`

    Markdown representation preserving formatting

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `type?: "header"`

    Page header container

    - `"header"`

### Heading Item

- `HeadingItem`

  - `level: number`

    Heading level (1-6)

  - `md: string`

    Markdown representation preserving formatting

  - `value: string`

    Heading text content

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `type?: "heading"`

    Heading item type

    - `"heading"`

### Image Item

- `ImageItem`

  - `caption: string`

    Image caption

  - `md: string`

    Markdown representation preserving formatting

  - `url: string`

    URL to the image

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `type?: "image"`

    Image item type

    - `"image"`

### Link Item

- `LinkItem`

  - `md: string`

    Markdown representation preserving formatting

  - `text: string`

    Display text of the link

  - `url: string`

    URL of the link

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `type?: "link"`

    Link item type

    - `"link"`

### List Item

- `ListItem`

  - `items: Array<TextItem | ListItem>`

    List of nested text or list items

    - `TextItem`

      - `md: string`

        Markdown representation preserving formatting

      - `value: string`

        Text content

      - `bbox?: Array<BBox> | null`

        List of bounding boxes

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

        - `confidence?: number | null`

          Confidence score

        - `end_index?: number | null`

          End index in the text

        - `label?: string | null`

          Label for the bounding box

        - `start_index?: number | null`

          Start index in the text

      - `type?: "text"`

        Text item type

        - `"text"`

    - `ListItem`

  - `md: string`

    Markdown representation preserving formatting

  - `ordered: boolean`

    Whether the list is ordered or unordered

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `type?: "list"`

    List item type

    - `"list"`

### Llama Parse Supported File Extensions

- `LlamaParseSupportedFileExtensions = ".pdf" | ".abw" | ".awt" | 144 more`

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

- `ParsingJob`

  A parse job (v1).

  - `id: string`

    Unique parse job identifier

  - `status: StatusEnum`

    Current job status

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `error_code?: string | null`

    Machine-readable error code when failed

  - `error_message?: string | null`

    Human-readable error details when failed

### Parsing Languages

- `ParsingLanguages = "af" | "az" | "bs" | 83 more`

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

- `ParsingMode = "parse_page_without_llm" | "parse_page_with_llm" | "parse_page_with_lvm" | 5 more`

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

- `StatusEnum = "PENDING" | "SUCCESS" | "ERROR" | 2 more`

  Enum for representing the status of a job

  - `"PENDING"`

  - `"SUCCESS"`

  - `"ERROR"`

  - `"PARTIAL_SUCCESS"`

  - `"CANCELLED"`

### Table Item

- `TableItem`

  - `csv: string`

    CSV representation of the table

  - `html: string`

    HTML representation of the table

  - `md: string`

    Markdown representation preserving formatting

  - `rows: Array<Array<string | number | null>>`

    Table data as array of arrays (string, number, or null)

    - `string`

    - `number`

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `merged_from_pages?: Array<number> | null`

    List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

  - `merged_into_page?: number | null`

    Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

  - `parse_concerns?: Array<ParseConcern> | null`

    Quality concerns detected during table extraction, indicating the table may have issues

    - `details: string`

      Human-readable details about the concern

    - `type: string`

      Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

  - `type?: "table"`

    Table item type

    - `"table"`

### Text Item

- `TextItem`

  - `md: string`

    Markdown representation preserving formatting

  - `value: string`

    Text content

  - `bbox?: Array<BBox> | null`

    List of bounding boxes

    - `h: number`

      Height of the bounding box

    - `w: number`

      Width of the bounding box

    - `x: number`

      X coordinate of the bounding box

    - `y: number`

      Y coordinate of the bounding box

    - `confidence?: number | null`

      Confidence score

    - `end_index?: number | null`

      End index in the text

    - `label?: string | null`

      Label for the bounding box

    - `start_index?: number | null`

      Start index in the text

  - `type?: "text"`

    Text item type

    - `"text"`

### Parsing Create Response

- `ParsingCreateResponse`

  A parse job.

  - `id: string`

    Unique parse job identifier

  - `project_id: string`

    Project this job belongs to

  - `status: "PENDING" | "RUNNING" | "COMPLETED" | 2 more`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error details when status is FAILED

  - `name?: string | null`

    Optional display name for this parse job

  - `tier?: string | null`

    Parsing tier used for this job

  - `updated_at?: string | null`

    Update datetime

### Parsing Get Response

- `ParsingGetResponse`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `job: Job`

    Parse job status and metadata

    - `id: string`

      Unique parse job identifier

    - `project_id: string`

      Project this job belongs to

    - `status: "PENDING" | "RUNNING" | "COMPLETED" | 2 more`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `"PENDING"`

      - `"RUNNING"`

      - `"COMPLETED"`

      - `"FAILED"`

      - `"CANCELLED"`

    - `created_at?: string | null`

      Creation datetime

    - `error_message?: string | null`

      Error details when status is FAILED

    - `name?: string | null`

      Optional display name for this parse job

    - `tier?: string | null`

      Parsing tier used for this job

    - `updated_at?: string | null`

      Update datetime

  - `images_content_metadata?: ImagesContentMetadata | null`

    Metadata for all extracted images.

    - `images: Array<Image>`

      List of image metadata with presigned URLs

      - `filename: string`

        Image filename (e.g., 'image_0.png')

      - `index: number`

        Index of the image in the extraction order

      - `bbox?: Bbox | null`

        Bounding box for an image on its page.

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

      - `category?: "screenshot" | "embedded" | "layout" | null`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `content_type?: string | null`

        MIME type of the image

      - `presigned_url?: string | null`

        Presigned URL to download the image

      - `size_bytes?: number | null`

        Deprecated: always returns None. Will be removed in a future release.

    - `total_count: number`

      Total number of extracted images

  - `items?: Items | null`

    Structured JSON result (if requested)

    - `pages: Array<StructuredResultPage | FailedStructuredPage>`

      List of structured pages or failed page entries

      - `StructuredResultPage`

        - `items: Array<TextItem | HeadingItem | ListItem | 6 more>`

          List of structured items on the page

          - `TextItem`

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Text content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "text"`

              Text item type

              - `"text"`

          - `HeadingItem`

            - `level: number`

              Heading level (1-6)

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Heading text content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "heading"`

              Heading item type

              - `"heading"`

          - `ListItem`

            - `items: Array<TextItem | ListItem>`

              List of nested text or list items

              - `TextItem`

              - `ListItem`

            - `md: string`

              Markdown representation preserving formatting

            - `ordered: boolean`

              Whether the list is ordered or unordered

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "list"`

              List item type

              - `"list"`

          - `CodeItem`

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Code content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `language?: string | null`

              Programming language identifier

            - `type?: "code"`

              Code block item type

              - `"code"`

          - `TableItem`

            - `csv: string`

              CSV representation of the table

            - `html: string`

              HTML representation of the table

            - `md: string`

              Markdown representation preserving formatting

            - `rows: Array<Array<string | number | null>>`

              Table data as array of arrays (string, number, or null)

              - `string`

              - `number`

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `merged_from_pages?: Array<number> | null`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `merged_into_page?: number | null`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `parse_concerns?: Array<ParseConcern> | null`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `details: string`

                Human-readable details about the concern

              - `type: string`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `type?: "table"`

              Table item type

              - `"table"`

          - `ImageItem`

            - `caption: string`

              Image caption

            - `md: string`

              Markdown representation preserving formatting

            - `url: string`

              URL to the image

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "image"`

              Image item type

              - `"image"`

          - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `text: string`

              Display text of the link

            - `url: string`

              URL of the link

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "link"`

              Link item type

              - `"link"`

          - `HeaderItem`

            - `items: Array<TextItem | HeadingItem | ListItem | 4 more>`

              List of items within the header

              - `TextItem`

              - `HeadingItem`

              - `ListItem`

              - `CodeItem`

              - `TableItem`

              - `ImageItem`

              - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "header"`

              Page header container

              - `"header"`

          - `FooterItem`

            - `items: Array<TextItem | HeadingItem | ListItem | 4 more>`

              List of items within the footer

              - `TextItem`

              - `HeadingItem`

              - `ListItem`

              - `CodeItem`

              - `TableItem`

              - `ImageItem`

              - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "footer"`

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

          - `true`

      - `FailedStructuredPage`

        - `error: string`

          Error message describing the failure

        - `page_number: number`

          Page number of the document

        - `success: false`

          Failure indicator

          - `false`

  - `job_metadata?: Record<string, unknown> | null`

    Job execution metadata (if requested)

  - `markdown?: Markdown | null`

    Markdown result (if requested)

    - `pages: Array<MarkdownResultPage | FailedMarkdownPage>`

      List of markdown pages or failed page entries

      - `MarkdownResultPage`

        - `markdown: string`

          Markdown content of the page

        - `page_number: number`

          Page number of the document

        - `success: true`

          Success indicator

          - `true`

        - `footer?: string | null`

          Footer of the page in markdown

        - `header?: string | null`

          Header of the page in markdown

      - `FailedMarkdownPage`

        - `error: string`

          Error message describing the failure

        - `page_number: number`

          Page number of the document

        - `success: false`

          Failure indicator

          - `false`

  - `markdown_full?: string | null`

    Full raw markdown content (if requested)

  - `metadata?: Metadata | null`

    Result containing metadata (page level and general) for the parsed document.

    - `pages: Array<Page>`

      List of page metadata entries

      - `page_number: number`

        Page number of the document

      - `confidence?: number | null`

        Confidence score for the page parsing (0-1)

      - `cost_optimized?: boolean | null`

        Whether cost-optimized parsing was used for the page

      - `original_orientation_angle?: number | null`

        Original orientation angle of the page in degrees

      - `printed_page_number?: string | null`

        Printed page number as it appears in the document

      - `slide_section_name?: string | null`

        Section name from presentation slides

      - `speaker_notes?: string | null`

        Speaker notes from presentation slides

      - `triggered_auto_mode?: boolean | null`

        Whether auto mode was triggered for the page

  - `raw_parameters?: Record<string, unknown> | null`

  - `result_content_metadata?: Record<string, ResultContentMetadata> | null`

    Metadata including size, existence, and presigned URLs for result files

    - `size_bytes: number`

      Size of the result file in bytes

    - `exists?: boolean`

      Whether the result file exists in S3

    - `presigned_url?: string | null`

      Presigned URL to download the result file

  - `text?: Text | null`

    Plain text result (if requested)

    - `pages: Array<Page>`

      List of text pages

      - `page_number: number`

        Page number of the document

      - `text: string`

        Plain text content of the page

  - `text_full?: string | null`

    Full raw text content (if requested)

### Parsing List Response

- `ParsingListResponse`

  A parse job.

  - `id: string`

    Unique parse job identifier

  - `project_id: string`

    Project this job belongs to

  - `status: "PENDING" | "RUNNING" | "COMPLETED" | 2 more`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error details when status is FAILED

  - `name?: string | null`

    Optional display name for this parse job

  - `tier?: string | null`

    Parsing tier used for this job

  - `updated_at?: string | null`

    Update datetime
