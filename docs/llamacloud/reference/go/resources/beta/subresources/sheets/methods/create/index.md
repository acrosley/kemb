## Create Spreadsheet Job

`client.Beta.Sheets.New(ctx, params) (*SheetsJob, error)`

**post** `/api/v1/beta/sheets/jobs`

Create a spreadsheet parsing job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `params BetaSheetNewParams`

  - `FileID param.Field[string]`

    Body param: The ID of the file to parse

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Config param.Field[SheetsParsingConfig]`

    Body param: Configuration for the parsing job

### Returns

- `type SheetsJob struct{…}`

  A spreadsheet parsing job

  - `ID string`

    The ID of the job

  - `Config SheetsParsingConfig`

    Configuration for the parsing job

    - `ExtractionRange string`

      A1 notation of the range to extract a single region from. If None, the entire sheet is used.

    - `FlattenHierarchicalTables bool`

      Return a flattened dataframe when a detected table is recognized as hierarchical.

    - `GenerateAdditionalMetadata bool`

      Whether to generate additional metadata (title, description) for each extracted region.

    - `IncludeHiddenCells bool`

      Whether to include hidden cells when extracting regions from the spreadsheet.

    - `SheetNames []string`

      The names of the sheets to extract regions from. If empty, all sheets will be processed.

    - `Specialization string`

      Optional specialization mode for domain-specific extraction. Supported values: 'financial-standard', 'financial-enhanced', 'financial-precise'. Default None uses the general-purpose pipeline.

    - `TableMergeSensitivity SheetsParsingConfigTableMergeSensitivity`

      Influences how likely similar-looking regions are merged into a single table. Useful for spreadsheets that either have sparse tables (strong merging) or many distinct tables close together (weak merging).

      - `const SheetsParsingConfigTableMergeSensitivityStrong SheetsParsingConfigTableMergeSensitivity = "strong"`

      - `const SheetsParsingConfigTableMergeSensitivityWeak SheetsParsingConfigTableMergeSensitivity = "weak"`

    - `UseExperimentalProcessing bool`

      Enables experimental processing. Accuracy may be impacted.

  - `CreatedAt string`

    When the job was created

  - `FileID string`

    The ID of the input file

  - `ProjectID string`

    The ID of the project

  - `Status StatusEnum`

    The status of the parsing job

    - `const StatusEnumPending StatusEnum = "PENDING"`

    - `const StatusEnumSuccess StatusEnum = "SUCCESS"`

    - `const StatusEnumError StatusEnum = "ERROR"`

    - `const StatusEnumPartialSuccess StatusEnum = "PARTIAL_SUCCESS"`

    - `const StatusEnumCancelled StatusEnum = "CANCELLED"`

  - `UpdatedAt string`

    When the job was last updated

  - `UserID string`

    The ID of the user

  - `Errors []string`

    Any errors encountered

  - `File File`

    Schema for a file.

    - `ID string`

      Unique identifier

    - `Name string`

    - `ProjectID string`

      The ID of the project that the file belongs to

    - `CreatedAt Time`

      Creation datetime

    - `DataSourceID string`

      The ID of the data source that the file belongs to

    - `ExpiresAt Time`

      The expiration date for the file. Files past this date can be deleted.

    - `ExternalFileID string`

      The ID of the file in the external system

    - `FileSize int64`

      Size of the file in bytes

    - `FileType string`

      File type (e.g. pdf, docx, etc.)

    - `LastModifiedAt Time`

      The last modified time of the file

    - `PermissionInfo map[string, FilePermissionInfoUnion]`

      Permission information for the file

      - `type FilePermissionInfoMap map[string, any]`

      - `type FilePermissionInfoArray []any`

      - `string`

      - `float64`

      - `bool`

    - `Purpose string`

      The intended purpose of the file (e.g., 'user_data', 'parse', 'extract', 'split', 'classify')

    - `ResourceInfo map[string, FileResourceInfoUnion]`

      Resource information for the file

      - `type FileResourceInfoMap map[string, any]`

      - `type FileResourceInfoArray []any`

      - `string`

      - `float64`

      - `bool`

    - `UpdatedAt Time`

      Update datetime

  - `Regions []SheetsJobRegion`

    All extracted regions (populated when job is complete)

    - `Location string`

      Location of the region in the spreadsheet

    - `RegionType string`

      Type of the extracted region

    - `SheetName string`

      Worksheet name where region was found

    - `Description string`

      Generated description for the region

    - `RegionID string`

      Unique identifier for this region within the file

    - `Title string`

      Generated title for the region

  - `Success bool`

    Whether the job completed successfully

  - `WorksheetMetadata []SheetsJobWorksheetMetadata`

    Metadata for each processed worksheet (populated when job is complete)

    - `SheetName string`

      Name of the worksheet

    - `Description string`

      Generated description of the worksheet

    - `Title string`

      Generated title for the worksheet

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
  sheetsJob, err := client.Beta.Sheets.New(context.TODO(), llamacloudprod.BetaSheetNewParams{
    FileID: "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", sheetsJob.ID)
}
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
