# Data Sinks

## List Data Sinks

`data_sinks.list(DataSinkListParams**kwargs)  -> DataSinkListResponse`

**get** `/api/v1/data-sinks`

List data sinks for a given project.

### Parameters

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `List[DataSink]`

  - `id: str`

    Unique identifier

  - `component: Component`

    Component that implements the data sink

    - `Dict[str, object]`

    - `class CloudPineconeVectorStore: …`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `api_key: str`

        The API key for authenticating with Pinecone

      - `index_name: str`

      - `class_name: Optional[str]`

      - `insert_kwargs: Optional[Dict[str, object]]`

      - `namespace: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudPostgresVectorStore: …`

      - `database: str`

      - `embed_dim: int`

      - `host: str`

      - `password: str`

      - `port: int`

      - `schema_name: str`

      - `table_name: str`

      - `user: str`

      - `class_name: Optional[str]`

      - `hnsw_settings: Optional[PgVectorHnswSettings]`

        HNSW settings for PGVector.

        - `distance_method: Optional[Literal["l2", "ip", "cosine", 3 more]]`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction: Optional[int]`

          The number of edges to use during the construction phase.

        - `ef_search: Optional[int]`

          The number of edges to use during the search phase.

        - `m: Optional[int]`

          The number of bi-directional links created for each new element.

        - `vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]]`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search: Optional[bool]`

      - `perform_setup: Optional[bool]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudQdrantVectorStore: …`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `api_key: str`

      - `collection_name: str`

      - `url: str`

      - `class_name: Optional[str]`

      - `client_kwargs: Optional[Dict[str, object]]`

      - `max_retries: Optional[int]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudAzureAISearchVectorStore: …`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: str`

      - `search_service_endpoint: str`

      - `class_name: Optional[str]`

      - `client_id: Optional[str]`

      - `client_secret: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `filterable_metadata_field_keys: Optional[Dict[str, object]]`

      - `index_name: Optional[str]`

      - `search_service_api_version: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

      - `tenant_id: Optional[str]`

    - `class CloudMongoDBAtlasVectorSearch: …`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `collection_name: str`

      - `db_name: str`

      - `mongodb_uri: str`

      - `class_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `fulltext_index_name: Optional[str]`

      - `supports_nested_metadata_filters: Optional[bool]`

      - `vector_index_name: Optional[str]`

    - `class CloudMilvusVectorStore: …`

      Cloud Milvus Vector Store.

      - `uri: str`

      - `token: Optional[str]`

      - `class_name: Optional[str]`

      - `collection_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudAstraDBVectorStore: …`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `token: str`

        The Astra DB Application Token to use

      - `api_endpoint: str`

        The Astra DB JSON API endpoint for your database

      - `collection_name: str`

        Collection name to use. If not existing, it will be created

      - `embedding_dimension: int`

        Length of the embedding vectors in use

      - `class_name: Optional[str]`

      - `keyspace: Optional[str]`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

  - `name: str`

    The name of the data sink.

  - `project_id: str`

  - `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
data_sinks = client.data_sinks.list()
print(data_sinks)
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

`data_sinks.create(DataSinkCreateParams**kwargs)  -> DataSink`

**post** `/api/v1/data-sinks`

Create a new data sink.

### Parameters

- `component: Component`

  Component that implements the data sink

  - `Dict[str, object]`

  - `class CloudPineconeVectorStore: …`

    Cloud Pinecone Vector Store.

    This class is used to store the configuration for a Pinecone vector store, so that it can be
    created and used in LlamaCloud.

    Args:
    api_key (str): API key for authenticating with Pinecone
    index_name (str): name of the Pinecone index
    namespace (optional[str]): namespace to use in the Pinecone index
    insert_kwargs (optional[dict]): additional kwargs to pass during insertion

    - `api_key: str`

      The API key for authenticating with Pinecone

    - `index_name: str`

    - `class_name: Optional[str]`

    - `insert_kwargs: Optional[Dict[str, object]]`

    - `namespace: Optional[str]`

    - `supports_nested_metadata_filters: Optional[Literal[true]]`

      - `true`

  - `class CloudPostgresVectorStore: …`

    - `database: str`

    - `embed_dim: int`

    - `host: str`

    - `password: str`

    - `port: int`

    - `schema_name: str`

    - `table_name: str`

    - `user: str`

    - `class_name: Optional[str]`

    - `hnsw_settings: Optional[PgVectorHnswSettings]`

      HNSW settings for PGVector.

      - `distance_method: Optional[Literal["l2", "ip", "cosine", 3 more]]`

        The distance method to use.

        - `"l2"`

        - `"ip"`

        - `"cosine"`

        - `"l1"`

        - `"hamming"`

        - `"jaccard"`

      - `ef_construction: Optional[int]`

        The number of edges to use during the construction phase.

      - `ef_search: Optional[int]`

        The number of edges to use during the search phase.

      - `m: Optional[int]`

        The number of bi-directional links created for each new element.

      - `vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]]`

        The type of vector to use.

        - `"vector"`

        - `"half_vec"`

        - `"bit"`

        - `"sparse_vec"`

    - `hybrid_search: Optional[bool]`

    - `perform_setup: Optional[bool]`

    - `supports_nested_metadata_filters: Optional[bool]`

  - `class CloudQdrantVectorStore: …`

    Cloud Qdrant Vector Store.

    This class is used to store the configuration for a Qdrant vector store, so that it can be
    created and used in LlamaCloud.

    Args:
    collection_name (str): name of the Qdrant collection
    url (str): url of the Qdrant instance
    api_key (str): API key for authenticating with Qdrant
    max_retries (int): maximum number of retries in case of a failure. Defaults to 3
    client_kwargs (dict): additional kwargs to pass to the Qdrant client

    - `api_key: str`

    - `collection_name: str`

    - `url: str`

    - `class_name: Optional[str]`

    - `client_kwargs: Optional[Dict[str, object]]`

    - `max_retries: Optional[int]`

    - `supports_nested_metadata_filters: Optional[Literal[true]]`

      - `true`

  - `class CloudAzureAISearchVectorStore: …`

    Cloud Azure AI Search Vector Store.

    - `search_service_api_key: str`

    - `search_service_endpoint: str`

    - `class_name: Optional[str]`

    - `client_id: Optional[str]`

    - `client_secret: Optional[str]`

    - `embedding_dimension: Optional[int]`

    - `filterable_metadata_field_keys: Optional[Dict[str, object]]`

    - `index_name: Optional[str]`

    - `search_service_api_version: Optional[str]`

    - `supports_nested_metadata_filters: Optional[Literal[true]]`

      - `true`

    - `tenant_id: Optional[str]`

  - `class CloudMongoDBAtlasVectorSearch: …`

    Cloud MongoDB Atlas Vector Store.

    This class is used to store the configuration for a MongoDB Atlas vector store,
    so that it can be created and used in LlamaCloud.

    Args:
    mongodb_uri (str): URI for connecting to MongoDB Atlas
    db_name (str): name of the MongoDB database
    collection_name (str): name of the MongoDB collection
    vector_index_name (str): name of the MongoDB Atlas vector index
    fulltext_index_name (str): name of the MongoDB Atlas full-text index

    - `collection_name: str`

    - `db_name: str`

    - `mongodb_uri: str`

    - `class_name: Optional[str]`

    - `embedding_dimension: Optional[int]`

    - `fulltext_index_name: Optional[str]`

    - `supports_nested_metadata_filters: Optional[bool]`

    - `vector_index_name: Optional[str]`

  - `class CloudMilvusVectorStore: …`

    Cloud Milvus Vector Store.

    - `uri: str`

    - `token: Optional[str]`

    - `class_name: Optional[str]`

    - `collection_name: Optional[str]`

    - `embedding_dimension: Optional[int]`

    - `supports_nested_metadata_filters: Optional[bool]`

  - `class CloudAstraDBVectorStore: …`

    Cloud AstraDB Vector Store.

    This class is used to store the configuration for an AstraDB vector store, so that it can be
    created and used in LlamaCloud.

    Args:
    token (str): The Astra DB Application Token to use.
    api_endpoint (str): The Astra DB JSON API endpoint for your database.
    collection_name (str): Collection name to use. If not existing, it will be created.
    embedding_dimension (int): Length of the embedding vectors in use.
    keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

    - `token: str`

      The Astra DB Application Token to use

    - `api_endpoint: str`

      The Astra DB JSON API endpoint for your database

    - `collection_name: str`

      Collection name to use. If not existing, it will be created

    - `embedding_dimension: int`

      Length of the embedding vectors in use

    - `class_name: Optional[str]`

    - `keyspace: Optional[str]`

      The keyspace to use. If not provided, 'default_keyspace'

    - `supports_nested_metadata_filters: Optional[Literal[true]]`

      - `true`

- `name: str`

  The name of the data sink.

- `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

  - `"PINECONE"`

  - `"POSTGRES"`

  - `"QDRANT"`

  - `"AZUREAI_SEARCH"`

  - `"MONGODB_ATLAS"`

  - `"MILVUS"`

  - `"ASTRA_DB"`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class DataSink: …`

  Schema for a data sink.

  - `id: str`

    Unique identifier

  - `component: Component`

    Component that implements the data sink

    - `Dict[str, object]`

    - `class CloudPineconeVectorStore: …`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `api_key: str`

        The API key for authenticating with Pinecone

      - `index_name: str`

      - `class_name: Optional[str]`

      - `insert_kwargs: Optional[Dict[str, object]]`

      - `namespace: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudPostgresVectorStore: …`

      - `database: str`

      - `embed_dim: int`

      - `host: str`

      - `password: str`

      - `port: int`

      - `schema_name: str`

      - `table_name: str`

      - `user: str`

      - `class_name: Optional[str]`

      - `hnsw_settings: Optional[PgVectorHnswSettings]`

        HNSW settings for PGVector.

        - `distance_method: Optional[Literal["l2", "ip", "cosine", 3 more]]`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction: Optional[int]`

          The number of edges to use during the construction phase.

        - `ef_search: Optional[int]`

          The number of edges to use during the search phase.

        - `m: Optional[int]`

          The number of bi-directional links created for each new element.

        - `vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]]`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search: Optional[bool]`

      - `perform_setup: Optional[bool]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudQdrantVectorStore: …`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `api_key: str`

      - `collection_name: str`

      - `url: str`

      - `class_name: Optional[str]`

      - `client_kwargs: Optional[Dict[str, object]]`

      - `max_retries: Optional[int]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudAzureAISearchVectorStore: …`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: str`

      - `search_service_endpoint: str`

      - `class_name: Optional[str]`

      - `client_id: Optional[str]`

      - `client_secret: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `filterable_metadata_field_keys: Optional[Dict[str, object]]`

      - `index_name: Optional[str]`

      - `search_service_api_version: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

      - `tenant_id: Optional[str]`

    - `class CloudMongoDBAtlasVectorSearch: …`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `collection_name: str`

      - `db_name: str`

      - `mongodb_uri: str`

      - `class_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `fulltext_index_name: Optional[str]`

      - `supports_nested_metadata_filters: Optional[bool]`

      - `vector_index_name: Optional[str]`

    - `class CloudMilvusVectorStore: …`

      Cloud Milvus Vector Store.

      - `uri: str`

      - `token: Optional[str]`

      - `class_name: Optional[str]`

      - `collection_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudAstraDBVectorStore: …`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `token: str`

        The Astra DB Application Token to use

      - `api_endpoint: str`

        The Astra DB JSON API endpoint for your database

      - `collection_name: str`

        Collection name to use. If not existing, it will be created

      - `embedding_dimension: int`

        Length of the embedding vectors in use

      - `class_name: Optional[str]`

      - `keyspace: Optional[str]`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

  - `name: str`

    The name of the data sink.

  - `project_id: str`

  - `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
