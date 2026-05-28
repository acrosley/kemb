# Shared

## Domain Types

### Cloud Astra DB Vector Store

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

### Cloud Az Storage Blob Data Source

- `class CloudAzStorageBlobDataSource: …`

  - `account_url: str`

    The Azure Storage Blob account URL to use for authentication.

  - `container_name: str`

    The name of the Azure Storage Blob container to read from.

  - `account_key: Optional[str]`

    The Azure Storage Blob account key to use for authentication.

  - `account_name: Optional[str]`

    The Azure Storage Blob account name to use for authentication.

  - `blob: Optional[str]`

    The blob name to read from.

  - `class_name: Optional[str]`

  - `client_id: Optional[str]`

    The Azure AD client ID to use for authentication.

  - `client_secret: Optional[str]`

    The Azure AD client secret to use for authentication.

  - `prefix: Optional[str]`

    The prefix of the Azure Storage Blob objects to read from.

  - `supports_access_control: Optional[bool]`

  - `tenant_id: Optional[str]`

    The Azure AD tenant ID to use for authentication.

### Cloud Azure AI Search Vector Store

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

### Cloud Box Data Source

- `class CloudBoxDataSource: …`

  - `authentication_mechanism: Literal["developer_token", "ccg"]`

    The type of authentication to use (Developer Token or CCG)

    - `"developer_token"`

    - `"ccg"`

  - `class_name: Optional[str]`

  - `client_id: Optional[str]`

    Box API key used for identifying the application the user is authenticating with

  - `client_secret: Optional[str]`

    Box API secret used for making auth requests.

  - `developer_token: Optional[str]`

    Developer token for authentication if authentication_mechanism is 'developer_token'.

  - `enterprise_id: Optional[str]`

    Box Enterprise ID, if provided authenticates as service.

  - `folder_id: Optional[str]`

    The ID of the Box folder to read from.

  - `supports_access_control: Optional[bool]`

  - `user_id: Optional[str]`

    Box User ID, if provided authenticates as user.

### Cloud Confluence Data Source

- `class CloudConfluenceDataSource: …`

  - `authentication_mechanism: str`

    Type of Authentication for connecting to Confluence APIs.

  - `server_url: str`

    The server URL of the Confluence instance.

  - `api_token: Optional[str]`

    The API token to use for authentication.

  - `class_name: Optional[str]`

  - `cql: Optional[str]`

    The CQL query to use for fetching pages.

  - `failure_handling: Optional[FailureHandlingConfig]`

    Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

    Example:
    {
    "skip_list_failures": true
    }

    Currently supports:

    - skip_list_failures: Skip failed batches/lists and continue processing

    - `skip_list_failures: Optional[bool]`

      Whether to skip failed batches/lists and continue processing

  - `index_restricted_pages: Optional[bool]`

    Whether to index restricted pages.

  - `keep_markdown_format: Optional[bool]`

    Whether to keep the markdown format.

  - `label: Optional[str]`

    The label to use for fetching pages.

  - `page_ids: Optional[str]`

    The page IDs of the Confluence to read from.

  - `space_key: Optional[str]`

    The space key to read from.

  - `supports_access_control: Optional[bool]`

  - `user_name: Optional[str]`

    The username to use for authentication.

### Cloud Google Drive Data Source

- `class CloudGoogleDriveDataSource: …`

  - `folder_id: str`

    The ID of the Google Drive folder to read from.

  - `class_name: Optional[str]`

  - `service_account_key: Optional[Dict[str, str]]`

    A dictionary containing secret values

  - `supports_access_control: Optional[bool]`

### Cloud Jira Data Source

- `class CloudJiraDataSource: …`

  Cloud Jira Data Source integrating JiraReader.

  - `authentication_mechanism: str`

    Type of Authentication for connecting to Jira APIs.

  - `query: str`

    JQL (Jira Query Language) query to search.

  - `api_token: Optional[str]`

    The API/ Access Token used for Basic, PAT and OAuth2 authentication.

  - `class_name: Optional[str]`

  - `cloud_id: Optional[str]`

    The cloud ID, used in case of OAuth2.

  - `email: Optional[str]`

    The email address to use for authentication.

  - `server_url: Optional[str]`

    The server url for Jira Cloud.

  - `supports_access_control: Optional[bool]`

### Cloud Jira Data Source V2

- `class CloudJiraDataSourceV2: …`

  Cloud Jira Data Source integrating JiraReaderV2.

  - `authentication_mechanism: str`

    Type of Authentication for connecting to Jira APIs.

  - `query: str`

    JQL (Jira Query Language) query to search.

  - `server_url: str`

    The server url for Jira Cloud.

  - `api_token: Optional[str]`

    The API Access Token used for Basic, PAT and OAuth2 authentication.

  - `api_version: Optional[Literal["2", "3"]]`

    Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

    - `"2"`

    - `"3"`

  - `class_name: Optional[str]`

  - `cloud_id: Optional[str]`

    The cloud ID, used in case of OAuth2.

  - `email: Optional[str]`

    The email address to use for authentication.

  - `expand: Optional[str]`

    Fields to expand in the response.

  - `fields: Optional[List[str]]`

    List of fields to retrieve from Jira. If None, retrieves all fields.

  - `get_permissions: Optional[bool]`

    Whether to fetch project role permissions and issue-level security

  - `requests_per_minute: Optional[int]`

    Rate limit for Jira API requests per minute.

  - `supports_access_control: Optional[bool]`

