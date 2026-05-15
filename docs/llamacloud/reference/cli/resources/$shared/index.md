# Shared

## Domain Types

### Cloud Astra DB Vector Store

- `cloud_astra_db_vector_store: object { token, api_endpoint, collection_name, 4 more }`

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

### Cloud Az Storage Blob Data Source

- `cloud_az_storage_blob_data_source: object { account_url, container_name, account_key, 8 more }`

  - `account_url: string`

    The Azure Storage Blob account URL to use for authentication.

  - `container_name: string`

    The name of the Azure Storage Blob container to read from.

  - `account_key: optional string`

    The Azure Storage Blob account key to use for authentication.

  - `account_name: optional string`

    The Azure Storage Blob account name to use for authentication.

  - `blob: optional string`

    The blob name to read from.

  - `class_name: optional string`

  - `client_id: optional string`

    The Azure AD client ID to use for authentication.

  - `client_secret: optional string`

    The Azure AD client secret to use for authentication.

  - `prefix: optional string`

    The prefix of the Azure Storage Blob objects to read from.

  - `supports_access_control: optional boolean`

  - `tenant_id: optional string`

    The Azure AD tenant ID to use for authentication.

### Cloud Azure AI Search Vector Store

- `cloud_azure_ai_search_vector_store: object { search_service_api_key, search_service_endpoint, class_name, 8 more }`

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

### Cloud Box Data Source

- `cloud_box_data_source: object { authentication_mechanism, class_name, client_id, 6 more }`

  - `authentication_mechanism: "developer_token" or "ccg"`

    The type of authentication to use (Developer Token or CCG)

    - `"developer_token"`

    - `"ccg"`

  - `class_name: optional string`

  - `client_id: optional string`

    Box API key used for identifying the application the user is authenticating with

  - `client_secret: optional string`

    Box API secret used for making auth requests.

  - `developer_token: optional string`

    Developer token for authentication if authentication_mechanism is 'developer_token'.

  - `enterprise_id: optional string`

    Box Enterprise ID, if provided authenticates as service.

  - `folder_id: optional string`

    The ID of the Box folder to read from.

  - `supports_access_control: optional boolean`

  - `user_id: optional string`

    Box User ID, if provided authenticates as user.

### Cloud Confluence Data Source

- `cloud_confluence_data_source: object { authentication_mechanism, server_url, api_token, 10 more }`

  - `authentication_mechanism: string`

    Type of Authentication for connecting to Confluence APIs.

  - `server_url: string`

    The server URL of the Confluence instance.

  - `api_token: optional string`

    The API token to use for authentication.

  - `class_name: optional string`

  - `cql: optional string`

    The CQL query to use for fetching pages.

  - `failure_handling: optional object { skip_list_failures }`

    Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

    Example:
    {
    "skip_list_failures": true
    }

    Currently supports:

    - skip_list_failures: Skip failed batches/lists and continue processing

    - `skip_list_failures: optional boolean`

      Whether to skip failed batches/lists and continue processing

  - `index_restricted_pages: optional boolean`

    Whether to index restricted pages.

  - `keep_markdown_format: optional boolean`

    Whether to keep the markdown format.

  - `label: optional string`

    The label to use for fetching pages.

  - `page_ids: optional string`

    The page IDs of the Confluence to read from.

  - `space_key: optional string`

    The space key to read from.

  - `supports_access_control: optional boolean`

  - `user_name: optional string`

    The username to use for authentication.

### Cloud Google Drive Data Source

- `cloud_google_drive_data_source: object { folder_id, class_name, service_account_key, supports_access_control }`

  - `folder_id: string`

    The ID of the Google Drive folder to read from.

  - `class_name: optional string`

  - `service_account_key: optional map[string]`

    A dictionary containing secret values

  - `supports_access_control: optional boolean`

### Cloud Jira Data Source

- `cloud_jira_data_source: object { authentication_mechanism, query, api_token, 5 more }`

  Cloud Jira Data Source integrating JiraReader.

  - `authentication_mechanism: string`

    Type of Authentication for connecting to Jira APIs.

  - `query: string`

    JQL (Jira Query Language) query to search.

  - `api_token: optional string`

    The API/ Access Token used for Basic, PAT and OAuth2 authentication.

  - `class_name: optional string`

  - `cloud_id: optional string`

    The cloud ID, used in case of OAuth2.

  - `email: optional string`

    The email address to use for authentication.

  - `server_url: optional string`

    The server url for Jira Cloud.

  - `supports_access_control: optional boolean`

### Cloud Jira Data Source V2

- `cloud_jira_data_source_v2: object { authentication_mechanism, query, server_url, 10 more }`

  Cloud Jira Data Source integrating JiraReaderV2.

  - `authentication_mechanism: string`

    Type of Authentication for connecting to Jira APIs.

  - `query: string`

    JQL (Jira Query Language) query to search.

  - `server_url: string`

    The server url for Jira Cloud.

  - `api_token: optional string`

    The API Access Token used for Basic, PAT and OAuth2 authentication.

  - `api_version: optional "2" or "3"`

    Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

    - `"2"`

    - `"3"`

  - `class_name: optional string`

  - `cloud_id: optional string`

    The cloud ID, used in case of OAuth2.

  - `email: optional string`

    The email address to use for authentication.

  - `expand: optional string`

    Fields to expand in the response.

  - `fields: optional array of string`

    List of fields to retrieve from Jira. If None, retrieves all fields.

  - `get_permissions: optional boolean`

    Whether to fetch project role permissions and issue-level security

  - `requests_per_minute: optional number`

    Rate limit for Jira API requests per minute.

  - `supports_access_control: optional boolean`

