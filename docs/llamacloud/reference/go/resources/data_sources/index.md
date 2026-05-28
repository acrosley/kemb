# Data Sources

## List Data Sources

`client.DataSources.List(ctx, query) (*[]DataSource, error)`

**get** `/api/v1/data-sources`

List data sources for a given project.
If project_id is not provided, uses the default project.

### Parameters

- `query DataSourceListParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type DataSourceListResponse []DataSource`

  - `ID string`

    Unique identifier

  - `Component DataSourceComponentUnion`

    Component that implements the data source

    - `type DataSourceComponentMap map[string, any]`

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

    - `type CloudGoogleDriveDataSource struct{…}`

      - `FolderID string`

        The ID of the Google Drive folder to read from.

      - `ClassName string`

      - `ServiceAccountKey map[string, string]`

        A dictionary containing secret values

      - `SupportsAccessControl bool`

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

    - `type CloudNotionPageDataSource struct{…}`

      - `IntegrationToken string`

        The integration token to use for authentication.

      - `ClassName string`

      - `DatabaseIDs string`

        The Notion Database Id to read content from.

      - `PageIDs string`

        The Page ID's of the Notion to read from.

      - `SupportsAccessControl bool`

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

  - `Name string`

    The name of the data source.

  - `ProjectID string`

  - `SourceType DataSourceSourceType`

    - `const DataSourceSourceTypeS3 DataSourceSourceType = "S3"`

    - `const DataSourceSourceTypeAzureStorageBlob DataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const DataSourceSourceTypeGoogleDrive DataSourceSourceType = "GOOGLE_DRIVE"`

    - `const DataSourceSourceTypeMicrosoftOnedrive DataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const DataSourceSourceTypeMicrosoftSharepoint DataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const DataSourceSourceTypeSlack DataSourceSourceType = "SLACK"`

    - `const DataSourceSourceTypeNotionPage DataSourceSourceType = "NOTION_PAGE"`

    - `const DataSourceSourceTypeConfluence DataSourceSourceType = "CONFLUENCE"`

    - `const DataSourceSourceTypeJira DataSourceSourceType = "JIRA"`

    - `const DataSourceSourceTypeJiraV2 DataSourceSourceType = "JIRA_V2"`

    - `const DataSourceSourceTypeBox DataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, DataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type DataSourceCustomMetadataMap map[string, any]`

    - `type DataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

  - `VersionMetadata DataSourceReaderVersionMetadata`

    Version metadata for the data source

    - `ReaderVersion DataSourceReaderVersionMetadataReaderVersion`

      The version of the reader to use for this data source.

      - `const DataSourceReaderVersionMetadataReaderVersion1_0 DataSourceReaderVersionMetadataReaderVersion = "1.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_0 DataSourceReaderVersionMetadataReaderVersion = "2.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_1 DataSourceReaderVersionMetadataReaderVersion = "2.1"`

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
  dataSources, err := client.DataSources.List(context.TODO(), llamacloudprod.DataSourceListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", dataSources)
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
    "source_type": "S3",
    "created_at": "2019-12-27T18:11:19.117Z",
    "custom_metadata": {
      "foo": {
        "foo": "bar"
      }
    },
    "updated_at": "2019-12-27T18:11:19.117Z",
    "version_metadata": {
      "reader_version": "1.0"
    }
  }
]
```

## Create Data Source

`client.DataSources.New(ctx, params) (*DataSource, error)`

**post** `/api/v1/data-sources`

Create a new data source.

### Parameters

