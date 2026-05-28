# Beta

# Agent Data

## Get Agent Data

`client.beta.agentData.get(stringitemID, AgentDataGetParamsquery?, RequestOptionsoptions?): AgentData`

**get** `/api/v1/beta/agent-data/{item_id}`

Get agent data by ID.

### Parameters

- `itemID: string`

- `query: AgentDataGetParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `AgentData`

  API Result for a single agent data item

  - `data: Record<string, unknown>`

  - `deployment_name: string`

  - `id?: string | null`

  - `collection?: string`

  - `created_at?: string | null`

  - `project_id?: string | null`

  - `updated_at?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const agentData = await client.beta.agentData.get('item_id');

console.log(agentData.id);
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

`client.beta.agentData.update(stringitemID, AgentDataUpdateParamsparams, RequestOptionsoptions?): AgentData`

**put** `/api/v1/beta/agent-data/{item_id}`

Update agent data by ID (overwrites).

### Parameters

- `itemID: string`

- `params: AgentDataUpdateParams`

  - `data: Record<string, unknown>`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `AgentData`

  API Result for a single agent data item

  - `data: Record<string, unknown>`

  - `deployment_name: string`

  - `id?: string | null`

  - `collection?: string`

  - `created_at?: string | null`

  - `project_id?: string | null`

  - `updated_at?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const agentData = await client.beta.agentData.update('item_id', { data: { foo: 'bar' } });

console.log(agentData.id);
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

`client.beta.agentData.delete(stringitemID, AgentDataDeleteParamsparams?, RequestOptionsoptions?): AgentDataDeleteResponse`

**delete** `/api/v1/beta/agent-data/{item_id}`

Delete agent data by ID.

### Parameters

- `itemID: string`

- `params: AgentDataDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `AgentDataDeleteResponse = Record<string, string>`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const agentData = await client.beta.agentData.delete('item_id');

console.log(agentData);
```

#### Response

```json
{
  "foo": "string"
}
```

## Create Agent Data

`client.beta.agentData.create(AgentDataCreateParamsparams, RequestOptionsoptions?): AgentData`

**post** `/api/v1/beta/agent-data`

Create new agent data.

### Parameters

- `params: AgentDataCreateParams`

  - `data: Record<string, unknown>`

    Body param

  - `deployment_name: string`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `collection?: string`

    Body param

### Returns

- `AgentData`

  API Result for a single agent data item

  - `data: Record<string, unknown>`

  - `deployment_name: string`

  - `id?: string | null`

  - `collection?: string`

  - `created_at?: string | null`

  - `project_id?: string | null`

  - `updated_at?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const agentData = await client.beta.agentData.create({
  data: { foo: 'bar' },
  deployment_name: 'deployment_name',
});

console.log(agentData.id);
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

`client.beta.agentData.search(AgentDataSearchParamsparams, RequestOptionsoptions?): PaginatedCursorPost<AgentData>`

**post** `/api/v1/beta/agent-data/:search`

Search agent data with filtering, sorting, and pagination.

### Parameters

- `params: AgentDataSearchParams`

  - `deployment_name: string`

    Body param: The agent deployment's name to search within

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `collection?: string`

    Body param: The logical agent data collection to search within

  - `filter?: Record<string, Filter> | null`

    Body param: A filter object or expression that filters resources listed in the response.

    - `eq?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `excludes?: Array<number | string | (string & {}) | null>`

      - `number`

      - `string`

      - `(string & {})`

    - `gt?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `gte?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `includes?: Array<number | string | (string & {}) | null>`

      - `number`

      - `string`

      - `(string & {})`

    - `lt?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `lte?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `ne?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

  - `include_total?: boolean`

    Body param: Whether to include the total number of items in the response

  - `offset?: number | null`

    Body param: The offset to start from. If not provided, the first page is returned

  - `order_by?: string | null`

    Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `page_size?: number | null`

    Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

  - `page_token?: string | null`

    Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `AgentData`

  API Result for a single agent data item

  - `data: Record<string, unknown>`

  - `deployment_name: string`

  - `id?: string | null`

  - `collection?: string`

  - `created_at?: string | null`

  - `project_id?: string | null`

  - `updated_at?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentData of client.beta.agentData.search({
  deployment_name: 'deployment_name',
})) {
  console.log(agentData.id);
}
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

`client.beta.agentData.aggregate(AgentDataAggregateParamsparams, RequestOptionsoptions?): PaginatedCursorPost<AgentDataAggregateResponse>`

**post** `/api/v1/beta/agent-data/:aggregate`

Aggregate agent data with grouping and optional counting/first item retrieval.

### Parameters

- `params: AgentDataAggregateParams`

  - `deployment_name: string`

    Body param: The agent deployment's name to aggregate data for

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `collection?: string`

    Body param: The logical agent data collection to aggregate data for

  - `count?: boolean | null`

    Body param: Whether to count the number of items in each group

  - `filter?: Record<string, Filter> | null`

    Body param: A filter object or expression that filters resources listed in the response.

    - `eq?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `excludes?: Array<number | string | (string & {}) | null>`

      - `number`

      - `string`

      - `(string & {})`

    - `gt?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `gte?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `includes?: Array<number | string | (string & {}) | null>`

      - `number`

      - `string`

      - `(string & {})`

    - `lt?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `lte?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `ne?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

  - `first?: boolean | null`

    Body param: Whether to return the first item in each group (Sorted by created_at)

  - `group_by?: Array<string> | null`

    Body param: The fields to group by. If empty, the entire dataset is grouped on. e.g. if left out, can be used for simple count operations

  - `offset?: number | null`

    Body param: The offset to start from. If not provided, the first page is returned

  - `order_by?: string | null`

    Body param: A comma-separated list of fields to order by, sorted in ascending order. Use 'field_name desc' to specify descending order.

  - `page_size?: number | null`

    Body param: The maximum number of items to return. The service may return fewer than this value. If unspecified, a default page size will be used. The maximum value is typically 1000; values above this will be coerced to the maximum.

  - `page_token?: string | null`

    Body param: A page token, received from a previous list call. Provide this to retrieve the subsequent page.

### Returns

- `AgentDataAggregateResponse`

  API Result for a single group in the aggregate response

  - `group_key: Record<string, unknown>`

  - `count?: number | null`

  - `first_item?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentDataAggregateResponse of client.beta.agentData.aggregate({
  deployment_name: 'deployment_name',
})) {
  console.log(agentDataAggregateResponse.group_key);
}
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

`client.beta.agentData.deleteByQuery(AgentDataDeleteByQueryParamsparams, RequestOptionsoptions?): AgentDataDeleteByQueryResponse`

**post** `/api/v1/beta/agent-data/:delete`

Bulk delete agent data by query (deployment_name, collection, optional filters).

### Parameters

- `params: AgentDataDeleteByQueryParams`

  - `deployment_name: string`

    Body param: The agent deployment's name to delete data for

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `collection?: string`

    Body param: The logical agent data collection to delete from

  - `filter?: Record<string, Filter> | null`

    Body param: Optional filters to select which items to delete

    - `eq?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `excludes?: Array<number | string | (string & {}) | null>`

      - `number`

      - `string`

      - `(string & {})`

    - `gt?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `gte?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `includes?: Array<number | string | (string & {}) | null>`

      - `number`

      - `string`

      - `(string & {})`

    - `lt?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `lte?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

    - `ne?: number | string | (string & {}) | null`

      - `number`

      - `string`

      - `(string & {})`

### Returns

- `AgentDataDeleteByQueryResponse`

  API response for bulk delete operation

  - `deleted_count: number`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.agentData.deleteByQuery({ deployment_name: 'deployment_name' });

console.log(response.deleted_count);
```

#### Response

```json
{
  "deleted_count": 0
}
```

## Domain Types

### Agent Data

- `AgentData`

  API Result for a single agent data item

  - `data: Record<string, unknown>`

  - `deployment_name: string`

  - `id?: string | null`

  - `collection?: string`

  - `created_at?: string | null`

  - `project_id?: string | null`

  - `updated_at?: string | null`

### Agent Data Delete Response

- `AgentDataDeleteResponse = Record<string, string>`

### Agent Data Aggregate Response

- `AgentDataAggregateResponse`

  API Result for a single group in the aggregate response

  - `group_key: Record<string, unknown>`

  - `count?: number | null`

  - `first_item?: Record<string, unknown> | null`

### Agent Data Delete By Query Response

- `AgentDataDeleteByQueryResponse`

  API response for bulk delete operation

  - `deleted_count: number`

# Sheets

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

## List Spreadsheet Jobs

`client.beta.sheets.list(SheetListParamsquery?, RequestOptionsoptions?): PaginatedCursor<SheetsJob>`

**get** `/api/v1/beta/sheets/jobs`

List spreadsheet parsing jobs.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `query: SheetListParams`

  - `created_at_on_or_after?: string | null`

    Include items created at or after this timestamp (inclusive)

  - `created_at_on_or_before?: string | null`

    Include items created at or before this timestamp (inclusive)

  - `include_results?: boolean`

  - `job_ids?: Array<string> | null`

    Filter by specific job IDs

  - `organization_id?: string | null`

  - `page_size?: number | null`

  - `page_token?: string | null`

  - `project_id?: string | null`

  - `status?: StatusEnum | null`

    Filter by job status

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

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

