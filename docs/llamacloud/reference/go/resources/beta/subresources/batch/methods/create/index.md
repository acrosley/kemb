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
