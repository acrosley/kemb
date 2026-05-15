## Get Data Sink

**get** `/api/v1/data-sinks/{data_sink_id}`

Get a data sink by ID.

### Path Parameters

- `data_sink_id: string`

### Cookie Parameters

- `session: optional string`

### Returns

- `DataSink = object { id, component, name, 4 more }`

  Schema for a data sink.

  - `id: string`

    Unique identifier

  - `component: map[unknown] or CloudPineconeVectorStore or CloudPostgresVectorStore or 5 more`

    Component that implements the data sink

    - `map[unknown]`

    - `CloudPineconeVectorStore = object { api_key, index_name, class_name, 3 more }`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `api_key: string`

        The API key for authenticating with Pinecone

      - `index_name: string`

      - `class_name: optional string`

      - `insert_kwargs: optional map[unknown]`

      - `namespace: optional string`

      - `supports_nested_metadata_filters: optional true`

        - `true`

    - `CloudPostgresVectorStore = object { database, embed_dim, host, 10 more }`

      - `database: string`

      - `embed_dim: number`

      - `host: string`

      - `password: string`

      - `port: number`

      - `schema_name: string`

      - `table_name: string`

      - `user: string`

      - `class_name: optional string`

      - `hnsw_settings: optional PgVectorHnswSettings`

        HNSW settings for PGVector.

        - `distance_method: optional "l2" or "ip" or "cosine" or 3 more`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction: optional number`

          The number of edges to use during the construction phase.

        - `ef_search: optional number`

          The number of edges to use during the search phase.

        - `m: optional number`

          The number of bi-directional links created for each new element.

        - `vector_type: optional "vector" or "half_vec" or "bit" or "sparse_vec"`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search: optional boolean`

      - `perform_setup: optional boolean`

      - `supports_nested_metadata_filters: optional boolean`

    - `CloudQdrantVectorStore = object { api_key, collection_name, url, 4 more }`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `api_key: string`

      - `collection_name: string`

      - `url: string`

      - `class_name: optional string`

      - `client_kwargs: optional map[unknown]`

      - `max_retries: optional number`

      - `supports_nested_metadata_filters: optional true`

        - `true`

    - `CloudAzureAISearchVectorStore = object { search_service_api_key, search_service_endpoint, class_name, 8 more }`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: string`

      - `search_service_endpoint: string`

      - `class_name: optional string`

      - `client_id: optional string`

      - `client_secret: optional string`

      - `embedding_dimension: optional number`

      - `filterable_metadata_field_keys: optional map[unknown]`

      - `index_name: optional string`

      - `search_service_api_version: optional string`

      - `supports_nested_metadata_filters: optional true`

        - `true`

      - `tenant_id: optional string`

    - `CloudMongoDBAtlasVectorSearch = object { collection_name, db_name, mongodb_uri, 5 more }`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `collection_name: string`

      - `db_name: string`

      - `mongodb_uri: string`

      - `class_name: optional string`

      - `embedding_dimension: optional number`

      - `fulltext_index_name: optional string`

      - `supports_nested_metadata_filters: optional boolean`

      - `vector_index_name: optional string`

    - `CloudMilvusVectorStore = object { uri, token, class_name, 3 more }`

      Cloud Milvus Vector Store.

      - `uri: string`

      - `token: optional string`

      - `class_name: optional string`

      - `collection_name: optional string`

      - `embedding_dimension: optional number`

      - `supports_nested_metadata_filters: optional boolean`

    - `CloudAstraDBVectorStore = object { token, api_endpoint, collection_name, 4 more }`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `token: string`

        The Astra DB Application Token to use

      - `api_endpoint: string`

        The Astra DB JSON API endpoint for your database

      - `collection_name: string`

        Collection name to use. If not existing, it will be created

      - `embedding_dimension: number`

        Length of the embedding vectors in use

      - `class_name: optional string`

      - `keyspace: optional string`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters: optional true`

        - `true`

  - `name: string`

    The name of the data sink.

  - `project_id: string`

  - `sink_type: "PINECONE" or "POSTGRES" or "QDRANT" or 4 more`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `created_at: optional string`

    Creation datetime

  - `updated_at: optional string`

    Update datetime

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/data-sinks/$DATA_SINK_ID \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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
