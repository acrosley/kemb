# Batch

## Create Batch Job

`client.Beta.Batch.New(ctx, params) (*BetaBatchNewResponse, error)`

**post** `/api/v1/beta/batch-processing`

Create a batch processing job.

Processes files from a directory or a specific list of item IDs.
Supports batch parsing and classification operations.

Provide either `directory_id` to process all files in a directory,
or `item_ids` for specific items. The job runs asynchronously —
poll `GET /batch/{job_id}` for progress.

### Parameters

- `params BetaBatchNewParams`

  - `JobConfig param.Field[BetaBatchNewParamsJobConfigUnion]`

    Body param: Job configuration — either a parse or classify config

    - `type BetaBatchNewParamsJobConfigBatchParseJobRecordCreate struct{…}`

      Batch-specific parse job record for batch processing.

      This model contains the metadata and configuration for a batch parse job,
      but excludes file-specific information. It's used as input to the batch
      parent workflow and combined with DirectoryFile data to create full
      ParseJobRecordCreate instances for each file.

      Attributes:
      job_name: Must be PARSE_RAW_FILE
      partitions: Partitions for job output location
      parameters: Generic parse configuration (BatchParseJobConfig)
      session_id: Upstream request ID for tracking
      correlation_id: Correlation ID for cross-service tracking
      parent_job_execution_id: Parent job execution ID if nested
      user_id: User who created the job
      project_id: Project this job belongs to
      webhook_url: Optional webhook URL for job completion notifications

      - `CorrelationID string`

        The correlation ID for this job. Used for tracking the job across services.

      - `JobName string`

        - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateJobNameParseRawFileJob BetaBatchNewParamsJobConfigBatchParseJobRecordCreateJobName = "parse_raw_file_job"`

      - `Parameters BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParameters`

        Generic parse job configuration for batch processing.

        This model contains the parsing configuration that applies to all files
        in a batch, but excludes file-specific fields like file_name, file_id, etc.
        Those file-specific fields are populated from DirectoryFile data when
        creating individual ParseJobRecordCreate instances for each file.

        The fields in this model should be generic settings that apply uniformly
        to all files being processed in the batch.

        - `AdaptiveLongTable bool`

        - `AggressiveTableExtraction bool`

        - `AnnotateLinks bool`

        - `AutoMode bool`

        - `AutoModeConfigurationJson string`

        - `AutoModeTriggerOnImageInPage bool`

        - `AutoModeTriggerOnRegexpInPage string`

        - `AutoModeTriggerOnTableInPage bool`

        - `AutoModeTriggerOnTextInPage string`

        - `AzureOpenAIAPIVersion string`

        - `AzureOpenAIDeploymentName string`

        - `AzureOpenAIEndpoint string`

        - `AzureOpenAIKey string`

        - `BboxBottom float64`

        - `BboxLeft float64`

        - `BboxRight float64`

        - `BboxTop float64`

        - `BoundingBox string`

        - `CompactMarkdownTable bool`

        - `ComplementalFormattingInstruction string`

        - `ContentGuidelineInstruction string`

        - `ContinuousMode bool`

        - `CustomMetadata map[string, any]`

          The custom metadata to attach to the documents.

        - `DisableImageExtraction bool`

        - `DisableOcr bool`

        - `DisableReconstruction bool`

        - `DoNotCache bool`

        - `DoNotUnrollColumns bool`

        - `EnableCostOptimizer bool`

        - `ExtractCharts bool`

        - `ExtractLayout bool`

        - `ExtractPrintedPageNumber bool`

        - `FastMode bool`

        - `FormattingInstruction string`

        - `Gpt4oAPIKey string`

        - `Gpt4oMode bool`

        - `GuessXlsxSheetName bool`

        - `HideFooters bool`

        - `HideHeaders bool`

        - `HighResOcr bool`

        - `HTMLMakeAllElementsVisible bool`

        - `HTMLRemoveFixedElements bool`

        - `HTMLRemoveNavigationElements bool`

        - `HTTPProxy string`

        - `IgnoreDocumentElementsForLayoutDetection bool`

        - `ImagesToSave []string`

          - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersImagesToSaveScreenshot BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersImagesToSave = "screenshot"`

          - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersImagesToSaveEmbedded BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersImagesToSave = "embedded"`

          - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersImagesToSaveLayout BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersImagesToSave = "layout"`

        - `InlineImagesInMarkdown bool`

        - `InputS3Path string`

        - `InputS3Region string`

          The region for the input S3 bucket.

        - `InputURL string`

        - `InternalIsScreenshotJob bool`

        - `InvalidateCache bool`

        - `IsFormattingInstruction bool`

        - `JobTimeoutExtraTimePerPageInSeconds float64`

        - `JobTimeoutInSeconds float64`

        - `KeepPageSeparatorWhenMergingTables bool`

        - `Lang string`

          The language.

        - `Languages []ParsingLanguages`

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

        - `LayoutAware bool`

        - `LineLevelBoundingBox bool`

        - `MarkdownTableMultilineHeaderSeparator string`

        - `MaxPages int64`

        - `MaxPagesEnforced int64`

        - `MergeTablesAcrossPagesInMarkdown bool`

        - `Model string`

        - `OutlinedTableExtraction bool`

        - `OutputPdfOfDocument bool`

        - `OutputS3PathPrefix string`

          If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

        - `OutputS3Region string`

          The region for the output S3 bucket.

        - `OutputTablesAsHTML bool`

        - `OutputBucket string`

          The output bucket.

        - `PageErrorTolerance float64`

        - `PageFooterPrefix string`

        - `PageFooterSuffix string`

        - `PageHeaderPrefix string`

        - `PageHeaderSuffix string`

        - `PagePrefix string`

        - `PageSeparator string`

        - `PageSuffix string`

        - `ParseMode ParsingMode`

          Enum for representing the mode of parsing to be used.

          - `const ParsingModeParsePageWithoutLlm ParsingMode = "parse_page_without_llm"`

          - `const ParsingModeParsePageWithLlm ParsingMode = "parse_page_with_llm"`

          - `const ParsingModeParsePageWithLvm ParsingMode = "parse_page_with_lvm"`

          - `const ParsingModeParsePageWithAgent ParsingMode = "parse_page_with_agent"`

          - `const ParsingModeParsePageWithLayoutAgent ParsingMode = "parse_page_with_layout_agent"`

          - `const ParsingModeParseDocumentWithLlm ParsingMode = "parse_document_with_llm"`

          - `const ParsingModeParseDocumentWithLvm ParsingMode = "parse_document_with_lvm"`

          - `const ParsingModeParseDocumentWithAgent ParsingMode = "parse_document_with_agent"`

        - `ParsingInstruction string`

        - `PipelineID string`

          The pipeline ID.

        - `PreciseBoundingBox bool`

        - `PremiumMode bool`

        - `PresentationOutOfBoundsContent bool`

        - `PresentationSkipEmbeddedData bool`

        - `PreserveLayoutAlignmentAcrossPages bool`

        - `PreserveVerySmallText bool`

        - `Preset string`

        - `Priority string`

          The priority for the request. This field may be ignored or overwritten depending on the organization tier.

          - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersPriorityLow BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersPriority = "low"`

          - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersPriorityMedium BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersPriority = "medium"`

          - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersPriorityHigh BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersPriority = "high"`

          - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersPriorityCritical BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersPriority = "critical"`

        - `ProjectID string`

        - `RemoveHiddenText bool`

        - `ReplaceFailedPageMode FailPageMode`

          Enum for representing the different available page error handling modes.

          - `const FailPageModeRawText FailPageMode = "raw_text"`

          - `const FailPageModeBlankPage FailPageMode = "blank_page"`

          - `const FailPageModeErrorMessage FailPageMode = "error_message"`

        - `ReplaceFailedPageWithErrorMessagePrefix string`

        - `ReplaceFailedPageWithErrorMessageSuffix string`

        - `ResourceInfo map[string, any]`

          The resource info about the file

        - `SaveImages bool`

        - `SkipDiagonalText bool`

        - `SpecializedChartParsingAgentic bool`

        - `SpecializedChartParsingEfficient bool`

        - `SpecializedChartParsingPlus bool`

        - `SpecializedImageParsing bool`

        - `SpreadsheetExtractSubTables bool`

        - `SpreadsheetForceFormulaComputation bool`

        - `SpreadsheetIncludeHiddenSheets bool`

        - `StrictModeBuggyFont bool`

        - `StrictModeImageExtraction bool`

        - `StrictModeImageOcr bool`

        - `StrictModeReconstruction bool`

        - `StructuredOutput bool`

        - `StructuredOutputJsonSchema string`

        - `StructuredOutputJsonSchemaName string`

        - `SystemPrompt string`

        - `SystemPromptAppend string`

        - `TakeScreenshot bool`

        - `TargetPages string`

        - `Tier string`

        - `Type string`

          - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersTypeParse BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersType = "parse"`

        - `UseVendorMultimodalModel bool`

        - `UserPrompt string`

        - `VendorMultimodalAPIKey string`

        - `VendorMultimodalModelName string`

        - `Version string`

        - `WebhookConfigurations []BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfiguration`

          Outbound webhook endpoints to notify on job status changes

          - `WebhookEvents []string`

            Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractPending BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.pending"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractSuccess BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.success"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractError BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.error"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractPartialSuccess BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.partial_success"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractCancelled BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.cancelled"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParsePending BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.pending"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParseRunning BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.running"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParseSuccess BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.success"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParseError BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.error"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParsePartialSuccess BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.partial_success"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParseCancelled BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.cancelled"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifyPending BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.pending"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifySuccess BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.success"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifyError BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.error"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifyPartialSuccess BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.partial_success"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifyCancelled BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.cancelled"`

            - `const BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventUnmappedEvent BetaBatchNewParamsJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "unmapped_event"`

          - `WebhookHeaders map[string, string]`

            Custom HTTP headers sent with each webhook request (e.g. auth tokens)

          - `WebhookOutputFormat string`

            Response format sent to the webhook: 'string' (default) or 'json'

          - `WebhookURL string`

            URL to receive webhook POST notifications

        - `WebhookURL string`

      - `ParentJobExecutionID string`

        The ID of the parent job execution.

      - `Partitions map[string, string]`

        The partitions for this execution. Used for determining where to save job output.

      - `ProjectID string`

        The ID of the project this job belongs to.

      - `SessionID string`

        The upstream request ID that created this job. Used for tracking the job across services.

      - `UserID string`

        The ID of the user that created this job

      - `WebhookURL string`

        The URL that needs to be called at the end of the parsing job.

    - `type ClassifyJob struct{…}`

      A classify job.

      - `ID string`

        Unique identifier

      - `ProjectID string`

        The ID of the project

      - `Rules []ClassifierRule`

        The rules to classify the files

        - `Description string`

          Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

        - `Type string`

          The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

      - `Status StatusEnum`

        The status of the classify job

        - `const StatusEnumPending StatusEnum = "PENDING"`

        - `const StatusEnumSuccess StatusEnum = "SUCCESS"`

        - `const StatusEnumError StatusEnum = "ERROR"`

        - `const StatusEnumPartialSuccess StatusEnum = "PARTIAL_SUCCESS"`

        - `const StatusEnumCancelled StatusEnum = "CANCELLED"`

      - `UserID string`

        The ID of the user

      - `CreatedAt Time`

        Creation datetime

      - `EffectiveAt Time`

      - `ErrorMessage string`

        Error message for the latest job attempt, if any.

      - `JobRecordID string`

        The job record ID associated with this status, if any.

      - `Mode ClassifyJobMode`

        The classification mode to use

        - `const ClassifyJobModeFast ClassifyJobMode = "FAST"`

        - `const ClassifyJobModeMultimodal ClassifyJobMode = "MULTIMODAL"`

      - `ParsingConfiguration ClassifyParsingConfiguration`

        The configuration for the parsing job

        - `Lang ParsingLanguages`

          The language to parse the files in

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

        - `MaxPages int64`

          The maximum number of pages to parse

        - `TargetPages []int64`

          The pages to target for parsing (0-indexed, so first page is at 0)

      - `UpdatedAt Time`

        Update datetime

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `ContinueAsNewThreshold param.Field[int64]`

    Body param: Maximum files to process per execution cycle in directory mode. Defaults to page_size.

  - `DirectoryID param.Field[string]`

    Body param: ID of the directory containing files to process

  - `ItemIDs param.Field[[]string]`

    Body param: List of specific item IDs to process. Either this or directory_id must be provided.

  - `PageSize param.Field[int64]`

    Body param: Number of files to process per batch when using directory mode

  - `TemporalNamespace param.Field[string]`

    Header param

