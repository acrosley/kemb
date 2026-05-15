## List Pipeline Data Sources

**get** `/api/v1/pipelines/{pipeline_id}/data-sources`

Get data sources for a pipeline.

### Path Parameters

- `pipeline_id: string`

### Cookie Parameters

- `session: optional string`

### Returns

- `id: string`

  Unique identifier

- `component: map[unknown] or CloudS3DataSource or CloudAzStorageBlobDataSource or 9 more`

  Component that implements the data source

  - `map[unknown]`

  - `CloudS3DataSource = object { bucket, aws_access_id, aws_access_secret, 5 more }`

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

  - `CloudAzStorageBlobDataSource = object { account_url, container_name, account_key, 8 more }`

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

  - `CloudGoogleDriveDataSource = object { folder_id, class_name, service_account_key, supports_access_control }`

    - `folder_id: string`

      The ID of the Google Drive folder to read from.

    - `class_name: optional string`

    - `service_account_key: optional map[string]`

      A dictionary containing secret values

    - `supports_access_control: optional boolean`

  - `CloudOneDriveDataSource = object { client_id, client_secret, tenant_id, 6 more }`

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

  - `CloudSharepointDataSource = object { client_id, client_secret, tenant_id, 11 more }`

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

  - `CloudSlackDataSource = object { slack_token, channel_ids, channel_patterns, 6 more }`

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

  - `CloudNotionPageDataSource = object { integration_token, class_name, database_ids, 2 more }`

    - `integration_token: string`

      The integration token to use for authentication.

    - `class_name: optional string`

    - `database_ids: optional string`

      The Notion Database Id to read content from.

    - `page_ids: optional string`

      The Page ID's of the Notion to read from.

    - `supports_access_control: optional boolean`

  - `CloudConfluenceDataSource = object { authentication_mechanism, server_url, api_token, 10 more }`

    - `authentication_mechanism: string`

      Type of Authentication for connecting to Confluence APIs.

    - `server_url: string`

      The server URL of the Confluence instance.

    - `api_token: optional string`

      The API token to use for authentication.

    - `class_name: optional string`

    - `cql: optional string`

      The CQL query to use for fetching pages.

    - `failure_handling: optional FailureHandlingConfig`

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

  - `CloudJiraDataSource = object { authentication_mechanism, query, api_token, 5 more }`

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

  - `CloudJiraDataSourceV2 = object { authentication_mechanism, query, server_url, 10 more }`

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

  - `CloudBoxDataSource = object { authentication_mechanism, class_name, client_id, 6 more }`

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

  - `map[unknown]`

  - `array of unknown`

  - `string`

  - `number`

  - `boolean`

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

- `version_metadata: optional DataSourceReaderVersionMetadata`

  Version metadata for the data source

  - `reader_version: optional "1.0" or "2.0" or "2.1"`

    The version of the reader to use for this data source.

    - `"1.0"`

    - `"2.0"`

    - `"2.1"`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v1/pipelines/$PIPELINE_ID/data-sources \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
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
