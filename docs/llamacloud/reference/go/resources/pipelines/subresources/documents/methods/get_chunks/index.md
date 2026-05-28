## List Pipeline Document Chunks

`client.Pipelines.Documents.GetChunks(ctx, documentID, query) (*[]TextNode, error)`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks`

Return a list of chunks for a pipeline document.

### Parameters

- `documentID string`

- `query PipelineDocumentGetChunksParams`

  - `PipelineID param.Field[string]`

### Returns

- `type PipelineDocumentGetChunksResponse []TextNode`

  - `ClassName string`

  - `Embedding []float64`

    Embedding of the node.

  - `EndCharIdx int64`

    End char index of the node.

  - `ExcludedEmbedMetadataKeys []string`

    Metadata keys that are excluded from text for the embed model.

  - `ExcludedLlmMetadataKeys []string`

    Metadata keys that are excluded from text for the LLM.

  - `ExtraInfo map[string, any]`

    A flat dictionary of metadata fields

  - `ID string`

    Unique ID of the node.

  - `MetadataSeperator string`

    Separator between metadata fields when converting to string.

  - `MetadataTemplate string`

    Template for how metadata is formatted, with {key} and {value} placeholders.

  - `Mimetype string`

    MIME type of the node content.

  - `Relationships map[string, TextNodeRelationshipUnion]`

    A mapping of relationships to other node information.

    - `type TextNodeRelationshipRelatedNodeInfo struct{…}`

      - `NodeID string`

      - `ClassName string`

      - `Hash string`

      - `Metadata map[string, any]`

      - `NodeType string`

        - `string`

          - `const TextNodeRelationshipRelatedNodeInfoNodeType1 TextNodeRelationshipRelatedNodeInfoNodeType = "1"`

          - `const TextNodeRelationshipRelatedNodeInfoNodeType2 TextNodeRelationshipRelatedNodeInfoNodeType = "2"`

          - `const TextNodeRelationshipRelatedNodeInfoNodeType3 TextNodeRelationshipRelatedNodeInfoNodeType = "3"`

          - `const TextNodeRelationshipRelatedNodeInfoNodeType4 TextNodeRelationshipRelatedNodeInfoNodeType = "4"`

          - `const TextNodeRelationshipRelatedNodeInfoNodeType5 TextNodeRelationshipRelatedNodeInfoNodeType = "5"`

        - `string`

    - `type TextNodeRelationshipArray []TextNodeRelationshipArrayItem`

      - `NodeID string`

      - `ClassName string`

      - `Hash string`

      - `Metadata map[string, any]`

      - `NodeType string`

        - `string`

          - `const TextNodeRelationshipArrayItemNodeType1 TextNodeRelationshipArrayItemNodeType = "1"`

          - `const TextNodeRelationshipArrayItemNodeType2 TextNodeRelationshipArrayItemNodeType = "2"`

          - `const TextNodeRelationshipArrayItemNodeType3 TextNodeRelationshipArrayItemNodeType = "3"`

          - `const TextNodeRelationshipArrayItemNodeType4 TextNodeRelationshipArrayItemNodeType = "4"`

          - `const TextNodeRelationshipArrayItemNodeType5 TextNodeRelationshipArrayItemNodeType = "5"`

        - `string`

  - `StartCharIdx int64`

    Start char index of the node.

  - `Text string`

    Text content of the node.

  - `TextTemplate string`

    Template for how text is formatted, with {content} and {metadata_str} placeholders.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  textNodes, err := client.Pipelines.Documents.GetChunks(
    context.TODO(),
    "document_id",
    llamacloudprod.PipelineDocumentGetChunksParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", textNodes)
}
```

#### Response

```json
[
  {
    "class_name": "class_name",
    "embedding": [
      0
    ],
    "end_char_idx": 0,
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ],
    "extra_info": {
      "foo": "bar"
    },
    "id_": "id_",
    "metadata_seperator": "metadata_seperator",
    "metadata_template": "metadata_template",
    "mimetype": "mimetype",
    "relationships": {
      "foo": {
        "node_id": "node_id",
        "class_name": "class_name",
        "hash": "hash",
        "metadata": {
          "foo": "bar"
        },
        "node_type": "1"
      }
    },
    "start_char_idx": 0,
    "text": "text",
    "text_template": "text_template"
  }
]
```
