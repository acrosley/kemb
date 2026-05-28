---
title: Parsing options | Developer Documentation
---

## Set language

LlamaParse uses OCR to extract text from images. Our OCR supports a [long list of languages](https://github.com/run-llama/llama_cloud_services/blob/main/py/llama_cloud_services/parse/utils.py#L54). You can specify one or more languages by separating them with a comma. This only affects text extracted from images.

- [Python](#tab-panel-461)
- [API](#tab-panel-462)

```
parser = LlamaParse(
  language="fr"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'language="fr"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Disable OCR

By default, LlamaParse runs OCR on images embedded in the document. You can disable it with `disable_ocr=True`.

- [Python](#tab-panel-463)
- [API](#tab-panel-464)

```
parser = LlamaParse(
  disable_ocr=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'disable_ocr="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Skip diagonal text

By default, LlamaParse will attempt to parse text that is diagonal on the page. This can be useful for some documents, but also introduce noise and errors. To avoid parsing diagonal text, set `skip_diagonal_text=True`.

- [Python](#tab-panel-465)
- [API](#tab-panel-466)

```
parser = LlamaParse(
  skip_diagonal_text=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'skip_diagonal_text="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Do not unroll columns

By default, LlamaParse tries to unroll columns into reading order. Set `do_not_unroll_columns=True` to prevent LlamaParse from doing so.

- [Python](#tab-panel-467)
- [API](#tab-panel-468)

```
parser = LlamaParse(
  do_not_unroll_columns=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'do_not_unroll_columns="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Target pages

By default, all pages will be extracted. To parse specific pages only, use a comma-separated string. Page numbering starts at 0.

- [Python](#tab-panel-469)
- [API](#tab-panel-470)

```
parser = LlamaParse(
  target_pages="0,2,7"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'target_pages="0,2,7"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Page separator

By default, LlamaParse will separate pages in the markdown and text output by \n---\n. You can change this separator by setting page\_separator to the desired string.

It’s also possible to include the page number within the separator using `{pageNumber}` in the string. It will be replaced by the page number of the next page.

- [Python](#tab-panel-471)
- [API](#tab-panel-472)

```
parser = LlamaParse(
  page_separator="\n=================\n",
  # page_separator="\n== {pageNumber} ==\n" # Will transform to "\n== 4 ==\n" to separate page 3 and 4.
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'page_separator="\n== {pageNumber} ==\n"' \
  --form 'page_prefix="START OF PAGE: {pageNumber}\n"' \
  --form 'page_suffix="\nEND OF PAGE: {pageNumber}"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Page prefix and suffix

It’s possible to specify a prefix or a suffix to be added to each page. These strings can contain `{pageNumber}` as well and will be replaced by the current page number. Both parameters are optional and empty by default.

- [Python](#tab-panel-473)
- [API](#tab-panel-474)

```
parser = LlamaParse(
  page_prefix="START OF PAGE: {pageNumber}\n"
  page_suffix="\nEND OF PAGE: {pageNumber}"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'page_prefix="START OF PAGE: {pageNumber}\n"
  page_suffix="\nEND OF PAGE: {pageNumber}"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Bounding box

Specify an area of a document that you want to parse. This can be helpful to remove headers and footers. To do so you need to provide the bounding box margin in clockwise order from the top in a comma-separated. The margins are expressed as a fraction of the page size, a number between 0 and 1.

Examples:

- To exclude the top 10% of a document: bounding\_box=“0.1,0,0,0”
- To exclude the top 10% and bottom 20% of a document: bounding\_box=“0.1,0,0.2,0”

* [Python](#tab-panel-475)
* [API](#tab-panel-476)

```
parser = LlamaParse(
  bounding_box="0.1,0,0.2,0"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'bounding_box="0.1,0,0.2,0"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Take screenshot

Take a screenshot of each page and add it to JSON output in the following format:

```
{
  "images": [
    {
      "name": "page_1.jpg",
      "height": 792,
      "width": 612,
      "x": 0,
      "y": 0,
      "type": "full_page_screenshot"
    }
  ]
}
```

- [Python](#tab-panel-477)
- [API](#tab-panel-478)

```
parser = LlamaParse(
  take_screenshot=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'take_screenshot="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Disable image extraction

It is possible to disable the extraction of image for better performance using `disable_image_extraction=true`

- [Python](#tab-panel-479)
- [API](#tab-panel-480)

```
parser = LlamaParse(
  disable_image_extraction=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'disable_image_extraction="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Extract multiple table per sheet in spreadsheet

By default LlamaParse extract each sheet of a spreadsheet as one table. Using `spreadsheet_extract_sub_tables=true`, LlamaParse will try to identify spreadsheet sheet with multiple table and return them as separated tables.

- [Python](#tab-panel-481)
- [API](#tab-panel-482)

```
parser = LlamaParse(
  spreadsheet_extract_sub_tables=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'spreadsheet_extract_sub_tables="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Force re-computation of cells containing formulas in spreadsheet

By default, for spreadsheet cells containing formulas, LlamaParse extracts cached (pre-computed) values if a cached cell value exists in the document. When `spreadsheet_force_formula_computation=true`, LlamaParse will re-compute values for all spreadsheet cells containing formulas.

- [Python](#tab-panel-483)
- [API](#tab-panel-484)

```
parser = LlamaParse(
  spreadsheet_force_formula_computation=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'spreadsheet_force_formula_computation="true"' \
  -F 'file=@/path/to/your/file.xlsx;type=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
```

Note that using `spreadsheet_force_formula_computation=true` will have a negative performance impact when parsing spreadsheets containing formulas.



## Output table as HTML in markdown

A common issue with markdown table is that they do not handle merged cells well. It is possible to ask LlamaParse to return table as html with `colspan` and `rowspan` to get a better representation of the table. When `output_tables_as_HTML=true`, tables present in the markdown will be output as HTML tables.

- [Python](#tab-panel-485)
- [API](#tab-panel-486)

```
parser = LlamaParse(
  output_tables_as_HTML=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'output_tables_as_HTML="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Preserve alignment across pages

If set to `preserve_layout_alignment_across_pages=True` will try to keep the text align in text mode accross pages. Useful for document with continuous table / alignment accross pages.

- [Python](#tab-panel-487)
- [API](#tab-panel-488)

```
parser = LlamaParse(
  preserve_layout_alignment_across_pages=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'preserve_layout_alignment_across_pages="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Preserve very small text

If set to `preserve_very_small_text=True`, LlamaParse will try to preserve very small text lines. This can be useful for documents containing vector graphics with very small text lines that may not be recognized by OCR or a vision model (such as in CAD drawings).

- [Python](#tab-panel-489)
- [API](#tab-panel-490)

```
parser = LlamaParse(
  preserve_very_small_text=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'preserve_very_small_text="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Hide headers

When set to true, LlamaParse will try to not output page headers in the Markdown output. The removed headers will be present in the JSON object inside the `pageHeaderMarkdown` field if needed.

LlamaParse will use different techniques to identify the headers of the page based on the chosen mode; headers will not be detected in Fast Mode.

- [Python](#tab-panel-491)
- [API](#tab-panel-492)

```
parser = LlamaParse(
  hide_headers=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'hide_headers="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Hide footers

When set to true, LlamaParse will try to not output page footers in the Markdown output. The removed footers will be present in the JSON object inside the `pageFooterMarkdown` field if needed.

LlamaParse will use different techniques to identify the footers of the page based on the chosen mode; footers will not be detected in Fast Mode.

- [Python](#tab-panel-493)
- [API](#tab-panel-494)

```
parser = LlamaParse(
  hide_footers=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'hide_footers="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Page header/footer prefix/suffix

LlamaParse allows you to prefix/suffix the headers/footers of a page’s Markdown with a string. This allows control of how headers/footers are displayed in the Markdown.

It is possible to set them using the following properties:

- `page_header_prefix` : Allows you to define the prefix to put before the page header
- `page_header_suffix` : Allows you to define the suffix to put after the page header
- `page_footer_prefix` : Allows you to define the prefix to put before page footer
- `page_footer_suffix` :Allows you to define the suffix to put after page footer

Note that headers and footers will not be detected in Fast Mode, so these parameters will have no effect.

- [Python](#tab-panel-495)
- [API](#tab-panel-496)

```
parser = LlamaParse(
  page_header_prefix="[Header]",
  page_header_suffix="[/Header]",
  page_footer_prefix="[Footer]",
  page_footer_suffix="[/Footer]"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'page_header_prefix=""[Header]"' \
  --form 'page_header_suffix=""[/Header]"' \
  --form 'page_footer_prefix=""[Footer]"' \
  --form 'page_footer_suffix=""[/Footer]"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```

With such a query the markdown for a page where header and footer are detected will look like:

```
[Header]
Journal of computer science, April 3 2025 edition
[/Header]


Some content


[Footer]
All right reserved, Corp Inc.
Page 2
[/Footer]
```



## Merge tables across pages in markdown

When set to true, LlamaParse will try to merge table across pages in the output markdown when it make sense. As a result the markdown will not be paginated, and all footer and headers will be removed.

- [Python](#tab-panel-497)
- [API](#tab-panel-498)

```
parser = LlamaParse(
  merge_tables_across_pages_in_markdown=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'merge_tables_across_pages_in_markdown="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Extract out of bounds content in presentation slides

When set to true, for supported presentation formats, LlamaParse will extract out of bounds content from slides. By default, out of bounds content is not extracted.

- [Python](#tab-panel-499)
- [API](#tab-panel-500)

```
parser = LlamaParse(
  presentation_out_of_bounds_content=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'presentation_out_of_bounds_content="true"' \
  -F 'file=@/path/to/your/file.pptx;type=application/vnd.openxmlformats-officedocument.presentationml.presentation'
```

Currently supported formats for out of bounds slide content extraction:

- `.pptx` (PowerPoint 2007+)

