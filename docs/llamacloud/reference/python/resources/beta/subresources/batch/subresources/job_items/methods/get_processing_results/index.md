## Get Item Processing Results

`beta.batch.job_items.get_processing_results(stritem_id, JobItemGetProcessingResultsParams**kwargs)  -> JobItemGetProcessingResultsResponse`

**get** `/api/v1/beta/batch-processing/items/{item_id}/processing-results`

Get all processing results for a specific item.

Returns the complete processing history for an item including
what operations were performed, parameters used, and where
outputs are stored. Optionally filter by `job_type`.

### Parameters

- `item_id: str`

- `job_type: Optional[Literal["parse", "extract", "classify"]]`

  Filter results by job type

  - `"parse"`

  - `"extract"`

  - `"classify"`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class JobItemGetProcessingResultsResponse: …`

  Response containing all processing results for an item.

  - `item_id: str`

    ID of the source item

  - `item_name: str`

    Name of the source item

  - `processing_results: Optional[List[ProcessingResult]]`

    List of all processing operations performed on this item

    - `item_id: str`

      Source item that was processed

    - `job_config: ProcessingResultJobConfig`

      Job configuration used for processing

      - `class ProcessingResultJobConfigBatchParseJobRecordCreate: …`

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

        - `parameters: Optional[ProcessingResultJobConfigBatchParseJobRecordCreateParameters]`

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

          - `webhook_configurations: Optional[List[ProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfiguration]]`

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

    - `job_type: Literal["parse", "extract", "classify"]`

      Type of processing performed

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `output_s3_path: str`

      Location of the processing output

    - `parameters_hash: str`

      Content hash of the job configuration for dedup

    - `processed_at: datetime`

      When this processing occurred

    - `result_id: str`

      Unique identifier for this result

    - `output_metadata: Optional[object]`

      Metadata about processing output.

      Currently empty - will be populated with job-type-specific metadata fields in the future.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.batch.job_items.get_processing_results(
    item_id="item_id",
)
print(response.item_id)
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