data_sink = client.data_sinks.create(
    component={
        "foo": "bar"
    },
    name="name",
    sink_type="PINECONE",
)
print(data_sink.id)
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

`data_sinks.get(strdata_sink_id)  -> DataSink`

**get** `/api/v1/data-sinks/{data_sink_id}`

Get a data sink by ID.

### Parameters

- `data_sink_id: str`

### Returns

- `class DataSink: …`

  Schema for a data sink.

  - `id: str`

    Unique identifier

  - `component: Component`

    Component that implements the data sink

    - `Dict[str, object]`

    - `class CloudPineconeVectorStore: …`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `api_key: str`

        The API key for authenticating with Pinecone

      - `index_name: str`

      - `class_name: Optional[str]`

      - `insert_kwargs: Optional[Dict[str, object]]`

      - `namespace: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudPostgresVectorStore: …`

      - `database: str`

      - `embed_dim: int`

      - `host: str`

      - `password: str`

      - `port: int`

      - `schema_name: str`

      - `table_name: str`

      - `user: str`

      - `class_name: Optional[str]`

      - `hnsw_settings: Optional[PgVectorHnswSettings]`

        HNSW settings for PGVector.

        - `distance_method: Optional[Literal["l2", "ip", "cosine", 3 more]]`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction: Optional[int]`

          The number of edges to use during the construction phase.

        - `ef_search: Optional[int]`

          The number of edges to use during the search phase.

        - `m: Optional[int]`

          The number of bi-directional links created for each new element.

        - `vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]]`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search: Optional[bool]`

      - `perform_setup: Optional[bool]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudQdrantVectorStore: …`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `api_key: str`

      - `collection_name: str`

      - `url: str`

      - `class_name: Optional[str]`

      - `client_kwargs: Optional[Dict[str, object]]`

      - `max_retries: Optional[int]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudAzureAISearchVectorStore: …`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: str`

      - `search_service_endpoint: str`

      - `class_name: Optional[str]`

      - `client_id: Optional[str]`

      - `client_secret: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `filterable_metadata_field_keys: Optional[Dict[str, object]]`

      - `index_name: Optional[str]`

      - `search_service_api_version: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

      - `tenant_id: Optional[str]`

    - `class CloudMongoDBAtlasVectorSearch: …`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `collection_name: str`

      - `db_name: str`

      - `mongodb_uri: str`

      - `class_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `fulltext_index_name: Optional[str]`

      - `supports_nested_metadata_filters: Optional[bool]`

      - `vector_index_name: Optional[str]`

    - `class CloudMilvusVectorStore: …`

      Cloud Milvus Vector Store.

      - `uri: str`

      - `token: Optional[str]`

      - `class_name: Optional[str]`

      - `collection_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudAstraDBVectorStore: …`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `token: str`

        The Astra DB Application Token to use

      - `api_endpoint: str`

        The Astra DB JSON API endpoint for your database

      - `collection_name: str`

        Collection name to use. If not existing, it will be created

      - `embedding_dimension: int`

        Length of the embedding vectors in use

      - `class_name: Optional[str]`

      - `keyspace: Optional[str]`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

  - `name: str`

    The name of the data sink.

  - `project_id: str`

  - `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
data_sink = client.data_sinks.get(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(data_sink.id)
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

`data_sinks.update(strdata_sink_id, DataSinkUpdateParams**kwargs)  -> DataSink`

**put** `/api/v1/data-sinks/{data_sink_id}`

Update a data sink by ID.

### Parameters

- `data_sink_id: str`

- `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

  - `"PINECONE"`

  - `"POSTGRES"`

  - `"QDRANT"`

  - `"AZUREAI_SEARCH"`

  - `"MONGODB_ATLAS"`

  - `"MILVUS"`

  - `"ASTRA_DB"`

