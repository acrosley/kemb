---
title: Index No-code UI Guide | Developer Documentation
description: Step-by-step guide to using the Index no-code UI for creating, managing, and testing indexes and data pipelines.
---

Core workflows for Index via the no-code UI.

## Create new index

Navigate to `Index` feature via the left navbar. ![new pipeline](/_astro/new_pipeline.D4Ow8zN-_Z1XO10Y.png)

Click `Create a new pipeline` button. You should see a index configuration form. ![configure](/_astro/configure.e94fwLyG_Z2f1XUi.png)

### Configure data source

Click `Select a data source` dropdown and select desired data source. ![data source](/_astro/data_source.D7Q7zDzD_Murdv.png)

Specify data source credentials and configurations (or upload files). ![file upload](/_astro/file_upload.eFPLj_OD_Z2wc2BW.png)

See [full list of supported data sources](../../integrations/data_sources)

#### Scheduled sync

If you are using an external data source, you can schedule regular syncs to update changed files and ensure your index is always up to date. The syncs start from the index creation date. To enable scheduled sync, click on the dropdown under the data source details and select a frequency. Only `no scheduled sync`, `6 hours`, `12 hours` and `24 hours` are available. Please contact us if you need more granular syncing options.

![scheduled sync when creating a new index](/_astro/scheduled_sync_creation.BeVPuosH_2klFF8.png)

### Configure data sink

Click `Select a data sink` dropdown and select desired data sink. ![data sink](/_astro/data_sink._ZF17cvC_KT1yI.png)

See [full list of supported data sinks](../../integrations/data_sinks)

### Configure embedding model

Select `OpenAI Embedding` and put in your API key. ![embed model](/_astro/embed_model.WHrOrl4-_Z2dBM73.png)

See [full list of supported embedding models](../../integrations/embedding_models/)

### Configure parsing & transformation settings

Toggle to enable or disable `Llama Parse`.

Select `Auto` mode for best default transformation setting (specify desired chunks size & chunk overlap as necessary.)

`Manual` mode is coming soon, with additional customizability.

![parsing](/_astro/parsing.DPBM_Dv8_wOMaW.png)

See [parsing & transformation details](../../parsing_transformation/)

### Deploy index

After configuring the ingestion pipeline, click `Deploy Index` to kick off ingestion. ![deploy index](/_astro/deploy_index.CSLXiRFl_UCrSC.png)

You should see an index overview with the latest ingestion status. ![index overview](/_astro/index_overview.CAOwFwWz_Z28u5v9.png)

## Manage existing index

### Update files

Navigate to `Data Sources` tab to manage your connected data sources.

You can upsert, delete, download, and preview uploaded files.

![manage files](/_astro/manage_files.DT-llgkp_1QNsO4.png)

### Sync index

Click `Sync` button on the top right to pull upstream changes (data sources & files) and refresh index with the latest content.

### Edit index

Click `Edit` to open up modal for configuring ingestion settings. ![edit](/_astro/edit.CPYWfrUb_Z1DrGlb.png)

### Delete index

Click `Delete` button to remove the index.

Note that this will not delete the uploaded files and previously registered data sources.

### Configure scheduled sync frequency

You can configure the scheduled sync frequency of your data source by going to the `Data Sources`, then scrolling down to the `Connectors` section, and clicking on the `Settings` icon on the right of the data source details.

![data source settings](/_astro/data_source_settings.BtkPhSwY_Z1J61JC.png)

Then, on the modal that pops up, you can select the desired sync frequency.

![data source settings modal](/_astro/data_source_settings_modal.CZWrhQaD_Z21gg6X.png)

For more details on scheduled sync, including how the sync timing works, refer to the [Scheduled sync section](#scheduled-sync) earlier in this page.

## Observe ingestion status & history

Navigate to index overview tab. You should see:

- the latest ingestion status on the `Index Information` card (top right), and
- ingestion job history on the `Activity` card (bottom left). ![index overview](/_astro/index_overview.CAOwFwWz_Z28u5v9.png)

## Test retrieval endpoint

Navigate to `Playground` tab to test your retrieval endpoint.

Select between `Fast`, `Accurate`, and `Advanced` retrieval modes.

- `Fast`: Only dense retrieval
- `Accurate`: Use hybrid search with dense & sparse retrieval and re-ranking
- `Advanced`: Full customizability for tuning hybrid search and re-ranking

Input test query and specify retrieval configurations (e.g. base retrieval and top n after re-ranking) and click `Run` button to see preview for retrieved nodes. ![data source](/_astro/playground.CWCTwTH4_tMk1.png)

Click `Copy` from bottom left panel to make direct REST API calls to the retrieval endpoint.
