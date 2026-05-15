---
title: Centralized Provider Configuration | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

Centralized LLM provider configuration allows you to configure LLM and managed embedding providers with custom credentials and API gateways. This configuration method enables use cases like routing through API gateways (Portkey, LiteLLM) or using custom credentials.

Note

Supports **OpenAI**, **Anthropic**, **Azure OpenAI**, **Google Gemini**, and **Google Vertex AI** providers.

## Use Cases

- **Custom API Gateways**: Route LLM requests through gateways like Portkey or LiteLLM
- **Custom Endpoints**: Use custom base URLs for proxies or regional endpoints
- **Custom Headers**: Add custom HTTP headers per provider instance (e.g., for gateway authentication)
- **Multiple Credentials**: Configure multiple provider instances with different API keys
- **Managed Embeddings**: Route managed Index embeddings through centrally configured OpenAI-compatible embedding providers

## Configuration Structure

Add provider configurations to your Helm values under `config.llms.providerConfigs`:

```
config:
  llms:
    providerConfigs:
      - id: "my-config-name"               # User-defined identifier (can be anything)
        provider: "openai"                 # Provider type: "openai", "anthropic", "azure", "gemini", or "vertexai"
        model_id: "openai-gpt-4o"          # LlamaCloud model identifier (fixed values, see below)
        provider_model_name: "gpt-4o"      # Optional: Provider-specific model name override, usually only needed if using an LLM gateway that requires a specific model name
        enabled: true                      # Enable/disable this configuration
        credentials:                       # Provider-specific credentials
          api_key: "sk-..."
          base_url: "https://custom.api.endpoint"  # Optional custom endpoint
        headers:                           # Custom HTTP headers (optional)
          X-Custom-Header: "value"
```

## Supported Providers

### OpenAI (Fully Supported)

```
- id: "openai-primary"
  provider: "openai"
  model_id: "openai-gpt-4o"
  credentials:
    api_key: "sk-..."                    # Required
    org_id: "org-..."                    # Optional
    base_url: "https://api.openai.com/v1"  # Optional
  headers:                               # Optional
    X-Custom-Header: "value"
```

**Supported model\_id values:**

- `openai-gpt-4o`
- `openai-gpt-4o-mini`
- `openai-gpt-4-1`
- `openai-gpt-4-1-mini`
- `openai-gpt-4-1-nano`
- `openai-gpt-5`
- `openai-gpt-5-mini`
- `openai-gpt-5-nano`
- `openai-text-embedding-3-small`
- `openai-text-embedding-3-large`

### Anthropic (Fully Supported)

```
- id: "anthropic-primary"
  provider: "anthropic"
  model_id: "anthropic-sonnet-4.5"
  credentials:
    api_key: "sk-ant-..."               # Required
    base_url: "https://api.anthropic.com"  # Optional
  headers:                               # Optional
    X-Custom-Header: "value"
```

**Supported model\_id values:**

- `anthropic-sonnet-4.6`
- `anthropic-sonnet-4.5`
- `anthropic-sonnet-4.0`
- `anthropic-sonnet-3.7`
- `anthropic-sonnet-3.5`
- `anthropic-sonnet-3.5-v2`
- `anthropic-haiku-4.5`
- `anthropic-haiku-3.5`
- `anthropic-opus-4.6`
- `anthropic-opus-4.5`

### Azure OpenAI (Fully Supported)

```
- id: "azure-sweden"
  provider: "azure"
  model_id: "openai-gpt-4o"
  credentials:
    api_key: "..."                      # Required
    endpoint: "https://your-resource.openai.azure.com"  # Required
    deployment_id: "gpt-4o"             # Optional
    api_version: "2024-08-06"           # Optional
  headers:                               # Optional
    X-Custom-Header: "value"
```

**Supported model\_id values:**

- `openai-gpt-4o`
- `openai-gpt-4o-mini`
- `openai-gpt-4-1`
- `openai-gpt-4-1-mini`
- `openai-gpt-4-1-nano`
- `openai-gpt-5`
- `openai-gpt-5-mini`
- `openai-gpt-5-nano`
- `openai-text-embedding-3-small`
- `openai-text-embedding-3-large`

For Azure-hosted embedding models, set `model_id` to the LlamaCloud model identifier and `credentials.deployment_id` to your Azure deployment name.

### Google Gemini (Fully Supported)

```
- id: "gemini-primary"
  provider: "gemini"
  model_id: "gemini-2.5-flash"
  credentials:
    api_key: "AIza..."                   # Required
    base_url: "https://generativelanguage.googleapis.com"  # Optional
  headers:                               # Optional
    X-Custom-Header: "value"
```

**Supported model\_id values:**

- `gemini-3.1-pro`
- `gemini-3.0-pro`
- `gemini-3.0-flash`
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`

### Google Vertex AI (Fully Supported)

Vertex AI serves both Gemini and Anthropic Claude models. Use service-account authentication with `project_id` + `location` + `credentials` (JSON-serialised service account key).

```
- id: "vertex-primary"
  provider: "vertexai"
  model_id: "gemini-2.5-flash"
  credentials:
    project_id: "your-gcp-project-id"    # Required
    location: "us-central1"              # Required
    credentials: |-                      # Required (service account key JSON)
      {
        "type": "service_account",
        "project_id": "your-gcp-project-id",
        "private_key_id": "...",
        "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
        "client_email": "...@your-gcp-project-id.iam.gserviceaccount.com",
        "client_id": "..."
      }
    base_url: "https://us-central1-aiplatform.googleapis.com"  # Optional
  headers:                               # Optional
    X-Custom-Header: "value"
```

Note

Keep `private_key` as a single line with literal `\n` escape sequences (the format you get directly from a downloaded service account key file). Expanding them to real newlines breaks the inner JSON parse — JSON strings cannot contain raw newline characters.

**Supported model\_id values (Gemini on Vertex):**

- `gemini-3.1-pro`
- `gemini-3.0-pro`
- `gemini-3.0-flash`
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`
- `gemini-2.0-flash`
- `gemini-2.0-flash-lite`

**Supported model\_id values (Anthropic on Vertex):**

- `anthropic-sonnet-4.6`
- `anthropic-sonnet-4.5`
- `anthropic-sonnet-4.0`
- `anthropic-sonnet-3.7`
- `anthropic-haiku-4.5`
- `anthropic-opus-4.6`
- `anthropic-opus-4.5`

## Common Use Cases

### Custom API Gateway

Use a custom API gateway or proxy (e.g., Portkey, LiteLLM):

```
config:
  llms:
    providerConfigs:
      - id: "portkey-openai"
        provider: "openai"
        model_id: "openai-gpt-4o-mini"
        provider_model_name: "@openai/gpt-4o-mini"
        enabled: true
        credentials:
          api_key: "your-portkey-api-key"
          base_url: "https://api.portkey.ai/v1"
        headers:
          x-portkey-api-key: "your-portkey-api-key"


      - id: "portkey-anthropic"
        provider: "anthropic"
        model_id: "anthropic-sonnet-4.5"
        provider_model_name: "@anthropic/claude-sonnet-4-5"
        enabled: true
        credentials:
          api_key: "your-portkey-api-key"
          base_url: "https://api.portkey.ai"
        headers:
          x-portkey-api-key: "your-portkey-api-key"
          x-portkey-strict-open-ai-compliance: "False"
```

## Verification

After configuration, verify your setup:

1. **Verify in Admin UI**: Check the LlamaCloud admin interface for available models

2. **Test parsing**: Upload a document to LlamaParse to confirm the configured providers are working