- `component: Optional[Component]`

  Component that implements the data sink

  - `Dict[str, object]`

  - `class CloudPineconeVectorStore: …`

    Cloud Pinecone Vector Store.

    This class is used to store the configuration for a Pinecone vector store, so that it can be
    created and used in LlamaCloud.

    Args:
    api_key (str): API key for authenticating with Pinecone
    index_name (str): name of the Pinecone index
    namespace (optional[str]): namespace to use in the Pinecone index
    insert_kwargs (optional[dict]): additional kwargs to pass during insertion

    - `api_key: str`

      The API key for authenticating with Pinecone

    - `index_name: str`

    - `class_name: Optional[str]`

    - `insert_kwargs: Optional[Dict[str, object]]`

    - `namespace: Optional[str]`

    - `supports_nested_metadata_filters: Optional[Literal[true]]`

      - `true`

  - `class CloudPostgresVectorStore: …`

    - `database: str`

    - `embed_dim: int`

    - `host: str`

    - `password: str`

    - `port: int`

    - `schema_name: str`

    - `table_name: str`

    - `user: str`

    - `class_name: Optional[str]`

    - `hnsw_settings: Optional[PgVectorHnswSettings]`

      HNSW settings for PGVector.

      - `distance_method: Optional[Literal["l2", "ip", "cosine", 3 more]]`

        The distance method to use.

        - `"l2"`

        - `"ip"`

        - `"cosine"`

        - `"l1"`

        - `"hamming"`

        - `"jaccard"`

      - `ef_construction: Optional[int]`

        The number of edges to use during the construction phase.

      - `ef_search: Optional[int]`

        The number of edges to use during the search phase.

      - `m: Optional[int]`

        The number of bi-directional links created for each new element.

      - `vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]]`

        The type of vector to use.

        - `"vector"`

        - `"half_vec"`

        - `"bit"`

        - `"sparse_vec"`

    - `hybrid_search: Optional[bool]`

    - `perform_setup: Optional[bool]`

    - `supports_nested_metadata_filters: Optional[bool]`

  - `class CloudQdrantVectorStore: …`

    Cloud Qdrant Vector Store.

    This class is used to store the configuration for a Qdrant vector store, so that it can be
    created and used in LlamaCloud.

    Args:
    collection_name (str): name of the Qdrant collection
    url (str): url of the Qdrant instance
    api_key (str): API key for authenticating with Qdrant
    max_retries (int): maximum number of retries in case of a failure. Defaults to 3
    client_kwargs (dict): additional kwargs to pass to the Qdrant client

    - `api_key: str`

    - `collection_name: str`

    - `url: str`

    - `class_name: Optional[str]`

    - `client_kwargs: Optional[Dict[str, object]]`

    - `max_retries: Optional[int]`

    - `supports_nested_metadata_filters: Optional[Literal[true]]`

      - `true`

  - `class CloudAzureAISearchVectorStore: …`

    Cloud Azure AI Search Vector Store.

    - `search_service_api_key: str`

    - `search_service_endpoint: str`

    - `class_name: Optional[str]`

    - `client_id: Optional[str]`

    - `client_secret: Optional[str]`

    - `embedding_dimension: Optional[int]`

    - `filterable_metadata_field_keys: Optional[Dict[str, object]]`

    - `index_name: Optional[str]`

    - `search_service_api_version: Optional[str]`

    - `supports_nested_metadata_filters: Optional[Literal[true]]`

      - `true`

    - `tenant_id: Optional[str]`

  - `class CloudMongoDBAtlasVectorSearch: …`

    Cloud MongoDB Atlas Vector Store.

    This class is used to store the configuration for a MongoDB Atlas vector store,
    so that it can be created and used in LlamaCloud.

    Args:
    mongodb_uri (str): URI for connecting to MongoDB Atlas
    db_name (str): name of the MongoDB database
    collection_name (str): name of the MongoDB collection
    vector_index_name (str): name of the MongoDB Atlas vector index
    fulltext_index_name (str): name of the MongoDB Atlas full-text index

    - `collection_name: str`

    - `db_name: str`

    - `mongodb_uri: str`

    - `class_name: Optional[str]`

    - `embedding_dimension: Optional[int]`

    - `fulltext_index_name: Optional[str]`

    - `supports_nested_metadata_filters: Optional[bool]`

    - `vector_index_name: Optional[str]`

  - `class CloudMilvusVectorStore: …`

    Cloud Milvus Vector Store.

    - `uri: str`

    - `token: Optional[str]`

    - `class_name: Optional[str]`

    - `collection_name: Optional[str]`

    - `embedding_dimension: Optional[int]`

    - `supports_nested_metadata_filters: Optional[bool]`

  - `class CloudAstraDBVectorStore: …`

    Cloud AstraDB Vector Store.

    This class is used to store the configuration for an AstraDB vector store, so that it can be
    created and used in LlamaCloud.

    Args:
    token (str): The Astra DB Application Token to use.
    api_endpoint (str): The Astra DB JSON API endpoint for your database.
    collection_name (str): Collection name to use. If not existing, it will be created.
    embedding_dimension (int): Length of the embedding vectors in use.
    keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

    - `token: str`

      The Astra DB Application Token to use

    - `api_endpoint: str`

      The Astra DB JSON API endpoint for your database

    - `collection_name: str`

      Collection name to use. If not existing, it will be created

    - `embedding_dimension: int`

      Length of the embedding vectors in use

    - `class_name: Optional[str]`

    - `keyspace: Optional[str]`

      The keyspace to use. If not provided, 'default_keyspace'

    - `supports_nested_metadata_filters: Optional[Literal[true]]`

      - `true`

