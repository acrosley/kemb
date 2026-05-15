## Get Data Source

`client.dataSources.get(stringdataSourceID, RequestOptionsoptions?): DataSource`

**get** `/api/v1/data-sources/{data_source_id}`

Get a data source by ID.

### Parameters

- `dataSourceID: string`

### Returns

- `DataSource`

  Schema for a data source.

  - `id: string`

    Unique identifier

  - `component: Record<string, unknown> | CloudS3DataSource | CloudAzStorageBlobDataSource | 9 more`

    Component that implements the data source

    - `Record<string, unknown>`

    - `CloudS3DataSource`

      - `bucket: string`

        The name of the S3 bucket to read from.

      - `aws_access_id?: string | null`

        The AWS access ID to use for authentication.

      - `aws_access_secret?: string | null`

        The AWS access secret to use for authentication.

      - `class_name?: string`

      - `prefix?: string | null`

        The prefix of the S3 objects to read from.

      - `regex_pattern?: string | null`

        The regex pattern to filter S3 objects. Must be a valid regex pattern.

      - `s3_endpoint_url?: string | null`

        The S3 endpoint URL to use for authentication.

      - `supports_access_control?: boolean`

    - `CloudAzStorageBlobDataSource`

      - `account_url: string`

        The Azure Storage Blob account URL to use for authentication.

      - `container_name: string`

        The name of the Azure Storage Blob container to read from.

      - `account_key?: string | null`

        The Azure Storage Blob account key to use for authentication.

      - `account_name?: string | null`

        The Azure Storage Blob account name to use for authentication.

      - `blob?: string | null`

        The blob name to read from.

      - `class_name?: string`

      - `client_id?: string | null`

        The Azure AD client ID to use for authentication.

      - `client_secret?: string | null`

        The Azure AD client secret to use for authentication.

      - `prefix?: string | null`

        The prefix of the Azure Storage Blob objects to read from.

      - `supports_access_control?: boolean`

      - `tenant_id?: string | null`

        The Azure AD tenant ID to use for authentication.

    - `CloudGoogleDriveDataSource`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name?: string`

      - `service_account_key?: Record<string, string> | null`

        A dictionary containing secret values

      - `supports_access_control?: boolean`

    - `CloudOneDriveDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `user_principal_name: string`

        The user principal name to use for authentication.

      - `class_name?: string`

      - `folder_id?: string | null`

        The ID of the OneDrive folder to read from.

      - `folder_path?: string | null`

        The path of the OneDrive folder to read from.

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `supports_access_control?: true`

        - `true`

    - `CloudSharepointDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `class_name?: string`

      - `drive_name?: string | null`

        The name of the Sharepoint drive to read from.

      - `exclude_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

      - `folder_id?: string | null`

        The ID of the Sharepoint folder to read from.

      - `folder_path?: string | null`

        The path of the Sharepoint folder to read from.

      - `get_permissions?: boolean | null`

        Whether to get permissions for the sharepoint site.

      - `include_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `site_id?: string | null`

        The ID of the SharePoint site to download from.

      - `site_name?: string | null`

        The name of the SharePoint site to download from.

      - `supports_access_control?: true`

        - `true`

    - `CloudSlackDataSource`

      - `slack_token: string`

        Slack Bot Token.

      - `channel_ids?: string | null`

        Slack Channel.

      - `channel_patterns?: string | null`

        Slack Channel name pattern.

      - `class_name?: string`

      - `earliest_date?: string | null`

        Earliest date.

      - `earliest_date_timestamp?: number | null`

        Earliest date timestamp.

      - `latest_date?: string | null`

        Latest date.

      - `latest_date_timestamp?: number | null`

        Latest date timestamp.

      - `supports_access_control?: boolean`

    - `CloudNotionPageDataSource`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name?: string`

      - `database_ids?: string | null`

        The Notion Database Id to read content from.

      - `page_ids?: string | null`

        The Page ID's of the Notion to read from.

      - `supports_access_control?: boolean`

    - `CloudConfluenceDataSource`

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Confluence APIs.

      - `server_url: string`

        The server URL of the Confluence instance.

      - `api_token?: string | null`

        The API token to use for authentication.

      - `class_name?: string`

      - `cql?: string | null`

        The CQL query to use for fetching pages.

      - `failure_handling?: FailureHandlingConfig`

        Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

        Example:
        {
        "skip_list_failures": true
        }

        Currently supports:

        - skip_list_failures: Skip failed batches/lists and continue processing

        - `skip_list_failures?: boolean`

          Whether to skip failed batches/lists and continue processing

      - `index_restricted_pages?: boolean`

        Whether to index restricted pages.

      - `keep_markdown_format?: boolean`

        Whether to keep the markdown format.

      - `label?: string | null`

        The label to use for fetching pages.

      - `page_ids?: string | null`

        The page IDs of the Confluence to read from.

      - `space_key?: string | null`

        The space key to read from.

      - `supports_access_control?: boolean`

      - `user_name?: string | null`

        The username to use for authentication.

    - `CloudJiraDataSource`

      Cloud Jira Data Source integrating JiraReader.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `api_token?: string | null`

        The API/ Access Token used for Basic, PAT and OAuth2 authentication.

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `server_url?: string | null`

        The server url for Jira Cloud.

      - `supports_access_control?: boolean`

    - `CloudJiraDataSourceV2`

      Cloud Jira Data Source integrating JiraReaderV2.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `server_url: string`

        The server url for Jira Cloud.

      - `api_token?: string | null`

        The API Access Token used for Basic, PAT and OAuth2 authentication.

      - `api_version?: "2" | "3"`

        Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

        - `"2"`

        - `"3"`

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `expand?: string | null`

        Fields to expand in the response.

      - `fields?: Array<string> | null`

        List of fields to retrieve from Jira. If None, retrieves all fields.

      - `get_permissions?: boolean`

        Whether to fetch project role permissions and issue-level security

      - `requests_per_minute?: number | null`

        Rate limit for Jira API requests per minute.

      - `supports_access_control?: boolean`

    - `CloudBoxDataSource`

      - `authentication_mechanism: "developer_token" | "ccg"`

        The type of authentication to use (Developer Token or CCG)

        - `"developer_token"`

        - `"ccg"`

      - `class_name?: string`

      - `client_id?: string | null`

        Box API key used for identifying the application the user is authenticating with

      - `client_secret?: string | null`

        Box API secret used for making auth requests.

      - `developer_token?: string | null`

        Developer token for authentication if authentication_mechanism is 'developer_token'.

      - `enterprise_id?: string | null`

        Box Enterprise ID, if provided authenticates as service.

      - `folder_id?: string | null`

        The ID of the Box folder to read from.

      - `supports_access_control?: boolean`

      - `user_id?: string | null`

        Box User ID, if provided authenticates as user.

  - `name: string`

    The name of the data source.

  - `project_id: string`

  - `source_type: "S3" | "AZURE_STORAGE_BLOB" | "GOOGLE_DRIVE" | 8 more`

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

  - `created_at?: string | null`

    Creation datetime

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata that will be present on all data loaded from the data source

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

  - `version_metadata?: DataSourceReaderVersionMetadata | null`

    Version metadata for the data source

    - `reader_version?: "1.0" | "2.0" | "2.1" | null`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const dataSource = await client.dataSources.get('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(dataSource.id);
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
