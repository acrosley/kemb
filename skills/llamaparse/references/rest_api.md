# LlamaParse REST API reference

Use this when the bundled `parse_document.py` script doesn't fit — for example, integrating LlamaParse into a non-Python service, batching at scale, or debugging an SDK response that looks wrong.

Base URL: `https://api.cloud.llamaindex.ai/api/v2/parse`
Auth: every request needs `Authorization: Bearer $LLAMA_CLOUD_API_KEY`.

## Lifecycle

LlamaParse is asynchronous. The full sequence is always:

1. **Upload** the file and a configuration JSON. The server queues a parse job and returns a job id.
2. **Poll** the job status until it becomes `COMPLETED` (or fails).
3. **Fetch** the parsed content by re-hitting the job endpoint with `?expand=<field>`.

There is no synchronous "parse and return" endpoint — even small files go through the same job pipeline.

## Endpoints

### Upload a file

```
POST /api/v2/parse/upload
Content-Type: multipart/form-data
```

Multipart fields:
- `file` (required) — the document binary.
- `configuration` (required) — JSON string with the parse settings. Minimum:

  ```json
  {
    "tier": "cost_effective",
    "input_options": { "language": "en" }
  }
  ```

  Common additions: `output_options.images_to_save` to save extracted images, plus `processing_options.*` for fine control. The full schema is documented at LlamaParse's API docs page.

There's also a sibling endpoint `POST /api/v2/parse` (no `/upload`) for parsing an already-uploaded file by `file_id` or a remote `source_url` — handy when files already live in LlamaCloud storage.

Response (200):
```json
{ "id": "abc123-...", "status": "PENDING" }
```

### Get job status (and result, with expand)

```
GET /api/v2/parse/{id}
GET /api/v2/parse/{id}?expand=markdown
```

By default, this endpoint returns only metadata (`id`, `status`, errors). Add `expand=` to inline the parsed content once status is `COMPLETED`. Multiple values are allowed; pass them comma-separated or repeat the param.

`expand` values:
- `text` — plain text
- `markdown` — markdown (NOT supported for `tier=fast`; will return an error)
- `items` — structured per-page items (paragraphs, tables, etc.) — also NOT supported for `tier=fast`
- `images_content_metadata` — image references and metadata
- `markdown_content_metadata`, `text_content_metadata` — per-format extraction metadata

Status transitions: `PENDING` → `RUNNING` → `COMPLETED` (or `FAILED`).

Poll with backoff. A reasonable schedule: every 1s for the first 10s, then every 5s. A typical PDF takes 5–30s; large/scanned ones can take a few minutes.

### List recent jobs

```
GET /api/v2/parse?page_size=20&status=COMPLETED
```

Useful for dashboards or auditing. Most production callers won't use this.

## Error handling

- `401` — missing or invalid API key. Check `LLAMA_CLOUD_API_KEY`.
- `400` — bad configuration JSON, or asking for `markdown` on the `fast` tier. Read the response body — the server explains the specific problem.
- `413` — file too large. Default cap is around 300MB; split the document.
- `415` — unsupported file type. Convert first or use a different parser.
- `429` — rate limited. Back off and retry.
- `5xx` — transient server issue; retry with exponential backoff.

The response body usually carries a JSON `{"detail": "..."}` describing the problem — surface it to the user verbatim rather than guessing.

## Minimal cURL example

```bash
# 1. Upload with configuration JSON.
JOB=$(curl -s -X POST https://api.cloud.llamaindex.ai/api/v2/parse/upload \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  -F "file=@./report.pdf" \
  -F 'configuration={"tier":"cost_effective","input_options":{"language":"en"}};type=application/json' \
  | jq -r .id)

# 2. Poll until COMPLETED.
while :; do
  STATUS=$(curl -s -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    "https://api.cloud.llamaindex.ai/api/v2/parse/$JOB" | jq -r .status)
  echo "status: $STATUS"
  [ "$STATUS" = "COMPLETED" ] && break
  [ "$STATUS" = "FAILED" -o "$STATUS" = "CANCELLED" ] && exit 1
  sleep 3
done

# 3. Fetch markdown via expand.
curl -s -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  "https://api.cloud.llamaindex.ai/api/v2/parse/$JOB?expand=markdown" \
  | jq -r .markdown > report.md
```
