# Data Sources

## List Pipeline Data Sources

`client.Pipelines.DataSources.GetDataSources(ctx, pipelineID) (*[]PipelineDataSource, error)`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources`

Get data sources for a pipeline.

### Parameters

- `pipelineID string`

### Returns

- `type PipelineDataSourceGetDataSourcesResponse []PipelineDataSource`

  - `ID string`

    Unique identifier

  - `Component PipelineDataSourceComponentUnion`

    Component that implements the data source

    - `type PipelineDataSourceComponentMap map[string, any]`

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

  - `DataSourceID string`

    The ID of the data source.

  - `LastSyncedAt Time`

    The last time the data source was automatically synced.

  - `Name string`

    The name of the data source.

  - `PipelineID string`

    The ID of the pipeline.

  - `ProjectID string`

  - `SourceType PipelineDataSourceSourceType`

    - `const PipelineDataSourceSourceTypeS3 PipelineDataSourceSourceType = "S3"`

    - `const PipelineDataSourceSourceTypeAzureStorageBlob PipelineDataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const PipelineDataSourceSourceTypeGoogleDrive PipelineDataSourceSourceType = "GOOGLE_DRIVE"`

    - `const PipelineDataSourceSourceTypeMicrosoftOnedrive PipelineDataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const PipelineDataSourceSourceTypeMicrosoftSharepoint PipelineDataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const PipelineDataSourceSourceTypeSlack PipelineDataSourceSourceType = "SLACK"`

    - `const PipelineDataSourceSourceTypeNotionPage PipelineDataSourceSourceType = "NOTION_PAGE"`

    - `const PipelineDataSourceSourceTypeConfluence PipelineDataSourceSourceType = "CONFLUENCE"`

    - `const PipelineDataSourceSourceTypeJira PipelineDataSourceSourceType = "JIRA"`

    - `const PipelineDataSourceSourceTypeJiraV2 PipelineDataSourceSourceType = "JIRA_V2"`

    - `const PipelineDataSourceSourceTypeBox PipelineDataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, PipelineDataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type PipelineDataSourceCustomMetadataMap map[string, any]`

    - `type PipelineDataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Status PipelineDataSourceStatus`

    The status of the data source in the pipeline.

    - `const PipelineDataSourceStatusNotStarted PipelineDataSourceStatus = "NOT_STARTED"`

    - `const PipelineDataSourceStatusInProgress PipelineDataSourceStatus = "IN_PROGRESS"`

    - `const PipelineDataSourceStatusSuccess PipelineDataSourceStatus = "SUCCESS"`

    - `const PipelineDataSourceStatusError PipelineDataSourceStatus = "ERROR"`

    - `const PipelineDataSourceStatusCancelled PipelineDataSourceStatus = "CANCELLED"`

  - `StatusUpdatedAt Time`

    The last time the status was updated.

  - `SyncInterval float64`

    The interval at which the data source should be synced.

  - `SyncScheduleSetBy string`

    The id of the user who set the sync schedule.

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
  pipelineDataSources, err := client.Pipelines.DataSources.GetDataSources(context.TODO(), "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", pipelineDataSources)
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
    "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "last_synced_at": "2019-12-27T18:11:19.117Z",
    "name": "name",
    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "source_type": "S3",
    "created_at": "2019-12-27T18:11:19.117Z",
    "custom_metadata": {
      "foo": {
        "foo": "bar"
      }
    },
    "status": "NOT_STARTED",
    "status_updated_at": "2019-12-27T18:11:19.117Z",
    "sync_interval": 0,
    "sync_schedule_set_by": "sync_schedule_set_by",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "version_metadata": {
      "reader_version": "1.0"
    }
  }
]
```

## Add Data Sources To Pipeline

`client.Pipelines.DataSources.UpdateDataSources(ctx, pipelineID, body) (*[]PipelineDataSource, error)`

**put** `/api/v1/pipelines/{pipeline_id}/data-sources`

Add data sources to a pipeline.

### Parameters

- `pipelineID string`

- `body PipelineDataSourceUpdateDataSourcesParams`

  - `Body param.Field[[]PipelineDataSourceUpdateDataSourcesParamsBody]`

    - `DataSourceID string`

      The ID of the data source.

    - `SyncInterval float64`

      The interval at which the data source should be synced. Valid values are: 21600, 43200, 86400

### Returns

