# Parsing

## Parse File

`parsing.create(ParsingCreateParams**kwargs)  -> ParsingCreateResponse`

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

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

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

- `file_id: Optional[str]`

  ID of an existing file in the project to parse. Mutually exclusive with source_url

- `http_proxy: Optional[str]`

  HTTP/HTTPS proxy for fetching source_url. Ignored if using file_id

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

  - `additional_outputs: Optional[SequenceNotStr[str]]`

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

  - `auto_mode_configuration: Optional[Iterable[ProcessingOptionsAutoModeConfiguration]]`

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

    - `filename_match_glob_list: Optional[SequenceNotStr[str]]`

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

- `source_url: Optional[str]`

  Public URL of the document to parse. Mutually exclusive with file_id

- `webhook_configurations: Optional[Iterable[WebhookConfiguration]]`

  Webhook endpoints for job status notifications. Multiple webhooks can be configured for different events or services

  - `webhook_events: Optional[SequenceNotStr[str]]`

    Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

  - `webhook_headers: Optional[Dict[str, object]]`

    Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

  - `webhook_url: Optional[str]`

    HTTPS URL to receive webhook POST requests. Must be publicly accessible

### Returns

- `class ParsingCreateResponse: …`

  A parse job.

  - `id: str`

    Unique parse job identifier

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["PENDING", "RUNNING", "COMPLETED", 2 more]`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error details when status is FAILED

  - `name: Optional[str]`

    Optional display name for this parse job

  - `tier: Optional[str]`

    Parsing tier used for this job

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
parsing = client.parsing.create(
    tier="fast",
    version="latest",
)
print(parsing.id)
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

`parsing.get(strjob_id, ParsingGetParams**kwargs)  -> ParsingGetResponse`

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

- `job_id: str`

- `expand: Optional[SequenceNotStr[str]]`

  Fields to include: text, markdown, items, metadata, job_metadata, text_content_metadata, markdown_content_metadata, items_content_metadata, metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata, output_pdf_content_metadata, images_content_metadata. Metadata fields include presigned URLs.

- `image_filenames: Optional[str]`

  Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class ParsingGetResponse: …`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `job: Job`

    Parse job status and metadata

    - `id: str`

      Unique parse job identifier

    - `project_id: str`

      Project this job belongs to

    - `status: Literal["PENDING", "RUNNING", "COMPLETED", 2 more]`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `"PENDING"`

      - `"RUNNING"`

      - `"COMPLETED"`

      - `"FAILED"`

      - `"CANCELLED"`

    - `created_at: Optional[datetime]`

      Creation datetime

    - `error_message: Optional[str]`

      Error details when status is FAILED

    - `name: Optional[str]`

      Optional display name for this parse job

    - `tier: Optional[str]`

      Parsing tier used for this job

    - `updated_at: Optional[datetime]`

      Update datetime

  - `images_content_metadata: Optional[ImagesContentMetadata]`

    Metadata for all extracted images.

    - `images: List[ImagesContentMetadataImage]`

      List of image metadata with presigned URLs

      - `filename: str`

        Image filename (e.g., 'image_0.png')

      - `index: int`

        Index of the image in the extraction order

      - `bbox: Optional[ImagesContentMetadataImageBbox]`

        Bounding box for an image on its page.

        - `h: int`

          Height of the bounding box

        - `w: int`

          Width of the bounding box

        - `x: int`

          X coordinate of the bounding box

        - `y: int`

          Y coordinate of the bounding box

      - `category: Optional[Literal["screenshot", "embedded", "layout"]]`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `content_type: Optional[str]`

        MIME type of the image

      - `presigned_url: Optional[str]`

        Presigned URL to download the image

      - `size_bytes: Optional[int]`

        Deprecated: always returns None. Will be removed in a future release.

    - `total_count: int`

      Total number of extracted images

  - `items: Optional[Items]`

    Structured JSON result (if requested)

    - `pages: List[ItemsPage]`

      List of structured pages or failed page entries

      - `class ItemsPageStructuredResultPage: …`

        - `items: List[ItemsPageStructuredResultPageItem]`

          List of structured items on the page

          - `class TextItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Text content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["text"]]`

              Text item type

              - `"text"`

          - `class HeadingItem: …`

            - `level: int`

              Heading level (1-6)

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Heading text content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["heading"]]`

              Heading item type

              - `"heading"`

          - `class ListItem: …`

            - `items: List[Item]`

              List of nested text or list items

              - `class TextItem: …`

              - `class ListItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `ordered: bool`

              Whether the list is ordered or unordered

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["list"]]`

              List item type

              - `"list"`

          - `class CodeItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Code content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `language: Optional[str]`

              Programming language identifier

            - `type: Optional[Literal["code"]]`

              Code block item type

              - `"code"`

          - `class TableItem: …`

            - `csv: str`

              CSV representation of the table

            - `html: str`

              HTML representation of the table

            - `md: str`

              Markdown representation preserving formatting

            - `rows: List[List[Union[str, float, null]]]`

              Table data as array of arrays (string, number, or null)

              - `str`

              - `float`

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `merged_from_pages: Optional[List[int]]`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `merged_into_page: Optional[int]`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `parse_concerns: Optional[List[ParseConcern]]`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `details: str`

                Human-readable details about the concern

              - `type: str`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `type: Optional[Literal["table"]]`

              Table item type

              - `"table"`

          - `class ImageItem: …`

            - `caption: str`

              Image caption

            - `md: str`

              Markdown representation preserving formatting

            - `url: str`

              URL to the image

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["image"]]`

              Image item type

              - `"image"`

          - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `text: str`

              Display text of the link

            - `url: str`

              URL of the link

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["link"]]`

              Link item type

              - `"link"`

          - `class HeaderItem: …`

            - `items: List[Item]`

              List of items within the header

              - `class TextItem: …`

              - `class HeadingItem: …`

              - `class ListItem: …`

              - `class CodeItem: …`

              - `class TableItem: …`

              - `class ImageItem: …`

              - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["header"]]`

              Page header container

              - `"header"`

          - `class FooterItem: …`

            - `items: List[Item]`

              List of items within the footer

              - `class TextItem: …`

              - `class HeadingItem: …`

              - `class ListItem: …`

              - `class CodeItem: …`

              - `class TableItem: …`

              - `class ImageItem: …`

              - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["footer"]]`

              Page footer container

              - `"footer"`

        - `page_height: float`

          Height of the page in points

        - `page_number: int`

          Page number of the document

        - `page_width: float`

          Width of the page in points

        - `success: Literal[true]`

          Success indicator

          - `true`

      - `class ItemsPageFailedStructuredPage: …`

        - `error: str`

          Error message describing the failure

        - `page_number: int`

          Page number of the document

        - `success: Literal[false]`

          Failure indicator

          - `false`

  - `job_metadata: Optional[Dict[str, object]]`

    Job execution metadata (if requested)

  - `markdown: Optional[Markdown]`

    Markdown result (if requested)

    - `pages: List[MarkdownPage]`

      List of markdown pages or failed page entries

      - `class MarkdownPageMarkdownResultPage: …`

        - `markdown: str`

          Markdown content of the page

        - `page_number: int`

          Page number of the document

        - `success: Literal[true]`

          Success indicator

          - `true`

        - `footer: Optional[str]`

          Footer of the page in markdown

        - `header: Optional[str]`

          Header of the page in markdown

      - `class MarkdownPageFailedMarkdownPage: …`

        - `error: str`

          Error message describing the failure

        - `page_number: int`

          Page number of the document

        - `success: Literal[false]`

          Failure indicator

          - `false`

  - `markdown_full: Optional[str]`

    Full raw markdown content (if requested)

  - `metadata: Optional[Metadata]`

    Result containing metadata (page level and general) for the parsed document.

    - `pages: List[MetadataPage]`

      List of page metadata entries

      - `page_number: int`

        Page number of the document

      - `confidence: Optional[float]`

        Confidence score for the page parsing (0-1)

      - `cost_optimized: Optional[bool]`

        Whether cost-optimized parsing was used for the page

      - `original_orientation_angle: Optional[int]`

        Original orientation angle of the page in degrees

      - `printed_page_number: Optional[str]`

        Printed page number as it appears in the document

      - `slide_section_name: Optional[str]`

        Section name from presentation slides

      - `speaker_notes: Optional[str]`

        Speaker notes from presentation slides

      - `triggered_auto_mode: Optional[bool]`

        Whether auto mode was triggered for the page

  - `raw_parameters: Optional[Dict[str, object]]`

  - `result_content_metadata: Optional[Dict[str, ResultContentMetadata]]`

    Metadata including size, existence, and presigned URLs for result files

    - `size_bytes: int`

      Size of the result file in bytes

    - `exists: Optional[bool]`

      Whether the result file exists in S3

    - `presigned_url: Optional[str]`

      Presigned URL to download the result file

  - `text: Optional[Text]`

    Plain text result (if requested)

    - `pages: List[TextPage]`

      List of text pages

      - `page_number: int`

        Page number of the document

      - `text: str`

        Plain text content of the page

  - `text_full: Optional[str]`

    Full raw text content (if requested)

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
parsing = client.parsing.get(
    job_id="job_id",
)
print(parsing.job)
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