// Automatically fetches more pages as needed.
for await (const sheetsJob of client.beta.sheets.list()) {
  console.log(sheetsJob.id);
}
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

`client.beta.sheets.get(stringspreadsheetJobID, SheetGetParamsquery?, RequestOptionsoptions?): SheetsJob`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Get a spreadsheet parsing job.

When include_results=True (default), the response will include extracted regions and results
if the job is complete, eliminating the need for a separate /results call.

Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheetJobID: string`

- `query: SheetGetParams`

  - `include_results?: boolean`

  - `organization_id?: string | null`

  - `project_id?: string | null`

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

const sheetsJob = await client.beta.sheets.get('spreadsheet_job_id');

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

## Get Result Region

`client.beta.sheets.getResultTable("table" | "extra" | "cell_metadata"regionType, SheetGetResultTableParamsparams, RequestOptionsoptions?): PresignedURL`

**get** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}`

Generate a presigned URL to download a specific extracted region.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `regionType: "table" | "extra" | "cell_metadata"`

  - `"table"`

  - `"extra"`

  - `"cell_metadata"`

- `params: SheetGetResultTableParams`

  - `spreadsheet_job_id: string`

    Path param

  - `region_id: string`

    Path param

  - `expires_at_seconds?: number | null`

    Query param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `PresignedURL`

  Schema for a presigned URL.

  - `expires_at: string`

    The time at which the presigned URL expires

  - `url: string`

    A presigned URL for IO operations against a private file

  - `form_fields?: Record<string, string> | null`

    Form fields for a presigned POST request

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const presignedURL = await client.beta.sheets.getResultTable('table', {
  spreadsheet_job_id: 'spreadsheet_job_id',
  region_id: 'region_id',
});

console.log(presignedURL.expires_at);
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

`client.beta.sheets.deleteJob(stringspreadsheetJobID, SheetDeleteJobParamsparams?, RequestOptionsoptions?): SheetDeleteJobResponse`

**delete** `/api/v1/beta/sheets/jobs/{spreadsheet_job_id}`

Delete a spreadsheet parsing job and its associated data.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `spreadsheetJobID: string`

- `params: SheetDeleteJobParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `SheetDeleteJobResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.sheets.deleteJob('spreadsheet_job_id');

console.log(response);
```

#### Response

```json
{}
```

## Domain Types

### Sheets Job

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

### Sheets Parsing Config

- `SheetsParsingConfig`

  Configuration for spreadsheet parsing and region extraction

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

### Sheet Delete Job Response

- `SheetDeleteJobResponse = unknown`

# Directories

## Create Directory

`client.beta.directories.create(DirectoryCreateParamsparams, RequestOptionsoptions?): DirectoryCreateResponse`

**post** `/api/v1/beta/directories`

Create a new directory within the specified project.

### Parameters

- `params: DirectoryCreateParams`

  - `name: string`

    Body param: Human-readable name for the directory.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `description?: string | null`

    Body param: Optional description shown to users.

### Returns

- `DirectoryCreateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const directory = await client.beta.directories.create({ name: 'x' });

console.log(directory.id);
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

`client.beta.directories.list(DirectoryListParamsquery?, RequestOptionsoptions?): PaginatedCursor<DirectoryListResponse>`

**get** `/api/v1/beta/directories`

List Directories

### Parameters

- `query: DirectoryListParams`

  - `include_deleted?: boolean`

  - `name?: string | null`

  - `organization_id?: string | null`

  - `page_size?: number | null`

  - `page_token?: string | null`

  - `project_id?: string | null`

  - `type?: "user" | "index" | null`

    - `"user"`

    - `"index"`

### Returns

- `DirectoryListResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const directoryListResponse of client.beta.directories.list()) {
  console.log(directoryListResponse.id);
}
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

`client.beta.directories.get(stringdirectoryID, DirectoryGetParamsquery?, RequestOptionsoptions?): DirectoryGetResponse`

**get** `/api/v1/beta/directories/{directory_id}`

Retrieve a directory by its identifier.

### Parameters

- `directoryID: string`

- `query: DirectoryGetParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `DirectoryGetResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const directory = await client.beta.directories.get('directory_id');

console.log(directory.id);
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

`client.beta.directories.update(stringdirectoryID, DirectoryUpdateParamsparams, RequestOptionsoptions?): DirectoryUpdateResponse`

**patch** `/api/v1/beta/directories/{directory_id}`

Update directory metadata.

### Parameters

- `directoryID: string`

- `params: DirectoryUpdateParams`

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `description?: string | null`

    Body param: Updated description for the directory.

  - `name?: string | null`

    Body param: Updated name for the directory.

### Returns

- `DirectoryUpdateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const directory = await client.beta.directories.update('directory_id');

console.log(directory.id);
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

`client.beta.directories.delete(stringdirectoryID, DirectoryDeleteParamsparams?, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/directories/{directory_id}`

Permanently delete a directory.

### Parameters

- `directoryID: string`

- `params: DirectoryDeleteParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.beta.directories.delete('directory_id');
```

## Domain Types

### Directory Create Response

- `DirectoryCreateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Directory List Response

- `DirectoryListResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Directory Get Response

- `DirectoryGetResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

### Directory Update Response

- `DirectoryUpdateResponse`

  API response schema for a directory.

  - `id: string`

    Unique identifier for the directory.

  - `name: string`

    Human-readable name for the directory.

  - `project_id: string`

    Project the directory belongs to.

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Optional timestamp of when the directory was deleted. Null if not deleted.

  - `description?: string | null`

    Optional description shown to users.

  - `updated_at?: string | null`

    Update datetime

# Files

## Add Directory File

`client.beta.directories.files.add(stringdirectoryID, FileAddParamsparams, RequestOptionsoptions?): FileAddResponse`

**post** `/api/v1/beta/directories/{directory_id}/files`

Create a new file within the specified directory.

The directory must exist and belong to the project passed in.
The file_id must be provided and exist in the project.

### Parameters

- `directoryID: string`

- `params: FileAddParams`

  - `file_id: string`

    Body param: File ID for the storage location (required).

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `display_name?: string | null`

    Body param: Display name for the file. If not provided, will use the file's name.

  - `metadata?: Record<string, string | number | boolean | null> | null`

    Body param: User-defined metadata key-value pairs to associate with the file.

    - `string`

    - `number`

    - `boolean`

  - `unique_id?: string | null`

    Body param: Unique identifier for the file in the directory. If not provided, will use the file's external_file_id or name.

### Returns

- `FileAddResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.directories.files.add('directory_id', { file_id: 'file_id' });

console.log(response.id);
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

`client.beta.directories.files.list(stringdirectoryID, FileListParamsquery?, RequestOptionsoptions?): PaginatedCursor<FileListResponse>`

**get** `/api/v1/beta/directories/{directory_id}/files`

List all files within the specified directory with optional filtering and pagination.

### Parameters

- `directoryID: string`

- `query: FileListParams`

  - `display_name?: string | null`

  - `display_name_contains?: string | null`

  - `expand?: Array<string> | null`

    Fields to expand on each directory file.

  - `file_id?: string | null`

  - `include_deleted?: boolean`

  - `organization_id?: string | null`

  - `page_size?: number | null`

  - `page_token?: string | null`

  - `project_id?: string | null`

  - `unique_id?: string | null`

  - `updated_at_on_or_after?: string | null`

    Include items updated at or after this timestamp (inclusive)

  - `updated_at_on_or_before?: string | null`

    Include items updated at or before this timestamp (inclusive)

### Returns

- `FileListResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const fileListResponse of client.beta.directories.files.list('directory_id')) {
  console.log(fileListResponse.id);
}
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

`client.beta.directories.files.get(stringdirectoryFileID, FileGetParamsparams, RequestOptionsoptions?): FileGetResponse`

**get** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Get a file by its directory_file_id within the specified directory. If you're trying to get a file by its unique_id, use the list endpoint with a filter instead.

### Parameters

- `directoryFileID: string`

- `params: FileGetParams`

  - `directory_id: string`

    Path param

  - `expand?: Array<string> | null`

    Query param: Fields to expand.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `FileGetResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const file = await client.beta.directories.files.get('directory_file_id', {
  directory_id: 'directory_id',
});

console.log(file.id);
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

`client.beta.directories.files.update(stringdirectoryFileID, FileUpdateParamsparams, RequestOptionsoptions?): FileUpdateResponse`

**patch** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Update file metadata within the specified directory.

Supports moving files to a different directory by setting directory_id.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to update a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID: string`

- `params: FileUpdateParams`

  - `body_directory_id?: string | null`

    Body param: Move file to a different directory.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `display_name?: string | null`

    Body param: Updated display name.

  - `metadata?: Record<string, string | number | boolean | null> | null`

    Body param: User-defined metadata key-value pairs. Replaces the user metadata layer.

    - `string`

    - `number`

    - `boolean`

  - `unique_id?: string | null`

    Body param: Updated unique identifier.

### Returns

- `FileUpdateResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const file = await client.beta.directories.files.update('directory_file_id', {
  path_directory_id: 'directory_id',
});

