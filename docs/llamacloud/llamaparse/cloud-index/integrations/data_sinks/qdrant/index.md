---
title: Qdrant | Developer Documentation
---

Configure your own Qdrant instance as data sink.

## Configure via UI

![qdrant](/_astro/qdrant.TSaQsni9_Z1yqV2C.png)

## Configure via API / Client

- [Python](#tab-panel-267)
- [TypeScript](#tab-panel-268)
- [Python (legacy)](#tab-panel-269)
- [TypeScript (legacy)](#tab-panel-270)

```
from llama_cloud.types.data_sink_create_params import (
  CloudQdrantVectorStore,
)


data_sink = client.data_sinks.create(
    name="my-data-sink",
    component=CloudQdrantVectorStore(
        api_key='<api_key>',
        collection_name='<collection_name>',
        url='<url>',
        max_retries='<max_retries>',  # optional
        client_kwargs='<client_kwargs>'  # optional
    ),
    sink_type="QDRANT",
)
```

```
const dataSink = await client.dataSinks.create({
  name: 'my-data-sink',
  component: {
    api_key: '<api_key>',
    collection_name: '<collection_name>',
    url: '<url>',
    max_retries: '<max_retries>',  // optional
    client_kwargs: '<client_kwargs>'  // optional
  },
  sink_type: 'QDRANT',
});
```

```
from llama_cloud.types import CloudQdrantVectorStore


ds = {
    'name': '<your-name>',
    'sink_type': 'QDRANT',
    'component': CloudQdrantVectorStore(
        api_key='<api_key>',
        collection_name='<collection_name>',
        url='<url>',
        max_retries='<max_retries>',  # optional
        client_kwargs='<client_kwargs>'  # optional
    )
}
data_sink = client.data_sinks.create_data_sink(request=ds)
```

```
const ds = {
    'name': 'qdrant',
    'sinkType': 'QDRANT',
    'component': {
        'api_key': '<api_key>',
        'collection_name': '<collection_name>',
        'url': '<url>',
        'max_retries': '<max_retries>',  // optional
        'client_kwargs': '<client_kwargs>'  // optional
    }
}


data_sink = await client.dataSinks.createDataSink({
  projectId: projectId,
  body: ds
})
```
