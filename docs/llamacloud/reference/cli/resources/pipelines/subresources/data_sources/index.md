# Data Sources

## List Pipeline Data Sources

`$ llamacloud-prod pipelines:data-sources get-data-sources`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources`

Get data sources for a pipeline.

### Parameters

- `--pipeline-id: string`

### Returns

- `Response List Pipeline Data Sources Api V1 Pipelines  Pipeline Id  Data Sources Get: array of PipelineDataSource`

  - `id: string`

    Unique identifier

  - `component: map[unknown] or CloudS3DataSource or CloudAzStorageBlobDataSource or 9 more`

    Component that implements the data source

    - `union_member_0: map[unknown]`

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

    - `cloud_google_drive_data_source: object { folder_id, class_name, service_account_key, supports_access_control }`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name: optional string`

      - `service_account_key: optional map[string]`

        A dictionary containing secret values

      - `supports_access_control: optional boolean`

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

    - `cloud_notion_page_data_source: object { integration_token, class_name, database_ids, 2 more }`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name: optional string`

      - `database_ids: optional string`

        The Notion Database Id to read content from.

      - `page_ids: optional string`

        The Page ID's of the Notion to read from.

      - `supports_access_control: optional boolean`

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

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" or "AZURE_STORAGE_BLOB" or "GOOGLE_DRIVE" or 8 more`

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

  - `created_at: optional string`

    Creation datetime

  - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Custom metadata that will be present on all data loaded from the data source

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `status: optional "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: optional string`

    The last time the status was updated.

  - `sync_interval: optional number`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by: optional string`

    The id of the user who set the sync schedule.

  - `updated_at: optional string`

    Update datetime

  - `version_metadata: optional object { reader_version }`

    Version metadata for the data source

    - `reader_version: optional "1.0" or "2.0" or "2.1"`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Example

```cli
llamacloud-prod pipelines:data-sources get-data-sources \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

`$ llamacloud-prod pipelines:data-sources update-data-sources`

**put** `/api/v1/pipelines/{pipeline_id}/data-sources`

Add data sources to a pipeline.

### Parameters

- `--pipeline-id: string`

- `--body: array of object { data_source_id, sync_interval }`

### Returns

- `Response Add Data Sources To Pipeline Api V1 Pipelines  Pipeline Id  Data Sources Put: array of PipelineDataSource`

  - `id: string`

    Unique identifier

  - `component: map[unknown] or CloudS3DataSource or CloudAzStorageBlobDataSource or 9 more`

    Component that implements the data source

    - `union_member_0: map[unknown]`

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

    - `cloud_google_drive_data_source: object { folder_id, class_name, service_account_key, supports_access_control }`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name: optional string`

      - `service_account_key: optional map[string]`

        A dictionary containing secret values

      - `supports_access_control: optional boolean`

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

    - `cloud_notion_page_data_source: object { integration_token, class_name, database_ids, 2 more }`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name: optional string`

      - `database_ids: optional string`

        The Notion Database Id to read content from.

      - `page_ids: optional string`

        The Page ID's of the Notion to read from.

      - `supports_access_control: optional boolean`

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

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" or "AZURE_STORAGE_BLOB" or "GOOGLE_DRIVE" or 8 more`

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

  - `created_at: optional string`

    Creation datetime

  - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Custom metadata that will be present on all data loaded from the data source

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `status: optional "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: optional string`

    The last time the status was updated.

  - `sync_interval: optional number`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by: optional string`

    The id of the user who set the sync schedule.

  - `updated_at: optional string`

    Update datetime

  - `version_metadata: optional object { reader_version }`

    Version metadata for the data source

    - `reader_version: optional "1.0" or "2.0" or "2.1"`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Example

```cli
llamacloud-prod pipelines:data-sources update-data-sources \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --body '{data_source_id: 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e}'
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

`$ llamacloud-prod pipelines:data-sources update`

