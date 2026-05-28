---
title: Getting Started | Developer Documentation
description: Step-by-step guide to building a RAG application with Index, including index setup, configuration, and integration with your application.
---

Using a coding agent?

Give your AI agent access to these docs: `claude mcp add llama-index-docs --transport http https://developers.llamaindex.ai/mcp` — [More options](/python/shared/mcp/index.md)

## Overview

Index is part of the LlamaCloud platform (which includes LlamaParse, LlamaExtract, LlamaAgents, and other products). It makes it easy to set up a highly scalable & customizable data ingestion pipeline for your RAG use case. No need to worry about scaling challenges, document management, or complex file parsing.

Index offers all of this through a no-code UI, REST API / clients, and seamless integration with our popular python & typescript framework.

Connect your index to your [data sources](../integrations/data_sources/), set your parse parameters & embedding model, and the index automatically handles syncing your data into your [vector databases](../integrations/data_sinks/). From there, we offer an easy-to-use interface to query your indexes and retrieve relevant ground truth information from your input documents.

Index v1 availability

Index v1 is only available for projects that already have existing index pipelines. If your project does not have any existing pipelines, the Index feature will not appear in the navigation. New projects should use the API/SDK to manage pipelines programmatically.

## Prerequisites

1. [Sign up for an account](https://cloud.llamaindex.ai)
2. Prepare an API key for your preferred embedding model service (e.g. OpenAI).

## Sign in

Sign in via <https://cloud.llamaindex.ai/>

You should see options to sign in via Google, Github, Microsoft, or email.

![sign-in](/_astro/login.BlvlZg95_ZeW2ar.png)

## Set up an index via UI

Navigate to `Index` feature via the left navbar. ![new pipeline](/_astro/new_index.CS9YbmGb_ZY0fLl.png)

Click the `Create Index` button. You should see a index configuration form. ![configure](/_astro/configure.e94fwLyG_Z2f1XUi.png)

Configure data source - file upload

Click `Select a data source` dropdown and select `Files` ![data source](/_astro/data_source.D7Q7zDzD_Murdv.png)

Drag files into file pond or `click to browse`. ![file upload](/_astro/file_upload.eFPLj_OD_Z2wc2BW.png)

[See full list of data sources and specifications](../integrations/data_sources/)

Configure data sink - managed

Select `Fully Managed` data sink. ![data source](/_astro/data_sink._ZF17cvC_KT1yI.png)

[See full list of data sinks and specifications](../integrations/data_sinks/)

Configure embedding model - OpenAI

Select `OpenAI Embedding` and put in your API key. ![embed model](/_astro/embed_model.DbJv8EHi_Z1LTl9V.png)

See [full list of supported embedding models](../integrations/embedding_models/)

Configure parsing & transformation settings

Toggle to enable or disable `Llama Parse`.

Select `Auto` mode for best default transformation setting (specify desired chunks size & chunk overlap as necessary.)

`Manual` mode is coming soon, with additional customizability.

![data source](/_astro/parsing.DPBM_Dv8_wOMaW.png)

[More details about parsing & transformation settings](../parsing_transformation/).

After configuring the ingestion pipeline, click `Deploy Index` to kick off ingestion. ![deploy index](/_astro/deploy_index.CSLXiRFl_UCrSC.png)

## (Optional) Observe and manage your index via UI

You should see an index overview with the latest ingestion status. ![index overview](/_astro/index_overview.CAOwFwWz_Z28u5v9.png)

(optional) Test retrieval via playground

Navigate to `Playground` tab to test your retrieval endpoint.

Select between `Fast`, `Accurate`, and `Advanced` retrieval modes. Input test query and specify retrieval configurations (e.g. base retrieval and top n after re-ranking). ![data source](/_astro/playground.CWCTwTH4_tMk1.png)

(optional) Manage connected data sources (or uploaded files)

Navigate to `Data Sources` tab to manage your connected data sources.

You can upsert, delete, download, and preview uploaded files.

![manage files](/_astro/manage_files.DT-llgkp_1QNsO4.png)

## Integrate your retrieval endpoint into RAG/agent application

After setting up the index, we can now integrate the retrieval endpoint into our RAG/agent application. Here, we will use a colab notebook as example.

Obtain LlamaCloud API key

Navigate to `API Key` page from left sidebar. Click `Generate New Key` button. ![api key](/_astro/api_keys.DwipGkM3_ZfSkud.png)

Copy the API key to safe location. You will not be able to retrieve this again. [More detailed walkthrough](../../general/api_key/).

Setup your RAG/agent application - python notebook

Install latest python framework:

```
pip install llama-index
```

[See detail instructions](https://docs.llamaindex.ai/en/stable/getting_started/installation/)

Navigate to `Overview` tab. Click `Copy` button under `Retrieval Endpoint` card ![retrieval endpoint](/_astro/retrieval_endpoint.DMb0uUqx_Z1K90nx.png)

Now you have a minimal RAG application ready to use! ![colab example](/_astro/colab_example.B8MWqaOK_X25r4.png)

You can find demo colab notebook [here](https://colab.research.google.com/drive/19s2rLBOnLGmdEbXYxCDsUJ1xHQMkpRUD?usp=sharing).
