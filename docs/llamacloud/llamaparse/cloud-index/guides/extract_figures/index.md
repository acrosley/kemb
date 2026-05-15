---
title: Extracting Figures from Documents | Developer Documentation
---

LlamaCloud provides several API endpoints to help you extract and work with figures (images) from your documents, including charts, tables, and other visual elements. This guide will show you how to use these endpoints effectively.

These figures can be used for a variety of purposes, such as creating visual summaries, generating reports, chatbot responses, and more.

Note

To extract figures from documents, you need to create an index with a file and enable `Extract Layout` option when creating the index on `Parse Settings -> Text and images handling -> Extract Layout`. This will allow you to extract and work with figures from your documents.

## How to Use

### App setup

- [Python](#tab-panel-69)
- [TypeScript](#tab-panel-70)

Install API client package

```
pip install llama-cloud>=1.0
```

Import and configure client

```
from llama_cloud.client import AsyncLlamaCloud, LlamaCloud


client = LlamaCloud(api_key='<llama-cloud-api-key>')
```

Install API client package

```
npm install @llamaindex/llama-cloud
```

Import and configure client

```
import { LlamaCloud } from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: 'llx-...',
});
```

### 1. List All Figures in a Document

To get a list of all figures across all pages in a document:

- [Python](#tab-panel-71)
- [TypeScript](#tab-panel-72)

```
# Get all figures from a document
figures = client.pipelines.images.list_page_figures(id="your-file-id")
```

```
const figures = await client.pipelines.images.listPageFigures("<file_id>");
```

output will look something like this:

```
[
  {
    "figure_name": "page_1_figure_1.jpg",
    "file_id": "71370e55-0f32-4977-b347-460735079386",
    "page_index": 1,
    "figure_size": 87724,
    "is_likely_noise": true,
    "confidence": 0.423
  },
  {
    "figure_name": "page_2_figure_1.jpg",
    "file_id": "71370e55-0f32-4977-b347-460735079386",
    "page_index": 2,
    "figure_size": 87724,
    "is_likely_noise": true,
    "confidence": 0.423
  },
]
```

### 2. Get a Specific Figure

To get figures from a specific page in your document:

- [Python Sync](#tab-panel-73)
- [TypeScript](#tab-panel-74)

```
# Get figures from a specific page
page_figure = client.pipelines.images.get_page_figure(
  "figure_name",
  id="file-id",
  page_index=2
)
```

```
# Get figures from a specific page
const page_figure = await client.pipelines.images.getPageFigure(
  "figure_name",
  {
    id: "file-id",
    page_index: 2
  }
)
```

This will return the binary data of the figure, which you can then save or process as needed.
