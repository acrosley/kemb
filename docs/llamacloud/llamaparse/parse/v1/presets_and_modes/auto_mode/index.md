---
title: Auto Mode | Developer Documentation
---

Automatically routes each page to Balanced or Premium preset

#### Overview

Auto Mode analyzes each page individually and dynamically chooses between Balanced and Premium parsing. This allows for higher accuracy while reducing unnecessary cost.

#### Under the Hood

When `auto_mode=True` is enabled, LlamaParse first attempts to parse each page using Balanced Mode. If specific conditions are met, it will automatically reparse that page using Premium Mode for improved fidelity.

This mode enables flexibility but may result in variable and less predictable costs depending on the content of the file.

To use this mode, set `auto_mode=True`.

- [Python](#tab-panel-543)
- [API](#tab-panel-544)

```
parser = LlamaParse(
  auto_mode=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'auto_mode="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Trigger on Table

If you want to upgrade parsing to Premium when a table is detected on the page, set `auto_mode_trigger_on_table_in_page=True`.

- [Python](#tab-panel-545)
- [API](#tab-panel-546)

```
parser = LlamaParse(
  auto_mode_trigger_on_table_in_page=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'auto_mode_trigger_on_table_in_page="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Trigger on Image

If you want to upgrade parsing to Premium when images are present on a page, set `auto_mode_trigger_on_image_in_page=True`.

- [Python](#tab-panel-547)
- [API](#tab-panel-548)

```
parser = LlamaParse(
  auto_mode_trigger_on_image_in_page=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'auto_mode_trigger_on_image_in_page="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Trigger on RegExp

To trigger Premium parsing when a regular expression matches text on the page, set `auto_mode_trigger_on_regexp_in_page` to your pattern (ECMA262 format).

- [Python](#tab-panel-549)
- [API](#tab-panel-550)

```
parser = LlamaParse(
  auto_mode_trigger_on_regexp_in_page="/((total cost)|(tax))/g"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'auto_mode_trigger_on_regexp_in_page="/((total cost)|(tax))/g"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Trigger on Text

To trigger Premium parsing when specific text appears on a page, use `auto_mode_trigger_on_text_in_page`.

- [Python](#tab-panel-551)
- [API](#tab-panel-552)

```
parser = LlamaParse(
  auto_mode_trigger_on_text_in_page="total"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'auto_mode_trigger_on_text_in_page="total"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```

