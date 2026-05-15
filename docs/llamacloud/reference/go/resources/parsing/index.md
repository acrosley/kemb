# Parsing

## Parse File

`client.Parsing.New(ctx, params) (*ParsingNewResponse, error)`

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

- `params ParsingNewParams`

  - `Tier param.Field[ParsingNewParamsTier]`

    Body param: Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced), 'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with highest accuracy)

    - `const ParsingNewParamsTierFast ParsingNewParamsTier = "fast"`

    - `const ParsingNewParamsTierCostEffective ParsingNewParamsTier = "cost_effective"`

    - `const ParsingNewParamsTierAgentic ParsingNewParamsTier = "agentic"`

    - `const ParsingNewParamsTierAgenticPlus ParsingNewParamsTier = "agentic_plus"`

  - `Version param.Field[ParsingNewParamsVersion]`

    Body param: Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

    - `type ParsingNewParamsVersion string`

      Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

      - `const ParsingNewParamsVersionLatest ParsingNewParamsVersion = "latest"`

      - `const ParsingNewParamsVersion2026_05_13 ParsingNewParamsVersion = "2026-05-13"`

      - `const ParsingNewParamsVersion2026_05_11 ParsingNewParamsVersion = "2026-05-11"`

      - `const ParsingNewParamsVersion2026_04_09 ParsingNewParamsVersion = "2026-04-09"`

      - `const ParsingNewParamsVersion2025_12_11 ParsingNewParamsVersion = "2025-12-11"`

    - `string`

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `AgenticOptions param.Field[ParsingNewParamsAgenticOptions]`

    Body param: Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

    These options customize how the AI processes and interprets document content.
    Only applicable when using non-fast tiers.

    - `CustomPrompt string`

      Custom instructions for the AI parser. Use to guide extraction behavior, specify output formatting, or provide domain-specific context. Example: 'Extract financial tables with currency symbols. Format dates as YYYY-MM-DD.'

  - `ClientName param.Field[string]`

    Body param: Identifier for the client/application making the request. Used for analytics and debugging. Example: 'my-app-v2'

  - `CropBox param.Field[ParsingNewParamsCropBox]`

    Body param: Crop boundaries to process only a portion of each page. Values are ratios 0-1 from page edges

    - `Bottom float64`

      Bottom boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content below this line is excluded

    - `Left float64`

      Left boundary as ratio (0-1). 0=left edge, 1=right edge. Content left of this line is excluded

    - `Right float64`

      Right boundary as ratio (0-1). 0=left edge, 1=right edge. Content right of this line is excluded

    - `Top float64`

      Top boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content above this line is excluded

  - `DisableCache param.Field[bool]`

    Body param: Bypass result caching and force re-parsing. Use when document content may have changed or you need fresh results

  - `FastOptions param.Field[any]`

    Body param: Options for fast tier parsing (rule-based, no AI).

    Fast tier uses deterministic algorithms for text extraction without AI enhancement.
    It's the fastest and most cost-effective option, best suited for simple documents
    with standard layouts. Currently has no configurable options but reserved for
    future expansion.

  - `FileID param.Field[string]`

    Body param: ID of an existing file in the project to parse. Mutually exclusive with source_url

  - `HTTPProxy param.Field[string]`

    Body param: HTTP/HTTPS proxy for fetching source_url. Ignored if using file_id

  - `InputOptions param.Field[ParsingNewParamsInputOptions]`

    Body param: Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on detected input file type

    - `HTML ParsingNewParamsInputOptionsHTML`

      HTML/web page parsing options (applies to .html, .htm files)

      - `MakeAllElementsVisible bool`

        Force all HTML elements to be visible by overriding CSS display/visibility properties. Useful for parsing pages with hidden content or collapsed sections

      - `RemoveFixedElements bool`

        Remove fixed-position elements (headers, footers, floating buttons) that appear on every page render

      - `RemoveNavigationElements bool`

        Remove navigation elements (nav bars, sidebars, menus) to focus on main content

    - `Pdf any`

      PDF-specific parsing options (applies to .pdf files)

    - `Presentation ParsingNewParamsInputOptionsPresentation`

      Presentation parsing options (applies to .pptx, .ppt, .odp, .key files)

      - `OutOfBoundsContent bool`

        Extract content positioned outside the visible slide area. Some presentations have hidden notes or content that extends beyond slide boundaries

      - `SkipEmbeddedData bool`

        Skip extraction of embedded chart data tables. When true, only the visual representation of charts is captured, not the underlying data

    - `Spreadsheet ParsingNewParamsInputOptionsSpreadsheet`

      Spreadsheet parsing options (applies to .xlsx, .xls, .csv, .ods files)

      - `DetectSubTablesInSheets bool`

        Detect and extract multiple tables within a single sheet. Useful when spreadsheets contain several data regions separated by blank rows/columns

      - `ForceFormulaComputationInSheets bool`

        Compute formula results instead of extracting formula text. Use when you need calculated values rather than formula definitions

      - `IncludeHiddenSheets bool`

        Parse hidden sheets in addition to visible ones. By default, hidden sheets are skipped

  - `OutputOptions param.Field[ParsingNewParamsOutputOptions]`

    Body param: Output formatting options for markdown, text, and extracted images

    - `AdditionalOutputs []string`

      Optional additional output artifacts to save alongside the primary parse output. Each value opts in to generating and persisting one extra file; the empty list (default) saves none. The three accepted values are: 'stripped_md' — per-page markdown stripped of formatting (links, bold/italic, images, HTML), saved as JSON for full-text-search indexing; fetch via `expand=stripped_markdown_content_metadata`. 'concatenated_stripped_txt' — all stripped pages concatenated into a single plain-text file with `\n\n---\n\n` between pages, useful for feeding the document into search or embedding pipelines as one blob; fetch via `expand=concatenated_stripped_markdown_content_metadata`. 'word_bbox' — raw word-level bounding boxes (one JSON object per word, with page number and x/y/w/h coordinates) saved as JSONL, useful for highlighting or grounding extracted answers back to the source document; fetch via `expand=raw_words_content_metadata`.

    - `ExtractPrintedPageNumber bool`

      Extract the printed page number as it appears in the document (e.g., 'Page 5 of 10', 'v', 'A-3'). Useful for referencing original page numbers

    - `ImagesToSave []string`

      Image categories to extract and save. Options: 'screenshot' (full page renders useful for visual QA), 'embedded' (images found within the document), 'layout' (cropped regions from layout detection like figures and diagrams). Empty list saves no images

      - `const ParsingNewParamsOutputOptionsImagesToSaveScreenshot ParsingNewParamsOutputOptionsImagesToSave = "screenshot"`

      - `const ParsingNewParamsOutputOptionsImagesToSaveEmbedded ParsingNewParamsOutputOptionsImagesToSave = "embedded"`

      - `const ParsingNewParamsOutputOptionsImagesToSaveLayout ParsingNewParamsOutputOptionsImagesToSave = "layout"`

    - `Markdown ParsingNewParamsOutputOptionsMarkdown`

      Markdown formatting options including table styles and link annotations

      - `AnnotateLinks bool`

        Add link annotations to markdown output in the format [text](url). When false, only the link text is included

      - `InlineImages bool`

        Embed images directly in markdown as base64 data URIs instead of extracting them as separate files. Useful for self-contained markdown output

      - `Tables ParsingNewParamsOutputOptionsMarkdownTables`

        Table formatting options including markdown vs HTML format and merging behavior

        - `CompactMarkdownTables bool`

          Remove extra whitespace padding in markdown table cells for more compact output

        - `MarkdownTableMultilineSeparator string`

          Separator string for multiline cell content in markdown tables. Example: '<br>' to preserve line breaks, ' ' to join with spaces

        - `MergeContinuedTables bool`

          Automatically merge tables that span multiple pages into a single table. The merged table appears on the first page with merged_from_pages metadata

        - `OutputTablesAsMarkdown bool`

          Output tables as markdown pipe tables instead of HTML <table> tags. Markdown tables are simpler but cannot represent complex structures like merged cells

    - `SpatialText ParsingNewParamsOutputOptionsSpatialText`

      Spatial text output options for preserving document layout structure

      - `DoNotUnrollColumns bool`

        Keep multi-column layouts intact instead of linearizing columns into sequential text. Automatically enabled for non-fast tiers

      - `PreserveLayoutAlignmentAcrossPages bool`

        Maintain consistent text column alignment across page boundaries. Automatically enabled for document-level parsing modes

      - `PreserveVerySmallText bool`

        Include text below the normal size threshold. Useful for footnotes, watermarks, or fine print that might otherwise be filtered out

    - `TablesAsSpreadsheet ParsingNewParamsOutputOptionsTablesAsSpreadsheet`

      Options for exporting tables as XLSX spreadsheets

      - `Enable bool`

        Whether this option is enabled

      - `GuessSheetName bool`

        Automatically generate descriptive sheet names from table context (headers, surrounding text) instead of using generic names like 'Table_1'

  - `PageRanges param.Field[ParsingNewParamsPageRanges]`

    Body param: Page selection: limit total pages or specify exact pages to process

    - `MaxPages int64`

      Maximum number of pages to process. Pages are processed in order starting from page 1. If both max_pages and target_pages are set, target_pages takes precedence

    - `TargetPages string`

      Comma-separated list of specific pages to process using 1-based indexing. Supports individual pages and ranges. Examples: '1,3,5' (pages 1, 3, 5), '1-5' (pages 1 through 5 inclusive), '1,3,5-8,10' (pages 1, 3, 5-8, and 10). Pages are sorted and deduplicated automatically. Duplicate pages cause an error

  - `ProcessingControl param.Field[ParsingNewParamsProcessingControl]`

    Body param: Job execution controls including timeouts and failure thresholds

    - `JobFailureConditions ParsingNewParamsProcessingControlJobFailureConditions`

      Quality thresholds that determine when a job should fail vs complete with partial results

      - `AllowedPageFailureRatio float64`

        Maximum ratio of pages allowed to fail before the job fails (0-1). Example: 0.1 means job fails if more than 10% of pages fail. Default is 0.05 (5%)

      - `FailOnBuggyFont bool`

        Fail the job if a problematic font is detected that may cause incorrect text extraction. Buggy fonts can produce garbled or missing characters

      - `FailOnImageExtractionError bool`

        Fail the entire job if any embedded image cannot be extracted. By default, image extraction errors are logged but don't fail the job

      - `FailOnImageOcrError bool`

        Fail the entire job if OCR fails on any image. By default, OCR errors result in empty text for that image

      - `FailOnMarkdownReconstructionError bool`

        Fail the entire job if markdown cannot be reconstructed for any page. By default, failed pages use fallback text extraction

    - `Timeouts ParsingNewParamsProcessingControlTimeouts`

      Timeout settings for job execution. Increase for large or complex documents

      - `BaseInSeconds int64`

        Base timeout for the job in seconds (max 1800 = 30 minutes). This is the minimum time allowed regardless of document size

      - `ExtraTimePerPageInSeconds int64`

        Additional timeout per page in seconds (max 300 = 5 minutes). Total timeout = base + (this value × page count)

  - `ProcessingOptions param.Field[ParsingNewParamsProcessingOptions]`

    Body param: Document processing options including OCR, table extraction, and chart parsing

    - `AggressiveTableExtraction bool`

      Use aggressive heuristics to detect table boundaries, even without visible borders. Useful for documents with borderless or complex tables

    - `AutoModeConfiguration []ParsingNewParamsProcessingOptionsAutoModeConfiguration`

      Conditional processing rules that apply different parsing options based on page content, document structure, or filename patterns. Each entry defines trigger conditions and the parsing configuration to apply when triggered

      - `ParsingConf ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConf`

        Parsing configuration to apply when trigger conditions are met

        - `AdaptiveLongTable bool`

          Whether to use adaptive long table handling

        - `AggressiveTableExtraction bool`

          Whether to use aggressive table extraction

        - `CropBox ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfCropBox`

          Crop box options for auto mode parsing configuration.

          - `Bottom float64`

            Bottom boundary of crop box as ratio (0-1)

          - `Left float64`

            Left boundary of crop box as ratio (0-1)

          - `Right float64`

            Right boundary of crop box as ratio (0-1)

          - `Top float64`

            Top boundary of crop box as ratio (0-1)

        - `CustomPrompt string`

          Custom AI instructions for matched pages. Overrides the base custom_prompt

        - `ExtractLayout bool`

          Whether to extract layout information

        - `HighResOcr bool`

          Whether to use high resolution OCR

        - `Ignore ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfIgnore`

          Ignore options for auto mode parsing configuration.

          - `IgnoreDiagonalText bool`

            Whether to ignore diagonal text in the document

          - `IgnoreHiddenText bool`

            Whether to ignore hidden text in the document

        - `Language string`

          Primary language of the document

        - `OutlinedTableExtraction bool`

          Whether to use outlined table extraction

        - `Presentation ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfPresentation`

          Presentation-specific options for auto mode parsing configuration.

          - `OutOfBoundsContent bool`

            Extract out of bounds content in presentation slides

          - `SkipEmbeddedData bool`

            Skip extraction of embedded data for charts in presentation slides

        - `SpatialText ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfSpatialText`

          Spatial text options for auto mode parsing configuration.

          - `DoNotUnrollColumns bool`

            Keep column structure intact without unrolling

          - `PreserveLayoutAlignmentAcrossPages bool`

            Preserve text alignment across page boundaries

          - `PreserveVerySmallText bool`

            Include very small text in spatial output

        - `SpecializedChartParsing string`

          Enable specialized chart parsing with the specified mode

          - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsingAgenticPlus ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsing = "agentic_plus"`

          - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsingAgentic ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsing = "agentic"`

          - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsingEfficient ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsing = "efficient"`

        - `Tier string`

          Override the parsing tier for matched pages. Must be paired with version

          - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfTierFast ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfTier = "fast"`

          - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfTierCostEffective ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfTier = "cost_effective"`

          - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfTierAgentic ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfTier = "agentic"`

          - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfTierAgenticPlus ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfTier = "agentic_plus"`

        - `Version string`

          Tier version when overriding tier. Required when tier is specified

          - `string`

            - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersionLatest ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion = "latest"`

            - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion2026_05_13 ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion = "2026-05-13"`

            - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion2026_05_11 ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion = "2026-05-11"`

            - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion2026_04_09 ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion = "2026-04-09"`

            - `const ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion2025_12_11 ParsingNewParamsProcessingOptionsAutoModeConfigurationParsingConfVersion = "2025-12-11"`

          - `string`

      - `FilenameMatchGlob string`

        Single glob pattern to match against filename

      - `FilenameMatchGlobList []string`

        List of glob patterns to match against filename

      - `FilenameRegexp string`

        Regex pattern to match against filename

      - `FilenameRegexpMode string`

        Regex mode flags (e.g., 'i' for case-insensitive)

      - `FullPageImageInPage bool`

        Trigger if page contains a full-page image (scanned page detection)

      - `FullPageImageInPageThreshold ParsingNewParamsProcessingOptionsAutoModeConfigurationFullPageImageInPageThresholdUnion`

        Threshold for full page image detection (0.0-1.0, default 0.8)

        - `float64`

        - `string`

      - `ImageInPage bool`

        Trigger if page contains non-screenshot images

      - `LayoutElementInPage string`

        Trigger if page contains this layout element type

      - `LayoutElementInPageConfidenceThreshold ParsingNewParamsProcessingOptionsAutoModeConfigurationLayoutElementInPageConfidenceThresholdUnion`

        Confidence threshold for layout element detection

        - `float64`

        - `string`

      - `PageContainsAtLeastNCharts ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNChartsUnion`

        Trigger if page has more than N charts

        - `int64`

        - `string`

      - `PageContainsAtLeastNImages ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNImagesUnion`

        Trigger if page has more than N images

        - `int64`

        - `string`

      - `PageContainsAtLeastNLayoutElements ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNLayoutElementsUnion`

        Trigger if page has more than N layout elements

        - `int64`

        - `string`

      - `PageContainsAtLeastNLines ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNLinesUnion`

        Trigger if page has more than N lines

        - `int64`

        - `string`

      - `PageContainsAtLeastNLinks ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNLinksUnion`

        Trigger if page has more than N links

        - `int64`

        - `string`

      - `PageContainsAtLeastNNumbers ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNNumbersUnion`

        Trigger if page has more than N numeric words

        - `int64`

        - `string`

      - `PageContainsAtLeastNPercentNumbers ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNPercentNumbersUnion`

        Trigger if page has more than N% numeric words

        - `int64`

        - `string`

      - `PageContainsAtLeastNTables ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNTablesUnion`

        Trigger if page has more than N tables

        - `int64`

        - `string`

      - `PageContainsAtLeastNWords ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtLeastNWordsUnion`

        Trigger if page has more than N words

        - `int64`

        - `string`

      - `PageContainsAtMostNCharts ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNChartsUnion`

        Trigger if page has fewer than N charts

        - `int64`

        - `string`

      - `PageContainsAtMostNImages ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNImagesUnion`

        Trigger if page has fewer than N images

        - `int64`

        - `string`

      - `PageContainsAtMostNLayoutElements ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNLayoutElementsUnion`

        Trigger if page has fewer than N layout elements

        - `int64`

        - `string`

      - `PageContainsAtMostNLines ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNLinesUnion`

        Trigger if page has fewer than N lines

        - `int64`

        - `string`

      - `PageContainsAtMostNLinks ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNLinksUnion`

        Trigger if page has fewer than N links

        - `int64`

        - `string`

      - `PageContainsAtMostNNumbers ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNNumbersUnion`

        Trigger if page has fewer than N numeric words

        - `int64`

        - `string`

      - `PageContainsAtMostNPercentNumbers ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNPercentNumbersUnion`

        Trigger if page has fewer than N% numeric words

        - `int64`

        - `string`

      - `PageContainsAtMostNTables ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNTablesUnion`

        Trigger if page has fewer than N tables

        - `int64`

        - `string`

      - `PageContainsAtMostNWords ParsingNewParamsProcessingOptionsAutoModeConfigurationPageContainsAtMostNWordsUnion`

        Trigger if page has fewer than N words

        - `int64`

        - `string`

      - `PageLongerThanNChars ParsingNewParamsProcessingOptionsAutoModeConfigurationPageLongerThanNCharsUnion`

        Trigger if page has more than N characters

        - `int64`

        - `string`

      - `PageMdError bool`

        Trigger on pages with markdown extraction errors

      - `PageShorterThanNChars ParsingNewParamsProcessingOptionsAutoModeConfigurationPageShorterThanNCharsUnion`

        Trigger if page has fewer than N characters

        - `int64`

        - `string`

      - `RegexpInPage string`

        Regex pattern to match in page content

      - `RegexpInPageMode string`

        Regex mode flags for regexp_in_page

      - `TableInPage bool`

        Trigger if page contains a table

      - `TextInPage string`

        Trigger if page text/markdown contains this string

      - `TriggerMode string`

        How to combine multiple trigger conditions: 'and' (all conditions must match, this is the default) or 'or' (any single condition can trigger)

    - `CostOptimizer ParsingNewParamsProcessingOptionsCostOptimizer`

      Cost optimizer configuration for reducing parsing costs on simpler pages.

      When enabled, the parser analyzes each page and routes simpler pages to faster,
      cheaper processing while preserving quality for complex pages. Only works with
      'agentic' or 'agentic_plus' tiers.

      - `Enable bool`

        Enable cost-optimized parsing. Routes simpler pages to faster processing while complex pages use full AI analysis. May reduce speed on some documents. IMPORTANT: Only available with 'agentic' or 'agentic_plus' tiers

    - `DisableHeuristics bool`

      Disable automatic heuristics including outlined table extraction and adaptive long table handling. Use when heuristics produce incorrect results

    - `Ignore ParsingNewParamsProcessingOptionsIgnore`

      Options for ignoring specific text types (diagonal, hidden, text in images)

      - `IgnoreDiagonalText bool`

        Skip text rotated at an angle (not horizontal/vertical). Useful for ignoring watermarks or decorative angled text

      - `IgnoreHiddenText bool`

        Skip text marked as hidden in the document structure. Some PDFs contain invisible text layers used for accessibility or search indexing

      - `IgnoreTextInImage bool`

        Skip OCR text extraction from embedded images. Use when images contain irrelevant text (watermarks, logos) that shouldn't be in the output

    - `OcrParameters ParsingNewParamsProcessingOptionsOcrParameters`

      OCR configuration including language detection settings

      - `Languages []ParsingLanguages`

        Languages to use for OCR text recognition. Specify multiple languages if document contains mixed-language content. Order matters - put primary language first. Example: ['en', 'es'] for English with Spanish

        - `const ParsingLanguagesAf ParsingLanguages = "af"`

        - `const ParsingLanguagesAz ParsingLanguages = "az"`

        - `const ParsingLanguagesBs ParsingLanguages = "bs"`

        - `const ParsingLanguagesCs ParsingLanguages = "cs"`

        - `const ParsingLanguagesCy ParsingLanguages = "cy"`

        - `const ParsingLanguagesDa ParsingLanguages = "da"`

        - `const ParsingLanguagesDe ParsingLanguages = "de"`

        - `const ParsingLanguagesEn ParsingLanguages = "en"`

        - `const ParsingLanguagesEs ParsingLanguages = "es"`

        - `const ParsingLanguagesEt ParsingLanguages = "et"`

        - `const ParsingLanguagesFr ParsingLanguages = "fr"`

        - `const ParsingLanguagesGa ParsingLanguages = "ga"`

        - `const ParsingLanguagesHr ParsingLanguages = "hr"`

        - `const ParsingLanguagesHu ParsingLanguages = "hu"`

        - `const ParsingLanguagesID ParsingLanguages = "id"`

        - `const ParsingLanguagesIs ParsingLanguages = "is"`

        - `const ParsingLanguagesIt ParsingLanguages = "it"`

        - `const ParsingLanguagesKu ParsingLanguages = "ku"`

        - `const ParsingLanguagesLa ParsingLanguages = "la"`

        - `const ParsingLanguagesLt ParsingLanguages = "lt"`

        - `const ParsingLanguagesLv ParsingLanguages = "lv"`

        - `const ParsingLanguagesMi ParsingLanguages = "mi"`

        - `const ParsingLanguagesMs ParsingLanguages = "ms"`

        - `const ParsingLanguagesMt ParsingLanguages = "mt"`

        - `const ParsingLanguagesNl ParsingLanguages = "nl"`

        - `const ParsingLanguagesNo ParsingLanguages = "no"`

        - `const ParsingLanguagesOc ParsingLanguages = "oc"`

        - `const ParsingLanguagesPi ParsingLanguages = "pi"`

        - `const ParsingLanguagesPl ParsingLanguages = "pl"`

        - `const ParsingLanguagesPt ParsingLanguages = "pt"`

        - `const ParsingLanguagesRo ParsingLanguages = "ro"`

        - `const ParsingLanguagesRsLatin ParsingLanguages = "rs_latin"`

        - `const ParsingLanguagesSk ParsingLanguages = "sk"`

        - `const ParsingLanguagesSl ParsingLanguages = "sl"`

        - `const ParsingLanguagesSq ParsingLanguages = "sq"`

        - `const ParsingLanguagesSv ParsingLanguages = "sv"`

        - `const ParsingLanguagesSw ParsingLanguages = "sw"`

        - `const ParsingLanguagesTl ParsingLanguages = "tl"`

        - `const ParsingLanguagesTr ParsingLanguages = "tr"`

        - `const ParsingLanguagesUz ParsingLanguages = "uz"`

        - `const ParsingLanguagesVi ParsingLanguages = "vi"`

        - `const ParsingLanguagesAr ParsingLanguages = "ar"`

        - `const ParsingLanguagesFa ParsingLanguages = "fa"`

        - `const ParsingLanguagesUg ParsingLanguages = "ug"`

        - `const ParsingLanguagesUr ParsingLanguages = "ur"`

        - `const ParsingLanguagesBn ParsingLanguages = "bn"`

        - `const ParsingLanguagesAs ParsingLanguages = "as"`

        - `const ParsingLanguagesMni ParsingLanguages = "mni"`

        - `const ParsingLanguagesRu ParsingLanguages = "ru"`

        - `const ParsingLanguagesRsCyrillic ParsingLanguages = "rs_cyrillic"`

        - `const ParsingLanguagesBe ParsingLanguages = "be"`

        - `const ParsingLanguagesBg ParsingLanguages = "bg"`

        - `const ParsingLanguagesUk ParsingLanguages = "uk"`

        - `const ParsingLanguagesMn ParsingLanguages = "mn"`

        - `const ParsingLanguagesAbq ParsingLanguages = "abq"`

        - `const ParsingLanguagesAdy ParsingLanguages = "ady"`

        - `const ParsingLanguagesKbd ParsingLanguages = "kbd"`

        - `const ParsingLanguagesAva ParsingLanguages = "ava"`

        - `const ParsingLanguagesDar ParsingLanguages = "dar"`

        - `const ParsingLanguagesInh ParsingLanguages = "inh"`

        - `const ParsingLanguagesChe ParsingLanguages = "che"`

        - `const ParsingLanguagesLbe ParsingLanguages = "lbe"`

        - `const ParsingLanguagesLez ParsingLanguages = "lez"`

        - `const ParsingLanguagesTab ParsingLanguages = "tab"`

        - `const ParsingLanguagesTjk ParsingLanguages = "tjk"`

        - `const ParsingLanguagesHi ParsingLanguages = "hi"`

        - `const ParsingLanguagesMr ParsingLanguages = "mr"`

        - `const ParsingLanguagesNe ParsingLanguages = "ne"`

        - `const ParsingLanguagesBh ParsingLanguages = "bh"`

        - `const ParsingLanguagesMai ParsingLanguages = "mai"`

        - `const ParsingLanguagesAng ParsingLanguages = "ang"`

        - `const ParsingLanguagesBho ParsingLanguages = "bho"`

        - `const ParsingLanguagesMah ParsingLanguages = "mah"`

        - `const ParsingLanguagesSck ParsingLanguages = "sck"`

        - `const ParsingLanguagesNew ParsingLanguages = "new"`

        - `const ParsingLanguagesGom ParsingLanguages = "gom"`

        - `const ParsingLanguagesSa ParsingLanguages = "sa"`

        - `const ParsingLanguagesBgc ParsingLanguages = "bgc"`

        - `const ParsingLanguagesTh ParsingLanguages = "th"`

        - `const ParsingLanguagesChSim ParsingLanguages = "ch_sim"`

        - `const ParsingLanguagesChTra ParsingLanguages = "ch_tra"`

        - `const ParsingLanguagesJa ParsingLanguages = "ja"`

        - `const ParsingLanguagesKo ParsingLanguages = "ko"`

        - `const ParsingLanguagesTa ParsingLanguages = "ta"`

        - `const ParsingLanguagesTe ParsingLanguages = "te"`

        - `const ParsingLanguagesKn ParsingLanguages = "kn"`

    - `SpecializedChartParsing string`

      Enable AI-powered chart analysis. Modes: 'efficient' (fast, lower cost), 'agentic' (balanced), 'agentic_plus' (highest accuracy). Automatically enables extract_layout and precise_bounding_box when set

      - `const ParsingNewParamsProcessingOptionsSpecializedChartParsingAgenticPlus ParsingNewParamsProcessingOptionsSpecializedChartParsing = "agentic_plus"`

      - `const ParsingNewParamsProcessingOptionsSpecializedChartParsingAgentic ParsingNewParamsProcessingOptionsSpecializedChartParsing = "agentic"`

      - `const ParsingNewParamsProcessingOptionsSpecializedChartParsingEfficient ParsingNewParamsProcessingOptionsSpecializedChartParsing = "efficient"`

  - `SourceURL param.Field[string]`

    Body param: Public URL of the document to parse. Mutually exclusive with file_id

  - `WebhookConfigurations param.Field[[]ParsingNewParamsWebhookConfiguration]`

    Body param: Webhook endpoints for job status notifications. Multiple webhooks can be configured for different events or services

    - `WebhookEvents []string`

      Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

    - `WebhookHeaders map[string, any]`

      Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

    - `WebhookURL string`

      HTTPS URL to receive webhook POST requests. Must be publicly accessible

### Returns

- `type ParsingNewResponse struct{…}`

  A parse job.

  - `ID string`

    Unique parse job identifier

  - `ProjectID string`

    Project this job belongs to

  - `Status ParsingNewResponseStatus`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `const ParsingNewResponseStatusPending ParsingNewResponseStatus = "PENDING"`

    - `const ParsingNewResponseStatusRunning ParsingNewResponseStatus = "RUNNING"`

    - `const ParsingNewResponseStatusCompleted ParsingNewResponseStatus = "COMPLETED"`

    - `const ParsingNewResponseStatusFailed ParsingNewResponseStatus = "FAILED"`

    - `const ParsingNewResponseStatusCancelled ParsingNewResponseStatus = "CANCELLED"`

  - `CreatedAt Time`

    Creation datetime

  - `ErrorMessage string`

    Error details when status is FAILED

  - `Name string`

    Optional display name for this parse job

  - `Tier string`

    Parsing tier used for this job

  - `UpdatedAt Time`

    Update datetime

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
  parsing, err := client.Parsing.New(context.TODO(), llamacloudprod.ParsingNewParams{
    Tier: llamacloudprod.ParsingNewParamsTierFast,
    Version: llamacloudprod.ParsingNewParamsVersionLatest,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", parsing.ID)
}
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

`client.Parsing.Get(ctx, jobID, query) (*ParsingGetResponse, error)`

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

- `jobID string`

- `query ParsingGetParams`

  - `Expand param.Field[[]string]`

    Fields to include: text, markdown, items, metadata, job_metadata, text_content_metadata, markdown_content_metadata, items_content_metadata, metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata, output_pdf_content_metadata, images_content_metadata. Metadata fields include presigned URLs.

  - `ImageFilenames param.Field[string]`

    Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type ParsingGetResponse struct{…}`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `Job ParsingGetResponseJob`

    Parse job status and metadata

    - `ID string`

      Unique parse job identifier

    - `ProjectID string`

      Project this job belongs to

    - `Status string`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `const ParsingGetResponseJobStatusPending ParsingGetResponseJobStatus = "PENDING"`

      - `const ParsingGetResponseJobStatusRunning ParsingGetResponseJobStatus = "RUNNING"`

      - `const ParsingGetResponseJobStatusCompleted ParsingGetResponseJobStatus = "COMPLETED"`

      - `const ParsingGetResponseJobStatusFailed ParsingGetResponseJobStatus = "FAILED"`

      - `const ParsingGetResponseJobStatusCancelled ParsingGetResponseJobStatus = "CANCELLED"`

    - `CreatedAt Time`

      Creation datetime

    - `ErrorMessage string`

      Error details when status is FAILED

    - `Name string`

      Optional display name for this parse job

    - `Tier string`

      Parsing tier used for this job

    - `UpdatedAt Time`

      Update datetime

  - `ImagesContentMetadata ParsingGetResponseImagesContentMetadata`

    Metadata for all extracted images.

    - `Images []ParsingGetResponseImagesContentMetadataImage`

      List of image metadata with presigned URLs

      - `Filename string`

        Image filename (e.g., 'image_0.png')

      - `Index int64`

        Index of the image in the extraction order

      - `Bbox ParsingGetResponseImagesContentMetadataImageBbox`

        Bounding box for an image on its page.

        - `H int64`

          Height of the bounding box

        - `W int64`

          Width of the bounding box

        - `X int64`

          X coordinate of the bounding box

        - `Y int64`

          Y coordinate of the bounding box

      - `Category string`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `const ParsingGetResponseImagesContentMetadataImageCategoryScreenshot ParsingGetResponseImagesContentMetadataImageCategory = "screenshot"`

        - `const ParsingGetResponseImagesContentMetadataImageCategoryEmbedded ParsingGetResponseImagesContentMetadataImageCategory = "embedded"`

        - `const ParsingGetResponseImagesContentMetadataImageCategoryLayout ParsingGetResponseImagesContentMetadataImageCategory = "layout"`

      - `ContentType string`

        MIME type of the image

      - `PresignedURL string`

        Presigned URL to download the image

      - `SizeBytes int64`

        Deprecated: always returns None. Will be removed in a future release.

    - `TotalCount int64`

      Total number of extracted images

  - `Items ParsingGetResponseItems`

    Structured JSON result (if requested)

    - `Pages []ParsingGetResponseItemsPageUnion`

      List of structured pages or failed page entries

      - `type ParsingGetResponseItemsPageStructuredResultPage struct{…}`

        - `Items []ParsingGetResponseItemsPageStructuredResultPageItemUnion`

          List of structured items on the page

          - `type TextItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Value string`

              Text content

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type TextItemType`

              Text item type

              - `const TextItemTypeText TextItemType = "text"`

          - `type HeadingItem struct{…}`

            - `Level int64`

              Heading level (1-6)

            - `Md string`

              Markdown representation preserving formatting

            - `Value string`

              Heading text content

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type HeadingItemType`

              Heading item type

              - `const HeadingItemTypeHeading HeadingItemType = "heading"`

          - `type ListItem struct{…}`

            - `Items []ListItemItemUnion`

              List of nested text or list items

              - `type TextItem struct{…}`

              - `type ListItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Ordered bool`

              Whether the list is ordered or unordered

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type ListItemType`

              List item type

              - `const ListItemTypeList ListItemType = "list"`

          - `type CodeItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Value string`

              Code content

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Language string`

              Programming language identifier

            - `Type CodeItemType`

              Code block item type

              - `const CodeItemTypeCode CodeItemType = "code"`

          - `type TableItem struct{…}`

            - `Csv string`

              CSV representation of the table

            - `HTML string`

              HTML representation of the table

            - `Md string`

              Markdown representation preserving formatting

            - `Rows [][]TableItemRowUnion`

              Table data as array of arrays (string, number, or null)

              - `string`

              - `float64`

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `MergedFromPages []int64`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `MergedIntoPage int64`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `ParseConcerns []TableItemParseConcern`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `Details string`

                Human-readable details about the concern

              - `Type string`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `Type TableItemType`

              Table item type

              - `const TableItemTypeTable TableItemType = "table"`

          - `type ImageItem struct{…}`

            - `Caption string`

              Image caption

            - `Md string`

              Markdown representation preserving formatting

            - `URL string`

              URL to the image

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type ImageItemType`

              Image item type

              - `const ImageItemTypeImage ImageItemType = "image"`

          - `type LinkItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Text string`

              Display text of the link

            - `URL string`

              URL of the link

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type LinkItemType`

              Link item type

              - `const LinkItemTypeLink LinkItemType = "link"`

          - `type HeaderItem struct{…}`

            - `Items []HeaderItemItemUnion`

              List of items within the header

              - `type TextItem struct{…}`

              - `type HeadingItem struct{…}`

              - `type ListItem struct{…}`

              - `type CodeItem struct{…}`

              - `type TableItem struct{…}`

              - `type ImageItem struct{…}`

              - `type LinkItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type HeaderItemType`

              Page header container

              - `const HeaderItemTypeHeader HeaderItemType = "header"`

          - `type FooterItem struct{…}`

            - `Items []FooterItemItemUnion`

              List of items within the footer

              - `type TextItem struct{…}`

              - `type HeadingItem struct{…}`

              - `type ListItem struct{…}`

              - `type CodeItem struct{…}`

              - `type TableItem struct{…}`

              - `type ImageItem struct{…}`

              - `type LinkItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type FooterItemType`

              Page footer container

              - `const FooterItemTypeFooter FooterItemType = "footer"`

        - `PageHeight float64`

          Height of the page in points

        - `PageNumber int64`

          Page number of the document

        - `PageWidth float64`

          Width of the page in points

        - `Success bool`

          Success indicator

          - `const ParsingGetResponseItemsPageStructuredResultPageSuccessTrue ParsingGetResponseItemsPageStructuredResultPageSuccess = true`

      - `type ParsingGetResponseItemsPageFailedStructuredPage struct{…}`

        - `Error string`

          Error message describing the failure

        - `PageNumber int64`

          Page number of the document

        - `Success bool`

          Failure indicator

          - `const ParsingGetResponseItemsPageFailedStructuredPageSuccessFalse ParsingGetResponseItemsPageFailedStructuredPageSuccess = false`

  - `JobMetadata map[string, any]`

    Job execution metadata (if requested)

  - `Markdown ParsingGetResponseMarkdown`

    Markdown result (if requested)

    - `Pages []ParsingGetResponseMarkdownPageUnion`

      List of markdown pages or failed page entries

      - `type ParsingGetResponseMarkdownPageMarkdownResultPage struct{…}`

        - `Markdown string`

          Markdown content of the page

        - `PageNumber int64`

          Page number of the document

        - `Success bool`

          Success indicator

          - `const ParsingGetResponseMarkdownPageMarkdownResultPageSuccessTrue ParsingGetResponseMarkdownPageMarkdownResultPageSuccess = true`

        - `Footer string`

          Footer of the page in markdown

        - `Header string`

          Header of the page in markdown

      - `type ParsingGetResponseMarkdownPageFailedMarkdownPage struct{…}`

        - `Error string`

          Error message describing the failure

        - `PageNumber int64`

          Page number of the document

        - `Success bool`

          Failure indicator

          - `const ParsingGetResponseMarkdownPageFailedMarkdownPageSuccessFalse ParsingGetResponseMarkdownPageFailedMarkdownPageSuccess = false`

  - `MarkdownFull string`

    Full raw markdown content (if requested)

  - `Metadata ParsingGetResponseMetadata`

    Result containing metadata (page level and general) for the parsed document.

    - `Pages []ParsingGetResponseMetadataPage`

      List of page metadata entries

      - `PageNumber int64`

        Page number of the document

      - `Confidence float64`

        Confidence score for the page parsing (0-1)

      - `CostOptimized bool`

        Whether cost-optimized parsing was used for the page

      - `OriginalOrientationAngle int64`

        Original orientation angle of the page in degrees

      - `PrintedPageNumber string`

        Printed page number as it appears in the document

      - `SlideSectionName string`

        Section name from presentation slides

      - `SpeakerNotes string`

        Speaker notes from presentation slides

      - `TriggeredAutoMode bool`

        Whether auto mode was triggered for the page

  - `RawParameters map[string, any]`

  - `ResultContentMetadata map[string, ParsingGetResponseResultContentMetadata]`

    Metadata including size, existence, and presigned URLs for result files

    - `SizeBytes int64`

      Size of the result file in bytes

    - `Exists bool`

      Whether the result file exists in S3

    - `PresignedURL string`

      Presigned URL to download the result file

  - `Text ParsingGetResponseText`

    Plain text result (if requested)

    - `Pages []ParsingGetResponseTextPage`

      List of text pages

      - `PageNumber int64`

        Page number of the document

      - `Text string`

        Plain text content of the page

  - `TextFull string`

    Full raw text content (if requested)

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
  parsing, err := client.Parsing.Get(
    context.TODO(),
    "job_id",
    llamacloudprod.ParsingGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", parsing.Job)
}
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