console.log(file.id);
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

`client.beta.directories.files.delete(stringdirectoryFileID, FileDeleteParamsparams, RequestOptionsoptions?): void`

**delete** `/api/v1/beta/directories/{directory_id}/files/{directory_file_id}`

Delete a file from the specified directory.

Note: This endpoint uses directory_file_id (the internal ID). If you're trying to delete a file by its unique_id, use the list endpoint with a filter to find the directory_file_id first.

### Parameters

- `directoryFileID: string`

- `params: FileDeleteParams`

  - `directory_id: string`

    Path param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.beta.directories.files.delete('directory_file_id', { directory_id: 'directory_id' });
```

## Upload File To Directory

`client.beta.directories.files.upload(stringdirectoryID, FileUploadParamsparams, RequestOptionsoptions?): FileUploadResponse`

**post** `/api/v1/beta/directories/{directory_id}/files/upload`

Upload a file directly to a directory.

Uploads a file and creates a directory file entry in a single operation.
If unique_id or display_name are not provided, they will be derived from the file metadata.

### Parameters

- `directoryID: string`

- `params: FileUploadParams`

  - `upload_file: Uploadable`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `display_name?: string | null`

    Body param

  - `external_file_id?: string | null`

    Body param

  - `metadata?: string | null`

    Body param: User metadata as a JSON object string.

  - `unique_id?: string | null`

    Body param

### Returns

- `FileUploadResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.directories.files.upload('directory_id', {
  upload_file: fs.createReadStream('path/to/file'),
});

console.log(response.id);
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

- `FileAddResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### File List Response

- `FileListResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### File Get Response

- `FileGetResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### File Update Response

- `FileUpdateResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

### File Upload Response

- `FileUploadResponse`

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

  - `created_at?: string | null`

    Creation datetime

  - `deleted_at?: string | null`

    Soft delete marker when the file is removed upstream or by user action.

  - `download_url?: PresignedURL | null`

    Schema for a presigned URL.

    - `expires_at: string`

      The time at which the presigned URL expires

    - `url: string`

      A presigned URL for IO operations against a private file

    - `form_fields?: Record<string, string> | null`

      Form fields for a presigned POST request

  - `file_id?: string | null`

    File ID for the storage location.

  - `metadata?: Record<string, string | number | boolean | null>`

    Merged metadata from all sources. Higher-priority sources override lower.

    - `string`

    - `number`

    - `boolean`

  - `updated_at?: string | null`

    Update datetime

# Batch

## Create Batch Job

`client.beta.batch.create(BatchCreateParamsparams, RequestOptionsoptions?): BatchCreateResponse`

**post** `/api/v1/beta/batch-processing`

Create a batch processing job.

Processes files from a directory or a specific list of item IDs.
Supports batch parsing and classification operations.

Provide either `directory_id` to process all files in a directory,
or `item_ids` for specific items. The job runs asynchronously —
poll `GET /batch/{job_id}` for progress.

### Parameters