**put** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}`

Update the configuration of a data source in a pipeline.

### Parameters

- `--pipeline-id: string`

  Path param

- `--data-source-id: string`

  Path param

- `--sync-interval: optional number`

  Body param: The interval at which the data source should be synced.

### Returns

- `pipeline_data_source: object { id, component, data_source_id, 13 more }`

  Schema for a data source in a pipeline.

  - `id: string`

    Unique identifier

  - `component: map[unknown] or CloudS3DataSource or CloudAzStorageBlobDataSource or 9 more`

    Component that implements the data source

    - `union_member_0: map[unknown]`

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

    - `cloud_google_drive_data_source: object { folder_id, class_name, service_account_key, supports_access_control }`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name: optional string`

      - `service_account_key: optional map[string]`

        A dictionary containing secret values

      - `supports_access_control: optional boolean`

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

    - `cloud_notion_page_data_source: object { integration_token, class_name, database_ids, 2 more }`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name: optional string`

      - `database_ids: optional string`

        The Notion Database Id to read content from.

      - `page_ids: optional string`

        The Page ID's of the Notion to read from.

      - `supports_access_control: optional boolean`

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

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" or "AZURE_STORAGE_BLOB" or "GOOGLE_DRIVE" or 8 more`

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

  - `created_at: optional string`

    Creation datetime

  - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Custom metadata that will be present on all data loaded from the data source

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `status: optional "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: optional string`

    The last time the status was updated.

  - `sync_interval: optional number`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by: optional string`

    The id of the user who set the sync schedule.

  - `updated_at: optional string`

    Update datetime

  - `version_metadata: optional object { reader_version }`

    Version metadata for the data source

    - `reader_version: optional "1.0" or "2.0" or "2.1"`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Example

```cli
llamacloud-prod pipelines:data-sources update \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --data-source-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

`$ llamacloud-prod pipelines:data-sources get-status`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status`

Get the status of a data source for a pipeline.

### Parameters

- `--pipeline-id: string`

- `--data-source-id: string`

### Returns

- `managed_ingestion_status_response: object { status, deployment_date, effective_at, 2 more }`

  - `status: "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date: optional string`

    Date of the deployment.

  - `effective_at: optional string`

    When the status is effective

  - `error: optional array of object { job_id, message, step }`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" or "DATA_SOURCE" or "FILE_UPDATER" or 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id: optional string`

    ID of the latest job.

### Example

```cli
llamacloud-prod pipelines:data-sources get-status \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --data-source-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

`$ llamacloud-prod pipelines:data-sources sync`

**post** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/sync`

Run ingestion for the pipeline data source by incrementally updating the data-sink with upstream changes from data-source.

### Parameters

- `--pipeline-id: string`

  Path param

- `--data-source-id: string`

  Path param

- `--pipeline-file-id: optional array of string`

  Body param

### Returns

