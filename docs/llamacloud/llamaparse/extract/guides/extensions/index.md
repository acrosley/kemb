---
title: Metadata Extensions | Developer Documentation
description: Advanced extraction features including citations, reasoning, and confidence scores for enhanced data extraction workflows.
---

LlamaExtract offers several advanced features that provide additional metadata and insights alongside your extracted data. These extensions are available under `Advanced Settings` in the UI and return schema-level metadata in the `extract_metadata` field of the response.

## Citations

Citations provide the source information for every extracted field, allowing you to trace back exactly where each piece of data came from in the original document.

**How it works**: For every leaf-level field in your schema, citations return:

- The page number where the information was found
- The verbatim text that was used to extract the field value
- Bounding box coordinates (`x`, `y`, `w`, `h`) indicating the exact location of the cited text on the page
- Page dimensions (`width`, `height`) to help you render the bounding boxes accurately

The citation information appears both in the API response (`extract_metadata.field_metadata`) and is visualized in the LlamaCloud UI.

**Example API response structure (scalar fields):**

```
"extract_metadata": {
  "field_metadata": {
    "phone": {
      "citation": [
        {
          "page": 1,
          "matching_text": "(555) 123-4567",
          "bounding_boxes": [
            {
              "x": 177,
              "y": 82,
              "w": 318,
              "h": 43
            }
          ],
          "page_dimensions": {
            "width": 612,
            "height": 792
          }
        }
      ]
    }
  }
}
```

**Array fields:** Citations attach at the **leaf sub-field level**, not the array item level. The `field_metadata` tree mirrors the structure of your extracted data, with each leaf value replaced by its citation metadata.

For a schema like `key_facts: list[KeyFact]` where `KeyFact` has a `fact: str` field, the metadata structure is:

```
"extract_metadata": {
  "field_metadata": {
    "key_facts": [
      {
        "fact": {
          "citation": [
            {
              "page": 3,
              "matching_text": "Revenue grew 114% year-over-year",
              "bounding_boxes": [{ "x": 50, "y": 200, "w": 400, "h": 20 }],
              "page_dimensions": { "width": 612, "height": 792 }
            }
          ]
        }
      },
      {
        "fact": {
          "citation": [
            {
              "page": 7,
              "matching_text": "Operating expenses increased to $3.2B",
              "bounding_boxes": [{ "x": 50, "y": 310, "w": 380, "h": 20 }],
              "page_dimensions": { "width": 612, "height": 792 }
            }
          ]
        }
      }
    ]
  }
}
```

Note: the citation path is `field_metadata.key_facts[i].fact.citation`, **not** `field_metadata.key_facts[i].citation`. Each array element in the metadata corresponds positionally to the same element in the extracted data.

**Usage**: Set `cite_sources: true` in the configuration to enable this feature.

**Use cases**:

- Compliance and audit requirements
- Fact-checking and verification workflows
- Understanding extraction quality and accuracy
- Building custom highlighting/annotation features using bounding box coordinates

## Confidence Scores (Beta)

Confidence scores provide quantitative measures of how confident the system is in the extracted values, helping you identify potentially unreliable extractions.

**How it works**: This feature adds three confidence-related fields to the extraction metadata:

- **`parsing_confidence`**: Confidence score indicating how well the relevant context was parsed from the source document. Available on both tiers.
- **`extraction_confidence`**: Confidence score indicating the relevance of the extraction based on the JSON schema field.
- **`confidence`**: Combined confidence score that incorporates both parsing and extraction confidence.

**Usage**: Set `confidence_scores: true` in the configuration to enable confidence scores.

**⚠️ Important:** Scores Are Uncalibrated. Critical understanding for proper usage:

- **Relative scale matters, not absolute values**: The confidence scores are not calibrated to real-world accuracy percentages. A score of 0.6 doesn’t mean “60% accurate” - it could indicate the model is hallucinating entirely.
- **Use for comparison, not thresholds**: Focus on relative differences between scores rather than absolute values. A field with a score of 0.9 is more reliable than one with 0.6, but neither score directly translates to accuracy.
- **Longer text fields score lower**: Summaries, descriptions, and other lengthy text fields will typically have lower confidence scores on average. This doesn’t indicate lower accuracy - it reflects that there are many valid ways to construct longer text, making the model naturally less “confident” about any specific phrasing.
- **Threshold determination is use-case specific**: The confidence score threshold for triggering human review must be determined through testing with your specific documents and use cases. What works for financial data extraction may not work for legal document processing.
- **Beta feature subject to change**: This is an experimental feature. We may modify the computation method as we gather more data, including potentially adding proper calibration in future releases.

**Limitations**:

- Currently has a 100-page size limit

**Use cases**:

- Quality assurance workflows (with properly tuned thresholds)
- Relative ranking of extraction reliability across fields
- Identifying documents that may need manual review (after threshold validation)

### Performance Considerations

**⚠️ Important**: Citations and confidence scores will significantly slow down extraction processing time. Enable these features only when the additional metadata is essential for your use case.

### Configuration and Usage

For complete examples of how to configure and use these extensions with both the Python SDK and REST API, see the **[Configuration Options](../options#setting-configuration-options)** page.

The configuration section includes:

- Complete Python SDK examples with extension settings
- REST API curl command examples
- Configuration reference table with all available options

**Quick reference for extensions:**

- [Python](#tab-panel-170)
- [TypeScript](#tab-panel-171)

```
import time
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="your_api_key")


file_obj = client.files.create(file="path/to/your/document.pdf", purpose="extract")
file_id = file_obj.id


job = client.extract.create(
    file_input=file_id,
    configuration={
        "data_schema": {"type": "object", "properties": {}},  # your extraction schema
        "tier": "agentic",
        "cite_sources": True,
        "confidence_scores": True,
    },
)


# Poll for completion
while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
    time.sleep(2)
    job = client.extract.get(job.id)
```

```
import fs from 'fs';
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: 'your_api_key',
});


const fileObj = await client.files.create({
  file: fs.createReadStream('path/to/your/document.pdf'),
  purpose: 'extract',
});


let job = await client.extract.create({
  file_input: fileObj.id,
  configuration: {
      data_schema: { /* your extraction schema */ },
      tier: 'agentic',
      cite_sources: true,
      confidence_scores: true,
    },
});


// Poll for completion
while (!['COMPLETED', 'FAILED', 'CANCELLED'].includes(job.status)) {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.extract.get(job.id);
}
```
