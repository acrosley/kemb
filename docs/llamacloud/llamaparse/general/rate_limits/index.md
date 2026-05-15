---
title: Rate Limits | Developer Documentation
description: Information about LlamaCloud API rate limits.
---

LlamaCloud implements rate limiting on specific high-traffic endpoints to ensure fair usage and service stability across all customers:

| Endpoint     | QPS (Queries Per Second) | Window     | API Route                     |
| ------------ | ------------------------ | ---------- | ----------------------------- |
| File Upload  | 50                       | 5 seconds  | POST `/api/v1/files`          |
| Parse Upload | 50                       | 10 seconds | POST `/api/v1/parsing/upload` |
| Classify     | 40                       | 1 second   | POST `/api/v2/classify`       |

These rate limits are applied at different scopes as indicated above and reset at the end of each time window. File upload limits are applied per project, while Parse upload limits are applied per organization.

Free tier organizations have lower rate limits, at 20 requests per minute.

## Rate Limit Response

When you exceed the rate limit, the API will return a `429 Too Many Requests` status code. If you are consistently hitting rate limits, consider batching your requests or contact <support@runllama.ai> to discuss your usage needs.

For real-time service status and incident updates, visit the [LlamaParse Status Page](https://llamaindex.statuspage.io/).
