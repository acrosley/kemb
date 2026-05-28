# Documents

## Create Batch Pipeline Documents

`pipelines.documents.create(strpipeline_id, DocumentCreateParams**kwargs)  -> DocumentCreateResponse`

**post** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create documents for a pipeline.

### Parameters

- `pipeline_id: str`

- `body: Iterable[CloudDocumentCreateParam]`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `id: Optional[str]`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `List[CloudDocument]`

  - `id: str`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: Optional[Dict[str, object]]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
cloud_documents = client.pipelines.documents.create(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    body=[{
        "metadata": {
            "foo": "bar"
        },
        "text": "text",
    }],
)
print(cloud_documents)
```

#### Response

```json
[
  {
    "id": "id",
    "metadata": {
      "foo": "bar"
    },
    "text": "text",
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ],
    "page_positions": [
      0
    ],
    "status_metadata": {
      "foo": "bar"
    }
  }
]
```

## Paginated List Pipeline Documents

`pipelines.documents.list(strpipeline_id, DocumentListParams**kwargs)  -> SyncPaginatedCloudDocuments[CloudDocument]`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `pipeline_id: str`

- `file_id: Optional[str]`

- `limit: Optional[int]`

- `only_api_data_source_documents: Optional[bool]`

- `only_direct_upload: Optional[bool]`

- `skip: Optional[int]`

- `status_refresh_policy: Optional[Literal["cached", "ttl"]]`

  - `"cached"`

  - `"ttl"`

### Returns

- `class CloudDocument: …`

  Cloud document stored in S3.

  - `id: str`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: Optional[Dict[str, object]]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.pipelines.documents.list(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
page = page.documents[0]
print(page.id)
```

#### Response

```json
{
  "documents": [
    {
      "id": "id",
      "metadata": {
        "foo": "bar"
      },
      "text": "text",
      "excluded_embed_metadata_keys": [
        "string"
      ],
      "excluded_llm_metadata_keys": [
        "string"
      ],
      "page_positions": [
        0
      ],
      "status_metadata": {
        "foo": "bar"
      }
    }
  ],
  "limit": 0,
  "offset": 0,
  "total_count": 0
}
```

## Get Pipeline Document

`pipelines.documents.get(strdocument_id, DocumentGetParams**kwargs)  -> CloudDocument`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Parameters

- `pipeline_id: str`

- `document_id: str`

### Returns

- `class CloudDocument: …`

  Cloud document stored in S3.

  - `id: str`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: Optional[Dict[str, object]]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
cloud_document = client.pipelines.documents.get(
    document_id="document_id",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(cloud_document.id)
```

#### Response

```json
{
  "id": "id",
  "metadata": {
    "foo": "bar"
  },
  "text": "text",
  "excluded_embed_metadata_keys": [
    "string"
  ],
  "excluded_llm_metadata_keys": [
    "string"
  ],
  "page_positions": [
    0
  ],
  "status_metadata": {
    "foo": "bar"
  }
}
```

## Delete Pipeline Document

`pipelines.documents.delete(strdocument_id, DocumentDeleteParams**kwargs)`

**delete** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Delete a document from a pipeline.
Initiates an async job that will:

1. Delete vectors from the vector store
1. Delete the document from MongoDB after vectors are successfully deleted

### Parameters

- `pipeline_id: str`

- `document_id: str`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.pipelines.documents.delete(
    document_id="document_id",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

## Get Pipeline Document Status

`pipelines.documents.get_status(strdocument_id, DocumentGetStatusParams**kwargs)  -> ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/status`

Return a single document for a pipeline.

### Parameters

- `pipeline_id: str`

- `document_id: str`

### Returns

- `class ManagedIngestionStatusResponse: …`

  - `status: Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", 3 more]`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date: Optional[datetime]`

    Date of the deployment.

  - `effective_at: Optional[datetime]`

    When the status is effective

  - `error: Optional[List[Error]]`

    List of errors that occurred during ingestion.

    - `job_id: str`

      ID of the job that failed.

    - `message: str`

      List of errors that occurred during ingestion.

    - `step: Literal["MANAGED_INGESTION", "DATA_SOURCE", "FILE_UPDATER", 4 more]`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id: Optional[str]`

    ID of the latest job.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
managed_ingestion_status_response = client.pipelines.documents.get_status(
    document_id="document_id",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(managed_ingestion_status_response.job_id)
```

#### Response

```json
{
  "status": "NOT_STARTED",
  "deployment_date": "2019-12-27T18:11:19.117Z",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error": [
    {
      "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "message": "message",
      "step": "MANAGED_INGESTION"
    }
  ],
  "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```

## Sync Pipeline Document

`pipelines.documents.sync(strdocument_id, DocumentSyncParams**kwargs)  -> object`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `pipeline_id: str`

- `document_id: str`

### Returns

- `object`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.pipelines.documents.sync(
    document_id="document_id",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response)
```

#### Response

```json
{}
```

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

## Upsert Batch Pipeline Documents

`pipelines.documents.upsert(strpipeline_id, DocumentUpsertParams**kwargs)  -> DocumentUpsertResponse`

**put** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create or update a document for a pipeline.

### Parameters

- `pipeline_id: str`

- `body: Iterable[CloudDocumentCreateParam]`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `id: Optional[str]`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `List[CloudDocument]`

  - `id: str`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: Optional[Dict[str, object]]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
cloud_documents = client.pipelines.documents.upsert(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    body=[{
        "metadata": {
            "foo": "bar"
        },
        "text": "text",
    }],
)
print(cloud_documents)
```

#### Response

```json
[
  {
    "id": "id",
    "metadata": {
      "foo": "bar"
    },
    "text": "text",
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ],
    "page_positions": [
      0
    ],
    "status_metadata": {
      "foo": "bar"
    }
  }
]
```

## Domain Types

### Cloud Document

- `class CloudDocument: …`

  Cloud document stored in S3.

  - `id: str`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: Optional[Dict[str, object]]`

### Cloud Document Create

- `class CloudDocumentCreate: …`

  Create a new cloud document.

  - `metadata: Dict[str, object]`

  - `text: str`

  - `id: Optional[str]`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Text Node

- `class TextNode: …`

  Provided for backward compatibility.

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

### Document Create Response

- `List[CloudDocument]`

  - `id: str`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: Optional[Dict[str, object]]`

### Document Get Chunks Response

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

### Document Upsert Response

- `List[CloudDocument]`

  - `id: str`

  - `metadata: Dict[str, object]`

  - `text: str`

  - `excluded_embed_metadata_keys: Optional[List[str]]`

  - `excluded_llm_metadata_keys: Optional[List[str]]`

  - `page_positions: Optional[List[int]]`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: Optional[Dict[str, object]]`