`parsing.list(ParsingListParams**kwargs)  -> SyncPaginatedCursor[ParsingListResponse]`

**get** `/api/v2/parse`

List parse jobs for the current project.

Filter by `status` or creation date range. Results are
paginated — use `page_token` from the response to fetch
subsequent pages.

### Parameters

- `created_at_on_or_after: Optional[Union[str, datetime, null]]`

  Include items created at or after this timestamp (inclusive)

- `created_at_on_or_before: Optional[Union[str, datetime, null]]`

  Include items created at or before this timestamp (inclusive)

- `job_ids: Optional[SequenceNotStr[str]]`

  Filter by specific job IDs

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

  Number of items per page

- `page_token: Optional[str]`

  Token for pagination

- `project_id: Optional[str]`

- `status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", 2 more]]`

  Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

  - `"PENDING"`

  - `"RUNNING"`

  - `"COMPLETED"`

  - `"FAILED"`

  - `"CANCELLED"`

### Returns

- `class ParsingListResponse: …`

  A parse job.

  - `id: str`

    Unique parse job identifier

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["PENDING", "RUNNING", "COMPLETED", 2 more]`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error details when status is FAILED

  - `name: Optional[str]`

    Optional display name for this parse job

  - `tier: Optional[str]`

    Parsing tier used for this job

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.parsing.list()
page = page.items[0]
print(page.id)
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

- `class BBox: …`

  Bounding box with coordinates and optional metadata.

  - `h: float`

    Height of the bounding box

  - `w: float`

    Width of the bounding box

  - `x: float`

    X coordinate of the bounding box

  - `y: float`

    Y coordinate of the bounding box

  - `confidence: Optional[float]`

    Confidence score

  - `end_index: Optional[int]`

    End index in the text

  - `label: Optional[str]`

    Label for the bounding box

  - `start_index: Optional[int]`

    Start index in the text

### Code Item

- `class CodeItem: …`

  - `md: str`

    Markdown representation preserving formatting

  - `value: str`

    Code content

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `language: Optional[str]`

    Programming language identifier

  - `type: Optional[Literal["code"]]`

    Code block item type

    - `"code"`

### Fail Page Mode

- `Literal["raw_text", "blank_page", "error_message"]`

  Enum for representing the different available page error handling modes.

  - `"raw_text"`

  - `"blank_page"`

  - `"error_message"`

### Footer Item

- `class FooterItem: …`

  - `items: List[Item]`

    List of items within the footer

    - `class TextItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `value: str`

        Text content

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["text"]]`

        Text item type

        - `"text"`

    - `class HeadingItem: …`

      - `level: int`

        Heading level (1-6)

      - `md: str`

        Markdown representation preserving formatting

      - `value: str`

        Heading text content

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["heading"]]`

        Heading item type

        - `"heading"`

    - `class ListItem: …`

      - `items: List[Item]`

        List of nested text or list items

        - `class TextItem: …`

        - `class ListItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `ordered: bool`

        Whether the list is ordered or unordered

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["list"]]`

        List item type

        - `"list"`

    - `class CodeItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `value: str`

        Code content

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `language: Optional[str]`

        Programming language identifier

      - `type: Optional[Literal["code"]]`

        Code block item type

        - `"code"`

    - `class TableItem: …`

      - `csv: str`

        CSV representation of the table

      - `html: str`

        HTML representation of the table

      - `md: str`

        Markdown representation preserving formatting

      - `rows: List[List[Union[str, float, null]]]`

        Table data as array of arrays (string, number, or null)

        - `str`

        - `float`

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `merged_from_pages: Optional[List[int]]`

        List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

      - `merged_into_page: Optional[int]`

        Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

      - `parse_concerns: Optional[List[ParseConcern]]`

        Quality concerns detected during table extraction, indicating the table may have issues

        - `details: str`

          Human-readable details about the concern

        - `type: str`

          Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

      - `type: Optional[Literal["table"]]`

        Table item type

        - `"table"`

    - `class ImageItem: …`

      - `caption: str`

        Image caption

      - `md: str`

        Markdown representation preserving formatting

      - `url: str`

        URL to the image

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["image"]]`

        Image item type

        - `"image"`

    - `class LinkItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `text: str`

        Display text of the link

      - `url: str`

        URL of the link

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["link"]]`

        Link item type

        - `"link"`

  - `md: str`

    Markdown representation preserving formatting

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `type: Optional[Literal["footer"]]`

    Page footer container

    - `"footer"`

