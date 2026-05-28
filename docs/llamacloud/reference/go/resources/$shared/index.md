# Shared

## Domain Types

### Cloud Astra DB Vector Store

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

### Cloud Az Storage Blob Data Source

- `type CloudAzStorageBlobDataSource struct{…}`

  - `AccountURL string`

    The Azure Storage Blob account URL to use for authentication.

  - `ContainerName string`

    The name of the Azure Storage Blob container to read from.

  - `AccountKey string`

    The Azure Storage Blob account key to use for authentication.

  - `AccountName string`

    The Azure Storage Blob account name to use for authentication.

  - `Blob string`

    The blob name to read from.

  - `ClassName string`

  - `ClientID string`

    The Azure AD client ID to use for authentication.

  - `ClientSecret string`

    The Azure AD client secret to use for authentication.

  - `Prefix string`

    The prefix of the Azure Storage Blob objects to read from.

  - `SupportsAccessControl bool`

  - `TenantID string`

    The Azure AD tenant ID to use for authentication.

### Cloud Azure AI Search Vector Store

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

### Cloud Box Data Source

- `type CloudBoxDataSource struct{…}`

  - `AuthenticationMechanism CloudBoxDataSourceAuthenticationMechanism`

    The type of authentication to use (Developer Token or CCG)

    - `const CloudBoxDataSourceAuthenticationMechanismDeveloperToken CloudBoxDataSourceAuthenticationMechanism = "developer_token"`

    - `const CloudBoxDataSourceAuthenticationMechanismCcg CloudBoxDataSourceAuthenticationMechanism = "ccg"`

  - `ClassName string`

  - `ClientID string`

    Box API key used for identifying the application the user is authenticating with

  - `ClientSecret string`

    Box API secret used for making auth requests.

  - `DeveloperToken string`

    Developer token for authentication if authentication_mechanism is 'developer_token'.

  - `EnterpriseID string`

    Box Enterprise ID, if provided authenticates as service.

  - `FolderID string`

    The ID of the Box folder to read from.

  - `SupportsAccessControl bool`

  - `UserID string`

    Box User ID, if provided authenticates as user.

### Cloud Confluence Data Source

- `type CloudConfluenceDataSource struct{…}`

  - `AuthenticationMechanism string`

    Type of Authentication for connecting to Confluence APIs.

  - `ServerURL string`

    The server URL of the Confluence instance.

  - `APIToken string`

    The API token to use for authentication.

  - `ClassName string`

  - `Cql string`

    The CQL query to use for fetching pages.

  - `FailureHandling FailureHandlingConfig`

    Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

    Example:
    {
    "skip_list_failures": true
    }

    Currently supports:

    - skip_list_failures: Skip failed batches/lists and continue processing

    - `SkipListFailures bool`

      Whether to skip failed batches/lists and continue processing

  - `IndexRestrictedPages bool`

    Whether to index restricted pages.

  - `KeepMarkdownFormat bool`

    Whether to keep the markdown format.

  - `Label string`

    The label to use for fetching pages.

  - `PageIDs string`

    The page IDs of the Confluence to read from.

  - `SpaceKey string`

    The space key to read from.

  - `SupportsAccessControl bool`

  - `UserName string`

    The username to use for authentication.

### Cloud Google Drive Data Source

- `type CloudGoogleDriveDataSource struct{…}`

  - `FolderID string`

    The ID of the Google Drive folder to read from.

  - `ClassName string`

  - `ServiceAccountKey map[string, string]`

    A dictionary containing secret values

  - `SupportsAccessControl bool`

### Cloud Jira Data Source

- `type CloudJiraDataSource struct{…}`

  Cloud Jira Data Source integrating JiraReader.

  - `AuthenticationMechanism string`

    Type of Authentication for connecting to Jira APIs.

  - `Query string`

    JQL (Jira Query Language) query to search.

  - `APIToken string`

    The API/ Access Token used for Basic, PAT and OAuth2 authentication.

  - `ClassName string`

  - `CloudID string`

    The cloud ID, used in case of OAuth2.

  - `Email string`

    The email address to use for authentication.

  - `ServerURL string`

    The server url for Jira Cloud.

  - `SupportsAccessControl bool`

### Cloud Jira Data Source V2

