---
title: Architecture | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

This page provides an overview of the LlamaCloud architecture.

## Overview

Self-hosted LlamaCloud is an Enterprise-only feature, designed specifically to meet the needs of organizations that require a high degree of control over their data and infrastructure. Please contact us at <https://www.llamaindex.ai/contact> if you’re interested in learning more about self-hosting.

The following diagram shows the architecture of LlamaCloud:

![LlamaCloud Architecture](/_astro/architecture.BJvH2wuD_Z2mwYTd.png)

## Databases, Queues, and File Stores

Note

Containerized deployments of the required databases and queues are enabled by default in self-hosted deployments. This is only to help you get started. For production deployments, we recommend connecting LlamaCloud to externally managed services. For more information, please refer to the [installation guide](/llamaparse/self_hosting/cloud-specific-guides/overview/index.md).

- **Postgres**: LlamaCloud uses Postgres as its primary, relational database for almost everything.
- **MongoDB**: LlamaCloud uses MongoDB as its secondary, document database for storing data around document ingestion and pipelines.
- **Redis**: LlamaCloud uses Redis as its primary, in-memory key-value store for queuing and caching operations.
- **RabbitMQ**: LlamaCloud uses RabbitMQ as its message queue. We leverage a series of queues to manage large-scale data processing jobs.
- **S3Proxy**: To support non-S3 object storage options, we allow users to deploy [s3proxy](https://github.com/andrewgaul/s3proxy), an S3-compatible proxy, to interact with other storage solutions.

## Internal Services

### LlamaCloud Frontend

The frontend is the main user interface for LlamaCloud. We recommend exposing it through a reverse proxy like Nginx or Traefik for users to connect to in production.

### LlamaCloud Backend

This is the API entrypoint for LlamaCloud. It handles all requests from the frontend and the business logic of our platform. This service can also be used as a standalone API.

### LlamaCloud Jobs Service

The jobs service is responsible for managing job processing and ingestion pipelines.

### LlamaCloud Jobs Worker

The jobs worker works with the jobs service to process and ingest data.

### LlamaCloud Usage Service

This service tracks all parsing and ingestion usage across projects, indexes, and organizations.

### LlamaParse Service

LlamaParse is the engine that powers LlamaCloud’s unstructured document parsing. It supports a variety of file formats, parsing modes, and output formats. For more information, please refer to the [LlamaParse documentation](/llamaparse/parse/index.md).

### LlamaParse OCR Service

This service works hand-in-hand with LlamaParse to increase the accuracy of our document parsing.
