## List Configurations

`client.configurations.list(ConfigurationListParamsquery?, RequestOptionsoptions?): PaginatedCursor<ConfigurationResponse>`

**get** `/api/v1/beta/configurations`

List product configurations for the current project.

### Parameters

- `query: ConfigurationListParams`

  - `latest_only?: boolean`

    Return only the latest version per configuration name.

  - `name?: string | null`

    Filter by configuration name.

  - `organization_id?: string | null`

  - `page_size?: number | null`

    Number of items per page.

  - `page_token?: string | null`

    Pagination token.

  - `product_type?: Array<"split_v1" | "extract_v2" | "classify_v2" | 3 more> | null`

    Filter by one or more product types. Repeat the parameter for multiple values.

    - `"split_v1"`

    - `"extract_v2"`

    - `"classify_v2"`

    - `"parse_v2"`

    - `"spreadsheet_v1"`

    - `"unknown"`

  - `project_id?: string | null`

### Returns

- `ConfigurationResponse`

  Response schema for a single product configuration.

  - `id: string`

    Unique configuration ID.

  - `name: string`

    Configuration name.

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

  - `product_type: "split_v1" | "extract_v2" | "classify_v2" | 3 more`

    Product type.

    - `"split_v1"`

    - `"extract_v2"`

    - `"classify_v2"`

    - `"parse_v2"`

    - `"spreadsheet_v1"`

    - `"unknown"`

  - `version: string`

    Version identifier (datetime string).

  - `created_at?: string | null`

    Creation timestamp.

  - `updated_at?: string | null`

    Last update timestamp.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const configurationResponse of client.configurations.list()) {
  console.log(configurationResponse.id);
}
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "name": "name",
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
      },
      "product_type": "split_v1",
      "version": "version",
      "created_at": "2019-12-27T18:11:19.117Z",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
