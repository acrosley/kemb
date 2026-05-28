---
title: AstraDB | Developer Documentation
---

Configure your own AstraDB instance as data sink.

## Configure via UI

![astradb](/_astro/astradb.NW_IJMJB_2qUhoq.png)

## Configure via API / Client

- [Python](#tab-panel-245)
- [TypeScript](#tab-panel-246)

```
from llama_cloud.types.data_sink_create_params import (
  ComponentCloudAstraDBVectorStore,
)


data_sink = client.data_sinks.create(
    name="my-data-sink",
    component=CloudAstraDBVectorStore(
        token='<astra-db-application-token>',
        api_endpoint='<astra-db-api-endpoint>',
        collection_name='<collection-name>',
        embedding_dimension=1536,  # Length of embedding vectors
        keyspace='<keyspace-name>',  # optional (default: 'default_keyspace')
    ),
    sink_type="ASTRA_DB",
)
```

```
const dataSink = await client.dataSinks.create({
  name: 'my-data-sink',
  component: {
    token: 'my-astra-db-application-token',
    api_endpoint: 'my-astra-db-api-endpoint',
    collection_name: 'my-collection-name',
    embedding_dimension: 1536,
    keyspace: 'my-keyspace',
  },
  sink_type: 'ASTRA_DB',
});
```

## Configuration Parameters

| Parameter             | Type    | Required | Description                                                            |
| --------------------- | ------- | -------- | ---------------------------------------------------------------------- |
| `token`               | string  | Yes      | The Astra DB Application Token to use for authentication               |
| `api_endpoint`        | string  | Yes      | The Astra DB JSON API endpoint for your database                       |
| `collection_name`     | string  | Yes      | Collection name to use. If not existing, it will be created            |
| `embedding_dimension` | integer | Yes      | Length of the embedding vectors in use (e.g., 1536 for OpenAI)         |
| `keyspace`            | string  | No       | The keyspace to use. If not provided, ‘default\_keyspace’ will be used |

## Prerequisites

Before configuring AstraDB as a data sink, ensure you have:

1. **AstraDB Database**: A running AstraDB database instance
2. **Application Token**: An AstraDB Application Token with appropriate permissions
3. **API Endpoint**: The JSON API endpoint URL for your database
4. **Keyspace**: A keyspace in your database (optional, will use ‘default\_keyspace’ if not specified)

## Getting Started with AstraDB

### 1. Create an AstraDB Database

- Visit the [AstraDB Console](https://astra.datastax.com)
- Create a new database or use an existing one
- Note down your database’s API endpoint

### 2. Generate an Application Token

- In the AstraDB Console, navigate to your database
- Go to the “Connect” tab
- Generate an Application Token with the necessary permissions
- Save the token securely

### 3. Configure the Data Sink

Use the token and API endpoint in your data sink configuration as shown in the examples above.

## Filter Syntax

When using AstraDB as a data sink, you can apply filters using standard MongoDB-style query operators:

| Filter Operator | Description            |
| --------------- | ---------------------- |
| `$eq`           | Equals                 |
| `$ne`           | Not equal              |
| `$gt`           | Greater than           |
| `$lt`           | Less than              |
| `$gte`          | Greater than or equal  |
| `$lte`          | Less than or equal     |
| `$in`           | Value is in a list     |
| `$nin`          | Value is not in a list |

These filters can be applied to metadata fields when querying your AstraDB collection to refine search results based on specific criteria.
