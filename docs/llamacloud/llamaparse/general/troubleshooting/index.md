---
title: Troubleshooting & Error Codes | Developer Documentation
description: Solutions for common issues and a complete error reference for LlamaParse APIs.
---

Solutions for the most common issues encountered when using LlamaParse. Error code reference tables are at the [bottom of this page](#error-reference).

## Authentication & API Keys

401 Unauthorized on every request

- Verify your API key is valid and not revoked in the [dashboard](https://cloud.llamaindex.ai).
- **HTTP API**: Check the header format: `Authorization: Bearer llx-...`
- **Python SDK**: Ensure `LLAMA_CLOUD_API_KEY` is set in your environment, or pass `api_key="llx-..."` to the client constructor.
- **TypeScript SDK**: Ensure `LLAMA_CLOUD_API_KEY` is set, or pass `apiKey: "llx-..."` to the client.
- Verify you’re hitting the correct regional API endpoint — a key created in NA won’t work against the EU API, and vice versa. See [Regions](/llamaparse/general/regions/index.md).
- API keys are project-scoped — confirm the key belongs to the project you’re targeting.

403 Forbidden when accessing a resource

- The resource belongs to a different organization or project.
- Your role may not have sufficient permissions — check with your org admin.
- Your project may have been disabled by an administrator.
- For BYOC deployments, verify your OIDC configuration (token audience, required scopes, SSL settings).

## Region & Base URL

Getting errors when using the EU region or BYOC

- **EU region**: Set the base URL to `api.cloud.eu.llamaindex.ai`. In the Python SDK: `LlamaCloud(api_key="llx-...", base_url="api.cloud.eu.llamaindex.ai")`. See [Regions](/llamaparse/general/regions/index.md).
- **BYOC**: Set the base URL to your custom deployment endpoint. Ensure your OIDC provider is configured correctly (audience, scopes, SSL).
- API keys are region-specific — a key created in NA cannot be used with the EU endpoint.

## File Upload Issues

File upload fails or times out

- Check file size against [product-specific limits](/llamaparse/general/limitations/index.md).
- Verify the file format is in the [supported types](/llamaparse/general/supported_document_types/index.md).
- Ensure the file is not empty and has a filename.
- For large files, ensure a stable network connection — uploads are not resumable.
- Check [Rate Limits](/llamaparse/general/rate_limits/index.md) for current per-endpoint limits.

File type not supported error

- Verify the file extension matches a [supported format](/llamaparse/general/supported_document_types/index.md).
- Password-protected or DRM-encrypted files cannot be processed — remove protection before uploading.
- Audio files (mp3, mp4, wav, m4a, webm) are auto-detected by extension — no special mode is needed.

## Parsing Problems

Parse job is stuck or taking too long

- Complex documents with many images take longer, especially with OCR.
- Check job status via the API or dashboard.
- If using Agentic or Agentic Plus tiers, try Cost-effective (3 credits/page) first — it still uses AI and produces markdown, but processes faster.
- Use `target_pages` (e.g., `"1,3,5-8"`) to parse only the pages you need instead of the full document.
- Disable features you don’t need (e.g., image extraction, specialized chart parsing) to speed up processing.

Poor parsing quality or missing content

- **Upgrade tier gradually**: Cost-effective (3 credits) → Agentic (10 credits) → Agentic Plus (45 credits). Each tier uses more sophisticated AI models. Note: Fast tier (1 credit) outputs spatial text only, not markdown.
- Add layout extraction (+3 credits/page) for documents with columns, complex headers, or mixed structure.
- Use parsing instructions (`parsing_instruction` in v1, or `agentic_options.system_prompt` / `user_prompt` in v2) to guide the model. This only applies to AI-powered tiers (not Fast).
- For scanned documents, ensure image quality is sufficient for OCR. You can specify OCR language via `processing_options.ocr_parameters.languages` in v2.
- Content beyond 64 KB per page is silently truncated. Only the 35 largest images per page are processed. If your document hits these limits, content will be missing without an error. See [Limitations](/llamaparse/general/limitations/index.md).

Parse job timed out

- By default, parse jobs have no explicit application-level timeout — they run until completion. You can set timeouts via `processing_control.timeouts` in v2 (max: 30 min base + 5 min per page).
- Use `target_pages` to reduce the number of pages processed.
- Use Cost-effective tier instead of Agentic/Agentic Plus for faster processing with markdown output.
- Disable unnecessary features (image extraction, chart parsing) to reduce processing time.

## Extraction Issues

Extraction returns empty or incorrect results

- Review your schema — field names and descriptions guide the model’s extraction. Be specific and unambiguous in descriptions.
- Verify your extraction target (`PER_DOC`, `PER_PAGE`, `PER_TABLE_ROW`) matches your document structure.
- If using Fast or Balanced mode, try Multimodal or Premium for visually complex documents. The default mode is Premium (highest accuracy).
- Check that the document actually contains the data you’re trying to extract.
- For pre-parsed files, extraction uses the cached parse result — if the parse quality was poor, extraction will be too.
- The root of your schema must be `type: object` with `properties`.

Schema validation error

- The schema root must be `type: object` with `properties`.
- Default values (other than null) are not supported.
- There are limits on total properties, nesting depth, character counts, and raw schema size. See [Schema Design](/llamaparse/extract/guides/schema_design/index.md) for the full list of constraints.

## Classification Issues

Documents are misclassified

- Write specific, detailed rule descriptions (10-500 characters). Precision matters more than length — include examples of what should and shouldn’t match within the description.
- Multimodal mode (2 credits/page) uses vision models on page screenshots instead of parsed text, which helps when visual layout matters. Note: Multimodal is only available in the v1 classify API.
- Ensure rule types are distinct — overlapping or vague descriptions cause ambiguity.

## Rate Limits & Throttling

Getting 429 Too Many Requests

- See [Rate Limits](/llamaparse/general/rate_limits/index.md) for current per-endpoint limits.
- Free tier organizations have a lower rate limit of 20 requests per minute.
- Implement exponential backoff with jitter in your retry logic (the API does not return `Retry-After` headers).
- For high-volume workloads, use the batch API to submit jobs in bulk rather than making many individual requests.

## Webhook Issues

Webhooks are not firing

- Webhook URLs must be publicly accessible — the platform blocks delivery to private/loopback IPs (localhost, 192.168.x.x, 10.x.x.x, etc.).
- Check that the correct events are configured for your webhook.
- Webhooks retry up to 3 times with exponential backoff (1s, then 2s delays between attempts).
- Your endpoint must respond within 30 seconds with a 2xx status code, or the delivery is treated as failed.

## Still Need Help?

- Check the [LlamaParse Status Page](https://llamaindex.statuspage.io/) for ongoing incidents.
- Review [Limitations](/llamaparse/general/limitations/index.md) for current service limits.
- Contact support at <support@runllama.ai> or through your LlamaParse dashboard.

---

## Error Reference

LlamaParse APIs return a JSON body with a `detail` field describing the error.

```
{
  "detail": "Human-readable error message"
}
```

For server errors (5xx), the response includes a correlation ID — include this when contacting support.

### Quota & Billing Errors

| Error Message                                                         | Status | Resolution                                                                                                |
| --------------------------------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------- |
| `"You've exceeded the maximum number of credits for your plan."`      | 402    | Upgrade your plan or wait for the next billing cycle. See [Billing](/llamaparse/general/billing/index.md) |
| `"No quota left to create a job"`                                     | 402    | Credits exhausted — upgrade your plan                                                                     |
| `"The total number of files would exceed the maximum allowed..."`     | 402    | Upgrade your plan for a higher file limit                                                                 |
| `"You've already reached the maximum number of projects..."`          | 429    | Plan limit reached — upgrade or delete unused projects                                                    |
| `"You've already reached the maximum number of indexes..."`           | 429    | Plan limit reached — upgrade or delete unused indexes                                                     |
| `"You've already reached the maximum number of users..."`             | 429    | Plan limit reached — upgrade or remove unused members                                                     |
| `"You've already reached the maximum number of data sources..."`      | 429    | Plan limit reached — upgrade or remove unused data sources                                                |
| `"You've already reached the maximum number of extraction agents..."` | 429    | Plan limit reached — upgrade or delete unused agents                                                      |

### File Upload Errors

| Error Message                                                              | Status | Resolution                                                                         |
| -------------------------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------- |
| `"Uploaded file is empty."`                                                | 400    | Ensure the file has content before uploading                                       |
| `"File must have a filename."`                                             | 400    | Include a filename in the multipart upload                                         |
| `"file field is required for multipart requests."`                         | 400    | Send the file in a field named `file` using `multipart/form-data`                  |
| `"Rate limit exceeded. The file upload limit is ... requests per second."` | 429    | Slow down upload rate. See [Rate Limits](/llamaparse/general/rate_limits/index.md) |

### Parse Errors

| Error Message                                                      | Status | Resolution                                                                                        |
| ------------------------------------------------------------------ | ------ | ------------------------------------------------------------------------------------------------- |
| `"Either file, input_url, or input_s3_path must be provided."`     | 400    | Provide a file, URL, or S3 path to parse                                                          |
| `"File name exceeds the maximum length of ... characters"`         | 400    | Shorten the filename                                                                              |
| `"Parsing mode ... is not supported."`                             | 400    | Use a supported parse mode. See [Pricing](/llamaparse/general/pricing/index.md) for current modes |
| `"Vendor multimodal model ... is not supported."`                  | 400    | Use a supported model — the error message lists the valid options                                 |
| `"Markdown expansion is not available for FAST tier jobs."`        | 400    | Use Cost-effective tier or higher for markdown expansion                                          |
| `"Invalid JSON in webhook_configurations: ..."`                    | 400    | Fix the JSON syntax in your webhook configuration                                                 |
| `"Access denied to this parse configuration"`                      | 403    | You don’t have access to this saved configuration                                                 |
| `"Parse job not found"`                                            | 404    | The job ID is invalid or the job has been deleted                                                 |
| `"Result not found. Check job status to see if it has completed."` | 404    | The job hasn’t finished yet — poll the job status endpoint first                                  |
| `"Source file not found in storage"`                               | 404    | The original file is no longer available (files are cached for 48 hours)                          |

**Job failure reasons** — these appear in job status rather than HTTP responses:

| Error Type              | Meaning                                  | Resolution                                                                                       |
| ----------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `UNSUPPORTED_FILE_TYPE` | File format is not supported             | Check [Supported Document Types](/llamaparse/general/supported_document_types/index.md)          |
| `PDF_IS_PROTECTED`      | The PDF is password-protected            | Remove password protection and re-upload                                                         |
| `PDF_IS_BROKEN`         | The PDF is corrupted or malformed        | Try re-exporting the PDF from the source application                                             |
| `NO_DATA_FOUND_IN_FILE` | The file contains no extractable content | Verify the file isn’t blank or image-only without OCR                                            |
| `DOCUMENT_TOO_LARGE`    | The document exceeds processing limits   | Reduce file size or use page ranges. See [Limitations](/llamaparse/general/limitations/index.md) |
| `TOO_MANY_PAGES`        | Document exceeds the maximum page count  | Use page ranges to parse specific sections                                                       |
| `TIMEOUT`               | Processing exceeded the timeout limit    | Use a faster tier, reduce page count, or split into smaller jobs                                 |

### Extract Errors

| Error Message                                                              | Status | Resolution                                                                                                          |
| -------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------- |
| `"schema_validation: ..."`                                                 | 400    | Schema exceeds limits. See [Schema Design](/llamaparse/extract/guides/schema_design/index.md) for constraints       |
| `"inputs_invalid: ..."`                                                    | 400    | Check file ID, parse job ID, or other input parameters                                                              |
| `"inputs_invalid: Parse job ... is not completed (status: ...)"`           | 400    | Wait for the parse job to complete before running extraction                                                        |
| `"File size exceeds ...MB limit."`                                         | 413    | File exceeds the Extract size limit — reduce file size. See [Limitations](/llamaparse/general/limitations/index.md) |
| `"Extraction agent name must have at least some alphanumeric characters."` | 400    | Use a name with alphanumeric characters                                                                             |
| `"Cannot delete the default extraction agent."`                            | 400    | Default agents are system-managed and cannot be deleted                                                             |
| `"Access denied to the specified file."`                                   | 403    | The file belongs to a different project                                                                             |
| `"Extraction agent ... not found or user does not have access."`           | 404    | Check the agent name and your permissions                                                                           |
| `"engine_error: ..."`                                                      | 422    | Extraction engine failure — simplify your schema or try a different mode                                            |
| `"llm_refusal"`                                                            | 422    | The LLM refused to process the content — check for content policy issues                                            |
| `"Resources exhausted. Please wait for existing jobs to complete."`        | 429    | Too many concurrent extraction jobs — wait and retry                                                                |

### Classify Errors

| Error Message                                                          | Status | Resolution                                             |
| ---------------------------------------------------------------------- | ------ | ------------------------------------------------------ |
| `"File ID ... is not in Project ID ..."`                               | 400    | Ensure the file belongs to the specified project       |
| `"Parse Job ID ... is not in Project ID ..."`                          | 400    | Ensure the parse job belongs to the specified project  |
| `"Invalid classify configuration parameters for ...: ..."`             | 400    | Fix the configuration parameters per the error details |
| `"Classify job not found"`                                             | 404    | The job ID is invalid or has been deleted              |
| `"Classify configuration ... not found"`                               | 404    | The saved configuration doesn’t exist                  |
| `"Rate limit exceeded. Maximum 40 classify job creations per second."` | 429    | Wait before creating more classify jobs                |
| `"Classify endpoints are currently unavailable."`                      | 503    | The classify service is temporarily down — retry later |

### Split Errors

| Error Message                                                      | Status | Resolution                                           |
| ------------------------------------------------------------------ | ------ | ---------------------------------------------------- |
| `"Only file_id document inputs are supported for split jobs."`     | 400    | Upload the file first, then reference it by file ID  |
| `"Unsupported file type: ... Supported file types are ..."`        | 400    | Use PDF, DOC, DOCX, PPT, or PPTX                     |
| `"File size (... MB) exceeds the maximum allowed size of ... MB."` | 400    | Reduce file size to under the limit                  |
| `"Split configuration ... has no categories"`                      | 400    | Add at least one category to the split configuration |
| `"File ... not found in project ..."`                              | 404    | Ensure the file exists in the specified project      |
| `"Split job not found"`                                            | 404    | The job ID is invalid or has been deleted            |

### Handling Errors

- Parse the `detail` field for human-readable context.
- Implement exponential backoff with jitter for `429` and `5xx` errors.
- For `402` errors, check your credit usage in the dashboard under Settings > Billing > Usage.
- For `404` errors on jobs, verify the job ID and check that the job hasn’t expired.
- Check the [Status Page](https://llamaindex.statuspage.io/) for ongoing incidents before debugging further.
- Include the correlation ID (from `500` responses) when contacting <support@runllama.ai>.

### HTTP Status Code Reference

| Status | Name                  | Description                                                                          |
| ------ | --------------------- | ------------------------------------------------------------------------------------ |
| 400    | Bad Request           | Malformed request or missing required parameters                                     |
| 401    | Unauthorized          | Missing or invalid API key                                                           |
| 402    | Payment Required      | Credit or quota limit exceeded                                                       |
| 403    | Forbidden             | Insufficient permissions for this resource                                           |
| 404    | Not Found             | Resource doesn’t exist (invalid ID or deleted)                                       |
| 409    | Conflict              | Duplicate resource or concurrent modification                                        |
| 413    | Payload Too Large     | File exceeds size limit. See [Limitations](/llamaparse/general/limitations/index.md) |
| 422    | Unprocessable Entity  | Valid request but invalid data (schema violations, bad enum values)                  |
| 429    | Too Many Requests     | Rate limit exceeded. See [Rate Limits](/llamaparse/general/rate_limits/index.md)     |
| 500    | Internal Server Error | Server issue — retry with exponential backoff                                        |
| 502    | Bad Gateway           | Backend temporarily unavailable — retry shortly                                      |
| 503    | Service Unavailable   | Service overloaded or under maintenance                                              |
| 504    | Gateway Timeout       | Backend timed out — retry shortly                                                    |
