---
title: Output | Developer Documentation
---

LlamaParse supports the following output formats:

- Text: A basic text representation of the parsed document
- Markdown: A [Markdown](https://en.wikipedia.org/wiki/Markdown) representation of the parsed document
- JSON : A JSON representation of the content of the document
- XLSX: A spreadsheet containing all the tables found in the document
- PDF: A PDF representation of the parsed document (note: this is not the same as the original document)
- Images: All images contained in the document. Need to set `save_images=True` on the job parameters.
- Page Screenshot: Screenshots of document pages
- Structured: if structured output is required, a JSON object containing the required data.



## Parsing modes and output

LlamaParse supports different output formats depending on the parsing mode:

| Mode                                | `text` | `markdown` | `json` | `xlsx` | `pdf` | structured [1](#user-content-fn-1) | `images` | screenshots [2](#user-content-fn-2) |
| ----------------------------------- | ------ | ---------- | ------ | ------ | ----- | ---------------------------------- | -------- | ----------------------------------- |
| default (accurate) mode             | ✅      | ✅          | ✅      | ✅      | ✅     | ✅                                  | ✅        | ✅                                   |
| fast\_mode                          | ✅      | 🚫         | ✅      | 🚫     | ✅     | 🚫                                 | ✅        | ✅                                   |
| vendor\_multimodal\_mode            | 🚫     | ✅          | ✅      | ✅      | ✅     | 🚫                                 | 🚫       | ✅                                   |
| premium\_mode                       | ✅      | ✅          | ✅      | ✅      | ✅     | 🚫                                 | ✅        | ✅                                   |
| auto\_mode                          | ✅      | ✅          | ✅      | ✅      | ✅     | 🚫                                 | ✅        | ✅                                   |
| continuous\_mode                    | ✅      | ✅          | ✅      | ✅      | ✅     | 🚫                                 | ✅        | ✅                                   |
| spreadsheet [3](#user-content-fn-3) | ✅      | ✅          | ✅      | ✅      | 🚫    | 🚫                                 | ✅        | 🚫                                  |
| audio files [4](#user-content-fn-4) | ✅      | 🚫         | 🚫     | 🚫     | 🚫    | 🚫                                 | 🚫       | 🚫                                  |



## Result endpoint

LlamaParse allows you to retrieve your job results in different ways using the result endpoint. The supported result formats are `text`, `markdown`, `json`, `xlsx`, `pdf`, or `structured`.

- [API](#tab-panel-553)

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}/result/markdown'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```

The return result is a json object containing the requested result and a `job_metadata` field. The `job_metadata` contain:

- `job_pages` : How many pages (or for spreadsheet sheets) were in your document.
- `job_auto_mode_triggered_pages` : How many pages where upgraded to `premium_mode` after triggering `auto_mode`
- `job_is_cache_hit` : If the job was a cache hit (we do not bill cache hits).

```
{
  "markdown": "Here the markdown of the document if you asked for markdown as the result type....",
  "job_metadata": {
    "job_pages": 5,
    "job_auto_mode_triggered_pages": 0,
    "job_is_cache_hit": false
  }
}
```



## Raw endpoint

Instead of returning a JSON object containing your parsed document, you can set LlamaParse to return the raw text extracted from the document by retrieving the data in “raw” mode. The raw result can be `text`, `markdown`, `json`, `xlsx`, or `structured`.

- [API](#tab-panel-554)

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}/raw/result/markdown'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```



## Images

Image (and screenshot) can be download using the `job/{job_id}/result/image/image_name.png` endpoint.

- [API](#tab-panel-555)

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}/result/image/image_name.png'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```



## Details endpoint

It is possible to see the details of a job including eventual job error or warning (both at the document and page model), but also the original job parameter using the `job/{job_id}/details` endpoint.

- [API](#tab-panel-556)

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}/details'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```



## Status endpoint

It is possible to see the status of a job using the `job/{job_id}` endpoint.

- [API](#tab-panel-557)

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```



---



## Footnotes

1. structured output is only available if `structured_output=True` [↩](#user-content-fnref-1)

2. document screenshots are available when `take_screenshot=True` [↩](#user-content-fnref-2)

3. Spreadsheets have their own pipeline and are processed differently than other documents, independently of the selected mode. [↩](#user-content-fnref-3)

4. Audio file have their own pipeline and are processed differently than other documents, independently of the selected mode. [↩](#user-content-fnref-4)
