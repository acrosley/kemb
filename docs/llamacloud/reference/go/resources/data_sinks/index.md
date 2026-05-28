# Data Sinks

## List Data Sinks

`client.DataSinks.List(ctx, query) (*[]DataSink, error)`

**get** `/api/v1/data-sinks`

List data sinks for a given project.

### Parameters

- `query DataSinkListParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type DataSinkListResponse []DataSink`

  - `ID string`

    Unique identifier

  - `Component DataSinkComponentUnion`

    Component that implements the data sink

    - `type DataSinkComponentMap map[string, any]`

    - `type CloudPineconeVectorStore struct{…}`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `APIKey string`

        The API key for authenticating with Pinecone

      - `IndexName string`

      - `ClassName string`

      - `InsertKwargs map[string, any]`

      - `Namespace string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudPineconeVectorStoreSupportsNestedMetadataFiltersTrue CloudPineconeVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudPostgresVectorStore struct{…}`

      - `Database string`

      - `EmbedDim int64`

      - `Host string`

      - `Password string`

      - `Port int64`

      - `SchemaName string`

      - `TableName string`

      - `User string`

      - `ClassName string`

      - `HnswSettings PgVectorHnswSettings`

        HNSW settings for PGVector.

        - `DistanceMethod PgVectorHnswSettingsDistanceMethod`

          The distance method to use.

          - `const PgVectorHnswSettingsDistanceMethodL2 PgVectorHnswSettingsDistanceMethod = "l2"`

          - `const PgVectorHnswSettingsDistanceMethodIP PgVectorHnswSettingsDistanceMethod = "ip"`

          - `const PgVectorHnswSettingsDistanceMethodCosine PgVectorHnswSettingsDistanceMethod = "cosine"`

          - `const PgVectorHnswSettingsDistanceMethodL1 PgVectorHnswSettingsDistanceMethod = "l1"`

          - `const PgVectorHnswSettingsDistanceMethodHamming PgVectorHnswSettingsDistanceMethod = "hamming"`

          - `const PgVectorHnswSettingsDistanceMethodJaccard PgVectorHnswSettingsDistanceMethod = "jaccard"`

        - `EfConstruction int64`

          The number of edges to use during the construction phase.

        - `EfSearch int64`

          The number of edges to use during the search phase.

        - `M int64`

          The number of bi-directional links created for each new element.

        - `VectorType PgVectorHnswSettingsVectorType`

          The type of vector to use.

          - `const PgVectorHnswSettingsVectorTypeVector PgVectorHnswSettingsVectorType = "vector"`

          - `const PgVectorHnswSettingsVectorTypeHalfVec PgVectorHnswSettingsVectorType = "half_vec"`

          - `const PgVectorHnswSettingsVectorTypeBit PgVectorHnswSettingsVectorType = "bit"`

          - `const PgVectorHnswSettingsVectorTypeSparseVec PgVectorHnswSettingsVectorType = "sparse_vec"`

      - `HybridSearch bool`

      - `PerformSetup bool`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudQdrantVectorStore struct{…}`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `APIKey string`

      - `CollectionName string`

      - `URL string`

      - `ClassName string`

      - `ClientKwargs map[string, any]`

      - `MaxRetries int64`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudQdrantVectorStoreSupportsNestedMetadataFiltersTrue CloudQdrantVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudAzureAISearchVectorStore struct{…}`

      Cloud Azure AI Search Vector Store.

      - `SearchServiceAPIKey string`

      - `SearchServiceEndpoint string`

      - `ClassName string`

      - `ClientID string`

      - `ClientSecret string`

      - `EmbeddingDimension int64`

      - `FilterableMetadataFieldKeys map[string, any]`

      - `IndexName string`

      - `SearchServiceAPIVersion string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAzureAISearchVectorStoreSupportsNestedMetadataFiltersTrue CloudAzureAISearchVectorStoreSupportsNestedMetadataFilters = true`

      - `TenantID string`

    - `type CloudMongoDBAtlasVectorSearch struct{…}`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `CollectionName string`

      - `DBName string`

      - `MongoDBUri string`

      - `ClassName string`

      - `EmbeddingDimension int64`

      - `FulltextIndexName string`

      - `SupportsNestedMetadataFilters bool`

      - `VectorIndexName string`

    - `type CloudMilvusVectorStore struct{…}`

      Cloud Milvus Vector Store.

      - `Uri string`

      - `Token string`

      - `ClassName string`

      - `CollectionName string`

      - `EmbeddingDimension int64`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudAstraDBVectorStore struct{…}`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `Token string`

        The Astra DB Application Token to use

      - `APIEndpoint string`

        The Astra DB JSON API endpoint for your database

      - `CollectionName string`

        Collection name to use. If not existing, it will be created

      - `EmbeddingDimension int64`

        Length of the embedding vectors in use

      - `ClassName string`

      - `Keyspace string`

        The keyspace to use. If not provided, 'default_keyspace'

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAstraDBVectorStoreSupportsNestedMetadataFiltersTrue CloudAstraDBVectorStoreSupportsNestedMetadataFilters = true`

  - `Name string`

    The name of the data sink.

  - `ProjectID string`

  - `SinkType DataSinkSinkType`

    - `const DataSinkSinkTypePinecone DataSinkSinkType = "PINECONE"`

    - `const DataSinkSinkTypePostgres DataSinkSinkType = "POSTGRES"`

    - `const DataSinkSinkTypeQdrant DataSinkSinkType = "QDRANT"`

    - `const DataSinkSinkTypeAzureaiSearch DataSinkSinkType = "AZUREAI_SEARCH"`

    - `const DataSinkSinkTypeMongoDBAtlas DataSinkSinkType = "MONGODB_ATLAS"`

    - `const DataSinkSinkTypeMilvus DataSinkSinkType = "MILVUS"`

    - `const DataSinkSinkTypeAstraDB DataSinkSinkType = "ASTRA_DB"`

  - `CreatedAt Time`

    Creation datetime

  - `UpdatedAt Time`

    Update datetime

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
  dataSinks, err := client.DataSinks.List(context.TODO(), llamacloudprod.DataSinkListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", dataSinks)
}
```

#### Response

```json
[
  {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  }
]
```

## Create Data Sink

`client.DataSinks.New(ctx, params) (*DataSink, error)`

**post** `/api/v1/data-sinks`

Create a new data sink.

### Parameters

- `params DataSinkNewParams`

  - `DataSinkCreate param.Field[DataSinkCreate]`

    Body param: Schema for creating a data sink.

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

### Returns

- `type DataSink struct{…}`

  Schema for a data sink.

  - `ID string`

    Unique identifier

  - `Component DataSinkComponentUnion`

    Component that implements the data sink

    - `type DataSinkComponentMap map[string, any]`

    - `type CloudPineconeVectorStore struct{…}`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `APIKey string`

        The API key for authenticating with Pinecone

      - `IndexName string`

      - `ClassName string`

      - `InsertKwargs map[string, any]`

      - `Namespace string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudPineconeVectorStoreSupportsNestedMetadataFiltersTrue CloudPineconeVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudPostgresVectorStore struct{…}`

      - `Database string`

      - `EmbedDim int64`

      - `Host string`

      - `Password string`

      - `Port int64`

      - `SchemaName string`

      - `TableName string`

      - `User string`

      - `ClassName string`

      - `HnswSettings PgVectorHnswSettings`

        HNSW settings for PGVector.

        - `DistanceMethod PgVectorHnswSettingsDistanceMethod`

          The distance method to use.

          - `const PgVectorHnswSettingsDistanceMethodL2 PgVectorHnswSettingsDistanceMethod = "l2"`

          - `const PgVectorHnswSettingsDistanceMethodIP PgVectorHnswSettingsDistanceMethod = "ip"`

          - `const PgVectorHnswSettingsDistanceMethodCosine PgVectorHnswSettingsDistanceMethod = "cosine"`

          - `const PgVectorHnswSettingsDistanceMethodL1 PgVectorHnswSettingsDistanceMethod = "l1"`

          - `const PgVectorHnswSettingsDistanceMethodHamming PgVectorHnswSettingsDistanceMethod = "hamming"`

          - `const PgVectorHnswSettingsDistanceMethodJaccard PgVectorHnswSettingsDistanceMethod = "jaccard"`

        - `EfConstruction int64`

          The number of edges to use during the construction phase.

        - `EfSearch int64`

          The number of edges to use during the search phase.

        - `M int64`

          The number of bi-directional links created for each new element.

        - `VectorType PgVectorHnswSettingsVectorType`

          The type of vector to use.

          - `const PgVectorHnswSettingsVectorTypeVector PgVectorHnswSettingsVectorType = "vector"`

          - `const PgVectorHnswSettingsVectorTypeHalfVec PgVectorHnswSettingsVectorType = "half_vec"`

          - `const PgVectorHnswSettingsVectorTypeBit PgVectorHnswSettingsVectorType = "bit"`

          - `const PgVectorHnswSettingsVectorTypeSparseVec PgVectorHnswSettingsVectorType = "sparse_vec"`

      - `HybridSearch bool`

      - `PerformSetup bool`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudQdrantVectorStore struct{…}`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `APIKey string`

      - `CollectionName string`

      - `URL string`

      - `ClassName string`

      - `ClientKwargs map[string, any]`

      - `MaxRetries int64`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudQdrantVectorStoreSupportsNestedMetadataFiltersTrue CloudQdrantVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudAzureAISearchVectorStore struct{…}`

      Cloud Azure AI Search Vector Store.

      - `SearchServiceAPIKey string`

      - `SearchServiceEndpoint string`

      - `ClassName string`

      - `ClientID string`

      - `ClientSecret string`

      - `EmbeddingDimension int64`

      - `FilterableMetadataFieldKeys map[string, any]`

      - `IndexName string`

      - `SearchServiceAPIVersion string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAzureAISearchVectorStoreSupportsNestedMetadataFiltersTrue CloudAzureAISearchVectorStoreSupportsNestedMetadataFilters = true`

      - `TenantID string`

    - `type CloudMongoDBAtlasVectorSearch struct{…}`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `CollectionName string`

      - `DBName string`

      - `MongoDBUri string`

      - `ClassName string`

      - `EmbeddingDimension int64`

      - `FulltextIndexName string`

      - `SupportsNestedMetadataFilters bool`

      - `VectorIndexName string`

    - `type CloudMilvusVectorStore struct{…}`

      Cloud Milvus Vector Store.

      - `Uri string`

      - `Token string`

      - `ClassName string`

      - `CollectionName string`

      - `EmbeddingDimension int64`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudAstraDBVectorStore struct{…}`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `Token string`

        The Astra DB Application Token to use

      - `APIEndpoint string`

        The Astra DB JSON API endpoint for your database

      - `CollectionName string`

        Collection name to use. If not existing, it will be created

      - `EmbeddingDimension int64`

        Length of the embedding vectors in use

      - `ClassName string`

      - `Keyspace string`

        The keyspace to use. If not provided, 'default_keyspace'

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAstraDBVectorStoreSupportsNestedMetadataFiltersTrue CloudAstraDBVectorStoreSupportsNestedMetadataFilters = true`

  - `Name string`

    The name of the data sink.

  - `ProjectID string`

  - `SinkType DataSinkSinkType`

    - `const DataSinkSinkTypePinecone DataSinkSinkType = "PINECONE"`

    - `const DataSinkSinkTypePostgres DataSinkSinkType = "POSTGRES"`

    - `const DataSinkSinkTypeQdrant DataSinkSinkType = "QDRANT"`

    - `const DataSinkSinkTypeAzureaiSearch DataSinkSinkType = "AZUREAI_SEARCH"`

    - `const DataSinkSinkTypeMongoDBAtlas DataSinkSinkType = "MONGODB_ATLAS"`

    - `const DataSinkSinkTypeMilvus DataSinkSinkType = "MILVUS"`

    - `const DataSinkSinkTypeAstraDB DataSinkSinkType = "ASTRA_DB"`

  - `CreatedAt Time`

    Creation datetime

  - `UpdatedAt Time`

    Update datetime

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
  dataSink, err := client.DataSinks.New(context.TODO(), llamacloudprod.DataSinkNewParams{
    DataSinkCreate: llamacloudprod.DataSinkCreateParam{
      Component: llamacloudprod.DataSinkCreateComponentUnionParam{
        OfAnyMap: map[string]any{
        "foo": "bar",
        },
      },
      Name: "name",
      SinkType: llamacloudprod.DataSinkCreateSinkTypePinecone,
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", dataSink.ID)
}
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "component": {
    "foo": "bar"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "sink_type": "PINECONE",
  "created_at": "2019-12-27T18:11:19.117Z",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Get Data Sink

`client.DataSinks.Get(ctx, dataSinkID) (*DataSink, error)`

**get** `/api/v1/data-sinks/{data_sink_id}`

Get a data sink by ID.

### Parameters

- `dataSinkID string`

### Returns

- `type DataSink struct{…}`

  Schema for a data sink.

  - `ID string`

    Unique identifier

  - `Component DataSinkComponentUnion`

    Component that implements the data sink

    - `type DataSinkComponentMap map[string, any]`

    - `type CloudPineconeVectorStore struct{…}`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `APIKey string`

        The API key for authenticating with Pinecone

      - `IndexName string`

      - `ClassName string`

      - `InsertKwargs map[string, any]`

      - `Namespace string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudPineconeVectorStoreSupportsNestedMetadataFiltersTrue CloudPineconeVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudPostgresVectorStore struct{…}`

      - `Database string`

      - `EmbedDim int64`

      - `Host string`

      - `Password string`

      - `Port int64`

      - `SchemaName string`

      - `TableName string`

      - `User string`

      - `ClassName string`

      - `HnswSettings PgVectorHnswSettings`

        HNSW settings for PGVector.

        - `DistanceMethod PgVectorHnswSettingsDistanceMethod`

          The distance method to use.

          - `const PgVectorHnswSettingsDistanceMethodL2 PgVectorHnswSettingsDistanceMethod = "l2"`

          - `const PgVectorHnswSettingsDistanceMethodIP PgVectorHnswSettingsDistanceMethod = "ip"`

          - `const PgVectorHnswSettingsDistanceMethodCosine PgVectorHnswSettingsDistanceMethod = "cosine"`

          - `const PgVectorHnswSettingsDistanceMethodL1 PgVectorHnswSettingsDistanceMethod = "l1"`

          - `const PgVectorHnswSettingsDistanceMethodHamming PgVectorHnswSettingsDistanceMethod = "hamming"`

          - `const PgVectorHnswSettingsDistanceMethodJaccard PgVectorHnswSettingsDistanceMethod = "jaccard"`

        - `EfConstruction int64`

          The number of edges to use during the construction phase.

        - `EfSearch int64`

          The number of edges to use during the search phase.

        - `M int64`

          The number of bi-directional links created for each new element.

        - `VectorType PgVectorHnswSettingsVectorType`

          The type of vector to use.

          - `const PgVectorHnswSettingsVectorTypeVector PgVectorHnswSettingsVectorType = "vector"`

          - `const PgVectorHnswSettingsVectorTypeHalfVec PgVectorHnswSettingsVectorType = "half_vec"`

          - `const PgVectorHnswSettingsVectorTypeBit PgVectorHnswSettingsVectorType = "bit"`

          - `const PgVectorHnswSettingsVectorTypeSparseVec PgVectorHnswSettingsVectorType = "sparse_vec"`

      - `HybridSearch bool`

      - `PerformSetup bool`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudQdrantVectorStore struct{…}`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `APIKey string`

      - `CollectionName string`

      - `URL string`

      - `ClassName string`

      - `ClientKwargs map[string, any]`

      - `MaxRetries int64`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudQdrantVectorStoreSupportsNestedMetadataFiltersTrue CloudQdrantVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudAzureAISearchVectorStore struct{…}`

      Cloud Azure AI Search Vector Store.

      - `SearchServiceAPIKey string`

      - `SearchServiceEndpoint string`

      - `ClassName string`

      - `ClientID string`

      - `ClientSecret string`

      - `EmbeddingDimension int64`

      - `FilterableMetadataFieldKeys map[string, any]`

      - `IndexName string`

      - `SearchServiceAPIVersion string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAzureAISearchVectorStoreSupportsNestedMetadataFiltersTrue CloudAzureAISearchVectorStoreSupportsNestedMetadataFilters = true`

      - `TenantID string`

    - `type CloudMongoDBAtlasVectorSearch struct{…}`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `CollectionName string`

      - `DBName string`

      - `MongoDBUri string`

      - `ClassName string`

      - `EmbeddingDimension int64`

      - `FulltextIndexName string`

      - `SupportsNestedMetadataFilters bool`

      - `VectorIndexName string`

    - `type CloudMilvusVectorStore struct{…}`

      Cloud Milvus Vector Store.

      - `Uri string`

      - `Token string`

      - `ClassName string`

      - `CollectionName string`

      - `EmbeddingDimension int64`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudAstraDBVectorStore struct{…}`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `Token string`

        The Astra DB Application Token to use

      - `APIEndpoint string`

        The Astra DB JSON API endpoint for your database

      - `CollectionName string`

        Collection name to use. If not existing, it will be created

      - `EmbeddingDimension int64`

        Length of the embedding vectors in use

      - `ClassName string`

      - `Keyspace string`

        The keyspace to use. If not provided, 'default_keyspace'

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAstraDBVectorStoreSupportsNestedMetadataFiltersTrue CloudAstraDBVectorStoreSupportsNestedMetadataFilters = true`

  - `Name string`

    The name of the data sink.

  - `ProjectID string`

  - `SinkType DataSinkSinkType`

    - `const DataSinkSinkTypePinecone DataSinkSinkType = "PINECONE"`

    - `const DataSinkSinkTypePostgres DataSinkSinkType = "POSTGRES"`

    - `const DataSinkSinkTypeQdrant DataSinkSinkType = "QDRANT"`

    - `const DataSinkSinkTypeAzureaiSearch DataSinkSinkType = "AZUREAI_SEARCH"`

    - `const DataSinkSinkTypeMongoDBAtlas DataSinkSinkType = "MONGODB_ATLAS"`

    - `const DataSinkSinkTypeMilvus DataSinkSinkType = "MILVUS"`

    - `const DataSinkSinkTypeAstraDB DataSinkSinkType = "ASTRA_DB"`

  - `CreatedAt Time`

    Creation datetime

  - `UpdatedAt Time`

    Update datetime

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
  dataSink, err := client.DataSinks.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", dataSink.ID)
}
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "component": {
    "foo": "bar"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "sink_type": "PINECONE",
  "created_at": "2019-12-27T18:11:19.117Z",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Data Sink

`client.DataSinks.Update(ctx, dataSinkID, body) (*DataSink, error)`

**put** `/api/v1/data-sinks/{data_sink_id}`

Update a data sink by ID.

### Parameters

- `dataSinkID string`

- `body DataSinkUpdateParams`

  - `SinkType param.Field[DataSinkUpdateParamsSinkType]`

    - `const DataSinkUpdateParamsSinkTypePinecone DataSinkUpdateParamsSinkType = "PINECONE"`

    - `const DataSinkUpdateParamsSinkTypePostgres DataSinkUpdateParamsSinkType = "POSTGRES"`

    - `const DataSinkUpdateParamsSinkTypeQdrant DataSinkUpdateParamsSinkType = "QDRANT"`

    - `const DataSinkUpdateParamsSinkTypeAzureaiSearch DataSinkUpdateParamsSinkType = "AZUREAI_SEARCH"`

    - `const DataSinkUpdateParamsSinkTypeMongoDBAtlas DataSinkUpdateParamsSinkType = "MONGODB_ATLAS"`

    - `const DataSinkUpdateParamsSinkTypeMilvus DataSinkUpdateParamsSinkType = "MILVUS"`

    - `const DataSinkUpdateParamsSinkTypeAstraDB DataSinkUpdateParamsSinkType = "ASTRA_DB"`

  - `Component param.Field[DataSinkUpdateParamsComponentUnion]`

    Component that implements the data sink

    - `type DataSinkUpdateParamsComponentMap map[string, any]`

    - `type CloudPineconeVectorStore struct{…}`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `APIKey string`

        The API key for authenticating with Pinecone

      - `IndexName string`

      - `ClassName string`

      - `InsertKwargs map[string, any]`

      - `Namespace string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudPineconeVectorStoreSupportsNestedMetadataFiltersTrue CloudPineconeVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudPostgresVectorStore struct{…}`

      - `Database string`

      - `EmbedDim int64`

      - `Host string`

      - `Password string`

      - `Port int64`

      - `SchemaName string`

      - `TableName string`

      - `User string`

      - `ClassName string`

      - `HnswSettings PgVectorHnswSettings`

        HNSW settings for PGVector.

        - `DistanceMethod PgVectorHnswSettingsDistanceMethod`

          The distance method to use.

          - `const PgVectorHnswSettingsDistanceMethodL2 PgVectorHnswSettingsDistanceMethod = "l2"`

          - `const PgVectorHnswSettingsDistanceMethodIP PgVectorHnswSettingsDistanceMethod = "ip"`

          - `const PgVectorHnswSettingsDistanceMethodCosine PgVectorHnswSettingsDistanceMethod = "cosine"`

          - `const PgVectorHnswSettingsDistanceMethodL1 PgVectorHnswSettingsDistanceMethod = "l1"`

          - `const PgVectorHnswSettingsDistanceMethodHamming PgVectorHnswSettingsDistanceMethod = "hamming"`

          - `const PgVectorHnswSettingsDistanceMethodJaccard PgVectorHnswSettingsDistanceMethod = "jaccard"`

        - `EfConstruction int64`

          The number of edges to use during the construction phase.

        - `EfSearch int64`

          The number of edges to use during the search phase.

        - `M int64`

          The number of bi-directional links created for each new element.

        - `VectorType PgVectorHnswSettingsVectorType`

          The type of vector to use.

          - `const PgVectorHnswSettingsVectorTypeVector PgVectorHnswSettingsVectorType = "vector"`

          - `const PgVectorHnswSettingsVectorTypeHalfVec PgVectorHnswSettingsVectorType = "half_vec"`

          - `const PgVectorHnswSettingsVectorTypeBit PgVectorHnswSettingsVectorType = "bit"`

          - `const PgVectorHnswSettingsVectorTypeSparseVec PgVectorHnswSettingsVectorType = "sparse_vec"`

      - `HybridSearch bool`

      - `PerformSetup bool`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudQdrantVectorStore struct{…}`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `APIKey string`

      - `CollectionName string`

      - `URL string`

      - `ClassName string`

      - `ClientKwargs map[string, any]`

      - `MaxRetries int64`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudQdrantVectorStoreSupportsNestedMetadataFiltersTrue CloudQdrantVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudAzureAISearchVectorStore struct{…}`

      Cloud Azure AI Search Vector Store.

      - `SearchServiceAPIKey string`

      - `SearchServiceEndpoint string`

      - `ClassName string`

      - `ClientID string`

      - `ClientSecret string`

      - `EmbeddingDimension int64`

      - `FilterableMetadataFieldKeys map[string, any]`

      - `IndexName string`

      - `SearchServiceAPIVersion string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAzureAISearchVectorStoreSupportsNestedMetadataFiltersTrue CloudAzureAISearchVectorStoreSupportsNestedMetadataFilters = true`

      - `TenantID string`

    - `type CloudMongoDBAtlasVectorSearch struct{…}`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `CollectionName string`

      - `DBName string`

      - `MongoDBUri string`

      - `ClassName string`

      - `EmbeddingDimension int64`

      - `FulltextIndexName string`

      - `SupportsNestedMetadataFilters bool`

      - `VectorIndexName string`

    - `type CloudMilvusVectorStore struct{…}`

      Cloud Milvus Vector Store.

      - `Uri string`

      - `Token string`

      - `ClassName string`

      - `CollectionName string`

      - `EmbeddingDimension int64`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudAstraDBVectorStore struct{…}`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `Token string`

        The Astra DB Application Token to use

      - `APIEndpoint string`

        The Astra DB JSON API endpoint for your database

      - `CollectionName string`

        Collection name to use. If not existing, it will be created

      - `EmbeddingDimension int64`

        Length of the embedding vectors in use

      - `ClassName string`

      - `Keyspace string`

        The keyspace to use. If not provided, 'default_keyspace'

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAstraDBVectorStoreSupportsNestedMetadataFiltersTrue CloudAstraDBVectorStoreSupportsNestedMetadataFilters = true`

  - `Name param.Field[string]`

    The name of the data sink.

### Returns

- `type DataSink struct{…}`

  Schema for a data sink.

  - `ID string`

    Unique identifier

  - `Component DataSinkComponentUnion`

    Component that implements the data sink

    - `type DataSinkComponentMap map[string, any]`

    - `type CloudPineconeVectorStore struct{…}`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `APIKey string`

        The API key for authenticating with Pinecone

      - `IndexName string`

      - `ClassName string`

      - `InsertKwargs map[string, any]`

      - `Namespace string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudPineconeVectorStoreSupportsNestedMetadataFiltersTrue CloudPineconeVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudPostgresVectorStore struct{…}`

      - `Database string`

      - `EmbedDim int64`

      - `Host string`

      - `Password string`

      - `Port int64`

      - `SchemaName string`

      - `TableName string`

      - `User string`

      - `ClassName string`

      - `HnswSettings PgVectorHnswSettings`

        HNSW settings for PGVector.

        - `DistanceMethod PgVectorHnswSettingsDistanceMethod`

          The distance method to use.

          - `const PgVectorHnswSettingsDistanceMethodL2 PgVectorHnswSettingsDistanceMethod = "l2"`

          - `const PgVectorHnswSettingsDistanceMethodIP PgVectorHnswSettingsDistanceMethod = "ip"`

          - `const PgVectorHnswSettingsDistanceMethodCosine PgVectorHnswSettingsDistanceMethod = "cosine"`

          - `const PgVectorHnswSettingsDistanceMethodL1 PgVectorHnswSettingsDistanceMethod = "l1"`

          - `const PgVectorHnswSettingsDistanceMethodHamming PgVectorHnswSettingsDistanceMethod = "hamming"`

          - `const PgVectorHnswSettingsDistanceMethodJaccard PgVectorHnswSettingsDistanceMethod = "jaccard"`

        - `EfConstruction int64`

          The number of edges to use during the construction phase.

        - `EfSearch int64`

          The number of edges to use during the search phase.

        - `M int64`

          The number of bi-directional links created for each new element.

        - `VectorType PgVectorHnswSettingsVectorType`

          The type of vector to use.

          - `const PgVectorHnswSettingsVectorTypeVector PgVectorHnswSettingsVectorType = "vector"`

          - `const PgVectorHnswSettingsVectorTypeHalfVec PgVectorHnswSettingsVectorType = "half_vec"`

          - `const PgVectorHnswSettingsVectorTypeBit PgVectorHnswSettingsVectorType = "bit"`

          - `const PgVectorHnswSettingsVectorTypeSparseVec PgVectorHnswSettingsVectorType = "sparse_vec"`

      - `HybridSearch bool`

      - `PerformSetup bool`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudQdrantVectorStore struct{…}`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `APIKey string`

      - `CollectionName string`

      - `URL string`

      - `ClassName string`

      - `ClientKwargs map[string, any]`

      - `MaxRetries int64`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudQdrantVectorStoreSupportsNestedMetadataFiltersTrue CloudQdrantVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudAzureAISearchVectorStore struct{…}`

      Cloud Azure AI Search Vector Store.

      - `SearchServiceAPIKey string`

      - `SearchServiceEndpoint string`

      - `ClassName string`

      - `ClientID string`

      - `ClientSecret string`

      - `EmbeddingDimension int64`

      - `FilterableMetadataFieldKeys map[string, any]`

      - `IndexName string`

      - `SearchServiceAPIVersion string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAzureAISearchVectorStoreSupportsNestedMetadataFiltersTrue CloudAzureAISearchVectorStoreSupportsNestedMetadataFilters = true`

      - `TenantID string`

    - `type CloudMongoDBAtlasVectorSearch struct{…}`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `CollectionName string`

      - `DBName string`

      - `MongoDBUri string`

      - `ClassName string`

      - `EmbeddingDimension int64`

      - `FulltextIndexName string`

      - `SupportsNestedMetadataFilters bool`

      - `VectorIndexName string`

    - `type CloudMilvusVectorStore struct{…}`

      Cloud Milvus Vector Store.

      - `Uri string`

      - `Token string`

      - `ClassName string`

      - `CollectionName string`

      - `EmbeddingDimension int64`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudAstraDBVectorStore struct{…}`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `Token string`

        The Astra DB Application Token to use

      - `APIEndpoint string`

        The Astra DB JSON API endpoint for your database

      - `CollectionName string`

        Collection name to use. If not existing, it will be created

      - `EmbeddingDimension int64`

        Length of the embedding vectors in use

      - `ClassName string`

      - `Keyspace string`

        The keyspace to use. If not provided, 'default_keyspace'

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAstraDBVectorStoreSupportsNestedMetadataFiltersTrue CloudAstraDBVectorStoreSupportsNestedMetadataFilters = true`

  - `Name string`

    The name of the data sink.

  - `ProjectID string`

  - `SinkType DataSinkSinkType`

    - `const DataSinkSinkTypePinecone DataSinkSinkType = "PINECONE"`

    - `const DataSinkSinkTypePostgres DataSinkSinkType = "POSTGRES"`

    - `const DataSinkSinkTypeQdrant DataSinkSinkType = "QDRANT"`

    - `const DataSinkSinkTypeAzureaiSearch DataSinkSinkType = "AZUREAI_SEARCH"`

    - `const DataSinkSinkTypeMongoDBAtlas DataSinkSinkType = "MONGODB_ATLAS"`

    - `const DataSinkSinkTypeMilvus DataSinkSinkType = "MILVUS"`

    - `const DataSinkSinkTypeAstraDB DataSinkSinkType = "ASTRA_DB"`

  - `CreatedAt Time`

    Creation datetime

  - `UpdatedAt Time`

    Update datetime

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
  dataSink, err := client.DataSinks.Update(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.DataSinkUpdateParams{
      SinkType: llamacloudprod.DataSinkUpdateParamsSinkTypePinecone,
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", dataSink.ID)
}
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "component": {
    "foo": "bar"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "sink_type": "PINECONE",
  "created_at": "2019-12-27T18:11:19.117Z",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Data Sink

`client.DataSinks.Delete(ctx, dataSinkID) error`

**delete** `/api/v1/data-sinks/{data_sink_id}`

Delete a data sink by ID.

### Parameters

- `dataSinkID string`

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
  err := client.DataSinks.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
  if err != nil {
    panic(err.Error())
  }
}
```

