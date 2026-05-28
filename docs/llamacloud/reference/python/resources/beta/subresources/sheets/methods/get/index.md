## Get Spreadsheet Job

`beta.sheets.get(strspreadsheet_job_id, SheetGetParams**kwargs)  -> SheetsJob`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Get a spreadsheet parsing job.

When include_results=True (default), the response will include extracted regions and results
if the job is complete, eliminating the need for a separate /results call.

Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheet_job_id: str`

- `include_results: Optional[bool]`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class SheetsJob: …`

  A spreadsheet parsing job

  - `id: str`

    The ID of the job

  - `config: SheetsParsingConfig`

    Configuration for the parsing job

    - `extraction_range: Optional[str]`

      A1 notation of the range to extract a single region from. If None, the entire sheet is used.

    - `flatten_hierarchical_tables: Optional[bool]`

      Return a flattened dataframe when a detected table is recognized as hierarchical.

    - `generate_additional_metadata: Optional[bool]`

      Whether to generate additional metadata (title, description) for each extracted region.

    - `include_hidden_cells: Optional[bool]`

      Whether to include hidden cells when extracting regions from the spreadsheet.

    - `sheet_names: Optional[List[str]]`

      The names of the sheets to extract regions from. If empty, all sheets will be processed.

    - `specialization: Optional[str]`

      Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

    - `table_merge_sensitivity: Optional[Literal["strong", "weak"]]`

      Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

      - `"strong"`

      - `"weak"`

    - `use_experimental_processing: Optional[bool]`

      Enables experimental processing. Accuracy may be impacted.

  - `created_at: str`

    When the job was created

  - `file_id: Optional[str]`

    The ID of the input file

  - `project_id: str`

    The ID of the project

  - `status: StatusEnum`

    The status of the parsing job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `updated_at: str`

    When the job was last updated

  - `user_id: str`

    The ID of the user

  - `errors: Optional[List[str]]`

    Any errors encountered

  - `file: Optional[File]`

    Schema for a file.

    - `id: str`

      Unique identifier

    - `name: str`

    - `project_id: str`

      The ID of the project that the file belongs to

    - `created_at: Optional[datetime]`

      Creation datetime

    - `data_source_id: Optional[str]`

      The ID of the data source that the file belongs to

    - `expires_at: Optional[datetime]`

      The expiration date for the file. Files past this date can be deleted.

    - `external_file_id: Optional[str]`

      The ID of the file in the external system

    - `file_size: Optional[int]`

      Size of the file in bytes

    - `file_type: Optional[str]`

      File type (e.g. pdf, docx, etc.)

    - `last_modified_at: Optional[datetime]`

      The last modified time of the file

    - `permission_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

      Permission information for the file

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `purpose: Optional[str]`

      The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

    - `resource_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, 3 more]]]`

      Resource information for the file

      - `Dict[str, object]`

      - `List[object]`

      - `str`

      - `float`

      - `bool`

    - `updated_at: Optional[datetime]`

      Update datetime

  - `regions: Optional[List[Region]]`

    All extracted regions (populated when job is complete)

    - `location: str`

      Location of the region in the spreadsheet

    - `region_type: str`

      Type of the extracted region

    - `sheet_name: str`

      Worksheet name where region was found

    - `description: Optional[str]`

      Generated description for the region

    - `region_id: Optional[str]`

      Unique identifier for this region within the file

    - `title: Optional[str]`

      Generated title for the region

  - `success: Optional[bool]`

    Whether the job completed successfully

  - `worksheet_metadata: Optional[List[WorksheetMetadata]]`

    Metadata for each processed worksheet (populated when job is complete)

    - `sheet_name: str`

      Name of the worksheet

    - `description: Optional[str]`

      Generated description of the worksheet

    - `title: Optional[str]`

      Generated title for the worksheet

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
sheets_job = client.beta.sheets.get(
    spreadsheet_job_id="spreadsheet_job_id",
)
print(sheets_job.id)
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