- `type CloudJiraDataSourceV2 struct{…}`

  Cloud Jira Data Source integrating JiraReaderV2.

  - `AuthenticationMechanism string`

    Type of Authentication for connecting to Jira APIs.

  - `Query string`

    JQL (Jira Query Language) query to search.

  - `ServerURL string`

    The server url for Jira Cloud.

  - `APIToken string`

    The API Access Token used for Basic, PAT and OAuth2 authentication.

  - `APIVersion CloudJiraDataSourceV2APIVersion`

    Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

    - `const CloudJiraDataSourceV2APIVersion2 CloudJiraDataSourceV2APIVersion = "2"`

    - `const CloudJiraDataSourceV2APIVersion3 CloudJiraDataSourceV2APIVersion = "3"`

  - `ClassName string`

  - `CloudID string`

    The cloud ID, used in case of OAuth2.

  - `Email string`

    The email address to use for authentication.

  - `Expand string`

    Fields to expand in the response.

  - `Fields []string`

    List of fields to retrieve from Jira. If None, retrieves all fields.

  - `GetPermissions bool`

    Whether to fetch project role permissions and issue-level security

  - `RequestsPerMinute int64`

    Rate limit for Jira API requests per minute.

  - `SupportsAccessControl bool`

### Cloud Milvus Vector Store

- `type CloudMilvusVectorStore struct{…}`

  Cloud Milvus Vector Store.

  - `Uri string`

  - `Token string`

  - `ClassName string`

  - `CollectionName string`

  - `EmbeddingDimension int64`

  - `SupportsNestedMetadataFilters bool`

### Cloud MongoDB Atlas Vector Search

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

### Cloud Notion Page Data Source

- `type CloudNotionPageDataSource struct{…}`

  - `IntegrationToken string`

    The integration token to use for authentication.

  - `ClassName string`

  - `DatabaseIDs string`

    The Notion Database Id to read content from.

  - `PageIDs string`

    The Page ID's of the Notion to read from.

  - `SupportsAccessControl bool`

### Cloud One Drive Data Source

- `type CloudOneDriveDataSource struct{…}`

  - `ClientID string`

    The client ID to use for authentication.

  - `ClientSecret string`

    The client secret to use for authentication.

  - `TenantID string`

    The tenant ID to use for authentication.

  - `UserPrincipalName string`

    The user principal name to use for authentication.

  - `ClassName string`

  - `FolderID string`

    The ID of the OneDrive folder to read from.

  - `FolderPath string`

    The path of the OneDrive folder to read from.

  - `RequiredExts []string`

    The list of required file extensions.

  - `SupportsAccessControl bool`

    - `const CloudOneDriveDataSourceSupportsAccessControlTrue CloudOneDriveDataSourceSupportsAccessControl = true`

### Cloud Pinecone Vector Store

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

### Cloud Postgres Vector Store

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

### Cloud Qdrant Vector Store

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

### Cloud S3 Data Source

- `type CloudS3DataSource struct{…}`

  - `Bucket string`

    The name of the S3 bucket to read from.

  - `AwsAccessID string`

    The AWS access ID to use for authentication.

  - `AwsAccessSecret string`

    The AWS access secret to use for authentication.

  - `ClassName string`

  - `Prefix string`

    The prefix of the S3 objects to read from.

  - `RegexPattern string`

    The regex pattern to filter S3 objects. Must be a valid regex pattern.

  - `S3EndpointURL string`

    The S3 endpoint URL to use for authentication.

  - `SupportsAccessControl bool`

### Cloud Sharepoint Data Source

- `type CloudSharepointDataSource struct{…}`

  - `ClientID string`

    The client ID to use for authentication.

  - `ClientSecret string`

    The client secret to use for authentication.

  - `TenantID string`

    The tenant ID to use for authentication.

  - `ClassName string`

  - `DriveName string`

    The name of the Sharepoint drive to read from.

  - `ExcludePathPatterns []string`

    List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

  - `FolderID string`

    The ID of the Sharepoint folder to read from.

  - `FolderPath string`

    The path of the Sharepoint folder to read from.

  - `GetPermissions bool`

    Whether to get permissions for the sharepoint site.

  - `IncludePathPatterns []string`

    List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

  - `RequiredExts []string`

    The list of required file extensions.

  - `SiteID string`

    The ID of the SharePoint site to download from.

  - `SiteName string`

    The name of the SharePoint site to download from.

  - `SupportsAccessControl bool`

    - `const CloudSharepointDataSourceSupportsAccessControlTrue CloudSharepointDataSourceSupportsAccessControl = true`

### Cloud Slack Data Source

- `type CloudSlackDataSource struct{…}`

  - `SlackToken string`

    Slack Bot Token.

  - `ChannelIDs string`

    Slack Channel.

  - `ChannelPatterns string`

    Slack Channel name pattern.

  - `ClassName string`

  - `EarliestDate string`

    Earliest date.

  - `EarliestDateTimestamp float64`

    Earliest date timestamp.

  - `LatestDate string`

    Latest date.

  - `LatestDateTimestamp float64`

    Latest date timestamp.

  - `SupportsAccessControl bool`

### Failure Handling Config

- `type FailureHandlingConfig struct{…}`

  Configuration for handling different types of failures during data source processing.

  - `SkipListFailures bool`

    Whether to skip failed batches/lists and continue processing

### Pg Vector Hnsw Settings

- `type PgVectorHnswSettings struct{…}`

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
