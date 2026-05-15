# Shared

## Domain Types

### Cloud Astra DB Vector Store

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

### Cloud Az Storage Blob Data Source

- `CloudAzStorageBlobDataSource`

  - `account_url: string`

    The Azure Storage Blob account URL to use for authentication.

  - `container_name: string`

    The name of the Azure Storage Blob container to read from.

  - `account_key?: string | null`

    The Azure Storage Blob account key to use for authentication.

  - `account_name?: string | null`

    The Azure Storage Blob account name to use for authentication.

  - `blob?: string | null`

    The blob name to read from.

  - `class_name?: string`

  - `client_id?: string | null`

    The Azure AD client ID to use for authentication.

  - `client_secret?: string | null`

    The Azure AD client secret to use for authentication.

  - `prefix?: string | null`

    The prefix of the Azure Storage Blob objects to read from.

  - `supports_access_control?: boolean`

  - `tenant_id?: string | null`

    The Azure AD tenant ID to use for authentication.

### Cloud Azure AI Search Vector Store

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

### Cloud Box Data Source

- `CloudBoxDataSource`

  - `authentication_mechanism: "developer_token" | "ccg"`

    The type of authentication to use (Developer Token or CCG)

    - `"developer_token"`

    - `"ccg"`

  - `class_name?: string`

  - `client_id?: string | null`

    Box API key used for identifying the application the user is authenticating with

  - `client_secret?: string | null`

    Box API secret used for making auth requests.

  - `developer_token?: string | null`

    Developer token for authentication if authentication_mechanism is 'developer_token'.

  - `enterprise_id?: string | null`

    Box Enterprise ID, if provided authenticates as service.

  - `folder_id?: string | null`

    The ID of the Box folder to read from.

  - `supports_access_control?: boolean`

  - `user_id?: string | null`

    Box User ID, if provided authenticates as user.

### Cloud Confluence Data Source

- `CloudConfluenceDataSource`

  - `authentication_mechanism: string`

    Type of Authentication for connecting to Confluence APIs.

  - `server_url: string`

    The server URL of the Confluence instance.

  - `api_token?: string | null`

    The API token to use for authentication.

  - `class_name?: string`

  - `cql?: string | null`

    The CQL query to use for fetching pages.

  - `failure_handling?: FailureHandlingConfig`

    Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

    Example:
    {
    "skip_list_failures": true
    }

    Currently supports:

    - skip_list_failures: Skip failed batches/lists and continue processing

    - `skip_list_failures?: boolean`

      Whether to skip failed batches/lists and continue processing

  - `index_restricted_pages?: boolean`

    Whether to index restricted pages.

  - `keep_markdown_format?: boolean`

    Whether to keep the markdown format.

  - `label?: string | null`

    The label to use for fetching pages.

  - `page_ids?: string | null`

    The page IDs of the Confluence to read from.

  - `space_key?: string | null`

    The space key to read from.

  - `supports_access_control?: boolean`

  - `user_name?: string | null`

    The username to use for authentication.

### Cloud Google Drive Data Source

- `CloudGoogleDriveDataSource`

  - `folder_id: string`

    The ID of the Google Drive folder to read from.

  - `class_name?: string`

  - `service_account_key?: Record<string, string> | null`

    A dictionary containing secret values

  - `supports_access_control?: boolean`

### Cloud Jira Data Source

- `CloudJiraDataSource`

  Cloud Jira Data Source integrating JiraReader.

  - `authentication_mechanism: string`

    Type of Authentication for connecting to Jira APIs.

  - `query: string`

    JQL (Jira Query Language) query to search.

  - `api_token?: string | null`

    The API/ Access Token used for Basic, PAT and OAuth2 authentication.

  - `class_name?: string`

  - `cloud_id?: string | null`

    The cloud ID, used in case of OAuth2.

  - `email?: string | null`

    The email address to use for authentication.

  - `server_url?: string | null`

    The server url for Jira Cloud.

  - `supports_access_control?: boolean`

### Cloud Jira Data Source V2

- `CloudJiraDataSourceV2`

  Cloud Jira Data Source integrating JiraReaderV2.

  - `authentication_mechanism: string`

    Type of Authentication for connecting to Jira APIs.

  - `query: string`

    JQL (Jira Query Language) query to search.

  - `server_url: string`

    The server url for Jira Cloud.

  - `api_token?: string | null`

    The API Access Token used for Basic, PAT and OAuth2 authentication.

  - `api_version?: "2" | "3"`

    Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

    - `"2"`

    - `"3"`

  - `class_name?: string`

  - `cloud_id?: string | null`

    The cloud ID, used in case of OAuth2.

  - `email?: string | null`

    The email address to use for authentication.

  - `expand?: string | null`

    Fields to expand in the response.

  - `fields?: Array<string> | null`

    List of fields to retrieve from Jira. If None, retrieves all fields.

  - `get_permissions?: boolean`

    Whether to fetch project role permissions and issue-level security

  - `requests_per_minute?: number | null`

    Rate limit for Jira API requests per minute.

  - `supports_access_control?: boolean`

