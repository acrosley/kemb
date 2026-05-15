# Data Sources

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

## Add Data Sources To Pipeline

`pipelines.data_sources.update_data_sources(strpipeline_id, DataSourceUpdateDataSourcesParams**kwargs)  -> DataSourceUpdateDataSourcesResponse`

**put** `/api/v1/pipelines/{pipeline_id}/data-sources`

Add data sources to a pipeline.

### Parameters

- `pipeline_id: str`

- `body: Iterable[Body]`

  - `data_source_id: str`

    The ID of the data source.

  - `sync_interval: Optional[float]`

    The interval at which the data source should be synced. Valid values are: 21600, 43200, 86400

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
pipeline_data_sources = client.pipelines.data_sources.update_data_sources(
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    body=[{
        "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
    }],
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

## Update Pipeline Data Source

`pipelines.data_sources.update(strdata_source_id, DataSourceUpdateParams**kwargs)  -> PipelineDataSource`

**put** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}`

Update the configuration of a data source in a pipeline.

### Parameters

- `pipeline_id: str`

- `data_source_id: str`

- `sync_interval: Optional[float]`

  The interval at which the data source should be synced.

### Returns

- `class PipelineDataSource: …`

  Schema for a data source in a pipeline.

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
pipeline_data_source = client.pipelines.data_sources.update(
    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(pipeline_data_source.id)
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

`pipelines.data_sources.get_status(strdata_source_id, DataSourceGetStatusParams**kwargs)  -> ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status`

Get the status of a data source for a pipeline.

### Parameters

- `pipeline_id: str`

- `data_source_id: str`

### Returns

- `class ManagedIngestionStatusResponse: …`

  - `status: Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", 3 more]`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date: Optional[datetime]`

    Date of the deployment.

  - `effective_at: Optional[datetime]`

    When the status is effective

  - `error: Optional[List[Error]]`

    List of errors that occurred during ingestion.

    - `job_id: str`

      ID of the job that failed.

    - `message: str`

      List of errors that occurred during ingestion.

    - `step: Literal["MANAGED_INGESTION", "DATA_SOURCE", "FILE_UPDATER", 4 more]`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id: Optional[str]`

    ID of the latest job.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
managed_ingestion_status_response = client.pipelines.data_sources.get_status(
    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(managed_ingestion_status_response.job_id)
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

`pipelines.data_sources.sync(strdata_source_id, DataSourceSyncParams**kwargs)  -> Pipeline`

**post** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/sync`

Run ingestion for the pipeline data source by incrementally updating the data-sink with upstream changes from data-source.

### Parameters

- `pipeline_id: str`

- `data_source_id: str`

- `pipeline_file_ids: Optional[SequenceNotStr[str]]`

### Returns