- `name: Optional[str]`

  The name of the data sink.

### Returns

- `class DataSink: …`

  Schema for a data sink.

  - `id: str`

    Unique identifier

  - `component: Component`

    Component that implements the data sink

    - `Dict[str, object]`

    - `class CloudPineconeVectorStore: …`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `api_key: str`

        The API key for authenticating with Pinecone

      - `index_name: str`

      - `class_name: Optional[str]`

      - `insert_kwargs: Optional[Dict[str, object]]`

      - `namespace: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudPostgresVectorStore: …`

      - `database: str`

      - `embed_dim: int`

      - `host: str`

      - `password: str`

      - `port: int`

      - `schema_name: str`

      - `table_name: str`

      - `user: str`

      - `class_name: Optional[str]`

      - `hnsw_settings: Optional[PgVectorHnswSettings]`

        HNSW settings for PGVector.

        - `distance_method: Optional[Literal["l2", "ip", "cosine", 3 more]]`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction: Optional[int]`

          The number of edges to use during the construction phase.

        - `ef_search: Optional[int]`

          The number of edges to use during the search phase.

        - `m: Optional[int]`

          The number of bi-directional links created for each new element.

        - `vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]]`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search: Optional[bool]`

      - `perform_setup: Optional[bool]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudQdrantVectorStore: …`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `api_key: str`

      - `collection_name: str`

      - `url: str`

      - `class_name: Optional[str]`

      - `client_kwargs: Optional[Dict[str, object]]`

      - `max_retries: Optional[int]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudAzureAISearchVectorStore: …`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: str`

      - `search_service_endpoint: str`

      - `class_name: Optional[str]`

      - `client_id: Optional[str]`

      - `client_secret: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `filterable_metadata_field_keys: Optional[Dict[str, object]]`

      - `index_name: Optional[str]`

      - `search_service_api_version: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

      - `tenant_id: Optional[str]`

    - `class CloudMongoDBAtlasVectorSearch: …`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `collection_name: str`

      - `db_name: str`

      - `mongodb_uri: str`

      - `class_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `fulltext_index_name: Optional[str]`

      - `supports_nested_metadata_filters: Optional[bool]`

      - `vector_index_name: Optional[str]`

    - `class CloudMilvusVectorStore: …`

      Cloud Milvus Vector Store.

      - `uri: str`

      - `token: Optional[str]`

      - `class_name: Optional[str]`

      - `collection_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudAstraDBVectorStore: …`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `token: str`

        The Astra DB Application Token to use

      - `api_endpoint: str`

        The Astra DB JSON API endpoint for your database

      - `collection_name: str`

        Collection name to use. If not existing, it will be created

      - `embedding_dimension: int`

        Length of the embedding vectors in use

      - `class_name: Optional[str]`

      - `keyspace: Optional[str]`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

  - `name: str`

    The name of the data sink.

  - `project_id: str`

  - `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
data_sink = client.data_sinks.update(
    data_sink_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    sink_type="PINECONE",
)
print(data_sink.id)
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

`data_sinks.delete(strdata_sink_id)`

**delete** `/api/v1/data-sinks/{data_sink_id}`

Delete a data sink by ID.

### Parameters

- `data_sink_id: str`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.data_sinks.delete(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
```

