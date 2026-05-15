## Create Batch Job

**post** `/api/v1/beta/batch-processing`

Create a batch processing job.

Processes files from a directory or a specific list of item IDs.
Supports batch parsing and classification operations.

Provide either `directory_id` to process all files in a directory,
or `item_ids` for specific items. The job runs asynchronously —
poll `GET /batch/{job_id}` for progress.

### Query Parameters

- `organization_id: optional string`

- `project_id: optional string`

### Header Parameters

- `"temporal-namespace": optional string`

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `job_config: object { correlation_id, job_name, parameters, 6 more }  or ClassifyJob`

  Job configuration — either a parse or classify config

  - `BatchParseJobRecordCreate = object { correlation_id, job_name, parameters, 6 more }`

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

    - `correlation_id: optional string`

      The correlation ID for this job. Used for tracking the job across services.

    - `job_name: optional "parse_raw_file_job"`

      - `"parse_raw_file_job"`

    - `parameters: optional object { adaptive_long_table, aggressive_table_extraction, annotate_links, 122 more }`

      Generic parse job configuration for batch processing.

      This model contains the parsing configuration that applies to all files
      in a batch, but excludes file-specific fields like file_name, file_id, etc.
      Those file-specific fields are populated from DirectoryFile data when
      creating individual ParseJobRecordCreate instances for each file.

      The fields in this model should be generic settings that apply uniformly
      to all files being processed in the batch.

      - `adaptive_long_table: optional boolean`

      - `aggressive_table_extraction: optional boolean`

      - `annotate_links: optional boolean`

      - `auto_mode: optional boolean`

      - `auto_mode_configuration_json: optional string`

      - `auto_mode_trigger_on_image_in_page: optional boolean`

      - `auto_mode_trigger_on_regexp_in_page: optional string`

      - `auto_mode_trigger_on_table_in_page: optional boolean`

      - `auto_mode_trigger_on_text_in_page: optional string`

      - `azure_openai_api_version: optional string`

      - `azure_openai_deployment_name: optional string`

      - `azure_openai_endpoint: optional string`

      - `azure_openai_key: optional string`

      - `bbox_bottom: optional number`

      - `bbox_left: optional number`

      - `bbox_right: optional number`

      - `bbox_top: optional number`

      - `bounding_box: optional string`

      - `compact_markdown_table: optional boolean`

      - `complemental_formatting_instruction: optional string`

      - `content_guideline_instruction: optional string`

      - `continuous_mode: optional boolean`

      - `custom_metadata: optional map[unknown]`

        The custom metadata to attach to the documents.

      - `disable_image_extraction: optional boolean`

      - `disable_ocr: optional boolean`

      - `disable_reconstruction: optional boolean`

      - `do_not_cache: optional boolean`

      - `do_not_unroll_columns: optional boolean`

      - `enable_cost_optimizer: optional boolean`

      - `extract_charts: optional boolean`

      - `extract_layout: optional boolean`

      - `extract_printed_page_number: optional boolean`

      - `fast_mode: optional boolean`

      - `formatting_instruction: optional string`

      - `gpt4o_api_key: optional string`

      - `gpt4o_mode: optional boolean`

      - `guess_xlsx_sheet_name: optional boolean`

      - `hide_footers: optional boolean`

      - `hide_headers: optional boolean`

      - `high_res_ocr: optional boolean`

      - `html_make_all_elements_visible: optional boolean`

      - `html_remove_fixed_elements: optional boolean`

      - `html_remove_navigation_elements: optional boolean`

      - `http_proxy: optional string`

      - `ignore_document_elements_for_layout_detection: optional boolean`

      - `images_to_save: optional array of "screenshot" or "embedded" or "layout"`

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `inline_images_in_markdown: optional boolean`

      - `input_s3_path: optional string`

      - `input_s3_region: optional string`

        The region for the input S3 bucket.

      - `input_url: optional string`

      - `internal_is_screenshot_job: optional boolean`

      - `invalidate_cache: optional boolean`

      - `is_formatting_instruction: optional boolean`

      - `job_timeout_extra_time_per_page_in_seconds: optional number`

      - `job_timeout_in_seconds: optional number`

      - `keep_page_separator_when_merging_tables: optional boolean`

      - `lang: optional string`

        The language.

      - `languages: optional array of ParsingLanguages`

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

      - `layout_aware: optional boolean`

      - `line_level_bounding_box: optional boolean`

      - `markdown_table_multiline_header_separator: optional string`

      - `max_pages: optional number`

      - `max_pages_enforced: optional number`

      - `merge_tables_across_pages_in_markdown: optional boolean`

      - `model: optional string`

      - `outlined_table_extraction: optional boolean`

      - `output_pdf_of_document: optional boolean`

      - `output_s3_path_prefix: optional string`

        If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

      - `output_s3_region: optional string`

        The region for the output S3 bucket.

      - `output_tables_as_HTML: optional boolean`

      - `outputBucket: optional string`

        The output bucket.

      - `page_error_tolerance: optional number`

      - `page_footer_prefix: optional string`

      - `page_footer_suffix: optional string`

      - `page_header_prefix: optional string`

      - `page_header_suffix: optional string`

      - `page_prefix: optional string`

      - `page_separator: optional string`

      - `page_suffix: optional string`

      - `parse_mode: optional ParsingMode`

        Enum for representing the mode of parsing to be used.

        - `"parse_page_without_llm"`

        - `"parse_page_with_llm"`

        - `"parse_page_with_lvm"`

        - `"parse_page_with_agent"`

        - `"parse_page_with_layout_agent"`

        - `"parse_document_with_llm"`

        - `"parse_document_with_lvm"`

        - `"parse_document_with_agent"`

      - `parsing_instruction: optional string`

      - `pipeline_id: optional string`

        The pipeline ID.

      - `precise_bounding_box: optional boolean`

      - `premium_mode: optional boolean`

      - `presentation_out_of_bounds_content: optional boolean`

      - `presentation_skip_embedded_data: optional boolean`

      - `preserve_layout_alignment_across_pages: optional boolean`

      - `preserve_very_small_text: optional boolean`

      - `preset: optional string`

      - `priority: optional "low" or "medium" or "high" or "critical"`

        The priority for the request. This field may be ignored or overwritten depending on the organization tier.

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"critical"`

      - `project_id: optional string`

      - `remove_hidden_text: optional boolean`

      - `replace_failed_page_mode: optional FailPageMode`

        Enum for representing the different available page error handling modes.

        - `"raw_text"`

        - `"blank_page"`

        - `"error_message"`

      - `replace_failed_page_with_error_message_prefix: optional string`

      - `replace_failed_page_with_error_message_suffix: optional string`

      - `resource_info: optional map[unknown]`

        The resource info about the file

      - `save_images: optional boolean`

      - `skip_diagonal_text: optional boolean`

      - `specialized_chart_parsing_agentic: optional boolean`

      - `specialized_chart_parsing_efficient: optional boolean`

      - `specialized_chart_parsing_plus: optional boolean`

      - `specialized_image_parsing: optional boolean`

      - `spreadsheet_extract_sub_tables: optional boolean`

      - `spreadsheet_force_formula_computation: optional boolean`

      - `spreadsheet_include_hidden_sheets: optional boolean`

      - `strict_mode_buggy_font: optional boolean`

      - `strict_mode_image_extraction: optional boolean`

      - `strict_mode_image_ocr: optional boolean`

      - `strict_mode_reconstruction: optional boolean`

      - `structured_output: optional boolean`

      - `structured_output_json_schema: optional string`

      - `structured_output_json_schema_name: optional string`

      - `system_prompt: optional string`

      - `system_prompt_append: optional string`

      - `take_screenshot: optional boolean`

      - `target_pages: optional string`

      - `tier: optional string`

      - `type: optional "parse"`

        - `"parse"`

      - `use_vendor_multimodal_model: optional boolean`

      - `user_prompt: optional string`

      - `vendor_multimodal_api_key: optional string`

      - `vendor_multimodal_model_name: optional string`

      - `version: optional string`

      - `webhook_configurations: optional array of object { webhook_events, webhook_headers, webhook_output_format, webhook_url }`

        Outbound webhook endpoints to notify on job status changes

        - `webhook_events: optional array of "extract.pending" or "extract.success" or "extract.error" or 14 more`

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

        - `webhook_headers: optional map[string]`

          Custom HTTP headers sent with each webhook request (e.g. auth tokens)

        - `webhook_output_format: optional string`

          Response format sent to the webhook: 'string' (default) or 'json'

        - `webhook_url: optional string`

          URL to receive webhook POST notifications

      - `webhook_url: optional string`

    - `parent_job_execution_id: optional string`

      The ID of the parent job execution.

    - `partitions: optional map[string]`

      The partitions for this execution. Used for determining where to save job output.

    - `project_id: optional string`

      The ID of the project this job belongs to.

    - `session_id: optional string`

      The upstream request ID that created this job. Used for tracking the job across services.

    - `user_id: optional string`

      The ID of the user that created this job

    - `webhook_url: optional string`

      The URL that needs to be called at the end of the parsing job.

  - `ClassifyJob = object { id, project_id, rules, 9 more }`

    A classify job.

    - `id: string`

      Unique identifier

    - `project_id: string`

      The ID of the project

    - `rules: array of ClassifierRule`

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

    - `created_at: optional string`

      Creation datetime

    - `effective_at: optional string`

    - `error_message: optional string`

      Error message for the latest job attempt, if any.

    - `job_record_id: optional string`

      The job record ID associated with this status, if any.

    - `mode: optional "FAST" or "MULTIMODAL"`

      The classification mode to use

      - `"FAST"`

      - `"MULTIMODAL"`

    - `parsing_configuration: optional ClassifyParsingConfiguration`

      The configuration for the parsing job

      - `lang: optional ParsingLanguages`

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

      - `max_pages: optional number`

        The maximum number of pages to parse

      - `target_pages: optional array of number`

        The pages to target for parsing (0-indexed, so first page is at 0)

    - `updated_at: optional string`

      Update datetime

- `continue_as_new_threshold: optional number`

  Maximum files to process per execution cycle in directory mode. Defaults to page_size.

- `directory_id: optional string`

  ID of the directory containing files to process

- `item_ids: optional array of string`

  List of specific item IDs to process. Either this or directory_id must be provided.

- `page_size: optional number`

  Number of files to process per batch when using directory mode

### Returns

- `id: string`

  Unique identifier for the batch job

- `job_type: "parse" or "extract" or "classify"`

  Type of processing operation (parse or classify)

  - `"parse"`

  - `"extract"`

  - `"classify"`

- `project_id: string`

  Project this job belongs to

- `status: "pending" or "running" or "dispatched" or 3 more`

  Current job status

  - `"pending"`

  - `"running"`

  - `"dispatched"`

  - `"completed"`

  - `"failed"`

  - `"cancelled"`

- `total_items: number`

  Total number of items in the job

- `completed_at: optional string`

  Timestamp when job completed

- `created_at: optional string`

  Creation datetime

- `directory_id: optional string`

  Directory being processed

- `effective_at: optional string`

- `error_message: optional string`

  Error message for the latest job attempt, if any.

- `failed_items: optional number`

  Number of items that failed processing

- `job_record_id: optional string`

  The job record ID associated with this status, if any.

- `processed_items: optional number`

  Number of items processed so far

- `skipped_items: optional number`

  Number of items skipped (already processed or size limit)

- `started_at: optional string`

  Timestamp when job processing started

- `updated_at: optional string`

  Update datetime

- `workflow_id: optional string`

  Async job tracking ID

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/beta/batch-processing \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "job_config": {}
        }'
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
