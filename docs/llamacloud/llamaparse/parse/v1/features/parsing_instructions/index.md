---
title: Parsing instructions (deprecated) | Developer Documentation
---

Parsing instruction still work by are deprecated. Use [Prompts](/llamaparse/parse/features/prompts/index.md) instead.

LlamaParse can use LLMs under the hood, allowing you to give it natural-language instructions about what it’s parsing and how to parse. This is an incredibly powerful feature!

We support 3 different types of instruction, that can be used in combination of each other (it is possible to set all 3 of them)



## content\_guideline\_instruction (deprecated)

If you want to change / transform the content with LlamaParse, you should use `content_guideline_instruction`.

- [Python](#tab-panel-501)
- [API](#tab-panel-502)

```
parser = LlamaParse(
  content_guideline_instruction="If output is not in english, translate it in english."
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form '>content_guideline_instruction="If output is not in english, translate it in english."' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## complemental\_formatting\_instruction (deprecated)

If you need to change the way LlamaParse format the output document in some way, and want to keep the markdown output formatting, you should use `complemental_formatting_instruction`. Doing so will not override our formatting system, and will allow you to improve on our formatting.

- [Python](#tab-panel-503)
- [API](#tab-panel-504)

```
parser = LlamaParse(
  complemental_formatting_instruction="For headings, do not output level 1 heading, start at level 2 (##)"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'complemental_formatting_instruction="For headings, do not output level 1 heading, start at level 2 (##)"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## formatting\_instruction (deprecated)

This allow you to override any formatting instruction done by llamaParse. If you do not want the model to output Markdown and want to output something else, use it. However be mindful that it is easy to degrade LlamaParse performances with `formating_instruction` as this override our formatting and formatting correction (like table extractions).

- [Python](#tab-panel-505)
- [API](#tab-panel-506)

```
parser = LlamaParse(
  formatting_instruction="Output the document as a Latex page. For table use HTML"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'formatting_instruction="Output the document as a Latex page. For table use HTML"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```