- `params: BatchCreateParams`

  - `job_config: BatchParseJobRecordCreate | ClassifyJob`

    Body param: Job configuration — either a parse or classify config

    - `BatchParseJobRecordCreate`

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

      - `correlation_id?: string | null`

        The correlation ID for this job. Used for tracking the job across services.

      - `job_name?: "parse_raw_file_job"`

        - `"parse_raw_file_job"`

      - `parameters?: Parameters | null`

        Generic parse job configuration for batch processing.

        This model contains the parsing configuration that applies to all files
        in a batch, but excludes file-specific fields like file_name, file_id, etc.
        Those file-specific fields are populated from DirectoryFile data when
        creating individual ParseJobRecordCreate instances for each file.

        The fields in this model should be generic settings that apply uniformly
        to all files being processed in the batch.

        - `adaptive_long_table?: boolean | null`

        - `aggressive_table_extraction?: boolean | null`

        - `annotate_links?: boolean | null`

        - `auto_mode?: boolean | null`

        - `auto_mode_configuration_json?: string | null`

        - `auto_mode_trigger_on_image_in_page?: boolean | null`

        - `auto_mode_trigger_on_regexp_in_page?: string | null`

        - `auto_mode_trigger_on_table_in_page?: boolean | null`

        - `auto_mode_trigger_on_text_in_page?: string | null`

        - `azure_openai_api_version?: string | null`

        - `azure_openai_deployment_name?: string | null`

        - `azure_openai_endpoint?: string | null`

        - `azure_openai_key?: string | null`

        - `bbox_bottom?: number | null`

        - `bbox_left?: number | null`

        - `bbox_right?: number | null`

        - `bbox_top?: number | null`

        - `bounding_box?: string | null`

        - `compact_markdown_table?: boolean | null`

        - `complemental_formatting_instruction?: string | null`

        - `content_guideline_instruction?: string | null`

        - `continuous_mode?: boolean | null`

        - `custom_metadata?: Record<string, unknown> | null`

          The custom metadata to attach to the documents.

        - `disable_image_extraction?: boolean | null`

        - `disable_ocr?: boolean | null`

        - `disable_reconstruction?: boolean | null`

        - `do_not_cache?: boolean | null`

        - `do_not_unroll_columns?: boolean | null`

        - `enable_cost_optimizer?: boolean | null`

        - `extract_charts?: boolean | null`

        - `extract_layout?: boolean | null`

        - `extract_printed_page_number?: boolean | null`

        - `fast_mode?: boolean | null`

        - `formatting_instruction?: string | null`

        - `gpt4o_api_key?: string | null`

        - `gpt4o_mode?: boolean | null`

        - `guess_xlsx_sheet_name?: boolean | null`

        - `hide_footers?: boolean | null`

        - `hide_headers?: boolean | null`

        - `high_res_ocr?: boolean | null`

        - `html_make_all_elements_visible?: boolean | null`

        - `html_remove_fixed_elements?: boolean | null`

        - `html_remove_navigation_elements?: boolean | null`

        - `http_proxy?: string | null`

        - `ignore_document_elements_for_layout_detection?: boolean | null`

        - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

          - `"screenshot"`

          - `"embedded"`

          - `"layout"`

        - `inline_images_in_markdown?: boolean | null`

        - `input_s3_path?: string | null`

        - `input_s3_region?: string | null`

          The region for the input S3 bucket.

        - `input_url?: string | null`

        - `internal_is_screenshot_job?: boolean | null`

        - `invalidate_cache?: boolean | null`

        - `is_formatting_instruction?: boolean | null`

        - `job_timeout_extra_time_per_page_in_seconds?: number | null`

        - `job_timeout_in_seconds?: number | null`

        - `keep_page_separator_when_merging_tables?: boolean | null`

        - `lang?: string`

          The language.

        - `languages?: Array<ParsingLanguages>`

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

        - `layout_aware?: boolean | null`

        - `line_level_bounding_box?: boolean | null`

        - `markdown_table_multiline_header_separator?: string | null`

        - `max_pages?: number | null`

        - `max_pages_enforced?: number | null`

        - `merge_tables_across_pages_in_markdown?: boolean | null`

        - `model?: string | null`

        - `outlined_table_extraction?: boolean | null`

        - `output_pdf_of_document?: boolean | null`

        - `output_s3_path_prefix?: string | null`

          If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

        - `output_s3_region?: string | null`

          The region for the output S3 bucket.

        - `output_tables_as_HTML?: boolean | null`

        - `outputBucket?: string | null`

          The output bucket.

        - `page_error_tolerance?: number | null`

        - `page_footer_prefix?: string | null`

        - `page_footer_suffix?: string | null`

        - `page_header_prefix?: string | null`

        - `page_header_suffix?: string | null`

        - `page_prefix?: string | null`

        - `page_separator?: string | null`

        - `page_suffix?: string | null`

        - `parse_mode?: ParsingMode | null`

          Enum for representing the mode of parsing to be used.

          - `"parse_page_without_llm"`

          - `"parse_page_with_llm"`

          - `"parse_page_with_lvm"`

          - `"parse_page_with_agent"`

          - `"parse_page_with_layout_agent"`

          - `"parse_document_with_llm"`

          - `"parse_document_with_lvm"`

          - `"parse_document_with_agent"`

        - `parsing_instruction?: string | null`

        - `pipeline_id?: string | null`

          The pipeline ID.

        - `precise_bounding_box?: boolean | null`

        - `premium_mode?: boolean | null`

        - `presentation_out_of_bounds_content?: boolean | null`

        - `presentation_skip_embedded_data?: boolean | null`

        - `preserve_layout_alignment_across_pages?: boolean | null`

        - `preserve_very_small_text?: boolean | null`

        - `preset?: string | null`

        - `priority?: "low" | "medium" | "high" | "critical" | null`

          The priority for the request. This field may be ignored or overwritten depending on the organization tier.

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"critical"`

        - `project_id?: string | null`

        - `remove_hidden_text?: boolean | null`

        - `replace_failed_page_mode?: FailPageMode | null`

          Enum for representing the different available page error handling modes.

          - `"raw_text"`

          - `"blank_page"`

          - `"error_message"`

        - `replace_failed_page_with_error_message_prefix?: string | null`

        - `replace_failed_page_with_error_message_suffix?: string | null`

        - `resource_info?: Record<string, unknown> | null`

          The resource info about the file

        - `save_images?: boolean | null`

        - `skip_diagonal_text?: boolean | null`

        - `specialized_chart_parsing_agentic?: boolean | null`

        - `specialized_chart_parsing_efficient?: boolean | null`

        - `specialized_chart_parsing_plus?: boolean | null`

        - `specialized_image_parsing?: boolean | null`

        - `spreadsheet_extract_sub_tables?: boolean | null`

        - `spreadsheet_force_formula_computation?: boolean | null`

        - `spreadsheet_include_hidden_sheets?: boolean | null`

        - `strict_mode_buggy_font?: boolean | null`

        - `strict_mode_image_extraction?: boolean | null`

        - `strict_mode_image_ocr?: boolean | null`

        - `strict_mode_reconstruction?: boolean | null`

        - `structured_output?: boolean | null`

        - `structured_output_json_schema?: string | null`

        - `structured_output_json_schema_name?: string | null`

        - `system_prompt?: string | null`

        - `system_prompt_append?: string | null`

        - `take_screenshot?: boolean | null`

        - `target_pages?: string | null`

        - `tier?: string | null`

        - `type?: "parse"`

          - `"parse"`

        - `use_vendor_multimodal_model?: boolean | null`

        - `user_prompt?: string | null`

        - `vendor_multimodal_api_key?: string | null`

        - `vendor_multimodal_model_name?: string | null`

        - `version?: string | null`

        - `webhook_configurations?: Array<WebhookConfiguration> | null`

          Outbound webhook endpoints to notify on job status changes

          - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

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

          - `webhook_headers?: Record<string, string> | null`

            Custom HTTP headers sent with each webhook request (e.g. auth tokens)

          - `webhook_output_format?: string | null`

            Response format sent to the webhook: 'string' (default) or 'json'

          - `webhook_url?: string | null`

            URL to receive webhook POST notifications

        - `webhook_url?: string | null`

      - `parent_job_execution_id?: string | null`

        The ID of the parent job execution.

      - `partitions?: Record<string, string>`

        The partitions for this execution. Used for determining where to save job output.

      - `project_id?: string | null`

        The ID of the project this job belongs to.

      - `session_id?: string | null`

        The upstream request ID that created this job. Used for tracking the job across services.

      - `user_id?: string | null`

        The ID of the user that created this job

      - `webhook_url?: string | null`

        The URL that needs to be called at the end of the parsing job.

    - `ClassifyJob`

      A classify job.

      - `id: string`

        Unique identifier

      - `project_id: string`

        The ID of the project

      - `rules: Array<ClassifierRule>`

        The rules to classify the files

        - `description: string`

          Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

        - `type: string`

          The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

      - `status: StatusEnum`

        The status of the classify job

        - `"PENDING"`

        - `"SUCCESS"`

        - `"ERROR"`

        - `"PARTIAL_SUCCESS"`

        - `"CANCELLED"`

      - `user_id: string`

        The ID of the user

      - `created_at?: string | null`

        Creation datetime

      - `effective_at?: string`

      - `error_message?: string | null`

        Error message for the latest job attempt, if any.

      - `job_record_id?: string | null`

        The job record ID associated with this status, if any.

      - `mode?: "FAST" | "MULTIMODAL"`

        The classification mode to use

        - `"FAST"`

        - `"MULTIMODAL"`

      - `parsing_configuration?: ClassifyParsingConfiguration`

        The configuration for the parsing job

        - `lang?: ParsingLanguages`

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

        - `max_pages?: number | null`

          The maximum number of pages to parse

        - `target_pages?: Array<number> | null`

          The pages to target for parsing (0-indexed, so first page is at 0)

      - `updated_at?: string | null`

        Update datetime

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `continue_as_new_threshold?: number | null`

    Body param: Maximum files to process per execution cycle in directory mode. Defaults to page_size.

  - `directory_id?: string | null`

    Body param: ID of the directory containing files to process

  - `item_ids?: Array<string> | null`

    Body param: List of specific item IDs to process. Either this or directory_id must be provided.

  - `page_size?: number`

    Body param: Number of files to process per batch when using directory mode

  - `temporalNamespace?: string`

    Header param

### Returns

- `BatchCreateResponse`

  Response schema for a batch processing job.

  - `id: string`

    Unique identifier for the batch job

  - `job_type: "parse" | "extract" | "classify"`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: string`

    Project this job belongs to

  - `status: "pending" | "running" | "dispatched" | 3 more`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: number`

    Total number of items in the job

  - `completed_at?: string | null`

    Timestamp when job completed

  - `created_at?: string | null`

    Creation datetime

  - `directory_id?: string | null`

    Directory being processed

  - `effective_at?: string`

  - `error_message?: string | null`

    Error message for the latest job attempt, if any.

  - `failed_items?: number`

    Number of items that failed processing

  - `job_record_id?: string | null`

    The job record ID associated with this status, if any.

  - `processed_items?: number`

    Number of items processed so far

  - `skipped_items?: number`

    Number of items skipped (already processed or size limit)

  - `started_at?: string | null`

    Timestamp when job processing started

  - `updated_at?: string | null`

    Update datetime

  - `workflow_id?: string | null`

    Async job tracking ID

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const batch = await client.beta.batch.create({ job_config: {} });

console.log(batch.id);
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

`client.beta.batch.list(BatchListParamsquery?, RequestOptionsoptions?): PaginatedBatchItems<BatchListResponse>`

**get** `/api/v1/beta/batch-processing`

List batch processing jobs with optional filtering.

Filter by `directory_id`, `job_type`, or `status`. Results
are paginated with configurable `limit` and `offset`.

### Parameters

- `query: BatchListParams`

  - `directory_id?: string | null`

    Filter by directory ID

  - `job_type?: "parse" | "extract" | "classify" | null`

    Filter by job type (PARSE, EXTRACT, CLASSIFY)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `limit?: number`

    Maximum number of jobs to return

  - `offset?: number`

    Number of jobs to skip for pagination

  - `organization_id?: string | null`

  - `project_id?: string | null`

  - `status?: "pending" | "running" | "dispatched" | 3 more | null`

    Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

### Returns

- `BatchListResponse`

  Response schema for a batch processing job.

  - `id: string`

    Unique identifier for the batch job

  - `job_type: "parse" | "extract" | "classify"`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: string`

    Project this job belongs to

  - `status: "pending" | "running" | "dispatched" | 3 more`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: number`

    Total number of items in the job

  - `completed_at?: string | null`

    Timestamp when job completed

  - `created_at?: string | null`

    Creation datetime

  - `directory_id?: string | null`

    Directory being processed

  - `effective_at?: string`

  - `error_message?: string | null`

    Error message for the latest job attempt, if any.

  - `failed_items?: number`

    Number of items that failed processing

  - `job_record_id?: string | null`

    The job record ID associated with this status, if any.

  - `processed_items?: number`

    Number of items processed so far

  - `skipped_items?: number`

    Number of items skipped (already processed or size limit)

  - `started_at?: string | null`

    Timestamp when job processing started

  - `updated_at?: string | null`

    Update datetime

  - `workflow_id?: string | null`

    Async job tracking ID

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const batchListResponse of client.beta.batch.list()) {
  console.log(batchListResponse.id);
}
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

`client.beta.batch.getStatus(stringjobID, BatchGetStatusParamsquery?, RequestOptionsoptions?): BatchGetStatusResponse`

**get** `/api/v1/beta/batch-processing/{job_id}`

Get detailed status of a batch processing job.

Returns current progress percentage, file counts (total,
processed, failed, skipped), and timestamps.

### Parameters

- `jobID: string`

- `query: BatchGetStatusParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `BatchGetStatusResponse`

  Detailed status response for a batch processing job.

  - `job: Job`

    Response schema for a batch processing job.

    - `id: string`

      Unique identifier for the batch job

    - `job_type: "parse" | "extract" | "classify"`

      Type of processing operation (parse or classify)

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `project_id: string`

      Project this job belongs to

    - `status: "pending" | "running" | "dispatched" | 3 more`

      Current job status

      - `"pending"`

      - `"running"`

      - `"dispatched"`

      - `"completed"`

      - `"failed"`

      - `"cancelled"`

    - `total_items: number`

      Total number of items in the job

    - `completed_at?: string | null`

      Timestamp when job completed

    - `created_at?: string | null`

      Creation datetime

    - `directory_id?: string | null`

      Directory being processed

    - `effective_at?: string`

    - `error_message?: string | null`

      Error message for the latest job attempt, if any.

    - `failed_items?: number`

      Number of items that failed processing

    - `job_record_id?: string | null`

      The job record ID associated with this status, if any.

    - `processed_items?: number`

      Number of items processed so far

    - `skipped_items?: number`

      Number of items skipped (already processed or size limit)

    - `started_at?: string | null`

      Timestamp when job processing started

    - `updated_at?: string | null`

      Update datetime

    - `workflow_id?: string | null`

      Async job tracking ID

  - `progress_percentage: number`

    Percentage of items processed (0-100)

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.batch.getStatus('job_id');

