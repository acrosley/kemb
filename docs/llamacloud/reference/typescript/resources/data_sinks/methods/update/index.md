## Update Data Sink

`client.dataSinks.update(stringdataSinkID, DataSinkUpdateParamsbody, RequestOptionsoptions?): DataSink`

**put** `/api/v1/data-sinks/{data_sink_id}`

Update a data sink by ID.

### Parameters

- `dataSinkID: string`

- `body: DataSinkUpdateParams`

  - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `component?: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more | null`

    Component that implements the data sink

    - `Record<string, unknown>`

    - `CloudPineconeVectorStore`

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

      - `class_name?: string`

      - `insert_kwargs?: Record<string, unknown> | null`

      - `namespace?: string | null`

      - `supports_nested_metadata_filters?: true`

        - `true`

    - `CloudPostgresVectorStore`

      - `database: string`

      - `embed_dim: number`

      - `host: string`

      - `password: string`

      - `port: number`

      - `schema_name: string`

      - `table_name: string`

      - `user: string`

      - `class_name?: string`

      - `hnsw_settings?: PgVectorHnswSettings | null`

        HNSW settings for PGVector.

        - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction?: number`

          The number of edges to use during the construction phase.

        - `ef_search?: number`

          The number of edges to use during the search phase.

        - `m?: number`

          The number of bi-directional links created for each new element.

        - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search?: boolean | null`

      - `perform_setup?: boolean`

      - `supports_nested_metadata_filters?: boolean`

    - `CloudQdrantVectorStore`

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

      - `class_name?: string`

      - `client_kwargs?: Record<string, unknown>`

      - `max_retries?: number`

      - `supports_nested_metadata_filters?: true`

        - `true`

    - `CloudAzureAISearchVectorStore`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: string`

      - `search_service_endpoint: string`

      - `class_name?: string`

      - `client_id?: string | null`

      - `client_secret?: string | null`

      - `embedding_dimension?: number | null`

      - `filterable_metadata_field_keys?: Record<string, unknown> | null`

      - `index_name?: string | null`

      - `search_service_api_version?: string | null`

      - `supports_nested_metadata_filters?: true`

        - `true`

      - `tenant_id?: string | null`

    - `CloudMongoDBAtlasVectorSearch`

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

      - `class_name?: string`

      - `embedding_dimension?: number | null`

      - `fulltext_index_name?: string | null`

      - `supports_nested_metadata_filters?: boolean`

      - `vector_index_name?: string | null`

    - `CloudMilvusVectorStore`

      Cloud Milvus Vector Store.

      - `uri: string`

      - `token?: string | null`

      - `class_name?: string`

      - `collection_name?: string | null`

      - `embedding_dimension?: number | null`

      - `supports_nested_metadata_filters?: boolean`

    - `CloudAstraDBVectorStore`

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

      - `class_name?: string`

      - `keyspace?: string | null`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters?: true`

        - `true`

  - `name?: string | null`

    The name of the data sink.

### Returns

- `DataSink`

  Schema for a data sink.

  - `id: string`

    Unique identifier

  - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

    Component that implements the data sink

    - `Record<string, unknown>`

    - `CloudPineconeVectorStore`

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

      - `class_name?: string`

      - `insert_kwargs?: Record<string, unknown> | null`

      - `namespace?: string | null`

      - `supports_nested_metadata_filters?: true`

        - `true`

    - `CloudPostgresVectorStore`

      - `database: string`

      - `embed_dim: number`

      - `host: string`

      - `password: string`

      - `port: number`

      - `schema_name: string`

      - `table_name: string`

      - `user: string`

      - `class_name?: string`

      - `hnsw_settings?: PgVectorHnswSettings | null`

        HNSW settings for PGVector.

        - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction?: number`

          The number of edges to use during the construction phase.

        - `ef_search?: number`

          The number of edges to use during the search phase.

        - `m?: number`

          The number of bi-directional links created for each new element.

        - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search?: boolean | null`

      - `perform_setup?: boolean`

      - `supports_nested_metadata_filters?: boolean`

    - `CloudQdrantVectorStore`

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

      - `class_name?: string`

      - `client_kwargs?: Record<string, unknown>`

      - `max_retries?: number`

      - `supports_nested_metadata_filters?: true`

        - `true`

    - `CloudAzureAISearchVectorStore`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: string`

      - `search_service_endpoint: string`

      - `class_name?: string`

      - `client_id?: string | null`

      - `client_secret?: string | null`

      - `embedding_dimension?: number | null`

      - `filterable_metadata_field_keys?: Record<string, unknown> | null`

      - `index_name?: string | null`

      - `search_service_api_version?: string | null`

      - `supports_nested_metadata_filters?: true`

        - `true`

      - `tenant_id?: string | null`

    - `CloudMongoDBAtlasVectorSearch`

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

      - `class_name?: string`

      - `embedding_dimension?: number | null`

      - `fulltext_index_name?: string | null`

      - `supports_nested_metadata_filters?: boolean`

      - `vector_index_name?: string | null`

    - `CloudMilvusVectorStore`

      Cloud Milvus Vector Store.

      - `uri: string`

      - `token?: string | null`

      - `class_name?: string`

      - `collection_name?: string | null`

      - `embedding_dimension?: number | null`

      - `supports_nested_metadata_filters?: boolean`

    - `CloudAstraDBVectorStore`

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

      - `class_name?: string`

      - `keyspace?: string | null`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters?: true`

        - `true`

  - `name: string`

    The name of the data sink.

  - `project_id: string`

  - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

  - `created_at?: string | null`

    Creation datetime

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const dataSink = await client.dataSinks.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  sink_type: 'PINECONE',
});

console.log(dataSink.id);
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
