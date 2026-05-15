## Get Item Processing Results

`client.beta.batch.jobItems.getProcessingResults(stringitemID, JobItemGetProcessingResultsParamsquery?, RequestOptionsoptions?): JobItemGetProcessingResultsResponse`

**get** `/api/v1/beta/batch-processing/items/{item_id}/processing-results`

Get all processing results for a specific item.

Returns the complete processing history for an item including
what operations were performed, parameters used, and where
outputs are stored. Optionally filter by `job_type`.

### Parameters

- `itemID: string`

- `query: JobItemGetProcessingResultsParams`

  - `job_type?: "parse" | "extract" | "classify" | null`

    Filter results by job type

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `JobItemGetProcessingResultsResponse`

  Response containing all processing results for an item.

  - `item_id: string`

    ID of the source item

  - `item_name: string`

    Name of the source item

  - `processing_results?: Array<ProcessingResult>`

    List of all processing operations performed on this item

    - `item_id: string`

      Source item that was processed

    - `job_config: BatchParseJobRecordCreate | ClassifyJob`

      Job configuration used for processing

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

    - `job_type: "parse" | "extract" | "classify"`

      Type of processing performed

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `output_s3_path: string`

      Location of the processing output

    - `parameters_hash: string`

      Content hash of the job configuration for dedup

    - `processed_at: string`

      When this processing occurred

    - `result_id: string`

      Unique identifier for this result

    - `output_metadata?: unknown`

      Metadata about processing output.

      Currently empty - will be populated with job-type-specific metadata fields in the future.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.batch.jobItems.getProcessingResults('item_id');

console.log(response.item_id);
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
