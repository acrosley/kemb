## Create Batch Job

`beta.batch.create(BatchCreateParams**kwargs)  -> BatchCreateResponse`

**post** `/api/v1/beta/batch-processing`

Create a batch processing job.

Processes files from a directory or a specific list of item IDs.
Supports batch parsing and classification operations.

Provide either `directory_id` to process all files in a directory,
or `item_ids` for specific items. The job runs asynchronously —
poll `GET /batch/{job_id}` for progress.

### Parameters

- `job_config: JobConfig`

  Job configuration — either a parse or classify config

  - `class JobConfigBatchParseJobRecordCreate: …`

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

    - `correlation_id: Optional[str]`

      The correlation ID for this job. Used for tracking the job across services.

    - `job_name: Optional[Literal["parse_raw_file_job"]]`

      - `"parse_raw_file_job"`

    - `parameters: Optional[JobConfigBatchParseJobRecordCreateParameters]`

      Generic parse job configuration for batch processing.

      This model contains the parsing configuration that applies to all files
      in a batch, but excludes file-specific fields like file_name, file_id, etc.
      Those file-specific fields are populated from DirectoryFile data when
      creating individual ParseJobRecordCreate instances for each file.

      The fields in this model should be generic settings that apply uniformly
      to all files being processed in the batch.

      - `adaptive_long_table: Optional[bool]`

      - `aggressive_table_extraction: Optional[bool]`

      - `annotate_links: Optional[bool]`

      - `auto_mode: Optional[bool]`

      - `auto_mode_configuration_json: Optional[str]`

      - `auto_mode_trigger_on_image_in_page: Optional[bool]`

      - `auto_mode_trigger_on_regexp_in_page: Optional[str]`

      - `auto_mode_trigger_on_table_in_page: Optional[bool]`

      - `auto_mode_trigger_on_text_in_page: Optional[str]`

      - `azure_openai_api_version: Optional[str]`

      - `azure_openai_deployment_name: Optional[str]`

      - `azure_openai_endpoint: Optional[str]`

      - `azure_openai_key: Optional[str]`

      - `bbox_bottom: Optional[float]`

      - `bbox_left: Optional[float]`

      - `bbox_right: Optional[float]`

      - `bbox_top: Optional[float]`

      - `bounding_box: Optional[str]`

      - `compact_markdown_table: Optional[bool]`

      - `complemental_formatting_instruction: Optional[str]`

      - `content_guideline_instruction: Optional[str]`

      - `continuous_mode: Optional[bool]`

      - `custom_metadata: Optional[Dict[str, object]]`

        The custom metadata to attach to the documents.

      - `disable_image_extraction: Optional[bool]`

      - `disable_ocr: Optional[bool]`

      - `disable_reconstruction: Optional[bool]`

      - `do_not_cache: Optional[bool]`

      - `do_not_unroll_columns: Optional[bool]`

      - `enable_cost_optimizer: Optional[bool]`

      - `extract_charts: Optional[bool]`

      - `extract_layout: Optional[bool]`

      - `extract_printed_page_number: Optional[bool]`

      - `fast_mode: Optional[bool]`

      - `formatting_instruction: Optional[str]`

      - `gpt4o_api_key: Optional[str]`

      - `gpt4o_mode: Optional[bool]`

      - `guess_xlsx_sheet_name: Optional[bool]`

      - `hide_footers: Optional[bool]`

      - `hide_headers: Optional[bool]`

      - `high_res_ocr: Optional[bool]`

      - `html_make_all_elements_visible: Optional[bool]`

      - `html_remove_fixed_elements: Optional[bool]`

      - `html_remove_navigation_elements: Optional[bool]`

      - `http_proxy: Optional[str]`

      - `ignore_document_elements_for_layout_detection: Optional[bool]`

      - `images_to_save: Optional[List[Literal["screenshot", "embedded", "layout"]]]`

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `inline_images_in_markdown: Optional[bool]`

      - `input_s3_path: Optional[str]`

      - `input_s3_region: Optional[str]`

        The region for the input S3 bucket.

      - `input_url: Optional[str]`

      - `internal_is_screenshot_job: Optional[bool]`

      - `invalidate_cache: Optional[bool]`

      - `is_formatting_instruction: Optional[bool]`

      - `job_timeout_extra_time_per_page_in_seconds: Optional[float]`

      - `job_timeout_in_seconds: Optional[float]`

      - `keep_page_separator_when_merging_tables: Optional[bool]`

      - `lang: Optional[str]`

        The language.

      - `languages: Optional[List[ParsingLanguages]]`

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

      - `layout_aware: Optional[bool]`

      - `line_level_bounding_box: Optional[bool]`

      - `markdown_table_multiline_header_separator: Optional[str]`

      - `max_pages: Optional[int]`

      - `max_pages_enforced: Optional[int]`

      - `merge_tables_across_pages_in_markdown: Optional[bool]`

      - `model: Optional[str]`

      - `outlined_table_extraction: Optional[bool]`

      - `output_pdf_of_document: Optional[bool]`

      - `output_s3_path_prefix: Optional[str]`

        If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

      - `output_s3_region: Optional[str]`

        The region for the output S3 bucket.

      - `output_tables_as_html: Optional[bool]`

      - `output_bucket: Optional[str]`

        The output bucket.

      - `page_error_tolerance: Optional[float]`

      - `page_footer_prefix: Optional[str]`

      - `page_footer_suffix: Optional[str]`

      - `page_header_prefix: Optional[str]`

      - `page_header_suffix: Optional[str]`

      - `page_prefix: Optional[str]`

      - `page_separator: Optional[str]`

      - `page_suffix: Optional[str]`

      - `parse_mode: Optional[ParsingMode]`

        Enum for representing the mode of parsing to be used.

        - `"parse_page_without_llm"`

        - `"parse_page_with_llm"`

        - `"parse_page_with_lvm"`

        - `"parse_page_with_agent"`

        - `"parse_page_with_layout_agent"`

        - `"parse_document_with_llm"`

        - `"parse_document_with_lvm"`

        - `"parse_document_with_agent"`

      - `parsing_instruction: Optional[str]`

      - `pipeline_id: Optional[str]`

        The pipeline ID.

      - `precise_bounding_box: Optional[bool]`

      - `premium_mode: Optional[bool]`

      - `presentation_out_of_bounds_content: Optional[bool]`

      - `presentation_skip_embedded_data: Optional[bool]`

      - `preserve_layout_alignment_across_pages: Optional[bool]`

      - `preserve_very_small_text: Optional[bool]`

      - `preset: Optional[str]`

      - `priority: Optional[Literal["low", "medium", "high", "critical"]]`

        The priority for the request. This field may be ignored or overwritten depending on the organization tier.

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"critical"`

      - `project_id: Optional[str]`

      - `remove_hidden_text: Optional[bool]`

      - `replace_failed_page_mode: Optional[FailPageMode]`

        Enum for representing the different available page error handling modes.

        - `"raw_text"`

        - `"blank_page"`

        - `"error_message"`

      - `replace_failed_page_with_error_message_prefix: Optional[str]`

      - `replace_failed_page_with_error_message_suffix: Optional[str]`

      - `resource_info: Optional[Dict[str, object]]`

        The resource info about the file

      - `save_images: Optional[bool]`

      - `skip_diagonal_text: Optional[bool]`

      - `specialized_chart_parsing_agentic: Optional[bool]`

      - `specialized_chart_parsing_efficient: Optional[bool]`

      - `specialized_chart_parsing_plus: Optional[bool]`

      - `specialized_image_parsing: Optional[bool]`

      - `spreadsheet_extract_sub_tables: Optional[bool]`

      - `spreadsheet_force_formula_computation: Optional[bool]`

      - `spreadsheet_include_hidden_sheets: Optional[bool]`

      - `strict_mode_buggy_font: Optional[bool]`

      - `strict_mode_image_extraction: Optional[bool]`

      - `strict_mode_image_ocr: Optional[bool]`

      - `strict_mode_reconstruction: Optional[bool]`

      - `structured_output: Optional[bool]`

      - `structured_output_json_schema: Optional[str]`

      - `structured_output_json_schema_name: Optional[str]`

      - `system_prompt: Optional[str]`

      - `system_prompt_append: Optional[str]`

      - `take_screenshot: Optional[bool]`

      - `target_pages: Optional[str]`

      - `tier: Optional[str]`

      - `type: Optional[Literal["parse"]]`

        - `"parse"`

      - `use_vendor_multimodal_model: Optional[bool]`

      - `user_prompt: Optional[str]`

      - `vendor_multimodal_api_key: Optional[str]`

      - `vendor_multimodal_model_name: Optional[str]`

      - `version: Optional[str]`

      - `webhook_configurations: Optional[Iterable[JobConfigBatchParseJobRecordCreateParametersWebhookConfiguration]]`

        Outbound webhook endpoints to notify on job status changes

        - `webhook_events: Optional[List[Literal["extract.pending", "extract.success", "extract.error", 14 more]]]`

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

        - `webhook_headers: Optional[Dict[str, str]]`

          Custom HTTP headers sent with each webhook request (e.g. auth tokens)

        - `webhook_output_format: Optional[str]`

          Response format sent to the webhook: 'string' (default) or 'json'

        - `webhook_url: Optional[str]`

          URL to receive webhook POST notifications

      - `webhook_url: Optional[str]`

    - `parent_job_execution_id: Optional[str]`

      The ID of the parent job execution.

    - `partitions: Optional[Dict[str, str]]`

      The partitions for this execution. Used for determining where to save job output.

    - `project_id: Optional[str]`

      The ID of the project this job belongs to.

    - `session_id: Optional[str]`

      The upstream request ID that created this job. Used for tracking the job across services.

    - `user_id: Optional[str]`

      The ID of the user that created this job

    - `webhook_url: Optional[str]`

      The URL that needs to be called at the end of the parsing job.

  - `class ClassifyJob: …`

    A classify job.

    - `id: str`

      Unique identifier

    - `project_id: str`

      The ID of the project

    - `rules: List[ClassifierRule]`

      The rules to classify the files

      - `description: str`

        Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

      - `type: str`

        The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

    - `status: StatusEnum`

      The status of the classify job

      - `"PENDING"`

      - `"SUCCESS"`

      - `"ERROR"`

      - `"PARTIAL_SUCCESS"`

      - `"CANCELLED"`

    - `user_id: str`

      The ID of the user

    - `created_at: Optional[datetime]`

      Creation datetime

    - `effective_at: Optional[datetime]`

    - `error_message: Optional[str]`

      Error message for the latest job attempt, if any.

    - `job_record_id: Optional[str]`

      The job record ID associated with this status, if any.

    - `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

      The classification mode to use

      - `"FAST"`

      - `"MULTIMODAL"`

    - `parsing_configuration: Optional[ClassifyParsingConfiguration]`

      The configuration for the parsing job

      - `lang: Optional[ParsingLanguages]`

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

      - `max_pages: Optional[int]`

        The maximum number of pages to parse

      - `target_pages: Optional[List[int]]`

        The pages to target for parsing (0-indexed, so first page is at 0)

    - `updated_at: Optional[datetime]`

      Update datetime

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `continue_as_new_threshold: Optional[int]`

  Maximum files to process per execution cycle in directory mode. Defaults to page_size.

- `directory_id: Optional[str]`

  ID of the directory containing files to process

- `item_ids: Optional[SequenceNotStr[str]]`

  List of specific item IDs to process. Either this or directory_id must be provided.

- `page_size: Optional[int]`

  Number of files to process per batch when using directory mode

- `temporal_namespace: Optional[str]`

### Returns

- `class BatchCreateResponse: …`

  Response schema for a batch processing job.

  - `id: str`

    Unique identifier for the batch job

  - `job_type: Literal["parse", "extract", "classify"]`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: int`

    Total number of items in the job

  - `completed_at: Optional[datetime]`

    Timestamp when job completed

  - `created_at: Optional[datetime]`

    Creation datetime

  - `directory_id: Optional[str]`

    Directory being processed

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `failed_items: Optional[int]`

    Number of items that failed processing

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `processed_items: Optional[int]`

    Number of items processed so far

  - `skipped_items: Optional[int]`

    Number of items skipped (already processed or size limit)

  - `started_at: Optional[datetime]`

    Timestamp when job processing started

  - `updated_at: Optional[datetime]`

    Update datetime

  - `workflow_id: Optional[str]`

    Async job tracking ID

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
batch = client.beta.batch.create(
    job_config={},
)
print(batch.id)
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