### Returns

- `type BetaBatchNewResponse struct{…}`

  Response schema for a batch processing job.

  - `ID string`

    Unique identifier for the batch job

  - `JobType BetaBatchNewResponseJobType`

    Type of processing operation (parse or classify)

    - `const BetaBatchNewResponseJobTypeParse BetaBatchNewResponseJobType = "parse"`

    - `const BetaBatchNewResponseJobTypeExtract BetaBatchNewResponseJobType = "extract"`

    - `const BetaBatchNewResponseJobTypeClassify BetaBatchNewResponseJobType = "classify"`

  - `ProjectID string`

    Project this job belongs to

  - `Status BetaBatchNewResponseStatus`

    Current job status

    - `const BetaBatchNewResponseStatusPending BetaBatchNewResponseStatus = "pending"`

    - `const BetaBatchNewResponseStatusRunning BetaBatchNewResponseStatus = "running"`

    - `const BetaBatchNewResponseStatusDispatched BetaBatchNewResponseStatus = "dispatched"`

    - `const BetaBatchNewResponseStatusCompleted BetaBatchNewResponseStatus = "completed"`

    - `const BetaBatchNewResponseStatusFailed BetaBatchNewResponseStatus = "failed"`

    - `const BetaBatchNewResponseStatusCancelled BetaBatchNewResponseStatus = "cancelled"`

  - `TotalItems int64`

    Total number of items in the job

  - `CompletedAt Time`

    Timestamp when job completed

  - `CreatedAt Time`

    Creation datetime

  - `DirectoryID string`

    Directory being processed

  - `EffectiveAt Time`

  - `ErrorMessage string`

    Error message for the latest job attempt, if any.

  - `FailedItems int64`

    Number of items that failed processing

  - `JobRecordID string`

    The job record ID associated with this status, if any.

  - `ProcessedItems int64`

    Number of items processed so far

  - `SkippedItems int64`

    Number of items skipped (already processed or size limit)

  - `StartedAt Time`

    Timestamp when job processing started

  - `UpdatedAt Time`

    Update datetime

  - `WorkflowID string`

    Async job tracking ID

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
  batch, err := client.Beta.Batch.New(context.TODO(), llamacloudprod.BetaBatchNewParams{
    JobConfig: llamacloudprod.BetaBatchNewParamsJobConfigUnion{
      OfBatchParseJobRecordCreate: &llamacloudprod.BetaBatchNewParamsJobConfigBatchParseJobRecordCreate{

      },
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", batch.ID)
}
```

#### Response

```json
{
  "id": "bjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "job_type": "parse",
  "project_id": "proj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "status": "pending",
  "total_items": 0,
  "completed_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error_message": "error_message",
  "failed_items": 0,
  "job_record_id": "job_record_id",
  "processed_items": 0,
  "skipped_items": 0,
  "started_at": "2019-12-27T18:11:19.117Z",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "workflow_id": "workflow_id"
}
```

## List Batch Jobs

`client.Beta.Batch.List(ctx, query) (*PaginatedBatchItems[BetaBatchListResponse], error)`

**get** `/api/v1/beta/batch-processing`

List batch processing jobs with optional filtering.

Filter by `directory_id`, `job_type`, or `status`. Results
are paginated with configurable `limit` and `offset`.

### Parameters

- `query BetaBatchListParams`

  - `DirectoryID param.Field[string]`

    Filter by directory ID

  - `JobType param.Field[BetaBatchListParamsJobType]`

    Filter by job type (PARSE, EXTRACT, CLASSIFY)

    - `const BetaBatchListParamsJobTypeParse BetaBatchListParamsJobType = "parse"`

    - `const BetaBatchListParamsJobTypeExtract BetaBatchListParamsJobType = "extract"`

    - `const BetaBatchListParamsJobTypeClassify BetaBatchListParamsJobType = "classify"`

  - `Limit param.Field[int64]`

    Maximum number of jobs to return

  - `Offset param.Field[int64]`

    Number of jobs to skip for pagination

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

  - `Status param.Field[BetaBatchListParamsStatus]`

    Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

    - `const BetaBatchListParamsStatusPending BetaBatchListParamsStatus = "pending"`

    - `const BetaBatchListParamsStatusRunning BetaBatchListParamsStatus = "running"`

    - `const BetaBatchListParamsStatusDispatched BetaBatchListParamsStatus = "dispatched"`

    - `const BetaBatchListParamsStatusCompleted BetaBatchListParamsStatus = "completed"`

    - `const BetaBatchListParamsStatusFailed BetaBatchListParamsStatus = "failed"`

    - `const BetaBatchListParamsStatusCancelled BetaBatchListParamsStatus = "cancelled"`

### Returns

- `type BetaBatchListResponse struct{…}`

  Response schema for a batch processing job.

  - `ID string`

    Unique identifier for the batch job

  - `JobType BetaBatchListResponseJobType`

    Type of processing operation (parse or classify)

    - `const BetaBatchListResponseJobTypeParse BetaBatchListResponseJobType = "parse"`

    - `const BetaBatchListResponseJobTypeExtract BetaBatchListResponseJobType = "extract"`

    - `const BetaBatchListResponseJobTypeClassify BetaBatchListResponseJobType = "classify"`

  - `ProjectID string`

    Project this job belongs to

  - `Status BetaBatchListResponseStatus`

    Current job status

    - `const BetaBatchListResponseStatusPending BetaBatchListResponseStatus = "pending"`

    - `const BetaBatchListResponseStatusRunning BetaBatchListResponseStatus = "running"`

    - `const BetaBatchListResponseStatusDispatched BetaBatchListResponseStatus = "dispatched"`

    - `const BetaBatchListResponseStatusCompleted BetaBatchListResponseStatus = "completed"`

    - `const BetaBatchListResponseStatusFailed BetaBatchListResponseStatus = "failed"`

    - `const BetaBatchListResponseStatusCancelled BetaBatchListResponseStatus = "cancelled"`

  - `TotalItems int64`

    Total number of items in the job

  - `CompletedAt Time`

    Timestamp when job completed

  - `CreatedAt Time`

    Creation datetime

  - `DirectoryID string`

    Directory being processed

  - `EffectiveAt Time`

  - `ErrorMessage string`

    Error message for the latest job attempt, if any.

  - `FailedItems int64`

    Number of items that failed processing

  - `JobRecordID string`

    The job record ID associated with this status, if any.

  - `ProcessedItems int64`

    Number of items processed so far

  - `SkippedItems int64`

    Number of items skipped (already processed or size limit)

  - `StartedAt Time`

    Timestamp when job processing started

  - `UpdatedAt Time`

    Update datetime

  - `WorkflowID string`

    Async job tracking ID

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
  page, err := client.Beta.Batch.List(context.TODO(), llamacloudprod.BetaBatchListParams{

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
      "id": "bjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "job_type": "parse",
      "project_id": "proj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "status": "pending",
      "total_items": 0,
      "completed_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "effective_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "failed_items": 0,
      "job_record_id": "job_record_id",
      "processed_items": 0,
      "skipped_items": 0,
      "started_at": "2019-12-27T18:11:19.117Z",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "workflow_id": "workflow_id"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Batch Job Status

`client.Beta.Batch.GetStatus(ctx, jobID, query) (*BetaBatchGetStatusResponse, error)`

**get** `/api/v1/beta/batch-processing/{job_id}`

Get detailed status of a batch processing job.

Returns current progress percentage, file counts (total,
processed, failed, skipped), and timestamps.

### Parameters

- `jobID string`

- `query BetaBatchGetStatusParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type BetaBatchGetStatusResponse struct{…}`

  Detailed status response for a batch processing job.

  - `Job BetaBatchGetStatusResponseJob`

    Response schema for a batch processing job.

    - `ID string`

      Unique identifier for the batch job

    - `JobType string`

      Type of processing operation (parse or classify)

      - `const BetaBatchGetStatusResponseJobJobTypeParse BetaBatchGetStatusResponseJobJobType = "parse"`

      - `const BetaBatchGetStatusResponseJobJobTypeExtract BetaBatchGetStatusResponseJobJobType = "extract"`

      - `const BetaBatchGetStatusResponseJobJobTypeClassify BetaBatchGetStatusResponseJobJobType = "classify"`

    - `ProjectID string`

      Project this job belongs to

    - `Status string`

      Current job status

      - `const BetaBatchGetStatusResponseJobStatusPending BetaBatchGetStatusResponseJobStatus = "pending"`

      - `const BetaBatchGetStatusResponseJobStatusRunning BetaBatchGetStatusResponseJobStatus = "running"`

      - `const BetaBatchGetStatusResponseJobStatusDispatched BetaBatchGetStatusResponseJobStatus = "dispatched"`

      - `const BetaBatchGetStatusResponseJobStatusCompleted BetaBatchGetStatusResponseJobStatus = "completed"`

      - `const BetaBatchGetStatusResponseJobStatusFailed BetaBatchGetStatusResponseJobStatus = "failed"`

      - `const BetaBatchGetStatusResponseJobStatusCancelled BetaBatchGetStatusResponseJobStatus = "cancelled"`

    - `TotalItems int64`

      Total number of items in the job

    - `CompletedAt Time`

      Timestamp when job completed

    - `CreatedAt Time`

      Creation datetime

    - `DirectoryID string`

      Directory being processed

    - `EffectiveAt Time`

    - `ErrorMessage string`

      Error message for the latest job attempt, if any.

    - `FailedItems int64`

      Number of items that failed processing

    - `JobRecordID string`

      The job record ID associated with this status, if any.

    - `ProcessedItems int64`

      Number of items processed so far

    - `SkippedItems int64`

      Number of items skipped (already processed or size limit)

    - `StartedAt Time`

      Timestamp when job processing started

    - `UpdatedAt Time`

      Update datetime

    - `WorkflowID string`

      Async job tracking ID

  - `ProgressPercentage float64`

    Percentage of items processed (0-100)

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
  response, err := client.Beta.Batch.GetStatus(
    context.TODO(),
    "job_id",
    llamacloudprod.BetaBatchGetStatusParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Job)
}
```

#### Response

```json
{
  "job": {
    "id": "bjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "job_type": "parse",
    "project_id": "proj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "status": "pending",
    "total_items": 0,
    "completed_at": "2019-12-27T18:11:19.117Z",
    "created_at": "2019-12-27T18:11:19.117Z",
    "directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "effective_at": "2019-12-27T18:11:19.117Z",
    "error_message": "error_message",
    "failed_items": 0,
    "job_record_id": "job_record_id",
    "processed_items": 0,
    "skipped_items": 0,
    "started_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "workflow_id": "workflow_id"
  },
  "progress_percentage": 0
}
```

## Cancel Batch Job

`client.Beta.Batch.Cancel(ctx, jobID, params) (*BetaBatchCancelResponse, error)`

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Parameters

- `jobID string`

- `params BetaBatchCancelParams`

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Reason param.Field[string]`

    Body param: Optional reason for cancelling the job

  - `TemporalNamespace param.Field[string]`

    Header param

### Returns

- `type BetaBatchCancelResponse struct{…}`

  Response after cancelling a batch job.

  - `JobID string`

    ID of the cancelled job

  - `Message string`

    Confirmation message

  - `ProcessedItems int64`

    Number of items processed before cancellation

  - `Status BetaBatchCancelResponseStatus`

    New status (should be 'cancelled')

    - `const BetaBatchCancelResponseStatusPending BetaBatchCancelResponseStatus = "pending"`

    - `const BetaBatchCancelResponseStatusRunning BetaBatchCancelResponseStatus = "running"`

    - `const BetaBatchCancelResponseStatusDispatched BetaBatchCancelResponseStatus = "dispatched"`

    - `const BetaBatchCancelResponseStatusCompleted BetaBatchCancelResponseStatus = "completed"`

    - `const BetaBatchCancelResponseStatusFailed BetaBatchCancelResponseStatus = "failed"`

    - `const BetaBatchCancelResponseStatusCancelled BetaBatchCancelResponseStatus = "cancelled"`

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
  response, err := client.Beta.Batch.Cancel(
    context.TODO(),
    "job_id",
    llamacloudprod.BetaBatchCancelParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.JobID)
}
```

#### Response

```json
{
  "job_id": "job_id",
  "message": "message",
  "processed_items": 0,
  "status": "pending"
}
```

# Job Items

## List Batch Job Items

`client.Beta.Batch.JobItems.List(ctx, jobID, query) (*PaginatedBatchItems[BetaBatchJobItemListResponse], error)`

**get** `/api/v1/beta/batch-processing/{job_id}/items`

List items in a batch job with optional status filtering.

Useful for finding failed items, viewing completed items,
or debugging processing issues.

### Parameters

- `jobID string`

- `query BetaBatchJobItemListParams`

  - `Limit param.Field[int64]`

    Maximum number of items to return

  - `Offset param.Field[int64]`

    Number of items to skip

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

  - `Status param.Field[BetaBatchJobItemListParamsStatus]`

    Filter items by status

    - `const BetaBatchJobItemListParamsStatusPending BetaBatchJobItemListParamsStatus = "pending"`

    - `const BetaBatchJobItemListParamsStatusProcessing BetaBatchJobItemListParamsStatus = "processing"`

    - `const BetaBatchJobItemListParamsStatusCompleted BetaBatchJobItemListParamsStatus = "completed"`

    - `const BetaBatchJobItemListParamsStatusFailed BetaBatchJobItemListParamsStatus = "failed"`

    - `const BetaBatchJobItemListParamsStatusSkipped BetaBatchJobItemListParamsStatus = "skipped"`

    - `const BetaBatchJobItemListParamsStatusCancelled BetaBatchJobItemListParamsStatus = "cancelled"`

### Returns

- `type BetaBatchJobItemListResponse struct{…}`

  Detailed information about an item in a batch job.

  - `ItemID string`

    ID of the item

  - `ItemName string`

    Name of the item

  - `Status BetaBatchJobItemListResponseStatus`

    Processing status of this item

    - `const BetaBatchJobItemListResponseStatusPending BetaBatchJobItemListResponseStatus = "pending"`

    - `const BetaBatchJobItemListResponseStatusProcessing BetaBatchJobItemListResponseStatus = "processing"`

    - `const BetaBatchJobItemListResponseStatusCompleted BetaBatchJobItemListResponseStatus = "completed"`

    - `const BetaBatchJobItemListResponseStatusFailed BetaBatchJobItemListResponseStatus = "failed"`

    - `const BetaBatchJobItemListResponseStatusSkipped BetaBatchJobItemListResponseStatus = "skipped"`

    - `const BetaBatchJobItemListResponseStatusCancelled BetaBatchJobItemListResponseStatus = "cancelled"`

  - `CompletedAt Time`

    When processing completed for this item

  - `EffectiveAt Time`

  - `ErrorMessage string`

    Error message for the latest job attempt, if any.

  - `JobID string`

    Job ID for the underlying processing job (links to parse/extract job results)

  - `JobRecordID string`

    The job record ID associated with this status, if any.

  - `SkipReason string`

    Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

  - `StartedAt Time`

    When processing started for this item

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
  page, err := client.Beta.Batch.JobItems.List(
    context.TODO(),
    "job_id",
    llamacloudprod.BetaBatchJobItemListParams{

    },
  )
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
      "item_id": "item_id",
      "item_name": "item_name",
      "status": "pending",
      "completed_at": "2019-12-27T18:11:19.117Z",
      "effective_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "job_id": "job_id",
      "job_record_id": "job_record_id",
      "skip_reason": "skip_reason",
      "started_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Item Processing Results

`client.Beta.Batch.JobItems.GetProcessingResults(ctx, itemID, query) (*BetaBatchJobItemGetProcessingResultsResponse, error)`

**get** `/api/v1/beta/batch-processing/items/{item_id}/processing-results`

Get all processing results for a specific item.

Returns the complete processing history for an item including
what operations were performed, parameters used, and where
outputs are stored. Optionally filter by `job_type`.

### Parameters

- `itemID string`

- `query BetaBatchJobItemGetProcessingResultsParams`

  - `JobType param.Field[BetaBatchJobItemGetProcessingResultsParamsJobType]`

    Filter results by job type

    - `const BetaBatchJobItemGetProcessingResultsParamsJobTypeParse BetaBatchJobItemGetProcessingResultsParamsJobType = "parse"`

    - `const BetaBatchJobItemGetProcessingResultsParamsJobTypeExtract BetaBatchJobItemGetProcessingResultsParamsJobType = "extract"`

    - `const BetaBatchJobItemGetProcessingResultsParamsJobTypeClassify BetaBatchJobItemGetProcessingResultsParamsJobType = "classify"`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type BetaBatchJobItemGetProcessingResultsResponse struct{…}`

  Response containing all processing results for an item.

  - `ItemID string`

    ID of the source item

  - `ItemName string`

    Name of the source item

  - `ProcessingResults []BetaBatchJobItemGetProcessingResultsResponseProcessingResult`

    List of all processing operations performed on this item

    - `ItemID string`

      Source item that was processed

    - `JobConfig BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigUnion`

      Job configuration used for processing

      - `type BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreate struct{…}`

        Batch-specific parse job record for batch processing.

        This model contains the metadata and configuration for a batch parse job,
        but excludes file-specific information. It's used as input to the batch
        parent workflow and combined with DirectoryFile data to create full
        ParseJobRecordCreate instances for each file.

        Attributes:
        job_name: Must be PARSE_RAW_FILE
        partitions: Partitions for job output location
        parameters: Generic parse configuration (BatchParseJobConfig)
        session_id: Upstream request ID for tracking
        correlation_id: Correlation ID for cross-service tracking
        parent_job_execution_id: Parent job execution ID if nested
        user_id: User who created the job
        project_id: Project this job belongs to
        webhook_url: Optional webhook URL for job completion notifications

        - `CorrelationID string`

          The correlation ID for this job. Used for tracking the job across services.

        - `JobName string`

          - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateJobNameParseRawFileJob BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateJobName = "parse_raw_file_job"`

        - `Parameters BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParameters`

          Generic parse job configuration for batch processing.

          This model contains the parsing configuration that applies to all files
          in a batch, but excludes file-specific fields like file_name, file_id, etc.
          Those file-specific fields are populated from DirectoryFile data when
          creating individual ParseJobRecordCreate instances for each file.

          The fields in this model should be generic settings that apply uniformly
          to all files being processed in the batch.

          - `AdaptiveLongTable bool`

          - `AggressiveTableExtraction bool`

          - `AnnotateLinks bool`

          - `AutoMode bool`

          - `AutoModeConfigurationJson string`

          - `AutoModeTriggerOnImageInPage bool`

          - `AutoModeTriggerOnRegexpInPage string`

          - `AutoModeTriggerOnTableInPage bool`

          - `AutoModeTriggerOnTextInPage string`

          - `AzureOpenAIAPIVersion string`

          - `AzureOpenAIDeploymentName string`

          - `AzureOpenAIEndpoint string`

          - `AzureOpenAIKey string`

          - `BboxBottom float64`

          - `BboxLeft float64`

          - `BboxRight float64`

          - `BboxTop float64`

          - `BoundingBox string`

          - `CompactMarkdownTable bool`

          - `ComplementalFormattingInstruction string`

          - `ContentGuidelineInstruction string`

          - `ContinuousMode bool`

          - `CustomMetadata map[string, any]`

            The custom metadata to attach to the documents.

          - `DisableImageExtraction bool`

          - `DisableOcr bool`

          - `DisableReconstruction bool`

          - `DoNotCache bool`

          - `DoNotUnrollColumns bool`

          - `EnableCostOptimizer bool`

          - `ExtractCharts bool`

          - `ExtractLayout bool`

          - `ExtractPrintedPageNumber bool`

          - `FastMode bool`

          - `FormattingInstruction string`

          - `Gpt4oAPIKey string`

          - `Gpt4oMode bool`

          - `GuessXlsxSheetName bool`

          - `HideFooters bool`

          - `HideHeaders bool`

          - `HighResOcr bool`

          - `HTMLMakeAllElementsVisible bool`

          - `HTMLRemoveFixedElements bool`

          - `HTMLRemoveNavigationElements bool`

          - `HTTPProxy string`

          - `IgnoreDocumentElementsForLayoutDetection bool`

          - `ImagesToSave []string`

            - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersImagesToSaveScreenshot BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersImagesToSave = "screenshot"`

            - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersImagesToSaveEmbedded BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersImagesToSave = "embedded"`

            - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersImagesToSaveLayout BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersImagesToSave = "layout"`

          - `InlineImagesInMarkdown bool`

          - `InputS3Path string`

          - `InputS3Region string`

            The region for the input S3 bucket.

          - `InputURL string`

          - `InternalIsScreenshotJob bool`

          - `InvalidateCache bool`

          - `IsFormattingInstruction bool`

          - `JobTimeoutExtraTimePerPageInSeconds float64`

          - `JobTimeoutInSeconds float64`

          - `KeepPageSeparatorWhenMergingTables bool`

          - `Lang string`

            The language.

          - `Languages []ParsingLanguages`

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

          - `LayoutAware bool`

          - `LineLevelBoundingBox bool`

          - `MarkdownTableMultilineHeaderSeparator string`

          - `MaxPages int64`

          - `MaxPagesEnforced int64`

          - `MergeTablesAcrossPagesInMarkdown bool`

          - `Model string`

          - `OutlinedTableExtraction bool`

          - `OutputPdfOfDocument bool`

          - `OutputS3PathPrefix string`

            If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

          - `OutputS3Region string`

            The region for the output S3 bucket.

          - `OutputTablesAsHTML bool`

          - `OutputBucket string`

            The output bucket.

          - `PageErrorTolerance float64`

          - `PageFooterPrefix string`

          - `PageFooterSuffix string`

          - `PageHeaderPrefix string`

          - `PageHeaderSuffix string`

          - `PagePrefix string`

          - `PageSeparator string`

          - `PageSuffix string`

          - `ParseMode ParsingMode`

            Enum for representing the mode of parsing to be used.

            - `const ParsingModeParsePageWithoutLlm ParsingMode = "parse_page_without_llm"`

            - `const ParsingModeParsePageWithLlm ParsingMode = "parse_page_with_llm"`

            - `const ParsingModeParsePageWithLvm ParsingMode = "parse_page_with_lvm"`

            - `const ParsingModeParsePageWithAgent ParsingMode = "parse_page_with_agent"`

            - `const ParsingModeParsePageWithLayoutAgent ParsingMode = "parse_page_with_layout_agent"`

            - `const ParsingModeParseDocumentWithLlm ParsingMode = "parse_document_with_llm"`

            - `const ParsingModeParseDocumentWithLvm ParsingMode = "parse_document_with_lvm"`

            - `const ParsingModeParseDocumentWithAgent ParsingMode = "parse_document_with_agent"`

          - `ParsingInstruction string`

          - `PipelineID string`

            The pipeline ID.

          - `PreciseBoundingBox bool`

          - `PremiumMode bool`

          - `PresentationOutOfBoundsContent bool`

          - `PresentationSkipEmbeddedData bool`

          - `PreserveLayoutAlignmentAcrossPages bool`

          - `PreserveVerySmallText bool`

          - `Preset string`

          - `Priority string`

            The priority for the request. This field may be ignored or overwritten depending on the organization tier.

            - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersPriorityLow BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersPriority = "low"`

            - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersPriorityMedium BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersPriority = "medium"`

            - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersPriorityHigh BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersPriority = "high"`

            - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersPriorityCritical BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersPriority = "critical"`

          - `ProjectID string`

          - `RemoveHiddenText bool`

          - `ReplaceFailedPageMode FailPageMode`

            Enum for representing the different available page error handling modes.

            - `const FailPageModeRawText FailPageMode = "raw_text"`

            - `const FailPageModeBlankPage FailPageMode = "blank_page"`

            - `const FailPageModeErrorMessage FailPageMode = "error_message"`

          - `ReplaceFailedPageWithErrorMessagePrefix string`

          - `ReplaceFailedPageWithErrorMessageSuffix string`

          - `ResourceInfo map[string, any]`

            The resource info about the file

          - `SaveImages bool`

          - `SkipDiagonalText bool`

          - `SpecializedChartParsingAgentic bool`

          - `SpecializedChartParsingEfficient bool`

          - `SpecializedChartParsingPlus bool`

          - `SpecializedImageParsing bool`

          - `SpreadsheetExtractSubTables bool`

          - `SpreadsheetForceFormulaComputation bool`

          - `SpreadsheetIncludeHiddenSheets bool`

          - `StrictModeBuggyFont bool`

          - `StrictModeImageExtraction bool`

          - `StrictModeImageOcr bool`

          - `StrictModeReconstruction bool`

          - `StructuredOutput bool`

          - `StructuredOutputJsonSchema string`

          - `StructuredOutputJsonSchemaName string`

          - `SystemPrompt string`

          - `SystemPromptAppend string`

          - `TakeScreenshot bool`

          - `TargetPages string`

          - `Tier string`

          - `Type string`

            - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersTypeParse BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersType = "parse"`

          - `UseVendorMultimodalModel bool`

          - `UserPrompt string`

          - `VendorMultimodalAPIKey string`

          - `VendorMultimodalModelName string`

          - `Version string`

          - `WebhookConfigurations []BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfiguration`

            Outbound webhook endpoints to notify on job status changes

            - `WebhookEvents []string`

              Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractPending BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.pending"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractSuccess BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.success"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractError BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.error"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractPartialSuccess BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.partial_success"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventExtractCancelled BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "extract.cancelled"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParsePending BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.pending"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParseRunning BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.running"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParseSuccess BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.success"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParseError BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.error"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParsePartialSuccess BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.partial_success"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventParseCancelled BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "parse.cancelled"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifyPending BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.pending"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifySuccess BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.success"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifyError BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.error"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifyPartialSuccess BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.partial_success"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventClassifyCancelled BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "classify.cancelled"`

              - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEventUnmappedEvent BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfigurationWebhookEvent = "unmapped_event"`

            - `WebhookHeaders map[string, string]`

              Custom HTTP headers sent with each webhook request (e.g. auth tokens)

            - `WebhookOutputFormat string`

              Response format sent to the webhook: 'string' (default) or 'json'

            - `WebhookURL string`

              URL to receive webhook POST notifications

          - `WebhookURL string`

        - `ParentJobExecutionID string`

          The ID of the parent job execution.

        - `Partitions map[string, string]`

          The partitions for this execution. Used for determining where to save job output.

        - `ProjectID string`

          The ID of the project this job belongs to.

        - `SessionID string`

          The upstream request ID that created this job. Used for tracking the job across services.

        - `UserID string`

          The ID of the user that created this job

        - `WebhookURL string`

          The URL that needs to be called at the end of the parsing job.

      - `type ClassifyJob struct{…}`

        A classify job.

        - `ID string`

          Unique identifier

        - `ProjectID string`

          The ID of the project

        - `Rules []ClassifierRule`

          The rules to classify the files

          - `Description string`

            Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

          - `Type string`

            The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

        - `Status StatusEnum`

          The status of the classify job

          - `const StatusEnumPending StatusEnum = "PENDING"`

          - `const StatusEnumSuccess StatusEnum = "SUCCESS"`

          - `const StatusEnumError StatusEnum = "ERROR"`

          - `const StatusEnumPartialSuccess StatusEnum = "PARTIAL_SUCCESS"`

          - `const StatusEnumCancelled StatusEnum = "CANCELLED"`

        - `UserID string`

          The ID of the user

        - `CreatedAt Time`

          Creation datetime

        - `EffectiveAt Time`

        - `ErrorMessage string`

          Error message for the latest job attempt, if any.

        - `JobRecordID string`

          The job record ID associated with this status, if any.

        - `Mode ClassifyJobMode`

          The classification mode to use

          - `const ClassifyJobModeFast ClassifyJobMode = "FAST"`

          - `const ClassifyJobModeMultimodal ClassifyJobMode = "MULTIMODAL"`

        - `ParsingConfiguration ClassifyParsingConfiguration`

          The configuration for the parsing job

          - `Lang ParsingLanguages`

            The language to parse the files in

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

          - `MaxPages int64`

            The maximum number of pages to parse

          - `TargetPages []int64`

            The pages to target for parsing (0-indexed, so first page is at 0)

        - `UpdatedAt Time`

          Update datetime

    - `JobType string`

      Type of processing performed

      - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobTypeParse BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobType = "parse"`

      - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobTypeExtract BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobType = "extract"`

      - `const BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobTypeClassify BetaBatchJobItemGetProcessingResultsResponseProcessingResultJobType = "classify"`

    - `OutputS3Path string`

      Location of the processing output

    - `ParametersHash string`

      Content hash of the job configuration for dedup

    - `ProcessedAt Time`

      When this processing occurred

    - `ResultID string`

      Unique identifier for this result

    - `OutputMetadata any`

      Metadata about processing output.

      Currently empty - will be populated with job-type-specific metadata fields in the future.

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
  response, err := client.Beta.Batch.JobItems.GetProcessingResults(
    context.TODO(),
    "item_id",
    llamacloudprod.BetaBatchJobItemGetProcessingResultsParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.ItemID)
}
```

#### Response

```json
{
  "item_id": "item_id",
  "item_name": "item_name",
  "processing_results": [
    {
      "item_id": "item_id",
      "job_config": {
        "correlation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "job_name": "parse_raw_file_job",
        "parameters": {
          "adaptive_long_table": true,
          "aggressive_table_extraction": true,
          "annotate_links": true,
          "auto_mode": true,
          "auto_mode_configuration_json": "auto_mode_configuration_json",
          "auto_mode_trigger_on_image_in_page": true,
          "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
          "auto_mode_trigger_on_table_in_page": true,
          "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
          "azure_openai_api_version": "azure_openai_api_version",
          "azure_openai_deployment_name": "azure_openai_deployment_name",
          "azure_openai_endpoint": "azure_openai_endpoint",
          "azure_openai_key": "azure_openai_key",
          "bbox_bottom": 0,
          "bbox_left": 0,
          "bbox_right": 0,
          "bbox_top": 0,
          "bounding_box": "bounding_box",
          "compact_markdown_table": true,
          "complemental_formatting_instruction": "complemental_formatting_instruction",
          "content_guideline_instruction": "content_guideline_instruction",
          "continuous_mode": true,
          "custom_metadata": {
            "foo": "bar"
          },
          "disable_image_extraction": true,
          "disable_ocr": true,
          "disable_reconstruction": true,
          "do_not_cache": true,
          "do_not_unroll_columns": true,
          "enable_cost_optimizer": true,
          "extract_charts": true,
          "extract_layout": true,
          "extract_printed_page_number": true,
          "fast_mode": true,
          "formatting_instruction": "formatting_instruction",
          "gpt4o_api_key": "gpt4o_api_key",
          "gpt4o_mode": true,
          "guess_xlsx_sheet_name": true,
          "hide_footers": true,
          "hide_headers": true,
          "high_res_ocr": true,
          "html_make_all_elements_visible": true,
          "html_remove_fixed_elements": true,
          "html_remove_navigation_elements": true,
          "http_proxy": "http_proxy",
          "ignore_document_elements_for_layout_detection": true,
          "images_to_save": [
            "screenshot"
          ],
          "inline_images_in_markdown": true,
          "input_s3_path": "input_s3_path",
          "input_s3_region": "input_s3_region",
          "input_url": "input_url",
          "internal_is_screenshot_job": true,
          "invalidate_cache": true,
          "is_formatting_instruction": true,
          "job_timeout_extra_time_per_page_in_seconds": 0,
          "job_timeout_in_seconds": 0,
          "keep_page_separator_when_merging_tables": true,
          "lang": "lang",
          "languages": [
            "af"
          ],
          "layout_aware": true,
          "line_level_bounding_box": true,
          "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
          "max_pages": 0,
          "max_pages_enforced": 0,
          "merge_tables_across_pages_in_markdown": true,
          "model": "model",
          "outlined_table_extraction": true,
          "output_pdf_of_document": true,
          "output_s3_path_prefix": "output_s3_path_prefix",
          "output_s3_region": "output_s3_region",
          "output_tables_as_HTML": true,
          "outputBucket": "outputBucket",
          "page_error_tolerance": 0,
          "page_footer_prefix": "page_footer_prefix",
          "page_footer_suffix": "page_footer_suffix",
          "page_header_prefix": "page_header_prefix",
          "page_header_suffix": "page_header_suffix",
          "page_prefix": "page_prefix",
          "page_separator": "page_separator",
          "page_suffix": "page_suffix",
          "parse_mode": "parse_page_without_llm",
          "parsing_instruction": "parsing_instruction",
          "pipeline_id": "pipeline_id",
          "precise_bounding_box": true,
          "premium_mode": true,
          "presentation_out_of_bounds_content": true,
          "presentation_skip_embedded_data": true,
          "preserve_layout_alignment_across_pages": true,
          "preserve_very_small_text": true,
          "preset": "preset",
          "priority": "low",
          "project_id": "project_id",
          "remove_hidden_text": true,
          "replace_failed_page_mode": "raw_text",
          "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
          "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
          "resource_info": {
            "foo": "bar"
          },
          "save_images": true,
          "skip_diagonal_text": true,
          "specialized_chart_parsing_agentic": true,
          "specialized_chart_parsing_efficient": true,
          "specialized_chart_parsing_plus": true,
          "specialized_image_parsing": true,
          "spreadsheet_extract_sub_tables": true,
          "spreadsheet_force_formula_computation": true,
          "spreadsheet_include_hidden_sheets": true,
          "strict_mode_buggy_font": true,
          "strict_mode_image_extraction": true,
          "strict_mode_image_ocr": true,
          "strict_mode_reconstruction": true,
          "structured_output": true,
          "structured_output_json_schema": "structured_output_json_schema",
          "structured_output_json_schema_name": "structured_output_json_schema_name",
          "system_prompt": "system_prompt",
          "system_prompt_append": "system_prompt_append",
          "take_screenshot": true,
          "target_pages": "target_pages",
          "tier": "tier",
          "type": "parse",
          "use_vendor_multimodal_model": true,
          "user_prompt": "user_prompt",
          "vendor_multimodal_api_key": "vendor_multimodal_api_key",
          "vendor_multimodal_model_name": "vendor_multimodal_model_name",
          "version": "version",
          "webhook_configurations": [
            {
              "webhook_events": [
                "parse.success",
                "parse.error"
              ],
              "webhook_headers": {
                "Authorization": "Bearer sk-..."
              },
              "webhook_output_format": "json",
              "webhook_url": "https://example.com/webhooks/llamacloud"
            }
          ],
          "webhook_url": "webhook_url"
        },
        "parent_job_execution_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "partitions": {
          "foo": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
        },
        "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "user_id": "user_id",
        "webhook_url": "webhook_url"
      },
      "job_type": "parse",
      "output_s3_path": "output_s3_path",
      "parameters_hash": "parameters_hash",
      "processed_at": "2019-12-27T18:11:19.117Z",
      "result_id": "result_id",
      "output_metadata": {}
    }
  ]
}
```