- `pipeline: object { id, embedding_config, name, 15 more }`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: object { component, type }  or AzureOpenAIEmbeddingConfig or CohereEmbeddingConfig or 5 more`

    - `MANAGED_OPENAI_EMBEDDING: object { component, type }`

      - `component: optional object { class_name, embed_batch_size, model_name, num_workers }`

        Configuration for the Managed OpenAI embedding model.

        - `class_name: optional string`

        - `embed_batch_size: optional number`

          The batch size for embedding calls.

        - `model_name: optional "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers: optional number`

          The number of workers to use for async embedding calls.

      - `type: optional "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `azure_openai_embedding_config: object { component, type }`

      - `component: optional object { additional_kwargs, api_base, api_key, 12 more }`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs: optional map[unknown]`

          Additional kwargs for the OpenAI API.

        - `api_base: optional string`

          The base URL for Azure deployment.

        - `api_key: optional string`

          The OpenAI API key.

        - `api_version: optional string`

          The version for Azure OpenAI API.

        - `azure_deployment: optional string`

          The Azure deployment to use.

        - `azure_endpoint: optional string`

          The Azure endpoint to use.

        - `class_name: optional string`

        - `default_headers: optional map[string]`

          The default headers for API requests.

        - `dimensions: optional number`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size: optional number`

          The batch size for embedding calls.

        - `max_retries: optional number`

          Maximum number of retries.

        - `model_name: optional string`

          The name of the OpenAI embedding model.

        - `num_workers: optional number`

          The number of workers to use for async embedding calls.

        - `reuse_client: optional boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout: optional number`

          Timeout for each request.

      - `type: optional "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `cohere_embedding_config: object { component, type }`

      - `component: optional object { api_key, class_name, embed_batch_size, 5 more }`

        Configuration for the Cohere embedding model.

        - `api_key: string`

          The Cohere API key.

        - `class_name: optional string`

        - `embed_batch_size: optional number`

          The batch size for embedding calls.

        - `embedding_type: optional string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type: optional string`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name: optional string`

          The modelId of the Cohere model to use.

        - `num_workers: optional number`

          The number of workers to use for async embedding calls.

        - `truncate: optional string`

          Truncation type - START/ END/ NONE

      - `type: optional "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `gemini_embedding_config: object { component, type }`

      - `component: optional object { api_base, api_key, class_name, 7 more }`

        Configuration for the Gemini embedding model.

        - `api_base: optional string`

          API base to access the model. Defaults to None.

        - `api_key: optional string`

          API key to access the model. Defaults to None.

        - `class_name: optional string`

        - `embed_batch_size: optional number`

          The batch size for embedding calls.

        - `model_name: optional string`

          The modelId of the Gemini model to use.

        - `num_workers: optional number`

          The number of workers to use for async embedding calls.

        - `output_dimensionality: optional number`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type: optional string`

          The task for embedding model.

        - `title: optional string`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport: optional string`

          Transport to access the model. Defaults to None.

      - `type: optional "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `hugging_face_inference_api_embedding_config: object { component, type }`

      - `component: optional object { token, class_name, cookies, 9 more }`

        Configuration for the HuggingFace Inference API embedding model.

        - `token: optional string or boolean`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `union_member_0: string`

          - `union_member_1: boolean`

        - `class_name: optional string`

        - `cookies: optional map[string]`

          Additional cookies to send to the server.

        - `embed_batch_size: optional number`

          The batch size for embedding calls.

        - `headers: optional map[string]`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name: optional string`

          Hugging Face model name. If None, the task will be used.

        - `num_workers: optional number`

          The number of workers to use for async embedding calls.

        - `pooling: optional "cls" or "mean" or "last"`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction: optional string`

          Instruction to prepend during query embedding.

        - `task: optional string`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction: optional string`

          Instruction to prepend during text embedding.

        - `timeout: optional number`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type: optional "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `openai_embedding_config: object { component, type }`

      - `component: optional object { additional_kwargs, api_base, api_key, 10 more }`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs: optional map[unknown]`

          Additional kwargs for the OpenAI API.

        - `api_base: optional string`

          The base URL for OpenAI API.

        - `api_key: optional string`

          The OpenAI API key.

        - `api_version: optional string`

          The version for OpenAI API.

        - `class_name: optional string`

        - `default_headers: optional map[string]`

          The default headers for API requests.

        - `dimensions: optional number`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size: optional number`

          The batch size for embedding calls.

        - `max_retries: optional number`

          Maximum number of retries.

        - `model_name: optional string`

          The name of the OpenAI embedding model.

        - `num_workers: optional number`

          The number of workers to use for async embedding calls.

        - `reuse_client: optional boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout: optional number`

          Timeout for each request.

      - `type: optional "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `vertex_ai_embedding_config: object { component, type }`

      - `component: optional object { client_email, location, private_key, 9 more }`

        Configuration for the VertexAI embedding model.

        - `client_email: string`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string`

          The private key for the VertexAI credentials.

        - `private_key_id: string`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string`

          The token URI for the VertexAI credentials.

        - `additional_kwargs: optional map[unknown]`

          Additional kwargs for the Vertex.

        - `class_name: optional string`

        - `embed_batch_size: optional number`

          The batch size for embedding calls.

        - `embed_mode: optional "default" or "classification" or "clustering" or 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name: optional string`

          The modelId of the VertexAI model to use.

        - `num_workers: optional number`

          The number of workers to use for async embedding calls.

      - `type: optional "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `bedrock_embedding_config: object { component, type }`

      - `component: optional object { additional_kwargs, aws_access_key_id, aws_secret_access_key, 9 more }`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs: optional map[unknown]`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id: optional string`

          AWS Access Key ID to use

        - `aws_secret_access_key: optional string`

          AWS Secret Access Key to use

        - `aws_session_token: optional string`

          AWS Session Token to use

        - `class_name: optional string`

        - `embed_batch_size: optional number`

          The batch size for embedding calls.

        - `max_retries: optional number`

          The maximum number of API retries.

        - `model_name: optional string`

          The modelId of the Bedrock model to use.

        - `num_workers: optional number`

          The number of workers to use for async embedding calls.

        - `profile_name: optional string`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name: optional string`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout: optional number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type: optional "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash: optional object { embedding_config_hash, parsing_config_hash, transform_config_hash }`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash: optional string`

      Hash of the embedding config.

    - `parsing_config_hash: optional string`

      Hash of the llama parse parameters.

    - `transform_config_hash: optional string`

      Hash of the transform config.

  - `created_at: optional string`

    Creation datetime

  - `data_sink: optional object { id, component, name, 4 more }`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: map[unknown] or CloudPineconeVectorStore or CloudPostgresVectorStore or 5 more`

      Component that implements the data sink

      - `union_member_0: map[unknown]`

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

      - `cloud_milvus_vector_store: object { uri, token, class_name, 3 more }`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token: optional string`

        - `class_name: optional string`

        - `collection_name: optional string`

        - `embedding_dimension: optional number`

        - `supports_nested_metadata_filters: optional boolean`

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

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" or "POSTGRES" or "QDRANT" or 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at: optional string`

      Creation datetime

    - `updated_at: optional string`

      Update datetime

  - `embedding_model_config: optional object { id, embedding_config, name, 3 more }`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig or CohereEmbeddingConfig or GeminiEmbeddingConfig or 4 more`

      The embedding configuration for the embedding model config.

      - `azure_openai_embedding_config: object { component, type }`

      - `cohere_embedding_config: object { component, type }`

      - `gemini_embedding_config: object { component, type }`

      - `hugging_face_inference_api_embedding_config: object { component, type }`

      - `openai_embedding_config: object { component, type }`

      - `vertex_ai_embedding_config: object { component, type }`

      - `bedrock_embedding_config: object { component, type }`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at: optional string`

      Creation datetime

    - `updated_at: optional string`

      Update datetime

  - `embedding_model_config_id: optional string`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters: optional object { adaptive_long_table, aggressive_table_extraction, annotate_links, 116 more }`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table: optional boolean`

    - `aggressive_table_extraction: optional boolean`

    - `annotate_links: optional boolean`

    - `auto_mode: optional boolean`

    - `auto_mode_configuration_json: optional string`

    - `auto_mode_trigger_on_image_in_page: optional boolean`

    - `auto_mode_trigger_on_regexp_in_page: optional string`

    - `auto_mode_trigger_on_table_in_page: optional boolean`

    - `auto_mode_trigger_on_text_in_page: optional string`

    - `azure_openai_api_version: optional string`

    - `azure_openai_deployment_name: optional string`

    - `azure_openai_endpoint: optional string`

    - `azure_openai_key: optional string`

    - `bbox_bottom: optional number`

    - `bbox_left: optional number`

    - `bbox_right: optional number`

    - `bbox_top: optional number`

    - `bounding_box: optional string`

    - `compact_markdown_table: optional boolean`

    - `complemental_formatting_instruction: optional string`

    - `content_guideline_instruction: optional string`

    - `continuous_mode: optional boolean`

    - `disable_image_extraction: optional boolean`

    - `disable_ocr: optional boolean`

    - `disable_reconstruction: optional boolean`

    - `do_not_cache: optional boolean`

    - `do_not_unroll_columns: optional boolean`

    - `enable_cost_optimizer: optional boolean`

    - `extract_charts: optional boolean`

    - `extract_layout: optional boolean`

    - `extract_printed_page_number: optional boolean`

    - `fast_mode: optional boolean`

    - `formatting_instruction: optional string`

    - `gpt4o_api_key: optional string`

    - `gpt4o_mode: optional boolean`

    - `guess_xlsx_sheet_name: optional boolean`

    - `hide_footers: optional boolean`

    - `hide_headers: optional boolean`

    - `high_res_ocr: optional boolean`

    - `html_make_all_elements_visible: optional boolean`

    - `html_remove_fixed_elements: optional boolean`

    - `html_remove_navigation_elements: optional boolean`

    - `http_proxy: optional string`

    - `ignore_document_elements_for_layout_detection: optional boolean`

    - `images_to_save: optional array of "screenshot" or "embedded" or "layout"`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown: optional boolean`

    - `input_s3_path: optional string`

    - `input_s3_region: optional string`

    - `input_url: optional string`

    - `internal_is_screenshot_job: optional boolean`

    - `invalidate_cache: optional boolean`

    - `is_formatting_instruction: optional boolean`

    - `job_timeout_extra_time_per_page_in_seconds: optional number`

    - `job_timeout_in_seconds: optional number`

    - `keep_page_separator_when_merging_tables: optional boolean`

    - `languages: optional array of ParsingLanguages`

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

    - `layout_aware: optional boolean`

    - `line_level_bounding_box: optional boolean`

    - `markdown_table_multiline_header_separator: optional string`

    - `max_pages: optional number`

    - `max_pages_enforced: optional number`

    - `merge_tables_across_pages_in_markdown: optional boolean`

    - `model: optional string`

    - `outlined_table_extraction: optional boolean`

    - `output_pdf_of_document: optional boolean`

    - `output_s3_path_prefix: optional string`

    - `output_s3_region: optional string`

    - `output_tables_as_HTML: optional boolean`

    - `page_error_tolerance: optional number`

    - `page_footer_prefix: optional string`

    - `page_footer_suffix: optional string`

    - `page_header_prefix: optional string`

    - `page_header_suffix: optional string`

    - `page_prefix: optional string`

    - `page_separator: optional string`

    - `page_suffix: optional string`

    - `parse_mode: optional "parse_page_without_llm" or "parse_page_with_llm" or "parse_page_with_lvm" or 5 more`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction: optional string`

    - `precise_bounding_box: optional boolean`

    - `premium_mode: optional boolean`

    - `presentation_out_of_bounds_content: optional boolean`

    - `presentation_skip_embedded_data: optional boolean`

    - `preserve_layout_alignment_across_pages: optional boolean`

    - `preserve_very_small_text: optional boolean`

    - `preset: optional string`

    - `priority: optional "low" or "medium" or "high" or "critical"`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id: optional string`

    - `remove_hidden_text: optional boolean`

    - `replace_failed_page_mode: optional "raw_text" or "blank_page" or "error_message"`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix: optional string`

    - `replace_failed_page_with_error_message_suffix: optional string`

    - `save_images: optional boolean`

    - `skip_diagonal_text: optional boolean`

    - `specialized_chart_parsing_agentic: optional boolean`

    - `specialized_chart_parsing_efficient: optional boolean`

    - `specialized_chart_parsing_plus: optional boolean`

    - `specialized_image_parsing: optional boolean`

    - `spreadsheet_extract_sub_tables: optional boolean`

    - `spreadsheet_force_formula_computation: optional boolean`

    - `spreadsheet_include_hidden_sheets: optional boolean`

    - `strict_mode_buggy_font: optional boolean`

    - `strict_mode_image_extraction: optional boolean`

    - `strict_mode_image_ocr: optional boolean`

    - `strict_mode_reconstruction: optional boolean`

    - `structured_output: optional boolean`

    - `structured_output_json_schema: optional string`

    - `structured_output_json_schema_name: optional string`

    - `system_prompt: optional string`

    - `system_prompt_append: optional string`

    - `take_screenshot: optional boolean`

    - `target_pages: optional string`

    - `tier: optional string`

    - `use_vendor_multimodal_model: optional boolean`

    - `user_prompt: optional string`

    - `vendor_multimodal_api_key: optional string`

    - `vendor_multimodal_model_name: optional string`

    - `version: optional string`

    - `webhook_configurations: optional array of object { webhook_events, webhook_headers, webhook_output_format, webhook_url }`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events: optional array of "extract.pending" or "extract.success" or "extract.error" or 14 more`

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

      - `webhook_headers: optional map[string]`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format: optional string`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url: optional string`

        URL to receive webhook POST notifications

    - `webhook_url: optional string`

  - `managed_pipeline_id: optional string`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config: optional object { excluded_embed_metadata_keys, excluded_llm_metadata_keys }`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys: optional array of string`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys: optional array of string`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type: optional "PLAYGROUND" or "MANAGED"`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters: optional object { alpha, class_name, dense_similarity_cutoff, 11 more }`

    Preset retrieval parameters for the pipeline.

    - `alpha: optional number`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name: optional string`

    - `dense_similarity_cutoff: optional number`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k: optional number`

      Number of nodes for dense retrieval.

    - `enable_reranking: optional boolean`

      Enable reranking for retrieval

    - `files_top_k: optional number`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n: optional number`

      Number of reranked nodes for returning.

    - `retrieval_mode: optional "chunks" or "files_via_metadata" or "files_via_content" or "auto_routed"`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes: optional boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes: optional boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes: optional boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters: optional object { filters, condition }`

      Metadata filters for vector stores.

      - `filters: array of object { key, value, operator }  or MetadataFilters`

        - `MetadataFilter: object { key, value, operator }`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number or string or array of string or 2 more`

            - `union_member_0: number`

            - `union_member_1: string`

            - `union_member_2: array of string`

            - `union_member_3: array of number`

            - `union_member_4: array of number`

          - `operator: optional "==" or ">" or "<" or 11 more`

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

        - `metadata_filters: object { filters, condition }`

          Metadata filters for vector stores.

          - `filters: array of object { key, value, operator }  or MetadataFilters`

          - `condition: optional "and" or "or" or "not"`

            Vector store filter conditions to combine different filters.

            - `"and"`

            - `"or"`

            - `"not"`

      - `condition: optional "and" or "or" or "not"`

        Vector store filter conditions to combine different filters.

    - `search_filters_inference_schema: optional map[map[unknown] or array of unknown or string or 2 more]`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `sparse_similarity_top_k: optional number`

      Number of nodes for sparse retrieval.

  - `sparse_model_config: optional object { class_name, model_type }`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name: optional string`

    - `model_type: optional "splade" or "bm25" or "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status: optional "CREATED" or "DELETING"`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config: optional AutoTransformConfig or AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `auto_transform_config: object { chunk_overlap, chunk_size, mode }`

      - `chunk_overlap: optional number`

        Chunk overlap for the transformation.

      - `chunk_size: optional number`

        Chunk size for the transformation.

      - `mode: optional "auto"`

        - `"auto"`

    - `advanced_mode_transform_config: object { chunking_config, mode, segmentation_config }`

      - `chunking_config: optional object { mode }  or object { chunk_overlap, chunk_size, mode }  or object { chunk_overlap, chunk_size, mode, separator }  or 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig: object { mode }`

          - `mode: optional "none"`

            - `"none"`

        - `CharacterChunkingConfig: object { chunk_overlap, chunk_size, mode }`

          - `chunk_overlap: optional number`

          - `chunk_size: optional number`

          - `mode: optional "character"`

            - `"character"`

        - `TokenChunkingConfig: object { chunk_overlap, chunk_size, mode, separator }`

          - `chunk_overlap: optional number`

          - `chunk_size: optional number`

          - `mode: optional "token"`

            - `"token"`

          - `separator: optional string`

        - `SentenceChunkingConfig: object { chunk_overlap, chunk_size, mode, 2 more }`

          - `chunk_overlap: optional number`

          - `chunk_size: optional number`

          - `mode: optional "sentence"`

            - `"sentence"`

          - `paragraph_separator: optional string`

          - `separator: optional string`

        - `SemanticChunkingConfig: object { breakpoint_percentile_threshold, buffer_size, mode }`

          - `breakpoint_percentile_threshold: optional number`

          - `buffer_size: optional number`

          - `mode: optional "semantic"`

            - `"semantic"`

      - `mode: optional "advanced"`

        - `"advanced"`

      - `segmentation_config: optional object { mode }  or object { mode, page_separator }  or object { mode }`

        Configuration for the segmentation.

        - `NoneSegmentationConfig: object { mode }`

          - `mode: optional "none"`

            - `"none"`

        - `PageSegmentationConfig: object { mode, page_separator }`

          - `mode: optional "page"`

            - `"page"`

          - `page_separator: optional string`

        - `ElementSegmentationConfig: object { mode }`

          - `mode: optional "element"`

            - `"element"`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod pipelines:data-sources sync \
  --api-key 'My API Key' \
  --pipeline-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e \
  --data-source-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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