console.log(response.job);
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

`client.beta.batch.cancel(stringjobID, BatchCancelParamsparams, RequestOptionsoptions?): BatchCancelResponse`

**post** `/api/v1/beta/batch-processing/{job_id}/cancel`

Cancel a running batch processing job.

Stops processing and marks pending items as cancelled.
Items currently being processed may still complete.

### Parameters

- `jobID: string`

- `params: BatchCancelParams`

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `reason?: string | null`

    Body param: Optional reason for cancelling the job

  - `temporalNamespace?: string`

    Header param

### Returns

- `BatchCancelResponse`

  Response after cancelling a batch job.

  - `job_id: string`

    ID of the cancelled job

  - `message: string`

    Confirmation message

  - `processed_items: number`

    Number of items processed before cancellation

  - `status: "pending" | "running" | "dispatched" | 3 more`

    New status (should be 'cancelled')

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.batch.cancel('job_id');

console.log(response.job_id);
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

- `BatchCreateResponse`

  Response schema for a batch processing job.

  - `id: string`

    Unique identifier for the batch job

  - `job_type: "parse" | "extract" | "classify"`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: string`

    Project this job belongs to

  - `status: "pending" | "running" | "dispatched" | 3 more`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: number`

    Total number of items in the job

  - `completed_at?: string | null`

    Timestamp when job completed

  - `created_at?: string | null`

    Creation datetime

  - `directory_id?: string | null`

    Directory being processed

  - `effective_at?: string`

  - `error_message?: string | null`

    Error message for the latest job attempt, if any.

  - `failed_items?: number`

    Number of items that failed processing

  - `job_record_id?: string | null`

    The job record ID associated with this status, if any.

  - `processed_items?: number`

    Number of items processed so far

  - `skipped_items?: number`

    Number of items skipped (already processed or size limit)

  - `started_at?: string | null`

    Timestamp when job processing started

  - `updated_at?: string | null`

    Update datetime

  - `workflow_id?: string | null`

    Async job tracking ID

### Batch List Response

- `BatchListResponse`

  Response schema for a batch processing job.

  - `id: string`

    Unique identifier for the batch job

  - `job_type: "parse" | "extract" | "classify"`

    Type of processing operation (parse or classify)

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `project_id: string`

    Project this job belongs to

  - `status: "pending" | "running" | "dispatched" | 3 more`

    Current job status

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

  - `total_items: number`

    Total number of items in the job

  - `completed_at?: string | null`

    Timestamp when job completed

  - `created_at?: string | null`

    Creation datetime

  - `directory_id?: string | null`

    Directory being processed

  - `effective_at?: string`

  - `error_message?: string | null`

    Error message for the latest job attempt, if any.

  - `failed_items?: number`

    Number of items that failed processing

  - `job_record_id?: string | null`

    The job record ID associated with this status, if any.

  - `processed_items?: number`

    Number of items processed so far

  - `skipped_items?: number`

    Number of items skipped (already processed or size limit)

  - `started_at?: string | null`

    Timestamp when job processing started

  - `updated_at?: string | null`

    Update datetime

  - `workflow_id?: string | null`

    Async job tracking ID

### Batch Get Status Response

- `BatchGetStatusResponse`

  Detailed status response for a batch processing job.

  - `job: Job`

    Response schema for a batch processing job.

    - `id: string`

      Unique identifier for the batch job

    - `job_type: "parse" | "extract" | "classify"`

      Type of processing operation (parse or classify)

      - `"parse"`

      - `"extract"`

      - `"classify"`

    - `project_id: string`

      Project this job belongs to

    - `status: "pending" | "running" | "dispatched" | 3 more`

      Current job status

      - `"pending"`

      - `"running"`

      - `"dispatched"`

      - `"completed"`

      - `"failed"`

      - `"cancelled"`

    - `total_items: number`

      Total number of items in the job

    - `completed_at?: string | null`

      Timestamp when job completed

    - `created_at?: string | null`

      Creation datetime

    - `directory_id?: string | null`

      Directory being processed

    - `effective_at?: string`

    - `error_message?: string | null`

      Error message for the latest job attempt, if any.

    - `failed_items?: number`

      Number of items that failed processing

    - `job_record_id?: string | null`

      The job record ID associated with this status, if any.

    - `processed_items?: number`

      Number of items processed so far

    - `skipped_items?: number`

      Number of items skipped (already processed or size limit)

    - `started_at?: string | null`

      Timestamp when job processing started

    - `updated_at?: string | null`

      Update datetime

    - `workflow_id?: string | null`

      Async job tracking ID

  - `progress_percentage: number`

    Percentage of items processed (0-100)

### Batch Cancel Response

