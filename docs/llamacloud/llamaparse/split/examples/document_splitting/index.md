---
title: Splitting Concatenated Documents | Developer Documentation
description: Learn how to split a PDF containing multiple documents into separate segments using AI-powered classification.
---

This guide demonstrates how to use the Split API to automatically segment a concatenated PDF into logical document sections based on content categories.

## Use Case

When dealing with large PDFs that contain multiple distinct documents or sections (e.g., a bundle of research papers, a collection of reports), you often need to split them into individual segments. The Split API uses AI to:

1. Analyze each page’s content
2. Classify pages into user-defined categories
3. Group consecutive pages of the same category into segments

## Example Document

We’ll use a PDF containing three concatenated documents:

- **Alan Turing’s essay** “Intelligent Machinery, A Heretical Theory” (an essay)
- **ImageNet paper** (a research paper)
- **“Attention is All You Need”** paper (a research paper)

We’ll split this into segments categorized as either `essay` or `research_paper`.

📄 [Download the example PDF](https://github.com/run-llama/llama_cloud_services/blob/main/examples/split/document_splitting/data/turing%2Bimagenet%2Battention.pdf)

## Setup

Install the required packages:

- [Python](#tab-panel-207)
- [TypeScript](#tab-panel-208)

Terminal window

```
pip install llama-cloud>=1.0
```

Set up your environment (or pass your API key directly in code later):

Terminal window

```
export LLAMA_CLOUD_API_KEY="your_api_key_here"
```

Terminal window

```
npm install @llamaindex/llama-cloud
```

Set up your environment (or pass your API key directly in code later):

Terminal window

```
export LLAMA_CLOUD_API_KEY="your_api_key_here"
```

## Step 1: Upload the PDF

Upload the concatenated PDF to LlamaCloud using the `llama-cloud` SDK:

- [Python](#tab-panel-209)
- [TypeScript](#tab-panel-210)

```
from llama_cloud import LlamaCloud


client = LlamaCloud()


pdf_path = "./data/turing+imagenet+attention.pdf"


uploaded_file = client.files.create(file=pdf_path, purpose="split")


file_id = uploaded_file.id
print(f"✅ File uploaded: {uploaded_file.id}")
```

```
import fs from "fs";
import { LlamaCloud } from "@llamaindex/llama-cloud";


const client = new LlamaCloud();


const pdfPath = "./data/turing+imagenet+attention.pdf";


const uploadedFile = await client.files.create({
  file: fs.createReadStream(pdfPath),
  purpose: "split",
});


const fileId = uploadedFile.id;
console.log(`✅ File uploaded: ${uploadedFile.id}`);
```

## Step 2: Create a Split Job

Create a split job with category definitions. Each category needs a `name` and a `description` that helps the AI understand what content belongs to that category:

- [Python](#tab-panel-211)
- [TypeScript](#tab-panel-212)

```
job = client.beta.split.create(
    document_input={
        "type": "file_id",
        "value": file_id,
    },
    categories=[
        {
            "name": "essay",
            "description": "A philosophical or reflective piece of writing that presents personal viewpoints, arguments, or thoughts on a topic without strict formal structure",
        },
        {
            "name": "research_paper",
            "description": "A formal academic document presenting original research, methodology, experiments, results, and conclusions with citations and references",
        },
    ],
)


print(f"✅ Split job created: {job.id}")
print(f"   Status: {job.status}")
```

```
const job = await client.beta.split.create({
  document_input: {
    type: "file_id",
    value: fileId,
  },
  categories: [
    {
      name: "essay",
      description:
        "A philosophical or reflective piece of writing that presents personal viewpoints, arguments, or thoughts on a topic without strict formal structure",
    },
    {
      name: "research_paper",
      description:
        "A formal academic document presenting original research, methodology, experiments, results, and conclusions with citations and references",
    },
  ],
});


console.log(`✅ Split job created: ${job.id}`);
console.log(`   Status: ${job.status}`);
```

## Step 3: Poll for Completion

The split job runs asynchronously. Poll until it completes:

- [Python](#tab-panel-213)
- [TypeScript](#tab-panel-214)

```
completed_job = client.beta.split.wait_for_completion(job.id, polling_interval=2.0)
```

```
const completedJob = await client.beta.split.waitForCompletion(job.id, { pollingInterval: 2.0 });
```

## Step 4: Analyze Results

Examine the split results:

- [Python](#tab-panel-215)
- [TypeScript](#tab-panel-216)

```
segments = completed_job.result.segments if completed_job.result else []


print(f"📊 Total segments found: {len(segments)}")


for i, segment in enumerate(segments, 1):
    category = segment.category
    pages = segment.pages
    confidence = segment.confidence_category


    if len(pages) == 1:
        page_range = f"Page {pages[0]}"
    else:
        page_range = f"Pages {min(pages)}-{max(pages)}"


    print(f"\nSegment {i}:")
    print(f"   Category: {category}")
    print(f"   {page_range} ({len(pages)} pages)")
    print(f"   Confidence: {confidence}")
```

```
const segments = completedJob.result?.segments || [];


console.log(`📊 Total segments found: ${segments.length}`);


segments.forEach((segment, index) => {
  const category = segment.category;
  const pages = segment.pages;
  const confidence = segment.confidence_category;


  const pageRange =
    pages.length === 1
      ? `Page ${pages[0]}`
      : `Pages ${Math.min(...pages)}-${Math.max(...pages)}`;


  console.log(`\nSegment ${index + 1}:`);
  console.log(`   Category: ${category}`);
  console.log(`   ${pageRange} (${pages.length} pages)`);
  console.log(`   Confidence: ${confidence}`);
});
```

### Expected Output

```
📊 Total segments found: 3


Segment 1:
   Category: essay
   Pages 1-4 (4 pages)
   Confidence: high


Segment 2:
   Category: research_paper
   Pages 5-13 (9 pages)
   Confidence: high


Segment 3:
   Category: research_paper
   Pages 14-24 (11 pages)
   Confidence: high
```

The Split API correctly identified:

- **1 essay segment**: Alan Turing’s “Intelligent Machinery, A Heretical Theory”
- **2 research paper segments**: ImageNet paper and “Attention is All You Need”

## Controlling uncategorized pages

By default, pages that don’t match any defined category are grouped as `uncategorized`. You can control this with `allow_uncategorized`:

- `"include"` (default) — pages that don’t match any category will be grouped as `uncategorized` and included in results
- `"forbid"` — all pages must be assigned to a defined category
- `"omit"` — pages that don’t match any category will not appear in results

* [Python](#tab-panel-217)
* [TypeScript](#tab-panel-218)

```
# Exclude uncategorized pages from results
job = client.beta.split.create(..., splitting_strategy={"allow_uncategorized": "omit"})


# Force all pages into defined categories
job = client.beta.split.create(..., splitting_strategy={"allow_uncategorized": "forbid"})
```

```
// Exclude uncategorized pages from results
const job = await client.beta.split.create({..., splitting_strategy: { allow_uncategorized: "omit" } });


// Force all pages into defined categories
const job = await client.beta.split.create({..., splitting_strategy: { allow_uncategorized: "forbid" } });
```

## Next Steps

- Explore the [REST API reference](../../getting_started/api) for all available options
- Combine Split with [LlamaExtract](../../../llamaextract/getting_started) to run targeted extraction on each segment
- Use [LlamaParse](../../../llamaparse/getting_started) to parse individual segments with optimized settings
