---
title: Glossary | Developer Documentation
description: Definitions of key terms and concepts used across LlamaParse products and documentation.
---

Quick reference for terms used throughout the LlamaParse documentation.

### Agent (LlamaAgents)

An AI agent workflow that uses LlamaParse products (Parse, Extract, Index) as tools to process documents autonomously. Not to be confused with product-specific agents like the extraction agent. Currently in beta.

### Agentic (tier)

A [Parse](/llamaparse/parse/getting_started/index.md) tier (10 credits/page) that uses AI agents for complex document understanding, handling tables, charts, and mixed layouts.

### Agentic Plus (tier)

The highest [Parse](/llamaparse/parse/getting_started/index.md) tier (45 credits/page) for the most complex documents requiring multi-pass agent processing.

### API Key

A secret token used to authenticate requests to LlamaParse APIs. Managed at [API Keys](/llamaparse/general/api_key/index.md).

### BYOC (Bring Your Own Cloud)

A deployment model where LlamaParse runs within your own cloud infrastructure for data sovereignty and compliance. Available on Enterprise plans — [contact us](https://www.llamaindex.ai/contact). See [Self-Hosting (BYOC)](/python/cloud/self_hosting/index.md) for details.

### Chunk

A segment of a parsed document, created during indexing. Chunks are embedded and stored for retrieval in RAG workflows.

### Classification Rule

A named category with a description used by Classify to sort documents. See [Classify](/llamaparse/classify/getting_started/index.md).

### Classify

A service that classifies documents into user-defined categories. Formerly LlamaClassify. See [Classify](/llamaparse/classify/getting_started/index.md).

### Cost-effective (tier)

A [Parse](/llamaparse/parse/getting_started/index.md) tier (3 credits/page) using LLM-based parsing. Optimized for speed and cost, best for text-heavy documents with minimal structure.

### Credit

The billing unit for LlamaParse. All operations consume credits based on pages processed, mode, and model. See [Pricing](/llamaparse/general/pricing/index.md).

### Data Sink

A destination where indexed data is stored (e.g., a managed vector store or external database like MongoDB or Pinecone).

### Data Source

An origin from which LlamaParse ingests files for indexing (e.g., S3, Google Drive, SharePoint, Confluence).

### Embedding

A numerical vector representation of text, generated during indexing for similarity search in RAG pipelines.

### Extract

A service that extracts structured data from documents using user-defined schemas. Formerly LlamaExtract. See [Extract](/llamaparse/extract/getting_started/index.md).

### Extraction Schema

A JSON schema defining the structured fields to extract from documents using Extract. See [Schema Design](/llamaparse/extract/guides/schema_design/index.md).

### Fast (tier)

The cheapest [Parse](/llamaparse/parse/getting_started/index.md) tier (1 credit/page). Outputs spatial text only (not markdown). Best when you need raw text extraction without AI processing.

### Index

A searchable collection of parsed and embedded document chunks, used for RAG retrieval. See [LlamaCloud Index](/llamaparse/cloud-index/getting_started/index.md).

### Job

An asynchronous processing task (parse, extract, classify, or split). Jobs can be polled for status or monitored via webhooks.

### Multimodal

A processing mode that uses vision models to understand both text and visual content (images, charts, diagrams).

### OCR (Optical Character Recognition)

The process of extracting text from images or scanned documents. Used automatically when needed during parsing.

### Organization

The top-level account unit in LlamaParse. Billing and members are scoped to an organization. Organizations contain one or more [projects](#project).

### Page

The base billing unit. For documents, one page equals one document page. For text files, one page equals approximately 600 tokens. For audio, billing is per minute.

### Parse

The core document parsing service supporting 130+ file formats. Converts documents to markdown, text, or structured output. The parsing product within the LlamaParse platform. See [Parse](/llamaparse/parse/getting_started/index.md).

### Pipeline

An indexing pipeline that defines how documents are ingested, parsed, chunked, embedded, and stored in an index.

### Project

A workspace within an organization for organizing files, jobs, indexes, and API keys.

### RAG (Retrieval Augmented Generation)

A pattern where relevant document chunks are retrieved from an index and provided as context to an LLM for answering questions.

### Sheets

A spreadsheet-based interface for document processing. Formerly LlamaSheets. Currently in beta.

### Split

A service that splits documents into categorized sections based on content. See [Split](/llamaparse/split/getting_started/index.md).

### Tier

A parsing quality level in Parse v2 (Fast, Cost-effective, Agentic, Agentic Plus) that determines the processing approach and credit cost.

### Vector Store

A database optimized for storing and searching embeddings. LlamaParse supports managed stores and external options (Pinecone, Qdrant, etc.).

### Webhook

An HTTP callback that notifies your application when a job completes or changes status. See [Webhooks](/llamaparse/general/webhooks/index.md).
