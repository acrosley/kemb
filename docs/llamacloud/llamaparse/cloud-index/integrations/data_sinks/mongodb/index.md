---
title: MongoDB Atlas Vector Search | Developer Documentation
---

Configure your own MongoDB Atlas instance as data sink.

## Configure via UI

![mongodb](/_astro/mongodb.BZQZqT8y_pALpQ.png)

## Configure via API / Client

- [Python](#tab-panel-257)
- [TypeScript](#tab-panel-258)
- [Python (legacy)](#tab-panel-259)
- [TypeScript (legacy)](#tab-panel-260)

```
from llama_cloud.types.data_sink_create_params import (
  CloudMongoDBAtlasVectorSearch,
)


data_sink = client.data_sinks.create(
    name="my-data-sink",
    component=CloudMongoDBAtlasVectorSearch(
        mongodb_uri='<database-connection-uri>',
        db_name='<database-name>',
        collection_name='<collection-name>',
        vector_index_name='<vector-search-index>',  # optional (default: vector_index)
        fulltext_index_name='<full-text-index>',  # optional (default: fulltext_index)
    ),
    sink_type="MONGODB_ATLAS",
)
```

```
const dataSink = await client.dataSinks.create({
  name: 'my-data-sink',
  component: {
    mongodb_uri: '<database-connection-uri>',
    db_name: '<database-name>',
    collection_name: '<collection-name>',
    vector_index_name: '<vector-search-index>',  // optional (default: vector_index)
    fulltext_index_name: '<full-text-index>',  // optional (default: fulltext_index)
  },
  sink_type: 'MONGODB_ATLAS',
});
```

```
  from llama_cloud.types import CloudAzureAISearchVectorStore


  ds = {
      'name': '<your-name>',
      'sink_type': 'MONGODB_ATLAS',
      'component': CloudMongoDBAtlasVectorSearch(
          mongodb_uri='<database-connection-uri>',
          db_name='<database-name>',
          collection_name='<collection-name>',
          vector_index_name='<vector-search-index>',  # optional (default: vector_index)
          fulltext_index_name='<full-text-index>',  # optional (default: fulltext_index)
      )
  }
  data_sink = client.data_sinks.create_data_sink(request=ds)
```

```
  const ds = {
      'name': 'mongodbatlas',
      'sinkType': 'MONGODB_ATLAS',
      'component': {
          'mongodb_uri': '<database-connection-uri>',
          'db_name': '<database-name>',
          'collection_name': '<collection-name>',
          'vector_index_name': '<vector-search-index>',  // optional (default: vector_index)
          'fulltext_index_name': '<full-text-index>',  // optional (default: fulltext_index)
      }
  }


  data_sink = await client.dataSinks.createDataSink({
    projectId: projectId,
    body: ds
  })
```

**Note:** Database and Collection should already be created in MongoDB Atlas, and an Atlas Vector Search index should be created on the `embedding` field, as well as filters on the `metadata.pipeline_id`, and `metadata.doc_id` fields for retrieval, before configuring the Data Sink. The process on how to create it is explained [here](#how-to-index-fields-for-vector-search).

## How to Index Fields for Vector Search

This section demonstrates how to create the index on the fields in the `sample_mflix.embedded_movies` collection:

- An Atlas Vector Search index on the `embedding` field for running vector queries against it, as well as filters on the `metadata.pipeline_id`, and `metadata.doc_id` fields.

### Required Access

To create Atlas Vector Search and Atlas Search indexes, you must have at least Project Data Access Admin access to the project.

### Procedure

#### 1. In Atlas, go to the Clusters page for your project.

- If it’s not already displayed, select the organization that contains your desired project from the Organizations menu in the navigation bar.
- If it’s not already displayed, select your desired project from the Projects menu in the navigation bar.
- If the Clusters page is not already displayed, click Database in the sidebar.

#### 2. Go to the Atlas Search page for your cluster.

You can go to the Atlas Search page from the sidebar, the Data Explorer, or your cluster details page.

- **Sidebar**: In the sidebar, click Atlas Search under the Services heading.
- **Data Explorer**: From the Select data source dropdown, select your cluster and click Go to Atlas Search.
- **Cluster Details**: Click Create Index.

#### 3. Define the Atlas Vector Search index.

- Click Create Search Index.
- Under Atlas Vector Search, select JSON Editor and then click Next.
- In the Database and Collection section, find the `sample_mflix` database, and select the `embedded_movies` collection.
- In the Index Name field, enter `vector_index`.
- Replace the default definition with the following index definition and then click Next:

Syntax:

```
{
  "fields":[
    {
      "type": "vector",
      "path": "<embedding_key>",
      "numDimensions": "<number-of-dimensions>",
      "similarity": "euclidean | cosine | dotProduct"
    },
    {
      "type": "filter",
      "path": "<metadata_key.pipeline_id_key>"
    },
    {
      "type": "filter",
      "path": "<metadata_key.doc_id_key>"
    }
  ]
}
```

Example:

```
{
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 1536,
      "similarity": "euclidean"
    },
    {
      "type": "filter",
      "path": "metadata.pipeline_id"
    },
    {
      "type": "filter",
      "path": "metadata.doc_id"
    }
  ]
}
```

- Review the index definition and then click Create Search Index. A modal window displays to let you know that your index is building.

- Click Close to close the You’re All Set! modal window and wait for the index to finish building. The index should take about one minute to build. While it builds, the Status column reads Initial Sync. When it finishes building, the Status column reads Active.

- [More Details](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-type)