- `type PipelineDataSourceUpdateDataSourcesResponse []PipelineDataSource`

  - `ID string`

    Unique identifier

  - `Component PipelineDataSourceComponentUnion`

    Component that implements the data source

    - `type PipelineDataSourceComponentMap map[string, any]`

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

  - `DataSourceID string`

    The ID of the data source.

  - `LastSyncedAt Time`

    The last time the data source was automatically synced.

  - `Name string`

    The name of the data source.

  - `PipelineID string`

    The ID of the pipeline.

  - `ProjectID string`

  - `SourceType PipelineDataSourceSourceType`

    - `const PipelineDataSourceSourceTypeS3 PipelineDataSourceSourceType = "S3"`

    - `const PipelineDataSourceSourceTypeAzureStorageBlob PipelineDataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const PipelineDataSourceSourceTypeGoogleDrive PipelineDataSourceSourceType = "GOOGLE_DRIVE"`

    - `const PipelineDataSourceSourceTypeMicrosoftOnedrive PipelineDataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const PipelineDataSourceSourceTypeMicrosoftSharepoint PipelineDataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const PipelineDataSourceSourceTypeSlack PipelineDataSourceSourceType = "SLACK"`

    - `const PipelineDataSourceSourceTypeNotionPage PipelineDataSourceSourceType = "NOTION_PAGE"`

    - `const PipelineDataSourceSourceTypeConfluence PipelineDataSourceSourceType = "CONFLUENCE"`

    - `const PipelineDataSourceSourceTypeJira PipelineDataSourceSourceType = "JIRA"`

    - `const PipelineDataSourceSourceTypeJiraV2 PipelineDataSourceSourceType = "JIRA_V2"`

    - `const PipelineDataSourceSourceTypeBox PipelineDataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, PipelineDataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type PipelineDataSourceCustomMetadataMap map[string, any]`

    - `type PipelineDataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Status PipelineDataSourceStatus`

    The status of the data source in the pipeline.

    - `const PipelineDataSourceStatusNotStarted PipelineDataSourceStatus = "NOT_STARTED"`

    - `const PipelineDataSourceStatusInProgress PipelineDataSourceStatus = "IN_PROGRESS"`

    - `const PipelineDataSourceStatusSuccess PipelineDataSourceStatus = "SUCCESS"`

    - `const PipelineDataSourceStatusError PipelineDataSourceStatus = "ERROR"`

    - `const PipelineDataSourceStatusCancelled PipelineDataSourceStatus = "CANCELLED"`

  - `StatusUpdatedAt Time`

    The last time the status was updated.

  - `SyncInterval float64`

    The interval at which the data source should be synced.

  - `SyncScheduleSetBy string`

    The id of the user who set the sync schedule.

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
  pipelineDataSources, err := client.Pipelines.DataSources.UpdateDataSources(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDataSourceUpdateDataSourcesParams{
      Body: []llamacloudprod.PipelineDataSourceUpdateDataSourcesParamsBody{llamacloudprod.PipelineDataSourceUpdateDataSourcesParamsBody{
        DataSourceID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", pipelineDataSources)
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
    "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "last_synced_at": "2019-12-27T18:11:19.117Z",
    "name": "name",
    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "source_type": "S3",
    "created_at": "2019-12-27T18:11:19.117Z",
    "custom_metadata": {
      "foo": {
        "foo": "bar"
      }
    },
    "status": "NOT_STARTED",
    "status_updated_at": "2019-12-27T18:11:19.117Z",
    "sync_interval": 0,
    "sync_schedule_set_by": "sync_schedule_set_by",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "version_metadata": {
      "reader_version": "1.0"
    }
  }
]
```

## Update Pipeline Data Source

`client.Pipelines.DataSources.Update(ctx, dataSourceID, params) (*PipelineDataSource, error)`

**put** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}`

Update the configuration of a data source in a pipeline.

### Parameters

- `dataSourceID string`

- `params PipelineDataSourceUpdateParams`

  - `PipelineID param.Field[string]`

    Path param

  - `SyncInterval param.Field[float64]`

    Body param: The interval at which the data source should be synced.

### Returns

- `type PipelineDataSource struct{…}`

  Schema for a data source in a pipeline.

  - `ID string`

    Unique identifier

  - `Component PipelineDataSourceComponentUnion`

    Component that implements the data source

    - `type PipelineDataSourceComponentMap map[string, any]`

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

  - `DataSourceID string`

    The ID of the data source.

  - `LastSyncedAt Time`

    The last time the data source was automatically synced.

  - `Name string`

    The name of the data source.

  - `PipelineID string`

    The ID of the pipeline.

  - `ProjectID string`

  - `SourceType PipelineDataSourceSourceType`

    - `const PipelineDataSourceSourceTypeS3 PipelineDataSourceSourceType = "S3"`

    - `const PipelineDataSourceSourceTypeAzureStorageBlob PipelineDataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const PipelineDataSourceSourceTypeGoogleDrive PipelineDataSourceSourceType = "GOOGLE_DRIVE"`

    - `const PipelineDataSourceSourceTypeMicrosoftOnedrive PipelineDataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const PipelineDataSourceSourceTypeMicrosoftSharepoint PipelineDataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const PipelineDataSourceSourceTypeSlack PipelineDataSourceSourceType = "SLACK"`

    - `const PipelineDataSourceSourceTypeNotionPage PipelineDataSourceSourceType = "NOTION_PAGE"`

    - `const PipelineDataSourceSourceTypeConfluence PipelineDataSourceSourceType = "CONFLUENCE"`

    - `const PipelineDataSourceSourceTypeJira PipelineDataSourceSourceType = "JIRA"`

    - `const PipelineDataSourceSourceTypeJiraV2 PipelineDataSourceSourceType = "JIRA_V2"`

    - `const PipelineDataSourceSourceTypeBox PipelineDataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, PipelineDataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type PipelineDataSourceCustomMetadataMap map[string, any]`

    - `type PipelineDataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Status PipelineDataSourceStatus`

    The status of the data source in the pipeline.

    - `const PipelineDataSourceStatusNotStarted PipelineDataSourceStatus = "NOT_STARTED"`

    - `const PipelineDataSourceStatusInProgress PipelineDataSourceStatus = "IN_PROGRESS"`

    - `const PipelineDataSourceStatusSuccess PipelineDataSourceStatus = "SUCCESS"`

    - `const PipelineDataSourceStatusError PipelineDataSourceStatus = "ERROR"`

    - `const PipelineDataSourceStatusCancelled PipelineDataSourceStatus = "CANCELLED"`

  - `StatusUpdatedAt Time`

    The last time the status was updated.

  - `SyncInterval float64`

    The interval at which the data source should be synced.

  - `SyncScheduleSetBy string`

    The id of the user who set the sync schedule.

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
  pipelineDataSource, err := client.Pipelines.DataSources.Update(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDataSourceUpdateParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", pipelineDataSource.ID)
}
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "component": {
    "foo": "bar"
  },
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "last_synced_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "source_type": "S3",
  "created_at": "2019-12-27T18:11:19.117Z",
  "custom_metadata": {
    "foo": {
      "foo": "bar"
    }
  },
  "status": "NOT_STARTED",
  "status_updated_at": "2019-12-27T18:11:19.117Z",
  "sync_interval": 0,
  "sync_schedule_set_by": "sync_schedule_set_by",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "version_metadata": {
    "reader_version": "1.0"
  }
}
```

## Get Pipeline Data Source Status

`client.Pipelines.DataSources.GetStatus(ctx, dataSourceID, query) (*ManagedIngestionStatusResponse, error)`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status`

Get the status of a data source for a pipeline.

### Parameters

- `dataSourceID string`

- `query PipelineDataSourceGetStatusParams`

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
  managedIngestionStatusResponse, err := client.Pipelines.DataSources.GetStatus(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDataSourceGetStatusParams{
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

## Sync Pipeline Data Source

`client.Pipelines.DataSources.Sync(ctx, dataSourceID, params) (*Pipeline, error)`

**post** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/sync`

Run ingestion for the pipeline data source by incrementally updating the data-sink with upstream changes from data-source.

### Parameters

- `dataSourceID string`

- `params PipelineDataSourceSyncParams`

  - `PipelineID param.Field[string]`

    Path param

  - `PipelineFileIDs param.Field[[]string]`

    Body param

### Returns

- `type Pipeline struct{…}`

  Schema for a pipeline.

  - `ID string`

    Unique identifier

  - `EmbeddingConfig PipelineEmbeddingConfigUnion`

    - `type PipelineEmbeddingConfigManagedOpenAIEmbedding struct{…}`

      - `Component PipelineEmbeddingConfigManagedOpenAIEmbeddingComponent`

        Configuration for the Managed OpenAI embedding model.

        - `ClassName string`

        - `EmbedBatchSize int64`

          The batch size for embedding calls.

        - `ModelName string`

          The name of the OpenAI embedding model.

          - `const PipelineEmbeddingConfigManagedOpenAIEmbeddingComponentModelNameOpenAITextEmbedding3Small PipelineEmbeddingConfigManagedOpenAIEmbeddingComponentModelName = "openai-text-embedding-3-small"`

        - `NumWorkers int64`

          The number of workers to use for async embedding calls.

      - `Type string`

        Type of the embedding model.

        - `const PipelineEmbeddingConfigManagedOpenAIEmbeddingTypeManagedOpenAIEmbedding PipelineEmbeddingConfigManagedOpenAIEmbeddingType = "MANAGED_OPENAI_EMBEDDING"`

    - `type AzureOpenAIEmbeddingConfig struct{…}`

      - `Component AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `AdditionalKwargs map[string, any]`

          Additional kwargs for the OpenAI API.

        - `APIBase string`

          The base URL for Azure deployment.

        - `APIKey string`

          The OpenAI API key.

        - `APIVersion string`

          The version for Azure OpenAI API.

        - `AzureDeployment string`

          The Azure deployment to use.

        - `AzureEndpoint string`

          The Azure endpoint to use.

        - `ClassName string`

        - `DefaultHeaders map[string, string]`

          The default headers for API requests.

        - `Dimensions int64`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `EmbedBatchSize int64`

          The batch size for embedding calls.

        - `MaxRetries int64`

          Maximum number of retries.

        - `ModelName string`

          The name of the OpenAI embedding model.

        - `NumWorkers int64`

          The number of workers to use for async embedding calls.

        - `ReuseClient bool`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `Timeout float64`

          Timeout for each request.

      - `Type AzureOpenAIEmbeddingConfigType`

        Type of the embedding model.

        - `const AzureOpenAIEmbeddingConfigTypeAzureEmbedding AzureOpenAIEmbeddingConfigType = "AZURE_EMBEDDING"`

    - `type CohereEmbeddingConfig struct{…}`

      - `Component CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `APIKey string`

          The Cohere API key.

        - `ClassName string`

        - `EmbedBatchSize int64`

          The batch size for embedding calls.

        - `EmbeddingType string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `InputType string`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `ModelName string`

          The modelId of the Cohere model to use.

        - `NumWorkers int64`

          The number of workers to use for async embedding calls.

        - `Truncate string`

          Truncation type - START/ END/ NONE

      - `Type CohereEmbeddingConfigType`

        Type of the embedding model.

        - `const CohereEmbeddingConfigTypeCohereEmbedding CohereEmbeddingConfigType = "COHERE_EMBEDDING"`

    - `type GeminiEmbeddingConfig struct{…}`

      - `Component GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `APIBase string`

          API base to access the model. Defaults to None.

        - `APIKey string`

          API key to access the model. Defaults to None.

        - `ClassName string`

        - `EmbedBatchSize int64`

          The batch size for embedding calls.

        - `ModelName string`

          The modelId of the Gemini model to use.

        - `NumWorkers int64`

          The number of workers to use for async embedding calls.

        - `OutputDimensionality int64`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `TaskType string`

          The task for embedding model.

        - `Title string`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `Transport string`

          Transport to access the model. Defaults to None.

      - `Type GeminiEmbeddingConfigType`

        Type of the embedding model.

        - `const GeminiEmbeddingConfigTypeGeminiEmbedding GeminiEmbeddingConfigType = "GEMINI_EMBEDDING"`

    - `type HuggingFaceInferenceAPIEmbeddingConfig struct{…}`

      - `Component HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `Token HuggingFaceInferenceAPIEmbeddingTokenUnion`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `bool`

        - `ClassName string`

        - `Cookies map[string, string]`

          Additional cookies to send to the server.

        - `EmbedBatchSize int64`

          The batch size for embedding calls.

        - `Headers map[string, string]`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `ModelName string`

          Hugging Face model name. If None, the task will be used.

        - `NumWorkers int64`

          The number of workers to use for async embedding calls.

        - `Pooling HuggingFaceInferenceAPIEmbeddingPooling`

          Enum of possible pooling choices with pooling behaviors.

          - `const HuggingFaceInferenceAPIEmbeddingPoolingCls HuggingFaceInferenceAPIEmbeddingPooling = "cls"`

          - `const HuggingFaceInferenceAPIEmbeddingPoolingMean HuggingFaceInferenceAPIEmbeddingPooling = "mean"`

          - `const HuggingFaceInferenceAPIEmbeddingPoolingLast HuggingFaceInferenceAPIEmbeddingPooling = "last"`

        - `QueryInstruction string`

          Instruction to prepend during query embedding.

        - `Task string`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `TextInstruction string`

          Instruction to prepend during text embedding.

        - `Timeout float64`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `Type HuggingFaceInferenceAPIEmbeddingConfigType`

        Type of the embedding model.

        - `const HuggingFaceInferenceAPIEmbeddingConfigTypeHuggingfaceAPIEmbedding HuggingFaceInferenceAPIEmbeddingConfigType = "HUGGINGFACE_API_EMBEDDING"`

    - `type OpenAIEmbeddingConfig struct{…}`

      - `Component OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `AdditionalKwargs map[string, any]`

          Additional kwargs for the OpenAI API.

        - `APIBase string`

          The base URL for OpenAI API.

        - `APIKey string`

          The OpenAI API key.

        - `APIVersion string`

          The version for OpenAI API.

        - `ClassName string`

        - `DefaultHeaders map[string, string]`

          The default headers for API requests.

        - `Dimensions int64`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `EmbedBatchSize int64`

          The batch size for embedding calls.

        - `MaxRetries int64`

          Maximum number of retries.

        - `ModelName string`

          The name of the OpenAI embedding model.

        - `NumWorkers int64`

          The number of workers to use for async embedding calls.

        - `ReuseClient bool`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `Timeout float64`

          Timeout for each request.

      - `Type OpenAIEmbeddingConfigType`

        Type of the embedding model.

        - `const OpenAIEmbeddingConfigTypeOpenAIEmbedding OpenAIEmbeddingConfigType = "OPENAI_EMBEDDING"`

    - `type VertexAIEmbeddingConfig struct{…}`

      - `Component VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `ClientEmail string`

          The client email for the VertexAI credentials.

        - `Location string`

          The default location to use when making API calls.

        - `PrivateKey string`

          The private key for the VertexAI credentials.

        - `PrivateKeyID string`

          The private key ID for the VertexAI credentials.

        - `Project string`

          The default GCP project to use when making Vertex API calls.

        - `TokenUri string`

          The token URI for the VertexAI credentials.

        - `AdditionalKwargs map[string, any]`

          Additional kwargs for the Vertex.

        - `ClassName string`

        - `EmbedBatchSize int64`

          The batch size for embedding calls.

        - `EmbedMode VertexTextEmbeddingEmbedMode`

          The embedding mode to use.

          - `const VertexTextEmbeddingEmbedModeDefault VertexTextEmbeddingEmbedMode = "default"`

          - `const VertexTextEmbeddingEmbedModeClassification VertexTextEmbeddingEmbedMode = "classification"`

          - `const VertexTextEmbeddingEmbedModeClustering VertexTextEmbeddingEmbedMode = "clustering"`

          - `const VertexTextEmbeddingEmbedModeSimilarity VertexTextEmbeddingEmbedMode = "similarity"`

          - `const VertexTextEmbeddingEmbedModeRetrieval VertexTextEmbeddingEmbedMode = "retrieval"`

        - `ModelName string`

          The modelId of the VertexAI model to use.

        - `NumWorkers int64`

          The number of workers to use for async embedding calls.

      - `Type VertexAIEmbeddingConfigType`

        Type of the embedding model.

        - `const VertexAIEmbeddingConfigTypeVertexaiEmbedding VertexAIEmbeddingConfigType = "VERTEXAI_EMBEDDING"`

    - `type BedrockEmbeddingConfig struct{…}`

      - `Component BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `AdditionalKwargs map[string, any]`

          Additional kwargs for the bedrock client.

        - `AwsAccessKeyID string`

          AWS Access Key ID to use

        - `AwsSecretAccessKey string`

          AWS Secret Access Key to use

        - `AwsSessionToken string`

          AWS Session Token to use

        - `ClassName string`

        - `EmbedBatchSize int64`

          The batch size for embedding calls.

        - `MaxRetries int64`

          The maximum number of API retries.

        - `ModelName string`

          The modelId of the Bedrock model to use.

        - `NumWorkers int64`

          The number of workers to use for async embedding calls.

        - `ProfileName string`

          The name of aws profile to use. If not given, then the default profile is used.

        - `RegionName string`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `Timeout float64`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `Type BedrockEmbeddingConfigType`

        Type of the embedding model.

        - `const BedrockEmbeddingConfigTypeBedrockEmbedding BedrockEmbeddingConfigType = "BEDROCK_EMBEDDING"`

  - `Name string`

  - `ProjectID string`

  - `ConfigHash PipelineConfigHash`

    Hashes for the configuration of a pipeline.

    - `EmbeddingConfigHash string`

      Hash of the embedding config.

    - `ParsingConfigHash string`

      Hash of the llama parse parameters.

    - `TransformConfigHash string`

      Hash of the transform config.

  - `CreatedAt Time`

    Creation datetime

  - `DataSink DataSink`

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

  - `EmbeddingModelConfig PipelineEmbeddingModelConfig`

    Schema for an embedding model config.

    - `ID string`

      Unique identifier

    - `EmbeddingConfig PipelineEmbeddingModelConfigEmbeddingConfigUnion`

      The embedding configuration for the embedding model config.

      - `type AzureOpenAIEmbeddingConfig struct{…}`

      - `type CohereEmbeddingConfig struct{…}`

      - `type GeminiEmbeddingConfig struct{…}`

      - `type HuggingFaceInferenceAPIEmbeddingConfig struct{…}`

      - `type OpenAIEmbeddingConfig struct{…}`

      - `type VertexAIEmbeddingConfig struct{…}`

      - `type BedrockEmbeddingConfig struct{…}`

    - `Name string`

      The name of the embedding model config.

    - `ProjectID string`

    - `CreatedAt Time`

      Creation datetime

    - `UpdatedAt Time`

      Update datetime

  - `EmbeddingModelConfigID string`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `LlamaParseParameters LlamaParseParametersResp`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `AdaptiveLongTable bool`

    - `AggressiveTableExtraction bool`

    - `AnnotateLinks bool`

    - `AutoMode bool`

    - `AutoModeConfigurationJson string`

    - `AutoModeTriggerOnImageInPage bool`

    - `AutoModeTriggerOnRegexpInPage string`

    - `AutoModeTriggerOnTableInPage bool`

    - `AutoModeTriggerOnTextInPage string`

    - `AzureOpenAIAPIVersion string`

    - `AzureOpenAIDeploymentName string`

    - `AzureOpenAIEndpoint string`

    - `AzureOpenAIKey string`

    - `BboxBottom float64`

    - `BboxLeft float64`

    - `BboxRight float64`

    - `BboxTop float64`

    - `BoundingBox string`

    - `CompactMarkdownTable bool`

    - `ComplementalFormattingInstruction string`

    - `ContentGuidelineInstruction string`

    - `ContinuousMode bool`

    - `DisableImageExtraction bool`

    - `DisableOcr bool`

    - `DisableReconstruction bool`

    - `DoNotCache bool`

    - `DoNotUnrollColumns bool`

    - `EnableCostOptimizer bool`

    - `ExtractCharts bool`

    - `ExtractLayout bool`

    - `ExtractPrintedPageNumber bool`

    - `FastMode bool`

    - `FormattingInstruction string`

    - `Gpt4oAPIKey string`

    - `Gpt4oMode bool`

    - `GuessXlsxSheetName bool`

    - `HideFooters bool`

    - `HideHeaders bool`

    - `HighResOcr bool`

    - `HTMLMakeAllElementsVisible bool`

    - `HTMLRemoveFixedElements bool`

    - `HTMLRemoveNavigationElements bool`

    - `HTTPProxy string`

    - `IgnoreDocumentElementsForLayoutDetection bool`

    - `ImagesToSave []string`

      - `const LlamaParseParametersImagesToSaveScreenshot LlamaParseParametersImagesToSave = "screenshot"`

      - `const LlamaParseParametersImagesToSaveEmbedded LlamaParseParametersImagesToSave = "embedded"`

      - `const LlamaParseParametersImagesToSaveLayout LlamaParseParametersImagesToSave = "layout"`

    - `InlineImagesInMarkdown bool`

    - `InputS3Path string`

    - `InputS3Region string`

    - `InputURL string`

    - `InternalIsScreenshotJob bool`

    - `InvalidateCache bool`

    - `IsFormattingInstruction bool`

    - `JobTimeoutExtraTimePerPageInSeconds float64`

    - `JobTimeoutInSeconds float64`

    - `KeepPageSeparatorWhenMergingTables bool`

    - `Languages []ParsingLanguages`

      - `const ParsingLanguagesAf ParsingLanguages = "af"`

      - `const ParsingLanguagesAz ParsingLanguages = "az"`

      - `const ParsingLanguagesBs ParsingLanguages = "bs"`

      - `const ParsingLanguagesCs ParsingLanguages = "cs"`

      - `const ParsingLanguagesCy ParsingLanguages = "cy"`

      - `const ParsingLanguagesDa ParsingLanguages = "da"`

      - `const ParsingLanguagesDe ParsingLanguages = "de"`

      - `const ParsingLanguagesEn ParsingLanguages = "en"`

      - `const ParsingLanguagesEs ParsingLanguages = "es"`

      - `const ParsingLanguagesEt ParsingLanguages = "et"`

      - `const ParsingLanguagesFr ParsingLanguages = "fr"`

      - `const ParsingLanguagesGa ParsingLanguages = "ga"`

      - `const ParsingLanguagesHr ParsingLanguages = "hr"`

      - `const ParsingLanguagesHu ParsingLanguages = "hu"`

      - `const ParsingLanguagesID ParsingLanguages = "id"`

      - `const ParsingLanguagesIs ParsingLanguages = "is"`

      - `const ParsingLanguagesIt ParsingLanguages = "it"`

      - `const ParsingLanguagesKu ParsingLanguages = "ku"`

      - `const ParsingLanguagesLa ParsingLanguages = "la"`

      - `const ParsingLanguagesLt ParsingLanguages = "lt"`

      - `const ParsingLanguagesLv ParsingLanguages = "lv"`

      - `const ParsingLanguagesMi ParsingLanguages = "mi"`

      - `const ParsingLanguagesMs ParsingLanguages = "ms"`

      - `const ParsingLanguagesMt ParsingLanguages = "mt"`

      - `const ParsingLanguagesNl ParsingLanguages = "nl"`

      - `const ParsingLanguagesNo ParsingLanguages = "no"`

      - `const ParsingLanguagesOc ParsingLanguages = "oc"`

      - `const ParsingLanguagesPi ParsingLanguages = "pi"`

      - `const ParsingLanguagesPl ParsingLanguages = "pl"`

      - `const ParsingLanguagesPt ParsingLanguages = "pt"`

      - `const ParsingLanguagesRo ParsingLanguages = "ro"`

      - `const ParsingLanguagesRsLatin ParsingLanguages = "rs_latin"`

      - `const ParsingLanguagesSk ParsingLanguages = "sk"`

      - `const ParsingLanguagesSl ParsingLanguages = "sl"`

      - `const ParsingLanguagesSq ParsingLanguages = "sq"`

      - `const ParsingLanguagesSv ParsingLanguages = "sv"`

      - `const ParsingLanguagesSw ParsingLanguages = "sw"`

      - `const ParsingLanguagesTl ParsingLanguages = "tl"`

      - `const ParsingLanguagesTr ParsingLanguages = "tr"`

      - `const ParsingLanguagesUz ParsingLanguages = "uz"`

      - `const ParsingLanguagesVi ParsingLanguages = "vi"`

      - `const ParsingLanguagesAr ParsingLanguages = "ar"`

      - `const ParsingLanguagesFa ParsingLanguages = "fa"`

      - `const ParsingLanguagesUg ParsingLanguages = "ug"`

      - `const ParsingLanguagesUr ParsingLanguages = "ur"`

      - `const ParsingLanguagesBn ParsingLanguages = "bn"`

      - `const ParsingLanguagesAs ParsingLanguages = "as"`

      - `const ParsingLanguagesMni ParsingLanguages = "mni"`

      - `const ParsingLanguagesRu ParsingLanguages = "ru"`

      - `const ParsingLanguagesRsCyrillic ParsingLanguages = "rs_cyrillic"`

      - `const ParsingLanguagesBe ParsingLanguages = "be"`

      - `const ParsingLanguagesBg ParsingLanguages = "bg"`

      - `const ParsingLanguagesUk ParsingLanguages = "uk"`

      - `const ParsingLanguagesMn ParsingLanguages = "mn"`

      - `const ParsingLanguagesAbq ParsingLanguages = "abq"`

      - `const ParsingLanguagesAdy ParsingLanguages = "ady"`

      - `const ParsingLanguagesKbd ParsingLanguages = "kbd"`

      - `const ParsingLanguagesAva ParsingLanguages = "ava"`

      - `const ParsingLanguagesDar ParsingLanguages = "dar"`

      - `const ParsingLanguagesInh ParsingLanguages = "inh"`

      - `const ParsingLanguagesChe ParsingLanguages = "che"`

      - `const ParsingLanguagesLbe ParsingLanguages = "lbe"`

      - `const ParsingLanguagesLez ParsingLanguages = "lez"`

      - `const ParsingLanguagesTab ParsingLanguages = "tab"`

      - `const ParsingLanguagesTjk ParsingLanguages = "tjk"`

      - `const ParsingLanguagesHi ParsingLanguages = "hi"`

      - `const ParsingLanguagesMr ParsingLanguages = "mr"`

      - `const ParsingLanguagesNe ParsingLanguages = "ne"`

      - `const ParsingLanguagesBh ParsingLanguages = "bh"`

      - `const ParsingLanguagesMai ParsingLanguages = "mai"`

      - `const ParsingLanguagesAng ParsingLanguages = "ang"`

      - `const ParsingLanguagesBho ParsingLanguages = "bho"`

      - `const ParsingLanguagesMah ParsingLanguages = "mah"`

      - `const ParsingLanguagesSck ParsingLanguages = "sck"`

      - `const ParsingLanguagesNew ParsingLanguages = "new"`

      - `const ParsingLanguagesGom ParsingLanguages = "gom"`

      - `const ParsingLanguagesSa ParsingLanguages = "sa"`

      - `const ParsingLanguagesBgc ParsingLanguages = "bgc"`

      - `const ParsingLanguagesTh ParsingLanguages = "th"`

      - `const ParsingLanguagesChSim ParsingLanguages = "ch_sim"`

      - `const ParsingLanguagesChTra ParsingLanguages = "ch_tra"`

      - `const ParsingLanguagesJa ParsingLanguages = "ja"`

      - `const ParsingLanguagesKo ParsingLanguages = "ko"`

      - `const ParsingLanguagesTa ParsingLanguages = "ta"`

      - `const ParsingLanguagesTe ParsingLanguages = "te"`

      - `const ParsingLanguagesKn ParsingLanguages = "kn"`

    - `LayoutAware bool`

    - `LineLevelBoundingBox bool`

    - `MarkdownTableMultilineHeaderSeparator string`

    - `MaxPages int64`

    - `MaxPagesEnforced int64`

    - `MergeTablesAcrossPagesInMarkdown bool`

    - `Model string`

    - `OutlinedTableExtraction bool`

    - `OutputPdfOfDocument bool`

    - `OutputS3PathPrefix string`

    - `OutputS3Region string`

    - `OutputTablesAsHTML bool`

    - `PageErrorTolerance float64`

    - `PageFooterPrefix string`

    - `PageFooterSuffix string`

    - `PageHeaderPrefix string`

    - `PageHeaderSuffix string`

    - `PagePrefix string`

    - `PageSeparator string`

    - `PageSuffix string`

    - `ParseMode ParsingMode`

      Enum for representing the mode of parsing to be used.

      - `const ParsingModeParsePageWithoutLlm ParsingMode = "parse_page_without_llm"`

      - `const ParsingModeParsePageWithLlm ParsingMode = "parse_page_with_llm"`

      - `const ParsingModeParsePageWithLvm ParsingMode = "parse_page_with_lvm"`

      - `const ParsingModeParsePageWithAgent ParsingMode = "parse_page_with_agent"`

      - `const ParsingModeParsePageWithLayoutAgent ParsingMode = "parse_page_with_layout_agent"`

      - `const ParsingModeParseDocumentWithLlm ParsingMode = "parse_document_with_llm"`

      - `const ParsingModeParseDocumentWithLvm ParsingMode = "parse_document_with_lvm"`

      - `const ParsingModeParseDocumentWithAgent ParsingMode = "parse_document_with_agent"`

    - `ParsingInstruction string`

    - `PreciseBoundingBox bool`

    - `PremiumMode bool`

    - `PresentationOutOfBoundsContent bool`

    - `PresentationSkipEmbeddedData bool`

    - `PreserveLayoutAlignmentAcrossPages bool`

    - `PreserveVerySmallText bool`

    - `Preset string`

    - `Priority LlamaParseParametersPriority`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `const LlamaParseParametersPriorityLow LlamaParseParametersPriority = "low"`

      - `const LlamaParseParametersPriorityMedium LlamaParseParametersPriority = "medium"`

      - `const LlamaParseParametersPriorityHigh LlamaParseParametersPriority = "high"`

      - `const LlamaParseParametersPriorityCritical LlamaParseParametersPriority = "critical"`

    - `ProjectID string`

    - `RemoveHiddenText bool`

    - `ReplaceFailedPageMode FailPageMode`

      Enum for representing the different available page error handling modes.

      - `const FailPageModeRawText FailPageMode = "raw_text"`

      - `const FailPageModeBlankPage FailPageMode = "blank_page"`

      - `const FailPageModeErrorMessage FailPageMode = "error_message"`

    - `ReplaceFailedPageWithErrorMessagePrefix string`

    - `ReplaceFailedPageWithErrorMessageSuffix string`

    - `SaveImages bool`

    - `SkipDiagonalText bool`

    - `SpecializedChartParsingAgentic bool`

    - `SpecializedChartParsingEfficient bool`

    - `SpecializedChartParsingPlus bool`

    - `SpecializedImageParsing bool`

    - `SpreadsheetExtractSubTables bool`

    - `SpreadsheetForceFormulaComputation bool`

    - `SpreadsheetIncludeHiddenSheets bool`

    - `StrictModeBuggyFont bool`

    - `StrictModeImageExtraction bool`

    - `StrictModeImageOcr bool`

    - `StrictModeReconstruction bool`

    - `StructuredOutput bool`

    - `StructuredOutputJsonSchema string`

    - `StructuredOutputJsonSchemaName string`

    - `SystemPrompt string`

    - `SystemPromptAppend string`

    - `TakeScreenshot bool`

    - `TargetPages string`

    - `Tier string`

    - `UseVendorMultimodalModel bool`

    - `UserPrompt string`

    - `VendorMultimodalAPIKey string`

    - `VendorMultimodalModelName string`

    - `Version string`

    - `WebhookConfigurations []LlamaParseParametersWebhookConfigurationResp`

      Outbound webhook endpoints to notify on job status changes

      - `WebhookEvents []string`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `const LlamaParseParametersWebhookConfigurationWebhookEventExtractPending LlamaParseParametersWebhookConfigurationWebhookEvent = "extract.pending"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventExtractSuccess LlamaParseParametersWebhookConfigurationWebhookEvent = "extract.success"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventExtractError LlamaParseParametersWebhookConfigurationWebhookEvent = "extract.error"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventExtractPartialSuccess LlamaParseParametersWebhookConfigurationWebhookEvent = "extract.partial_success"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventExtractCancelled LlamaParseParametersWebhookConfigurationWebhookEvent = "extract.cancelled"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventParsePending LlamaParseParametersWebhookConfigurationWebhookEvent = "parse.pending"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventParseRunning LlamaParseParametersWebhookConfigurationWebhookEvent = "parse.running"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventParseSuccess LlamaParseParametersWebhookConfigurationWebhookEvent = "parse.success"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventParseError LlamaParseParametersWebhookConfigurationWebhookEvent = "parse.error"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventParsePartialSuccess LlamaParseParametersWebhookConfigurationWebhookEvent = "parse.partial_success"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventParseCancelled LlamaParseParametersWebhookConfigurationWebhookEvent = "parse.cancelled"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventClassifyPending LlamaParseParametersWebhookConfigurationWebhookEvent = "classify.pending"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventClassifySuccess LlamaParseParametersWebhookConfigurationWebhookEvent = "classify.success"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventClassifyError LlamaParseParametersWebhookConfigurationWebhookEvent = "classify.error"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventClassifyPartialSuccess LlamaParseParametersWebhookConfigurationWebhookEvent = "classify.partial_success"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventClassifyCancelled LlamaParseParametersWebhookConfigurationWebhookEvent = "classify.cancelled"`

        - `const LlamaParseParametersWebhookConfigurationWebhookEventUnmappedEvent LlamaParseParametersWebhookConfigurationWebhookEvent = "unmapped_event"`

      - `WebhookHeaders map[string, string]`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `WebhookOutputFormat string`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `WebhookURL string`

        URL to receive webhook POST notifications

    - `WebhookURL string`

  - `ManagedPipelineID string`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `MetadataConfig PipelineMetadataConfig`

    Metadata configuration for the pipeline.

    - `ExcludedEmbedMetadataKeys []string`

      List of metadata keys to exclude from embeddings

    - `ExcludedLlmMetadataKeys []string`

      List of metadata keys to exclude from LLM during retrieval

  - `PipelineType PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `const PipelineTypePlayground PipelineType = "PLAYGROUND"`

    - `const PipelineTypeManaged PipelineType = "MANAGED"`

  - `PresetRetrievalParameters PresetRetrievalParamsResp`

    Preset retrieval parameters for the pipeline.

    - `Alpha float64`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `ClassName string`

    - `DenseSimilarityCutoff float64`

      Minimum similarity score wrt query for retrieval

    - `DenseSimilarityTopK int64`

      Number of nodes for dense retrieval.

    - `EnableReranking bool`

      Enable reranking for retrieval

    - `FilesTopK int64`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `RerankTopN int64`

      Number of reranked nodes for returning.

    - `RetrievalMode RetrievalMode`

      The retrieval mode for the query.

      - `const RetrievalModeChunks RetrievalMode = "chunks"`

      - `const RetrievalModeFilesViaMetadata RetrievalMode = "files_via_metadata"`

      - `const RetrievalModeFilesViaContent RetrievalMode = "files_via_content"`

      - `const RetrievalModeAutoRouted RetrievalMode = "auto_routed"`

    - `RetrieveImageNodes bool`

      Whether to retrieve image nodes.

    - `RetrievePageFigureNodes bool`

      Whether to retrieve page figure nodes.

    - `RetrievePageScreenshotNodes bool`

      Whether to retrieve page screenshot nodes.

    - `SearchFilters MetadataFilters`

      Metadata filters for vector stores.

      - `Filters []MetadataFiltersFilterUnion`

        - `type MetadataFiltersFilterMetadataFilter struct{…}`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `Key string`

          - `Value MetadataFiltersFilterMetadataFilterValueUnion`

            - `float64`

            - `string`

            - `type MetadataFiltersFilterMetadataFilterValueArray []string`

            - `type MetadataFiltersFilterMetadataFilterValueArray []float64`

            - `type MetadataFiltersFilterMetadataFilterValueArray []int64`

          - `Operator string`

            Vector store filter operator.

            - `const MetadataFiltersFilterMetadataFilterOperatorEquals MetadataFiltersFilterMetadataFilterOperator = "=="`

            - `const MetadataFiltersFilterMetadataFilterOperatorGreater MetadataFiltersFilterMetadataFilterOperator = ">"`

            - `const MetadataFiltersFilterMetadataFilterOperatorLess MetadataFiltersFilterMetadataFilterOperator = "<"`

            - `const MetadataFiltersFilterMetadataFilterOperatorNotEquals MetadataFiltersFilterMetadataFilterOperator = "!="`

            - `const MetadataFiltersFilterMetadataFilterOperatorGreaterOrEquals MetadataFiltersFilterMetadataFilterOperator = ">="`

            - `const MetadataFiltersFilterMetadataFilterOperatorLessOrEquals MetadataFiltersFilterMetadataFilterOperator = "<="`

            - `const MetadataFiltersFilterMetadataFilterOperatorIn MetadataFiltersFilterMetadataFilterOperator = "in"`

            - `const MetadataFiltersFilterMetadataFilterOperatorNin MetadataFiltersFilterMetadataFilterOperator = "nin"`

            - `const MetadataFiltersFilterMetadataFilterOperatorAny MetadataFiltersFilterMetadataFilterOperator = "any"`

            - `const MetadataFiltersFilterMetadataFilterOperatorAll MetadataFiltersFilterMetadataFilterOperator = "all"`

            - `const MetadataFiltersFilterMetadataFilterOperatorTextMatch MetadataFiltersFilterMetadataFilterOperator = "text_match"`

            - `const MetadataFiltersFilterMetadataFilterOperatorTextMatchInsensitive MetadataFiltersFilterMetadataFilterOperator = "text_match_insensitive"`

            - `const MetadataFiltersFilterMetadataFilterOperatorContains MetadataFiltersFilterMetadataFilterOperator = "contains"`

            - `const MetadataFiltersFilterMetadataFilterOperatorIsEmpty MetadataFiltersFilterMetadataFilterOperator = "is_empty"`

        - `type MetadataFilters struct{…}`

          Metadata filters for vector stores.

      - `Condition MetadataFiltersCondition`

        Vector store filter conditions to combine different filters.

        - `const MetadataFiltersConditionAnd MetadataFiltersCondition = "and"`

        - `const MetadataFiltersConditionOr MetadataFiltersCondition = "or"`

        - `const MetadataFiltersConditionNot MetadataFiltersCondition = "not"`

    - `SearchFiltersInferenceSchema map[string, PresetRetrievalParamsSearchFiltersInferenceSchemaUnionResp]`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `type PresetRetrievalParamsSearchFiltersInferenceSchemaMap map[string, any]`

      - `type PresetRetrievalParamsSearchFiltersInferenceSchemaArray []any`

      - `string`

      - `float64`

      - `bool`

    - `SparseSimilarityTopK int64`

      Number of nodes for sparse retrieval.

  - `SparseModelConfig SparseModelConfig`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `ClassName string`

    - `ModelType SparseModelConfigModelType`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `const SparseModelConfigModelTypeSplade SparseModelConfigModelType = "splade"`

      - `const SparseModelConfigModelTypeBm25 SparseModelConfigModelType = "bm25"`

      - `const SparseModelConfigModelTypeAuto SparseModelConfigModelType = "auto"`

  - `Status PipelineStatus`

    Status of the pipeline.

    - `const PipelineStatusCreated PipelineStatus = "CREATED"`

    - `const PipelineStatusDeleting PipelineStatus = "DELETING"`

  - `TransformConfig PipelineTransformConfigUnion`

    Configuration for the transformation.

    - `type AutoTransformConfig struct{…}`

      - `ChunkOverlap int64`

        Chunk overlap for the transformation.

      - `ChunkSize int64`

        Chunk size for the transformation.

      - `Mode AutoTransformConfigMode`

        - `const AutoTransformConfigModeAuto AutoTransformConfigMode = "auto"`

    - `type AdvancedModeTransformConfig struct{…}`

      - `ChunkingConfig AdvancedModeTransformConfigChunkingConfigUnion`

        Configuration for the chunking.

        - `type AdvancedModeTransformConfigChunkingConfigNoneChunkingConfig struct{…}`

          - `Mode string`

            - `const AdvancedModeTransformConfigChunkingConfigNoneChunkingConfigModeNone AdvancedModeTransformConfigChunkingConfigNoneChunkingConfigMode = "none"`

        - `type AdvancedModeTransformConfigChunkingConfigCharacterChunkingConfig struct{…}`

          - `ChunkOverlap int64`

          - `ChunkSize int64`

          - `Mode string`

            - `const AdvancedModeTransformConfigChunkingConfigCharacterChunkingConfigModeCharacter AdvancedModeTransformConfigChunkingConfigCharacterChunkingConfigMode = "character"`

        - `type AdvancedModeTransformConfigChunkingConfigTokenChunkingConfig struct{…}`

          - `ChunkOverlap int64`

          - `ChunkSize int64`

          - `Mode string`

            - `const AdvancedModeTransformConfigChunkingConfigTokenChunkingConfigModeToken AdvancedModeTransformConfigChunkingConfigTokenChunkingConfigMode = "token"`

          - `Separator string`

        - `type AdvancedModeTransformConfigChunkingConfigSentenceChunkingConfig struct{…}`

          - `ChunkOverlap int64`

          - `ChunkSize int64`

          - `Mode string`

            - `const AdvancedModeTransformConfigChunkingConfigSentenceChunkingConfigModeSentence AdvancedModeTransformConfigChunkingConfigSentenceChunkingConfigMode = "sentence"`

          - `ParagraphSeparator string`

          - `Separator string`

        - `type AdvancedModeTransformConfigChunkingConfigSemanticChunkingConfig struct{…}`

          - `BreakpointPercentileThreshold int64`

          - `BufferSize int64`

          - `Mode string`

            - `const AdvancedModeTransformConfigChunkingConfigSemanticChunkingConfigModeSemantic AdvancedModeTransformConfigChunkingConfigSemanticChunkingConfigMode = "semantic"`

      - `Mode AdvancedModeTransformConfigMode`

        - `const AdvancedModeTransformConfigModeAdvanced AdvancedModeTransformConfigMode = "advanced"`

      - `SegmentationConfig AdvancedModeTransformConfigSegmentationConfigUnion`

        Configuration for the segmentation.

        - `type AdvancedModeTransformConfigSegmentationConfigNoneSegmentationConfig struct{…}`

          - `Mode string`

            - `const AdvancedModeTransformConfigSegmentationConfigNoneSegmentationConfigModeNone AdvancedModeTransformConfigSegmentationConfigNoneSegmentationConfigMode = "none"`

        - `type AdvancedModeTransformConfigSegmentationConfigPageSegmentationConfig struct{…}`

          - `Mode string`

            - `const AdvancedModeTransformConfigSegmentationConfigPageSegmentationConfigModePage AdvancedModeTransformConfigSegmentationConfigPageSegmentationConfigMode = "page"`

          - `PageSeparator string`

        - `type AdvancedModeTransformConfigSegmentationConfigElementSegmentationConfig struct{…}`

          - `Mode string`

            - `const AdvancedModeTransformConfigSegmentationConfigElementSegmentationConfigModeElement AdvancedModeTransformConfigSegmentationConfigElementSegmentationConfigMode = "element"`

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
  pipeline, err := client.Pipelines.DataSources.Sync(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.PipelineDataSourceSyncParams{
      PipelineID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", pipeline.ID)
}
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "embedding_config": {
    "component": {
      "class_name": "class_name",
      "embed_batch_size": 1,
      "model_name": "openai-text-embedding-3-small",
      "num_workers": 0
    },
    "type": "MANAGED_OPENAI_EMBEDDING"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "embedding_config_hash": "embedding_config_hash",
    "parsing_config_hash": "parsing_config_hash",
    "transform_config_hash": "transform_config_hash"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "data_sink": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "additional_kwargs": {
          "foo": "bar"
        },
        "api_base": "api_base",
        "api_key": "api_key",
        "api_version": "api_version",
        "azure_deployment": "azure_deployment",
        "azure_endpoint": "azure_endpoint",
        "class_name": "class_name",
        "default_headers": {
          "foo": "string"
        },
        "dimensions": 0,
        "embed_batch_size": 1,
        "max_retries": 0,
        "model_name": "model_name",
        "num_workers": 0,
        "reuse_client": true,
        "timeout": 0
      },
      "type": "AZURE_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "llama_parse_parameters": {
    "adaptive_long_table": true,
    "aggressive_table_extraction": true,
    "annotate_links": true,
    "auto_mode": true,
    "auto_mode_configuration_json": "auto_mode_configuration_json",
    "auto_mode_trigger_on_image_in_page": true,
    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
    "auto_mode_trigger_on_table_in_page": true,
    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
    "azure_openai_api_version": "azure_openai_api_version",
    "azure_openai_deployment_name": "azure_openai_deployment_name",
    "azure_openai_endpoint": "azure_openai_endpoint",
    "azure_openai_key": "azure_openai_key",
    "bbox_bottom": 0,
    "bbox_left": 0,
    "bbox_right": 0,
    "bbox_top": 0,
    "bounding_box": "bounding_box",
    "compact_markdown_table": true,
    "complemental_formatting_instruction": "complemental_formatting_instruction",
    "content_guideline_instruction": "content_guideline_instruction",
    "continuous_mode": true,
    "disable_image_extraction": true,
    "disable_ocr": true,
    "disable_reconstruction": true,
    "do_not_cache": true,
    "do_not_unroll_columns": true,
    "enable_cost_optimizer": true,
    "extract_charts": true,
    "extract_layout": true,
    "extract_printed_page_number": true,
    "fast_mode": true,
    "formatting_instruction": "formatting_instruction",
    "gpt4o_api_key": "gpt4o_api_key",
    "gpt4o_mode": true,
    "guess_xlsx_sheet_name": true,
    "hide_footers": true,
    "hide_headers": true,
    "high_res_ocr": true,
    "html_make_all_elements_visible": true,
    "html_remove_fixed_elements": true,
    "html_remove_navigation_elements": true,
    "http_proxy": "http_proxy",
    "ignore_document_elements_for_layout_detection": true,
    "images_to_save": [
      "screenshot"
    ],
    "inline_images_in_markdown": true,
    "input_s3_path": "input_s3_path",
    "input_s3_region": "input_s3_region",
    "input_url": "input_url",
    "internal_is_screenshot_job": true,
    "invalidate_cache": true,
    "is_formatting_instruction": true,
    "job_timeout_extra_time_per_page_in_seconds": 0,
    "job_timeout_in_seconds": 0,
    "keep_page_separator_when_merging_tables": true,
    "languages": [
      "af"
    ],
    "layout_aware": true,
    "line_level_bounding_box": true,
    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
    "max_pages": 0,
    "max_pages_enforced": 0,
    "merge_tables_across_pages_in_markdown": true,
    "model": "model",
    "outlined_table_extraction": true,
    "output_pdf_of_document": true,
    "output_s3_path_prefix": "output_s3_path_prefix",
    "output_s3_region": "output_s3_region",
    "output_tables_as_HTML": true,
    "page_error_tolerance": 0,
    "page_footer_prefix": "page_footer_prefix",
    "page_footer_suffix": "page_footer_suffix",
    "page_header_prefix": "page_header_prefix",
    "page_header_suffix": "page_header_suffix",
    "page_prefix": "page_prefix",
    "page_separator": "page_separator",
    "page_suffix": "page_suffix",
    "parse_mode": "parse_page_without_llm",
    "parsing_instruction": "parsing_instruction",
    "precise_bounding_box": true,
    "premium_mode": true,
    "presentation_out_of_bounds_content": true,
    "presentation_skip_embedded_data": true,
    "preserve_layout_alignment_across_pages": true,
    "preserve_very_small_text": true,
    "preset": "preset",
    "priority": "low",
    "project_id": "project_id",
    "remove_hidden_text": true,
    "replace_failed_page_mode": "raw_text",
    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
    "save_images": true,
    "skip_diagonal_text": true,
    "specialized_chart_parsing_agentic": true,
    "specialized_chart_parsing_efficient": true,
    "specialized_chart_parsing_plus": true,
    "specialized_image_parsing": true,
    "spreadsheet_extract_sub_tables": true,
    "spreadsheet_force_formula_computation": true,
    "spreadsheet_include_hidden_sheets": true,
    "strict_mode_buggy_font": true,
    "strict_mode_image_extraction": true,
    "strict_mode_image_ocr": true,
    "strict_mode_reconstruction": true,
    "structured_output": true,
    "structured_output_json_schema": "structured_output_json_schema",
    "structured_output_json_schema_name": "structured_output_json_schema_name",
    "system_prompt": "system_prompt",
    "system_prompt_append": "system_prompt_append",
    "take_screenshot": true,
    "target_pages": "target_pages",
    "tier": "tier",
    "use_vendor_multimodal_model": true,
    "user_prompt": "user_prompt",
    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
    "version": "version",
    "webhook_configurations": [
      {
        "webhook_events": [
          "parse.success",
          "parse.error"
        ],
        "webhook_headers": {
          "Authorization": "Bearer sk-..."
        },
        "webhook_output_format": "json",
        "webhook_url": "https://example.com/webhooks/llamacloud"
      }
    ],
    "webhook_url": "webhook_url"
  },
  "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "metadata_config": {
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ]
  },
  "pipeline_type": "PLAYGROUND",
  "preset_retrieval_parameters": {
    "alpha": 0,
    "class_name": "class_name",
    "dense_similarity_cutoff": 0,
    "dense_similarity_top_k": 1,
    "enable_reranking": true,
    "files_top_k": 1,
    "rerank_top_n": 1,
    "retrieval_mode": "chunks",
    "retrieve_image_nodes": true,
    "retrieve_page_figure_nodes": true,
    "retrieve_page_screenshot_nodes": true,
    "search_filters": {
      "filters": [
        {
          "key": "key",
          "value": 0,
          "operator": "=="
        }
      ],
      "condition": "and"
    },
    "search_filters_inference_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "sparse_similarity_top_k": 1
  },
  "sparse_model_config": {
    "class_name": "class_name",
    "model_type": "splade"
  },
  "status": "CREATED",
  "transform_config": {
    "chunk_overlap": 0,
    "chunk_size": 1,
    "mode": "auto"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Domain Types

### Pipeline Data Source

- `type PipelineDataSource struct{…}`

  Schema for a data source in a pipeline.

  - `ID string`

    Unique identifier

  - `Component PipelineDataSourceComponentUnion`

    Component that implements the data source

    - `type PipelineDataSourceComponentMap map[string, any]`

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

  - `DataSourceID string`

    The ID of the data source.

  - `LastSyncedAt Time`

    The last time the data source was automatically synced.

  - `Name string`

    The name of the data source.

  - `PipelineID string`

    The ID of the pipeline.

  - `ProjectID string`

  - `SourceType PipelineDataSourceSourceType`

    - `const PipelineDataSourceSourceTypeS3 PipelineDataSourceSourceType = "S3"`

    - `const PipelineDataSourceSourceTypeAzureStorageBlob PipelineDataSourceSourceType = "AZURE_STORAGE_BLOB"`

    - `const PipelineDataSourceSourceTypeGoogleDrive PipelineDataSourceSourceType = "GOOGLE_DRIVE"`

    - `const PipelineDataSourceSourceTypeMicrosoftOnedrive PipelineDataSourceSourceType = "MICROSOFT_ONEDRIVE"`

    - `const PipelineDataSourceSourceTypeMicrosoftSharepoint PipelineDataSourceSourceType = "MICROSOFT_SHAREPOINT"`

    - `const PipelineDataSourceSourceTypeSlack PipelineDataSourceSourceType = "SLACK"`

    - `const PipelineDataSourceSourceTypeNotionPage PipelineDataSourceSourceType = "NOTION_PAGE"`

    - `const PipelineDataSourceSourceTypeConfluence PipelineDataSourceSourceType = "CONFLUENCE"`

    - `const PipelineDataSourceSourceTypeJira PipelineDataSourceSourceType = "JIRA"`

    - `const PipelineDataSourceSourceTypeJiraV2 PipelineDataSourceSourceType = "JIRA_V2"`

    - `const PipelineDataSourceSourceTypeBox PipelineDataSourceSourceType = "BOX"`

  - `CreatedAt Time`

    Creation datetime

  - `CustomMetadata map[string, PipelineDataSourceCustomMetadataUnion]`

    Custom metadata that will be present on all data loaded from the data source

    - `type PipelineDataSourceCustomMetadataMap map[string, any]`

    - `type PipelineDataSourceCustomMetadataArray []any`

    - `string`

    - `float64`

    - `bool`

  - `Status PipelineDataSourceStatus`

    The status of the data source in the pipeline.

    - `const PipelineDataSourceStatusNotStarted PipelineDataSourceStatus = "NOT_STARTED"`

    - `const PipelineDataSourceStatusInProgress PipelineDataSourceStatus = "IN_PROGRESS"`

    - `const PipelineDataSourceStatusSuccess PipelineDataSourceStatus = "SUCCESS"`

    - `const PipelineDataSourceStatusError PipelineDataSourceStatus = "ERROR"`

    - `const PipelineDataSourceStatusCancelled PipelineDataSourceStatus = "CANCELLED"`

  - `StatusUpdatedAt Time`

    The last time the status was updated.

  - `SyncInterval float64`

    The interval at which the data source should be synced.

  - `SyncScheduleSetBy string`

    The id of the user who set the sync schedule.

  - `UpdatedAt Time`

    Update datetime

  - `VersionMetadata DataSourceReaderVersionMetadata`

    Version metadata for the data source

    - `ReaderVersion DataSourceReaderVersionMetadataReaderVersion`

      The version of the reader to use for this data source.

      - `const DataSourceReaderVersionMetadataReaderVersion1_0 DataSourceReaderVersionMetadataReaderVersion = "1.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_0 DataSourceReaderVersionMetadataReaderVersion = "2.0"`

      - `const DataSourceReaderVersionMetadataReaderVersion2_1 DataSourceReaderVersionMetadataReaderVersion = "2.1"`