`client.Parsing.List(ctx, query) (*PaginatedCursor[ParsingListResponse], error)`

**get** `/api/v2/parse`

List parse jobs for the current project.

Filter by `status` or creation date range. Results are
paginated — use `page_token` from the response to fetch
subsequent pages.

### Parameters

- `query ParsingListParams`

  - `CreatedAtOnOrAfter param.Field[Time]`

    Include items created at or after this timestamp (inclusive)

  - `CreatedAtOnOrBefore param.Field[Time]`

    Include items created at or before this timestamp (inclusive)

  - `JobIDs param.Field[[]string]`

    Filter by specific job IDs

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

    Number of items per page

  - `PageToken param.Field[string]`

    Token for pagination

  - `ProjectID param.Field[string]`

  - `Status param.Field[ParsingListParamsStatus]`

    Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

    - `const ParsingListParamsStatusPending ParsingListParamsStatus = "PENDING"`

    - `const ParsingListParamsStatusRunning ParsingListParamsStatus = "RUNNING"`

    - `const ParsingListParamsStatusCompleted ParsingListParamsStatus = "COMPLETED"`

    - `const ParsingListParamsStatusFailed ParsingListParamsStatus = "FAILED"`

    - `const ParsingListParamsStatusCancelled ParsingListParamsStatus = "CANCELLED"`

