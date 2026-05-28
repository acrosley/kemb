---
title: Prompts | Developer Documentation
---

LlamaParse use LLMs / LVMs under the hood, and allow you to customized / set your own prompt This is an incredibly powerful feature!

We support 3 different types of prompt, that can be used in combination of each other (it is possible to set all 3 of them)



## user\_prompt

If you want to change / transform the content with LlamaParse, you should use `user_prompt`.

- [Python](#tab-panel-507)
- [API](#tab-panel-508)

```
parser = LlamaParse(
  user_prompt="If output is not in english, translate it in english."
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form '>user_prompt="If output is not in english, translate it in english."' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## system\_prompt\_append

If you need to change the way LlamaParse format the output document in some way, and want to keep the markdown output formatting, you should use `system_prompt_append`. Doing so will not override our `system_prompt`, and will append to it instead, allowing you to improve on our formatting.

- [Python](#tab-panel-509)
- [API](#tab-panel-510)

```
parser = LlamaParse(
  system_prompt_append="For headings, do not output level 1 heading, start at level 2 (##)"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'system_prompt_append="For headings, do not output level 1 heading, start at level 2 (##)"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## system\_prompt

This allow you to override our system prompts. If you do not want the model to output Markdown and want to output something else, use it. However be mindful that it is easy to degrade LlamaParse performances with `system_prompt` as this override our system\_prompt and may impact our formatting correction (like table extractions).

- [Python](#tab-panel-511)
- [API](#tab-panel-512)

```
parser = LlamaParse(
  system_prompt="Output the document as a Latex page. For table use HTML"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'system_prompt="Output the document as a Latex page. For table use HTML"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```
