---
title: Getting Started | Developer Documentation
description: Introduction to LlamaSheets, a new beta service for extracting regions and tables from spreadsheets.
---

Using a coding agent?

Give your AI agent access to these docs: `claude mcp add llama-index-docs --transport http https://developers.llamaindex.ai/mcp` — [More options](/python/shared/mcp/index.md)

LlamaSheets is a new beta API for extracting regions and tables out of messy spreadsheets. A critical step in document understanding is normalizing inputs. Using the LlamaSheets API, it will

1. Intelligently identify regions per spreadsheet
2. Isolate and extract each region in a spreadsheet
3. Output them as [Parquet files](https://parquet.apache.org/docs/overview/), a portable format supported by many languages that retains type information. For example, you can load these directly as dataframes with Pandas in Python.
4. Generates additional metadata about the regions (extracted location, title, description) and spreadsheets (title, description) to assist in downstream flows.

## Basic Usage

The SDK provides an end-to-end method across multiple API calls to complete the extraction.

- [Python](#tab-panel-40)
- [Typescript](#tab-panel-41)

```
from llama_cloud import LlamaCloud, AsyncLlamaCloud


client = LlamaCloud()


# Upload a spreadsheet
file_obj = client.files.create(file="example_sheet.xlsx", purpose="parse")
file_id = file_obj.id


# Extract tables from the spreadsheet
result = client.beta.sheets.parse(
    file_id=file_id,
    config={
        "generate_additional_metadata": True,
    },
)


# Print extracted regions
print(result.regions)


# Download result parquet files
assert result.regions is not None
for region in result.regions:
    assert region.region_id is not None
    parquet_region_resp = client.beta.sheets.get_result_table(
        region_type=region.region_type,  # type: ignore
        spreadsheet_job_id=result.id,
        region_id=region.region_id,
    )


    url = parquet_region_resp.url
    with httpx.Client() as httpx_client:
        resp = httpx_client.get(url)
        with open(f"./downloaded_region_{region.region_id}.parquet", "wb") as f:
            f.write(resp.content)
        print(f"Downloaded parquet for region {region.region_id}")


    parquet_metadata_resp = client.beta.sheets.get_result_table(
        region_type="cell_metadata",
        spreadsheet_job_id=result.id,
        region_id=region.region_id,
    )


    url = parquet_metadata_resp.url
    with httpx.Client() as httpx_client:
        resp = httpx_client.get(url)
        with open(f"./downloaded_region_{region.region_id}_metadata.parquet", "wb") as f:
            f.write(resp.content)
        print(f"Downloaded parquet metadata for region {region.region_id}")
```

```
import { LlamaCloud } from "@llamaindex/llama-cloud";
import fs from 'fs';


const client = new LlamaCloud();


// Upload a spreadsheet
const fileObj = await client.files.create({
  file: fs.createReadStream('example_sheet.xlsx'),
  purpose: 'parse',
});
const fileId = fileObj.id;


// Extract tables from the spreadsheet
const result = await client.beta.sheets.parse({
  file_id: fileId,
  config: {
    generate_additional_metadata: true,
  },
});


// Print extracted regions
console.log(result.regions);


// Download result parquet files
if (result.regions) {
  for (const region of result.regions) {
    if (region.region_id) {
      const parquetRegionResp = await client.beta.sheets.getResultTable(
        region.region_type as 'table' | 'extra' | 'cell_metadata',
        {
          spreadsheet_job_id: result.id,
          region_id: region.region_id,
        },
      );


      const url = parquetRegionResp.url;
      const response = await fetch(url);
      const buffer = Buffer.from(await response.arrayBuffer());
      fs.writeFileSync(`./downloaded_region_${region.region_id}.parquet`, buffer);
      console.log(`Downloaded parquet for region ${region.region_id}`);


      const parquetMetadataResp = await client.beta.sheets.getResultTable('cell_metadata', {
        spreadsheet_job_id: result.id,
        region_id: region.region_id,
      });


      const metadataUrl = parquetMetadataResp.url;
      const metadataResponse = await fetch(metadataUrl);
      const metadataBuffer = Buffer.from(await metadataResponse.arrayBuffer());
      fs.writeFileSync(`./downloaded_region_${region.region_id}_metadata.parquet`, metadataBuffer);
      console.log(`Downloaded parquet metadata for region ${region.region_id}`);
    }
  }
}
```

### Lower-Level Usage

Using the LlamaSheets API for region and table extraction generally consists of 4 main steps.

Below, we detail each step using both the Python SDK and raw HTTP calls.

#### 1. Upload a File

First, upload a file, and get a File ID:

- [Python SDK](#tab-panel-42)
- [TypeScript](#tab-panel-43)
- [HTTP Calls](#tab-panel-44)

```
from llama_cloud import LlamaCloud, AsyncLlamaCloud


client = LlamaCloud(
    api_key="llx-..."  # Or set LLAMA_CLOUD_API_KEY env var
)


file_obj = client.files.create(file="example_sheet.xlsx", purpose="parse")
file_id = file_obj.id
```

```
import fs from 'fs';
import LlamaCloud from '@llamaindex/llama-cloud';


const client = new LlamaCloud({
  apiKey: process.env.LLAMA_CLOUD_API_KEY!,
});


const file_obj = await client.files.create({
  file: fs.createReadStream('example_sheet.xlsx'),
  purpose: 'parse',
});
const file_id = file_obj.id;
```

Terminal window

```
curl -X POST "https://api.cloud.llamaindex.ai/api/v1/files" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "upload_file=@path/to/your/spreadsheet.xlsx"
```

Response:

```
{
  "id": "file-id-here",
  ...
}
```

#### 2. Create a job

Using the File ID, you can create a job for extraction to get a job ID.

- [Python SDK](#tab-panel-45)
- [TypeScript](#tab-panel-46)
- [HTTP Calls](#tab-panel-47)

```
# Extract tables from the spreadsheet
job = client.beta.sheets.create(
    file_id=file_id,
    config={
        "generate_additional_metadata": True,
    },
)


# Get the job ID
print(job.id)
```

```
// Extract tables from the spreadsheet
const job = await client.beta.sheets.create({
  file_id: file_id,
  config: {
    generate_additional_metadata: true,
  },
});


// Get the job ID
console.log(job.id);
```

Terminal window

```
curl -X POST "https://api.cloud.llamaindex.ai/api/v1/beta/sheets/jobs" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "file_id": "file-id-here",
    "config": {
      "sheet_names": null,
      "generate_additional_metadata": true
    }
  }'
```

Response:

```
{
  "id": "job-id-here",
  "file_id": "file-id-here",
  "status": "PENDING",
  "project_id": "project-id",
  "created_at": "2024-01-01T00:00:00Z",
  ...
}
```

#### 3. Wait for completion

Now that you have a job ID, you can wait for the job to finish:

- [Python SDK](#tab-panel-48)
- [TypeScript](#tab-panel-49)
- [HTTP Calls](#tab-panel-50)

```
# Wait for the job to complete (polls automatically)
while True:
    result = client.beta.sheets.get(spreadsheet_job_id=job.id, include_results=True)
    if result.status != "PENDING":
        break
    print(f"Job status: {result.status}. Waiting...")
    await asyncio.sleep(3)


# Print extracted regions
print(result.regions)


# Access extracted regions metadata
if result.regions:
    print(f"Found {len(result.regions)} region(s)")
    for region in result.regions:
        print(f"  - Region ID: {region.region_id}")
        print(f"    Sheet: {region.sheet_name}")
        print(f"    Location: {region.location}")


for worksheet_metadata in result.worksheet_metadata:
    print(f"Worksheet Title: {worksheet_metadata.title}")
    print(f"Worksheet Description: {worksheet_metadata.description}")
```

```
let result = await client.beta.sheets.get(job.id, { include_results: true });
  while (result.status === 'PENDING') {
    console.log(`Job status: ${result.status}. Waiting...`);
    await new Promise((resolve) => setTimeout(resolve, 3000));
    result = await client.beta.sheets.get(job.id, { include_results: true });
  }


if (result.regions) {
  console.log(`Found ${result.regions.length} region(s):`);
  result.regions.forEach((region) => {
    console.log(`  - Region ID: ${region.region_id}`);
    console.log(`    Sheet: ${region.sheet_name}`);
    console.log(`    Location: ${region.location}`);
  });
}


for (const worksheetMetadata of result.worksheet_metadata || []) {
  console.log(`Worksheet Title: ${worksheetMetadata.title}`);
  console.log(`Worksheet Description: ${worksheetMetadata.description}`);
}
```

Terminal window

```
# Poll for job status
curl -X GET "https://api.cloud.llamaindex.ai/api/v1/beta/sheets/jobs/job-id-here?include_results=true" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response when complete:

```
{
  "id": "job-id-here",
  "status": "SUCCESS",
  "regions": [
    {
      "region_id": "region-id-1",
      "sheet_name": "Sheet1",
      "location": "A1:D10",
      "title": "Sales Data",
      "description": "Monthly sales figures"
    }
  ],
  ...
}
```

Keep polling until `status` is one of: `SUCCESS`, `PARTIAL_SUCCESS`, `ERROR`, or `FAILURE`.

#### 4. Download the result

With a completed job, you can download the generated Parquet file and read any additional metadata about the job result:

- [Python SDK](#tab-panel-51)
- [TypeScript](#tab-panel-52)
- [HTTP Calls](#tab-panel-53)

```
for region in result.regions:
    if result.region_id is None:
        continue


    parquet_region_resp = client.beta.sheets.get_result_table(
        region_type=region.region_type,  # type: ignore
        spreadsheet_job_id=result.id,
        region_id=region.region_id,
    )


    url = parquet_region_resp.url
    with httpx.Client() as httpx_client:
        resp = httpx_client.get(url)
        with open(f"./downloaded_region_{region.region_id}.parquet", "wb") as f:
            f.write(resp.content)
        print(f"Downloaded parquet for region {region.region_id}")


    parquet_metadata_resp = client.beta.sheets.get_result_table(
        region_type="cell_metadata",
        spreadsheet_job_id=result.id,
        region_id=region.region_id,
    )


    url = parquet_metadata_resp.url
    with httpx.Client() as httpx_client:
        resp = httpx_client.get(url)
        with open(f"./downloaded_region_{region.region_id}_metadata.parquet", "wb") as f:
            f.write(resp.content)
        print(f"Downloaded parquet metadata for region {region.region_id}")
```

```
import fs from 'fs';


for (const region of result.regions || []) {
  if (!region.region_id) continue;


  const parquetRegionResp = await client.beta.sheets.getResultTable({
    region_type: region.region_type as any, // type: ignore
    spreadsheet_job_id: result.id,
    region_id: region.region_id,
  });


  const url = parquetRegionResp.url;
  const response = await fetch(url);
  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(`./downloaded_region_${region.region_id}.parquet`, buffer);
  console.log(`Downloaded parquet for region ${region.region_id}`);


  const parquetMetadataResp = await client.beta.sheets.getResultTable({
    region_type: 'cell_metadata',
    spreadsheet_job_id: result.id,
    region_id: region.region_id,
  });


  const metadataUrl = parquetMetadataResp.url;
  const metadataResponse = await fetch(metadataUrl);
  const metadataBuffer = Buffer.from(await metadataResponse.arrayBuffer());
  fs.writeFileSync(`./downloaded_region_${region.region_id}_metadata.parquet`, metadataBuffer);
  console.log(`Downloaded parquet metadata for region ${region.region_id}`);
}
```

Terminal window

```
# Step 1: Get presigned URL for the regino
curl -X GET "https://api.cloud.llamaindex.ai/api/v1/beta/sheets/jobs/job-id-here/regions/region-id-here/result/table" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response:

```
{
  "url": "https://s3.amazonaws.com/...",
  "expires_at": "2024-01-01T01:00:00Z"
}
```

Terminal window

```
# Step 2: Download the parquet file using the presigned URL
curl -X GET "https://s3.amazonaws.com/..." -o region.parquet


# Load with pandas
python -c "import pandas as pd; df = pd.read_parquet('region.parquet'); print(df.head())"
```

To download cell metadata, use `result/cell_metadata` instead of `result/table`:

Terminal window

```
curl -X GET "https://api.cloud.llamaindex.ai/api/v1/beta/sheets/jobs/job-id-here/regions/region-id-here/result/cell_metadata" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Understanding the Output Format

When a LlamaSheets job completes successfully, you receive rich structured data about the extracted regions. This section explains the different components of the output.

### Job Result Structure

The job result object contains:

```
{
  "id": "job-id",
  "status": "SUCCESS",
  "file_id": "original-file-id",
  "config": { /* your parsing config */ },
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:05:00Z",
  "regions": [
    {
      "region_id": "uuid-here",
      "sheet_name": "Sheet1",
      "location": "A2:E11",
      "title": "Some title",
      "description": "Some description"
    }
  ],
  "worksheet_metadata": [
    {
      "sheet_name": "Sheet1",
      "title": "Sales Data Q1 2024",
      "description": "Quarterly sales figures with revenue, units sold, and regional breakdowns"
    }
  ],
  "errors": []
}
```

**Key fields:**

- `regions`: Array of extracted regions and tables with their IDs and locations
- `worksheet_metadata`: Generated titles and descriptions for each sheet (when `generate_additional_metadata: true`)
- `status`: One of `SUCCESS`, `PARTIAL_SUCCESS`, `ERROR`, or `FAILURE`

### Region Table Data (Parquet Files)

Each extracted region is saved as a [Parquet file](https://parquet.apache.org/docs/overview/) containing the normalized table data. Parquet is a columnar storage format that:

- Preserves data types (dates, numbers, strings, booleans)
- Is highly efficient and compressed
- Can be read by pandas, polars, DuckDB, and many other tools

**Example region structure:**

```
import pandas as pd


df = pd.read_parquet("region.parquet")
print(df.head())


# Output:
#    col_0  col_1      col_2       col_3  col_4
# 0     44  -124.6  Value_0_2  2020-01-01  False
# 1    153   -34.4  Value_1_2  2020-01-02   True
# 2    184    34.4  Value_2_2  2020-01-03  False
```

### Cell Metadata (Parquet Files)

In addition to the region data, you can download rich **cell-level metadata** that provides detailed information about each cell in the extracted region. This is particularly useful for:

- Understanding cell formatting and styling
- Analyzing table structure and layout
- Detecting data types and patterns
- Preserving formatting for downstream processing

The following types of fields are available:

**Position & Layout:**

- `row_number`, `column_number`: Cell coordinates
- `coordinate`: Excel-style cell reference (e.g., “A1”)
- `relative_row_position`, `relative_column_position`: Normalized position (0.0 to 1.0)
- `is_in_first_row`, `is_in_last_row`, `is_in_first_column`, `is_in_last_column`: Boolean flags
- `distance_from_origin`, `distance_from_center`: Geometric distances

**Formatting:**

- `font_bold`, `font_italic`: Font style flags
- `font_size`: Font size in points
- `font_color_rgb`, `background_color_rgb`: Color values
- `has_border`, `border_style_score`: Border information
- `horizontal_alignment`, `vertical_alignment`: Alignment values
- `text_wrap`: Text wrapping setting

**Cell Properties:**

- `is_merged_cell`: Whether the cell is part of a merged range
- `horizontal_size`, `vertical_size`: Cell dimensions
- `alignment_indent`: Indentation level

**Data Type Detection:**

- `data_type`: Detected type (Number, Text, Date, etc.)
- `is_date_like`: Boolean flag for date detection
- `is_percentage`, `is_currency`: Boolean flags for special number formats
- `number_format_category`: Excel number format category
- `text_length`: Length of text content
- `has_special_chars`: Whether text contains special characters

**Content:**

- `cell_value`: Processed cell value
- `raw_cell_value`: Original raw value

**Clustering & Grouping:**

- `group`, `sub_group`: Cell grouping identifiers
- `l0_category`, `f_group`: Hierarchical categorization

**Example metadata usage:**

```
import pandas as pd


# Load cell metadata
metadata_df = pd.read_parquet("metadata.parquet")


# Find all header cells (first row)
headers = metadata_df[metadata_df['is_in_first_row'] == True]


# Find all bolded cells (likely headers or emphasis)
bold_cells = metadata_df[metadata_df['font_bold'] == True]


# Find date columns
date_cells = metadata_df[metadata_df['is_date_like'] == True]
date_columns = date_cells['column_number'].unique()


# Analyze formatting patterns
print(f"Font sizes used: {metadata_df['font_size'].unique()}")
print(f"Data types present: {metadata_df['data_type'].unique()}")
```

### Downloading Results

You can download two types of parquet files for each extracted region:

1. **Table data** (`result_type="table"`): The actual table content
2. **Extra data** (`result_type="extra"`): Any region that is not strictly a table of data (notes, titles, etc.)
3. **Cell metadata** (`result_type="cell_metadata"`): Rich formatting and position metadata

All are stored as parquet files and can be easily loaded into pandas DataFrames for analysis.

## Beta Limitations

As part of the beta period, there are a few key limitations to note:

1. Job creation is limited to 1 request per second
2. Sheet size is limited to max 100 columns or 10,000 rows (whichever limit is reached first per-sheet)

## Learn More

Beyond just extracting the regions, there are many downstream use-cases that can wrap these outputs.

- [Use LlamaSheets with a Coding Agent](./examples/coding_agent/)
- [Code your own agent around LlamaSheets](./examples/llama_index/)
