## Get Configuration

`client.Configurations.Get(ctx, configID, query) (*ConfigurationResponse, error)`

**get** `/api/v1/beta/configurations/{config_id}`

Get a single product configuration by ID.

### Parameters

- `configID string`

- `query ConfigurationGetParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type ConfigurationResponse struct{…}`

  Response schema for a single product configuration.

  - `ID string`

    Unique configuration ID.

  - `Name string`

    Configuration name.

  - `Parameters ConfigurationResponseParametersUnion`

    Product-specific configuration parameters.

    - `type SplitV1ParametersResp struct{…}`

      Typed parameters for a *split v1* product configuration.

      - `Categories []SplitCategory`

        Categories to split documents into.

        - `Name string`

          Name of the category.

        - `Description string`

          Optional description of what content belongs in this category.

      - `ProductType SplitV1`

        Product type.

        - `const SplitV1SplitV1 SplitV1 = "split_v1"`

      - `SplittingStrategy SplitV1ParametersSplittingStrategyResp`

        Strategy for splitting documents.

        - `AllowUncategorized string`

          Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

          - `const SplitV1ParametersSplittingStrategyAllowUncategorizedInclude SplitV1ParametersSplittingStrategyAllowUncategorized = "include"`

          - `const SplitV1ParametersSplittingStrategyAllowUncategorizedForbid SplitV1ParametersSplittingStrategyAllowUncategorized = "forbid"`

          - `const SplitV1ParametersSplittingStrategyAllowUncategorizedOmit SplitV1ParametersSplittingStrategyAllowUncategorized = "omit"`

    - `type ExtractV2ParametersResp struct{…}`

      Typed parameters for an *extract v2* product configuration.

      - `DataSchema map[string, ExtractV2ParametersDataSchemaUnionResp]`

        JSON Schema defining the fields to extract. Validate with the /schema/validate endpoint first.

        - `type ExtractV2ParametersDataSchemaMap map[string, any]`

        - `type ExtractV2ParametersDataSchemaArray []any`

        - `string`

        - `float64`

        - `bool`

      - `ProductType ExtractV2`

        Product type.

        - `const ExtractV2ExtractV2 ExtractV2 = "extract_v2"`

      - `CiteSources bool`

        Include citations in results

      - `ConfidenceScores bool`

        Include confidence scores in results

      - `ExtractVersion string`

        Extract algorithm version. Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to pin to a specific release.

      - `ExtractionTarget ExtractV2ParametersExtractionTarget`

        Granularity of extraction: per_doc returns one object per document, per_page returns one object per page, per_table_row returns one object per table row

        - `const ExtractV2ParametersExtractionTargetPerDoc ExtractV2ParametersExtractionTarget = "per_doc"`

        - `const ExtractV2ParametersExtractionTargetPerPage ExtractV2ParametersExtractionTarget = "per_page"`

        - `const ExtractV2ParametersExtractionTargetPerTableRow ExtractV2ParametersExtractionTarget = "per_table_row"`

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

      - `Tier ExtractV2ParametersTier`

        Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)

        - `const ExtractV2ParametersTierCostEffective ExtractV2ParametersTier = "cost_effective"`

        - `const ExtractV2ParametersTierAgentic ExtractV2ParametersTier = "agentic"`

    - `type ClassifyV2ParametersResp struct{…}`

      Typed parameters for a *classify v2* product configuration.

      - `ProductType ClassifyV2`

        Product type.

        - `const ClassifyV2ClassifyV2 ClassifyV2 = "classify_v2"`

      - `Rules []ClassifyV2ParametersRuleResp`

        Classify rules to evaluate against the document (at least one required)

        - `Description string`

          Natural language criteria for matching this rule

        - `Type string`

          Document type to assign when rule matches

      - `Mode ClassifyV2ParametersMode`

        Classify execution mode

        - `const ClassifyV2ParametersModeFast ClassifyV2ParametersMode = "FAST"`

      - `ParsingConfiguration ClassifyV2ParametersParsingConfigurationResp`

        Parsing configuration for classify jobs.

        - `Lang string`

          ISO 639-1 language code for the document

        - `MaxPages int64`

          Maximum number of pages to process. Omit for no limit.

        - `TargetPages string`

          Comma-separated page numbers or ranges to process (1-based). Omit to process all pages.

    - `type ParseV2ParametersResp struct{…}`

      Configuration for LlamaParse v2 document parsing.

      Includes tier selection, processing options, output formatting,
      page targeting, and webhook delivery. Refer to the LlamaParse
      documentation for details on each field.

      - `ProductType ParseV2`

        Product type.

        - `const ParseV2ParseV2 ParseV2 = "parse_v2"`

      - `Tier ParseV2ParametersTier`

        Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced), 'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with highest accuracy)

        - `const ParseV2ParametersTierFast ParseV2ParametersTier = "fast"`

        - `const ParseV2ParametersTierCostEffective ParseV2ParametersTier = "cost_effective"`

        - `const ParseV2ParametersTierAgentic ParseV2ParametersTier = "agentic"`

        - `const ParseV2ParametersTierAgenticPlus ParseV2ParametersTier = "agentic_plus"`

      - `Version ParseV2ParametersVersion`

        Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

        - `type ParseV2ParametersVersion string`

          Tier version. Use 'latest' for the current stable version, or pin a dated version for reproducible results. See GET /api/v2/parse/versions for the per-tier list.

          - `const ParseV2ParametersVersionLatest ParseV2ParametersVersion = "latest"`

          - `const ParseV2ParametersVersion2026_05_13 ParseV2ParametersVersion = "2026-05-13"`

          - `const ParseV2ParametersVersion2026_05_11 ParseV2ParametersVersion = "2026-05-11"`

          - `const ParseV2ParametersVersion2026_04_09 ParseV2ParametersVersion = "2026-04-09"`

          - `const ParseV2ParametersVersion2025_12_11 ParseV2ParametersVersion = "2025-12-11"`

        - `string`

      - `AgenticOptions ParseV2ParametersAgenticOptionsResp`

        Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

        These options customize how the AI processes and interprets document content.
        Only applicable when using non-fast tiers.

        - `CustomPrompt string`

          Custom instructions for the AI parser. Use to guide extraction behavior, specify output formatting, or provide domain-specific context. Example: 'Extract financial tables with currency symbols. Format dates as YYYY-MM-DD.'

      - `ClientName string`

        Identifier for the client/application making the request. Used for analytics and debugging. Example: 'my-app-v2'

      - `CropBox ParseV2ParametersCropBoxResp`

        Crop boundaries to process only a portion of each page. Values are ratios 0-1 from page edges

        - `Bottom float64`

          Bottom boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content below this line is excluded

        - `Left float64`

          Left boundary as ratio (0-1). 0=left edge, 1=right edge. Content left of this line is excluded

        - `Right float64`

          Right boundary as ratio (0-1). 0=left edge, 1=right edge. Content right of this line is excluded

        - `Top float64`

          Top boundary as ratio (0-1). 0=top edge, 1=bottom edge. Content above this line is excluded

      - `DisableCache bool`

        Bypass result caching and force re-parsing. Use when document content may have changed or you need fresh results

      - `FastOptions any`

        Options for fast tier parsing (rule-based, no AI).

        Fast tier uses deterministic algorithms for text extraction without AI enhancement.
        It's the fastest and most cost-effective option, best suited for simple documents
        with standard layouts. Currently has no configurable options but reserved for
        future expansion.

      - `InputOptions ParseV2ParametersInputOptionsResp`

        Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on detected input file type

        - `HTML ParseV2ParametersInputOptionsHTMLResp`

          HTML/web page parsing options (applies to .html, .htm files)

          - `MakeAllElementsVisible bool`

            Force all HTML elements to be visible by overriding CSS display/visibility properties. Useful for parsing pages with hidden content or collapsed sections

          - `RemoveFixedElements bool`

            Remove fixed-position elements (headers, footers, floating buttons) that appear on every page render

          - `RemoveNavigationElements bool`

            Remove navigation elements (nav bars, sidebars, menus) to focus on main content

        - `Pdf any`

          PDF-specific parsing options (applies to .pdf files)

        - `Presentation ParseV2ParametersInputOptionsPresentationResp`

          Presentation parsing options (applies to .pptx, .ppt, .odp, .key files)

          - `OutOfBoundsContent bool`

            Extract content positioned outside the visible slide area. Some presentations have hidden notes or content that extends beyond slide boundaries

          - `SkipEmbeddedData bool`

            Skip extraction of embedded chart data tables. When true, only the visual representation of charts is captured, not the underlying data

        - `Spreadsheet ParseV2ParametersInputOptionsSpreadsheetResp`

          Spreadsheet parsing options (applies to .xlsx, .xls, .csv, .ods files)

          - `DetectSubTablesInSheets bool`

            Detect and extract multiple tables within a single sheet. Useful when spreadsheets contain several data regions separated by blank rows/columns

          - `ForceFormulaComputationInSheets bool`

            Compute formula results instead of extracting formula text. Use when you need calculated values rather than formula definitions

          - `IncludeHiddenSheets bool`

            Parse hidden sheets in addition to visible ones. By default, hidden sheets are skipped

      - `OutputOptions ParseV2ParametersOutputOptionsResp`

        Output formatting options for markdown, text, and extracted images

        - `AdditionalOutputs []string`

          Optional additional output artifacts to save alongside the primary parse output. Each value opts in to generating and persisting one extra file; the empty list (default) saves none. The three accepted values are: 'stripped_md' — per-page markdown stripped of formatting (links, bold/italic, images, HTML), saved as JSON for full-text-search indexing; fetch via `expand=stripped_markdown_content_metadata`. 'concatenated_stripped_txt' — all stripped pages concatenated into a single plain-text file with `\n\n---\n\n` between pages, useful for feeding the document into search or embedding pipelines as one blob; fetch via `expand=concatenated_stripped_markdown_content_metadata`. 'word_bbox' — raw word-level bounding boxes (one JSON object per word, with page number and x/y/w/h coordinates) saved as JSONL, useful for highlighting or grounding extracted answers back to the source document; fetch via `expand=raw_words_content_metadata`.

        - `ExtractPrintedPageNumber bool`

          Extract the printed page number as it appears in the document (e.g., 'Page 5 of 10', 'v', 'A-3'). Useful for referencing original page numbers

        - `ImagesToSave []string`

          Image categories to extract and save. Options: 'screenshot' (full page renders useful for visual QA), 'embedded' (images found within the document), 'layout' (cropped regions from layout detection like figures and diagrams). Empty list saves no images

          - `const ParseV2ParametersOutputOptionsImagesToSaveScreenshot ParseV2ParametersOutputOptionsImagesToSave = "screenshot"`

          - `const ParseV2ParametersOutputOptionsImagesToSaveEmbedded ParseV2ParametersOutputOptionsImagesToSave = "embedded"`

          - `const ParseV2ParametersOutputOptionsImagesToSaveLayout ParseV2ParametersOutputOptionsImagesToSave = "layout"`

        - `Markdown ParseV2ParametersOutputOptionsMarkdownResp`

          Markdown formatting options including table styles and link annotations

          - `AnnotateLinks bool`

            Add link annotations to markdown output in the format [text](url). When false, only the link text is included

          - `InlineImages bool`

            Embed images directly in markdown as base64 data URIs instead of extracting them as separate files. Useful for self-contained markdown output

          - `Tables ParseV2ParametersOutputOptionsMarkdownTablesResp`

            Table formatting options including markdown vs HTML format and merging behavior

            - `CompactMarkdownTables bool`

              Remove extra whitespace padding in markdown table cells for more compact output

            - `MarkdownTableMultilineSeparator string`

              Separator string for multiline cell content in markdown tables. Example: '<br>' to preserve line breaks, ' ' to join with spaces

            - `MergeContinuedTables bool`

              Automatically merge tables that span multiple pages into a single table. The merged table appears on the first page with merged_from_pages metadata

            - `OutputTablesAsMarkdown bool`

              Output tables as markdown pipe tables instead of HTML <table> tags. Markdown tables are simpler but cannot represent complex structures like merged cells

        - `SpatialText ParseV2ParametersOutputOptionsSpatialTextResp`

          Spatial text output options for preserving document layout structure

          - `DoNotUnrollColumns bool`

            Keep multi-column layouts intact instead of linearizing columns into sequential text. Automatically enabled for non-fast tiers

          - `PreserveLayoutAlignmentAcrossPages bool`

            Maintain consistent text column alignment across page boundaries. Automatically enabled for document-level parsing modes

          - `PreserveVerySmallText bool`

            Include text below the normal size threshold. Useful for footnotes, watermarks, or fine print that might otherwise be filtered out

        - `TablesAsSpreadsheet ParseV2ParametersOutputOptionsTablesAsSpreadsheetResp`

          Options for exporting tables as XLSX spreadsheets

          - `Enable bool`

            Whether this option is enabled

          - `GuessSheetName bool`

            Automatically generate descriptive sheet names from table context (headers, surrounding text) instead of using generic names like 'Table_1'

      - `PageRanges ParseV2ParametersPageRangesResp`

        Page selection: limit total pages or specify exact pages to process

        - `MaxPages int64`

          Maximum number of pages to process. Pages are processed in order starting from page 1. If both max_pages and target_pages are set, target_pages takes precedence

        - `TargetPages string`

          Comma-separated list of specific pages to process using 1-based indexing. Supports individual pages and ranges. Examples: '1,3,5' (pages 1, 3, 5), '1-5' (pages 1 through 5 inclusive), '1,3,5-8,10' (pages 1, 3, 5-8, and 10). Pages are sorted and deduplicated automatically. Duplicate pages cause an error

      - `ProcessingControl ParseV2ParametersProcessingControlResp`

        Job execution controls including timeouts and failure thresholds

        - `JobFailureConditions ParseV2ParametersProcessingControlJobFailureConditionsResp`

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

        - `Timeouts ParseV2ParametersProcessingControlTimeoutsResp`

          Timeout settings for job execution. Increase for large or complex documents

          - `BaseInSeconds int64`

            Base timeout for the job in seconds (max 1800 = 30 minutes). This is the minimum time allowed regardless of document size

          - `ExtraTimePerPageInSeconds int64`

            Additional timeout per page in seconds (max 300 = 5 minutes). Total timeout = base + (this value × page count)

      - `ProcessingOptions ParseV2ParametersProcessingOptionsResp`

        Document processing options including OCR, table extraction, and chart parsing

        - `AggressiveTableExtraction bool`

          Use aggressive heuristics to detect table boundaries, even without visible borders. Useful for documents with borderless or complex tables

        - `AutoModeConfiguration []ParseV2ParametersProcessingOptionsAutoModeConfigurationResp`

          Conditional processing rules that apply different parsing options based on page content, document structure, or filename patterns. Each entry defines trigger conditions and the parsing configuration to apply when triggered

          - `ParsingConf ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfResp`

            Parsing configuration to apply when trigger conditions are met

            - `AdaptiveLongTable bool`

              Whether to use adaptive long table handling

            - `AggressiveTableExtraction bool`

              Whether to use aggressive table extraction

            - `CropBox ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfCropBoxResp`

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

            - `Ignore ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfIgnoreResp`

              Ignore options for auto mode parsing configuration.

              - `IgnoreDiagonalText bool`

                Whether to ignore diagonal text in the document

              - `IgnoreHiddenText bool`

                Whether to ignore hidden text in the document

            - `Language string`

              Primary language of the document

            - `OutlinedTableExtraction bool`

              Whether to use outlined table extraction

            - `Presentation ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfPresentationResp`

              Presentation-specific options for auto mode parsing configuration.

              - `OutOfBoundsContent bool`

                Extract out of bounds content in presentation slides

              - `SkipEmbeddedData bool`

                Skip extraction of embedded data for charts in presentation slides

            - `SpatialText ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfSpatialTextResp`

              Spatial text options for auto mode parsing configuration.

              - `DoNotUnrollColumns bool`

                Keep column structure intact without unrolling

              - `PreserveLayoutAlignmentAcrossPages bool`

                Preserve text alignment across page boundaries

              - `PreserveVerySmallText bool`

                Include very small text in spatial output

            - `SpecializedChartParsing string`

              Enable specialized chart parsing with the specified mode

              - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsingAgenticPlus ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsing = "agentic_plus"`

              - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsingAgentic ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsing = "agentic"`

              - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsingEfficient ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfSpecializedChartParsing = "efficient"`

            - `Tier string`

              Override the parsing tier for matched pages. Must be paired with version

              - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfTierFast ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfTier = "fast"`

              - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfTierCostEffective ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfTier = "cost_effective"`

              - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfTierAgentic ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfTier = "agentic"`

              - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfTierAgenticPlus ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfTier = "agentic_plus"`

            - `Version string`

              Tier version when overriding tier. Required when tier is specified

              - `string`

                - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersionLatest ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion = "latest"`

                - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion2026_05_13 ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion = "2026-05-13"`

                - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion2026_05_11 ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion = "2026-05-11"`

                - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion2026_04_09 ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion = "2026-04-09"`

                - `const ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion2025_12_11 ParseV2ParametersProcessingOptionsAutoModeConfigurationParsingConfVersion = "2025-12-11"`

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

          - `FullPageImageInPageThreshold ParseV2ParametersProcessingOptionsAutoModeConfigurationFullPageImageInPageThresholdUnionResp`

            Threshold for full page image detection (0.0-1.0, default 0.8)

            - `float64`

            - `string`

          - `ImageInPage bool`

            Trigger if page contains non-screenshot images

          - `LayoutElementInPage string`

            Trigger if page contains this layout element type

          - `LayoutElementInPageConfidenceThreshold ParseV2ParametersProcessingOptionsAutoModeConfigurationLayoutElementInPageConfidenceThresholdUnionResp`

            Confidence threshold for layout element detection

            - `float64`

            - `string`

          - `PageContainsAtLeastNCharts ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNChartsUnionResp`

            Trigger if page has more than N charts

            - `int64`

            - `string`

          - `PageContainsAtLeastNImages ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNImagesUnionResp`

            Trigger if page has more than N images

            - `int64`

            - `string`

          - `PageContainsAtLeastNLayoutElements ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNLayoutElementsUnionResp`

            Trigger if page has more than N layout elements

            - `int64`

            - `string`

          - `PageContainsAtLeastNLines ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNLinesUnionResp`

            Trigger if page has more than N lines

            - `int64`

            - `string`

          - `PageContainsAtLeastNLinks ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNLinksUnionResp`

            Trigger if page has more than N links

            - `int64`

            - `string`

          - `PageContainsAtLeastNNumbers ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNNumbersUnionResp`

            Trigger if page has more than N numeric words

            - `int64`

            - `string`

          - `PageContainsAtLeastNPercentNumbers ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNPercentNumbersUnionResp`

            Trigger if page has more than N% numeric words

            - `int64`

            - `string`

          - `PageContainsAtLeastNTables ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNTablesUnionResp`

            Trigger if page has more than N tables

            - `int64`

            - `string`

          - `PageContainsAtLeastNWords ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtLeastNWordsUnionResp`

            Trigger if page has more than N words

            - `int64`

            - `string`

          - `PageContainsAtMostNCharts ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNChartsUnionResp`

            Trigger if page has fewer than N charts

            - `int64`

            - `string`

          - `PageContainsAtMostNImages ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNImagesUnionResp`

            Trigger if page has fewer than N images

            - `int64`

            - `string`

          - `PageContainsAtMostNLayoutElements ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNLayoutElementsUnionResp`

            Trigger if page has fewer than N layout elements

            - `int64`

            - `string`

          - `PageContainsAtMostNLines ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNLinesUnionResp`

            Trigger if page has fewer than N lines

            - `int64`

            - `string`

          - `PageContainsAtMostNLinks ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNLinksUnionResp`

            Trigger if page has fewer than N links

            - `int64`

            - `string`

          - `PageContainsAtMostNNumbers ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNNumbersUnionResp`

            Trigger if page has fewer than N numeric words

            - `int64`

            - `string`

          - `PageContainsAtMostNPercentNumbers ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNPercentNumbersUnionResp`

            Trigger if page has fewer than N% numeric words

            - `int64`

            - `string`

          - `PageContainsAtMostNTables ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNTablesUnionResp`

            Trigger if page has fewer than N tables

            - `int64`

            - `string`

          - `PageContainsAtMostNWords ParseV2ParametersProcessingOptionsAutoModeConfigurationPageContainsAtMostNWordsUnionResp`

            Trigger if page has fewer than N words

            - `int64`

            - `string`

          - `PageLongerThanNChars ParseV2ParametersProcessingOptionsAutoModeConfigurationPageLongerThanNCharsUnionResp`

            Trigger if page has more than N characters

            - `int64`

            - `string`

          - `PageMdError bool`

            Trigger on pages with markdown extraction errors

          - `PageShorterThanNChars ParseV2ParametersProcessingOptionsAutoModeConfigurationPageShorterThanNCharsUnionResp`

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

        - `CostOptimizer ParseV2ParametersProcessingOptionsCostOptimizerResp`

          Cost optimizer configuration for reducing parsing costs on simpler pages.

          When enabled, the parser analyzes each page and routes simpler pages to faster,
          cheaper processing while preserving quality for complex pages. Only works with
          'agentic' or 'agentic_plus' tiers.

          - `Enable bool`

            Enable cost-optimized parsing. Routes simpler pages to faster processing while complex pages use full AI analysis. May reduce speed on some documents. IMPORTANT: Only available with 'agentic' or 'agentic_plus' tiers

        - `DisableHeuristics bool`

          Disable automatic heuristics including outlined table extraction and adaptive long table handling. Use when heuristics produce incorrect results

        - `Ignore ParseV2ParametersProcessingOptionsIgnoreResp`

          Options for ignoring specific text types (diagonal, hidden, text in images)

          - `IgnoreDiagonalText bool`

            Skip text rotated at an angle (not horizontal/vertical). Useful for ignoring watermarks or decorative angled text

          - `IgnoreHiddenText bool`

            Skip text marked as hidden in the document structure. Some PDFs contain invisible text layers used for accessibility or search indexing

          - `IgnoreTextInImage bool`

            Skip OCR text extraction from embedded images. Use when images contain irrelevant text (watermarks, logos) that shouldn't be in the output

        - `OcrParameters ParseV2ParametersProcessingOptionsOcrParametersResp`

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

          - `const ParseV2ParametersProcessingOptionsSpecializedChartParsingAgenticPlus ParseV2ParametersProcessingOptionsSpecializedChartParsing = "agentic_plus"`

          - `const ParseV2ParametersProcessingOptionsSpecializedChartParsingAgentic ParseV2ParametersProcessingOptionsSpecializedChartParsing = "agentic"`

          - `const ParseV2ParametersProcessingOptionsSpecializedChartParsingEfficient ParseV2ParametersProcessingOptionsSpecializedChartParsing = "efficient"`

      - `WebhookConfigurations []ParseV2ParametersWebhookConfigurationResp`

        Webhook endpoints for job status notifications. Multiple webhooks can be configured for different events or services

        - `WebhookEvents []string`

          Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

        - `WebhookHeaders map[string, any]`

          Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

        - `WebhookURL string`

          HTTPS URL to receive webhook POST requests. Must be publicly accessible

    - `type ConfigurationResponseParametersSpreadsheetV1 struct{…}`

      Typed parameters for a *spreadsheet v1* product configuration.

      - `ProductType SpreadsheetV1`

        Product type.

        - `const SpreadsheetV1SpreadsheetV1 SpreadsheetV1 = "spreadsheet_v1"`

      - `ExtractionRange string`

        A1 notation of the range to extract a single region from. If None, the entire sheet is used.

      - `FlattenHierarchicalTables bool`

        Return a flattened dataframe when a detected table is recognized as hierarchical.

      - `GenerateAdditionalMetadata bool`

        Whether to generate additional metadata (title, description) for each extracted region.

      - `IncludeHiddenCells bool`

        Whether to include hidden cells when extracting regions from the spreadsheet.

      - `SheetNames []string`

        The names of the sheets to extract regions from. If empty, all sheets will be processed.

      - `Specialization string`

        Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

      - `TableMergeSensitivity string`

        Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

        - `const ConfigurationResponseParametersSpreadsheetV1TableMergeSensitivityStrong ConfigurationResponseParametersSpreadsheetV1TableMergeSensitivity = "strong"`

        - `const ConfigurationResponseParametersSpreadsheetV1TableMergeSensitivityWeak ConfigurationResponseParametersSpreadsheetV1TableMergeSensitivity = "weak"`

      - `UseExperimentalProcessing bool`

        Enables experimental processing. Accuracy may be impacted.

    - `type UntypedParametersResp struct{…}`

      Catch-all for configurations without a dedicated typed schema.

      Accepts arbitrary JSON fields alongside `product_type`.

      - `ProductType Unknown`

        Product type.

        - `const UnknownUnknown Unknown = "unknown"`

  - `ProductType ConfigurationResponseProductType`

    Product type.

    - `const ConfigurationResponseProductTypeSplitV1 ConfigurationResponseProductType = "split_v1"`

    - `const ConfigurationResponseProductTypeExtractV2 ConfigurationResponseProductType = "extract_v2"`

    - `const ConfigurationResponseProductTypeClassifyV2 ConfigurationResponseProductType = "classify_v2"`

    - `const ConfigurationResponseProductTypeParseV2 ConfigurationResponseProductType = "parse_v2"`

    - `const ConfigurationResponseProductTypeSpreadsheetV1 ConfigurationResponseProductType = "spreadsheet_v1"`

    - `const ConfigurationResponseProductTypeUnknown ConfigurationResponseProductType = "unknown"`

  - `Version string`

    Version identifier (datetime string).

  - `CreatedAt Time`

    Creation timestamp.

  - `UpdatedAt Time`

    Last update timestamp.

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
  configurationResponse, err := client.Configurations.Get(
    context.TODO(),
    "config_id",
    llamacloudprod.ConfigurationGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", configurationResponse.ID)
}
```

#### Response

```json
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
```
