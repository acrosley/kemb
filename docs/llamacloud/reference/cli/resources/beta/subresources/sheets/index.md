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
