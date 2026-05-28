## List Pipeline Document Chunks

`client.pipelines.documents.getChunks(stringdocumentID, DocumentGetChunksParamsparams, RequestOptionsoptions?): DocumentGetChunksResponse`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks`

Return a list of chunks for a pipeline document.

### Parameters

- `documentID: string`

- `params: DocumentGetChunksParams`

  - `pipeline_id: string`

### Returns

- `DocumentGetChunksResponse = Array<TextNode>`

  - `class_name?: string`

  - `embedding?: Array<number> | null`

    Embedding of the node.

  - `end_char_idx?: number | null`

    End char index of the node.

  - `excluded_embed_metadata_keys?: Array<string>`

    Metadata keys that are excluded from text for the embed model.

  - `excluded_llm_metadata_keys?: Array<string>`

    Metadata keys that are excluded from text for the LLM.

  - `extra_info?: Record<string, unknown>`

    A flat dictionary of metadata fields

  - `id_?: string`

    Unique ID of the node.

  - `metadata_seperator?: string`

    Separator between metadata fields when converting to string.

  - `metadata_template?: string`

    Template for how metadata is formatted, with {key} and {value} placeholders.

  - `mimetype?: string`

    MIME type of the node content.

  - `relationships?: Record<string, RelatedNodeInfo | Array<UnionMember1>>`

    A mapping of relationships to other node information.

    - `RelatedNodeInfo`

      - `node_id: string`

      - `class_name?: string`

      - `hash?: string | null`

      - `metadata?: Record<string, unknown>`

      - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

        - `"1" | "2" | "3" | 2 more`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `(string & {})`

    - `Array<UnionMember1>`

      - `node_id: string`

      - `class_name?: string`

      - `hash?: string | null`

      - `metadata?: Record<string, unknown>`

      - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

        - `"1" | "2" | "3" | 2 more`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `(string & {})`

  - `start_char_idx?: number | null`

    Start char index of the node.

  - `text?: string`

    Text content of the node.

  - `text_template?: string`

    Template for how text is formatted, with {content} and {metadata_str} placeholders.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const textNodes = await client.pipelines.documents.getChunks('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(textNodes);
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