### Returns

- `type ParsingListResponse struct{…}`

  A parse job.

  - `ID string`

    Unique parse job identifier

  - `ProjectID string`

    Project this job belongs to

  - `Status ParsingListResponseStatus`

    Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

    - `const ParsingListResponseStatusPending ParsingListResponseStatus = "PENDING"`

    - `const ParsingListResponseStatusRunning ParsingListResponseStatus = "RUNNING"`

    - `const ParsingListResponseStatusCompleted ParsingListResponseStatus = "COMPLETED"`

    - `const ParsingListResponseStatusFailed ParsingListResponseStatus = "FAILED"`

    - `const ParsingListResponseStatusCancelled ParsingListResponseStatus = "CANCELLED"`

  - `CreatedAt Time`

    Creation datetime

  - `ErrorMessage string`

    Error details when status is FAILED

  - `Name string`

    Optional display name for this parse job

  - `Tier string`

    Parsing tier used for this job

  - `UpdatedAt Time`

    Update datetime

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
  page, err := client.Parsing.List(context.TODO(), llamacloudprod.ParsingListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

- `type BBox struct{…}`

  Bounding box with coordinates and optional metadata.

  - `H float64`

    Height of the bounding box

  - `W float64`

    Width of the bounding box

  - `X float64`

    X coordinate of the bounding box

  - `Y float64`

    Y coordinate of the bounding box

  - `Confidence float64`

    Confidence score

  - `EndIndex int64`

    End index in the text

  - `Label string`

    Label for the bounding box

  - `StartIndex int64`

    Start index in the text

### Code Item

- `type CodeItem struct{…}`

  - `Md string`

    Markdown representation preserving formatting

  - `Value string`

    Code content

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `Language string`

    Programming language identifier

  - `Type CodeItemType`

    Code block item type

    - `const CodeItemTypeCode CodeItemType = "code"`

### Fail Page Mode

- `type FailPageMode string`

  Enum for representing the different available page error handling modes.

  - `const FailPageModeRawText FailPageMode = "raw_text"`

  - `const FailPageModeBlankPage FailPageMode = "blank_page"`

  - `const FailPageModeErrorMessage FailPageMode = "error_message"`

### Footer Item

- `type FooterItem struct{…}`

  - `Items []FooterItemItemUnion`

    List of items within the footer

    - `type TextItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Value string`

        Text content

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type TextItemType`

        Text item type

        - `const TextItemTypeText TextItemType = "text"`

    - `type HeadingItem struct{…}`

      - `Level int64`

        Heading level (1-6)

      - `Md string`

        Markdown representation preserving formatting

      - `Value string`

        Heading text content

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type HeadingItemType`

        Heading item type

        - `const HeadingItemTypeHeading HeadingItemType = "heading"`

    - `type ListItem struct{…}`

      - `Items []ListItemItemUnion`

        List of nested text or list items

        - `type TextItem struct{…}`

        - `type ListItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Ordered bool`

        Whether the list is ordered or unordered

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type ListItemType`

        List item type

        - `const ListItemTypeList ListItemType = "list"`

    - `type CodeItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Value string`

        Code content

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Language string`

        Programming language identifier

      - `Type CodeItemType`

        Code block item type

        - `const CodeItemTypeCode CodeItemType = "code"`

    - `type TableItem struct{…}`

      - `Csv string`

        CSV representation of the table

      - `HTML string`

        HTML representation of the table

      - `Md string`

        Markdown representation preserving formatting

      - `Rows [][]TableItemRowUnion`

        Table data as array of arrays (string, number, or null)

        - `string`

        - `float64`

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `MergedFromPages []int64`

        List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

      - `MergedIntoPage int64`

        Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

      - `ParseConcerns []TableItemParseConcern`

        Quality concerns detected during table extraction, indicating the table may have issues

        - `Details string`

          Human-readable details about the concern

        - `Type string`

          Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

      - `Type TableItemType`

        Table item type

        - `const TableItemTypeTable TableItemType = "table"`

    - `type ImageItem struct{…}`

      - `Caption string`

        Image caption

      - `Md string`

        Markdown representation preserving formatting

      - `URL string`

        URL to the image

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type ImageItemType`

        Image item type

        - `const ImageItemTypeImage ImageItemType = "image"`

    - `type LinkItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Text string`

        Display text of the link

      - `URL string`

        URL of the link

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type LinkItemType`

        Link item type

        - `const LinkItemTypeLink LinkItemType = "link"`

  - `Md string`

    Markdown representation preserving formatting

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `Type FooterItemType`

    Page footer container

    - `const FooterItemTypeFooter FooterItemType = "footer"`

### Header Item

- `type HeaderItem struct{…}`

  - `Items []HeaderItemItemUnion`

    List of items within the header

    - `type TextItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Value string`

        Text content

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type TextItemType`

        Text item type

        - `const TextItemTypeText TextItemType = "text"`

    - `type HeadingItem struct{…}`

      - `Level int64`

        Heading level (1-6)

      - `Md string`

        Markdown representation preserving formatting

      - `Value string`

        Heading text content

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type HeadingItemType`

        Heading item type

        - `const HeadingItemTypeHeading HeadingItemType = "heading"`

    - `type ListItem struct{…}`

      - `Items []ListItemItemUnion`

        List of nested text or list items

        - `type TextItem struct{…}`

        - `type ListItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Ordered bool`

        Whether the list is ordered or unordered

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type ListItemType`

        List item type

        - `const ListItemTypeList ListItemType = "list"`

    - `type CodeItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Value string`

        Code content

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Language string`

        Programming language identifier

      - `Type CodeItemType`

        Code block item type

        - `const CodeItemTypeCode CodeItemType = "code"`

    - `type TableItem struct{…}`

      - `Csv string`

        CSV representation of the table

      - `HTML string`

        HTML representation of the table

      - `Md string`

        Markdown representation preserving formatting

      - `Rows [][]TableItemRowUnion`

        Table data as array of arrays (string, number, or null)

        - `string`

        - `float64`

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `MergedFromPages []int64`

        List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

      - `MergedIntoPage int64`

        Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

      - `ParseConcerns []TableItemParseConcern`

        Quality concerns detected during table extraction, indicating the table may have issues

        - `Details string`

          Human-readable details about the concern

        - `Type string`

          Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

      - `Type TableItemType`

        Table item type

        - `const TableItemTypeTable TableItemType = "table"`

    - `type ImageItem struct{…}`

      - `Caption string`

        Image caption

      - `Md string`

        Markdown representation preserving formatting

      - `URL string`

        URL to the image

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type ImageItemType`

        Image item type

        - `const ImageItemTypeImage ImageItemType = "image"`

    - `type LinkItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Text string`

        Display text of the link

      - `URL string`

        URL of the link

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type LinkItemType`

        Link item type

        - `const LinkItemTypeLink LinkItemType = "link"`

  - `Md string`

    Markdown representation preserving formatting

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `Type HeaderItemType`

    Page header container

    - `const HeaderItemTypeHeader HeaderItemType = "header"`

### Heading Item

- `type HeadingItem struct{…}`

  - `Level int64`

    Heading level (1-6)

  - `Md string`

    Markdown representation preserving formatting

  - `Value string`

    Heading text content

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `Type HeadingItemType`

    Heading item type

    - `const HeadingItemTypeHeading HeadingItemType = "heading"`

### Image Item

- `type ImageItem struct{…}`

  - `Caption string`

    Image caption

  - `Md string`

    Markdown representation preserving formatting

  - `URL string`

    URL to the image

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `Type ImageItemType`

    Image item type

    - `const ImageItemTypeImage ImageItemType = "image"`

### Link Item

- `type LinkItem struct{…}`

  - `Md string`

    Markdown representation preserving formatting

  - `Text string`

    Display text of the link

  - `URL string`

    URL of the link

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `Type LinkItemType`

    Link item type

    - `const LinkItemTypeLink LinkItemType = "link"`

### List Item

- `type ListItem struct{…}`

  - `Items []ListItemItemUnion`

    List of nested text or list items

    - `type TextItem struct{…}`

      - `Md string`

        Markdown representation preserving formatting

      - `Value string`

        Text content

      - `Bbox []BBox`

        List of bounding boxes

        - `H float64`

          Height of the bounding box

        - `W float64`

          Width of the bounding box

        - `X float64`

          X coordinate of the bounding box

        - `Y float64`

          Y coordinate of the bounding box

        - `Confidence float64`

          Confidence score

        - `EndIndex int64`

          End index in the text

        - `Label string`

          Label for the bounding box

        - `StartIndex int64`

          Start index in the text

      - `Type TextItemType`

        Text item type

        - `const TextItemTypeText TextItemType = "text"`

    - `type ListItem struct{…}`

  - `Md string`

    Markdown representation preserving formatting

  - `Ordered bool`

    Whether the list is ordered or unordered

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `Type ListItemType`

    List item type

    - `const ListItemTypeList ListItemType = "list"`

### Llama Parse Supported File Extensions

- `type LlamaParseSupportedFileExtensions string`

  Enum for supported file extensions.

  - `const LlamaParseSupportedFileExtensionsPdf LlamaParseSupportedFileExtensions = ".pdf"`

  - `const LlamaParseSupportedFileExtensionsAbw LlamaParseSupportedFileExtensions = ".abw"`

  - `const LlamaParseSupportedFileExtensionsAwt LlamaParseSupportedFileExtensions = ".awt"`

  - `const LlamaParseSupportedFileExtensionsCgm LlamaParseSupportedFileExtensions = ".cgm"`

  - `const LlamaParseSupportedFileExtensionsCwk LlamaParseSupportedFileExtensions = ".cwk"`

  - `const LlamaParseSupportedFileExtensionsDoc LlamaParseSupportedFileExtensions = ".doc"`

  - `const LlamaParseSupportedFileExtensionsDocm LlamaParseSupportedFileExtensions = ".docm"`

  - `const LlamaParseSupportedFileExtensionsDocx LlamaParseSupportedFileExtensions = ".docx"`

  - `const LlamaParseSupportedFileExtensionsDot LlamaParseSupportedFileExtensions = ".dot"`

  - `const LlamaParseSupportedFileExtensionsDotm LlamaParseSupportedFileExtensions = ".dotm"`

  - `const LlamaParseSupportedFileExtensionsDotx LlamaParseSupportedFileExtensions = ".dotx"`

  - `const LlamaParseSupportedFileExtensionsFodg LlamaParseSupportedFileExtensions = ".fodg"`

  - `const LlamaParseSupportedFileExtensionsFodp LlamaParseSupportedFileExtensions = ".fodp"`

  - `const LlamaParseSupportedFileExtensionsFopd LlamaParseSupportedFileExtensions = ".fopd"`

  - `const LlamaParseSupportedFileExtensionsFodt LlamaParseSupportedFileExtensions = ".fodt"`

  - `const LlamaParseSupportedFileExtensionsFb2 LlamaParseSupportedFileExtensions = ".fb2"`

  - `const LlamaParseSupportedFileExtensionsHwp LlamaParseSupportedFileExtensions = ".hwp"`

  - `const LlamaParseSupportedFileExtensionsLwp LlamaParseSupportedFileExtensions = ".lwp"`

  - `const LlamaParseSupportedFileExtensionsMcw LlamaParseSupportedFileExtensions = ".mcw"`

  - `const LlamaParseSupportedFileExtensionsMw LlamaParseSupportedFileExtensions = ".mw"`

  - `const LlamaParseSupportedFileExtensionsMwd LlamaParseSupportedFileExtensions = ".mwd"`

  - `const LlamaParseSupportedFileExtensionsOdf LlamaParseSupportedFileExtensions = ".odf"`

  - `const LlamaParseSupportedFileExtensionsOdt LlamaParseSupportedFileExtensions = ".odt"`

  - `const LlamaParseSupportedFileExtensionsOtg LlamaParseSupportedFileExtensions = ".otg"`

  - `const LlamaParseSupportedFileExtensionsOtt LlamaParseSupportedFileExtensions = ".ott"`

  - `const LlamaParseSupportedFileExtensionsPages LlamaParseSupportedFileExtensions = ".pages"`

  - `const LlamaParseSupportedFileExtensionsPbd LlamaParseSupportedFileExtensions = ".pbd"`

  - `const LlamaParseSupportedFileExtensionsPsw LlamaParseSupportedFileExtensions = ".psw"`

  - `const LlamaParseSupportedFileExtensionsRtf LlamaParseSupportedFileExtensions = ".rtf"`

  - `const LlamaParseSupportedFileExtensionsSda LlamaParseSupportedFileExtensions = ".sda"`

  - `const LlamaParseSupportedFileExtensionsSdd LlamaParseSupportedFileExtensions = ".sdd"`

  - `const LlamaParseSupportedFileExtensionsSdp LlamaParseSupportedFileExtensions = ".sdp"`

  - `const LlamaParseSupportedFileExtensionsSdw LlamaParseSupportedFileExtensions = ".sdw"`

  - `const LlamaParseSupportedFileExtensionsSgl LlamaParseSupportedFileExtensions = ".sgl"`

  - `const LlamaParseSupportedFileExtensionsStd LlamaParseSupportedFileExtensions = ".std"`

  - `const LlamaParseSupportedFileExtensionsStw LlamaParseSupportedFileExtensions = ".stw"`

  - `const LlamaParseSupportedFileExtensionsSxd LlamaParseSupportedFileExtensions = ".sxd"`

  - `const LlamaParseSupportedFileExtensionsSxg LlamaParseSupportedFileExtensions = ".sxg"`

  - `const LlamaParseSupportedFileExtensionsSxm LlamaParseSupportedFileExtensions = ".sxm"`

  - `const LlamaParseSupportedFileExtensionsSxw LlamaParseSupportedFileExtensions = ".sxw"`

  - `const LlamaParseSupportedFileExtensionsUof LlamaParseSupportedFileExtensions = ".uof"`

  - `const LlamaParseSupportedFileExtensionsUop LlamaParseSupportedFileExtensions = ".uop"`

  - `const LlamaParseSupportedFileExtensionsUot LlamaParseSupportedFileExtensions = ".uot"`

  - `const LlamaParseSupportedFileExtensionsVor LlamaParseSupportedFileExtensions = ".vor"`

  - `const LlamaParseSupportedFileExtensionsWpd LlamaParseSupportedFileExtensions = ".wpd"`

  - `const LlamaParseSupportedFileExtensionsWps LlamaParseSupportedFileExtensions = ".wps"`

  - `const LlamaParseSupportedFileExtensionsWpt LlamaParseSupportedFileExtensions = ".wpt"`

  - `const LlamaParseSupportedFileExtensionsWri LlamaParseSupportedFileExtensions = ".wri"`

  - `const LlamaParseSupportedFileExtensionsWn LlamaParseSupportedFileExtensions = ".wn"`

  - `const LlamaParseSupportedFileExtensionsXml LlamaParseSupportedFileExtensions = ".xml"`

  - `const LlamaParseSupportedFileExtensionsZabw LlamaParseSupportedFileExtensions = ".zabw"`

  - `const LlamaParseSupportedFileExtensionsKey LlamaParseSupportedFileExtensions = ".key"`

  - `const LlamaParseSupportedFileExtensionsOdp LlamaParseSupportedFileExtensions = ".odp"`

  - `const LlamaParseSupportedFileExtensionsOdg LlamaParseSupportedFileExtensions = ".odg"`

  - `const LlamaParseSupportedFileExtensionsOtp LlamaParseSupportedFileExtensions = ".otp"`

  - `const LlamaParseSupportedFileExtensionsPot LlamaParseSupportedFileExtensions = ".pot"`

  - `const LlamaParseSupportedFileExtensionsPotm LlamaParseSupportedFileExtensions = ".potm"`

  - `const LlamaParseSupportedFileExtensionsPotx LlamaParseSupportedFileExtensions = ".potx"`

  - `const LlamaParseSupportedFileExtensionsPpt LlamaParseSupportedFileExtensions = ".ppt"`

  - `const LlamaParseSupportedFileExtensionsPptm LlamaParseSupportedFileExtensions = ".pptm"`

  - `const LlamaParseSupportedFileExtensionsPptx LlamaParseSupportedFileExtensions = ".pptx"`

  - `const LlamaParseSupportedFileExtensionsSti LlamaParseSupportedFileExtensions = ".sti"`

  - `const LlamaParseSupportedFileExtensionsSxi LlamaParseSupportedFileExtensions = ".sxi"`

  - `const LlamaParseSupportedFileExtensionsVsd LlamaParseSupportedFileExtensions = ".vsd"`

  - `const LlamaParseSupportedFileExtensionsVsdm LlamaParseSupportedFileExtensions = ".vsdm"`

  - `const LlamaParseSupportedFileExtensionsVsdx LlamaParseSupportedFileExtensions = ".vsdx"`

  - `const LlamaParseSupportedFileExtensionsVdx LlamaParseSupportedFileExtensions = ".vdx"`

  - `const LlamaParseSupportedFileExtensionsBmp LlamaParseSupportedFileExtensions = ".bmp"`

  - `const LlamaParseSupportedFileExtensionsGif LlamaParseSupportedFileExtensions = ".gif"`

  - `const LlamaParseSupportedFileExtensionsHeic LlamaParseSupportedFileExtensions = ".heic"`

  - `const LlamaParseSupportedFileExtensionsHeif LlamaParseSupportedFileExtensions = ".heif"`

  - `const LlamaParseSupportedFileExtensionsJpg LlamaParseSupportedFileExtensions = ".jpg"`

  - `const LlamaParseSupportedFileExtensionsJpeg LlamaParseSupportedFileExtensions = ".jpeg"`

  - `const LlamaParseSupportedFileExtensionsPng LlamaParseSupportedFileExtensions = ".png"`

  - `const LlamaParseSupportedFileExtensionsSvg LlamaParseSupportedFileExtensions = ".svg"`

  - `const LlamaParseSupportedFileExtensionsTif LlamaParseSupportedFileExtensions = ".tif"`

  - `const LlamaParseSupportedFileExtensionsTiff LlamaParseSupportedFileExtensions = ".tiff"`

  - `const LlamaParseSupportedFileExtensionsWebp LlamaParseSupportedFileExtensions = ".webp"`

  - `const LlamaParseSupportedFileExtensionsHtm LlamaParseSupportedFileExtensions = ".htm"`

  - `const LlamaParseSupportedFileExtensionsHTML LlamaParseSupportedFileExtensions = ".html"`

  - `const LlamaParseSupportedFileExtensionsXhtm LlamaParseSupportedFileExtensions = ".xhtm"`

  - `const LlamaParseSupportedFileExtensionsCsv LlamaParseSupportedFileExtensions = ".csv"`

  - `const LlamaParseSupportedFileExtensionsDbf LlamaParseSupportedFileExtensions = ".dbf"`

  - `const LlamaParseSupportedFileExtensionsDif LlamaParseSupportedFileExtensions = ".dif"`

  - `const LlamaParseSupportedFileExtensionsEt LlamaParseSupportedFileExtensions = ".et"`

  - `const LlamaParseSupportedFileExtensionsEth LlamaParseSupportedFileExtensions = ".eth"`

  - `const LlamaParseSupportedFileExtensionsFods LlamaParseSupportedFileExtensions = ".fods"`

  - `const LlamaParseSupportedFileExtensionsNumbers LlamaParseSupportedFileExtensions = ".numbers"`

  - `const LlamaParseSupportedFileExtensionsOds LlamaParseSupportedFileExtensions = ".ods"`

  - `const LlamaParseSupportedFileExtensionsOts LlamaParseSupportedFileExtensions = ".ots"`

  - `const LlamaParseSupportedFileExtensionsPrn LlamaParseSupportedFileExtensions = ".prn"`

  - `const LlamaParseSupportedFileExtensionsQpw LlamaParseSupportedFileExtensions = ".qpw"`

  - `const LlamaParseSupportedFileExtensionsSlk LlamaParseSupportedFileExtensions = ".slk"`

  - `const LlamaParseSupportedFileExtensionsStc LlamaParseSupportedFileExtensions = ".stc"`

  - `const LlamaParseSupportedFileExtensionsSxc LlamaParseSupportedFileExtensions = ".sxc"`

  - `const LlamaParseSupportedFileExtensionsSylk LlamaParseSupportedFileExtensions = ".sylk"`

  - `const LlamaParseSupportedFileExtensionsTsv LlamaParseSupportedFileExtensions = ".tsv"`

  - `const LlamaParseSupportedFileExtensionsUos1 LlamaParseSupportedFileExtensions = ".uos1"`

  - `const LlamaParseSupportedFileExtensionsUos2 LlamaParseSupportedFileExtensions = ".uos2"`

  - `const LlamaParseSupportedFileExtensionsUos LlamaParseSupportedFileExtensions = ".uos"`

  - `const LlamaParseSupportedFileExtensionsWb1 LlamaParseSupportedFileExtensions = ".wb1"`

  - `const LlamaParseSupportedFileExtensionsWb2 LlamaParseSupportedFileExtensions = ".wb2"`

  - `const LlamaParseSupportedFileExtensionsWb3 LlamaParseSupportedFileExtensions = ".wb3"`

  - `const LlamaParseSupportedFileExtensionsWk1 LlamaParseSupportedFileExtensions = ".wk1"`

  - `const LlamaParseSupportedFileExtensionsWk2 LlamaParseSupportedFileExtensions = ".wk2"`

  - `const LlamaParseSupportedFileExtensionsWk3 LlamaParseSupportedFileExtensions = ".wk3"`

  - `const LlamaParseSupportedFileExtensionsWk4 LlamaParseSupportedFileExtensions = ".wk4"`

  - `const LlamaParseSupportedFileExtensionsWks LlamaParseSupportedFileExtensions = ".wks"`

  - `const LlamaParseSupportedFileExtensionsWq1 LlamaParseSupportedFileExtensions = ".wq1"`

  - `const LlamaParseSupportedFileExtensionsWq2 LlamaParseSupportedFileExtensions = ".wq2"`

  - `const LlamaParseSupportedFileExtensionsXlr LlamaParseSupportedFileExtensions = ".xlr"`

  - `const LlamaParseSupportedFileExtensionsXls LlamaParseSupportedFileExtensions = ".xls"`

  - `const LlamaParseSupportedFileExtensionsXlsb LlamaParseSupportedFileExtensions = ".xlsb"`

  - `const LlamaParseSupportedFileExtensionsXlsm LlamaParseSupportedFileExtensions = ".xlsm"`

  - `const LlamaParseSupportedFileExtensionsXlsx LlamaParseSupportedFileExtensions = ".xlsx"`

  - `const LlamaParseSupportedFileExtensionsXlw LlamaParseSupportedFileExtensions = ".xlw"`

  - `const LlamaParseSupportedFileExtensionsAzw LlamaParseSupportedFileExtensions = ".azw"`

  - `const LlamaParseSupportedFileExtensionsAzw3 LlamaParseSupportedFileExtensions = ".azw3"`

  - `const LlamaParseSupportedFileExtensionsAzw4 LlamaParseSupportedFileExtensions = ".azw4"`

  - `const LlamaParseSupportedFileExtensionsCb7 LlamaParseSupportedFileExtensions = ".cb7"`

  - `const LlamaParseSupportedFileExtensionsCbc LlamaParseSupportedFileExtensions = ".cbc"`

  - `const LlamaParseSupportedFileExtensionsCbr LlamaParseSupportedFileExtensions = ".cbr"`

  - `const LlamaParseSupportedFileExtensionsCbz LlamaParseSupportedFileExtensions = ".cbz"`

  - `const LlamaParseSupportedFileExtensionsChm LlamaParseSupportedFileExtensions = ".chm"`

  - `const LlamaParseSupportedFileExtensionsDjvu LlamaParseSupportedFileExtensions = ".djvu"`

  - `const LlamaParseSupportedFileExtensionsEpub LlamaParseSupportedFileExtensions = ".epub"`

  - `const LlamaParseSupportedFileExtensionsFbz LlamaParseSupportedFileExtensions = ".fbz"`

  - `const LlamaParseSupportedFileExtensionsHtmlz LlamaParseSupportedFileExtensions = ".htmlz"`

  - `const LlamaParseSupportedFileExtensionsLit LlamaParseSupportedFileExtensions = ".lit"`

  - `const LlamaParseSupportedFileExtensionsLrf LlamaParseSupportedFileExtensions = ".lrf"`

  - `const LlamaParseSupportedFileExtensionsMd LlamaParseSupportedFileExtensions = ".md"`

  - `const LlamaParseSupportedFileExtensionsMobi LlamaParseSupportedFileExtensions = ".mobi"`

  - `const LlamaParseSupportedFileExtensionsPdb LlamaParseSupportedFileExtensions = ".pdb"`

  - `const LlamaParseSupportedFileExtensionsPml LlamaParseSupportedFileExtensions = ".pml"`

  - `const LlamaParseSupportedFileExtensionsPrc LlamaParseSupportedFileExtensions = ".prc"`

  - `const LlamaParseSupportedFileExtensionsRb LlamaParseSupportedFileExtensions = ".rb"`

  - `const LlamaParseSupportedFileExtensionsSnb LlamaParseSupportedFileExtensions = ".snb"`

  - `const LlamaParseSupportedFileExtensionsTcr LlamaParseSupportedFileExtensions = ".tcr"`

  - `const LlamaParseSupportedFileExtensionsTxtz LlamaParseSupportedFileExtensions = ".txtz"`

  - `const LlamaParseSupportedFileExtensionsM4a LlamaParseSupportedFileExtensions = ".m4a"`

  - `const LlamaParseSupportedFileExtensionsMP3 LlamaParseSupportedFileExtensions = ".mp3"`

  - `const LlamaParseSupportedFileExtensionsMP4 LlamaParseSupportedFileExtensions = ".mp4"`

  - `const LlamaParseSupportedFileExtensionsMpeg LlamaParseSupportedFileExtensions = ".mpeg"`

  - `const LlamaParseSupportedFileExtensionsMpga LlamaParseSupportedFileExtensions = ".mpga"`

  - `const LlamaParseSupportedFileExtensionsWav LlamaParseSupportedFileExtensions = ".wav"`

  - `const LlamaParseSupportedFileExtensionsWebm LlamaParseSupportedFileExtensions = ".webm"`

  - `const LlamaParseSupportedFileExtensionsYxmd LlamaParseSupportedFileExtensions = ".yxmd"`

### Parsing Job

- `type ParsingJob struct{…}`

  A parse job (v1).

  - `ID string`

    Unique parse job identifier

  - `Status StatusEnum`

    Current job status

    - `const StatusEnumPending StatusEnum = "PENDING"`

    - `const StatusEnumSuccess StatusEnum = "SUCCESS"`

    - `const StatusEnumError StatusEnum = "ERROR"`

    - `const StatusEnumPartialSuccess StatusEnum = "PARTIAL_SUCCESS"`

    - `const StatusEnumCancelled StatusEnum = "CANCELLED"`

  - `ErrorCode string`

    Machine-readable error code when failed

  - `ErrorMessage string`

    Human-readable error details when failed

### Parsing Languages

- `type ParsingLanguages string`

  Enum for representing the languages supported by the parser.

  - `const ParsingLanguagesAf ParsingLanguages = "af"`

  - `const ParsingLanguagesAz ParsingLanguages = "az"`

  - `const ParsingLanguagesBs ParsingLanguages = "bs"`

  - `const ParsingLanguagesCs ParsingLanguages = "cs"`

  - `const ParsingLanguagesCy ParsingLanguages = "cy"`

  - `const ParsingLanguagesDa ParsingLanguages = "da"`

  - `const ParsingLanguagesDe ParsingLanguages = "de"`

  - `const ParsingLanguagesEn ParsingLanguages = "en"`

  - `const ParsingLanguagesEs ParsingLanguages = "es"`

  - `const ParsingLanguagesEt ParsingLanguages = "et"`

  - `const ParsingLanguagesFr ParsingLanguages = "fr"`

  - `const ParsingLanguagesGa ParsingLanguages = "ga"`

  - `const ParsingLanguagesHr ParsingLanguages = "hr"`

  - `const ParsingLanguagesHu ParsingLanguages = "hu"`

  - `const ParsingLanguagesID ParsingLanguages = "id"`

  - `const ParsingLanguagesIs ParsingLanguages = "is"`

  - `const ParsingLanguagesIt ParsingLanguages = "it"`

  - `const ParsingLanguagesKu ParsingLanguages = "ku"`

  - `const ParsingLanguagesLa ParsingLanguages = "la"`

  - `const ParsingLanguagesLt ParsingLanguages = "lt"`

  - `const ParsingLanguagesLv ParsingLanguages = "lv"`

  - `const ParsingLanguagesMi ParsingLanguages = "mi"`

  - `const ParsingLanguagesMs ParsingLanguages = "ms"`

  - `const ParsingLanguagesMt ParsingLanguages = "mt"`

  - `const ParsingLanguagesNl ParsingLanguages = "nl"`

  - `const ParsingLanguagesNo ParsingLanguages = "no"`

  - `const ParsingLanguagesOc ParsingLanguages = "oc"`

  - `const ParsingLanguagesPi ParsingLanguages = "pi"`

  - `const ParsingLanguagesPl ParsingLanguages = "pl"`

  - `const ParsingLanguagesPt ParsingLanguages = "pt"`

  - `const ParsingLanguagesRo ParsingLanguages = "ro"`

  - `const ParsingLanguagesRsLatin ParsingLanguages = "rs_latin"`

  - `const ParsingLanguagesSk ParsingLanguages = "sk"`

  - `const ParsingLanguagesSl ParsingLanguages = "sl"`

  - `const ParsingLanguagesSq ParsingLanguages = "sq"`

  - `const ParsingLanguagesSv ParsingLanguages = "sv"`

  - `const ParsingLanguagesSw ParsingLanguages = "sw"`

  - `const ParsingLanguagesTl ParsingLanguages = "tl"`

  - `const ParsingLanguagesTr ParsingLanguages = "tr"`

  - `const ParsingLanguagesUz ParsingLanguages = "uz"`

  - `const ParsingLanguagesVi ParsingLanguages = "vi"`

  - `const ParsingLanguagesAr ParsingLanguages = "ar"`

  - `const ParsingLanguagesFa ParsingLanguages = "fa"`

  - `const ParsingLanguagesUg ParsingLanguages = "ug"`

  - `const ParsingLanguagesUr ParsingLanguages = "ur"`

  - `const ParsingLanguagesBn ParsingLanguages = "bn"`

  - `const ParsingLanguagesAs ParsingLanguages = "as"`

  - `const ParsingLanguagesMni ParsingLanguages = "mni"`

  - `const ParsingLanguagesRu ParsingLanguages = "ru"`

  - `const ParsingLanguagesRsCyrillic ParsingLanguages = "rs_cyrillic"`

  - `const ParsingLanguagesBe ParsingLanguages = "be"`

  - `const ParsingLanguagesBg ParsingLanguages = "bg"`

  - `const ParsingLanguagesUk ParsingLanguages = "uk"`

  - `const ParsingLanguagesMn ParsingLanguages = "mn"`

  - `const ParsingLanguagesAbq ParsingLanguages = "abq"`

  - `const ParsingLanguagesAdy ParsingLanguages = "ady"`

  - `const ParsingLanguagesKbd ParsingLanguages = "kbd"`

  - `const ParsingLanguagesAva ParsingLanguages = "ava"`

  - `const ParsingLanguagesDar ParsingLanguages = "dar"`

  - `const ParsingLanguagesInh ParsingLanguages = "inh"`

  - `const ParsingLanguagesChe ParsingLanguages = "che"`

  - `const ParsingLanguagesLbe ParsingLanguages = "lbe"`

  - `const ParsingLanguagesLez ParsingLanguages = "lez"`

  - `const ParsingLanguagesTab ParsingLanguages = "tab"`

  - `const ParsingLanguagesTjk ParsingLanguages = "tjk"`

  - `const ParsingLanguagesHi ParsingLanguages = "hi"`

  - `const ParsingLanguagesMr ParsingLanguages = "mr"`

  - `const ParsingLanguagesNe ParsingLanguages = "ne"`

  - `const ParsingLanguagesBh ParsingLanguages = "bh"`

  - `const ParsingLanguagesMai ParsingLanguages = "mai"`

  - `const ParsingLanguagesAng ParsingLanguages = "ang"`

  - `const ParsingLanguagesBho ParsingLanguages = "bho"`

  - `const ParsingLanguagesMah ParsingLanguages = "mah"`

  - `const ParsingLanguagesSck ParsingLanguages = "sck"`

  - `const ParsingLanguagesNew ParsingLanguages = "new"`

  - `const ParsingLanguagesGom ParsingLanguages = "gom"`

  - `const ParsingLanguagesSa ParsingLanguages = "sa"`

  - `const ParsingLanguagesBgc ParsingLanguages = "bgc"`

  - `const ParsingLanguagesTh ParsingLanguages = "th"`

  - `const ParsingLanguagesChSim ParsingLanguages = "ch_sim"`

  - `const ParsingLanguagesChTra ParsingLanguages = "ch_tra"`

  - `const ParsingLanguagesJa ParsingLanguages = "ja"`

  - `const ParsingLanguagesKo ParsingLanguages = "ko"`

  - `const ParsingLanguagesTa ParsingLanguages = "ta"`

  - `const ParsingLanguagesTe ParsingLanguages = "te"`

  - `const ParsingLanguagesKn ParsingLanguages = "kn"`

### Parsing Mode

- `type ParsingMode string`

  Enum for representing the mode of parsing to be used.

  - `const ParsingModeParsePageWithoutLlm ParsingMode = "parse_page_without_llm"`

  - `const ParsingModeParsePageWithLlm ParsingMode = "parse_page_with_llm"`

  - `const ParsingModeParsePageWithLvm ParsingMode = "parse_page_with_lvm"`

  - `const ParsingModeParsePageWithAgent ParsingMode = "parse_page_with_agent"`

  - `const ParsingModeParsePageWithLayoutAgent ParsingMode = "parse_page_with_layout_agent"`

  - `const ParsingModeParseDocumentWithLlm ParsingMode = "parse_document_with_llm"`

  - `const ParsingModeParseDocumentWithLvm ParsingMode = "parse_document_with_lvm"`

  - `const ParsingModeParseDocumentWithAgent ParsingMode = "parse_document_with_agent"`

### Status Enum

- `type StatusEnum string`

  Enum for representing the status of a job

  - `const StatusEnumPending StatusEnum = "PENDING"`

  - `const StatusEnumSuccess StatusEnum = "SUCCESS"`

  - `const StatusEnumError StatusEnum = "ERROR"`

  - `const StatusEnumPartialSuccess StatusEnum = "PARTIAL_SUCCESS"`

  - `const StatusEnumCancelled StatusEnum = "CANCELLED"`

### Table Item

- `type TableItem struct{…}`

  - `Csv string`

    CSV representation of the table

  - `HTML string`

    HTML representation of the table

  - `Md string`

    Markdown representation preserving formatting

  - `Rows [][]TableItemRowUnion`

    Table data as array of arrays (string, number, or null)

    - `string`

    - `float64`

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `MergedFromPages []int64`

    List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

  - `MergedIntoPage int64`

    Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

  - `ParseConcerns []TableItemParseConcern`

    Quality concerns detected during table extraction, indicating the table may have issues

    - `Details string`

      Human-readable details about the concern

    - `Type string`

      Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

  - `Type TableItemType`

    Table item type

    - `const TableItemTypeTable TableItemType = "table"`

### Text Item

- `type TextItem struct{…}`

  - `Md string`

    Markdown representation preserving formatting

  - `Value string`

    Text content

  - `Bbox []BBox`

    List of bounding boxes

    - `H float64`

      Height of the bounding box

    - `W float64`

      Width of the bounding box

    - `X float64`

      X coordinate of the bounding box

    - `Y float64`

      Y coordinate of the bounding box

    - `Confidence float64`

      Confidence score

    - `EndIndex int64`

      End index in the text

    - `Label string`

      Label for the bounding box

    - `StartIndex int64`

      Start index in the text

  - `Type TextItemType`

    Text item type

    - `const TextItemTypeText TextItemType = "text"`
