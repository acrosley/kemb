---
title: Microsoft OneDrive Data Source | Developer Documentation
description: Guide to configuring Microsoft OneDrive as a data source in LlamaCloud, including UI, API, and client setup.
---

Load data from Microsoft OneDrive

## Configure via UI

![OneDrive](/_astro/one_drive.CcMwidaw_1eafh4.png)

## Configure via API / Client

- [Python](#tab-panel-311)
- [TypeScript](#tab-panel-312)
- [Python (legacy)](#tab-panel-313)
- [TypeScript (legacy)](#tab-panel-314)

```
from llama_cloud.types.data_source_create_params import (
  CloudOneDriveDataSource,
)


data_source = client.data_sources.create(
    name="my-data-source",
    component=CloudOneDriveDataSource(
        user_principal_name='<user_principal_name>',
        folder_path='<folder_path>',  # optional
        folder_id='<folder_id>',  # optional
        client_id='<client_id>',
        client_secret='<client_secret>',
        tenant_id='<tenant_id>',
    ),
    source_type="MICROSOFT_ONEDRIVE",
    project_id="my-project-id",
)
```

```
const dataSource = await client.dataSources.create({
  name: 'my-data-source',
  component: {
    user_principal_name: '<user_principal_name>',
    folder_path: '<folder_path>',  // optional
    folder_id: '<folder_id>',  // optional
    client_id: '<client_id>',
    client_secret: '<client_secret>',
    tenant_id: '<tenant_id>',
  },
  source_type: 'MICROSOFT_ONEDRIVE',
  project_id: 'my-project-id',
});
```

```
from llama_cloud.types import CloudOneDriveDataSource


ds = {
    'name': '<your-name>',
    'source_type': 'MICROSOFT_ONEDRIVE',
    'component': CloudOneDriveDataSource(
        user_principal_name='<user_principal_name>',
        folder_path='<folder_path>',  # optional
        folder_id='<folder_id>',  # optional
        client_id='<client_id>',
        client_secret='<client_secret>',
        tenant_id='<tenant_id>',
    )
}
data_source = client.data_sources.create_data_source(request=ds)
```

```
const ds = {
    name: '<your-name>',
    sourceType: 'MICROSOFT_ONEDRIVE',
    component: {
        userPrincipalName: '<user_principal_name>',
        folderPath: '<folder_path>',  // optional
        folderId: '<folder_id>',  // optional
        clientId: '<client_id>',
        clientSecret: '<client_secret>',
        tenantId: '<tenant_id>',
    }
};


const dataSource = await client.dataSources.createDataSource({
  body: ds
});
```