## Domain Types

### Data Sink

- `type DataSink struct{…}`

  Schema for a data sink.

  - `ID string`

    Unique identifier

  - `Component DataSinkComponentUnion`

    Component that implements the data sink

    - `type DataSinkComponentMap map[string, any]`

    - `type CloudPineconeVectorStore struct{…}`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `APIKey string`

        The API key for authenticating with Pinecone

      - `IndexName string`

      - `ClassName string`

      - `InsertKwargs map[string, any]`

      - `Namespace string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudPineconeVectorStoreSupportsNestedMetadataFiltersTrue CloudPineconeVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudPostgresVectorStore struct{…}`

      - `Database string`

      - `EmbedDim int64`

      - `Host string`

      - `Password string`

      - `Port int64`

      - `SchemaName string`

      - `TableName string`

      - `User string`

      - `ClassName string`

      - `HnswSettings PgVectorHnswSettings`

        HNSW settings for PGVector.

        - `DistanceMethod PgVectorHnswSettingsDistanceMethod`

          The distance method to use.

          - `const PgVectorHnswSettingsDistanceMethodL2 PgVectorHnswSettingsDistanceMethod = "l2"`

          - `const PgVectorHnswSettingsDistanceMethodIP PgVectorHnswSettingsDistanceMethod = "ip"`

          - `const PgVectorHnswSettingsDistanceMethodCosine PgVectorHnswSettingsDistanceMethod = "cosine"`

          - `const PgVectorHnswSettingsDistanceMethodL1 PgVectorHnswSettingsDistanceMethod = "l1"`

          - `const PgVectorHnswSettingsDistanceMethodHamming PgVectorHnswSettingsDistanceMethod = "hamming"`

          - `const PgVectorHnswSettingsDistanceMethodJaccard PgVectorHnswSettingsDistanceMethod = "jaccard"`

        - `EfConstruction int64`

          The number of edges to use during the construction phase.

        - `EfSearch int64`

          The number of edges to use during the search phase.

        - `M int64`

          The number of bi-directional links created for each new element.

        - `VectorType PgVectorHnswSettingsVectorType`

          The type of vector to use.

          - `const PgVectorHnswSettingsVectorTypeVector PgVectorHnswSettingsVectorType = "vector"`

          - `const PgVectorHnswSettingsVectorTypeHalfVec PgVectorHnswSettingsVectorType = "half_vec"`

          - `const PgVectorHnswSettingsVectorTypeBit PgVectorHnswSettingsVectorType = "bit"`

          - `const PgVectorHnswSettingsVectorTypeSparseVec PgVectorHnswSettingsVectorType = "sparse_vec"`

      - `HybridSearch bool`

      - `PerformSetup bool`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudQdrantVectorStore struct{…}`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `APIKey string`

      - `CollectionName string`

      - `URL string`

      - `ClassName string`

      - `ClientKwargs map[string, any]`

      - `MaxRetries int64`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudQdrantVectorStoreSupportsNestedMetadataFiltersTrue CloudQdrantVectorStoreSupportsNestedMetadataFilters = true`

    - `type CloudAzureAISearchVectorStore struct{…}`

      Cloud Azure AI Search Vector Store.

      - `SearchServiceAPIKey string`

      - `SearchServiceEndpoint string`

      - `ClassName string`

      - `ClientID string`

      - `ClientSecret string`

      - `EmbeddingDimension int64`

      - `FilterableMetadataFieldKeys map[string, any]`

      - `IndexName string`

      - `SearchServiceAPIVersion string`

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAzureAISearchVectorStoreSupportsNestedMetadataFiltersTrue CloudAzureAISearchVectorStoreSupportsNestedMetadataFilters = true`

      - `TenantID string`

    - `type CloudMongoDBAtlasVectorSearch struct{…}`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `CollectionName string`

      - `DBName string`

      - `MongoDBUri string`

      - `ClassName string`

      - `EmbeddingDimension int64`

      - `FulltextIndexName string`

      - `SupportsNestedMetadataFilters bool`

      - `VectorIndexName string`

    - `type CloudMilvusVectorStore struct{…}`

      Cloud Milvus Vector Store.

      - `Uri string`

      - `Token string`

      - `ClassName string`

      - `CollectionName string`

      - `EmbeddingDimension int64`

      - `SupportsNestedMetadataFilters bool`

    - `type CloudAstraDBVectorStore struct{…}`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `Token string`

        The Astra DB Application Token to use

      - `APIEndpoint string`

        The Astra DB JSON API endpoint for your database

      - `CollectionName string`

        Collection name to use. If not existing, it will be created

      - `EmbeddingDimension int64`

        Length of the embedding vectors in use

      - `ClassName string`

      - `Keyspace string`

        The keyspace to use. If not provided, 'default_keyspace'

      - `SupportsNestedMetadataFilters bool`

        - `const CloudAstraDBVectorStoreSupportsNestedMetadataFiltersTrue CloudAstraDBVectorStoreSupportsNestedMetadataFilters = true`

  - `Name string`

    The name of the data sink.

  - `ProjectID string`

  - `SinkType DataSinkSinkType`

    - `const DataSinkSinkTypePinecone DataSinkSinkType = "PINECONE"`

    - `const DataSinkSinkTypePostgres DataSinkSinkType = "POSTGRES"`

    - `const DataSinkSinkTypeQdrant DataSinkSinkType = "QDRANT"`

    - `const DataSinkSinkTypeAzureaiSearch DataSinkSinkType = "AZUREAI_SEARCH"`

    - `const DataSinkSinkTypeMongoDBAtlas DataSinkSinkType = "MONGODB_ATLAS"`

    - `const DataSinkSinkTypeMilvus DataSinkSinkType = "MILVUS"`

    - `const DataSinkSinkTypeAstraDB DataSinkSinkType = "ASTRA_DB"`

  - `CreatedAt Time`

    Creation datetime

  - `UpdatedAt Time`

    Update datetime
