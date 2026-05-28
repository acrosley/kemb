## List Pipeline Document Chunks

`pipelines.documents.get_chunks(strdocument_id, DocumentGetChunksParams**kwargs)  -> DocumentGetChunksResponse`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks`

Return a list of chunks for a pipeline document.

### Parameters

- `pipeline_id: str`

- `document_id: str`

### Returns

- `List[TextNode]`

  - `class_name: Optional[str]`

  - `embedding: Optional[List[float]]`

    Embedding of the node.

  - `end_char_idx: Optional[int]`

    End char index of the node.

  - `excluded_embed_metadata_keys: Optional[List[str]]`

    Metadata keys that are excluded from text for the embed model.

  - `excluded_llm_metadata_keys: Optional[List[str]]`

    Metadata keys that are excluded from text for the LLM.

  - `extra_info: Optional[Dict[str, object]]`

    A flat dictionary of metadata fields

  - `id: Optional[str]`

    Unique ID of the node.

  - `metadata_seperator: Optional[str]`

    Separator between metadata fields when converting to string.

  - `metadata_template: Optional[str]`

    Template for how metadata is formatted, with {key} and {value} placeholders.

  - `mimetype: Optional[str]`

    MIME type of the node content.

  - `relationships: Optional[Dict[str, Relationships]]`

    A mapping of relationships to other node information.

    - `class RelationshipsRelatedNodeInfo: …`

      - `node_id: str`

      - `class_name: Optional[str]`

      - `hash: Optional[str]`

      - `metadata: Optional[Dict[str, object]]`

      - `node_type: Optional[Union[Literal["1", "2", "3", 2 more], str, null]]`

        - `Literal["1", "2", "3", 2 more]`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `str`

    - `List[RelationshipsUnionMember1]`

      - `node_id: str`

      - `class_name: Optional[str]`

      - `hash: Optional[str]`

      - `metadata: Optional[Dict[str, object]]`

      - `node_type: Optional[Union[Literal["1", "2", "3", 2 more], str, null]]`

        - `Literal["1", "2", "3", 2 more]`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `str`

  - `start_char_idx: Optional[int]`

    Start char index of the node.

  - `text: Optional[str]`

    Text content of the node.

  - `text_template: Optional[str]`

    Template for how text is formatted, with {content} and {metadata_str} placeholders.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
text_nodes = client.pipelines.documents.get_chunks(
    document_id="document_id",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(text_nodes)
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
