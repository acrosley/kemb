## Create Spreadsheet Job

`client.beta.sheets.create(SheetCreateParamsparams, RequestOptionsoptions?): SheetsJob`

**post** `/api/v1/beta/sheets/jobs`

Create a spreadsheet parsing job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `params: SheetCreateParams`

  - `file_id: string`

    Body param: The ID of the file to parse

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `config?: SheetsParsingConfig`

    Body param: Configuration for the parsing job

    - `extraction_range?: string | null`

      A1 notation of the range to extract a single region from. If None, the entire sheet is used.

    - `flatten_hierarchical_tables?: boolean`

      Return a flattened dataframe when a detected table is recognized as hierarchical.

    - `generate_additional_metadata?: boolean`

      Whether to generate additional metadata (title, description) for each extracted region.

    - `include_hidden_cells?: boolean`

      Whether to include hidden cells when extracting regions from the spreadsheet.

    - `sheet_names?: Array<string> | null`

      The names of the sheets to extract regions from. If empty, all sheets will be processed.

    - `specialization?: string | null`

      Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

    - `table_merge_sensitivity?: "strong" | "weak"`

      Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

      - `"strong"`

      - `"weak"`

    - `use_experimental_processing?: boolean`

      Enables experimental processing. Accuracy may be impacted.

### Returns

- `SheetsJob`

  A spreadsheet parsing job

  - `id: string`

    The ID of the job

  - `config: SheetsParsingConfig`

    Configuration for the parsing job

    - `extraction_range?: string | null`

      A1 notation of the range to extract a single region from. If None, the entire sheet is used.

    - `flatten_hierarchical_tables?: boolean`

      Return a flattened dataframe when a detected table is recognized as hierarchical.

    - `generate_additional_metadata?: boolean`

      Whether to generate additional metadata (title, description) for each extracted region.

    - `include_hidden_cells?: boolean`

      Whether to include hidden cells when extracting regions from the spreadsheet.

    - `sheet_names?: Array<string> | null`

      The names of the sheets to extract regions from. If empty, all sheets will be processed.

    - `specialization?: string | null`

      Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

    - `table_merge_sensitivity?: "strong" | "weak"`

      Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

      - `"strong"`

      - `"weak"`

    - `use_experimental_processing?: boolean`

      Enables experimental processing. Accuracy may be impacted.

  - `created_at: string`

    When the job was created

  - `file_id: string | null`

    The ID of the input file

  - `project_id: string`

    The ID of the project

  - `status: StatusEnum`

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

  - `errors?: Array<string>`

    Any errors encountered

  - `file?: File | null`

    Schema for a file.

    - `id: string`

      Unique identifier

    - `name: string`

    - `project_id: string`

      The ID of the project that the file belongs to

    - `created_at?: string | null`

      Creation datetime

    - `data_source_id?: string | null`

      The ID of the data source that the file belongs to

    - `expires_at?: string | null`

      The expiration date for the file. Files past this date can be deleted.

    - `external_file_id?: string | null`

      The ID of the file in the external system

    - `file_size?: number | null`

      Size of the file in bytes

    - `file_type?: string | null`

      File type (e.g. pdf, docx, etc.)

    - `last_modified_at?: string | null`

      The last modified time of the file

    - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      Permission information for the file

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `purpose?: string | null`

      The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

    - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      Resource information for the file

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `updated_at?: string | null`

      Update datetime

  - `regions?: Array<Region>`

    All extracted regions (populated when job is complete)

    - `location: string`

      Location of the region in the spreadsheet

    - `region_type: string`

      Type of the extracted region

    - `sheet_name: string`

      Worksheet name where region was found

    - `description?: string | null`

      Generated description for the region

    - `region_id?: string`

      Unique identifier for this region within the file

    - `title?: string | null`

      Generated title for the region

  - `success?: boolean | null`

    Whether the job completed successfully

  - `worksheet_metadata?: Array<WorksheetMetadata>`

    Metadata for each processed worksheet (populated when job is complete)

    - `sheet_name: string`

      Name of the worksheet

    - `description?: string | null`

      Generated description of the worksheet

    - `title?: string | null`

      Generated title for the worksheet

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const sheetsJob = await client.beta.sheets.create({
  file_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(sheetsJob.id);
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