### Header Item

- `class HeaderItem: …`

  - `items: List[Item]`

    List of items within the header

    - `class TextItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `value: str`

        Text content

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["text"]]`

        Text item type

        - `"text"`

    - `class HeadingItem: …`

      - `level: int`

        Heading level (1-6)

      - `md: str`

        Markdown representation preserving formatting

      - `value: str`

        Heading text content

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["heading"]]`

        Heading item type

        - `"heading"`

    - `class ListItem: …`

      - `items: List[Item]`

        List of nested text or list items

        - `class TextItem: …`

        - `class ListItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `ordered: bool`

        Whether the list is ordered or unordered

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["list"]]`

        List item type

        - `"list"`

    - `class CodeItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `value: str`

        Code content

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `language: Optional[str]`

        Programming language identifier

      - `type: Optional[Literal["code"]]`

        Code block item type

        - `"code"`

    - `class TableItem: …`

      - `csv: str`

        CSV representation of the table

      - `html: str`

        HTML representation of the table

      - `md: str`

        Markdown representation preserving formatting

      - `rows: List[List[Union[str, float, null]]]`

        Table data as array of arrays (string, number, or null)

        - `str`

        - `float`

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `merged_from_pages: Optional[List[int]]`

        List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

      - `merged_into_page: Optional[int]`

        Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

      - `parse_concerns: Optional[List[ParseConcern]]`

        Quality concerns detected during table extraction, indicating the table may have issues

        - `details: str`

          Human-readable details about the concern

        - `type: str`

          Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

      - `type: Optional[Literal["table"]]`

        Table item type

        - `"table"`

    - `class ImageItem: …`

      - `caption: str`

        Image caption

      - `md: str`

        Markdown representation preserving formatting

      - `url: str`

        URL to the image

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["image"]]`

        Image item type

        - `"image"`

    - `class LinkItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `text: str`

        Display text of the link

      - `url: str`

        URL of the link

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["link"]]`

        Link item type

        - `"link"`

  - `md: str`

    Markdown representation preserving formatting

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `type: Optional[Literal["header"]]`

    Page header container

    - `"header"`

### Heading Item

- `class HeadingItem: …`

  - `level: int`

    Heading level (1-6)

  - `md: str`

    Markdown representation preserving formatting

  - `value: str`

    Heading text content

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `type: Optional[Literal["heading"]]`

    Heading item type

    - `"heading"`

### Image Item

- `class ImageItem: …`

  - `caption: str`

    Image caption

  - `md: str`

    Markdown representation preserving formatting

  - `url: str`

    URL to the image

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `type: Optional[Literal["image"]]`

    Image item type

    - `"image"`

### Link Item

- `class LinkItem: …`

  - `md: str`

    Markdown representation preserving formatting

  - `text: str`

    Display text of the link

  - `url: str`

    URL of the link

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `type: Optional[Literal["link"]]`

    Link item type

    - `"link"`

### List Item

- `class ListItem: …`

  - `items: List[Item]`

    List of nested text or list items

    - `class TextItem: …`

      - `md: str`

        Markdown representation preserving formatting

      - `value: str`

        Text content

      - `bbox: Optional[List[BBox]]`

        List of bounding boxes

        - `h: float`

          Height of the bounding box

        - `w: float`

          Width of the bounding box

        - `x: float`

          X coordinate of the bounding box

        - `y: float`

          Y coordinate of the bounding box

        - `confidence: Optional[float]`

          Confidence score

        - `end_index: Optional[int]`

          End index in the text

        - `label: Optional[str]`

          Label for the bounding box

        - `start_index: Optional[int]`

          Start index in the text

      - `type: Optional[Literal["text"]]`

        Text item type

        - `"text"`

    - `class ListItem: …`

  - `md: str`

    Markdown representation preserving formatting

  - `ordered: bool`

    Whether the list is ordered or unordered

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `type: Optional[Literal["list"]]`

    List item type

    - `"list"`

### Llama Parse Supported File Extensions

- `Literal[".pdf", ".abw", ".awt", 144 more]`

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

- `class ParsingJob: …`

  A parse job (v1).

  - `id: str`

    Unique parse job identifier

  - `status: StatusEnum`

    Current job status

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `error_code: Optional[str]`

    Machine-readable error code when failed

  - `error_message: Optional[str]`

    Human-readable error details when failed

### Parsing Languages

- `Literal["af", "az", "bs", 83 more]`

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

- `Literal["parse_page_without_llm", "parse_page_with_llm", "parse_page_with_lvm", 5 more]`

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

- `Literal["PENDING", "SUCCESS", "ERROR", 2 more]`

  Enum for representing the status of a job

  - `"PENDING"`

  - `"SUCCESS"`

  - `"ERROR"`

  - `"PARTIAL_SUCCESS"`

  - `"CANCELLED"`

### Table Item

- `class TableItem: …`

  - `csv: str`

    CSV representation of the table

  - `html: str`

    HTML representation of the table

  - `md: str`

    Markdown representation preserving formatting

  - `rows: List[List[Union[str, float, null]]]`

    Table data as array of arrays (string, number, or null)

    - `str`

    - `float`

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `merged_from_pages: Optional[List[int]]`

    List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

  - `merged_into_page: Optional[int]`

    Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

  - `parse_concerns: Optional[List[ParseConcern]]`

    Quality concerns detected during table extraction, indicating the table may have issues

    - `details: str`

      Human-readable details about the concern

    - `type: str`

      Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

  - `type: Optional[Literal["table"]]`

    Table item type

    - `"table"`

### Text Item

- `class TextItem: …`

  - `md: str`

    Markdown representation preserving formatting

  - `value: str`

    Text content

  - `bbox: Optional[List[BBox]]`

    List of bounding boxes

    - `h: float`

      Height of the bounding box

    - `w: float`

      Width of the bounding box

    - `x: float`

      X coordinate of the bounding box

    - `y: float`

      Y coordinate of the bounding box

    - `confidence: Optional[float]`

      Confidence score

    - `end_index: Optional[int]`

      End index in the text

    - `label: Optional[str]`

      Label for the bounding box

    - `start_index: Optional[int]`

      Start index in the text

  - `type: Optional[Literal["text"]]`

    Text item type

    - `"text"`

### Parsing Create Response

- `class ParsingCreateResponse: …`

  A parse job.

  - `id: str`

    Unique parse job identifier

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["PENDING", "RUNNING", "COMPLETED", 2 more]`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error details when status is FAILED

  - `name: Optional[str]`

    Optional display name for this parse job

  - `tier: Optional[str]`

    Parsing tier used for this job

  - `updated_at: Optional[datetime]`

    Update datetime