## Domain Types

### Data Sink

- `class DataSink: …`

  Schema for a data sink.

  - `id: str`

    Unique identifier

  - `component: Component`

    Component that implements the data sink

    - `Dict[str, object]`

    - `class CloudPineconeVectorStore: …`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `api_key: str`

        The API key for authenticating with Pinecone

      - `index_name: str`

      - `class_name: Optional[str]`

      - `insert_kwargs: Optional[Dict[str, object]]`

      - `namespace: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudPostgresVectorStore: …`

      - `database: str`

      - `embed_dim: int`

      - `host: str`

      - `password: str`

      - `port: int`

      - `schema_name: str`

      - `table_name: str`

      - `user: str`

      - `class_name: Optional[str]`

      - `hnsw_settings: Optional[PgVectorHnswSettings]`

        HNSW settings for PGVector.

        - `distance_method: Optional[Literal["l2", "ip", "cosine", 3 more]]`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction: Optional[int]`

          The number of edges to use during the construction phase.

        - `ef_search: Optional[int]`

          The number of edges to use during the search phase.

        - `m: Optional[int]`

          The number of bi-directional links created for each new element.

        - `vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]]`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search: Optional[bool]`

      - `perform_setup: Optional[bool]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudQdrantVectorStore: …`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `api_key: str`

      - `collection_name: str`

      - `url: str`

      - `class_name: Optional[str]`

      - `client_kwargs: Optional[Dict[str, object]]`

      - `max_retries: Optional[int]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudAzureAISearchVectorStore: …`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: str`

      - `search_service_endpoint: str`

      - `class_name: Optional[str]`

      - `client_id: Optional[str]`

      - `client_secret: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `filterable_metadata_field_keys: Optional[Dict[str, object]]`

      - `index_name: Optional[str]`

      - `search_service_api_version: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

      - `tenant_id: Optional[str]`

    - `class CloudMongoDBAtlasVectorSearch: …`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `collection_name: str`

      - `db_name: str`

      - `mongodb_uri: str`

      - `class_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `fulltext_index_name: Optional[str]`

      - `supports_nested_metadata_filters: Optional[bool]`

      - `vector_index_name: Optional[str]`

    - `class CloudMilvusVectorStore: …`

      Cloud Milvus Vector Store.

      - `uri: str`

      - `token: Optional[str]`

      - `class_name: Optional[str]`

      - `collection_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudAstraDBVectorStore: …`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `token: str`

        The Astra DB Application Token to use

      - `api_endpoint: str`

        The Astra DB JSON API endpoint for your database

      - `collection_name: str`

        Collection name to use. If not existing, it will be created

      - `embedding_dimension: int`

        Length of the embedding vectors in use

      - `class_name: Optional[str]`

      - `keyspace: Optional[str]`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

  - `name: str`

    The name of the data sink.

  - `project_id: str`

  - `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `updated_at: Optional[datetime]`

    Update datetime

### Data Sink List Response

- `List[DataSink]`

  - `id: str`

    Unique identifier

  - `component: Component`

    Component that implements the data sink

    - `Dict[str, object]`

    - `class CloudPineconeVectorStore: …`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `api_key: str`

        The API key for authenticating with Pinecone

      - `index_name: str`

      - `class_name: Optional[str]`

      - `insert_kwargs: Optional[Dict[str, object]]`

      - `namespace: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudPostgresVectorStore: …`

      - `database: str`

      - `embed_dim: int`

      - `host: str`

      - `password: str`

      - `port: int`

      - `schema_name: str`

      - `table_name: str`

      - `user: str`

      - `class_name: Optional[str]`

      - `hnsw_settings: Optional[PgVectorHnswSettings]`

        HNSW settings for PGVector.

        - `distance_method: Optional[Literal["l2", "ip", "cosine", 3 more]]`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction: Optional[int]`

          The number of edges to use during the construction phase.

        - `ef_search: Optional[int]`

          The number of edges to use during the search phase.

        - `m: Optional[int]`

          The number of bi-directional links created for each new element.

        - `vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]]`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search: Optional[bool]`

      - `perform_setup: Optional[bool]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudQdrantVectorStore: …`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `api_key: str`

      - `collection_name: str`

      - `url: str`

      - `class_name: Optional[str]`

      - `client_kwargs: Optional[Dict[str, object]]`

      - `max_retries: Optional[int]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

    - `class CloudAzureAISearchVectorStore: …`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: str`

      - `search_service_endpoint: str`

      - `class_name: Optional[str]`

      - `client_id: Optional[str]`

      - `client_secret: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `filterable_metadata_field_keys: Optional[Dict[str, object]]`

      - `index_name: Optional[str]`

      - `search_service_api_version: Optional[str]`

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

      - `tenant_id: Optional[str]`

    - `class CloudMongoDBAtlasVectorSearch: …`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `collection_name: str`

      - `db_name: str`

      - `mongodb_uri: str`

      - `class_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `fulltext_index_name: Optional[str]`

      - `supports_nested_metadata_filters: Optional[bool]`

      - `vector_index_name: Optional[str]`

    - `class CloudMilvusVectorStore: …`

      Cloud Milvus Vector Store.

      - `uri: str`

      - `token: Optional[str]`

      - `class_name: Optional[str]`

      - `collection_name: Optional[str]`

      - `embedding_dimension: Optional[int]`

      - `supports_nested_metadata_filters: Optional[bool]`

    - `class CloudAstraDBVectorStore: …`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `token: str`

        The Astra DB Application Token to use

      - `api_endpoint: str`

        The Astra DB JSON API endpoint for your database

      - `collection_name: str`

        Collection name to use. If not existing, it will be created

      - `embedding_dimension: int`

        Length of the embedding vectors in use

      - `class_name: Optional[str]`

      - `keyspace: Optional[str]`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters: Optional[Literal[true]]`

        - `true`

  - `name: str`

    The name of the data sink.

  - `project_id: str`

  - `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `updated_at: Optional[datetime]`

    Update datetime
