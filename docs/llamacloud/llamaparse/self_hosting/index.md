---
title: Self-Hosting & BYOC (Bring Your Own Cloud) | Developer Documentation
description: Deploy LlamaCloud in your own cloud infrastructure with full self-hosting and BYOC support. Run LlamaParse, LlamaExtract, and the complete LlamaCloud platform on Kubernetes using Helm charts — on AWS, Azure, or GCP.
---

LlamaCloud can be deployed entirely within your own infrastructure. Self-hosted deployments — also known as **BYOC (Bring Your Own Cloud)** — give you the full capabilities of the LlamaCloud platform while keeping your data, models, and infrastructure under your control.

## What You Get

A self-hosted LlamaCloud deployment includes the **complete platform** — the same features available on our managed cloud service:

- **[LlamaParse](/python/cloud/llamaparse/index.md)** — Document parsing with 130+ file format support, OCR, and agentic parsing modes
- **[LlamaExtract](/python/cloud/llamaextract/index.md)** — Structured data extraction from unstructured documents
- **[LlamaCloud Indexes](/python/cloud/llamacloud/index.md)** — Managed RAG pipelines with document ingestion, chunking, embedding, and retrieval
- **Full Web UI and API** — The same interface and REST API as the managed service, running in your environment

## How It Works

LlamaCloud is packaged as a **Helm chart** and deployed on **Kubernetes** (EKS, AKS, GKE, or any conformant cluster). You configure the deployment through a `values.yaml` file that specifies your database connections, LLM credentials, authentication provider, and storage backend.

## Cloud Provider Support

We provide deployment guides and tested configurations for all major cloud platforms:

| Cloud Provider            | Kubernetes | Storage            |
| ------------------------- | ---------- | ------------------ |
| **Amazon Web Services**   | EKS        | S3                 |
| **Microsoft Azure**       | AKS        | Azure Blob Storage |
| **Google Cloud Platform** | GKE        | GCS                |

## LLM Provider Support

LlamaParse uses models from OpenAI, Anthropic, and Google, selected per use case for best quality. Self-hosted deployments support both direct API access and enterprise cloud-hosted models:

| Model Family         | Direct API        | Enterprise Cloud |
| -------------------- | ----------------- | ---------------- |
| **OpenAI**           | OpenAI API        | Azure OpenAI     |
| **Anthropic Claude** | Anthropic API     | AWS Bedrock      |
| **Google Gemini**    | Google Gemini API | Google Vertex AI |

All LLM calls go directly from your cluster to providers using your own API keys and contracts. For organizations that need to restrict to a single cloud provider’s models, this is configurable — [contact us](https://www.llamaindex.ai/contact) to discuss your requirements.

## Security and Compliance

Self-hosting is designed for organizations with strict data governance requirements:

- **Data stays in your cloud** — Documents, embeddings, and processed outputs never leave your infrastructure
- **Enterprise authentication** — OIDC integration with your identity provider (Microsoft Entra ID, Okta, and others)
- **Network isolation** — Deploy within your VPC with full control over ingress, egress, and network policies

## Get Started

Self-hosted LlamaCloud is available on **Enterprise plans**.

1. **[Contact us](https://www.llamaindex.ai/contact)** to discuss your deployment and obtain a license key
2. Follow the **[Quick Start guide](/python/cloud/self_hosting/installation/index.md)** to deploy
3. Explore **[cloud-specific deployment guides](/python/cloud/self_hosting/cloud-specific-guides/overview/index.md)** for production-ready configurations
