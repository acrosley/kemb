## List Pipeline Data Sources

`pipelines.data_sources.get_data_sources(strpipeline_id)  -> DataSourceGetDataSourcesResponse`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources`

Get data sources for a pipeline.

### Parameters

- `pipeline_id: str`

### Returns

- `List[PipelineDataSource]`

  - `id: str`

    Unique identifier

  - `component: Component`

    Component that implements the data source

    - `Dict[str, object]`

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

    - `class CloudGoogleDriveDataSource: …`

      - `folder_id: str`

        The ID of the Google Drive folder to read from.

      - `class_name: Optional[str]`

      - `service_account_key: Optional[Dict[str, str]]`

        A dictionary containing secret values

      - `supports_access_control: Optional[bool]`

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

    - `class CloudNotionPageDataSource: …`

      - `integration_token: str`

        The integration token to use for authentication.

      - `class_name: Optional[str]`

      - `database_ids: Optional[str]`

        The Notion Database Id to read content from.

      - `page_ids: Optional[str]`

        The Page ID's of the Notion to read from.

      - `supports_access_control: Optional[bool]`

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

  - `data_source_id: str`

    The ID of the data source.

  - `last_synced_at: datetime`

    The last time the data source was automatically synced.

  - `name: str`

    The name of the data source.

  - `pipeline_id: str`

    The ID of the pipeline.

  - `project_id: str`

  - `source_type: Literal["S3", "AZURE_STORAGE_BLOB", "GOOGLE_DRIVE", 8 more]`

    - `"S3"`

    - `"AZURE_STORAGE_BLOB"`

    - `"GOOGLE_DRIVE"`

    - `"MICROSOFT_ONEDRIVE"`

    - `"MICROSOFT_SHAREPOINT"`

    - `"SLACK"`

    - `"NOTION_PAGE"`

    - `"CONFLUENCE"`

    - `"JIRA"`

    - `"JIRA_V2"`

    - `"BOX"`

  - `created_at: Optional[datetime]`

    Creation datetime

  - `custom_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

    Custom metadata that will be present on all data loaded from the data source

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

  - `status: Optional[Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", 2 more]]`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: Optional[datetime]`

    The last time the status was updated.

  - `sync_interval: Optional[float]`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by: Optional[str]`

    The id of the user who set the sync schedule.

  - `updated_at: Optional[datetime]`

    Update datetime

  - `version_metadata: Optional[DataSourceReaderVersionMetadata]`

    Version metadata for the data source

    - `reader_version: Optional[Literal["1.0", "2.0", "2.1"]]`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
pipeline_data_sources = client.pipelines.data_sources.get_data_sources(
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(pipeline_data_sources)
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
