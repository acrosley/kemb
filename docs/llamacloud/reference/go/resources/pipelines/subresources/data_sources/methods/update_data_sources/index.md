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