### Cloud Milvus Vector Store

- `CloudMilvusVectorStore`

  Cloud Milvus Vector Store.

  - `uri: string`

  - `token?: string | null`

  - `class_name?: string`

  - `collection_name?: string | null`

  - `embedding_dimension?: number | null`

  - `supports_nested_metadata_filters?: boolean`

### Cloud MongoDB Atlas Vector Search

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

### Cloud Notion Page Data Source

- `CloudNotionPageDataSource`

  - `integration_token: string`

    The integration token to use for authentication.

  - `class_name?: string`

  - `database_ids?: string | null`

    The Notion Database Id to read content from.

  - `page_ids?: string | null`

    The Page ID's of the Notion to read from.

  - `supports_access_control?: boolean`

### Cloud One Drive Data Source

- `CloudOneDriveDataSource`

  - `client_id: string`

    The client ID to use for authentication.

  - `client_secret: string`

    The client secret to use for authentication.

  - `tenant_id: string`

    The tenant ID to use for authentication.

  - `user_principal_name: string`

    The user principal name to use for authentication.

  - `class_name?: string`

  - `folder_id?: string | null`

    The ID of the OneDrive folder to read from.

  - `folder_path?: string | null`

    The path of the OneDrive folder to read from.

  - `required_exts?: Array<string> | null`

    The list of required file extensions.

  - `supports_access_control?: true`

    - `true`

### Cloud Pinecone Vector Store

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

### Cloud Postgres Vector Store

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

### Cloud Qdrant Vector Store

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

### Cloud S3 Data Source

- `CloudS3DataSource`

  - `bucket: string`

    The name of the S3 bucket to read from.

  - `aws_access_id?: string | null`

    The AWS access ID to use for authentication.

  - `aws_access_secret?: string | null`

    The AWS access secret to use for authentication.

  - `class_name?: string`

  - `prefix?: string | null`

    The prefix of the S3 objects to read from.

  - `regex_pattern?: string | null`

    The regex pattern to filter S3 objects. Must be a valid regex pattern.

  - `s3_endpoint_url?: string | null`

    The S3 endpoint URL to use for authentication.

  - `supports_access_control?: boolean`

### Cloud Sharepoint Data Source

- `CloudSharepointDataSource`

  - `client_id: string`

    The client ID to use for authentication.

  - `client_secret: string`

    The client secret to use for authentication.

  - `tenant_id: string`

    The tenant ID to use for authentication.

  - `class_name?: string`

  - `drive_name?: string | null`

    The name of the Sharepoint drive to read from.

  - `exclude_path_patterns?: Array<string> | null`

    List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

  - `folder_id?: string | null`

    The ID of the Sharepoint folder to read from.

  - `folder_path?: string | null`

    The path of the Sharepoint folder to read from.

  - `get_permissions?: boolean | null`

    Whether to get permissions for the sharepoint site.

  - `include_path_patterns?: Array<string> | null`

    List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

  - `required_exts?: Array<string> | null`

    The list of required file extensions.

  - `site_id?: string | null`

    The ID of the SharePoint site to download from.

  - `site_name?: string | null`

    The name of the SharePoint site to download from.

  - `supports_access_control?: true`

    - `true`

### Cloud Slack Data Source

- `CloudSlackDataSource`

  - `slack_token: string`

    Slack Bot Token.

  - `channel_ids?: string | null`

    Slack Channel.

  - `channel_patterns?: string | null`

    Slack Channel name pattern.

  - `class_name?: string`

  - `earliest_date?: string | null`

    Earliest date.

  - `earliest_date_timestamp?: number | null`

    Earliest date timestamp.

  - `latest_date?: string | null`

    Latest date.

  - `latest_date_timestamp?: number | null`

    Latest date timestamp.

  - `supports_access_control?: boolean`

### Failure Handling Config

- `FailureHandlingConfig`

  Configuration for handling different types of failures during data source processing.

  - `skip_list_failures?: boolean`

    Whether to skip failed batches/lists and continue processing

### Pg Vector Hnsw Settings

- `PgVectorHnswSettings`

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
