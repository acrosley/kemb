# Beta

# Agent Data

## Get Agent Data

`$ llamacloud-prod beta:agent-data get`

**get** `/api/v1/beta/agent-data/{item_id}`

Get agent data by ID.

### Parameters

- `--item-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

### Example

```cli
llamacloud-prod beta:agent-data get \
  --api-key 'My API Key' \
  --item-id item_id
```

#### Response

```json
{
  "data": {
    "foo": "bar"
  },
  "deployment_name": "deployment_name",
  "id": "id",
  "collection": "collection",
  "created_at": "2019-12-27T18:11:19.117Z",
  "project_id": "project_id",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Agent Data

`$ llamacloud-prod beta:agent-data update`

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Parameters

- `--item-id: string`

  Path param

- `--data: map[unknown]`

  Body param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Returns

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

### Example

```cli
llamacloud-prod beta:agent-data update \
  --api-key 'My API Key' \
  --item-id item_id \
  --data '{foo: bar}'
```

#### Response

```json
{
  "data": {
    "foo": "bar"
  },
  "deployment_name": "deployment_name",
  "id": "id",
  "collection": "collection",
  "created_at": "2019-12-27T18:11:19.117Z",
  "project_id": "project_id",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Agent Data

`$ llamacloud-prod beta:agent-data delete`

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Parameters

- `--item-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaAgentDataDeleteResponse: map[string]`

### Example

```cli
llamacloud-prod beta:agent-data delete \
  --api-key 'My API Key' \
  --item-id item_id
```

#### Response

```json
{
  "foo": "string"
}
```

## Create Agent Data

`$ llamacloud-prod beta:agent-data create`

**post** `/api/v1/beta/agent-data`

Create new agent data.

### Parameters

- `--data: map[unknown]`

  Body param

- `--deployment-name: string`

  Body param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param

### Returns

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

### Example

```cli
llamacloud-prod beta:agent-data create \
  --api-key 'My API Key' \
  --data '{foo: bar}' \
  --deployment-name deployment_name
```

#### Response

```json
{
  "data": {
    "foo": "bar"
  },
  "deployment_name": "deployment_name",
  "id": "id",
  "collection": "collection",
  "created_at": "2019-12-27T18:11:19.117Z",
  "project_id": "project_id",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Search Agent Data

`$ llamacloud-prod beta:agent-data search`

**post** `/api/v1/beta/agent-data/:search`

Search agent data with filtering, sorting, and pagination.

### Parameters

- `--deployment-name: string`

  Body param: The agent deployment's name to search within

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param: The logical agent data collection to search within

- `--filter: optional map[object { eq, excludes, gt, 5 more } ]`

  Body param: A filter object or expression that filters resources listed in the response.

- `--include-total: optional boolean`

  Body param: Whether to include the total number of items in the response

- `--offset: optional number`

  Body param: The offset to start from. If not provided, the first page is returned

- `--order-by: optional string`

  Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `--page-size: optional number`

  Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `--page-token: optional string`

  Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `PaginatedResponse_AgentData_: object { items, next_page_token, total_size }`

  - `items: array of AgentData`

    The list of items.

    - `data: map[unknown]`

    - `deployment_name: string`

    - `id: optional string`

    - `collection: optional string`

    - `created_at: optional string`

    - `project_id: optional string`

    - `updated_at: optional string`

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:agent-data search \
  --api-key 'My API Key' \
  --deployment-name deployment_name
```

#### Response

```json
{
  "items": [
    {
      "data": {
        "foo": "bar"
      },
      "deployment_name": "deployment_name",
      "id": "id",
      "collection": "collection",
      "created_at": "2019-12-27T18:11:19.117Z",
      "project_id": "project_id",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Aggregate Agent Data

`$ llamacloud-prod beta:agent-data aggregate`

**post** `/api/v1/beta/agent-data/:aggregate`

Aggregate agent data with grouping and optional counting/first item retrieval.

### Parameters

- `--deployment-name: string`

  Body param: The agent deployment's name to aggregate data for

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param: The logical agent data collection to aggregate data for

- `--count: optional boolean`

  Body param: Whether to count the number of items in each group

- `--filter: optional map[object { eq, excludes, gt, 5 more } ]`

  Body param: A filter object or expression that filters resources listed in the response.

- `--first: optional boolean`

  Body param: Whether to return the first item in each group (Sorted by created_at)

- `--group-by: optional array of string`

  Body param: The fields to group by. If empty, the entire dataset is grouped on. e.g. if left out, can be used for simple count operations

- `--offset: optional number`

  Body param: The offset to start from. If not provided, the first page is returned

- `--order-by: optional string`

  Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `--page-size: optional number`

  Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `--page-token: optional string`

  Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `PaginatedResponse_AggregateGroup_: object { items, next_page_token, total_size }`

  - `items: array of object { group_key, count, first_item }`

    The list of items.

    - `group_key: map[unknown]`

    - `count: optional number`

    - `first_item: optional map[unknown]`

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:agent-data aggregate \
  --api-key 'My API Key' \
  --deployment-name deployment_name
```

#### Response

```json
{
  "items": [
    {
      "group_key": {
        "foo": "bar"
      },
      "count": 0,
      "first_item": {
        "foo": "bar"
      }
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Delete Agent Data By Query

`$ llamacloud-prod beta:agent-data delete-by-query`

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Parameters

- `--deployment-name: string`

  Body param: The agent deployment's name to delete data for

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--collection: optional string`

  Body param: The logical agent data collection to delete from

- `--filter: optional map[object { eq, excludes, gt, 5 more } ]`

  Body param: Optional filters to select which items to delete

### Returns

- `BetaAgentDataDeleteByQueryResponse: object { deleted_count }`

  API response for bulk delete operation

  - `deleted_count: number`

### Example

```cli
llamacloud-prod beta:agent-data delete-by-query \
  --api-key 'My API Key' \
  --deployment-name deployment_name
```

#### Response

```json
{
  "deleted_count": 0
}
```

## Domain Types

### Agent Data

- `agent_data: object { data, deployment_name, id, 4 more }`

  API Result for a single agent data item

  - `data: map[unknown]`

  - `deployment_name: string`

  - `id: optional string`

  - `collection: optional string`

  - `created_at: optional string`

  - `project_id: optional string`

  - `updated_at: optional string`

# Sheets

## Create Spreadsheet Job

`$ llamacloud-prod beta:sheets create`

**post** `/api/v1/beta/sheets/jobs`

Create a spreadsheet parsing job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--file-id: string`

  Body param: The ID of the file to parse

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--config: optional object { extraction_range, flatten_hierarchical_tables, generate_additional_metadata, 5 more }`

  Body param: Configuration for the parsing job

### Returns

- `sheets_job: object { id, config, created_at, 10 more }`

  A spreadsheet parsing job

  - `id: string`

    The ID of the job

  - `config: object { extraction_range, flatten_hierarchical_tables, generate_additional_metadata, 5 more }`

    Configuration for the parsing job

    - `extraction_range: optional string`

      A1 notation of the range to extract a single region from. If None, the entire sheet is used.

    - `flatten_hierarchical_tables: optional boolean`

      Return a flattened dataframe when a detected table is recognized as hierarchical.

    - `generate_additional_metadata: optional boolean`

      Whether to generate additional metadata (title, description) for each extracted region.

    - `include_hidden_cells: optional boolean`

      Whether to include hidden cells when extracting regions from the spreadsheet.

    - `sheet_names: optional array of string`

      The names of the sheets to extract regions from. If empty, all sheets will be processed.

    - `specialization: optional string`

      Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

    - `table_merge_sensitivity: optional "strong" or "weak"`

      Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

      - `"strong"`

      - `"weak"`

    - `use_experimental_processing: optional boolean`

      Enables experimental processing. Accuracy may be impacted.

  - `created_at: string`

    When the job was created

  - `file_id: string`

    The ID of the input file

  - `project_id: string`

    The ID of the project

  - `status: "PENDING" or "SUCCESS" or "ERROR" or 2 more`

    The status of the parsing job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `updated_at: string`

    When the job was last updated

  - `user_id: string`

    The ID of the user

  - `errors: optional array of string`

    Any errors encountered

  - `file: optional object { id, name, project_id, 11 more }`

    Schema for a file.

    - `id: string`

      Unique identifier

    - `name: string`

    - `project_id: string`

      The ID of the project that the file belongs to

    - `created_at: optional string`

      Creation datetime

    - `data_source_id: optional string`

      The ID of the data source that the file belongs to

    - `expires_at: optional string`

      The expiration date for the file. Files past this date can be deleted.

    - `external_file_id: optional string`

      The ID of the file in the external system

    - `file_size: optional number`

      Size of the file in bytes

    - `file_type: optional string`

      File type (e.g. pdf, docx, etc.)

    - `last_modified_at: optional string`

      The last modified time of the file

    - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

      Permission information for the file

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `purpose: optional string`

      The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

    - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

      Resource information for the file

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `updated_at: optional string`

      Update datetime

  - `regions: optional array of object { location, region_type, sheet_name, 3 more }`

    All extracted regions (populated when job is complete)

    - `location: string`

      Location of the region in the spreadsheet

    - `region_type: string`

      Type of the extracted region

    - `sheet_name: string`

      Worksheet name where region was found

    - `description: optional string`

      Generated description for the region

    - `region_id: optional string`

      Unique identifier for this region within the file

    - `title: optional string`

      Generated title for the region

  - `success: optional boolean`

    Whether the job completed successfully

  - `worksheet_metadata: optional array of object { sheet_name, description, title }`

    Metadata for each processed worksheet (populated when job is complete)

    - `sheet_name: string`

      Name of the worksheet

    - `description: optional string`

      Generated description of the worksheet

    - `title: optional string`

      Generated title for the worksheet

### Example

```cli
llamacloud-prod beta:sheets create \
  --api-key 'My API Key' \
  --file-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
```

#### Response

```json
{
  "id": "id",
  "config": {
    "extraction_range": "extraction_range",
    "flatten_hierarchical_tables": true,
    "generate_additional_metadata": true,
    "include_hidden_cells": true,
    "sheet_names": [
      "string"
    ],
    "specialization": "specialization",
    "table_merge_sensitivity": "strong",
    "use_experimental_processing": true
  },
  "created_at": "created_at",
  "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "status": "PENDING",
  "updated_at": "updated_at",
  "user_id": "user_id",
  "errors": [
    "string"
  ],
  "file": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "name": "x",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "external_file_id": "external_file_id",
    "file_size": 0,
    "file_type": "x",
    "last_modified_at": "2019-12-27T18:11:19.117Z",
    "permission_info": {
      "foo": {
        "foo": "bar"
      }
    },
    "purpose": "purpose",
    "resource_info": {
      "foo": {
        "foo": "bar"
      }
    },
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "regions": [
    {
      "location": "location",
      "region_type": "region_type",
      "sheet_name": "sheet_name",
      "description": "description",
      "region_id": "region_id",
      "title": "title"
    }
  ],
  "success": true,
  "worksheet_metadata": [
    {
      "sheet_name": "sheet_name",
      "description": "description",
      "title": "title"
    }
  ]
}
```

## List Spreadsheet Jobs

`$ llamacloud-prod beta:sheets list`

**get** `/api/v1/beta/sheets/jobs`

List spreadsheet parsing jobs.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--created-at-on-or-after: optional string`

  Include items created at or after this timestamp (inclusive)

- `--created-at-on-or-before: optional string`

  Include items created at or before this timestamp (inclusive)

- `--include-results: optional boolean`

- `--job-id: optional array of string`

  Filter by specific job IDs

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--status: optional "PENDING" or "SUCCESS" or "ERROR" or 2 more`

  Filter by job status

### Returns

- `PaginatedResponse_SpreadsheetJob_: object { items, next_page_token, total_size }`

  - `items: array of SheetsJob`

    The list of items.

    - `id: string`

      The ID of the job

    - `config: object { extraction_range, flatten_hierarchical_tables, generate_additional_metadata, 5 more }`

      Configuration for the parsing job

      - `extraction_range: optional string`

        A1 notation of the range to extract a single region from. If None, the entire sheet is used.

      - `flatten_hierarchical_tables: optional boolean`

        Return a flattened dataframe when a detected table is recognized as hierarchical.

      - `generate_additional_metadata: optional boolean`

        Whether to generate additional metadata (title, description) for each extracted region.

      - `include_hidden_cells: optional boolean`

        Whether to include hidden cells when extracting regions from the spreadsheet.

      - `sheet_names: optional array of string`

        The names of the sheets to extract regions from. If empty, all sheets will be processed.

      - `specialization: optional string`

        Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

      - `table_merge_sensitivity: optional "strong" or "weak"`

        Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

        - `"strong"`

        - `"weak"`

      - `use_experimental_processing: optional boolean`

        Enables experimental processing. Accuracy may be impacted.

    - `created_at: string`

      When the job was created

    - `file_id: string`

      The ID of the input file

    - `project_id: string`

      The ID of the project

    - `status: "PENDING" or "SUCCESS" or "ERROR" or 2 more`

      The status of the parsing job

      - `"PENDING"`

      - `"SUCCESS"`

      - `"ERROR"`

      - `"PARTIAL_SUCCESS"`

      - `"CANCELLED"`

    - `updated_at: string`

      When the job was last updated

    - `user_id: string`

      The ID of the user

    - `errors: optional array of string`

      Any errors encountered

    - `file: optional object { id, name, project_id, 11 more }`

      Schema for a file.

      - `id: string`

        Unique identifier

      - `name: string`

      - `project_id: string`

        The ID of the project that the file belongs to

      - `created_at: optional string`

        Creation datetime

      - `data_source_id: optional string`

        The ID of the data source that the file belongs to

      - `expires_at: optional string`

        The expiration date for the file. Files past this date can be deleted.

      - `external_file_id: optional string`

        The ID of the file in the external system

      - `file_size: optional number`

        Size of the file in bytes

      - `file_type: optional string`

        File type (e.g. pdf, docx, etc.)

      - `last_modified_at: optional string`

        The last modified time of the file

      - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

        Permission information for the file

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `purpose: optional string`

        The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

      - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

        Resource information for the file

        - `union_member_0: map[unknown]`

        - `union_member_1: array of unknown`

        - `union_member_2: string`

        - `union_member_3: number`

        - `union_member_4: boolean`

      - `updated_at: optional string`

        Update datetime

    - `regions: optional array of object { location, region_type, sheet_name, 3 more }`

      All extracted regions (populated when job is complete)

      - `location: string`

        Location of the region in the spreadsheet

      - `region_type: string`

        Type of the extracted region

      - `sheet_name: string`

        Worksheet name where region was found

      - `description: optional string`

        Generated description for the region

      - `region_id: optional string`

        Unique identifier for this region within the file

      - `title: optional string`

        Generated title for the region

    - `success: optional boolean`

      Whether the job completed successfully

    - `worksheet_metadata: optional array of object { sheet_name, description, title }`

      Metadata for each processed worksheet (populated when job is complete)

      - `sheet_name: string`

        Name of the worksheet

      - `description: optional string`

        Generated description of the worksheet

      - `title: optional string`

        Generated title for the worksheet

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:sheets list \
  --api-key 'My API Key'
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "config": {
        "extraction_range": "extraction_range",
        "flatten_hierarchical_tables": true,
        "generate_additional_metadata": true,
        "include_hidden_cells": true,
        "sheet_names": [
          "string"
        ],
        "specialization": "specialization",
        "table_merge_sensitivity": "strong",
        "use_experimental_processing": true
      },
      "created_at": "created_at",
      "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "status": "PENDING",
      "updated_at": "updated_at",
      "user_id": "user_id",
      "errors": [
        "string"
      ],
      "file": {
        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "name": "x",
        "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "created_at": "2019-12-27T18:11:19.117Z",
        "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "expires_at": "2019-12-27T18:11:19.117Z",
        "external_file_id": "external_file_id",
        "file_size": 0,
        "file_type": "x",
        "last_modified_at": "2019-12-27T18:11:19.117Z",
        "permission_info": {
          "foo": {
            "foo": "bar"
          }
        },
        "purpose": "purpose",
        "resource_info": {
          "foo": {
            "foo": "bar"
          }
        },
        "updated_at": "2019-12-27T18:11:19.117Z"
      },
      "regions": [
        {
          "location": "location",
          "region_type": "region_type",
          "sheet_name": "sheet_name",
          "description": "description",
          "region_id": "region_id",
          "title": "title"
        }
      ],
      "success": true,
      "worksheet_metadata": [
        {
          "sheet_name": "sheet_name",
          "description": "description",
          "title": "title"
        }
      ]
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Spreadsheet Job

`$ llamacloud-prod beta:sheets get`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Get a spreadsheet parsing job.

When include_results=True (default), the response will include extracted regions and results
if the job is complete, eliminating the need for a separate /results call.

Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--spreadsheet-job-id: string`

- `--include-results: optional boolean`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `sheets_job: object { id, config, created_at, 10 more }`

  A spreadsheet parsing job

  - `id: string`

    The ID of the job

  - `config: object { extraction_range, flatten_hierarchical_tables, generate_additional_metadata, 5 more }`

    Configuration for the parsing job

    - `extraction_range: optional string`

      A1 notation of the range to extract a single region from. If None, the entire sheet is used.

    - `flatten_hierarchical_tables: optional boolean`

      Return a flattened dataframe when a detected table is recognized as hierarchical.

    - `generate_additional_metadata: optional boolean`

      Whether to generate additional metadata (title, description) for each extracted region.

    - `include_hidden_cells: optional boolean`

      Whether to include hidden cells when extracting regions from the spreadsheet.

    - `sheet_names: optional array of string`

      The names of the sheets to extract regions from. If empty, all sheets will be processed.

    - `specialization: optional string`

      Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

    - `table_merge_sensitivity: optional "strong" or "weak"`

      Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

      - `"strong"`

      - `"weak"`

    - `use_experimental_processing: optional boolean`

      Enables experimental processing. Accuracy may be impacted.

  - `created_at: string`

    When the job was created

  - `file_id: string`

    The ID of the input file

  - `project_id: string`

    The ID of the project

  - `status: "PENDING" or "SUCCESS" or "ERROR" or 2 more`

    The status of the parsing job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `updated_at: string`

    When the job was last updated

  - `user_id: string`

    The ID of the user

  - `errors: optional array of string`

    Any errors encountered

  - `file: optional object { id, name, project_id, 11 more }`

    Schema for a file.

    - `id: string`

      Unique identifier

    - `name: string`

    - `project_id: string`

      The ID of the project that the file belongs to

    - `created_at: optional string`

      Creation datetime

    - `data_source_id: optional string`

      The ID of the data source that the file belongs to

    - `expires_at: optional string`

      The expiration date for the file. Files past this date can be deleted.

    - `external_file_id: optional string`

      The ID of the file in the external system

    - `file_size: optional number`

      Size of the file in bytes

    - `file_type: optional string`

      File type (e.g. pdf, docx, etc.)

    - `last_modified_at: optional string`

      The last modified time of the file

    - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

      Permission information for the file

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `purpose: optional string`

      The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

    - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

      Resource information for the file

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `updated_at: optional string`

      Update datetime

  - `regions: optional array of object { location, region_type, sheet_name, 3 more }`

    All extracted regions (populated when job is complete)

    - `location: string`

      Location of the region in the spreadsheet

    - `region_type: string`

      Type of the extracted region

    - `sheet_name: string`

      Worksheet name where region was found

    - `description: optional string`

      Generated description for the region

    - `region_id: optional string`

      Unique identifier for this region within the file

    - `title: optional string`

      Generated title for the region

  - `success: optional boolean`

    Whether the job completed successfully

  - `worksheet_metadata: optional array of object { sheet_name, description, title }`

    Metadata for each processed worksheet (populated when job is complete)

    - `sheet_name: string`

      Name of the worksheet

    - `description: optional string`

      Generated description of the worksheet

    - `title: optional string`

      Generated title for the worksheet

### Example

```cli
llamacloud-prod beta:sheets get \
  --api-key 'My API Key' \
  --spreadsheet-job-id spreadsheet_job_id
```

#### Response

```json
{
  "id": "id",
  "config": {
    "extraction_range": "extraction_range",
    "flatten_hierarchical_tables": true,
    "generate_additional_metadata": true,
    "include_hidden_cells": true,
    "sheet_names": [
      "string"
    ],
    "specialization": "specialization",
    "table_merge_sensitivity": "strong",
    "use_experimental_processing": true
  },
  "created_at": "created_at",
  "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "status": "PENDING",
  "updated_at": "updated_at",
  "user_id": "user_id",
  "errors": [
    "string"
  ],
  "file": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "name": "x",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "external_file_id": "external_file_id",
    "file_size": 0,
    "file_type": "x",
    "last_modified_at": "2019-12-27T18:11:19.117Z",
    "permission_info": {
      "foo": {
        "foo": "bar"
      }
    },
    "purpose": "purpose",
    "resource_info": {
      "foo": {
        "foo": "bar"
      }
    },
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "regions": [
    {
      "location": "location",
      "region_type": "region_type",
      "sheet_name": "sheet_name",
      "description": "description",
      "region_id": "region_id",
      "title": "title"
    }
  ],
  "success": true,
  "worksheet_metadata": [
    {
      "sheet_name": "sheet_name",
      "description": "description",
      "title": "title"
    }
  ]
}
```

## Get Result Region

`$ llamacloud-prod beta:sheets get-result-table`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}`

Generate a presigned URL to download a specific extracted region.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--spreadsheet-job-id: string`

  Path param

- `--region-id: string`

  Path param

- `--region-type: "table" or "extra" or "cell_metadata"`

  Path param

- `--expires-at-seconds: optional number`

  Query param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Returns

- `presigned_url: object { expires_at, url, form_fields }`

  Schema for a presigned URL.

  - `expires_at: string`

    The time at which the presigned URL expires

  - `url: string`

    A presigned URL for IO operations against a private file

  - `form_fields: optional map[string]`

    Form fields for a presigned POST request

### Example

```cli
llamacloud-prod beta:sheets get-result-table \
  --api-key 'My API Key' \
  --spreadsheet-job-id spreadsheet_job_id \
  --region-id region_id \
  --region-type table
```

#### Response

```json
{
  "expires_at": "2019-12-27T18:11:19.117Z",
  "url": "https://example.com",
  "form_fields": {
    "foo": "string"
  }
}
```

## Delete Spreadsheet Job

`$ llamacloud-prod beta:sheets delete-job`

**delete** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Delete a spreadsheet parsing job and its associated data.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--spreadsheet-job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaSheetDeleteJobResponse: unknown`

### Example

```cli
llamacloud-prod beta:sheets delete-job \
  --api-key 'My API Key' \
  --spreadsheet-job-id spreadsheet_job_id
```

#### Response

```json
{}
```

## Domain Types

### Sheets Job

- `sheets_job: object { id, config, created_at, 10 more }`

  A spreadsheet parsing job

  - `id: string`

    The ID of the job

  - `config: object { extraction_range, flatten_hierarchical_tables, generate_additional_metadata, 5 more }`

    Configuration for the parsing job

    - `extraction_range: optional string`

      A1 notation of the range to extract a single region from. If None, the entire sheet is used.

    - `flatten_hierarchical_tables: optional boolean`

      Return a flattened dataframe when a detected table is recognized as hierarchical.

    - `generate_additional_metadata: optional boolean`

      Whether to generate additional metadata (title, description) for each extracted region.

    - `include_hidden_cells: optional boolean`

      Whether to include hidden cells when extracting regions from the spreadsheet.

    - `sheet_names: optional array of string`

      The names of the sheets to extract regions from. If empty, all sheets will be processed.

    - `specialization: optional string`

      Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

    - `table_merge_sensitivity: optional "strong" or "weak"`

      Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

      - `"strong"`

      - `"weak"`

    - `use_experimental_processing: optional boolean`

      Enables experimental processing. Accuracy may be impacted.

  - `created_at: string`

    When the job was created

  - `file_id: string`

    The ID of the input file

  - `project_id: string`

    The ID of the project

  - `status: "PENDING" or "SUCCESS" or "ERROR" or 2 more`

    The status of the parsing job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `updated_at: string`

    When the job was last updated

  - `user_id: string`

    The ID of the user

  - `errors: optional array of string`

    Any errors encountered

  - `file: optional object { id, name, project_id, 11 more }`

    Schema for a file.

    - `id: string`

      Unique identifier

    - `name: string`

    - `project_id: string`

      The ID of the project that the file belongs to

    - `created_at: optional string`

      Creation datetime

    - `data_source_id: optional string`

      The ID of the data source that the file belongs to

    - `expires_at: optional string`

      The expiration date for the file. Files past this date can be deleted.

    - `external_file_id: optional string`

      The ID of the file in the external system

    - `file_size: optional number`

      Size of the file in bytes

    - `file_type: optional string`

      File type (e.g. pdf, docx, etc.)

    - `last_modified_at: optional string`

      The last modified time of the file

    - `permission_info: optional map[map[unknown] or array of unknown or string or 2 more]`

      Permission information for the file

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `purpose: optional string`

      The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

    - `resource_info: optional map[map[unknown] or array of unknown or string or 2 more]`

      Resource information for the file

      - `union_member_0: map[unknown]`

      - `union_member_1: array of unknown`

      - `union_member_2: string`

      - `union_member_3: number`

      - `union_member_4: boolean`

    - `updated_at: optional string`

      Update datetime

  - `regions: optional array of object { location, region_type, sheet_name, 3 more }`

    All extracted regions (populated when job is complete)

    - `location: string`

      Location of the region in the spreadsheet

    - `region_type: string`

      Type of the extracted region

    - `sheet_name: string`

      Worksheet name where region was found

    - `description: optional string`

      Generated description for the region

    - `region_id: optional string`

      Unique identifier for this region within the file

    - `title: optional string`

      Generated title for the region

  - `success: optional boolean`

    Whether the job completed successfully

  - `worksheet_metadata: optional array of object { sheet_name, description, title }`

    Metadata for each processed worksheet (populated when job is complete)

    - `sheet_name: string`

      Name of the worksheet

    - `description: optional string`

      Generated description of the worksheet

    - `title: optional string`

      Generated title for the worksheet

### Sheets Parsing Config

- `sheets_parsing_config: object { extraction_range, flatten_hierarchical_tables, generate_additional_metadata, 5 more }`

  Configuration for spreadsheet parsing and region extraction

  - `extraction_range: optional string`

    A1 notation of the range to extract a single region from. If None, the entire sheet is used.

  - `flatten_hierarchical_tables: optional boolean`

    Return a flattened dataframe when a detected table is recognized as hierarchical.

  - `generate_additional_metadata: optional boolean`

    Whether to generate additional metadata (title, description) for each extracted region.

  - `include_hidden_cells: optional boolean`

    Whether to include hidden cells when extracting regions from the spreadsheet.

  - `sheet_names: optional array of string`

    The names of the sheets to extract regions from. If empty, all sheets will be processed.

  - `specialization: optional string`

    Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

  - `table_merge_sensitivity: optional "strong" or "weak"`

    Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

    - `"strong"`

    - `"weak"`

  - `use_experimental_processing: optional boolean`

    Enables experimental processing. Accuracy may be impacted.

# Directories

## Create Directory

`$ llamacloud-prod beta:directories create`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `--name: string`

  Body param: Human-readable name for the directory.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--description: optional string`

  Body param: Optional description shown to users.

### Returns

- `BetaDirectoryNewResponse: object { id, name, project_id, 4 more }`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: optional string`

    Optional description shown to users.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories create \
  --api-key 'My API Key' \
  --name x
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Directories

`$ llamacloud-prod beta:directories list`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `--include-deleted: optional boolean`

- `--name: optional string`

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--type: optional "user" or "index"`

### Returns

- `DirectoryQueryResponse: object { items, next_page_token, total_size }`

  API query response schema for directories.

  - `items: array of object { id, name, project_id, 4 more }`

    The list of items.

    - `id: string`

      Unique identifier for the directory.

    - `name: string`

      Human-readable name for the directory.

    - `project_id: string`

      Project the directory belongs to.

    - `created_at: optional string`

      Creation datetime

    - `deleted_at: optional string`

      Optional timestamp of when the directory was deleted. Null if not deleted.

    - `description: optional string`

      Optional description shown to users.

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:directories list \
  --api-key 'My API Key'
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "name": "x",
      "project_id": "project_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "deleted_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Directory

`$ llamacloud-prod beta:directories get`

**get** `/api/v1/beta/directories/{directory_id}`

Retrieve a directory by its identifier.

### Parameters

- `--directory-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaDirectoryGetResponse: object { id, name, project_id, 4 more }`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: optional string`

    Optional description shown to users.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories get \
  --api-key 'My API Key' \
  --directory-id directory_id
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Directory

`$ llamacloud-prod beta:directories update`

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Parameters

- `--directory-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--description: optional string`

  Body param: Updated description for the directory.

- `--name: optional string`

  Body param: Updated name for the directory.

### Returns

- `BetaDirectoryUpdateResponse: object { id, name, project_id, 4 more }`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: optional string`

    Optional description shown to users.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories update \
  --api-key 'My API Key' \
  --directory-id directory_id
```

#### Response

```json
{
  "id": "id",
  "name": "x",
  "project_id": "project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Directory

`$ llamacloud-prod beta:directories delete`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `--directory-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Example

```cli
llamacloud-prod beta:directories delete \
  --api-key 'My API Key' \
  --directory-id directory_id
```

# Files

## Add Directory File

`$ llamacloud-prod beta:directories:files add`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `--directory-id: string`

  Path param

- `--file-id: string`

  Body param: File ID for the storage location (required).

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--display-name: optional string`

  Body param: Display name for the file. If not provided, will use the file's name.

- `--metadata: optional map[string or number or boolean]`

  Body param: User-defined metadata key-value pairs to associate with the file.

- `--unique-id: optional string`

  Body param: Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `BetaDirectoryFileAddResponse: object { id, directory_id, display_name, 8 more }`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `file_id: optional string`

    File ID for the storage location.

  - `metadata: optional map[string or number or boolean]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files add \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --file-id file_id
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Directory Files

`$ llamacloud-prod beta:directories:files list`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `--directory-id: string`

- `--display-name: optional string`

- `--display-name-contains: optional string`

- `--expand: optional array of string`

  Fields to expand on each directory file.

- `--file-id: optional string`

- `--include-deleted: optional boolean`

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--unique-id: optional string`

- `--updated-at-on-or-after: optional string`

  Include items updated at or after this timestamp (inclusive)

- `--updated-at-on-or-before: optional string`

  Include items updated at or before this timestamp (inclusive)

### Returns

- `DirectoryFileQueryResponse: object { items, next_page_token, total_size }`

  API query response schema for directory files.

  - `items: array of object { id, directory_id, display_name, 8 more }`

    The list of items.

    - `id: string`

      Unique identifier for the directory file.

    - `directory_id: string`

      Directory the file belongs to.

    - `display_name: string`

      Display name for the file.

    - `project_id: string`

      Project the directory file belongs to.

    - `unique_id: string`

      Unique identifier for the file in the directory

    - `created_at: optional string`

      Creation datetime

    - `deleted_at: optional string`

      Soft delete marker when the file is removed upstream or by user action.

    - `download_url: optional object { expires_at, url, form_fields }`

      Schema for a presigned URL.

      - `expires_at: string`

        The time at which the presigned URL expires

      - `url: string`

        A presigned URL for IO operations against a private file

      - `form_fields: optional map[string]`

        Form fields for a presigned POST request

    - `file_id: optional string`

      File ID for the storage location.

    - `metadata: optional map[string or number or boolean]`

      Merged metadata from all sources. Higher-priority sources override lower.

      - `union_member_0: string`

      - `union_member_1: number`

      - `union_member_2: boolean`

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:directories:files list \
  --api-key 'My API Key' \
  --directory-id directory_id
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "directory_id": "directory_id",
      "display_name": "x",
      "project_id": "project_id",
      "unique_id": "x",
      "created_at": "2019-12-27T18:11:19.117Z",
      "deleted_at": "2019-12-27T18:11:19.117Z",
      "download_url": {
        "expires_at": "2019-12-27T18:11:19.117Z",
        "url": "https://example.com",
        "form_fields": {
          "foo": "string"
        }
      },
      "file_id": "file_id",
      "metadata": {
        "foo": "string"
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Directory File

`$ llamacloud-prod beta:directories:files get`

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Parameters

- `--directory-id: string`

  Path param

- `--directory-file-id: string`

  Path param

- `--expand: optional array of string`

  Query param: Fields to expand.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Returns

- `BetaDirectoryFileGetResponse: object { id, directory_id, display_name, 8 more }`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `file_id: optional string`

    File ID for the storage location.

  - `metadata: optional map[string or number or boolean]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files get \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --directory-file-id directory_file_id
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Directory File

`$ llamacloud-prod beta:directories:files update`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `--directory-id: string`

  Path param

- `--directory-file-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--directory-id: string`

  Path param

- `--display-name: optional string`

  Body param: Updated display name.

- `--metadata: optional map[string or number or boolean]`

  Body param: User-defined metadata key-value pairs. Replaces the user metadata layer.

- `--unique-id: optional string`

  Body param: Updated unique identifier.

### Returns

- `BetaDirectoryFileUpdateResponse: object { id, directory_id, display_name, 8 more }`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `file_id: optional string`

    File ID for the storage location.

  - `metadata: optional map[string or number or boolean]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files update \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --directory-file-id directory_file_id
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Directory File

`$ llamacloud-prod beta:directories:files delete`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `--directory-id: string`

  Path param

- `--directory-file-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

### Example

```cli
llamacloud-prod beta:directories:files delete \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --directory-file-id directory_file_id
```

## Upload File To Directory

`$ llamacloud-prod beta:directories:files upload`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `--directory-id: string`

  Path param

- `--upload-file: string`

  Body param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--display-name: optional string`

  Body param

- `--external-file-id: optional string`

  Body param

- `--metadata: optional string`

  Body param: User metadata as a JSON object string.

- `--unique-id: optional string`

  Body param

### Returns

- `BetaDirectoryFileUploadResponse: object { id, directory_id, display_name, 8 more }`

  API response schema for a directory file.

  - `id: string`

    Unique identifier for the directory file.

  - `directory_id: string`

    Directory the file belongs to.

  - `display_name: string`

    Display name for the file.

  - `project_id: string`

    Project the directory file belongs to.

  - `unique_id: string`

    Unique identifier for the file in the directory

  - `created_at: optional string`

    Creation datetime

  - `deleted_at: optional string`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: optional object { expires_at, url, form_fields }`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields: optional map[string]`

      Form fields for a presigned POST request

  - `file_id: optional string`

    File ID for the storage location.

  - `metadata: optional map[string or number or boolean]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `union_member_0: string`

    - `union_member_1: number`

    - `union_member_2: boolean`

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:directories:files upload \
  --api-key 'My API Key' \
  --directory-id directory_id \
  --upload-file 'Example data'
```

#### Response

```json
{
  "id": "id",
  "directory_id": "directory_id",
  "display_name": "x",
  "project_id": "project_id",
  "unique_id": "x",
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "download_url": {
    "expires_at": "2019-12-27T18:11:19.117Z",
    "url": "https://example.com",
    "form_fields": {
      "foo": "string"
    }
  },
  "file_id": "file_id",
  "metadata": {
    "foo": "string"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

# Batch

## Create Batch Job

`$ llamacloud-prod beta:batch create`

**post** `/api/v1/beta/batch-processing`

Create a batch processing job.

Processes files from a directory or a specific list of item IDs.
Supports batch parsing and classification operations.

Provide either `directory_id` to process all files in a directory,
or `item_ids` for specific items. The job runs asynchronously —
poll `GET /batch/{job_id}` for progress.

### Parameters

- `--job-config: object { correlation_id, job_name, parameters, 6 more }  or ClassifyJob`

  Body param: Job configuration — either a parse or classify config

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--continue-as-new-threshold: optional number`

  Body param: Maximum files to process per execution cycle in directory mode. Defaults to page_size.

- `--directory-id: optional string`

  Body param: ID of the directory containing files to process

- `--item-id: optional array of string`

  Body param: List of specific item IDs to process. Either this or directory_id must be provided.

- `--page-size: optional number`

  Body param: Number of files to process per batch when using directory mode

- `--temporal-namespace: optional string`

  Header param

### Returns

- `BetaBatchNewResponse: object { id, job_type, project_id, 14 more }`

  Response schema for a batch processing job.

  - `id: string`

    Unique identifier for the batch job

  - `job_type: "parse" or "extract" or "classify"`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: string`

    Project this job belongs to

  - `status: "pending" or "running" or "dispatched" or 3 more`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: number`

    Total number of items in the job

  - `completed_at: optional string`

    Timestamp when job completed

  - `created_at: optional string`

    Creation datetime

  - `directory_id: optional string`

    Directory being processed

  - `effective_at: optional string`

  - `error_message: optional string`

    Error message for the latest job attempt, if any.

  - `failed_items: optional number`

    Number of items that failed processing

  - `job_record_id: optional string`

    The job record ID associated with this status, if any.

  - `processed_items: optional number`

    Number of items processed so far

  - `skipped_items: optional number`

    Number of items skipped (already processed or size limit)

  - `started_at: optional string`

    Timestamp when job processing started

  - `updated_at: optional string`

    Update datetime

  - `workflow_id: optional string`

    Async job tracking ID

### Example

```cli
llamacloud-prod beta:batch create \
  --api-key 'My API Key' \
  --job-config '{}'
```

#### Response

```json
{
  "id": "bjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "job_type": "parse",
  "project_id": "proj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "status": "pending",
  "total_items": 0,
  "completed_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error_message": "error_message",
  "failed_items": 0,
  "job_record_id": "job_record_id",
  "processed_items": 0,
  "skipped_items": 0,
  "started_at": "2019-12-27T18:11:19.117Z",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "workflow_id": "workflow_id"
}
```

## List Batch Jobs

`$ llamacloud-prod beta:batch list`

**get** `/api/v1/beta/batch-processing`

List batch processing jobs with optional filtering.

Filter by `directory_id`, `job_type`, or `status`. Results
are paginated with configurable `limit` and `offset`.

### Parameters

- `--directory-id: optional string`

  Filter by directory ID

- `--job-type: optional "parse" or "extract" or "classify"`

  Filter by job type (PARSE, EXTRACT, CLASSIFY)

- `--limit: optional number`

  Maximum number of jobs to return

- `--offset: optional number`

  Number of jobs to skip for pagination

- `--organization-id: optional string`

- `--project-id: optional string`

- `--status: optional "pending" or "running" or "dispatched" or 3 more`

  Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

### Returns

- `BatchJobQueryResponse: object { items, next_page_token, total_size }`

  Response schema for paginated batch job queries.

  - `items: array of object { id, job_type, project_id, 14 more }`

    The list of items.

    - `id: string`

      Unique identifier for the batch job

    - `job_type: "parse" or "extract" or "classify"`

      Type of processing operation (parse or classify)

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `project_id: string`

      Project this job belongs to

    - `status: "pending" or "running" or "dispatched" or 3 more`

      Current job status

      - `"pending"`

      - `"running"`

      - `"dispatched"`

      - `"completed"`

      - `"failed"`

      - `"cancelled"`

    - `total_items: number`

      Total number of items in the job

    - `completed_at: optional string`

      Timestamp when job completed

    - `created_at: optional string`

      Creation datetime

    - `directory_id: optional string`

      Directory being processed

    - `effective_at: optional string`

    - `error_message: optional string`

      Error message for the latest job attempt, if any.

    - `failed_items: optional number`

      Number of items that failed processing

    - `job_record_id: optional string`

      The job record ID associated with this status, if any.

    - `processed_items: optional number`

      Number of items processed so far

    - `skipped_items: optional number`

      Number of items skipped (already processed or size limit)

    - `started_at: optional string`

      Timestamp when job processing started

    - `updated_at: optional string`

      Update datetime

    - `workflow_id: optional string`

      Async job tracking ID

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:batch list \
  --api-key 'My API Key'
```

#### Response

```json
{
  "items": [
    {
      "id": "bjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "job_type": "parse",
      "project_id": "proj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "status": "pending",
      "total_items": 0,
      "completed_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "effective_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "failed_items": 0,
      "job_record_id": "job_record_id",
      "processed_items": 0,
      "skipped_items": 0,
      "started_at": "2019-12-27T18:11:19.117Z",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "workflow_id": "workflow_id"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Batch Job Status

`$ llamacloud-prod beta:batch get-status`

**get** `/api/v1/beta/batch-processing/{job_id}`

Get detailed status of a batch processing job.

Returns current progress percentage, file counts (total,
processed, failed, skipped), and timestamps.

### Parameters

- `--job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaBatchGetStatusResponse: object { job, progress_percentage }`

  Detailed status response for a batch processing job.

  - `job: object { id, job_type, project_id, 14 more }`

    Response schema for a batch processing job.

    - `id: string`

      Unique identifier for the batch job

    - `job_type: "parse" or "extract" or "classify"`

      Type of processing operation (parse or classify)

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `project_id: string`

      Project this job belongs to

    - `status: "pending" or "running" or "dispatched" or 3 more`

      Current job status

      - `"pending"`

      - `"running"`

      - `"dispatched"`

      - `"completed"`

      - `"failed"`

      - `"cancelled"`

    - `total_items: number`

      Total number of items in the job

    - `completed_at: optional string`

      Timestamp when job completed

    - `created_at: optional string`

      Creation datetime

    - `directory_id: optional string`

      Directory being processed

    - `effective_at: optional string`

    - `error_message: optional string`

      Error message for the latest job attempt, if any.

    - `failed_items: optional number`

      Number of items that failed processing

    - `job_record_id: optional string`

      The job record ID associated with this status, if any.

    - `processed_items: optional number`

      Number of items processed so far

    - `skipped_items: optional number`

      Number of items skipped (already processed or size limit)

    - `started_at: optional string`

      Timestamp when job processing started

    - `updated_at: optional string`

      Update datetime

    - `workflow_id: optional string`

      Async job tracking ID

  - `progress_percentage: number`

    Percentage of items processed (0-100)

### Example

```cli
llamacloud-prod beta:batch get-status \
  --api-key 'My API Key' \
  --job-id job_id
```

#### Response

```json
{
  "job": {
    "id": "bjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "job_type": "parse",
    "project_id": "proj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "status": "pending",
    "total_items": 0,
    "completed_at": "2019-12-27T18:11:19.117Z",
    "created_at": "2019-12-27T18:11:19.117Z",
    "directory_id": "dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "effective_at": "2019-12-27T18:11:19.117Z",
    "error_message": "error_message",
    "failed_items": 0,
    "job_record_id": "job_record_id",
    "processed_items": 0,
    "skipped_items": 0,
    "started_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "workflow_id": "workflow_id"
  },
  "progress_percentage": 0
}
```

## Cancel Batch Job

`$ llamacloud-prod beta:batch cancel`

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Parameters

- `--job-id: string`

  Path param

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--reason: optional string`

  Body param: Optional reason for cancelling the job

- `--temporal-namespace: optional string`

  Header param

### Returns

- `BetaBatchCancelResponse: object { job_id, message, processed_items, status }`

  Response after cancelling a batch job.

  - `job_id: string`

    ID of the cancelled job

  - `message: string`

    Confirmation message

  - `processed_items: number`

    Number of items processed before cancellation

  - `status: "pending" or "running" or "dispatched" or 3 more`

    New status (should be 'cancelled')

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

### Example

```cli
llamacloud-prod beta:batch cancel \
  --api-key 'My API Key' \
  --job-id job_id
```

#### Response

```json
{
  "job_id": "job_id",
  "message": "message",
  "processed_items": 0,
  "status": "pending"
}
```

# Job Items

## List Batch Job Items

`$ llamacloud-prod beta:batch:job-items list`

**get** `/api/v1/beta/batch-processing/{job_id}/items`

List items in a batch job with optional status filtering.

Useful for finding failed items, viewing completed items,
or debugging processing issues.

### Parameters

- `--job-id: string`

- `--limit: optional number`

  Maximum number of items to return

- `--offset: optional number`

  Number of items to skip

- `--organization-id: optional string`

- `--project-id: optional string`

- `--status: optional "pending" or "processing" or "completed" or 3 more`

  Filter items by status

### Returns

- `BatchItemListResponse: object { items, next_page_token, total_size }`

  Paginated response containing batch job item details.

  - `items: optional array of object { item_id, item_name, status, 7 more }`

    List of item details

    - `item_id: string`

      ID of the item

    - `item_name: string`

      Name of the item

    - `status: "pending" or "processing" or "completed" or 3 more`

      Processing status of this item

      - `"pending"`

      - `"processing"`

      - `"completed"`

      - `"failed"`

      - `"skipped"`

      - `"cancelled"`

    - `completed_at: optional string`

      When processing completed for this item

    - `effective_at: optional string`

    - `error_message: optional string`

      Error message for the latest job attempt, if any.

    - `job_id: optional string`

      Job ID for the underlying processing job (links to parse/extract job results)

    - `job_record_id: optional string`

      The job record ID associated with this status, if any.

    - `skip_reason: optional string`

      Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

    - `started_at: optional string`

      When processing started for this item

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:batch:job-items list \
  --api-key 'My API Key' \
  --job-id job_id
```

#### Response

```json
{
  "items": [
    {
      "item_id": "item_id",
      "item_name": "item_name",
      "status": "pending",
      "completed_at": "2019-12-27T18:11:19.117Z",
      "effective_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "job_id": "job_id",
      "job_record_id": "job_record_id",
      "skip_reason": "skip_reason",
      "started_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Item Processing Results

`$ llamacloud-prod beta:batch:job-items get-processing-results`

**get** `/api/v1/beta/batch-processing/items/{item_id}/processing-results`

Get all processing results for a specific item.

Returns the complete processing history for an item including
what operations were performed, parameters used, and where
outputs are stored. Optionally filter by `job_type`.

### Parameters

- `--item-id: string`

- `--job-type: optional "parse" or "extract" or "classify"`

  Filter results by job type

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaBatchJobItemGetProcessingResultsResponse: object { item_id, item_name, processing_results }`

  Response containing all processing results for an item.

  - `item_id: string`

    ID of the source item

  - `item_name: string`

    Name of the source item

  - `processing_results: optional array of object { item_id, job_config, job_type, 5 more }`

    List of all processing operations performed on this item

    - `item_id: string`

      Source item that was processed

    - `job_config: object { correlation_id, job_name, parameters, 6 more }  or ClassifyJob`

      Job configuration used for processing

      - `BatchParseJobRecordCreate: object { correlation_id, job_name, parameters, 6 more }`

        Batch-specific parse job record for batch processing.

        This model contains the metadata and configuration for a batch parse job,
        but excludes file-specific information. It's used as input to the batch
        parent workflow and combined with DirectoryFile data to create full
        ParseJobRecordCreate instances for each file.

        Attributes:
        job_name: Must be PARSE_RAW_FILE
        partitions: Partitions for job output location
        parameters: Generic parse configuration (BatchParseJobConfig)
        session_id: Upstream request ID for tracking
        correlation_id: Correlation ID for cross-service tracking
        parent_job_execution_id: Parent job execution ID if nested
        user_id: User who created the job
        project_id: Project this job belongs to
        webhook_url: Optional webhook URL for job completion notifications

        - `correlation_id: optional string`

          The correlation ID for this job. Used for tracking the job across services.

        - `job_name: optional "parse_raw_file_job"`

          - `"parse_raw_file_job"`

        - `parameters: optional object { adaptive_long_table, aggressive_table_extraction, annotate_links, 122 more }`

          Generic parse job configuration for batch processing.

          This model contains the parsing configuration that applies to all files
          in a batch, but excludes file-specific fields like file_name, file_id, etc.
          Those file-specific fields are populated from DirectoryFile data when
          creating individual ParseJobRecordCreate instances for each file.

          The fields in this model should be generic settings that apply uniformly
          to all files being processed in the batch.

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

          - `custom_metadata: optional map[unknown]`

            The custom metadata to attach to the documents.

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

            The region for the input S3 bucket.

          - `input_url: optional string`

          - `internal_is_screenshot_job: optional boolean`

          - `invalidate_cache: optional boolean`

          - `is_formatting_instruction: optional boolean`

          - `job_timeout_extra_time_per_page_in_seconds: optional number`

          - `job_timeout_in_seconds: optional number`

          - `keep_page_separator_when_merging_tables: optional boolean`

          - `lang: optional string`

            The language.

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

            If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

          - `output_s3_region: optional string`

            The region for the output S3 bucket.

          - `output_tables_as_HTML: optional boolean`

          - `outputBucket: optional string`

            The output bucket.

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

          - `pipeline_id: optional string`

            The pipeline ID.

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

          - `resource_info: optional map[unknown]`

            The resource info about the file

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

          - `type: optional "parse"`

            - `"parse"`

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

        - `parent_job_execution_id: optional string`

          The ID of the parent job execution.

        - `partitions: optional map[string]`

          The partitions for this execution. Used for determining where to save job output.

        - `project_id: optional string`

          The ID of the project this job belongs to.

        - `session_id: optional string`

          The upstream request ID that created this job. Used for tracking the job across services.

        - `user_id: optional string`

          The ID of the user that created this job

        - `webhook_url: optional string`

          The URL that needs to be called at the end of the parsing job.

      - `classify_job: object { id, project_id, rules, 9 more }`

        A classify job.

        - `id: string`

          Unique identifier

        - `project_id: string`

          The ID of the project

        - `rules: array of ClassifierRule`

          The rules to classify the files

          - `description: string`

            Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

          - `type: string`

            The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

        - `status: "PENDING" or "SUCCESS" or "ERROR" or 2 more`

          The status of the classify job

          - `"PENDING"`

          - `"SUCCESS"`

          - `"ERROR"`

          - `"PARTIAL_SUCCESS"`

          - `"CANCELLED"`

        - `user_id: string`

          The ID of the user

        - `created_at: optional string`

          Creation datetime

        - `effective_at: optional string`

        - `error_message: optional string`

          Error message for the latest job attempt, if any.

        - `job_record_id: optional string`

          The job record ID associated with this status, if any.

        - `mode: optional "FAST" or "MULTIMODAL"`

          The classification mode to use

          - `"FAST"`

          - `"MULTIMODAL"`

        - `parsing_configuration: optional object { lang, max_pages, target_pages }`

          The configuration for the parsing job

          - `lang: optional "af" or "az" or "bs" or 83 more`

            The language to parse the files in

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

          - `max_pages: optional number`

            The maximum number of pages to parse

          - `target_pages: optional array of number`

            The pages to target for parsing (0-indexed, so first page is at 0)

        - `updated_at: optional string`

          Update datetime

    - `job_type: "parse" or "extract" or "classify"`

      Type of processing performed

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `output_s3_path: string`

      Location of the processing output

    - `parameters_hash: string`

      Content hash of the job configuration for dedup

    - `processed_at: string`

      When this processing occurred

    - `result_id: string`

      Unique identifier for this result

    - `output_metadata: optional unknown`

      Metadata about processing output.

      Currently empty - will be populated with job-type-specific metadata fields in the future.

### Example

```cli
llamacloud-prod beta:batch:job-items get-processing-results \
  --api-key 'My API Key' \
  --item-id item_id
```

#### Response

```json
{
  "item_id": "item_id",
  "item_name": "item_name",
  "processing_results": [
    {
      "item_id": "item_id",
      "job_config": {
        "correlation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "job_name": "parse_raw_file_job",
        "parameters": {
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
          "custom_metadata": {
            "foo": "bar"
          },
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
          "lang": "lang",
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
          "outputBucket": "outputBucket",
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
          "pipeline_id": "pipeline_id",
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
          "resource_info": {
            "foo": "bar"
          },
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
          "type": "parse",
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
        "parent_job_execution_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "partitions": {
          "foo": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
        },
        "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "user_id": "user_id",
        "webhook_url": "webhook_url"
      },
      "job_type": "parse",
      "output_s3_path": "output_s3_path",
      "parameters_hash": "parameters_hash",
      "processed_at": "2019-12-27T18:11:19.117Z",
      "result_id": "result_id",
      "output_metadata": {}
    }
  ]
}
```

# Split

## Create Split Job

`$ llamacloud-prod beta:split create`

**post** `/api/v1/beta/split/jobs`

Create a document split job.

### Parameters

- `--document-input: object { type, value }`

  Body param: Document to be split.

- `--organization-id: optional string`

  Query param

- `--project-id: optional string`

  Query param

- `--configuration: optional object { categories, splitting_strategy }`

  Body param: Split configuration with categories and splitting strategy.

- `--configuration-id: optional string`

  Body param: Saved split configuration ID.

### Returns

- `BetaSplitNewResponse: object { id, categories, document_input, 8 more }`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: array of SplitCategory`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description: optional string`

      Optional description of what content belongs in this category.

  - `document_input: object { type, value }`

    Document that was split.

    - `type: string`

      Type of document input. Valid values are: file_id

    - `value: string`

      Document identifier.

  - `project_id: string`

    Project ID this job belongs to.

  - `status: string`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: string`

    User ID who created this job.

  - `configuration_id: optional string`

    Split configuration ID used for this job.

  - `created_at: optional string`

    Creation datetime

  - `error_message: optional string`

    Error message if the job failed.

  - `result: optional object { segments }`

    Result of a completed split job.

    - `segments: array of SplitSegmentResponse`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: array of number`

        1-indexed page numbers in this split.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:split create \
  --api-key 'My API Key' \
  --document-input '{type: type, value: value}'
```

#### Response

```json
{
  "id": "id",
  "categories": [
    {
      "name": "x",
      "description": "x"
    }
  ],
  "document_input": {
    "type": "type",
    "value": "value"
  },
  "project_id": "project_id",
  "status": "status",
  "user_id": "user_id",
  "configuration_id": "configuration_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "error_message": "error_message",
  "result": {
    "segments": [
      {
        "category": "category",
        "confidence_category": "confidence_category",
        "pages": [
          0
        ]
      }
    ]
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Split Jobs

`$ llamacloud-prod beta:split list`

**get** `/api/v1/beta/split/jobs`

List document split jobs.

### Parameters

- `--created-at-on-or-after: optional string`

  Include items created at or after this timestamp (inclusive)

- `--created-at-on-or-before: optional string`

  Include items created at or before this timestamp (inclusive)

- `--job-id: optional array of string`

  Filter by specific job IDs

- `--organization-id: optional string`

- `--page-size: optional number`

- `--page-token: optional string`

- `--project-id: optional string`

- `--status: optional "pending" or "processing" or "completed" or 2 more`

  Filter by job status (pending, processing, completed, failed, cancelled)

### Returns

- `SplitJobQueryResponse: object { items, next_page_token, total_size }`

  Beta paginated list of split jobs.

  - `items: array of object { id, categories, document_input, 8 more }`

    The list of items.

    - `id: string`

      Unique identifier for the split job.

    - `categories: array of SplitCategory`

      Categories used for splitting.

      - `name: string`

        Name of the category.

      - `description: optional string`

        Optional description of what content belongs in this category.

    - `document_input: object { type, value }`

      Document that was split.

      - `type: string`

        Type of document input. Valid values are: file_id

      - `value: string`

        Document identifier.

    - `project_id: string`

      Project ID this job belongs to.

    - `status: string`

      Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

    - `user_id: string`

      User ID who created this job.

    - `configuration_id: optional string`

      Split configuration ID used for this job.

    - `created_at: optional string`

      Creation datetime

    - `error_message: optional string`

      Error message if the job failed.

    - `result: optional object { segments }`

      Result of a completed split job.

      - `segments: array of SplitSegmentResponse`

        List of document segments.

        - `category: string`

          Category name this split belongs to.

        - `confidence_category: string`

          Categorical confidence level. Valid values are: high, medium, low.

        - `pages: array of number`

          1-indexed page numbers in this split.

    - `updated_at: optional string`

      Update datetime

  - `next_page_token: optional string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: optional number`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```cli
llamacloud-prod beta:split list \
  --api-key 'My API Key'
```

#### Response

```json
{
  "items": [
    {
      "id": "id",
      "categories": [
        {
          "name": "x",
          "description": "x"
        }
      ],
      "document_input": {
        "type": "type",
        "value": "value"
      },
      "project_id": "project_id",
      "status": "status",
      "user_id": "user_id",
      "configuration_id": "configuration_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "result": {
        "segments": [
          {
            "category": "category",
            "confidence_category": "confidence_category",
            "pages": [
              0
            ]
          }
        ]
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Get Split Job

`$ llamacloud-prod beta:split get`

**get** `/api/v1/beta/split/jobs/{split_job_id}`

Get a document split job.

### Parameters

- `--split-job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `BetaSplitGetResponse: object { id, categories, document_input, 8 more }`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: array of SplitCategory`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description: optional string`

      Optional description of what content belongs in this category.

  - `document_input: object { type, value }`

    Document that was split.

    - `type: string`

      Type of document input. Valid values are: file_id

    - `value: string`

      Document identifier.

  - `project_id: string`

    Project ID this job belongs to.

  - `status: string`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: string`

    User ID who created this job.

  - `configuration_id: optional string`

    Split configuration ID used for this job.

  - `created_at: optional string`

    Creation datetime

  - `error_message: optional string`

    Error message if the job failed.

  - `result: optional object { segments }`

    Result of a completed split job.

    - `segments: array of SplitSegmentResponse`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: array of number`

        1-indexed page numbers in this split.

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod beta:split get \
  --api-key 'My API Key' \
  --split-job-id split_job_id
```

#### Response

```json
{
  "id": "id",
  "categories": [
    {
      "name": "x",
      "description": "x"
    }
  ],
  "document_input": {
    "type": "type",
    "value": "value"
  },
  "project_id": "project_id",
  "status": "status",
  "user_id": "user_id",
  "configuration_id": "configuration_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "error_message": "error_message",
  "result": {
    "segments": [
      {
        "category": "category",
        "confidence_category": "confidence_category",
        "pages": [
          0
        ]
      }
    ]
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Domain Types

### Split Category

- `split_category: object { name, description }`

  Category definition for document splitting.

  - `name: string`

    Name of the category.

  - `description: optional string`

    Optional description of what content belongs in this category.

### Split Document Input

- `split_document_input: object { type, value }`

  Document input specification for beta API.

  - `type: string`

    Type of document input. Valid values are: file_id

  - `value: string`

    Document identifier.

### Split Result Response

- `split_result_response: object { segments }`

  Result of a completed split job.

  - `segments: array of SplitSegmentResponse`

    List of document segments.

    - `category: string`

      Category name this split belongs to.

    - `confidence_category: string`

      Categorical confidence level. Valid values are: high, medium, low.

    - `pages: array of number`

      1-indexed page numbers in this split.

### Split Segment Response

- `split_segment_response: object { category, confidence_category, pages }`

  A segment of the split document.

  - `category: string`

    Category name this split belongs to.

  - `confidence_category: string`

    Categorical confidence level. Valid values are: high, medium, low.

  - `pages: array of number`

    1-indexed page numbers in this split.
