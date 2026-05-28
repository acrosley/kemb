---
title: Overview | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

LlamaCloud supports multiple LLM models through different provider access methods to power its document parsing, extraction, and AI capabilities. This section provides guidance on configuring and choosing between different model providers for your self-hosted deployment.

## Supported Models and Providers

| Model Family                                                            | Developer Direct *(Simple Setup)*                                                                   | Enterprise Cloud *(Advanced Features)*                                                                |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **OpenAI GPT** GPT-4o, GPT-4.1, GPT-5, GPT-5                            | [OpenAI API](/llamaparse/self_hosting/configuration/llm_integrations/openai/index.md)               | [Azure OpenAI](/llamaparse/self_hosting/configuration/llm_integrations/azure-openai/index.md)         |
| **Anthropic Claude** Claude 4.0 Sonnet, Claude 3.5 Haiku, Claude 3 Opus | [Anthropic API](/llamaparse/self_hosting/configuration/llm_integrations/anthropic/index.md)         | [AWS Bedrock](/llamaparse/self_hosting/configuration/llm_integrations/aws-bedrock/index.md)           |
| **Google Gemini** Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 2.0 Flash    | [Google Gemini API](/llamaparse/self_hosting/configuration/llm_integrations/google-gemini/index.md) | [Google Vertex AI](/llamaparse/self_hosting/configuration/llm_integrations/google-vertex-ai/index.md) |

## Configuration Methods

### Centralized Provider Configuration

Centralized provider configuration enables:

- Multiple provider instances with different credentials
- Custom API endpoints (e.g., for API gateways like Portkey)
- Custom HTTP headers per provider instance
- Custom provider-specific model names

Note

Supports **OpenAI**, **Anthropic**, **Azure OpenAI**, **Google Gemini**, and **Google Vertex AI** providers.

```
config:
  llms:
    providerConfigs:
      - id: "my-openai-config"
        provider: "openai"
        model_id: "openai-gpt-4o"
        provider_model_name: "@openai/gpt-4o"  # Optional: custom model name for gateway
        credentials:
          api_key: "sk-..."
          base_url: "https://api.gateway.com/v1"  # Optional: custom endpoint
        headers:  # Optional: custom headers
          x-api-key: "your-gateway-key"
      - id: "my-anthropic-config"
        provider: "anthropic"
        model_id: "anthropic-sonnet-4.5"
        provider_model_name: "@anthropic/claude-sonnet-4-5"  # Optional: custom model name for gateway
        credentials:
          api_key: "sk-ant-..."
          base_url: "https://api.gateway.com"  # Optional: custom endpoint
        headers:  # Optional: custom headers
          x-api-key: "your-gateway-key"
```

**See:** [Centralized Provider Configuration Guide](/llamaparse/self_hosting/configuration/llm_integrations/centralized-config/index.md) for complete documentation.

### Provider-Specific Configuration

For most deployments, use provider-specific configuration with Kubernetes secrets:

```
config:
  llms:
    openai:
      secret: <your-openai-secret>
    anthropic:
      secret: <your-anthropic-secret>
    gemini:
      secret: <your-gemini-secret>
    azureOpenAi:
      secret: <your-azureOpenAi-secret>
    awsBedrock:
      secret: <your-bedrock-secret>
    googleVertexAi:
      secret: <your-vertex-secret>
```

Helm Values Configuration (Legacy)

Some providers support direct configuration in Helm values (being deprecated):

```
backend:
  config:
    openAiApiKey: "your-api-key"
```

## Next Steps

### Configuration Guides

- [Centralized Provider Configuration](/llamaparse/self_hosting/configuration/llm_integrations/centralized-config/index.md) - For custom API gateways (LlamaParse only)

### Provider-Specific Setup

Choose your LLM provider and follow the detailed setup instructions:

- [OpenAI Setup](/llamaparse/self_hosting/configuration/llm_integrations/openai/index.md)
- [Azure OpenAI Setup](/llamaparse/self_hosting/configuration/llm_integrations/azure-openai/index.md)
- [Anthropic API Setup](/llamaparse/self_hosting/configuration/llm_integrations/anthropic/index.md)
- [AWS Bedrock Setup](/llamaparse/self_hosting/configuration/llm_integrations/aws-bedrock/index.md)
- [Google Gemini API Setup](/llamaparse/self_hosting/configuration/llm_integrations/google-gemini/index.md)
- [Google Vertex AI Setup](/llamaparse/self_hosting/configuration/llm_integrations/google-vertex-ai/index.md)

## Troubleshooting

### Verification Steps

After configuration, verify your setup by:

1. Using the LlamaCloud admin UI to confirm available models
2. Testing with a simple parsing or extraction task

### Common Issues

1. **Model not available**: Check provider documentation for model availability in your region
2. **Authentication failures**: Verify API keys and permissions
3. **Rate limiting**: Monitor usage and implement appropriate quotas