### Cloud Milvus Vector Store

- `cloud_milvus_vector_store: object { uri, token, class_name, 3 more }`

  Cloud Milvus Vector Store.

  - `uri: string`

  - `token: optional string`

  - `class_name: optional string`

  - `collection_name: optional string`

  - `embedding_dimension: optional number`

  - `supports_nested_metadata_filters: optional boolean`

### Cloud MongoDB Atlas Vector Search

- `cloud_mongodb_atlas_vector_search: object { collection_name, db_name, mongodb_uri, 5 more }`

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

### Cloud Notion Page Data Source

- `cloud_notion_page_data_source: object { integration_token, class_name, database_ids, 2 more }`

  - `integration_token: string`

    The integration token to use for authentication.

  - `class_name: optional string`

  - `database_ids: optional string`

    The Notion Database Id to read content from.

  - `page_ids: optional string`

    The Page ID's of the Notion to read from.

  - `supports_access_control: optional boolean`

### Cloud One Drive Data Source

- `cloud_one_drive_data_source: object { client_id, client_secret, tenant_id, 6 more }`

  - `client_id: string`

    The client ID to use for authentication.

  - `client_secret: string`

    The client secret to use for authentication.

  - `tenant_id: string`

    The tenant ID to use for authentication.

  - `user_principal_name: string`

    The user principal name to use for authentication.

  - `class_name: optional string`

  - `folder_id: optional string`

    The ID of the OneDrive folder to read from.

  - `folder_path: optional string`

    The path of the OneDrive folder to read from.

  - `required_exts: optional array of string`

    The list of required file extensions.

  - `supports_access_control: optional true`

    - `true`

### Cloud Pinecone Vector Store

- `cloud_pinecone_vector_store: object { api_key, index_name, class_name, 3 more }`

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

### Cloud Postgres Vector Store

- `cloud_postgres_vector_store: object { database, embed_dim, host, 10 more }`

  - `database: string`

  - `embed_dim: number`

  - `host: string`

  - `password: string`

  - `port: number`

  - `schema_name: string`

  - `table_name: string`

  - `user: string`

  - `class_name: optional string`

  - `hnsw_settings: optional object { distance_method, ef_construction, ef_search, 2 more }`

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

### Cloud Qdrant Vector Store

- `cloud_qdrant_vector_store: object { api_key, collection_name, url, 4 more }`

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

### Cloud S3 Data Source

- `cloud_s3_data_source: object { bucket, aws_access_id, aws_access_secret, 5 more }`

  - `bucket: string`

    The name of the S3 bucket to read from.

  - `aws_access_id: optional string`

    The AWS access ID to use for authentication.

  - `aws_access_secret: optional string`

    The AWS access secret to use for authentication.

  - `class_name: optional string`

  - `prefix: optional string`

    The prefix of the S3 objects to read from.

  - `regex_pattern: optional string`

    The regex pattern to filter S3 objects. Must be a valid regex pattern.

  - `s3_endpoint_url: optional string`

    The S3 endpoint URL to use for authentication.

  - `supports_access_control: optional boolean`

### Cloud Sharepoint Data Source

- `cloud_sharepoint_data_source: object { client_id, client_secret, tenant_id, 11 more }`

  - `client_id: string`

    The client ID to use for authentication.

  - `client_secret: string`

    The client secret to use for authentication.

  - `tenant_id: string`

    The tenant ID to use for authentication.

  - `class_name: optional string`

  - `drive_name: optional string`

    The name of the Sharepoint drive to read from.

  - `exclude_path_patterns: optional array of string`

    List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

  - `folder_id: optional string`

    The ID of the Sharepoint folder to read from.

  - `folder_path: optional string`

    The path of the Sharepoint folder to read from.

  - `get_permissions: optional boolean`

    Whether to get permissions for the sharepoint site.

  - `include_path_patterns: optional array of string`

    List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

  - `required_exts: optional array of string`

    The list of required file extensions.

  - `site_id: optional string`

    The ID of the SharePoint site to download from.

  - `site_name: optional string`

    The name of the SharePoint site to download from.

  - `supports_access_control: optional true`

    - `true`

### Cloud Slack Data Source

- `cloud_slack_data_source: object { slack_token, channel_ids, channel_patterns, 6 more }`

  - `slack_token: string`

    Slack Bot Token.

  - `channel_ids: optional string`

    Slack Channel.

  - `channel_patterns: optional string`

    Slack Channel name pattern.

  - `class_name: optional string`

  - `earliest_date: optional string`

    Earliest date.

  - `earliest_date_timestamp: optional number`

    Earliest date timestamp.

  - `latest_date: optional string`

    Latest date.

  - `latest_date_timestamp: optional number`

    Latest date timestamp.

  - `supports_access_control: optional boolean`

### Failure Handling Config

- `failure_handling_config: object { skip_list_failures }`

  Configuration for handling different types of failures during data source processing.

  - `skip_list_failures: optional boolean`

    Whether to skip failed batches/lists and continue processing

### Pg Vector Hnsw Settings

- `pg_vector_hnsw_settings: object { distance_method, ef_construction, ef_search, 2 more }`

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
