# Documents

## Create Batch Pipeline Documents

`$ llamacloud-prod pipelines:documents create`

**post** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create documents for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--body: array of CloudDocumentCreate`

### Returns

- `Response Create Batch Pipeline Documents Api V1 Pipelines  Pipeline Id  Documents Post: array of CloudDocument`

  - `id: string`

  - `metadata: map[unknown]`

  - `text: string`

  - `excluded_embed_metadata_keys: optional array of string`

  - `excluded_llm_metadata_keys: optional array of string`

  - `page_positions: optional array of number`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: optional map[unknown]`

### Example

```cli
llamacloud-prod pipelines:documents create \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --body '{metadata: {foo: bar}, text: text}'
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

`$ llamacloud-prod pipelines:documents list`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--file-id: optional string`

- `--limit: optional number`

- `--only-api-data-source-documents: optional boolean`

- `--only-direct-upload: optional boolean`

- `--skip: optional number`

- `--status-refresh-policy: optional "cached" or "ttl"`

### Returns

- `PaginatedListCloudDocumentsResponse: object { documents, limit, offset, total_count }`

  - `documents: array of CloudDocument`

    The documents to list

    - `id: string`

    - `metadata: map[unknown]`

    - `text: string`

    - `excluded_embed_metadata_keys: optional array of string`

    - `excluded_llm_metadata_keys: optional array of string`

    - `page_positions: optional array of number`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

    - `status_metadata: optional map[unknown]`

  - `limit: number`

    The limit of the documents

  - `offset: number`

    The offset of the documents

  - `total_count: number`

    The total number of documents

### Example

```cli
llamacloud-prod pipelines:documents list \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

`$ llamacloud-prod pipelines:documents get`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--document-id: string`

### Returns

- `cloud_document: object { id, metadata, text, 4 more }`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: map[unknown]`

  - `text: string`

  - `excluded_embed_metadata_keys: optional array of string`

  - `excluded_llm_metadata_keys: optional array of string`

  - `page_positions: optional array of number`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: optional map[unknown]`

### Example

```cli
llamacloud-prod pipelines:documents get \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --document-id document_id
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

`$ llamacloud-prod pipelines:documents delete`

**delete** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Delete a document from a pipeline.
Initiates an async job that will:

1. Delete vectors from the vector store
1. Delete the document from MongoDB after vectors are successfully deleted

### Parameters

- `--pipeline-id: string`

- `--document-id: string`

### Example

```cli
llamacloud-prod pipelines:documents delete \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --document-id document_id
```

## Get Pipeline Document Status

`$ llamacloud-prod pipelines:documents get-status`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/status`

Return a single document for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--document-id: string`

### Returns

- `managed_ingestion_status_response: object { status, deployment_date, effective_at, 2 more }`

  - `status: "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date: optional string`

    Date of the deployment.

  - `effective_at: optional string`

    When the status is effective

  - `error: optional array of object { job_id, message, step }`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" or "DATA_SOURCE" or "FILE_UPDATER" or 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id: optional string`

    ID of the latest job.

### Example

```cli
llamacloud-prod pipelines:documents get-status \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --document-id document_id
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

`$ llamacloud-prod pipelines:documents sync`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--document-id: string`

### Returns

- `PipelineDocumentSyncResponse: unknown`

### Example

```cli
llamacloud-prod pipelines:documents sync \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --document-id document_id
```

#### Response

```json
{}
```

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

## Upsert Batch Pipeline Documents

`$ llamacloud-prod pipelines:documents upsert`

**put** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create or update a document for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--body: array of CloudDocumentCreate`

### Returns

- `Response Upsert Batch Pipeline Documents Api V1 Pipelines  Pipeline Id  Documents Put: array of CloudDocument`

  - `id: string`

  - `metadata: map[unknown]`

  - `text: string`

  - `excluded_embed_metadata_keys: optional array of string`

  - `excluded_llm_metadata_keys: optional array of string`

  - `page_positions: optional array of number`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: optional map[unknown]`

### Example

```cli
llamacloud-prod pipelines:documents upsert \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --body '{metadata: {foo: bar}, text: text}'
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

- `cloud_document: object { id, metadata, text, 4 more }`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: map[unknown]`

  - `text: string`

  - `excluded_embed_metadata_keys: optional array of string`

  - `excluded_llm_metadata_keys: optional array of string`

  - `page_positions: optional array of number`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata: optional map[unknown]`

### Cloud Document Create

- `cloud_document_create: object { metadata, text, id, 3 more }`

  Create a new cloud document.

  - `metadata: map[unknown]`

  - `text: string`

  - `id: optional string`

  - `excluded_embed_metadata_keys: optional array of string`

  - `excluded_llm_metadata_keys: optional array of string`

  - `page_positions: optional array of number`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Text Node

- `text_node: object { class_name, embedding, end_char_idx, 11 more }`

  Provided for backward compatibility.

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