- `class Pipeline: …`

  Schema for a pipeline.

  - `id: str`

    Unique identifier

  - `embedding_config: EmbeddingConfig`

    - `class EmbeddingConfigManagedOpenAIEmbeddingConfig: …`

      - `component: Optional[EmbeddingConfigManagedOpenAIEmbeddingConfigComponent]`

        Configuration for the Managed OpenAI embedding model.

        - `class_name: Optional[str]`

        - `embed_batch_size: Optional[int]`

          The batch size for embedding calls.

        - `model_name: Optional[Literal["openai-text-embedding-3-small"]]`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers: Optional[int]`

          The number of workers to use for async embedding calls.

      - `type: Optional[Literal["MANAGED_OPENAI_EMBEDDING"]]`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `class AzureOpenAIEmbeddingConfig: …`

      - `component: Optional[AzureOpenAIEmbedding]`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs: Optional[Dict[str, object]]`

          Additional kwargs for the OpenAI API.

        - `api_base: Optional[str]`

          The base URL for Azure deployment.

        - `api_key: Optional[str]`

          The OpenAI API key.

        - `api_version: Optional[str]`

          The version for Azure OpenAI API.

        - `azure_deployment: Optional[str]`

          The Azure deployment to use.

        - `azure_endpoint: Optional[str]`

          The Azure endpoint to use.

        - `class_name: Optional[str]`

        - `default_headers: Optional[Dict[str, str]]`

          The default headers for API requests.

        - `dimensions: Optional[int]`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size: Optional[int]`

          The batch size for embedding calls.

        - `max_retries: Optional[int]`

          Maximum number of retries.

        - `model_name: Optional[str]`

          The name of the OpenAI embedding model.

        - `num_workers: Optional[int]`

          The number of workers to use for async embedding calls.

        - `reuse_client: Optional[bool]`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout: Optional[float]`

          Timeout for each request.

      - `type: Optional[Literal["AZURE_EMBEDDING"]]`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `class CohereEmbeddingConfig: …`

      - `component: Optional[CohereEmbedding]`

        Configuration for the Cohere embedding model.

        - `api_key: Optional[str]`

          The Cohere API key.

        - `class_name: Optional[str]`

        - `embed_batch_size: Optional[int]`

          The batch size for embedding calls.

        - `embedding_type: Optional[str]`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type: Optional[str]`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name: Optional[str]`

          The modelId of the Cohere model to use.

        - `num_workers: Optional[int]`

          The number of workers to use for async embedding calls.

        - `truncate: Optional[str]`

          Truncation type - START/ END/ NONE

      - `type: Optional[Literal["COHERE_EMBEDDING"]]`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `class GeminiEmbeddingConfig: …`

      - `component: Optional[GeminiEmbedding]`

        Configuration for the Gemini embedding model.

        - `api_base: Optional[str]`

          API base to access the model. Defaults to None.

        - `api_key: Optional[str]`

          API key to access the model. Defaults to None.

        - `class_name: Optional[str]`

        - `embed_batch_size: Optional[int]`

          The batch size for embedding calls.

        - `model_name: Optional[str]`

          The modelId of the Gemini model to use.

        - `num_workers: Optional[int]`

          The number of workers to use for async embedding calls.

        - `output_dimensionality: Optional[int]`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type: Optional[str]`

          The task for embedding model.

        - `title: Optional[str]`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport: Optional[str]`

          Transport to access the model. Defaults to None.

      - `type: Optional[Literal["GEMINI_EMBEDDING"]]`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `class HuggingFaceInferenceAPIEmbeddingConfig: …`

      - `component: Optional[HuggingFaceInferenceAPIEmbedding]`

        Configuration for the HuggingFace Inference API embedding model.

        - `token: Optional[Union[str, bool, null]]`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `str`

          - `bool`

        - `class_name: Optional[str]`

        - `cookies: Optional[Dict[str, str]]`

          Additional cookies to send to the server.

        - `embed_batch_size: Optional[int]`

          The batch size for embedding calls.

        - `headers: Optional[Dict[str, str]]`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name: Optional[str]`

          Hugging Face model name. If None, the task will be used.

        - `num_workers: Optional[int]`

          The number of workers to use for async embedding calls.

        - `pooling: Optional[Literal["cls", "mean", "last"]]`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction: Optional[str]`

          Instruction to prepend during query embedding.

        - `task: Optional[str]`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction: Optional[str]`

          Instruction to prepend during text embedding.

        - `timeout: Optional[float]`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type: Optional[Literal["HUGGINGFACE_API_EMBEDDING"]]`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `class OpenAIEmbeddingConfig: …`

      - `component: Optional[OpenAIEmbedding]`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs: Optional[Dict[str, object]]`

          Additional kwargs for the OpenAI API.

        - `api_base: Optional[str]`

          The base URL for OpenAI API.

        - `api_key: Optional[str]`

          The OpenAI API key.

        - `api_version: Optional[str]`

          The version for OpenAI API.

        - `class_name: Optional[str]`

        - `default_headers: Optional[Dict[str, str]]`

          The default headers for API requests.

        - `dimensions: Optional[int]`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size: Optional[int]`

          The batch size for embedding calls.

        - `max_retries: Optional[int]`

          Maximum number of retries.

        - `model_name: Optional[str]`

          The name of the OpenAI embedding model.

        - `num_workers: Optional[int]`

          The number of workers to use for async embedding calls.

        - `reuse_client: Optional[bool]`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout: Optional[float]`

          Timeout for each request.

      - `type: Optional[Literal["OPENAI_EMBEDDING"]]`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `class VertexAIEmbeddingConfig: …`

      - `component: Optional[VertexTextEmbedding]`

        Configuration for the VertexAI embedding model.

        - `client_email: Optional[str]`

          The client email for the VertexAI credentials.

        - `location: str`

          The default location to use when making API calls.

        - `private_key: Optional[str]`

          The private key for the VertexAI credentials.

        - `private_key_id: Optional[str]`

          The private key ID for the VertexAI credentials.

        - `project: str`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: Optional[str]`

          The token URI for the VertexAI credentials.

        - `additional_kwargs: Optional[Dict[str, object]]`

          Additional kwargs for the Vertex.

        - `class_name: Optional[str]`

        - `embed_batch_size: Optional[int]`

          The batch size for embedding calls.

        - `embed_mode: Optional[Literal["default", "classification", "clustering", 2 more]]`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name: Optional[str]`

          The modelId of the VertexAI model to use.

        - `num_workers: Optional[int]`

          The number of workers to use for async embedding calls.

      - `type: Optional[Literal["VERTEXAI_EMBEDDING"]]`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `class BedrockEmbeddingConfig: …`

      - `component: Optional[BedrockEmbedding]`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs: Optional[Dict[str, object]]`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id: Optional[str]`

          AWS Access Key ID to use

        - `aws_secret_access_key: Optional[str]`

          AWS Secret Access Key to use

        - `aws_session_token: Optional[str]`

          AWS Session Token to use

        - `class_name: Optional[str]`

        - `embed_batch_size: Optional[int]`

          The batch size for embedding calls.

        - `max_retries: Optional[int]`

          The maximum number of API retries.

        - `model_name: Optional[str]`

          The modelId of the Bedrock model to use.

        - `num_workers: Optional[int]`

          The number of workers to use for async embedding calls.

        - `profile_name: Optional[str]`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name: Optional[str]`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout: Optional[float]`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type: Optional[Literal["BEDROCK_EMBEDDING"]]`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: str`

  - `project_id: str`

  - `config_hash: Optional[ConfigHash]`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash: Optional[str]`

      Hash of the embedding config.

    - `parsing_config_hash: Optional[str]`

      Hash of the llama parse parameters.

    - `transform_config_hash: Optional[str]`

      Hash of the transform config.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `data_sink: Optional[DataSink]`

    Schema for a data sink.

    - `id: str`

      Unique identifier

    - `component: Component`

      Component that implements the data sink

      - `Dict[str, object]`

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

      - `class CloudMilvusVectorStore: …`

        Cloud Milvus Vector Store.

        - `uri: str`

        - `token: Optional[str]`

        - `class_name: Optional[str]`

        - `collection_name: Optional[str]`

        - `embedding_dimension: Optional[int]`

        - `supports_nested_metadata_filters: Optional[bool]`

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

    - `name: str`

      The name of the data sink.

    - `project_id: str`

    - `sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", 4 more]`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at: Optional[datetime]`

      Creation datetime

    - `updated_at: Optional[datetime]`

      Update datetime

  - `embedding_model_config: Optional[EmbeddingModelConfig]`

    Schema for an embedding model config.

    - `id: str`

      Unique identifier

    - `embedding_config: EmbeddingModelConfigEmbeddingConfig`

      The embedding configuration for the embedding model config.

      - `class AzureOpenAIEmbeddingConfig: …`

      - `class CohereEmbeddingConfig: …`

      - `class GeminiEmbeddingConfig: …`

      - `class HuggingFaceInferenceAPIEmbeddingConfig: …`

      - `class OpenAIEmbeddingConfig: …`

      - `class VertexAIEmbeddingConfig: …`

      - `class BedrockEmbeddingConfig: …`

    - `name: str`

      The name of the embedding model config.

    - `project_id: str`

    - `created_at: Optional[datetime]`

      Creation datetime

    - `updated_at: Optional[datetime]`

      Update datetime

  - `embedding_model_config_id: Optional[str]`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters: Optional[LlamaParseParameters]`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table: Optional[bool]`

    - `aggressive_table_extraction: Optional[bool]`

    - `annotate_links: Optional[bool]`

    - `auto_mode: Optional[bool]`

    - `auto_mode_configuration_json: Optional[str]`

    - `auto_mode_trigger_on_image_in_page: Optional[bool]`

    - `auto_mode_trigger_on_regexp_in_page: Optional[str]`

    - `auto_mode_trigger_on_table_in_page: Optional[bool]`

    - `auto_mode_trigger_on_text_in_page: Optional[str]`

    - `azure_openai_api_version: Optional[str]`

    - `azure_openai_deployment_name: Optional[str]`

    - `azure_openai_endpoint: Optional[str]`

    - `azure_openai_key: Optional[str]`

    - `bbox_bottom: Optional[float]`

    - `bbox_left: Optional[float]`

    - `bbox_right: Optional[float]`

    - `bbox_top: Optional[float]`

    - `bounding_box: Optional[str]`

    - `compact_markdown_table: Optional[bool]`

    - `complemental_formatting_instruction: Optional[str]`

    - `content_guideline_instruction: Optional[str]`

    - `continuous_mode: Optional[bool]`

    - `disable_image_extraction: Optional[bool]`

    - `disable_ocr: Optional[bool]`

    - `disable_reconstruction: Optional[bool]`

    - `do_not_cache: Optional[bool]`

    - `do_not_unroll_columns: Optional[bool]`

    - `enable_cost_optimizer: Optional[bool]`

    - `extract_charts: Optional[bool]`

    - `extract_layout: Optional[bool]`

    - `extract_printed_page_number: Optional[bool]`

    - `fast_mode: Optional[bool]`

    - `formatting_instruction: Optional[str]`

    - `gpt4o_api_key: Optional[str]`

    - `gpt4o_mode: Optional[bool]`

    - `guess_xlsx_sheet_name: Optional[bool]`

    - `hide_footers: Optional[bool]`

    - `hide_headers: Optional[bool]`

    - `high_res_ocr: Optional[bool]`

    - `html_make_all_elements_visible: Optional[bool]`

    - `html_remove_fixed_elements: Optional[bool]`

    - `html_remove_navigation_elements: Optional[bool]`

    - `http_proxy: Optional[str]`

    - `ignore_document_elements_for_layout_detection: Optional[bool]`

    - `images_to_save: Optional[List[Literal["screenshot", "embedded", "layout"]]]`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown: Optional[bool]`

    - `input_s3_path: Optional[str]`

    - `input_s3_region: Optional[str]`

    - `input_url: Optional[str]`

    - `internal_is_screenshot_job: Optional[bool]`

    - `invalidate_cache: Optional[bool]`

    - `is_formatting_instruction: Optional[bool]`

    - `job_timeout_extra_time_per_page_in_seconds: Optional[float]`

    - `job_timeout_in_seconds: Optional[float]`

    - `keep_page_separator_when_merging_tables: Optional[bool]`

    - `languages: Optional[List[ParsingLanguages]]`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware: Optional[bool]`

    - `line_level_bounding_box: Optional[bool]`

    - `markdown_table_multiline_header_separator: Optional[str]`

    - `max_pages: Optional[int]`

    - `max_pages_enforced: Optional[int]`

    - `merge_tables_across_pages_in_markdown: Optional[bool]`

    - `model: Optional[str]`

    - `outlined_table_extraction: Optional[bool]`

    - `output_pdf_of_document: Optional[bool]`

    - `output_s3_path_prefix: Optional[str]`

    - `output_s3_region: Optional[str]`

    - `output_tables_as_html: Optional[bool]`

    - `page_error_tolerance: Optional[float]`

    - `page_footer_prefix: Optional[str]`

    - `page_footer_suffix: Optional[str]`

    - `page_header_prefix: Optional[str]`

    - `page_header_suffix: Optional[str]`

    - `page_prefix: Optional[str]`

    - `page_separator: Optional[str]`

    - `page_suffix: Optional[str]`

    - `parse_mode: Optional[ParsingMode]`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction: Optional[str]`

    - `precise_bounding_box: Optional[bool]`

    - `premium_mode: Optional[bool]`

    - `presentation_out_of_bounds_content: Optional[bool]`

    - `presentation_skip_embedded_data: Optional[bool]`

    - `preserve_layout_alignment_across_pages: Optional[bool]`

    - `preserve_very_small_text: Optional[bool]`

    - `preset: Optional[str]`

    - `priority: Optional[Literal["low", "medium", "high", "critical"]]`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id: Optional[str]`

    - `remove_hidden_text: Optional[bool]`

    - `replace_failed_page_mode: Optional[FailPageMode]`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix: Optional[str]`

    - `replace_failed_page_with_error_message_suffix: Optional[str]`

    - `save_images: Optional[bool]`

    - `skip_diagonal_text: Optional[bool]`

    - `specialized_chart_parsing_agentic: Optional[bool]`

    - `specialized_chart_parsing_efficient: Optional[bool]`

    - `specialized_chart_parsing_plus: Optional[bool]`

    - `specialized_image_parsing: Optional[bool]`

    - `spreadsheet_extract_sub_tables: Optional[bool]`

    - `spreadsheet_force_formula_computation: Optional[bool]`

    - `spreadsheet_include_hidden_sheets: Optional[bool]`

    - `strict_mode_buggy_font: Optional[bool]`

    - `strict_mode_image_extraction: Optional[bool]`

    - `strict_mode_image_ocr: Optional[bool]`

    - `strict_mode_reconstruction: Optional[bool]`

    - `structured_output: Optional[bool]`

    - `structured_output_json_schema: Optional[str]`

    - `structured_output_json_schema_name: Optional[str]`

    - `system_prompt: Optional[str]`

    - `system_prompt_append: Optional[str]`

    - `take_screenshot: Optional[bool]`

    - `target_pages: Optional[str]`

    - `tier: Optional[str]`

    - `use_vendor_multimodal_model: Optional[bool]`

    - `user_prompt: Optional[str]`

    - `vendor_multimodal_api_key: Optional[str]`

    - `vendor_multimodal_model_name: Optional[str]`

    - `version: Optional[str]`

    - `webhook_configurations: Optional[List[WebhookConfiguration]]`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events: Optional[List[Literal["extract.pending", "extract.success", "extract.error", 14 more]]]`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers: Optional[Dict[str, str]]`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format: Optional[str]`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url: Optional[str]`

        URL to receive webhook POST notifications

    - `webhook_url: Optional[str]`

  - `managed_pipeline_id: Optional[str]`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config: Optional[PipelineMetadataConfig]`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys: Optional[List[str]]`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys: Optional[List[str]]`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type: Optional[PipelineType]`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters: Optional[PresetRetrievalParams]`

    Preset retrieval parameters for the pipeline.

    - `alpha: Optional[float]`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name: Optional[str]`

    - `dense_similarity_cutoff: Optional[float]`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k: Optional[int]`

      Number of nodes for dense retrieval.

    - `enable_reranking: Optional[bool]`

      Enable reranking for retrieval

    - `files_top_k: Optional[int]`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n: Optional[int]`

      Number of reranked nodes for returning.

    - `retrieval_mode: Optional[RetrievalMode]`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes: Optional[bool]`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes: Optional[bool]`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes: Optional[bool]`

      Whether to retrieve page screenshot nodes.

    - `search_filters: Optional[MetadataFilters]`

      Metadata filters for vector stores.

      - `filters: List[Filter]`

        - `class FilterMetadataFilter: …`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: str`

          - `value: Union[float, str, List[str], 3 more]`

            - `float`

            - `str`

            - `List[str]`

            - `List[float]`

            - `List[int]`

          - `operator: Optional[Literal["==", ">", "<", 11 more]]`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `class MetadataFilters: …`

          Metadata filters for vector stores.

      - `condition: Optional[Literal["and", "or", "not"]]`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `sparse_similarity_top_k: Optional[int]`

      Number of nodes for sparse retrieval.

  - `sparse_model_config: Optional[SparseModelConfig]`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name: Optional[str]`

    - `model_type: Optional[Literal["splade", "bm25", "auto"]]`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status: Optional[Literal["CREATED", "DELETING"]]`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config: Optional[TransformConfig]`

    Configuration for the transformation.

    - `class AutoTransformConfig: …`

      - `chunk_overlap: Optional[int]`

        Chunk overlap for the transformation.

      - `chunk_size: Optional[int]`

        Chunk size for the transformation.

      - `mode: Optional[Literal["auto"]]`

        - `"auto"`

    - `class AdvancedModeTransformConfig: …`

      - `chunking_config: Optional[ChunkingConfig]`

        Configuration for the chunking.

        - `class ChunkingConfigNoneChunkingConfig: …`

          - `mode: Optional[Literal["none"]]`

            - `"none"`

        - `class ChunkingConfigCharacterChunkingConfig: …`

          - `chunk_overlap: Optional[int]`

          - `chunk_size: Optional[int]`

          - `mode: Optional[Literal["character"]]`

            - `"character"`

        - `class ChunkingConfigTokenChunkingConfig: …`

          - `chunk_overlap: Optional[int]`

          - `chunk_size: Optional[int]`

          - `mode: Optional[Literal["token"]]`

            - `"token"`

          - `separator: Optional[str]`

        - `class ChunkingConfigSentenceChunkingConfig: …`

          - `chunk_overlap: Optional[int]`

          - `chunk_size: Optional[int]`

          - `mode: Optional[Literal["sentence"]]`

            - `"sentence"`

          - `paragraph_separator: Optional[str]`

          - `separator: Optional[str]`

        - `class ChunkingConfigSemanticChunkingConfig: …`

          - `breakpoint_percentile_threshold: Optional[int]`

          - `buffer_size: Optional[int]`

          - `mode: Optional[Literal["semantic"]]`

            - `"semantic"`

      - `mode: Optional[Literal["advanced"]]`

        - `"advanced"`

      - `segmentation_config: Optional[SegmentationConfig]`

        Configuration for the segmentation.

        - `class SegmentationConfigNoneSegmentationConfig: …`

          - `mode: Optional[Literal["none"]]`

            - `"none"`

        - `class SegmentationConfigPageSegmentationConfig: …`

          - `mode: Optional[Literal["page"]]`

            - `"page"`

          - `page_separator: Optional[str]`

        - `class SegmentationConfigElementSegmentationConfig: …`

          - `mode: Optional[Literal["element"]]`

            - `"element"`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
pipeline = client.pipelines.data_sources.sync(
    data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(pipeline.id)
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

- `class PipelineDataSource: …`

  Schema for a data source in a pipeline.

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

### Data Source Get Data Sources Response

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

### Data Source Update Data Sources Response

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
