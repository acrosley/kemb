## Create Batch Job

`client.beta.batch.create(BatchCreateParamsparams, RequestOptionsoptions?): BatchCreateResponse`

**post** `/api/v1/beta/batch-processing`

Create a batch processing job.

Processes files from a directory or a specific list of item IDs.
Supports batch parsing and classification operations.

Provide either `directory_id` to process all files in a directory,
or `item_ids` for specific items. The job runs asynchronously —
poll `GET /batch/{job_id}` for progress.

### Parameters

- `params: BatchCreateParams`

  - `job_config: BatchParseJobRecordCreate | ClassifyJob`

    Body param: Job configuration — either a parse or classify config

    - `BatchParseJobRecordCreate`

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

      - `correlation_id?: string | null`

        The correlation ID for this job. Used for tracking the job across services.

      - `job_name?: "parse_raw_file_job"`

        - `"parse_raw_file_job"`

      - `parameters?: Parameters | null`

        Generic parse job configuration for batch processing.

        This model contains the parsing configuration that applies to all files
        in a batch, but excludes file-specific fields like file_name, file_id, etc.
        Those file-specific fields are populated from DirectoryFile data when
        creating individual ParseJobRecordCreate instances for each file.

        The fields in this model should be generic settings that apply uniformly
        to all files being processed in the batch.

        - `adaptive_long_table?: boolean | null`

        - `aggressive_table_extraction?: boolean | null`

        - `annotate_links?: boolean | null`

        - `auto_mode?: boolean | null`

        - `auto_mode_configuration_json?: string | null`

        - `auto_mode_trigger_on_image_in_page?: boolean | null`

        - `auto_mode_trigger_on_regexp_in_page?: string | null`

        - `auto_mode_trigger_on_table_in_page?: boolean | null`

        - `auto_mode_trigger_on_text_in_page?: string | null`

        - `azure_openai_api_version?: string | null`

        - `azure_openai_deployment_name?: string | null`

        - `azure_openai_endpoint?: string | null`

        - `azure_openai_key?: string | null`

        - `bbox_bottom?: number | null`

        - `bbox_left?: number | null`

        - `bbox_right?: number | null`

        - `bbox_top?: number | null`

        - `bounding_box?: string | null`

        - `compact_markdown_table?: boolean | null`

        - `complemental_formatting_instruction?: string | null`

        - `content_guideline_instruction?: string | null`

        - `continuous_mode?: boolean | null`

        - `custom_metadata?: Record<string, unknown> | null`

          The custom metadata to attach to the documents.

        - `disable_image_extraction?: boolean | null`

        - `disable_ocr?: boolean | null`

        - `disable_reconstruction?: boolean | null`

        - `do_not_cache?: boolean | null`

        - `do_not_unroll_columns?: boolean | null`

        - `enable_cost_optimizer?: boolean | null`

        - `extract_charts?: boolean | null`

        - `extract_layout?: boolean | null`

        - `extract_printed_page_number?: boolean | null`

        - `fast_mode?: boolean | null`

        - `formatting_instruction?: string | null`

        - `gpt4o_api_key?: string | null`

        - `gpt4o_mode?: boolean | null`

        - `guess_xlsx_sheet_name?: boolean | null`

        - `hide_footers?: boolean | null`

        - `hide_headers?: boolean | null`

        - `high_res_ocr?: boolean | null`

        - `html_make_all_elements_visible?: boolean | null`

        - `html_remove_fixed_elements?: boolean | null`

        - `html_remove_navigation_elements?: boolean | null`

        - `http_proxy?: string | null`

        - `ignore_document_elements_for_layout_detection?: boolean | null`

        - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

          - `"screenshot"`

          - `"embedded"`

          - `"layout"`

        - `inline_images_in_markdown?: boolean | null`

        - `input_s3_path?: string | null`

        - `input_s3_region?: string | null`

          The region for the input S3 bucket.

        - `input_url?: string | null`

        - `internal_is_screenshot_job?: boolean | null`

        - `invalidate_cache?: boolean | null`

        - `is_formatting_instruction?: boolean | null`

        - `job_timeout_extra_time_per_page_in_seconds?: number | null`

        - `job_timeout_in_seconds?: number | null`

        - `keep_page_separator_when_merging_tables?: boolean | null`

        - `lang?: string`

          The language.

        - `languages?: Array<ParsingLanguages>`

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

        - `layout_aware?: boolean | null`

        - `line_level_bounding_box?: boolean | null`

        - `markdown_table_multiline_header_separator?: string | null`

        - `max_pages?: number | null`

        - `max_pages_enforced?: number | null`

        - `merge_tables_across_pages_in_markdown?: boolean | null`

        - `model?: string | null`

        - `outlined_table_extraction?: boolean | null`

        - `output_pdf_of_document?: boolean | null`

        - `output_s3_path_prefix?: string | null`

          If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

        - `output_s3_region?: string | null`

          The region for the output S3 bucket.

        - `output_tables_as_HTML?: boolean | null`

        - `outputBucket?: string | null`

          The output bucket.

        - `page_error_tolerance?: number | null`

        - `page_footer_prefix?: string | null`

        - `page_footer_suffix?: string | null`

        - `page_header_prefix?: string | null`

        - `page_header_suffix?: string | null`

        - `page_prefix?: string | null`

        - `page_separator?: string | null`

        - `page_suffix?: string | null`

        - `parse_mode?: ParsingMode | null`

          Enum for representing the mode of parsing to be used.

          - `"parse_page_without_llm"`

          - `"parse_page_with_llm"`

          - `"parse_page_with_lvm"`

          - `"parse_page_with_agent"`

          - `"parse_page_with_layout_agent"`

          - `"parse_document_with_llm"`

          - `"parse_document_with_lvm"`

          - `"parse_document_with_agent"`

        - `parsing_instruction?: string | null`

        - `pipeline_id?: string | null`

          The pipeline ID.

        - `precise_bounding_box?: boolean | null`

        - `premium_mode?: boolean | null`

        - `presentation_out_of_bounds_content?: boolean | null`

        - `presentation_skip_embedded_data?: boolean | null`

        - `preserve_layout_alignment_across_pages?: boolean | null`

        - `preserve_very_small_text?: boolean | null`

        - `preset?: string | null`

        - `priority?: "low" | "medium" | "high" | "critical" | null`

          The priority for the request. This field may be ignored or overwritten depending on the organization tier.

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"critical"`

        - `project_id?: string | null`

        - `remove_hidden_text?: boolean | null`

        - `replace_failed_page_mode?: FailPageMode | null`

          Enum for representing the different available page error handling modes.

          - `"raw_text"`

          - `"blank_page"`

          - `"error_message"`

        - `replace_failed_page_with_error_message_prefix?: string | null`

        - `replace_failed_page_with_error_message_suffix?: string | null`

        - `resource_info?: Record<string, unknown> | null`

          The resource info about the file

        - `save_images?: boolean | null`

        - `skip_diagonal_text?: boolean | null`

        - `specialized_chart_parsing_agentic?: boolean | null`

        - `specialized_chart_parsing_efficient?: boolean | null`

        - `specialized_chart_parsing_plus?: boolean | null`

        - `specialized_image_parsing?: boolean | null`

        - `spreadsheet_extract_sub_tables?: boolean | null`

        - `spreadsheet_force_formula_computation?: boolean | null`

        - `spreadsheet_include_hidden_sheets?: boolean | null`

        - `strict_mode_buggy_font?: boolean | null`

        - `strict_mode_image_extraction?: boolean | null`

        - `strict_mode_image_ocr?: boolean | null`

        - `strict_mode_reconstruction?: boolean | null`

        - `structured_output?: boolean | null`

        - `structured_output_json_schema?: string | null`

        - `structured_output_json_schema_name?: string | null`

        - `system_prompt?: string | null`

        - `system_prompt_append?: string | null`

        - `take_screenshot?: boolean | null`

        - `target_pages?: string | null`

        - `tier?: string | null`

        - `type?: "parse"`

          - `"parse"`

        - `use_vendor_multimodal_model?: boolean | null`

        - `user_prompt?: string | null`

        - `vendor_multimodal_api_key?: string | null`

        - `vendor_multimodal_model_name?: string | null`

        - `version?: string | null`

        - `webhook_configurations?: Array<WebhookConfiguration> | null`

          Outbound webhook endpoints to notify on job status changes

          - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

            Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

            - `"extract.pending"`

            - `"extract.success"`

            - `"extract.error"`

            - `"extract.partial_success"`

            - `"extract.cancelled"`

            - `"parse.pending"`

            - `"parse.running"`

            - `"parse.success"`

            - `"parse.error"`

            - `"parse.partial_success"`

            - `"parse.cancelled"`

            - `"classify.pending"`

            - `"classify.success"`

            - `"classify.error"`

            - `"classify.partial_success"`

            - `"classify.cancelled"`

            - `"unmapped_event"`

          - `webhook_headers?: Record<string, string> | null`

            Custom HTTP headers sent with each webhook request (e.g. auth tokens)

          - `webhook_output_format?: string | null`

            Response format sent to the webhook: 'string' (default) or 'json'

          - `webhook_url?: string | null`

            URL to receive webhook POST notifications

        - `webhook_url?: string | null`

      - `parent_job_execution_id?: string | null`

        The ID of the parent job execution.

      - `partitions?: Record<string, string>`

        The partitions for this execution. Used for determining where to save job output.

      - `project_id?: string | null`

        The ID of the project this job belongs to.

      - `session_id?: string | null`

        The upstream request ID that created this job. Used for tracking the job across services.

      - `user_id?: string | null`

        The ID of the user that created this job

      - `webhook_url?: string | null`

        The URL that needs to be called at the end of the parsing job.

    - `ClassifyJob`

      A classify job.

      - `id: string`

        Unique identifier

      - `project_id: string`

        The ID of the project

      - `rules: Array<ClassifierRule>`

        The rules to classify the files

        - `description: string`

          Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

        - `type: string`

          The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

      - `status: StatusEnum`

        The status of the classify job

        - `"PENDING"`

        - `"SUCCESS"`

        - `"ERROR"`

        - `"PARTIAL_SUCCESS"`

        - `"CANCELLED"`

      - `user_id: string`

        The ID of the user

      - `created_at?: string | null`

        Creation datetime

      - `effective_at?: string`

      - `error_message?: string | null`

        Error message for the latest job attempt, if any.

      - `job_record_id?: string | null`

        The job record ID associated with this status, if any.

      - `mode?: "FAST" | "MULTIMODAL"`

        The classification mode to use

        - `"FAST"`

        - `"MULTIMODAL"`

      - `parsing_configuration?: ClassifyParsingConfiguration`

        The configuration for the parsing job

        - `lang?: ParsingLanguages`

          The language to parse the files in

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

        - `max_pages?: number | null`

          The maximum number of pages to parse

        - `target_pages?: Array<number> | null`

          The pages to target for parsing (0-indexed, so first page is at 0)

      - `updated_at?: string | null`

        Update datetime

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `continue_as_new_threshold?: number | null`

    Body param: Maximum files to process per execution cycle in directory mode. Defaults to page_size.

  - `directory_id?: string | null`

    Body param: ID of the directory containing files to process

  - `item_ids?: Array<string> | null`

    Body param: List of specific item IDs to process. Either this or directory_id must be provided.

  - `page_size?: number`

    Body param: Number of files to process per batch when using directory mode

  - `temporalNamespace?: string`

    Header param

### Returns

- `BatchCreateResponse`

  Response schema for a batch processing job.

  - `id: string`

    Unique identifier for the batch job

  - `job_type: "parse" | "extract" | "classify"`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: string`

    Project this job belongs to

  - `status: "pending" | "running" | "dispatched" | 3 more`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: number`

    Total number of items in the job

  - `completed_at?: string | null`

    Timestamp when job completed

  - `created_at?: string | null`

    Creation datetime

  - `directory_id?: string | null`

    Directory being processed

  - `effective_at?: string`

  - `error_message?: string | null`

    Error message for the latest job attempt, if any.

  - `failed_items?: number`

    Number of items that failed processing

  - `job_record_id?: string | null`

    The job record ID associated with this status, if any.

  - `processed_items?: number`

    Number of items processed so far

  - `skipped_items?: number`

    Number of items skipped (already processed or size limit)

  - `started_at?: string | null`

    Timestamp when job processing started

  - `updated_at?: string | null`

    Update datetime

  - `workflow_id?: string | null`

    Async job tracking ID

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const batch = await client.beta.batch.create({ job_config: {} });

console.log(batch.id);
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