- `params DataSourceNewParams`

  - `Component param.Field[DataSourceNewParamsComponentUnion]`

    Body param: Component that implements the data source

    - `type DataSourceNewParamsComponentMap map[string, any]`

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

    - `type CloudGoogleDriveDataSource struct{…}`

      - `FolderID string`

        The ID of the Google Drive folder to read from.

      - `ClassName string`

      - `ServiceAccountKey map[string, string]`

        A dictionary containing secret values

      - `SupportsAccessControl bool`

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

    - `type CloudNotionPageDataSource struct{…}`

      - `IntegrationToken string`

        The integration token to use for authentication.

      - `ClassName string`

      - `DatabaseIDs string`

        The Notion Database Id to read content from.

      - `PageIDs string`

        The Page ID's of the Notion to read from.

      - `SupportsAccessControl bool`

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

  - `Name param.Field[string]`

    Body param: The name of the data source.

  - `SourceType param.Field[DataSourceNewParamsSourceType]`

    Body param

    - `const DataSourceNewParamsSourceTypeS3 DataSourceNewParamsSourceType = "S3"`

    - `const DataSourceNewParamsSourceTypeAzureStorageBlob DataSourceNewParamsSourceType = "AZURE_STORAGE_BLOB"`

    - `const DataSourceNewParamsSourceTypeGoogleDrive DataSourceNewParamsSourceType = "GOOGLE_DRIVE"`

    - `const DataSourceNewParamsSourceTypeMicrosoftOnedrive DataSourceNewParamsSourceType = "MICROSOFT_ONEDRIVE"`

    - `const DataSourceNewParamsSourceTypeMicrosoftSharepoint DataSourceNewParamsSourceType = "MICROSOFT_SHAREPOINT"`

    - `const DataSourceNewParamsSourceTypeSlack DataSourceNewParamsSourceType = "SLACK"`

    - `const DataSourceNewParamsSourceTypeNotionPage DataSourceNewParamsSourceType = "NOTION_PAGE"`

    - `const DataSourceNewParamsSourceTypeConfluence DataSourceNewParamsSourceType = "CONFLUENCE"`

    - `const DataSourceNewParamsSourceTypeJira DataSourceNewParamsSourceType = "JIRA"`

    - `const DataSourceNewParamsSourceTypeJiraV2 DataSourceNewParamsSourceType = "JIRA_V2"`

    - `const DataSourceNewParamsSourceTypeBox DataSourceNewParamsSourceType = "BOX"`

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `CustomMetadata param.Field[map[string, DataSourceNewParamsCustomMetadataUnion]]`

    Body param: Custom metadata that will be present on all data loaded from the data source

    - `type DataSourceNewParamsCustomMetadataMap map[string, any]`

    - `type DataSourceNewParamsCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

### Returns

- `type DataSource struct{…}`

  Schema for a data source.

  - `ID string`

    Unique identifier

  - `Component DataSourceComponentUnion`

    Component that implements the data source

    - `type DataSourceComponentMap map[string, any]`

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

    - `type CloudGoogleDriveDataSource struct{…}`

      - `FolderID string`

        The ID of the Google Drive folder to read from.

      - `ClassName string`

      - `ServiceAccountKey map[string, string]`

        A dictionary containing secret values

      - `SupportsAccessControl bool`

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

    - `type CloudNotionPageDataSource struct{…}`

      - `IntegrationToken string`

        The integration token to use for authentication.

      - `ClassName string`

      - `DatabaseIDs string`

        The Notion Database Id to read content from.

      - `PageIDs string`

        The Page ID's of the Notion to read from.

      - `SupportsAccessControl bool`

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

  - `Name string`

    The name of the data source.

  - `ProjectID string`

  - `SourceType DataSourceSourceType`

    - `const DataSourceSourceTypeS3 DataSourceSourceType = "S3"`

    - `const DataSourceSourceTypeAzureStorageBlob DataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const DataSourceSourceTypeGoogleDrive DataSourceSourceType = "GOOGLE_DRIVE"`

    - `const DataSourceSourceTypeMicrosoftOnedrive DataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const DataSourceSourceTypeMicrosoftSharepoint DataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const DataSourceSourceTypeSlack DataSourceSourceType = "SLACK"`

    - `const DataSourceSourceTypeNotionPage DataSourceSourceType = "NOTION_PAGE"`

    - `const DataSourceSourceTypeConfluence DataSourceSourceType = "CONFLUENCE"`

    - `const DataSourceSourceTypeJira DataSourceSourceType = "JIRA"`

    - `const DataSourceSourceTypeJiraV2 DataSourceSourceType = "JIRA_V2"`

    - `const DataSourceSourceTypeBox DataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, DataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type DataSourceCustomMetadataMap map[string, any]`

    - `type DataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

  - `VersionMetadata DataSourceReaderVersionMetadata`

    Version metadata for the data source

    - `ReaderVersion DataSourceReaderVersionMetadataReaderVersion`

      The version of the reader to use for this data source.

      - `const DataSourceReaderVersionMetadataReaderVersion1_0 DataSourceReaderVersionMetadataReaderVersion = "1.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_0 DataSourceReaderVersionMetadataReaderVersion = "2.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_1 DataSourceReaderVersionMetadataReaderVersion = "2.1"`

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
  dataSource, err := client.DataSources.New(context.TODO(), llamacloudprod.DataSourceNewParams{
    Component: llamacloudprod.DataSourceNewParamsComponentUnion{
      OfAnyMap: map[string]any{
      "foo": "bar",
      },
    },
    Name: "name",
    SourceType: llamacloudprod.DataSourceNewParamsSourceTypeS3,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", dataSource.ID)
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
  "source_type": "S3",
  "created_at": "2019-12-27T18:11:19.117Z",
  "custom_metadata": {
    "foo": {
      "foo": "bar"
    }
  },
  "updated_at": "2019-12-27T18:11:19.117Z",
  "version_metadata": {
    "reader_version": "1.0"
  }
}
```

## Get Data Source

`client.DataSources.Get(ctx, dataSourceID) (*DataSource, error)`

**get** `/api/v1/data-sources/{data_source_id}`

Get a data source by ID.

### Parameters

- `dataSourceID string`

### Returns

- `type DataSource struct{…}`

  Schema for a data source.

  - `ID string`

    Unique identifier

  - `Component DataSourceComponentUnion`

    Component that implements the data source

    - `type DataSourceComponentMap map[string, any]`

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

    - `type CloudGoogleDriveDataSource struct{…}`

      - `FolderID string`

        The ID of the Google Drive folder to read from.

      - `ClassName string`

      - `ServiceAccountKey map[string, string]`

        A dictionary containing secret values

      - `SupportsAccessControl bool`

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

    - `type CloudNotionPageDataSource struct{…}`

      - `IntegrationToken string`

        The integration token to use for authentication.

      - `ClassName string`

      - `DatabaseIDs string`

        The Notion Database Id to read content from.

      - `PageIDs string`

        The Page ID's of the Notion to read from.

      - `SupportsAccessControl bool`

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

  - `Name string`

    The name of the data source.

  - `ProjectID string`

  - `SourceType DataSourceSourceType`

    - `const DataSourceSourceTypeS3 DataSourceSourceType = "S3"`

    - `const DataSourceSourceTypeAzureStorageBlob DataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const DataSourceSourceTypeGoogleDrive DataSourceSourceType = "GOOGLE_DRIVE"`

    - `const DataSourceSourceTypeMicrosoftOnedrive DataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const DataSourceSourceTypeMicrosoftSharepoint DataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const DataSourceSourceTypeSlack DataSourceSourceType = "SLACK"`

    - `const DataSourceSourceTypeNotionPage DataSourceSourceType = "NOTION_PAGE"`

    - `const DataSourceSourceTypeConfluence DataSourceSourceType = "CONFLUENCE"`

    - `const DataSourceSourceTypeJira DataSourceSourceType = "JIRA"`

    - `const DataSourceSourceTypeJiraV2 DataSourceSourceType = "JIRA_V2"`

    - `const DataSourceSourceTypeBox DataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, DataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type DataSourceCustomMetadataMap map[string, any]`

    - `type DataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

  - `VersionMetadata DataSourceReaderVersionMetadata`

    Version metadata for the data source

    - `ReaderVersion DataSourceReaderVersionMetadataReaderVersion`

      The version of the reader to use for this data source.

      - `const DataSourceReaderVersionMetadataReaderVersion1_0 DataSourceReaderVersionMetadataReaderVersion = "1.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_0 DataSourceReaderVersionMetadataReaderVersion = "2.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_1 DataSourceReaderVersionMetadataReaderVersion = "2.1"`

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
  dataSource, err := client.DataSources.Get(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", dataSource.ID)
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
  "source_type": "S3",
  "created_at": "2019-12-27T18:11:19.117Z",
  "custom_metadata": {
    "foo": {
      "foo": "bar"
    }
  },
  "updated_at": "2019-12-27T18:11:19.117Z",
  "version_metadata": {
    "reader_version": "1.0"
  }
}
```

## Update Data Source

`client.DataSources.Update(ctx, dataSourceID, body) (*DataSource, error)`

**put** `/api/v1/data-sources/{data_source_id}`

Update a data source by ID.

### Parameters

- `dataSourceID string`

- `body DataSourceUpdateParams`

  - `SourceType param.Field[DataSourceUpdateParamsSourceType]`

    - `const DataSourceUpdateParamsSourceTypeS3 DataSourceUpdateParamsSourceType = "S3"`

    - `const DataSourceUpdateParamsSourceTypeAzureStorageBlob DataSourceUpdateParamsSourceType = "AZURE_STORAGE_BLOB"`

    - `const DataSourceUpdateParamsSourceTypeGoogleDrive DataSourceUpdateParamsSourceType = "GOOGLE_DRIVE"`

    - `const DataSourceUpdateParamsSourceTypeMicrosoftOnedrive DataSourceUpdateParamsSourceType = "MICROSOFT_ONEDRIVE"`

    - `const DataSourceUpdateParamsSourceTypeMicrosoftSharepoint DataSourceUpdateParamsSourceType = "MICROSOFT_SHAREPOINT"`

    - `const DataSourceUpdateParamsSourceTypeSlack DataSourceUpdateParamsSourceType = "SLACK"`

    - `const DataSourceUpdateParamsSourceTypeNotionPage DataSourceUpdateParamsSourceType = "NOTION_PAGE"`

    - `const DataSourceUpdateParamsSourceTypeConfluence DataSourceUpdateParamsSourceType = "CONFLUENCE"`

    - `const DataSourceUpdateParamsSourceTypeJira DataSourceUpdateParamsSourceType = "JIRA"`

    - `const DataSourceUpdateParamsSourceTypeJiraV2 DataSourceUpdateParamsSourceType = "JIRA_V2"`

    - `const DataSourceUpdateParamsSourceTypeBox DataSourceUpdateParamsSourceType = "BOX"`

  - `Component param.Field[DataSourceUpdateParamsComponentUnion]`

    Component that implements the data source

    - `type DataSourceUpdateParamsComponentMap map[string, any]`

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

    - `type CloudGoogleDriveDataSource struct{…}`

      - `FolderID string`

        The ID of the Google Drive folder to read from.

      - `ClassName string`

      - `ServiceAccountKey map[string, string]`

        A dictionary containing secret values

      - `SupportsAccessControl bool`

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

    - `type CloudNotionPageDataSource struct{…}`

      - `IntegrationToken string`

        The integration token to use for authentication.

      - `ClassName string`

      - `DatabaseIDs string`

        The Notion Database Id to read content from.

      - `PageIDs string`

        The Page ID's of the Notion to read from.

      - `SupportsAccessControl bool`

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

  - `CustomMetadata param.Field[map[string, DataSourceUpdateParamsCustomMetadataUnion]]`

    Custom metadata that will be present on all data loaded from the data source

    - `type DataSourceUpdateParamsCustomMetadataMap map[string, any]`

    - `type DataSourceUpdateParamsCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Name param.Field[string]`

    The name of the data source.

### Returns

- `type DataSource struct{…}`

  Schema for a data source.

  - `ID string`

    Unique identifier

  - `Component DataSourceComponentUnion`

    Component that implements the data source

    - `type DataSourceComponentMap map[string, any]`

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

    - `type CloudGoogleDriveDataSource struct{…}`

      - `FolderID string`

        The ID of the Google Drive folder to read from.

      - `ClassName string`

      - `ServiceAccountKey map[string, string]`

        A dictionary containing secret values

      - `SupportsAccessControl bool`

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

    - `type CloudNotionPageDataSource struct{…}`

      - `IntegrationToken string`

        The integration token to use for authentication.

      - `ClassName string`

      - `DatabaseIDs string`

        The Notion Database Id to read content from.

      - `PageIDs string`

        The Page ID's of the Notion to read from.

      - `SupportsAccessControl bool`

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

  - `Name string`

    The name of the data source.

  - `ProjectID string`

  - `SourceType DataSourceSourceType`

    - `const DataSourceSourceTypeS3 DataSourceSourceType = "S3"`

    - `const DataSourceSourceTypeAzureStorageBlob DataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const DataSourceSourceTypeGoogleDrive DataSourceSourceType = "GOOGLE_DRIVE"`

    - `const DataSourceSourceTypeMicrosoftOnedrive DataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const DataSourceSourceTypeMicrosoftSharepoint DataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const DataSourceSourceTypeSlack DataSourceSourceType = "SLACK"`

    - `const DataSourceSourceTypeNotionPage DataSourceSourceType = "NOTION_PAGE"`

    - `const DataSourceSourceTypeConfluence DataSourceSourceType = "CONFLUENCE"`

    - `const DataSourceSourceTypeJira DataSourceSourceType = "JIRA"`

    - `const DataSourceSourceTypeJiraV2 DataSourceSourceType = "JIRA_V2"`

    - `const DataSourceSourceTypeBox DataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, DataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type DataSourceCustomMetadataMap map[string, any]`

    - `type DataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

  - `VersionMetadata DataSourceReaderVersionMetadata`

    Version metadata for the data source

    - `ReaderVersion DataSourceReaderVersionMetadataReaderVersion`

      The version of the reader to use for this data source.

      - `const DataSourceReaderVersionMetadataReaderVersion1_0 DataSourceReaderVersionMetadataReaderVersion = "1.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_0 DataSourceReaderVersionMetadataReaderVersion = "2.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_1 DataSourceReaderVersionMetadataReaderVersion = "2.1"`

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
  dataSource, err := client.DataSources.Update(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.DataSourceUpdateParams{
      SourceType: llamacloudprod.DataSourceUpdateParamsSourceTypeS3,
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", dataSource.ID)
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
  "source_type": "S3",
  "created_at": "2019-12-27T18:11:19.117Z",
  "custom_metadata": {
    "foo": {
      "foo": "bar"
    }
  },
  "updated_at": "2019-12-27T18:11:19.117Z",
  "version_metadata": {
    "reader_version": "1.0"
  }
}
```

## Delete Data Source

`client.DataSources.Delete(ctx, dataSourceID) error`

**delete** `/api/v1/data-sources/{data_source_id}`

Delete a data source by ID.

### Parameters

- `dataSourceID string`

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
  err := client.DataSources.Delete(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
  if err != nil {
    panic(err.Error())
  }
}
```

## Domain Types

### Data Source

- `type DataSource struct{…}`

  Schema for a data source.

  - `ID string`

    Unique identifier

  - `Component DataSourceComponentUnion`

    Component that implements the data source

    - `type DataSourceComponentMap map[string, any]`

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

    - `type CloudGoogleDriveDataSource struct{…}`

      - `FolderID string`

        The ID of the Google Drive folder to read from.

      - `ClassName string`

      - `ServiceAccountKey map[string, string]`

        A dictionary containing secret values

      - `SupportsAccessControl bool`

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

    - `type CloudNotionPageDataSource struct{…}`

      - `IntegrationToken string`

        The integration token to use for authentication.

      - `ClassName string`

      - `DatabaseIDs string`

        The Notion Database Id to read content from.

      - `PageIDs string`

        The Page ID's of the Notion to read from.

      - `SupportsAccessControl bool`

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

  - `Name string`

    The name of the data source.

  - `ProjectID string`

  - `SourceType DataSourceSourceType`

    - `const DataSourceSourceTypeS3 DataSourceSourceType = "S3"`

    - `const DataSourceSourceTypeAzureStorageBlob DataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const DataSourceSourceTypeGoogleDrive DataSourceSourceType = "GOOGLE_DRIVE"`

    - `const DataSourceSourceTypeMicrosoftOnedrive DataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const DataSourceSourceTypeMicrosoftSharepoint DataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const DataSourceSourceTypeSlack DataSourceSourceType = "SLACK"`

    - `const DataSourceSourceTypeNotionPage DataSourceSourceType = "NOTION_PAGE"`

    - `const DataSourceSourceTypeConfluence DataSourceSourceType = "CONFLUENCE"`

    - `const DataSourceSourceTypeJira DataSourceSourceType = "JIRA"`

    - `const DataSourceSourceTypeJiraV2 DataSourceSourceType = "JIRA_V2"`

    - `const DataSourceSourceTypeBox DataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, DataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type DataSourceCustomMetadataMap map[string, any]`

    - `type DataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `UpdatedAt Time`

    Update datetime

  - `VersionMetadata DataSourceReaderVersionMetadata`

    Version metadata for the data source

    - `ReaderVersion DataSourceReaderVersionMetadataReaderVersion`

      The version of the reader to use for this data source.

      - `const DataSourceReaderVersionMetadataReaderVersion1_0 DataSourceReaderVersionMetadataReaderVersion = "1.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_0 DataSourceReaderVersionMetadataReaderVersion = "2.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_1 DataSourceReaderVersionMetadataReaderVersion = "2.1"`

### Data Source Reader Version Metadata

- `type DataSourceReaderVersionMetadata struct{…}`

  - `ReaderVersion DataSourceReaderVersionMetadataReaderVersion`

    The version of the reader to use for this data source.

    - `const DataSourceReaderVersionMetadataReaderVersion1_0 DataSourceReaderVersionMetadataReaderVersion = "1.0"`

    - `const DataSourceReaderVersionMetadataReaderVersion2_0 DataSourceReaderVersionMetadataReaderVersion = "2.0"`

    - `const DataSourceReaderVersionMetadataReaderVersion2_1 DataSourceReaderVersionMetadataReaderVersion = "2.1"`