### Cloud Milvus Vector Store

- `class CloudMilvusVectorStore: …`

  Cloud Milvus Vector Store.

  - `uri: str`

  - `token: Optional[str]`

  - `class_name: Optional[str]`

  - `collection_name: Optional[str]`

  - `embedding_dimension: Optional[int]`

  - `supports_nested_metadata_filters: Optional[bool]`

### Cloud MongoDB Atlas Vector Search

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

### Cloud Notion Page Data Source

- `class CloudNotionPageDataSource: …`

  - `integration_token: str`

    The integration token to use for authentication.

  - `class_name: Optional[str]`

  - `database_ids: Optional[str]`

    The Notion Database Id to read content from.

  - `page_ids: Optional[str]`

    The Page ID's of the Notion to read from.

  - `supports_access_control: Optional[bool]`

### Cloud One Drive Data Source

- `class CloudOneDriveDataSource: …`

  - `client_id: str`

    The client ID to use for authentication.

  - `client_secret: str`

    The client secret to use for authentication.

  - `tenant_id: str`

    The tenant ID to use for authentication.

  - `user_principal_name: str`

    The user principal name to use for authentication.

  - `class_name: Optional[str]`

  - `folder_id: Optional[str]`

    The ID of the OneDrive folder to read from.

  - `folder_path: Optional[str]`

    The path of the OneDrive folder to read from.

  - `required_exts: Optional[List[str]]`

    The list of required file extensions.

  - `supports_access_control: Optional[Literal[true]]`

    - `true`

### Cloud Pinecone Vector Store

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

### Cloud Postgres Vector Store

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

### Cloud Qdrant Vector Store

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

### Cloud S3 Data Source

- `class CloudS3DataSource: …`

  - `bucket: str`

    The name of the S3 bucket to read from.

  - `aws_access_id: Optional[str]`

    The AWS access ID to use for authentication.

  - `aws_access_secret: Optional[str]`

    The AWS access secret to use for authentication.

  - `class_name: Optional[str]`

  - `prefix: Optional[str]`

    The prefix of the S3 objects to read from.

  - `regex_pattern: Optional[str]`

    The regex pattern to filter S3 objects. Must be a valid regex pattern.

  - `s3_endpoint_url: Optional[str]`

    The S3 endpoint URL to use for authentication.

  - `supports_access_control: Optional[bool]`

### Cloud Sharepoint Data Source

- `class CloudSharepointDataSource: …`

  - `client_id: str`

    The client ID to use for authentication.

  - `client_secret: str`

    The client secret to use for authentication.

  - `tenant_id: str`

    The tenant ID to use for authentication.

  - `class_name: Optional[str]`

  - `drive_name: Optional[str]`

    The name of the Sharepoint drive to read from.

  - `exclude_path_patterns: Optional[List[str]]`

    List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

  - `folder_id: Optional[str]`

    The ID of the Sharepoint folder to read from.

  - `folder_path: Optional[str]`

    The path of the Sharepoint folder to read from.

  - `get_permissions: Optional[bool]`

    Whether to get permissions for the sharepoint site.

  - `include_path_patterns: Optional[List[str]]`

    List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

  - `required_exts: Optional[List[str]]`

    The list of required file extensions.

  - `site_id: Optional[str]`

    The ID of the SharePoint site to download from.

  - `site_name: Optional[str]`

    The name of the SharePoint site to download from.

  - `supports_access_control: Optional[Literal[true]]`

    - `true`

### Cloud Slack Data Source

- `class CloudSlackDataSource: …`

  - `slack_token: str`

    Slack Bot Token.

  - `channel_ids: Optional[str]`

    Slack Channel.

  - `channel_patterns: Optional[str]`

    Slack Channel name pattern.

  - `class_name: Optional[str]`

  - `earliest_date: Optional[str]`

    Earliest date.

  - `earliest_date_timestamp: Optional[float]`

    Earliest date timestamp.

  - `latest_date: Optional[str]`

    Latest date.

  - `latest_date_timestamp: Optional[float]`

    Latest date timestamp.

  - `supports_access_control: Optional[bool]`

### Failure Handling Config

- `class FailureHandlingConfig: …`

  Configuration for handling different types of failures during data source processing.

  - `skip_list_failures: Optional[bool]`

    Whether to skip failed batches/lists and continue processing

### Pg Vector Hnsw Settings

- `class PgVectorHnswSettings: …`

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