- `BatchCancelResponse`

  Response after cancelling a batch job.

  - `job_id: string`

    ID of the cancelled job

  - `message: string`

    Confirmation message

  - `processed_items: number`

    Number of items processed before cancellation

  - `status: "pending" | "running" | "dispatched" | 3 more`

    New status (should be 'cancelled')

    - `"pending"`

    - `"running"`

    - `"dispatched"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

# Job Items

## List Batch Job Items

`client.beta.batch.jobItems.list(stringjobID, JobItemListParamsquery?, RequestOptionsoptions?): PaginatedBatchItems<JobItemListResponse>`

**get** `/api/v1/beta/batch-processing/{job_id}/items`

List items in a batch job with optional status filtering.

Useful for finding failed items, viewing completed items,
or debugging processing issues.

### Parameters

- `jobID: string`

- `query: JobItemListParams`

  - `limit?: number`

    Maximum number of items to return

  - `offset?: number`

    Number of items to skip

  - `organization_id?: string | null`

  - `project_id?: string | null`

  - `status?: "pending" | "processing" | "completed" | 3 more | null`

    Filter items by status

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

    - `"cancelled"`

### Returns

- `JobItemListResponse`

  Detailed information about an item in a batch job.

  - `item_id: string`

    ID of the item

  - `item_name: string`

    Name of the item

  - `status: "pending" | "processing" | "completed" | 3 more`

    Processing status of this item

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

    - `"cancelled"`

  - `completed_at?: string | null`

    When processing completed for this item

  - `effective_at?: string`

  - `error_message?: string | null`

    Error message for the latest job attempt, if any.

  - `job_id?: string | null`

    Job ID for the underlying processing job (links to parse/extract job results)

  - `job_record_id?: string | null`

    The job record ID associated with this status, if any.

  - `skip_reason?: string | null`

    Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

  - `started_at?: string | null`

    When processing started for this item

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const jobItemListResponse of client.beta.batch.jobItems.list('job_id')) {
  console.log(jobItemListResponse.item_id);
}
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

`client.beta.batch.jobItems.getProcessingResults(stringitemID, JobItemGetProcessingResultsParamsquery?, RequestOptionsoptions?): JobItemGetProcessingResultsResponse`

**get** `/api/v1/beta/batch-processing/items/{item_id}/processing-results`

Get all processing results for a specific item.

Returns the complete processing history for an item including
what operations were performed, parameters used, and where
outputs are stored. Optionally filter by `job_type`.

### Parameters

- `itemID: string`

- `query: JobItemGetProcessingResultsParams`

  - `job_type?: "parse" | "extract" | "classify" | null`

    Filter results by job type

    - `"parse"`

    - `"extract"`

    - `"classify"`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `JobItemGetProcessingResultsResponse`

  Response containing all processing results for an item.

  - `item_id: string`

    ID of the source item

  - `item_name: string`

    Name of the source item

  - `processing_results?: Array<ProcessingResult>`

    List of all processing operations performed on this item

    - `item_id: string`

      Source item that was processed

    - `job_config: BatchParseJobRecordCreate | ClassifyJob`

      Job configuration used for processing

      - `BatchParseJobRecordCreate`

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

        - `correlation_id?: string | null`

          The correlation ID for this job. Used for tracking the job across services.

        - `job_name?: "parse_raw_file_job"`

          - `"parse_raw_file_job"`

        - `parameters?: Parameters | null`

          Generic parse job configuration for batch processing.

          This model contains the parsing configuration that applies to all files
          in a batch, but excludes file-specific fields like file_name, file_id, etc.
          Those file-specific fields are populated from DirectoryFile data when
          creating individual ParseJobRecordCreate instances for each file.

          The fields in this model should be generic settings that apply uniformly
          to all files being processed in the batch.

          - `adaptive_long_table?: boolean | null`

          - `aggressive_table_extraction?: boolean | null`

          - `annotate_links?: boolean | null`

          - `auto_mode?: boolean | null`

          - `auto_mode_configuration_json?: string | null`

          - `auto_mode_trigger_on_image_in_page?: boolean | null`

          - `auto_mode_trigger_on_regexp_in_page?: string | null`

          - `auto_mode_trigger_on_table_in_page?: boolean | null`

          - `auto_mode_trigger_on_text_in_page?: string | null`

          - `azure_openai_api_version?: string | null`

          - `azure_openai_deployment_name?: string | null`

          - `azure_openai_endpoint?: string | null`

          - `azure_openai_key?: string | null`

          - `bbox_bottom?: number | null`

          - `bbox_left?: number | null`

          - `bbox_right?: number | null`

          - `bbox_top?: number | null`

          - `bounding_box?: string | null`

          - `compact_markdown_table?: boolean | null`

          - `complemental_formatting_instruction?: string | null`

          - `content_guideline_instruction?: string | null`

          - `continuous_mode?: boolean | null`

          - `custom_metadata?: Record<string, unknown> | null`

            The custom metadata to attach to the documents.

          - `disable_image_extraction?: boolean | null`

          - `disable_ocr?: boolean | null`

          - `disable_reconstruction?: boolean | null`

          - `do_not_cache?: boolean | null`

          - `do_not_unroll_columns?: boolean | null`

          - `enable_cost_optimizer?: boolean | null`

          - `extract_charts?: boolean | null`

          - `extract_layout?: boolean | null`

          - `extract_printed_page_number?: boolean | null`

          - `fast_mode?: boolean | null`

          - `formatting_instruction?: string | null`

          - `gpt4o_api_key?: string | null`

          - `gpt4o_mode?: boolean | null`

          - `guess_xlsx_sheet_name?: boolean | null`

          - `hide_footers?: boolean | null`

          - `hide_headers?: boolean | null`

          - `high_res_ocr?: boolean | null`

          - `html_make_all_elements_visible?: boolean | null`

          - `html_remove_fixed_elements?: boolean | null`

          - `html_remove_navigation_elements?: boolean | null`

          - `http_proxy?: string | null`

          - `ignore_document_elements_for_layout_detection?: boolean | null`

          - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

            - `"screenshot"`

            - `"embedded"`

            - `"layout"`

          - `inline_images_in_markdown?: boolean | null`

          - `input_s3_path?: string | null`

          - `input_s3_region?: string | null`

            The region for the input S3 bucket.

          - `input_url?: string | null`

          - `internal_is_screenshot_job?: boolean | null`

          - `invalidate_cache?: boolean | null`

          - `is_formatting_instruction?: boolean | null`

          - `job_timeout_extra_time_per_page_in_seconds?: number | null`

          - `job_timeout_in_seconds?: number | null`

          - `keep_page_separator_when_merging_tables?: boolean | null`

          - `lang?: string`

            The language.

          - `languages?: Array<ParsingLanguages>`

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

          - `layout_aware?: boolean | null`

          - `line_level_bounding_box?: boolean | null`

          - `markdown_table_multiline_header_separator?: string | null`

          - `max_pages?: number | null`

          - `max_pages_enforced?: number | null`

          - `merge_tables_across_pages_in_markdown?: boolean | null`

          - `model?: string | null`

          - `outlined_table_extraction?: boolean | null`

          - `output_pdf_of_document?: boolean | null`

          - `output_s3_path_prefix?: string | null`

            If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

          - `output_s3_region?: string | null`

            The region for the output S3 bucket.

          - `output_tables_as_HTML?: boolean | null`

          - `outputBucket?: string | null`

            The output bucket.

          - `page_error_tolerance?: number | null`

          - `page_footer_prefix?: string | null`

          - `page_footer_suffix?: string | null`

          - `page_header_prefix?: string | null`

          - `page_header_suffix?: string | null`

          - `page_prefix?: string | null`

          - `page_separator?: string | null`

          - `page_suffix?: string | null`

          - `parse_mode?: ParsingMode | null`

            Enum for representing the mode of parsing to be used.

            - `"parse_page_without_llm"`

            - `"parse_page_with_llm"`

            - `"parse_page_with_lvm"`

            - `"parse_page_with_agent"`

            - `"parse_page_with_layout_agent"`

            - `"parse_document_with_llm"`

            - `"parse_document_with_lvm"`

            - `"parse_document_with_agent"`

          - `parsing_instruction?: string | null`

          - `pipeline_id?: string | null`

            The pipeline ID.

          - `precise_bounding_box?: boolean | null`

          - `premium_mode?: boolean | null`

          - `presentation_out_of_bounds_content?: boolean | null`

          - `presentation_skip_embedded_data?: boolean | null`

          - `preserve_layout_alignment_across_pages?: boolean | null`

          - `preserve_very_small_text?: boolean | null`

          - `preset?: string | null`

          - `priority?: "low" | "medium" | "high" | "critical" | null`

            The priority for the request. This field may be ignored or overwritten depending on the organization tier.

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"critical"`

          - `project_id?: string | null`

          - `remove_hidden_text?: boolean | null`

          - `replace_failed_page_mode?: FailPageMode | null`

            Enum for representing the different available page error handling modes.

            - `"raw_text"`

            - `"blank_page"`

            - `"error_message"`

          - `replace_failed_page_with_error_message_prefix?: string | null`

          - `replace_failed_page_with_error_message_suffix?: string | null`

          - `resource_info?: Record<string, unknown> | null`

            The resource info about the file

          - `save_images?: boolean | null`

          - `skip_diagonal_text?: boolean | null`

          - `specialized_chart_parsing_agentic?: boolean | null`

          - `specialized_chart_parsing_efficient?: boolean | null`

          - `specialized_chart_parsing_plus?: boolean | null`

          - `specialized_image_parsing?: boolean | null`

          - `spreadsheet_extract_sub_tables?: boolean | null`

          - `spreadsheet_force_formula_computation?: boolean | null`

          - `spreadsheet_include_hidden_sheets?: boolean | null`

          - `strict_mode_buggy_font?: boolean | null`

          - `strict_mode_image_extraction?: boolean | null`

          - `strict_mode_image_ocr?: boolean | null`

          - `strict_mode_reconstruction?: boolean | null`

          - `structured_output?: boolean | null`

          - `structured_output_json_schema?: string | null`

          - `structured_output_json_schema_name?: string | null`

          - `system_prompt?: string | null`

          - `system_prompt_append?: string | null`

          - `take_screenshot?: boolean | null`

          - `target_pages?: string | null`

          - `tier?: string | null`

          - `type?: "parse"`

            - `"parse"`

          - `use_vendor_multimodal_model?: boolean | null`

          - `user_prompt?: string | null`

          - `vendor_multimodal_api_key?: string | null`

          - `vendor_multimodal_model_name?: string | null`

          - `version?: string | null`

          - `webhook_configurations?: Array<WebhookConfiguration> | null`

            Outbound webhook endpoints to notify on job status changes

            - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

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

            - `webhook_headers?: Record<string, string> | null`

              Custom HTTP headers sent with each webhook request (e.g. auth tokens)

            - `webhook_output_format?: string | null`

              Response format sent to the webhook: 'string' (default) or 'json'

            - `webhook_url?: string | null`

              URL to receive webhook POST notifications

          - `webhook_url?: string | null`

        - `parent_job_execution_id?: string | null`

          The ID of the parent job execution.

        - `partitions?: Record<string, string>`

          The partitions for this execution. Used for determining where to save job output.

        - `project_id?: string | null`

          The ID of the project this job belongs to.

        - `session_id?: string | null`

          The upstream request ID that created this job. Used for tracking the job across services.

        - `user_id?: string | null`

          The ID of the user that created this job

        - `webhook_url?: string | null`

          The URL that needs to be called at the end of the parsing job.

      - `ClassifyJob`

        A classify job.

        - `id: string`

          Unique identifier

        - `project_id: string`

          The ID of the project

        - `rules: Array<ClassifierRule>`

          The rules to classify the files

          - `description: string`

            Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

          - `type: string`

            The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

        - `status: StatusEnum`

          The status of the classify job

          - `"PENDING"`

          - `"SUCCESS"`

          - `"ERROR"`

          - `"PARTIAL_SUCCESS"`

          - `"CANCELLED"`

        - `user_id: string`

          The ID of the user

        - `created_at?: string | null`

          Creation datetime

        - `effective_at?: string`

        - `error_message?: string | null`

          Error message for the latest job attempt, if any.

        - `job_record_id?: string | null`

          The job record ID associated with this status, if any.

        - `mode?: "FAST" | "MULTIMODAL"`

          The classification mode to use

          - `"FAST"`

          - `"MULTIMODAL"`

        - `parsing_configuration?: ClassifyParsingConfiguration`

          The configuration for the parsing job

          - `lang?: ParsingLanguages`

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

          - `max_pages?: number | null`

            The maximum number of pages to parse

          - `target_pages?: Array<number> | null`

            The pages to target for parsing (0-indexed, so first page is at 0)

        - `updated_at?: string | null`

          Update datetime

    - `job_type: "parse" | "extract" | "classify"`

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

    - `output_metadata?: unknown`

      Metadata about processing output.

      Currently empty - will be populated with job-type-specific metadata fields in the future.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.batch.jobItems.getProcessingResults('item_id');

