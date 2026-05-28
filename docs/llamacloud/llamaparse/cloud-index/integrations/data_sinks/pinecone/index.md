---
title: Pinecone | Developer Documentation
---

Configure your own Pinecone instance as data sink.

## Configure via UI

![pinecone](/_astro/pinecone.DdUUu4UX_1vvLYp.png)

## Configure via API / Client

- [Python](#tab-panel-261)
- [TypeScript](#tab-panel-262)
- [Python (legacy)](#tab-panel-263)
- [TypeScript (legacy)](#tab-panel-264)

```
from llama_cloud.types.data_sink_create_params import (
  CloudPineconeVectorStore,
)


data_sink = client.data_sinks.create(
    name="my-data-sink",
    component=CloudPineconeVectorStore(
        api_key='<api_key>',
        index_name='<index_name>',
        name_space='<name_space>',  # optional
        insert_kwargs='<insert_kwargs>'  # optional
    ),
    sink_type="PINECONE",
)
```

```
const dataSink = await client.dataSinks.create({
  name: 'my-data-sink',
  component: {
    api_key: '<api_key>',
    index_name: '<index_name>',
    name_space: '<name_space>',  // optional
    insert_kwargs: '<insert_kwargs>'  // optional
  },
  sink_type: 'PINECONE',
});
```

```
  from llama_cloud.types import CloudPineconeVectorStore


  ds = {
      'name': '<your-name>',
      'sink_type': 'PINECONE',
      'component': CloudPineconeVectorStore(
          api_key='<api_key>',
          index_name='<index_name>',
          name_space='<name_space>',  # optional
          insert_kwargs='<insert_kwargs>'  # optional
      )
  }
  data_sink = client.data_sinks.create_data_sink(request=ds)
```

```
const ds = {
    'name': 'pinecone',
    'sinkType': 'PINECONE',
    'component': {
        'api_key': '<api_key>',
        'index_name': '<index_name>',
        'name_space': '<name_space>',  // optional
        'insert_kwargs': '<insert_kwargs>'  // optional
    }
}


data_sink = await client.dataSinks.createDataSink({
  projectId: projectId,
  body: ds
})
```

## Filter Syntax

When using Pinecone as a data sink, you can apply filters using the following syntax:

| Filter Operator | Pinecone Equivalent | Description            |
| --------------- | ------------------- | ---------------------- |
| `==`            | `$eq`               | Equals                 |
| `!=`            | `$ne`               | Not equal              |
| `>`             | `$gt`               | Greater than           |
| `<`             | `$lt`               | Less than              |
| `>=`            | `$gte`              | Greater than or equal  |
| `<=`            | `$lte`              | Less than or equal     |
| `in`            | `$in`               | Value is in a list     |
| `nin`           | `$nin`              | Value is not in a list |

These filters can be applied to metadata fields when querying your Pinecone index to refine search results based on specific criteria.