- `pipeline_data_source: object { id, component, data_source_id, 13 more }`

  Schema for a data source in a pipeline.

  - `id: string`

    Unique identifier

  - `component: map[unknown] or CloudS3DataSource or CloudAzStorageBlobDataSource or 9 more`

    Component that implements the data source

    - `union_member_0: map[unknown]`

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

    - `cloud_google_drive_data_source: object { folder_id, class_name, service_account_key, supports_access_control }`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name: optional string`

      - `service_account_key: optional map[string]`

        A dictionary containing secret values

      - `supports_access_control: optional boolean`

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

    - `cloud_notion_page_data_source: object { integration_token, class_name, database_ids, 2 more }`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name: optional string`

      - `database_ids: optional string`

        The Notion Database Id to read content from.

      - `page_ids: optional string`

        The Page ID's of the Notion to read from.

      - `supports_access_control: optional boolean`

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

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" or "AZURE_STORAGE_BLOB" or "GOOGLE_DRIVE" or 8 more`

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

  - `created_at: optional string`

    Creation datetime

  - `custom_metadata: optional map[map[unknown] or array of unknown or string or 2 more]`

    Custom metadata that will be present on all data loaded from the data source

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

  - `status: optional "NOT_STARTED" or "IN_PROGRESS" or "SUCCESS" or 2 more`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at: optional string`

    The last time the status was updated.

  - `sync_interval: optional number`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by: optional string`

    The id of the user who set the sync schedule.

  - `updated_at: optional string`

    Update datetime

  - `version_metadata: optional object { reader_version }`

    Version metadata for the data source

    - `reader_version: optional "1.0" or "2.0" or "2.1"`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`
