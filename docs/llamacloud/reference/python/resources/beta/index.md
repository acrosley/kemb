# Beta

# Agent Data

## Get Agent Data

`beta.agent_data.get(stritem_id, AgentDataGetParams**kwargs)  -> AgentData`

**get** `/api/v1/beta/agent-data/{item_id}`

Get agent data by ID.

### Parameters

- `item_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class AgentData: …`

  API Result for a single agent data item

  - `data: Dict[str, object]`

  - `deployment_name: str`

  - `id: Optional[str]`

  - `collection: Optional[str]`

  - `created_at: Optional[datetime]`

  - `project_id: Optional[str]`

  - `updated_at: Optional[datetime]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
agent_data = client.beta.agent_data.get(
    item_id="item_id",
)
print(agent_data.id)
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

`beta.agent_data.update(stritem_id, AgentDataUpdateParams**kwargs)  -> AgentData`

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Parameters

- `item_id: str`

- `data: Dict[str, object]`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class AgentData: …`

  API Result for a single agent data item

  - `data: Dict[str, object]`

  - `deployment_name: str`

  - `id: Optional[str]`

  - `collection: Optional[str]`

  - `created_at: Optional[datetime]`

  - `project_id: Optional[str]`

  - `updated_at: Optional[datetime]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
agent_data = client.beta.agent_data.update(
    item_id="item_id",
    data={
        "foo": "bar"
    },
)
print(agent_data.id)
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

`beta.agent_data.delete(stritem_id, AgentDataDeleteParams**kwargs)  -> AgentDataDeleteResponse`

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Parameters

- `item_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `Dict[str, str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
agent_data = client.beta.agent_data.delete(
    item_id="item_id",
)
print(agent_data)
```

#### Response

```json
{
  "foo": "string"
}
```

## Create Agent Data

`beta.agent_data.create(AgentDataCreateParams**kwargs)  -> AgentData`

**post** `/api/v1/beta/agent-data`

Create new agent data.

### Parameters

- `data: Dict[str, object]`

- `deployment_name: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `collection: Optional[str]`

### Returns

- `class AgentData: …`

  API Result for a single agent data item

  - `data: Dict[str, object]`

  - `deployment_name: str`

  - `id: Optional[str]`

  - `collection: Optional[str]`

  - `created_at: Optional[datetime]`

  - `project_id: Optional[str]`

  - `updated_at: Optional[datetime]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
agent_data = client.beta.agent_data.create(
    data={
        "foo": "bar"
    },
    deployment_name="deployment_name",
)
print(agent_data.id)
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

`beta.agent_data.search(AgentDataSearchParams**kwargs)  -> SyncPaginatedCursorPost[AgentData]`

**post** `/api/v1/beta/agent-data/:search`

Search agent data with filtering, sorting, and pagination.

### Parameters

- `deployment_name: str`

  The agent deployment's name to search within

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `collection: Optional[str]`

  The logical agent data collection to search within

