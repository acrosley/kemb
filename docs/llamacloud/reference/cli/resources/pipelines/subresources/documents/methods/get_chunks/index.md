## List Pipeline Document Chunks

`$ llamacloud-prod pipelines:documents get-chunks`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks`

Return a list of chunks for a pipeline document.

### Parameters

- `--pipeline-id: string`

- `--document-id: string`

### Returns

- `Response List Pipeline Document Chunks Api V1 Pipelines  Pipeline Id  Documents  Document Id  Chunks Get: array of TextNode`

  - `class_name: optional string`

  - `embedding: optional array of number`

    Embedding of the node.

  - `end_char_idx: optional number`

    End char index of the node.

  - `excluded_embed_metadata_keys: optional array of string`

    Metadata keys that are excluded from text for the embed model.

  - `excluded_llm_metadata_keys: optional array of string`

    Metadata keys that are excluded from text for the LLM.

  - `extra_info: optional map[unknown]`

    A flat dictionary of metadata fields

  - `id_: optional string`

    Unique ID of the node.

  - `metadata_seperator: optional string`

    Separator between metadata fields when converting to string.

  - `metadata_template: optional string`

    Template for how metadata is formatted, with {key} and {value} placeholders.

  - `mimetype: optional string`

    MIME type of the node content.

  - `relationships: optional map[object { node_id, class_name, hash, 2 more }  or array of object { node_id, class_name, hash, 2 more } ]`

    A mapping of relationships to other node information.

    - `RelatedNodeInfo: object { node_id, class_name, hash, 2 more }`

      - `node_id: string`

      - `class_name: optional string`

      - `hash: optional string`

      - `metadata: optional map[unknown]`

      - `node_type: optional "1" or "2" or "3" or 2 more or string`

        - `"1"`

        - `"2"`

        - `"3"`

        - `"4"`

        - `"5"`

    - `union_member_1: array of object { node_id, class_name, hash, 2 more }`

      - `node_id: string`

      - `class_name: optional string`

      - `hash: optional string`

      - `metadata: optional map[unknown]`

      - `node_type: optional "1" or "2" or "3" or 2 more or string`

        - `"1"`

        - `"2"`

        - `"3"`

        - `"4"`

        - `"5"`

  - `start_char_idx: optional number`

    Start char index of the node.

  - `text: optional string`

    Text content of the node.

  - `text_template: optional string`

    Template for how text is formatted, with {content} and {metadata_str} placeholders.

### Example

```cli
llamacloud-prod pipelines:documents get-chunks \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --document-id document_id
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
