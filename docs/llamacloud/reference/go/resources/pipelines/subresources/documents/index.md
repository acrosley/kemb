# Documents

## Create Batch Pipeline Documents

`client.Pipelines.Documents.New(ctx, pipelineID, body) (*[]CloudDocument, error)`

**post** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create documents for a pipeline.

### Parameters

- `pipelineID string`

- `body PipelineDocumentNewParams`

  - `Body param.Field[[]CloudDocumentCreate]`

    - `Metadata map[string, any]`

    - `Text string`

    - `ID string`

    - `ExcludedEmbedMetadataKeys []string`

    - `ExcludedLlmMetadataKeys []string`

    - `PagePositions []int64`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `type PipelineDocumentNewResponse []CloudDocument`

  - `ID string`

  - `Metadata map[string, any]`

  - `Text string`

  - `ExcludedEmbedMetadataKeys []string`

  - `ExcludedLlmMetadataKeys []string`

  - `PagePositions []int64`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `StatusMetadata map[string, any]`

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
  cloudDocuments, err := client.Pipelines.Documents.New(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDocumentNewParams{
      Body: []llamacloudprod.CloudDocumentCreateParam{llamacloudprod.CloudDocumentCreateParam{
        Metadata: map[string]any{
        "foo": "bar",
        },
        Text: "text",
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", cloudDocuments)
}
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

`client.Pipelines.Documents.List(ctx, pipelineID, query) (*PaginatedCloudDocuments[CloudDocument], error)`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `pipelineID string`

- `query PipelineDocumentListParams`

  - `FileID param.Field[string]`

  - `Limit param.Field[int64]`

  - `OnlyAPIDataSourceDocuments param.Field[bool]`

  - `OnlyDirectUpload param.Field[bool]`

  - `Skip param.Field[int64]`

  - `StatusRefreshPolicy param.Field[PipelineDocumentListParamsStatusRefreshPolicy]`

    - `const PipelineDocumentListParamsStatusRefreshPolicyCached PipelineDocumentListParamsStatusRefreshPolicy = "cached"`

    - `const PipelineDocumentListParamsStatusRefreshPolicyTtl PipelineDocumentListParamsStatusRefreshPolicy = "ttl"`

### Returns

- `type CloudDocument struct{…}`

  Cloud document stored in S3.

  - `ID string`

  - `Metadata map[string, any]`

  - `Text string`

  - `ExcludedEmbedMetadataKeys []string`

  - `ExcludedLlmMetadataKeys []string`

  - `PagePositions []int64`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `StatusMetadata map[string, any]`

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
  page, err := client.Pipelines.Documents.List(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDocumentListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Pipelines.Documents.Get(ctx, documentID, query) (*CloudDocument, error)`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Parameters

- `documentID string`

- `query PipelineDocumentGetParams`

  - `PipelineID param.Field[string]`

### Returns

- `type CloudDocument struct{…}`

  Cloud document stored in S3.

  - `ID string`

  - `Metadata map[string, any]`

  - `Text string`

  - `ExcludedEmbedMetadataKeys []string`

  - `ExcludedLlmMetadataKeys []string`

  - `PagePositions []int64`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `StatusMetadata map[string, any]`

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
  cloudDocument, err := client.Pipelines.Documents.Get(
    context.TODO(),
    "document_id",
    llamacloudprod.PipelineDocumentGetParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", cloudDocument.ID)
}
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

`client.Pipelines.Documents.Delete(ctx, documentID, body) error`

**delete** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Delete a document from a pipeline.
Initiates an async job that will:

1. Delete vectors from the vector store
1. Delete the document from MongoDB after vectors are successfully deleted

### Parameters

- `documentID string`

- `body PipelineDocumentDeleteParams`

  - `PipelineID param.Field[string]`

### Example

```go
package main

import (
  "context"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Pipelines.Documents.Delete(
    context.TODO(),
    "document_id",
    llamacloudprod.PipelineDocumentDeleteParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

## Get Pipeline Document Status

`client.Pipelines.Documents.GetStatus(ctx, documentID, query) (*ManagedIngestionStatusResponse, error)`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/status`

Return a single document for a pipeline.

### Parameters

- `documentID string`

- `query PipelineDocumentGetStatusParams`

  - `PipelineID param.Field[string]`

### Returns

- `type ManagedIngestionStatusResponse struct{…}`

  - `Status ManagedIngestionStatusResponseStatus`

    Status of the ingestion.

    - `const ManagedIngestionStatusResponseStatusNotStarted ManagedIngestionStatusResponseStatus = "NOT_STARTED"`

    - `const ManagedIngestionStatusResponseStatusInProgress ManagedIngestionStatusResponseStatus = "IN_PROGRESS"`

    - `const ManagedIngestionStatusResponseStatusSuccess ManagedIngestionStatusResponseStatus = "SUCCESS"`

    - `const ManagedIngestionStatusResponseStatusError ManagedIngestionStatusResponseStatus = "ERROR"`

    - `const ManagedIngestionStatusResponseStatusPartialSuccess ManagedIngestionStatusResponseStatus = "PARTIAL_SUCCESS"`

    - `const ManagedIngestionStatusResponseStatusCancelled ManagedIngestionStatusResponseStatus = "CANCELLED"`

  - `DeploymentDate Time`

    Date of the deployment.

  - `EffectiveAt Time`

    When the status is effective

  - `Error []ManagedIngestionStatusResponseError`

    List of errors that occurred during ingestion.

    - `JobID string`

      ID of the job that failed.

    - `Message string`

      List of errors that occurred during ingestion.

    - `Step string`

      Name of the job that failed.

      - `const ManagedIngestionStatusResponseErrorStepManagedIngestion ManagedIngestionStatusResponseErrorStep = "MANAGED_INGESTION"`

      - `const ManagedIngestionStatusResponseErrorStepDataSource ManagedIngestionStatusResponseErrorStep = "DATA_SOURCE"`

      - `const ManagedIngestionStatusResponseErrorStepFileUpdater ManagedIngestionStatusResponseErrorStep = "FILE_UPDATER"`

      - `const ManagedIngestionStatusResponseErrorStepParse ManagedIngestionStatusResponseErrorStep = "PARSE"`

      - `const ManagedIngestionStatusResponseErrorStepTransform ManagedIngestionStatusResponseErrorStep = "TRANSFORM"`

      - `const ManagedIngestionStatusResponseErrorStepIngestion ManagedIngestionStatusResponseErrorStep = "INGESTION"`

      - `const ManagedIngestionStatusResponseErrorStepMetadataUpdate ManagedIngestionStatusResponseErrorStep = "METADATA_UPDATE"`

  - `JobID string`

    ID of the latest job.

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
  managedIngestionStatusResponse, err := client.Pipelines.Documents.GetStatus(
    context.TODO(),
    "document_id",
    llamacloudprod.PipelineDocumentGetStatusParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", managedIngestionStatusResponse.JobID)
}
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

`client.Pipelines.Documents.Sync(ctx, documentID, body) (*PipelineDocumentSyncResponse, error)`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `documentID string`

- `body PipelineDocumentSyncParams`

  - `PipelineID param.Field[string]`

### Returns

- `type PipelineDocumentSyncResponse interface{…}`

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
  response, err := client.Pipelines.Documents.Sync(
    context.TODO(),
    "document_id",
    llamacloudprod.PipelineDocumentSyncParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

#### Response

```json
{}
```

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

## Upsert Batch Pipeline Documents

`client.Pipelines.Documents.Upsert(ctx, pipelineID, body) (*[]CloudDocument, error)`

**put** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create or update a document for a pipeline.

### Parameters

- `pipelineID string`

- `body PipelineDocumentUpsertParams`

  - `Body param.Field[[]CloudDocumentCreate]`

    - `Metadata map[string, any]`

    - `Text string`

    - `ID string`

    - `ExcludedEmbedMetadataKeys []string`

    - `ExcludedLlmMetadataKeys []string`

    - `PagePositions []int64`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `type PipelineDocumentUpsertResponse []CloudDocument`

  - `ID string`

  - `Metadata map[string, any]`

  - `Text string`

  - `ExcludedEmbedMetadataKeys []string`

  - `ExcludedLlmMetadataKeys []string`

  - `PagePositions []int64`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `StatusMetadata map[string, any]`

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
  cloudDocuments, err := client.Pipelines.Documents.Upsert(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDocumentUpsertParams{
      Body: []llamacloudprod.CloudDocumentCreateParam{llamacloudprod.CloudDocumentCreateParam{
        Metadata: map[string]any{
        "foo": "bar",
        },
        Text: "text",
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", cloudDocuments)
}
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

- `type CloudDocument struct{…}`

  Cloud document stored in S3.

  - `ID string`

  - `Metadata map[string, any]`

  - `Text string`

  - `ExcludedEmbedMetadataKeys []string`

  - `ExcludedLlmMetadataKeys []string`

  - `PagePositions []int64`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `StatusMetadata map[string, any]`

### Cloud Document Create

- `type CloudDocumentCreate struct{…}`

  Create a new cloud document.

  - `Metadata map[string, any]`

  - `Text string`

  - `ID string`

  - `ExcludedEmbedMetadataKeys []string`

  - `ExcludedLlmMetadataKeys []string`

  - `PagePositions []int64`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Text Node

- `type TextNode struct{…}`

  Provided for backward compatibility.

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
