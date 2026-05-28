---
title: Cache options | Developer Documentation
---



## About cache

By default LlamaParse caches parsed documents for 48 hours before permanently deleting them. The cache takes into account the parsing parameters that can have an impact on the output (such as parsing\_instructions, language, and page\_separators).



## Cache invalidation

You can invalidate the cache for a specific document by setting the `invalidate_cache` option to `True`. The cache will be cleared, the document will be re-parsed and the new parsed document will be stored in the cache.

- [Python](#tab-panel-429)
- [API](#tab-panel-430)

```
parser = LlamaParse(
  invalidate_cache=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'invalidate_cache="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Do not cache

You can specify that you do not want a specific job to be cached by setting the `do_not_cache` option to `True`. In this case the document will not be added in the cache, so if you re-upload the document it will be re-processed.

- [Python](#tab-panel-431)
- [API](#tab-panel-432)

```
parser = LlamaParse(
  do_not_cache=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'do_not_cache="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```