console.log(response.item_id);
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

- `JobItemListResponse`

  Detailed information about an item in a batch job.

  - `item_id: string`

    ID of the item

  - `item_name: string`

    Name of the item

  - `status: "pending" | "processing" | "completed" | 3 more`

    Processing status of this item

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

    - `"cancelled"`

  - `completed_at?: string | null`

    When processing completed for this item

  - `effective_at?: string`

  - `error_message?: string | null`

    Error message for the latest job attempt, if any.

  - `job_id?: string | null`

    Job ID for the underlying processing job (links to parse/extract job results)

  - `job_record_id?: string | null`

    The job record ID associated with this status, if any.

  - `skip_reason?: string | null`

    Reason item was skipped (e.g., 'already_processed', 'size_limit_exceeded')

  - `started_at?: string | null`

    When processing started for this item

### Job Item Get Processing Results Response

- `JobItemGetProcessingResultsResponse`

  Response containing all processing results for an item.

  - `item_id: string`

    ID of the source item

  - `item_name: string`

    Name of the source item

  - `processing_results?: Array<ProcessingResult>`

    List of all processing operations performed on this item

    - `item_id: string`

      Source item that was processed

    - `job_config: BatchParseJobRecordCreate | ClassifyJob`

      Job configuration used for processing

      - `BatchParseJobRecordCreate`

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

        - `correlation_id?: string | null`

          The correlation ID for this job. Used for tracking the job across services.

        - `job_name?: "parse_raw_file_job"`

          - `"parse_raw_file_job"`

        - `parameters?: Parameters | null`

          Generic parse job configuration for batch processing.

          This model contains the parsing configuration that applies to all files
          in a batch, but excludes file-specific fields like file_name, file_id, etc.
          Those file-specific fields are populated from DirectoryFile data when
          creating individual ParseJobRecordCreate instances for each file.

          The fields in this model should be generic settings that apply uniformly
          to all files being processed in the batch.

          - `adaptive_long_table?: boolean | null`

          - `aggressive_table_extraction?: boolean | null`

          - `annotate_links?: boolean | null`

          - `auto_mode?: boolean | null`

          - `auto_mode_configuration_json?: string | null`

          - `auto_mode_trigger_on_image_in_page?: boolean | null`

          - `auto_mode_trigger_on_regexp_in_page?: string | null`

          - `auto_mode_trigger_on_table_in_page?: boolean | null`

          - `auto_mode_trigger_on_text_in_page?: string | null`

          - `azure_openai_api_version?: string | null`

          - `azure_openai_deployment_name?: string | null`

          - `azure_openai_endpoint?: string | null`

          - `azure_openai_key?: string | null`

          - `bbox_bottom?: number | null`

          - `bbox_left?: number | null`

          - `bbox_right?: number | null`

          - `bbox_top?: number | null`

          - `bounding_box?: string | null`

          - `compact_markdown_table?: boolean | null`

          - `complemental_formatting_instruction?: string | null`

          - `content_guideline_instruction?: string | null`

          - `continuous_mode?: boolean | null`

          - `custom_metadata?: Record<string, unknown> | null`

            The custom metadata to attach to the documents.

          - `disable_image_extraction?: boolean | null`

          - `disable_ocr?: boolean | null`

          - `disable_reconstruction?: boolean | null`

          - `do_not_cache?: boolean | null`

          - `do_not_unroll_columns?: boolean | null`

          - `enable_cost_optimizer?: boolean | null`

          - `extract_charts?: boolean | null`

          - `extract_layout?: boolean | null`

          - `extract_printed_page_number?: boolean | null`

          - `fast_mode?: boolean | null`

          - `formatting_instruction?: string | null`

          - `gpt4o_api_key?: string | null`

          - `gpt4o_mode?: boolean | null`

          - `guess_xlsx_sheet_name?: boolean | null`

          - `hide_footers?: boolean | null`

          - `hide_headers?: boolean | null`

          - `high_res_ocr?: boolean | null`

          - `html_make_all_elements_visible?: boolean | null`

          - `html_remove_fixed_elements?: boolean | null`

          - `html_remove_navigation_elements?: boolean | null`

          - `http_proxy?: string | null`

          - `ignore_document_elements_for_layout_detection?: boolean | null`

          - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

            - `"screenshot"`

            - `"embedded"`

            - `"layout"`

          - `inline_images_in_markdown?: boolean | null`

          - `input_s3_path?: string | null`

          - `input_s3_region?: string | null`

            The region for the input S3 bucket.

          - `input_url?: string | null`

          - `internal_is_screenshot_job?: boolean | null`

          - `invalidate_cache?: boolean | null`

          - `is_formatting_instruction?: boolean | null`

          - `job_timeout_extra_time_per_page_in_seconds?: number | null`

          - `job_timeout_in_seconds?: number | null`

          - `keep_page_separator_when_merging_tables?: boolean | null`

          - `lang?: string`

            The language.

          - `languages?: Array<ParsingLanguages>`

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

          - `layout_aware?: boolean | null`

          - `line_level_bounding_box?: boolean | null`

          - `markdown_table_multiline_header_separator?: string | null`

          - `max_pages?: number | null`

          - `max_pages_enforced?: number | null`

          - `merge_tables_across_pages_in_markdown?: boolean | null`

          - `model?: string | null`

          - `outlined_table_extraction?: boolean | null`

          - `output_pdf_of_document?: boolean | null`

          - `output_s3_path_prefix?: string | null`

            If specified, llamaParse will save the output to the specified path. All output file will use this 'prefix' should be a valid s3:// url

          - `output_s3_region?: string | null`

            The region for the output S3 bucket.

          - `output_tables_as_HTML?: boolean | null`

          - `outputBucket?: string | null`

            The output bucket.

          - `page_error_tolerance?: number | null`

          - `page_footer_prefix?: string | null`

          - `page_footer_suffix?: string | null`

          - `page_header_prefix?: string | null`

          - `page_header_suffix?: string | null`

          - `page_prefix?: string | null`

          - `page_separator?: string | null`

          - `page_suffix?: string | null`

          - `parse_mode?: ParsingMode | null`

            Enum for representing the mode of parsing to be used.

            - `"parse_page_without_llm"`

            - `"parse_page_with_llm"`

            - `"parse_page_with_lvm"`

            - `"parse_page_with_agent"`

            - `"parse_page_with_layout_agent"`

            - `"parse_document_with_llm"`

            - `"parse_document_with_lvm"`

            - `"parse_document_with_agent"`

          - `parsing_instruction?: string | null`

          - `pipeline_id?: string | null`

            The pipeline ID.

          - `precise_bounding_box?: boolean | null`

          - `premium_mode?: boolean | null`

          - `presentation_out_of_bounds_content?: boolean | null`

          - `presentation_skip_embedded_data?: boolean | null`

          - `preserve_layout_alignment_across_pages?: boolean | null`

          - `preserve_very_small_text?: boolean | null`

          - `preset?: string | null`

          - `priority?: "low" | "medium" | "high" | "critical" | null`

            The priority for the request. This field may be ignored or overwritten depending on the organization tier.

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"critical"`

          - `project_id?: string | null`

          - `remove_hidden_text?: boolean | null`

          - `replace_failed_page_mode?: FailPageMode | null`

            Enum for representing the different available page error handling modes.

            - `"raw_text"`

            - `"blank_page"`

            - `"error_message"`

          - `replace_failed_page_with_error_message_prefix?: string | null`

          - `replace_failed_page_with_error_message_suffix?: string | null`

          - `resource_info?: Record<string, unknown> | null`

            The resource info about the file

          - `save_images?: boolean | null`

          - `skip_diagonal_text?: boolean | null`

          - `specialized_chart_parsing_agentic?: boolean | null`

          - `specialized_chart_parsing_efficient?: boolean | null`

          - `specialized_chart_parsing_plus?: boolean | null`

          - `specialized_image_parsing?: boolean | null`

          - `spreadsheet_extract_sub_tables?: boolean | null`

          - `spreadsheet_force_formula_computation?: boolean | null`

          - `spreadsheet_include_hidden_sheets?: boolean | null`

          - `strict_mode_buggy_font?: boolean | null`

          - `strict_mode_image_extraction?: boolean | null`

          - `strict_mode_image_ocr?: boolean | null`

          - `strict_mode_reconstruction?: boolean | null`

          - `structured_output?: boolean | null`

          - `structured_output_json_schema?: string | null`

          - `structured_output_json_schema_name?: string | null`

          - `system_prompt?: string | null`

          - `system_prompt_append?: string | null`

          - `take_screenshot?: boolean | null`

          - `target_pages?: string | null`

          - `tier?: string | null`

          - `type?: "parse"`

            - `"parse"`

          - `use_vendor_multimodal_model?: boolean | null`

          - `user_prompt?: string | null`

          - `vendor_multimodal_api_key?: string | null`

          - `vendor_multimodal_model_name?: string | null`

          - `version?: string | null`

          - `webhook_configurations?: Array<WebhookConfiguration> | null`

            Outbound webhook endpoints to notify on job status changes

            - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

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

            - `webhook_headers?: Record<string, string> | null`

              Custom HTTP headers sent with each webhook request (e.g. auth tokens)

            - `webhook_output_format?: string | null`

              Response format sent to the webhook: 'string' (default) or 'json'

            - `webhook_url?: string | null`

              URL to receive webhook POST notifications

          - `webhook_url?: string | null`

        - `parent_job_execution_id?: string | null`

          The ID of the parent job execution.

        - `partitions?: Record<string, string>`

          The partitions for this execution. Used for determining where to save job output.

        - `project_id?: string | null`

          The ID of the project this job belongs to.

        - `session_id?: string | null`

          The upstream request ID that created this job. Used for tracking the job across services.

        - `user_id?: string | null`

          The ID of the user that created this job

        - `webhook_url?: string | null`

          The URL that needs to be called at the end of the parsing job.

      - `ClassifyJob`

        A classify job.

        - `id: string`

          Unique identifier

        - `project_id: string`

          The ID of the project

        - `rules: Array<ClassifierRule>`

          The rules to classify the files

          - `description: string`

            Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

          - `type: string`

            The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

        - `status: StatusEnum`

          The status of the classify job

          - `"PENDING"`

          - `"SUCCESS"`

          - `"ERROR"`

          - `"PARTIAL_SUCCESS"`

          - `"CANCELLED"`

        - `user_id: string`

          The ID of the user

        - `created_at?: string | null`

          Creation datetime

        - `effective_at?: string`

        - `error_message?: string | null`

          Error message for the latest job attempt, if any.

        - `job_record_id?: string | null`

          The job record ID associated with this status, if any.

        - `mode?: "FAST" | "MULTIMODAL"`

          The classification mode to use

          - `"FAST"`

          - `"MULTIMODAL"`

        - `parsing_configuration?: ClassifyParsingConfiguration`

          The configuration for the parsing job

          - `lang?: ParsingLanguages`

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

          - `max_pages?: number | null`

            The maximum number of pages to parse

          - `target_pages?: Array<number> | null`

            The pages to target for parsing (0-indexed, so first page is at 0)

        - `updated_at?: string | null`

          Update datetime

    - `job_type: "parse" | "extract" | "classify"`

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

    - `output_metadata?: unknown`

      Metadata about processing output.

      Currently empty - will be populated with job-type-specific metadata fields in the future.

# Split

## Create Split Job

`client.beta.split.create(SplitCreateParamsparams, RequestOptionsoptions?): SplitCreateResponse`

**post** `/api/v1/beta/split/jobs`

Create a document split job.

### Parameters

- `params: SplitCreateParams`

  - `document_input: SplitDocumentInput`

    Body param: Document to be split.

    - `type: string`

      Type of document input. Valid values are: file_id

    - `value: string`

      Document identifier.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `configuration?: Configuration | null`

    Body param: Split configuration with categories and splitting strategy.

    - `categories: Array<SplitCategory>`

      Categories to split documents into.

      - `name: string`

        Name of the category.

      - `description?: string | null`

        Optional description of what content belongs in this category.

    - `splitting_strategy?: SplittingStrategy`

      Strategy for splitting documents.

      - `allow_uncategorized?: "include" | "forbid" | "omit"`

        Controls handling of pages that don't match any category. 'include': pages can be grouped as 'uncategorized' and included in results. 'forbid': all pages must be assigned to a defined category. 'omit': pages can be classified as 'uncategorized' but are excluded from results.

        - `"include"`

        - `"forbid"`

        - `"omit"`

  - `configuration_id?: string | null`

    Body param: Saved split configuration ID.

### Returns

- `SplitCreateResponse`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: Array<SplitCategory>`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description?: string | null`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

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

  - `configuration_id?: string | null`

    Split configuration ID used for this job.

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error message if the job failed.

  - `result?: SplitResultResponse | null`

    Result of a completed split job.

    - `segments: Array<SplitSegmentResponse>`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: Array<number>`

        1-indexed page numbers in this split.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const split = await client.beta.split.create({ document_input: { type: 'type', value: 'value' } });

