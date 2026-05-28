---
title: Box Storage Data Source | Developer Documentation
description: Guide to configuring Box Storage as a data source in LlamaCloud, including UI, API, client setup, and authentication methods.
---

Load data from Box Storage.

## Configure via UI

We can load data from Box using one of two different types of authentication, either a Developer Token or a Client Credential Grant.

## 1. Developer Token Authentication Mechanism

Developer Tokens are short lived and can be created in the [Box Developer Console](https://developer.box.com/).

![box](/_astro/box_dev.BYEVmBK2_ZYgjCV.png)

## 2. Client Credential Grant Authentication Mechanism

These credentials can be used to access Box data for a specific user or an entire enterprise and are longer-lived than Developer Tokens. You can use either an Enterprise ID or a User ID to authenticate.

### Setting up Box CCG Credentials

1. Log in to your Box account / Create a Box developer account and navigate to the developer console.
2. Create a new custom app.
3. Select “Server Authentication (Client Credentials Grant)” as the authentication method.
4. Under “App Access Level”, select `App + Enterprise Access`.
5. We recommend giving your app all permissions, as shown: ![box](/_astro/box_scopes.Sf-38HOg_Z1zTrji.png)
6. Save your changes and submit the app for authorization.
7. Open the [Box Admin console](https://app.box.com/master/custom-apps). As an admin, authorize the app in the Custom Apps Manager.
8. Once the app is enabled, get your `User ID`, `Enterprise ID`, `Client ID` and `Client Secret` from app console in developer console.

### 1. Client Credential Grant Authentication Mechanism using an Enterprise ID

Note that to access files via an Enterprise ID, they need to have been shared with that app. You can share files with an app by its email address, which can be found in the Developer Console under “Service Account Info”.

![box](/_astro/box_ccg_enterprise.DmxqbGYS_ZsFnsD.png)

### 2. Client Credential Grant Authentication Mechanism using a User ID

If you are using a User ID, you can access files that have been shared with or created by that user. This will be the user ID of the person who created the app.

![box](/_astro/box_ccg_user.CTNZbuNx_Z15bD2z.png)

## Configure via API / Client

#### 1. Developer Token Authentication Mechanism

- [Python](#tab-panel-271)
- [TypeScript](#tab-panel-272)
- [Python (legacy)](#tab-panel-273)
- [TypeScript (legacy)](#tab-panel-274)

```
from llama_cloud.types.data_source_create_params import (
  CloudBoxDataSource,
)


data_source = client.data_sources.create(
    name="my-data-source",
    component=CloudBoxDataSource(
        folder_id='<folder_id>',  # optional
        developer_token='<token>',  # Developer Tokens are short lived
    ),
    source_type="BOX",
    project_id="my-project-id",
)
```

```
const dataSource = await client.dataSources.create({
  name: 'my-data-source',
  component: {
    folder_id: '<folder_id>',  // optional
    developer_token: '<token>',  // Developer Tokens are short lived
  },
  source_type: 'BOX',
  project_id: 'my-project-id',
});
```

```
from llama_cloud.types import CloudBoxDataSource


ds = {
    'name': '<your-name>',
    'source_type': 'BOX',
    'component': CloudBoxDataSource(
        folder_id='<folder_id>',  # optional
        developer_token='<token>',  # Developer Tokens are short lived
    )
}
data_source = client.data_sources.create_data_source(request=ds)
```

```
const ds = {
    'name': '<your-name>',
    'sourceType': 'BOX',
    'component': {
        'folder_id': '<folder_id>',  // optional
        'developer_token': '<token>',  // Developer Tokens are short lived
    }
}


data_source = await client.dataSources.createDataSource({
  body: ds
})
```

#### 2. Client Credential Grant Authentication Mechanism

- [Python](#tab-panel-275)
- [TypeScript](#tab-panel-276)
- [Python (legacy)](#tab-panel-277)
- [TypeScript (legacy)](#tab-panel-278)

```
from llama_cloud.types.data_source_create_params import (
  CloudBoxDataSource,
)


data_source = client.data_sources.create(
    name="my-data-source",
    component=CloudBoxDataSource(
        folder_id='<folder_id>',  # optional
        client_id='<client_id>',
        client_secret='<client_secret>',
        user_id='<user_id>',  # optional, if using enterprise_id
        enterprise_id='<enterprise_id>'  # optional, if using user_id
    ),
    source_type="BOX",
    project_id="my-project-id",
)
```

```
const dataSource = await client.dataSources.create({
  name: 'my-data-source',
  component: {
    folder_id: '<folder_id>',  // optional
    client_id: '<client_id>',
    client_secret: '<client_secret>',
    user_id: '<user_id>',  // optional, if using enterprise_id
    enterprise_id: '<enterprise_id>'  // optional, if using user_id
  },
  source_type: 'BOX',
  project_id: 'my-project-id',
});
```

```
from llama_cloud.types import CloudBoxDataSource


ds = {
    'name': '<your-name>',
    'source_type': 'BOX',
    'component': CloudBoxDataSource(
        folder_id='<folder_id>',  # optional
        client_id='<client_id>',
        client_secret='<client_secret>',
        user_id='<user_id>',  # optional, if using enterprise_id
        enterprise_id='<enterprise_id>'  # optional, if using user_id
    )
}
data_source = client.data_sources.create_data_source(request=ds)
```

```
const ds = {
    'name': '<your-name>',
    'sourceType': 'BOX',
    'component': {
        'folder_id': '<folder_id>',  // optional
        'client_id': '<client_id>',
        'client_secret': '<client_secret>',
        'user_id': '<user_id>',  // optional, if using enterprise_id
        'enterprise_id': '<enterprise_id>'  // optional, if using user_id
    }
}


data_source = await client.dataSources.createDataSource({
  body: ds
})
```
