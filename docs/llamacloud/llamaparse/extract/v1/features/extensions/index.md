---
title: Metadata Extensions | Developer Documentation
description: Advanced extraction features including citations, reasoning, and confidence scores for enhanced data extraction workflows.
---

LlamaExtract offers several advanced features that provide additional metadata and insights alongside your extracted data. These extensions are available under `Advanced Settings` in the UI and return schema-level metadata in the `extraction_metadata` field of the response.

## Citations

Citations provide the source information for every extracted field, allowing you to trace back exactly where each piece of data came from in the original document.

**How it works**: For every leaf-level field in your schema, citations return:

- The page number where the information was found
- The verbatim text that was used to extract the field value
- Bounding box coordinates (`x`, `y`, `w`, `h`) indicating the exact location of the cited text on the page
- Page dimensions (`width`, `height`) to help you render the bounding boxes accurately

The citation information appears both in the API response (`extraction_metadata.field_metadata`) and is visualized in the LlamaCloud UI.

**Example API response structure (scalar fields):**

```
"extraction_metadata": {
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
"extraction_metadata": {
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

**Usage**: Use the `ExtractConfig.cite_sources` argument from the SDK to enable this feature.

**Use cases**:

- Compliance and audit requirements
- Fact-checking and verification workflows
- Understanding extraction quality and accuracy
- Building custom highlighting/annotation features using bounding box coordinates

**Limitations**:

- Only available for MULTIMODAL and PREMIUM extraction modes

## Reasoning

Reasoning provides explanations for the extracted values, helping you understand the logic behind each extraction decision.

**How it works**: For every top-level field in your schema, reasoning returns:

- A brief explanation for the extracted value based on the provided text
- An error message if the text doesn’t contain enough information to extract the field

**Usage**: Use the `ExtractConfig.use_reasoning` argument from the SDK to enable this feature.

**Use cases**:

- Debugging extraction results
- Understanding model decision-making
- Improving schema design based on extraction logic

**Limitations**:

- Only available for BALANCED, MULTIMODAL and PREMIUM extraction modes

## Confidence Scores (Beta)

Confidence scores provide quantitative measures of how confident the system is in the extracted values, helping you identify potentially unreliable extractions.

**How it works**: This feature adds three confidence-related fields to the extraction metadata:

- **`parsing_confidence`**: Confidence score indicating how well the relevant context was parsed from the source document. Only available for Multimodal extraction mode.
- **`extraction_confidence`**: Confidence score indicating the relevance of the extraction based on the JSON schema field.
- **`confidence`**: Combined confidence score that incorporates both parsing and extraction confidence.

**Usage**: Use the `ExtractConfig.confidence_scores` argument from the SDK to enable confidence scores.

**⚠️ Important:** Scores Are Uncalibrated. Critical understanding for proper usage:

- **Relative scale matters, not absolute values**: The confidence scores are not calibrated to real-world accuracy percentages. A score of 0.6 doesn’t mean “60% accurate” - it could indicate the model is hallucinating entirely.
- **Use for comparison, not thresholds**: Focus on relative differences between scores rather than absolute values. A field with a score of 0.9 is more reliable than one with 0.6, but neither score directly translates to accuracy.
- **Longer text fields score lower**: Summaries, descriptions, and other lengthy text fields will typically have lower confidence scores on average. This doesn’t indicate lower accuracy - it reflects that there are many valid ways to construct longer text, making the model naturally less “confident” about any specific phrasing.
- **Threshold determination is use-case specific**: The confidence score threshold for triggering human review must be determined through testing with your specific documents and use cases. What works for financial data extraction may not work for legal document processing.
- **Beta feature subject to change**: This is an experimental feature. We may modify the computation method as we gather more data, including potentially adding proper calibration in future releases.

**Limitations**:

- Currently has a 100-page size limit
- Only available for MULTIMODAL and PREMIUM extraction modes

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

- [Python](#tab-panel-400)
- [TypeScript](#tab-panel-401)
- [Python (legacy)](#tab-panel-402)

```
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="your_api_key")


file_obj = client.files.create(file="path/to/your/document.pdf", purpose="extract")
file_id = file_obj.id


result = client.extraction.extract(
    file_id=file_id,
    data_schema={
        /* your extraction schema */
    },
    config={
        "cite_sources": True,        # Enable citations
        "use_reasoning": True,       # Enable reasoning
        "confidence_scores": True,   # Enable confidence scores (MULTIMODAL/PREMIUM only)
        "extraction_mode": "MULTIMODAL"  # Required for confidence scores
    }
)
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


const result = await client.extraction.extract({
  file_id: fileObj.id,
  data_schema: {
    /* your extraction schema */
  },
  config: {
    cite_sources: true,        // Enable citations
    use_reasoning: true,       // Enable reasoning
    confidence_scores: true,   // Enable confidence scores (MULTIMODAL/PREMIUM only)
    extraction_mode: 'MULTIMODAL'  // Required for confidence scores
  }
});
```

```
from llama_cloud import ExtractConfig, ExtractMode


config = ExtractConfig(
    cite_sources=True,        # Enable citations
    use_reasoning=True,       # Enable reasoning
    confidence_scores=True,   # Enable confidence scores (MULTIMODAL/PREMIUM only)
    extraction_mode=ExtractMode.MULTIMODAL  # Required for confidence scores
)
```