- `filter: Optional[Dict[str, Filter]]`

  A filter object or expression that filters resources listed in the response.

  - `eq: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `excludes: Optional[SequenceNotStr[Union[float, str, Union[str, datetime], null]]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `gt: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `gte: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `includes: Optional[SequenceNotStr[Union[float, str, Union[str, datetime], null]]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `lt: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `lte: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `ne: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

- `include_total: Optional[bool]`

  Whether to include the total number of items in the response

- `offset: Optional[int]`

  The offset to start from. If not provided, the first page is returned

- `order_by: Optional[str]`

  A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `page_size: Optional[int]`

  The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `page_token: Optional[str]`

  A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `class AgentData: …`

  API Result for a single agent data item

  - `data: Dict[str, object]`

  - `deployment_name: str`

  - `id: Optional[str]`

  - `collection: Optional[str]`

  - `created_at: Optional[datetime]`

  - `project_id: Optional[str]`

  - `updated_at: Optional[datetime]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agent_data.search(
    deployment_name="deployment_name",
)
page = page.items[0]
print(page.id)
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

`beta.agent_data.aggregate(AgentDataAggregateParams**kwargs)  -> SyncPaginatedCursorPost[AgentDataAggregateResponse]`

**post** `/api/v1/beta/agent-data/:aggregate`

Aggregate agent data with grouping and optional counting/first item retrieval.

### Parameters

- `deployment_name: str`

  The agent deployment's name to aggregate data for

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `collection: Optional[str]`

  The logical agent data collection to aggregate data for

- `count: Optional[bool]`

  Whether to count the number of items in each group

- `filter: Optional[Dict[str, Filter]]`

  A filter object or expression that filters resources listed in the response.

  - `eq: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `excludes: Optional[SequenceNotStr[Union[float, str, Union[str, datetime], null]]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `gt: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `gte: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `includes: Optional[SequenceNotStr[Union[float, str, Union[str, datetime], null]]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `lt: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `lte: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `ne: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

- `first: Optional[bool]`

  Whether to return the first item in each group (Sorted by created_at)

- `group_by: Optional[SequenceNotStr[str]]`

  The fields to group by. If empty, the entire dataset is grouped on. e.g. if left out, can be used for simple count operations

- `offset: Optional[int]`

  The offset to start from. If not provided, the first page is returned

- `order_by: Optional[str]`

  A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

- `page_size: Optional[int]`

  The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

- `page_token: Optional[str]`

  A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `class AgentDataAggregateResponse: …`

  API Result for a single group in the aggregate response

  - `group_key: Dict[str, object]`

  - `count: Optional[int]`

  - `first_item: Optional[Dict[str, object]]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agent_data.aggregate(
    deployment_name="deployment_name",
)
page = page.items[0]
print(page.group_key)
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

`beta.agent_data.delete_by_query(AgentDataDeleteByQueryParams**kwargs)  -> AgentDataDeleteByQueryResponse`

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Parameters

- `deployment_name: str`

  The agent deployment's name to delete data for

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `collection: Optional[str]`

  The logical agent data collection to delete from

- `filter: Optional[Dict[str, Filter]]`

  Optional filters to select which items to delete

  - `eq: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `excludes: Optional[SequenceNotStr[Union[float, str, Union[str, datetime], null]]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `gt: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `gte: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `includes: Optional[SequenceNotStr[Union[float, str, Union[str, datetime], null]]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `lt: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `lte: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

  - `ne: Optional[Union[float, str, Union[str, datetime], null]]`

    - `float`

    - `str`

    - `Union[str, datetime]`

### Returns

- `class AgentDataDeleteByQueryResponse: …`

  API response for bulk delete operation

  - `deleted_count: int`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.agent_data.delete_by_query(
    deployment_name="deployment_name",
)
print(response.deleted_count)
```

#### Response

```json
{
  "deleted_count": 0
}
```

## Domain Types

### Agent Data

- `class AgentData: …`

  API Result for a single agent data item

  - `data: Dict[str, object]`

  - `deployment_name: str`

  - `id: Optional[str]`

  - `collection: Optional[str]`

  - `created_at: Optional[datetime]`

  - `project_id: Optional[str]`

  - `updated_at: Optional[datetime]`

### Agent Data Delete Response

- `Dict[str, str]`

### Agent Data Aggregate Response

- `class AgentDataAggregateResponse: …`

  API Result for a single group in the aggregate response

  - `group_key: Dict[str, object]`

  - `count: Optional[int]`

  - `first_item: Optional[Dict[str, object]]`

### Agent Data Delete By Query Response

- `class AgentDataDeleteByQueryResponse: …`

  API response for bulk delete operation

  - `deleted_count: int`

# Sheets

## Create Spreadsheet Job

`beta.sheets.create(SheetCreateParams**kwargs)  -> SheetsJob`

**post** `/api/v1/beta/sheets/jobs`

Create a spreadsheet parsing job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `file_id: str`

  The ID of the file to parse

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `config: Optional[SheetsParsingConfigParam]`

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
sheets_job = client.beta.sheets.create(
    file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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

## List Spreadsheet Jobs

`beta.sheets.list(SheetListParams**kwargs)  -> SyncPaginatedCursor[SheetsJob]`

**get** `/api/v1/beta/sheets/jobs`

List spreadsheet parsing jobs.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `created_at_on_or_after: Optional[Union[str, datetime, null]]`

  Include items created at or after this timestamp (inclusive)

- `created_at_on_or_before: Optional[Union[str, datetime, null]]`

  Include items created at or before this timestamp (inclusive)

- `include_results: Optional[bool]`

- `job_ids: Optional[SequenceNotStr[str]]`

  Filter by specific job IDs

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

- `page_token: Optional[str]`

- `project_id: Optional[str]`

- `status: Optional[StatusEnum]`

  Filter by job status

  - `"PENDING"`

  - `"SUCCESS"`

  - `"ERROR"`

  - `"PARTIAL_SUCCESS"`

  - `"CANCELLED"`

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
page = client.beta.sheets.list()
page = page.items[0]
print(page.id)
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

## Get Result Region

`beta.sheets.get_result_table(Literal["table", "extra", "cell_metadata"]region_type, SheetGetResultTableParams**kwargs)  -> PresignedURL`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}`

Generate a presigned URL to download a specific extracted region.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheet_job_id: str`

- `region_id: str`

- `region_type: Literal["table", "extra", "cell_metadata"]`

  - `"table"`

  - `"extra"`

  - `"cell_metadata"`

- `expires_at_seconds: Optional[int]`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class PresignedURL: …`

  Schema for a presigned URL.

  - `expires_at: datetime`

    The time at which the presigned URL expires

  - `url: str`

    A presigned URL for IO operations against a private file

  - `form_fields: Optional[Dict[str, str]]`

    Form fields for a presigned POST request

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
presigned_url = client.beta.sheets.get_result_table(
    region_type="table",
    spreadsheet_job_id="spreadsheet_job_id",
    region_id="region_id",
)
print(presigned_url.expires_at)
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

`beta.sheets.delete_job(strspreadsheet_job_id, SheetDeleteJobParams**kwargs)  -> object`

**delete** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Delete a spreadsheet parsing job and its associated data.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheet_job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `object`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.sheets.delete_job(
    spreadsheet_job_id="spreadsheet_job_id",
)
print(response)
```

#### Response

```json
{}
```

## Domain Types

### Sheets Job

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

### Sheets Parsing Config

- `class SheetsParsingConfig: …`

  Configuration for spreadsheet parsing and region extraction

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

# Directories

## Create Directory

`beta.directories.create(DirectoryCreateParams**kwargs)  -> DirectoryCreateResponse`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `name: str`

  Human-readable name for the directory.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `description: Optional[str]`

  Optional description shown to users.

### Returns

- `class DirectoryCreateResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
directory = client.beta.directories.create(
    name="x",
)
print(directory.id)
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

`beta.directories.list(DirectoryListParams**kwargs)  -> SyncPaginatedCursor[DirectoryListResponse]`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `include_deleted: Optional[bool]`

- `name: Optional[str]`

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

- `page_token: Optional[str]`

- `project_id: Optional[str]`

- `type: Optional[Literal["user", "index"]]`

  - `"user"`

  - `"index"`

### Returns

- `class DirectoryListResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.directories.list()
page = page.items[0]
print(page.id)
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

`beta.directories.get(strdirectory_id, DirectoryGetParams**kwargs)  -> DirectoryGetResponse`

**get** `/api/v1/beta/directories/{directory_id}`

Retrieve a directory by its identifier.

### Parameters

- `directory_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class DirectoryGetResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
directory = client.beta.directories.get(
    directory_id="directory_id",
)
print(directory.id)
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

`beta.directories.update(strdirectory_id, DirectoryUpdateParams**kwargs)  -> DirectoryUpdateResponse`

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Parameters

- `directory_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `description: Optional[str]`

  Updated description for the directory.

- `name: Optional[str]`

  Updated name for the directory.

### Returns

- `class DirectoryUpdateResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
directory = client.beta.directories.update(
    directory_id="directory_id",
)
print(directory.id)
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

`beta.directories.delete(strdirectory_id, DirectoryDeleteParams**kwargs)`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `directory_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.beta.directories.delete(
    directory_id="directory_id",
)
```

## Domain Types

### Directory Create Response

- `class DirectoryCreateResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

### Directory List Response

- `class DirectoryListResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

### Directory Get Response

- `class DirectoryGetResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

### Directory Update Response

- `class DirectoryUpdateResponse: …`

  API response schema for a directory.

  - `id: str`

    Unique identifier for the directory.

  - `name: str`

    Human-readable name for the directory.

  - `project_id: str`

    Project the directory belongs to.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description: Optional[str]`

    Optional description shown to users.

  - `updated_at: Optional[datetime]`

    Update datetime

# Files

## Add Directory File

`beta.directories.files.add(strdirectory_id, FileAddParams**kwargs)  -> FileAddResponse`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `directory_id: str`

- `file_id: str`

  File ID for the storage location (required).

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `display_name: Optional[str]`

  Display name for the file. If not provided, will use the file's name.

- `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

  User-defined metadata key-value pairs to associate with the file.

  - `str`

  - `float`

  - `bool`

- `unique_id: Optional[str]`

  Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `class FileAddResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.directories.files.add(
    directory_id="directory_id",
    file_id="file_id",
)
print(response.id)
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

`beta.directories.files.list(strdirectory_id, FileListParams**kwargs)  -> SyncPaginatedCursor[FileListResponse]`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `directory_id: str`

- `display_name: Optional[str]`

- `display_name_contains: Optional[str]`

- `expand: Optional[SequenceNotStr[str]]`

  Fields to expand on each directory file.

- `file_id: Optional[str]`

- `include_deleted: Optional[bool]`

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

- `page_token: Optional[str]`

- `project_id: Optional[str]`

- `unique_id: Optional[str]`

- `updated_at_on_or_after: Optional[Union[str, datetime, null]]`

  Include items updated at or after this timestamp (inclusive)

- `updated_at_on_or_before: Optional[Union[str, datetime, null]]`

  Include items updated at or before this timestamp (inclusive)

### Returns

- `class FileListResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.directories.files.list(
    directory_id="directory_id",
)
page = page.items[0]
print(page.id)
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

`beta.directories.files.get(strdirectory_file_id, FileGetParams**kwargs)  -> FileGetResponse`

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Parameters

- `directory_id: str`

- `directory_file_id: str`

- `expand: Optional[SequenceNotStr[str]]`

  Fields to expand.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class FileGetResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
file = client.beta.directories.files.get(
    directory_file_id="directory_file_id",
    directory_id="directory_id",
)
print(file.id)
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

`beta.directories.files.update(strdirectory_file_id, FileUpdateParams**kwargs)  -> FileUpdateResponse`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directory_id: str`

- `directory_file_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `directory_id: str`

- `display_name: Optional[str]`

  Updated display name.

- `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

  User-defined metadata key-value pairs. Replaces the user metadata layer.

  - `str`

  - `float`

  - `bool`

- `unique_id: Optional[str]`

  Updated unique identifier.

### Returns

- `class FileUpdateResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
file = client.beta.directories.files.update(
    directory_file_id="directory_file_id",
    path_directory_id="directory_id",
)
print(file.id)
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

`beta.directories.files.delete(strdirectory_file_id, FileDeleteParams**kwargs)`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directory_id: str`

- `directory_file_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
client.beta.directories.files.delete(
    directory_file_id="directory_file_id",
    directory_id="directory_id",
)
```

## Upload File To Directory

`beta.directories.files.upload(strdirectory_id, FileUploadParams**kwargs)  -> FileUploadResponse`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `directory_id: str`

- `upload_file: FileTypes`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `display_name: Optional[str]`

- `external_file_id: Optional[str]`

- `metadata: Optional[str]`

  User metadata as a JSON object string.

- `unique_id: Optional[str]`

### Returns

- `class FileUploadResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.directories.files.upload(
    directory_id="directory_id",
    upload_file=b"Example data",
)
print(response.id)
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

## Domain Types

### File Add Response

- `class FileAddResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### File List Response

- `class FileListResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### File Get Response

- `class FileGetResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### File Update Response

- `class FileUpdateResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

### File Upload Response

- `class FileUploadResponse: …`

  API response schema for a directory file.

  - `id: str`

    Unique identifier for the directory file.

  - `directory_id: str`

    Directory the file belongs to.

  - `display_name: str`

    Display name for the file.

  - `project_id: str`

    Project the directory file belongs to.

  - `unique_id: str`

    Unique identifier for the file in the directory

  - `created_at: Optional[datetime]`

    Creation datetime

  - `deleted_at: Optional[datetime]`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url: Optional[PresignedURL]`

    Schema for a presigned URL.

    - `expires_at: datetime`

      The time at which the presigned URL expires

    - `url: str`

      A presigned URL for IO operations against a private file

    - `form_fields: Optional[Dict[str, str]]`

      Form fields for a presigned POST request

  - `file_id: Optional[str]`

    File ID for the storage location.

  - `metadata: Optional[Dict[str, Union[str, float, bool, null]]]`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `str`

    - `float`

    - `bool`

  - `updated_at: Optional[datetime]`

    Update datetime

# Batch

## Create Batch Job

`beta.batch.create(BatchCreateParams**kwargs)  -> BatchCreateResponse`

**post** `/api/v1/beta/batch-processing`

Create a batch processing job.

Processes files from a directory or a specific list of item IDs.
Supports batch parsing and classification operations.

Provide either `directory_id` to process all files in a directory,
or `item_ids` for specific items. The job runs asynchronously —
poll `GET /batch/{job_id}` for progress.

### Parameters

- `job_config: JobConfig`

  Job configuration — either a parse or classify config

  - `class JobConfigBatchParseJobRecordCreate: …`

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

    - `correlation_id: Optional[str]`

      The correlation ID for this job. Used for tracking the job across services.

    - `job_name: Optional[Literal["parse_raw_file_job"]]`

      - `"parse_raw_file_job"`

    - `parameters: Optional[JobConfigBatchParseJobRecordCreateParameters]`

      Generic parse job configuration for batch processing.

      This model contains the parsing configuration that applies to all files
      in a batch, but excludes file-specific fields like file_name, file_id, etc.
      Those file-specific fields are populated from DirectoryFile data when
      creating individual ParseJobRecordCreate instances for each file.

      The fields in this model should be generic settings that apply uniformly
      to all files being processed in the batch.

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

      - `custom_metadata: Optional[Dict[str, object]]`

        The custom metadata to attach to the documents.

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

        The region for the input S3 bucket.

      - `input_url: Optional[str]`

      - `internal_is_screenshot_job: Optional[bool]`

      - `invalidate_cache: Optional[bool]`

      - `is_formatting_instruction: Optional[bool]`

      - `job_timeout_extra_time_per_page_in_seconds: Optional[float]`

      - `job_timeout_in_seconds: Optional[float]`

      - `keep_page_separator_when_merging_tables: Optional[bool]`

      - `lang: Optional[str]`

        The language.

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

        If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

      - `output_s3_region: Optional[str]`

        The region for the output S3 bucket.

      - `output_tables_as_html: Optional[bool]`

      - `output_bucket: Optional[str]`

        The output bucket.

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

      - `pipeline_id: Optional[str]`

        The pipeline ID.

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

      - `resource_info: Optional[Dict[str, object]]`

        The resource info about the file

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

      - `type: Optional[Literal["parse"]]`

        - `"parse"`

      - `use_vendor_multimodal_model: Optional[bool]`

      - `user_prompt: Optional[str]`

      - `vendor_multimodal_api_key: Optional[str]`

      - `vendor_multimodal_model_name: Optional[str]`

      - `version: Optional[str]`

      - `webhook_configurations: Optional[Iterable[JobConfigBatchParseJobRecordCreateParametersWebhookConfiguration]]`

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

    - `parent_job_execution_id: Optional[str]`

      The ID of the parent job execution.

    - `partitions: Optional[Dict[str, str]]`

      The partitions for this execution. Used for determining where to save job output.

    - `project_id: Optional[str]`

      The ID of the project this job belongs to.

    - `session_id: Optional[str]`

      The upstream request ID that created this job. Used for tracking the job across services.

    - `user_id: Optional[str]`

      The ID of the user that created this job

    - `webhook_url: Optional[str]`

      The URL that needs to be called at the end of the parsing job.

  - `class ClassifyJob: …`

    A classify job.

    - `id: str`

      Unique identifier

    - `project_id: str`

      The ID of the project

    - `rules: List[ClassifierRule]`

      The rules to classify the files

      - `description: str`

        Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

      - `type: str`

        The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

    - `status: StatusEnum`

      The status of the classify job

      - `"PENDING"`

      - `"SUCCESS"`

      - `"ERROR"`

      - `"PARTIAL_SUCCESS"`

      - `"CANCELLED"`

    - `user_id: str`

      The ID of the user

    - `created_at: Optional[datetime]`

      Creation datetime

    - `effective_at: Optional[datetime]`

    - `error_message: Optional[str]`

      Error message for the latest job attempt, if any.

    - `job_record_id: Optional[str]`

      The job record ID associated with this status, if any.

    - `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

      The classification mode to use

      - `"FAST"`

      - `"MULTIMODAL"`

    - `parsing_configuration: Optional[ClassifyParsingConfiguration]`

      The configuration for the parsing job

      - `lang: Optional[ParsingLanguages]`

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

      - `max_pages: Optional[int]`

        The maximum number of pages to parse

      - `target_pages: Optional[List[int]]`

        The pages to target for parsing (0-indexed, so first page is at 0)

    - `updated_at: Optional[datetime]`

      Update datetime

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `continue_as_new_threshold: Optional[int]`

  Maximum files to process per execution cycle in directory mode. Defaults to page_size.

- `directory_id: Optional[str]`

  ID of the directory containing files to process

- `item_ids: Optional[SequenceNotStr[str]]`

  List of specific item IDs to process. Either this or directory_id must be provided.

- `page_size: Optional[int]`

  Number of files to process per batch when using directory mode

- `temporal_namespace: Optional[str]`

### Returns

- `class BatchCreateResponse: …`

  Response schema for a batch processing job.

  - `id: str`

    Unique identifier for the batch job

  - `job_type: Literal["parse", "extract", "classify"]`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: int`

    Total number of items in the job

  - `completed_at: Optional[datetime]`

    Timestamp when job completed

  - `created_at: Optional[datetime]`

    Creation datetime

  - `directory_id: Optional[str]`

    Directory being processed

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `failed_items: Optional[int]`

    Number of items that failed processing

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `processed_items: Optional[int]`

    Number of items processed so far

  - `skipped_items: Optional[int]`

    Number of items skipped (already processed or size limit)

  - `started_at: Optional[datetime]`

    Timestamp when job processing started

  - `updated_at: Optional[datetime]`

    Update datetime

  - `workflow_id: Optional[str]`

    Async job tracking ID

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
batch = client.beta.batch.create(
    job_config={},
)
print(batch.id)
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

`beta.batch.list(BatchListParams**kwargs)  -> SyncPaginatedBatchItems[BatchListResponse]`

**get** `/api/v1/beta/batch-processing`

List batch processing jobs with optional filtering.

Filter by `directory_id`, `job_type`, or `status`. Results
are paginated with configurable `limit` and `offset`.

### Parameters

- `directory_id: Optional[str]`

  Filter by directory ID

- `job_type: Optional[Literal["parse", "extract", "classify"]]`

  Filter by job type (PARSE, EXTRACT, CLASSIFY)

  - `"parse"`

  - `"extract"`

  - `"classify"`

- `limit: Optional[int]`

  Maximum number of jobs to return

- `offset: Optional[int]`

  Number of jobs to skip for pagination

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `status: Optional[Literal["pending", "running", "dispatched", 3 more]]`

  Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

  - `"pending"`

  - `"running"`

  - `"dispatched"`

  - `"completed"`

  - `"failed"`

  - `"cancelled"`

### Returns

- `class BatchListResponse: …`

  Response schema for a batch processing job.

  - `id: str`

    Unique identifier for the batch job

  - `job_type: Literal["parse", "extract", "classify"]`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: int`

    Total number of items in the job

  - `completed_at: Optional[datetime]`

    Timestamp when job completed

  - `created_at: Optional[datetime]`

    Creation datetime

  - `directory_id: Optional[str]`

    Directory being processed

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `failed_items: Optional[int]`

    Number of items that failed processing

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `processed_items: Optional[int]`

    Number of items processed so far

  - `skipped_items: Optional[int]`

    Number of items skipped (already processed or size limit)

  - `started_at: Optional[datetime]`

    Timestamp when job processing started

  - `updated_at: Optional[datetime]`

    Update datetime

  - `workflow_id: Optional[str]`

    Async job tracking ID

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.batch.list()
page = page.items[0]
print(page.id)
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

`beta.batch.get_status(strjob_id, BatchGetStatusParams**kwargs)  -> BatchGetStatusResponse`

**get** `/api/v1/beta/batch-processing/{job_id}`

Get detailed status of a batch processing job.

Returns current progress percentage, file counts (total,
processed, failed, skipped), and timestamps.

### Parameters

- `job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class BatchGetStatusResponse: …`

  Detailed status response for a batch processing job.

  - `job: Job`

    Response schema for a batch processing job.

    - `id: str`

      Unique identifier for the batch job

    - `job_type: Literal["parse", "extract", "classify"]`

      Type of processing operation (parse or classify)

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `project_id: str`

      Project this job belongs to

    - `status: Literal["pending", "running", "dispatched", 3 more]`

      Current job status

      - `"pending"`

      - `"running"`

      - `"dispatched"`

      - `"completed"`

      - `"failed"`

      - `"cancelled"`

    - `total_items: int`

      Total number of items in the job

    - `completed_at: Optional[datetime]`

      Timestamp when job completed

    - `created_at: Optional[datetime]`

      Creation datetime

    - `directory_id: Optional[str]`

      Directory being processed

    - `effective_at: Optional[datetime]`

    - `error_message: Optional[str]`

      Error message for the latest job attempt, if any.

    - `failed_items: Optional[int]`

      Number of items that failed processing

    - `job_record_id: Optional[str]`

      The job record ID associated with this status, if any.

    - `processed_items: Optional[int]`

      Number of items processed so far

    - `skipped_items: Optional[int]`

      Number of items skipped (already processed or size limit)

    - `started_at: Optional[datetime]`

      Timestamp when job processing started

    - `updated_at: Optional[datetime]`

      Update datetime

    - `workflow_id: Optional[str]`

      Async job tracking ID

  - `progress_percentage: float`

    Percentage of items processed (0-100)

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.batch.get_status(
    job_id="job_id",
)
print(response.job)
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

`beta.batch.cancel(strjob_id, BatchCancelParams**kwargs)  -> BatchCancelResponse`

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Parameters

- `job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `reason: Optional[str]`

  Optional reason for cancelling the job

- `temporal_namespace: Optional[str]`

### Returns

- `class BatchCancelResponse: …`

  Response after cancelling a batch job.

  - `job_id: str`

    ID of the cancelled job

  - `message: str`

    Confirmation message

  - `processed_items: int`

    Number of items processed before cancellation

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    New status (should be 'cancelled')

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.batch.cancel(
    job_id="job_id",
)
print(response.job_id)
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

## Domain Types

### Batch Create Response

- `class BatchCreateResponse: …`

  Response schema for a batch processing job.

  - `id: str`

    Unique identifier for the batch job

  - `job_type: Literal["parse", "extract", "classify"]`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: int`

    Total number of items in the job

  - `completed_at: Optional[datetime]`

    Timestamp when job completed

  - `created_at: Optional[datetime]`

    Creation datetime

  - `directory_id: Optional[str]`

    Directory being processed

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `failed_items: Optional[int]`

    Number of items that failed processing

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `processed_items: Optional[int]`

    Number of items processed so far

  - `skipped_items: Optional[int]`

    Number of items skipped (already processed or size limit)

  - `started_at: Optional[datetime]`

    Timestamp when job processing started

  - `updated_at: Optional[datetime]`

    Update datetime

  - `workflow_id: Optional[str]`

    Async job tracking ID

### Batch List Response

- `class BatchListResponse: …`

  Response schema for a batch processing job.

  - `id: str`

    Unique identifier for the batch job

  - `job_type: Literal["parse", "extract", "classify"]`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: str`

    Project this job belongs to

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: int`

    Total number of items in the job

  - `completed_at: Optional[datetime]`

    Timestamp when job completed

  - `created_at: Optional[datetime]`

    Creation datetime

  - `directory_id: Optional[str]`

    Directory being processed

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `failed_items: Optional[int]`

    Number of items that failed processing

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `processed_items: Optional[int]`

    Number of items processed so far

  - `skipped_items: Optional[int]`

    Number of items skipped (already processed or size limit)

  - `started_at: Optional[datetime]`

    Timestamp when job processing started

  - `updated_at: Optional[datetime]`

    Update datetime

  - `workflow_id: Optional[str]`

    Async job tracking ID

### Batch Get Status Response

- `class BatchGetStatusResponse: …`

  Detailed status response for a batch processing job.

  - `job: Job`

    Response schema for a batch processing job.

    - `id: str`

      Unique identifier for the batch job

    - `job_type: Literal["parse", "extract", "classify"]`

      Type of processing operation (parse or classify)

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `project_id: str`

      Project this job belongs to

    - `status: Literal["pending", "running", "dispatched", 3 more]`

      Current job status

      - `"pending"`

      - `"running"`

      - `"dispatched"`

      - `"completed"`

      - `"failed"`

      - `"cancelled"`

    - `total_items: int`

      Total number of items in the job

    - `completed_at: Optional[datetime]`

      Timestamp when job completed

    - `created_at: Optional[datetime]`

      Creation datetime

    - `directory_id: Optional[str]`

      Directory being processed

    - `effective_at: Optional[datetime]`

    - `error_message: Optional[str]`

      Error message for the latest job attempt, if any.

    - `failed_items: Optional[int]`

      Number of items that failed processing

    - `job_record_id: Optional[str]`

      The job record ID associated with this status, if any.

    - `processed_items: Optional[int]`

      Number of items processed so far

    - `skipped_items: Optional[int]`

      Number of items skipped (already processed or size limit)

    - `started_at: Optional[datetime]`

      Timestamp when job processing started

    - `updated_at: Optional[datetime]`

      Update datetime

    - `workflow_id: Optional[str]`

      Async job tracking ID

  - `progress_percentage: float`

    Percentage of items processed (0-100)

### Batch Cancel Response

- `class BatchCancelResponse: …`

  Response after cancelling a batch job.

  - `job_id: str`

    ID of the cancelled job

  - `message: str`

    Confirmation message

  - `processed_items: int`

    Number of items processed before cancellation

  - `status: Literal["pending", "running", "dispatched", 3 more]`

    New status (should be 'cancelled')

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

# Job Items

## List Batch Job Items

`beta.batch.job_items.list(strjob_id, JobItemListParams**kwargs)  -> SyncPaginatedBatchItems[JobItemListResponse]`

**get** `/api/v1/beta/batch-processing/{job_id}/items`

List items in a batch job with optional status filtering.

Useful for finding failed items, viewing completed items,
or debugging processing issues.

### Parameters

- `job_id: str`

- `limit: Optional[int]`

  Maximum number of items to return

- `offset: Optional[int]`

  Number of items to skip

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `status: Optional[Literal["pending", "processing", "completed", 3 more]]`

  Filter items by status

  - `"pending"`

  - `"processing"`

  - `"completed"`

  - `"failed"`

  - `"skipped"`

  - `"cancelled"`

### Returns

- `class JobItemListResponse: …`

  Detailed information about an item in a batch job.

  - `item_id: str`

    ID of the item

  - `item_name: str`

    Name of the item

  - `status: Literal["pending", "processing", "completed", 3 more]`

    Processing status of this item

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

    - `"cancelled"`

  - `completed_at: Optional[datetime]`

    When processing completed for this item

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `job_id: Optional[str]`

    Job ID for the underlying processing job (links to parse/extract job results)

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `skip_reason: Optional[str]`

    Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

  - `started_at: Optional[datetime]`

    When processing started for this item

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.batch.job_items.list(
    job_id="job_id",
)
page = page.items[0]
print(page.item_id)
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

`beta.batch.job_items.get_processing_results(stritem_id, JobItemGetProcessingResultsParams**kwargs)  -> JobItemGetProcessingResultsResponse`

**get** `/api/v1/beta/batch-processing/items/{item_id}/processing-results`

Get all processing results for a specific item.

Returns the complete processing history for an item including
what operations were performed, parameters used, and where
outputs are stored. Optionally filter by `job_type`.

### Parameters

- `item_id: str`

- `job_type: Optional[Literal["parse", "extract", "classify"]]`

  Filter results by job type

  - `"parse"`

  - `"extract"`

  - `"classify"`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class JobItemGetProcessingResultsResponse: …`

  Response containing all processing results for an item.

  - `item_id: str`

    ID of the source item

  - `item_name: str`

    Name of the source item

  - `processing_results: Optional[List[ProcessingResult]]`

    List of all processing operations performed on this item

    - `item_id: str`

      Source item that was processed

    - `job_config: ProcessingResultJobConfig`

      Job configuration used for processing

      - `class ProcessingResultJobConfigBatchParseJobRecordCreate: …`

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

        - `correlation_id: Optional[str]`

          The correlation ID for this job. Used for tracking the job across services.

        - `job_name: Optional[Literal["parse_raw_file_job"]]`

          - `"parse_raw_file_job"`

        - `parameters: Optional[ProcessingResultJobConfigBatchParseJobRecordCreateParameters]`

          Generic parse job configuration for batch processing.

          This model contains the parsing configuration that applies to all files
          in a batch, but excludes file-specific fields like file_name, file_id, etc.
          Those file-specific fields are populated from DirectoryFile data when
          creating individual ParseJobRecordCreate instances for each file.

          The fields in this model should be generic settings that apply uniformly
          to all files being processed in the batch.

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

          - `custom_metadata: Optional[Dict[str, object]]`

            The custom metadata to attach to the documents.

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

            The region for the input S3 bucket.

          - `input_url: Optional[str]`

          - `internal_is_screenshot_job: Optional[bool]`

          - `invalidate_cache: Optional[bool]`

          - `is_formatting_instruction: Optional[bool]`

          - `job_timeout_extra_time_per_page_in_seconds: Optional[float]`

          - `job_timeout_in_seconds: Optional[float]`

          - `keep_page_separator_when_merging_tables: Optional[bool]`

          - `lang: Optional[str]`

            The language.

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

            If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

          - `output_s3_region: Optional[str]`

            The region for the output S3 bucket.

          - `output_tables_as_html: Optional[bool]`

          - `output_bucket: Optional[str]`

            The output bucket.

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

          - `pipeline_id: Optional[str]`

            The pipeline ID.

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

          - `resource_info: Optional[Dict[str, object]]`

            The resource info about the file

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

          - `type: Optional[Literal["parse"]]`

            - `"parse"`

          - `use_vendor_multimodal_model: Optional[bool]`

          - `user_prompt: Optional[str]`

          - `vendor_multimodal_api_key: Optional[str]`

          - `vendor_multimodal_model_name: Optional[str]`

          - `version: Optional[str]`

          - `webhook_configurations: Optional[List[ProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfiguration]]`

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

        - `parent_job_execution_id: Optional[str]`

          The ID of the parent job execution.

        - `partitions: Optional[Dict[str, str]]`

          The partitions for this execution. Used for determining where to save job output.

        - `project_id: Optional[str]`

          The ID of the project this job belongs to.

        - `session_id: Optional[str]`

          The upstream request ID that created this job. Used for tracking the job across services.

        - `user_id: Optional[str]`

          The ID of the user that created this job

        - `webhook_url: Optional[str]`

          The URL that needs to be called at the end of the parsing job.

      - `class ClassifyJob: …`

        A classify job.

        - `id: str`

          Unique identifier

        - `project_id: str`

          The ID of the project

        - `rules: List[ClassifierRule]`

          The rules to classify the files

          - `description: str`

            Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

          - `type: str`

            The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

        - `status: StatusEnum`

          The status of the classify job

          - `"PENDING"`

          - `"SUCCESS"`

          - `"ERROR"`

          - `"PARTIAL_SUCCESS"`

          - `"CANCELLED"`

        - `user_id: str`

          The ID of the user

        - `created_at: Optional[datetime]`

          Creation datetime

        - `effective_at: Optional[datetime]`

        - `error_message: Optional[str]`

          Error message for the latest job attempt, if any.

        - `job_record_id: Optional[str]`

          The job record ID associated with this status, if any.

        - `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

          The classification mode to use

          - `"FAST"`

          - `"MULTIMODAL"`

        - `parsing_configuration: Optional[ClassifyParsingConfiguration]`

          The configuration for the parsing job

          - `lang: Optional[ParsingLanguages]`

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

          - `max_pages: Optional[int]`

            The maximum number of pages to parse

          - `target_pages: Optional[List[int]]`

            The pages to target for parsing (0-indexed, so first page is at 0)

        - `updated_at: Optional[datetime]`

          Update datetime

    - `job_type: Literal["parse", "extract", "classify"]`

      Type of processing performed

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `output_s3_path: str`

      Location of the processing output

    - `parameters_hash: str`

      Content hash of the job configuration for dedup

    - `processed_at: datetime`

      When this processing occurred

    - `result_id: str`

      Unique identifier for this result

    - `output_metadata: Optional[object]`

      Metadata about processing output.

      Currently empty - will be populated with job-type-specific metadata fields in the future.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.batch.job_items.get_processing_results(
    item_id="item_id",
)
print(response.item_id)
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

## Domain Types

### Job Item List Response

- `class JobItemListResponse: …`

  Detailed information about an item in a batch job.

  - `item_id: str`

    ID of the item

  - `item_name: str`

    Name of the item

  - `status: Literal["pending", "processing", "completed", 3 more]`

    Processing status of this item

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

    - `"cancelled"`

  - `completed_at: Optional[datetime]`

    When processing completed for this item

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `job_id: Optional[str]`

    Job ID for the underlying processing job (links to parse/extract job results)

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `skip_reason: Optional[str]`

    Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

  - `started_at: Optional[datetime]`

    When processing started for this item

### Job Item Get Processing Results Response

- `class JobItemGetProcessingResultsResponse: …`

  Response containing all processing results for an item.

  - `item_id: str`

    ID of the source item

  - `item_name: str`

    Name of the source item

  - `processing_results: Optional[List[ProcessingResult]]`

    List of all processing operations performed on this item

    - `item_id: str`

      Source item that was processed

    - `job_config: ProcessingResultJobConfig`

      Job configuration used for processing

      - `class ProcessingResultJobConfigBatchParseJobRecordCreate: …`

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

        - `correlation_id: Optional[str]`

          The correlation ID for this job. Used for tracking the job across services.

        - `job_name: Optional[Literal["parse_raw_file_job"]]`

          - `"parse_raw_file_job"`

        - `parameters: Optional[ProcessingResultJobConfigBatchParseJobRecordCreateParameters]`

          Generic parse job configuration for batch processing.

          This model contains the parsing configuration that applies to all files
          in a batch, but excludes file-specific fields like file_name, file_id, etc.
          Those file-specific fields are populated from DirectoryFile data when
          creating individual ParseJobRecordCreate instances for each file.

          The fields in this model should be generic settings that apply uniformly
          to all files being processed in the batch.

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

          - `custom_metadata: Optional[Dict[str, object]]`

            The custom metadata to attach to the documents.

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

            The region for the input S3 bucket.

          - `input_url: Optional[str]`

          - `internal_is_screenshot_job: Optional[bool]`

          - `invalidate_cache: Optional[bool]`

          - `is_formatting_instruction: Optional[bool]`

          - `job_timeout_extra_time_per_page_in_seconds: Optional[float]`

          - `job_timeout_in_seconds: Optional[float]`

          - `keep_page_separator_when_merging_tables: Optional[bool]`

          - `lang: Optional[str]`

            The language.

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

            If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

          - `output_s3_region: Optional[str]`

            The region for the output S3 bucket.

          - `output_tables_as_html: Optional[bool]`

          - `output_bucket: Optional[str]`

            The output bucket.

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

          - `pipeline_id: Optional[str]`

            The pipeline ID.

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

          - `resource_info: Optional[Dict[str, object]]`

            The resource info about the file

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

          - `type: Optional[Literal["parse"]]`

            - `"parse"`

          - `use_vendor_multimodal_model: Optional[bool]`

          - `user_prompt: Optional[str]`

          - `vendor_multimodal_api_key: Optional[str]`

          - `vendor_multimodal_model_name: Optional[str]`

          - `version: Optional[str]`

          - `webhook_configurations: Optional[List[ProcessingResultJobConfigBatchParseJobRecordCreateParametersWebhookConfiguration]]`

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

        - `parent_job_execution_id: Optional[str]`

          The ID of the parent job execution.

        - `partitions: Optional[Dict[str, str]]`

          The partitions for this execution. Used for determining where to save job output.

        - `project_id: Optional[str]`

          The ID of the project this job belongs to.

        - `session_id: Optional[str]`

          The upstream request ID that created this job. Used for tracking the job across services.

        - `user_id: Optional[str]`

          The ID of the user that created this job

        - `webhook_url: Optional[str]`

          The URL that needs to be called at the end of the parsing job.

      - `class ClassifyJob: …`

        A classify job.

        - `id: str`

          Unique identifier

        - `project_id: str`

          The ID of the project

        - `rules: List[ClassifierRule]`

          The rules to classify the files

          - `description: str`

            Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

          - `type: str`

            The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

        - `status: StatusEnum`

          The status of the classify job

          - `"PENDING"`

          - `"SUCCESS"`

          - `"ERROR"`

          - `"PARTIAL_SUCCESS"`

          - `"CANCELLED"`

        - `user_id: str`

          The ID of the user

        - `created_at: Optional[datetime]`

          Creation datetime

        - `effective_at: Optional[datetime]`

        - `error_message: Optional[str]`

          Error message for the latest job attempt, if any.

        - `job_record_id: Optional[str]`

          The job record ID associated with this status, if any.

        - `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

          The classification mode to use

          - `"FAST"`

          - `"MULTIMODAL"`

        - `parsing_configuration: Optional[ClassifyParsingConfiguration]`

          The configuration for the parsing job

          - `lang: Optional[ParsingLanguages]`

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

          - `max_pages: Optional[int]`

            The maximum number of pages to parse

          - `target_pages: Optional[List[int]]`

            The pages to target for parsing (0-indexed, so first page is at 0)

        - `updated_at: Optional[datetime]`

          Update datetime

    - `job_type: Literal["parse", "extract", "classify"]`

      Type of processing performed

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `output_s3_path: str`

      Location of the processing output

    - `parameters_hash: str`

      Content hash of the job configuration for dedup

    - `processed_at: datetime`

      When this processing occurred

    - `result_id: str`

      Unique identifier for this result

    - `output_metadata: Optional[object]`

      Metadata about processing output.

      Currently empty - will be populated with job-type-specific metadata fields in the future.

# Split

## Create Split Job

`beta.split.create(SplitCreateParams**kwargs)  -> SplitCreateResponse`

**post** `/api/v1/beta/split/jobs`

Create a document split job.

### Parameters

- `document_input: SplitDocumentInputParam`

  Document to be split.

  - `type: str`

    Type of document input. Valid values are: file_id

  - `value: str`

    Document identifier.

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `configuration: Optional[Configuration]`

  Split configuration with categories and splitting strategy.

  - `categories: Iterable[SplitCategoryParam]`

    Categories to split documents into.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `splitting_strategy: Optional[ConfigurationSplittingStrategy]`

    Strategy for splitting documents.

    - `allow_uncategorized: Optional[Literal["include", "forbid", "omit"]]`

      Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

      - `"include"`

      - `"forbid"`

      - `"omit"`

- `configuration_id: Optional[str]`

  Saved split configuration ID.

### Returns

- `class SplitCreateResponse: …`

  Beta response — uses nested document_input object.

  - `id: str`

    Unique identifier for the split job.

  - `categories: List[SplitCategory]`

    Categories used for splitting.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

    Document that was split.

    - `type: str`

      Type of document input. Valid values are: file_id

    - `value: str`

      Document identifier.

  - `project_id: str`

    Project ID this job belongs to.

  - `status: str`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: str`

    User ID who created this job.

  - `configuration_id: Optional[str]`

    Split configuration ID used for this job.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error message if the job failed.

  - `result: Optional[SplitResultResponse]`

    Result of a completed split job.

    - `segments: List[SplitSegmentResponse]`

      List of document segments.

      - `category: str`

        Category name this split belongs to.

      - `confidence_category: str`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: List[int]`

        1-indexed page numbers in this split.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
split = client.beta.split.create(
    document_input={
        "type": "type",
        "value": "value",
    },
)
print(split.id)
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

`beta.split.list(SplitListParams**kwargs)  -> SyncPaginatedCursor[SplitListResponse]`

**get** `/api/v1/beta/split/jobs`

List document split jobs.

### Parameters

- `created_at_on_or_after: Optional[Union[str, datetime, null]]`

  Include items created at or after this timestamp (inclusive)

- `created_at_on_or_before: Optional[Union[str, datetime, null]]`

  Include items created at or before this timestamp (inclusive)

- `job_ids: Optional[SequenceNotStr[str]]`

  Filter by specific job IDs

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

- `page_token: Optional[str]`

- `project_id: Optional[str]`

- `status: Optional[Literal["pending", "processing", "completed", 2 more]]`

  Filter by job status (pending, processing, completed, failed, cancelled)

  - `"pending"`

  - `"processing"`

  - `"completed"`

  - `"failed"`

  - `"cancelled"`

### Returns

- `class SplitListResponse: …`

  Beta response — uses nested document_input object.

  - `id: str`

    Unique identifier for the split job.

  - `categories: List[SplitCategory]`

    Categories used for splitting.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

    Document that was split.

    - `type: str`

      Type of document input. Valid values are: file_id

    - `value: str`

      Document identifier.

  - `project_id: str`

    Project ID this job belongs to.

  - `status: str`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: str`

    User ID who created this job.

  - `configuration_id: Optional[str]`

    Split configuration ID used for this job.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error message if the job failed.

  - `result: Optional[SplitResultResponse]`

    Result of a completed split job.

    - `segments: List[SplitSegmentResponse]`

      List of document segments.

      - `category: str`

        Category name this split belongs to.

      - `confidence_category: str`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: List[int]`

        1-indexed page numbers in this split.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.split.list()
page = page.items[0]
print(page.id)
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

`beta.split.get(strsplit_job_id, SplitGetParams**kwargs)  -> SplitGetResponse`

**get** `/api/v1/beta/split/jobs/{split_job_id}`

Get a document split job.

### Parameters

- `split_job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class SplitGetResponse: …`

  Beta response — uses nested document_input object.

  - `id: str`

    Unique identifier for the split job.

  - `categories: List[SplitCategory]`

    Categories used for splitting.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

    Document that was split.

    - `type: str`

      Type of document input. Valid values are: file_id

    - `value: str`

      Document identifier.

  - `project_id: str`

    Project ID this job belongs to.

  - `status: str`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: str`

    User ID who created this job.

  - `configuration_id: Optional[str]`

    Split configuration ID used for this job.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error message if the job failed.

  - `result: Optional[SplitResultResponse]`

    Result of a completed split job.

    - `segments: List[SplitSegmentResponse]`

      List of document segments.

      - `category: str`

        Category name this split belongs to.

      - `confidence_category: str`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: List[int]`

        1-indexed page numbers in this split.

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
split = client.beta.split.get(
    split_job_id="split_job_id",
)
print(split.id)
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

- `class SplitCategory: …`

  Category definition for document splitting.

  - `name: str`

    Name of the category.

  - `description: Optional[str]`

    Optional description of what content belongs in this category.

### Split Document Input

- `class SplitDocumentInput: …`

  Document input specification for beta API.

  - `type: str`

    Type of document input. Valid values are: file_id

  - `value: str`

    Document identifier.

### Split Result Response

- `class SplitResultResponse: …`

  Result of a completed split job.

  - `segments: List[SplitSegmentResponse]`

    List of document segments.

    - `category: str`

      Category name this split belongs to.

    - `confidence_category: str`

      Categorical confidence level. Valid values are: high, medium, low.

    - `pages: List[int]`

      1-indexed page numbers in this split.

### Split Segment Response

- `class SplitSegmentResponse: …`

  A segment of the split document.

  - `category: str`

    Category name this split belongs to.

  - `confidence_category: str`

    Categorical confidence level. Valid values are: high, medium, low.

  - `pages: List[int]`

    1-indexed page numbers in this split.

### Split Create Response

- `class SplitCreateResponse: …`

  Beta response — uses nested document_input object.

  - `id: str`

    Unique identifier for the split job.

  - `categories: List[SplitCategory]`

    Categories used for splitting.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

    Document that was split.

    - `type: str`

      Type of document input. Valid values are: file_id

    - `value: str`

      Document identifier.

  - `project_id: str`

    Project ID this job belongs to.

  - `status: str`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: str`

    User ID who created this job.

  - `configuration_id: Optional[str]`

    Split configuration ID used for this job.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error message if the job failed.

  - `result: Optional[SplitResultResponse]`

    Result of a completed split job.

    - `segments: List[SplitSegmentResponse]`

      List of document segments.

      - `category: str`

        Category name this split belongs to.

      - `confidence_category: str`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: List[int]`

        1-indexed page numbers in this split.

  - `updated_at: Optional[datetime]`

    Update datetime

### Split List Response

- `class SplitListResponse: …`

  Beta response — uses nested document_input object.

  - `id: str`

    Unique identifier for the split job.

  - `categories: List[SplitCategory]`

    Categories used for splitting.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

    Document that was split.

    - `type: str`

      Type of document input. Valid values are: file_id

    - `value: str`

      Document identifier.

  - `project_id: str`

    Project ID this job belongs to.

  - `status: str`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: str`

    User ID who created this job.

  - `configuration_id: Optional[str]`

    Split configuration ID used for this job.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error message if the job failed.

  - `result: Optional[SplitResultResponse]`

    Result of a completed split job.

    - `segments: List[SplitSegmentResponse]`

      List of document segments.

      - `category: str`

        Category name this split belongs to.

      - `confidence_category: str`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: List[int]`

        1-indexed page numbers in this split.

  - `updated_at: Optional[datetime]`

    Update datetime

### Split Get Response

- `class SplitGetResponse: …`

  Beta response — uses nested document_input object.

  - `id: str`

    Unique identifier for the split job.

  - `categories: List[SplitCategory]`

    Categories used for splitting.

    - `name: str`

      Name of the category.

    - `description: Optional[str]`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

    Document that was split.

    - `type: str`

      Type of document input. Valid values are: file_id

    - `value: str`

      Document identifier.

  - `project_id: str`

    Project ID this job belongs to.

  - `status: str`

    Current status of the job. Valid values are: pending, processing, completed, failed, cancelled.

  - `user_id: str`

    User ID who created this job.

  - `configuration_id: Optional[str]`

    Split configuration ID used for this job.

  - `created_at: Optional[datetime]`

    Creation datetime

  - `error_message: Optional[str]`

    Error message if the job failed.

  - `result: Optional[SplitResultResponse]`

    Result of a completed split job.

    - `segments: List[SplitSegmentResponse]`

      List of document segments.

      - `category: str`

        Category name this split belongs to.

      - `confidence_category: str`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: List[int]`

        1-indexed page numbers in this split.

  - `updated_at: Optional[datetime]`

    Update datetime
