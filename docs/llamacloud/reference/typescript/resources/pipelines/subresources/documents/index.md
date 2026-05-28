# Documents

## Create Batch Pipeline Documents

`client.pipelines.documents.create(stringpipelineID, DocumentCreateParamsparams, RequestOptionsoptions?): DocumentCreateResponse`

**post** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create documents for a pipeline.

### Parameters

- `pipelineID: string`

- `params: DocumentCreateParams`

  - `body: Array<CloudDocumentCreate>`

    - `metadata: Record<string, unknown>`

    - `text: string`

    - `id?: string | null`

    - `excluded_embed_metadata_keys?: Array<string>`

    - `excluded_llm_metadata_keys?: Array<string>`

    - `page_positions?: Array<number> | null`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `DocumentCreateResponse = Array<CloudDocument>`

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const cloudDocuments = await client.pipelines.documents.create(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  {
    body: [
      {
        metadata: { foo: 'bar' },
        text: 'text',
      },
    ],
  },
);

console.log(cloudDocuments);
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

`client.pipelines.documents.list(stringpipelineID, DocumentListParamsquery?, RequestOptionsoptions?): PaginatedCloudDocuments<CloudDocument>`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `pipelineID: string`

- `query: DocumentListParams`

  - `file_id?: string | null`

  - `limit?: number`

  - `only_api_data_source_documents?: boolean | null`

  - `only_direct_upload?: boolean | null`

  - `skip?: number`

  - `status_refresh_policy?: "cached" | "ttl"`

    - `"cached"`

    - `"ttl"`

### Returns

- `CloudDocument`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const cloudDocument of client.pipelines.documents.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(cloudDocument.id);
}
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

`client.pipelines.documents.get(stringdocumentID, DocumentGetParamsparams, RequestOptionsoptions?): CloudDocument`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Parameters

- `documentID: string`

- `params: DocumentGetParams`

  - `pipeline_id: string`

### Returns

- `CloudDocument`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const cloudDocument = await client.pipelines.documents.get('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(cloudDocument.id);
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

`client.pipelines.documents.delete(stringdocumentID, DocumentDeleteParamsparams, RequestOptionsoptions?): void`

**delete** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Delete a document from a pipeline.
Initiates an async job that will:

1. Delete vectors from the vector store
1. Delete the document from MongoDB after vectors are successfully deleted

### Parameters

- `documentID: string`

- `params: DocumentDeleteParams`

  - `pipeline_id: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.pipelines.documents.delete('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});
```

## Get Pipeline Document Status

`client.pipelines.documents.getStatus(stringdocumentID, DocumentGetStatusParamsparams, RequestOptionsoptions?): ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/status`

Return a single document for a pipeline.

### Parameters

- `documentID: string`

- `params: DocumentGetStatusParams`

  - `pipeline_id: string`

### Returns

- `ManagedIngestionStatusResponse`

  - `status: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date?: string | null`

    Date of the deployment.

  - `effective_at?: string | null`

    When the status is effective

  - `error?: Array<Error> | null`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" | "DATA_SOURCE" | "FILE_UPDATER" | 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id?: string | null`

    ID of the latest job.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const managedIngestionStatusResponse = await client.pipelines.documents.getStatus('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(managedIngestionStatusResponse.job_id);
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

`client.pipelines.documents.sync(stringdocumentID, DocumentSyncParamsparams, RequestOptionsoptions?): DocumentSyncResponse`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `documentID: string`

- `params: DocumentSyncParams`

  - `pipeline_id: string`

### Returns

- `DocumentSyncResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.documents.sync('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response);
```

#### Response

```json
{}
```

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

## Upsert Batch Pipeline Documents

`client.pipelines.documents.upsert(stringpipelineID, DocumentUpsertParamsparams, RequestOptionsoptions?): DocumentUpsertResponse`

**put** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create or update a document for a pipeline.

### Parameters

- `pipelineID: string`

- `params: DocumentUpsertParams`

  - `body: Array<CloudDocumentCreate>`

    - `metadata: Record<string, unknown>`

    - `text: string`

    - `id?: string | null`

    - `excluded_embed_metadata_keys?: Array<string>`

    - `excluded_llm_metadata_keys?: Array<string>`

    - `page_positions?: Array<number> | null`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `DocumentUpsertResponse = Array<CloudDocument>`

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const cloudDocuments = await client.pipelines.documents.upsert(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  {
    body: [
      {
        metadata: { foo: 'bar' },
        text: 'text',
      },
    ],
  },
);

console.log(cloudDocuments);
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

- `CloudDocument`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Cloud Document Create

- `CloudDocumentCreate`

  Create a new cloud document.

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `id?: string | null`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Text Node

- `TextNode`

  Provided for backward compatibility.

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

### Document Create Response

- `DocumentCreateResponse = Array<CloudDocument>`

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Document Sync Response

- `DocumentSyncResponse = unknown`

### Document Get Chunks Response

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

### Document Upsert Response

- `DocumentUpsertResponse = Array<CloudDocument>`

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`