### Parsing Get Response

- `class ParsingGetResponse: …`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `job: Job`

    Parse job status and metadata

    - `id: str`

      Unique parse job identifier

    - `project_id: str`

      Project this job belongs to

    - `status: Literal["PENDING", "RUNNING", "COMPLETED", 2 more]`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `"PENDING"`

      - `"RUNNING"`

      - `"COMPLETED"`

      - `"FAILED"`

      - `"CANCELLED"`

    - `created_at: Optional[datetime]`

      Creation datetime

    - `error_message: Optional[str]`

      Error details when status is FAILED

    - `name: Optional[str]`

      Optional display name for this parse job

    - `tier: Optional[str]`

      Parsing tier used for this job

    - `updated_at: Optional[datetime]`

      Update datetime

  - `images_content_metadata: Optional[ImagesContentMetadata]`

    Metadata for all extracted images.

    - `images: List[ImagesContentMetadataImage]`

      List of image metadata with presigned URLs

      - `filename: str`

        Image filename (e.g., 'image_0.png')

      - `index: int`

        Index of the image in the extraction order

      - `bbox: Optional[ImagesContentMetadataImageBbox]`

        Bounding box for an image on its page.

        - `h: int`

          Height of the bounding box

        - `w: int`

          Width of the bounding box

        - `x: int`

          X coordinate of the bounding box

        - `y: int`

          Y coordinate of the bounding box

      - `category: Optional[Literal["screenshot", "embedded", "layout"]]`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `content_type: Optional[str]`

        MIME type of the image

      - `presigned_url: Optional[str]`

        Presigned URL to download the image

      - `size_bytes: Optional[int]`

        Deprecated: always returns None. Will be removed in a future release.

    - `total_count: int`

      Total number of extracted images

  - `items: Optional[Items]`

    Structured JSON result (if requested)

    - `pages: List[ItemsPage]`

      List of structured pages or failed page entries

      - `class ItemsPageStructuredResultPage: …`

        - `items: List[ItemsPageStructuredResultPageItem]`

          List of structured items on the page

          - `class TextItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Text content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["text"]]`

              Text item type

              - `"text"`

          - `class HeadingItem: …`

            - `level: int`

              Heading level (1-6)

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Heading text content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["heading"]]`

              Heading item type

              - `"heading"`

          - `class ListItem: …`

            - `items: List[Item]`

              List of nested text or list items

              - `class TextItem: …`

              - `class ListItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `ordered: bool`

              Whether the list is ordered or unordered

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["list"]]`

              List item type

              - `"list"`

          - `class CodeItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Code content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `language: Optional[str]`

              Programming language identifier

            - `type: Optional[Literal["code"]]`

              Code block item type

              - `"code"`

          - `class TableItem: …`

            - `csv: str`

              CSV representation of the table

            - `html: str`

              HTML representation of the table

            - `md: str`

              Markdown representation preserving formatting

            - `rows: List[List[Union[str, float, null]]]`

              Table data as array of arrays (string, number, or null)

              - `str`

              - `float`

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `merged_from_pages: Optional[List[int]]`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `merged_into_page: Optional[int]`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `parse_concerns: Optional[List[ParseConcern]]`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `details: str`

                Human-readable details about the concern

              - `type: str`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `type: Optional[Literal["table"]]`

              Table item type

              - `"table"`

          - `class ImageItem: …`

            - `caption: str`

              Image caption

            - `md: str`

              Markdown representation preserving formatting

            - `url: str`

              URL to the image

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["image"]]`

              Image item type

              - `"image"`

          - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `text: str`

              Display text of the link

            - `url: str`

              URL of the link

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["link"]]`

              Link item type

              - `"link"`

          - `class HeaderItem: …`

            - `items: List[Item]`

              List of items within the header

              - `class TextItem: …`

              - `class HeadingItem: …`

              - `class ListItem: …`

              - `class CodeItem: …`

              - `class TableItem: …`

              - `class ImageItem: …`

              - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["header"]]`

              Page header container

              - `"header"`

          - `class FooterItem: …`

            - `items: List[Item]`

              List of items within the footer

              - `class TextItem: …`

              - `class HeadingItem: …`

              - `class ListItem: …`

              - `class CodeItem: …`

              - `class TableItem: …`

              - `class ImageItem: …`

              - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["footer"]]`

              Page footer container

              - `"footer"`

        - `page_height: float`

          Height of the page in points

        - `page_number: int`

          Page number of the document

        - `page_width: float`

          Width of the page in points

        - `success: Literal[true]`

          Success indicator

          - `true`

      - `class ItemsPageFailedStructuredPage: …`

        - `error: str`

          Error message describing the failure

        - `page_number: int`

          Page number of the document

        - `success: Literal[false]`

          Failure indicator

          - `false`

  - `job_metadata: Optional[Dict[str, object]]`

    Job execution metadata (if requested)

  - `markdown: Optional[Markdown]`

    Markdown result (if requested)

    - `pages: List[MarkdownPage]`

      List of markdown pages or failed page entries

      - `class MarkdownPageMarkdownResultPage: …`

        - `markdown: str`

          Markdown content of the page

        - `page_number: int`

          Page number of the document

        - `success: Literal[true]`

          Success indicator

          - `true`

        - `footer: Optional[str]`

          Footer of the page in markdown

        - `header: Optional[str]`

          Header of the page in markdown

      - `class MarkdownPageFailedMarkdownPage: …`

        - `error: str`

          Error message describing the failure

        - `page_number: int`

          Page number of the document

        - `success: Literal[false]`

          Failure indicator

          - `false`

  - `markdown_full: Optional[str]`

    Full raw markdown content (if requested)

  - `metadata: Optional[Metadata]`

    Result containing metadata (page level and general) for the parsed document.

    - `pages: List[MetadataPage]`

      List of page metadata entries

      - `page_number: int`

        Page number of the document

      - `confidence: Optional[float]`

        Confidence score for the page parsing (0-1)

      - `cost_optimized: Optional[bool]`

        Whether cost-optimized parsing was used for the page

      - `original_orientation_angle: Optional[int]`

        Original orientation angle of the page in degrees

      - `printed_page_number: Optional[str]`

        Printed page number as it appears in the document

      - `slide_section_name: Optional[str]`

        Section name from presentation slides

      - `speaker_notes: Optional[str]`

        Speaker notes from presentation slides

      - `triggered_auto_mode: Optional[bool]`

        Whether auto mode was triggered for the page

  - `raw_parameters: Optional[Dict[str, object]]`

  - `result_content_metadata: Optional[Dict[str, ResultContentMetadata]]`

    Metadata including size, existence, and presigned URLs for result files

    - `size_bytes: int`

      Size of the result file in bytes

    - `exists: Optional[bool]`

      Whether the result file exists in S3

    - `presigned_url: Optional[str]`

      Presigned URL to download the result file

  - `text: Optional[Text]`

    Plain text result (if requested)

    - `pages: List[TextPage]`

      List of text pages

      - `page_number: int`

        Page number of the document

      - `text: str`

        Plain text content of the page

  - `text_full: Optional[str]`

    Full raw text content (if requested)

### Parsing List Response

- `class ParsingListResponse: …`

  A parse job.

  - `id: str`

    Unique parse job identifier

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["PENDING", "RUNNING", "COMPLETED", 2 more]`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `"PENDING"`

    - `"RUNNING"`

    - `"COMPLETED"`

    - `"FAILED"`

    - `"CANCELLED"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error details when status is FAILED

  - `name: Optional[str]`

    Optional display name for this parse job

  - `tier: Optional[str]`

    Parsing tier used for this job

  - `updated_at: Optional[datetime]`

    Update datetime