console.log(split.id);
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

`client.beta.split.list(SplitListParamsquery?, RequestOptionsoptions?): PaginatedCursor<SplitListResponse>`

**get** `/api/v1/beta/split/jobs`

List document split jobs.

### Parameters

- `query: SplitListParams`

  - `created_at_on_or_after?: string | null`

    Include items created at or after this timestamp (inclusive)

  - `created_at_on_or_before?: string | null`

    Include items created at or before this timestamp (inclusive)

  - `job_ids?: Array<string> | null`

    Filter by specific job IDs

  - `organization_id?: string | null`

  - `page_size?: number | null`

  - `page_token?: string | null`

  - `project_id?: string | null`

  - `status?: "pending" | "processing" | "completed" | 2 more | null`

    Filter by job status (pending, processing, completed, failed, cancelled)

    - `"pending"`

    - `"processing"`

    - `"completed"`

    - `"failed"`

    - `"cancelled"`

### Returns

- `SplitListResponse`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: Array<SplitCategory>`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description?: string | null`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

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

  - `configuration_id?: string | null`

    Split configuration ID used for this job.

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error message if the job failed.

  - `result?: SplitResultResponse | null`

    Result of a completed split job.

    - `segments: Array<SplitSegmentResponse>`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: Array<number>`

        1-indexed page numbers in this split.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const splitListResponse of client.beta.split.list()) {
  console.log(splitListResponse.id);
}
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

`client.beta.split.get(stringsplitJobID, SplitGetParamsquery?, RequestOptionsoptions?): SplitGetResponse`

**get** `/api/v1/beta/split/jobs/{split_job_id}`

Get a document split job.

### Parameters

- `splitJobID: string`

- `query: SplitGetParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `SplitGetResponse`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: Array<SplitCategory>`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description?: string | null`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

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

  - `configuration_id?: string | null`

    Split configuration ID used for this job.

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error message if the job failed.

  - `result?: SplitResultResponse | null`

    Result of a completed split job.

    - `segments: Array<SplitSegmentResponse>`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: Array<number>`

        1-indexed page numbers in this split.

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const split = await client.beta.split.get('split_job_id');

console.log(split.id);
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

- `SplitCategory`

  Category definition for document splitting.

  - `name: string`

    Name of the category.

  - `description?: string | null`

    Optional description of what content belongs in this category.

### Split Document Input

- `SplitDocumentInput`

  Document input specification for beta API.

  - `type: string`

    Type of document input. Valid values are: file_id

  - `value: string`

    Document identifier.

### Split Result Response

- `SplitResultResponse`

  Result of a completed split job.

  - `segments: Array<SplitSegmentResponse>`

    List of document segments.

    - `category: string`

      Category name this split belongs to.

    - `confidence_category: string`

      Categorical confidence level. Valid values are: high, medium, low.

    - `pages: Array<number>`

      1-indexed page numbers in this split.

### Split Segment Response

- `SplitSegmentResponse`

  A segment of the split document.

  - `category: string`

    Category name this split belongs to.

  - `confidence_category: string`

    Categorical confidence level. Valid values are: high, medium, low.

  - `pages: Array<number>`

    1-indexed page numbers in this split.

### Split Create Response

- `SplitCreateResponse`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: Array<SplitCategory>`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description?: string | null`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

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

  - `configuration_id?: string | null`

    Split configuration ID used for this job.

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error message if the job failed.

  - `result?: SplitResultResponse | null`

    Result of a completed split job.

    - `segments: Array<SplitSegmentResponse>`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: Array<number>`

        1-indexed page numbers in this split.

  - `updated_at?: string | null`

    Update datetime

### Split List Response

- `SplitListResponse`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: Array<SplitCategory>`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description?: string | null`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

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

  - `configuration_id?: string | null`

    Split configuration ID used for this job.

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error message if the job failed.

  - `result?: SplitResultResponse | null`

    Result of a completed split job.

    - `segments: Array<SplitSegmentResponse>`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: Array<number>`

        1-indexed page numbers in this split.

  - `updated_at?: string | null`

    Update datetime

### Split Get Response

- `SplitGetResponse`

  Beta response — uses nested document_input object.

  - `id: string`

    Unique identifier for the split job.

  - `categories: Array<SplitCategory>`

    Categories used for splitting.

    - `name: string`

      Name of the category.

    - `description?: string | null`

      Optional description of what content belongs in this category.

  - `document_input: SplitDocumentInput`

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

  - `configuration_id?: string | null`

    Split configuration ID used for this job.

  - `created_at?: string | null`

    Creation datetime

  - `error_message?: string | null`

    Error message if the job failed.

  - `result?: SplitResultResponse | null`

    Result of a completed split job.

    - `segments: Array<SplitSegmentResponse>`

      List of document segments.

      - `category: string`

        Category name this split belongs to.

      - `confidence_category: string`

        Categorical confidence level. Valid values are: high, medium, low.

      - `pages: Array<number>`

        1-indexed page numbers in this split.

  - `updated_at?: string | null`

    Update datetime
