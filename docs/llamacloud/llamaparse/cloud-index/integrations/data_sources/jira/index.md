---
title: Jira Data Source | Developer Documentation
description: Guide to configuring Jira as a data source in LlamaCloud, including UI, API, client setup, and multiple authentication methods.
---

Load data from Jira

## Configure via UI

We can load data by using three different types of authentication methods:

## 1. OAuth2 Authentication Mechanism

![Jira](/_astro/jira_oauth2.Bx6WEz3t_1cXdmE.png)

## 2. PAT Authentication Mechanism

![Jira](/_astro/jira_pat.B1h_1qKn_1xahSD.png)

## 3. Basic Authentication Mechanism

![Jira](/_astro/jira_basic.CymBIH29_wiWlb.png)

## Configure via API / Client

#### 1. OAuth2 Authentication Mechanism

- [Python](#tab-panel-299)
- [TypeScript](#tab-panel-300)
- [Python (legacy)](#tab-panel-301)
- [TypeScript (legacy)](#tab-panel-302)

```
from llama_cloud.types.data_source_create_params import (
  CloudJiraDataSource,
)


data_source = client.data_sources.create(
    name="my-data-source",
    component=CloudJiraDataSource(
        api_token='<api_token>',  # Access token in this case
        cloud_id='<cloud_id>',
        authentication_mechanism='oauth2',
        query='<query>',
    ),
    source_type="JIRA",
    project_id="my-project-id",
)
```

```
const dataSource = await client.dataSources.create({
  name: 'my-data-source',
  component: {
    api_token: '<api_token>',  // Access token in this case
    cloud_id: '<cloud_id>',
    authentication_mechanism: 'oauth2',
    query: '<query>',
  },
  source_type: 'JIRA',
  project_id: 'my-project-id',
});
```

```
from llama_cloud.types import CloudJiraDataSource


ds = {
    'name': '<your-name>',
    'source_type': 'JIRA',
    'component': CloudJiraDataSource(
        api_token='<api_token>',  # Access token in this case
        cloud_id='<cloud_id>',
        authentication_mechanism='oauth2',
        query='<query>',
    )
}
data_source = client.data_sources.create_data_source(request=ds)
```

```
const ds = {
    'name': '<your-name>',
    'sourceType': 'JIRA',
    'component': {
        'api_token': '<api_token>',  // Access token in this case
        'cloud_id': '<cloud_id>',
        'authentication_mechanism': 'oauth2',
        'query': '<query>',
    }
};


const dataSource = await client.dataSources.createDataSource({
  body: ds
});
```

#### 2. PAT Authentication Mechanism

- [Python](#tab-panel-303)
- [TypeScript](#tab-panel-304)
- [Python (legacy)](#tab-panel-305)
- [TypeScript (legacy)](#tab-panel-306)

```
from llama_cloud.types.data_source_create_params import (
  CloudJiraDataSource,
)


data_source = client.data_sources.create(
    name="my-data-source",
    component=CloudJiraDataSource(
        api_token='<api_token>',  # Personal Access Token (PAT) in this case
        server_url='<server_url>',
        authentication_mechanism='pat',
        query='<query>',
    ),
    source_type="JIRA",
    project_id="my-project-id",
)
```

```
const dataSource = await client.dataSources.create({
  name: 'my-data-source',
  component: {
    api_token: '<api_token>',  // Personal Access Token (PAT) in this case
    server_url: '<server_url>',
    authentication_mechanism: 'pat',
    query: '<query>',
  },
  source_type: 'JIRA',
  project_id: 'my-project-id',
});
```

```
from llama_cloud.types import CloudJiraDataSource


ds = {
    'name': '<your-name>',
    'source_type': 'JIRA',
    'component': CloudJiraDataSource(
        api_token='<api_token>',  # Personal Access Token (PAT) in this case
        server_url='<server_url>',
        authentication_mechanism='pat',
        query='<query>',
    )
}
data_source = client.data_sources.create_data_source(request=ds)
```

```
const ds = {
    'name': '<your-name>',
    'sourceType': 'JIRA',
    'component': {
        'api_token': '<api_token>',  // Personal Access Token (PAT) in this case
        'server_url': '<server_url>',
        'authentication_mechanism': 'pat',
        'query': '<query>',
    }
};


const dataSource = await client.dataSources.createDataSource({
  body: ds
});
```

#### 3. Basic Authentication Mechanism

- [Python](#tab-panel-307)
- [TypeScript](#tab-panel-308)
- [Python (legacy)](#tab-panel-309)
- [TypeScript (legacy)](#tab-panel-310)

```
from llama_cloud.types.data_source_create_params import (
  CloudJiraDataSource,
)


data_source = client.data_sources.create(
    name="my-data-source",
    component=CloudJiraDataSource(
        email='<email>',
        api_token='<api_token>',
        server_url='<server_url>',
        authentication_mechanism='basic',
        query='<query>',
    ),
    source_type="JIRA",
    project_id="my-project-id",
)
```

```
const dataSource = await client.dataSources.create({
  name: 'my-data-source',
  component: {
    email: '<email>',
    api_token: '<api_token>',
    server_url: '<server_url>',
    authentication_mechanism: 'basic',
    query: '<query>',
  },
  source_type: 'JIRA',
  project_id: 'my-project-id',
});
```

```
from llama_cloud.types import CloudJiraDataSource


ds = {
    'name': '<your-name>',
    'source_type': 'JIRA',
    'component': CloudJiraDataSource(
        email='<email>',
        api_token='<api_token>',
        server_url='<server_url>',
        authentication_mechanism='basic',
        query='<query>',
    )
}
data_source = client.data_sources.create_data_source(request=ds)
```

```
const ds = {
    'name': '<your-name>',
    'sourceType': 'JIRA',
    'component': {
        'email': '<email>',
        'api_token': '<api_token>',
        'server_url': '<server_url>',
        'authentication_mechanism': 'basic',
        'query': '<query>',
    }
};


const dataSource = await client.dataSources.createDataSource({
  body: ds
});
```
