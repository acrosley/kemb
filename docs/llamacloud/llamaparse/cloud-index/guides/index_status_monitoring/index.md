---
title: Index Status Monitoring | Developer Documentation
description: Best practices for monitoring index health and determining when your index is ready to query using file count endpoints
---

This guide covers best practices for monitoring the health and status of your LlamaCloud indexes by using file count endpoints to determine when data is ready for querying.

## Overview

The key to effective index status monitoring is using the file counts endpoint to track the processing status of your documents. By monitoring the number of files in different states (success, error, pending), you can determine:

- Whether your index is ready to serve queries
- If there are processing errors that need attention
- The overall health of your data ingestion pipeline

## Status Resolution Logic

### Index Ready to Query

An index is **ready to query** when it has **one or more files** that have been successfully processed, regardless of whether other files are still pending or in error states:

```
✅ Index Ready Examples:
• 1 file SUCCESS / 0 ERROR / 3 PENDING → Ready to query
• 5 files SUCCESS / 2 ERROR / 0 PENDING → Ready to query
• 10 files SUCCESS / 0 ERROR / 0 PENDING → Ready to query
```

### Index Not Ready

An index is **not ready to query** when no files have been successfully processed:

```
❌ Index Not Ready Examples:
• 0 files SUCCESS / 3 ERROR / 4 PENDING → Not ready (pending processing)
• 0 files SUCCESS / 5 ERROR / 0 PENDING → Not ready (all files failed)
• 0 files SUCCESS / 0 ERROR / 2 PENDING → Not ready (processing in progress)
```

## API Usage

Use the file status counts endpoint to get current statistics:

- [cURL](#tab-panel-95)
- [Python](#tab-panel-96)
- [TypeScript](#tab-panel-97)

Terminal window

```
# Get file counts for a pipeline
curl -X GET "https://cloud.llamaindex.ai/api/v1/pipelines/{pipeline_id}/files/status-counts" \
  -H "Authorization: Bearer your-api-token" \
  -H "Content-Type: application/json"


# Optional: Filter by data source
curl -X GET "https://cloud.llamaindex.ai/api/v1/pipelines/{pipeline_id}/files/status-counts?data_source_id={data_source_id}" \
  -H "Authorization: Bearer your-api-token" \
  -H "Content-Type: application/json"
```

**Example Response:**

```
{
  "counts": {
    "SUCCESS": 3,
    "ERROR": 1,
    "PENDING": 2
  },
  "total_count": 6,
  "pipeline_id": "your-pipeline-id",
  "data_source_id": null,
  "only_manually_uploaded": false
}
```

```
from llama_cloud import LlamaCloud


# Initialize client
client = LlamaCloud(api_key="your-api-key")


def check_index_status(pipeline_id: str) -> dict:
    """Check if index is ready to query and return status info."""


    # Get file counts
    status_counts = client.pipelines.files.get_status_counts(
      pipeline_id=pipeline.id
    )


    success_count = status_counts.counts.get("SUCCESS", 0)
    error_count = status_counts.counts.get("ERROR", 0)
    pending_count = status_counts.counts.get("PENDING", 0)


    # Index is ready if at least 1 file succeeded
    is_ready = success_count > 0


    return {
        "ready_to_query": is_ready,
        "success_files": success_count,
        "error_files": error_count,
        "pending_files": pending_count,
        "total_files": response.total_count,
        "status_message": _get_status_message(success_count, error_count, pending_count)
    }


def _get_status_message(success: int, error: int, pending: int) -> str:
    """Generate human-readable status message."""
    if success > 0:
        if pending > 0:
            return f"Index ready - {success} files available, {pending} still processing"
        elif error > 0:
            return f"Index ready - {success} files available, {error} files failed"
        else:
            return f"Index ready - all {success} files processed successfully"
    else:
        if pending > 0:
            return f"Index not ready - {pending} files still processing"
        elif error > 0:
            return f"Index not ready - all {error} files failed processing"
        else:
            return "Index not ready - no files processed"


# Example usage
status = check_index_status("your-pipeline-id")
print(f"Ready to query: {status['ready_to_query']}")
print(f"Status: {status['status_message']}")
```

```
import { LlamaCloud } from '@llamaindex/llama-cloud';


interface IndexStatus {
  readyToQuery: boolean;
  successFiles: number;
  errorFiles: number;
  pendingFiles: number;
  totalFiles: number;
  statusMessage: string;
}


async function checkIndexStatus(pipelineId: string): Promise<IndexStatus> {
  const client = new LlamaCloud({
    api_key: process.env.LLAMACLOUD_API_KEY
  });


  // Get file status counts
  const statusCounts = await client.pipelines.files.getStatusCounts(pipeline.id);


  const successCount = statusCounts.counts.SUCCESS || 0;
  const errorCount = statusCounts.counts.ERROR || 0;
  const pendingCount = statusCounts.counts.PENDING || 0;


  // Index is ready if at least 1 file succeeded
  const isReady = successCount > 0;


  return {
    readyToQuery: isReady,
    successFiles: successCount,
    errorFiles: errorCount,
    pendingFiles: pendingCount,
    totalFiles: response.totalCount,
    statusMessage: getStatusMessage(successCount, errorCount, pendingCount)
  };
}


function getStatusMessage(success: number, error: number, pending: number): string {
  if (success > 0) {
    if (pending > 0) {
      return `Index ready - ${success} files available, ${pending} still processing`;
    } else if (error > 0) {
      return `Index ready - ${success} files available, ${error} files failed`;
    } else {
      return `Index ready - all ${success} files processed successfully`;
    }
  } else {
    if (pending > 0) {
      return `Index not ready - ${pending} files still processing`;
    } else if (error > 0) {
      return `Index not ready - all ${error} files failed processing`;
    } else {
      return 'Index not ready - no files processed';
    }
  }
}


// Example usage
async function main() {
  try {
    const status = await checkIndexStatus('your-pipeline-id');


    console.log(`Ready to query: ${status.readyToQuery}`);
    console.log(`Status: ${status.statusMessage}`);


    if (status.readyToQuery) {
      // Proceed with queries
      console.log('🟢 Index is ready - you can now run queries!');
    } else {
      // Wait and check again
      console.log('🟡 Index not ready - waiting for processing to complete...');
    }
  } catch (error) {
    console.error('Error checking index status:', error);
  }
}


main();
```

## Advanced Monitoring Patterns

### Polling with Timeout

```
import asyncio
import time
from typing import Optional
from llama_cloud import AsyncLlamaCloud


async def wait_for_index_ready(
    pipeline_id: str,
    timeout_seconds: int = 300,
    poll_interval: int = 10
) -> bool:
    """
    Wait for index to become ready with timeout.


    Returns True if ready within timeout, False otherwise.
    """
    client = AsyncLlamaCloud(api_key="your-api-key")
    start_time = time.time()


    while time.time() - start_time < timeout_seconds:
        try:
            response = await client.pipelines.files.get_status_counts(
                pipeline_id=pipeline_id
            )


            success_count = response.counts.get("SUCCESS", 0)


            if success_count > 0:
                print(f"✅ Index ready! {success_count} files successfully processed")
                return True


            pending_count = response.counts.get("PENDING", 0)
            if pending_count > 0:
                print(f"⏳ Still processing... {pending_count} files pending")


        except Exception as e:
            print(f"Error checking status: {e}")


        await asyncio.sleep(poll_interval)


    print(f"❌ Timeout reached after {timeout_seconds} seconds")
    return False


# Usage
if await wait_for_index_ready("your-pipeline-id", timeout_seconds=600):
    # Start querying
    print("Index is ready for queries!")
else:
    print("Index not ready within timeout period")
```

### Monitoring with Data Source Filtering

```
def check_data_source_status(pipeline_id: str, data_source_id: str) -> dict:
    """Check status for specific data source within a pipeline."""


    client = LlamaCloud(api_key="your-api-key")


    response = client.pipelines.files.get_status_counts(
        pipeline_id=pipeline_id,
        data_source_id=data_source_id
    )


    success_count = response.counts.get("SUCCESS", 0)
    error_count = response.counts.get("ERROR", 0)
    pending_count = response.counts.get("PENDING", 0)


    return {
        "data_source_id": data_source_id,
        "ready_to_query": success_count > 0,
        "success_files": success_count,
        "error_files": error_count,
        "pending_files": pending_count,
        "completion_percentage": (success_count + error_count) / response.total_count * 100 if response.total_count > 0 else 0
    }
```

## Best Practices

1. **Early Availability**: Start querying as soon as any files are processed successfully. Don’t wait for all files to complete.

2. **Error Handling**: Monitor error counts to identify systematic issues with document processing.

3. **Progressive Monitoring**:

   ```
   # Check immediately after upload
   status = check_index_status(pipeline_id)
   if not status['ready_to_query']:
       # Poll periodically until ready
       wait_for_index_ready(pipeline_id)
   ```

4. **User Experience**: Provide clear feedback about processing progress:

   ```
   def get_user_friendly_status(pipeline_id: str) -> str:
       status = check_index_status(pipeline_id)


       if status['ready_to_query']:
           return f"✅ Ready to search! ({status['success_files']} documents available)"
       else:
           pending = status['pending_files']
           if pending > 0:
               return f"⏳ Processing {pending} documents..."
           else:
               return "❌ No documents available for search"
   ```

5. **Rate Limiting**: Don’t poll too frequently - every 5-10 seconds is usually sufficient for status checks.

## Troubleshooting

### High Error Rates

If you see many files in ERROR state:

- Check document formats are supported
- Verify file sizes are within limits
- Review parsing parameters and instructions
- Check for corrupt or password-protected files

### Stuck in PENDING

If files remain PENDING for extended periods:

- Verify your pipeline is deployed and running
- Check for processing queue backlog
- Review pipeline configuration for bottlenecks
- Contact support if processing appears stalled

### No Files Processing

If total\_count is 0:

- Verify files were successfully uploaded
- Check data source configuration and permissions
- Confirm pipeline is properly connected to data sources
