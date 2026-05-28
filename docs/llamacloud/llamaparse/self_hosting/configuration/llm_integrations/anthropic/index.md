---
title: Anthropic API Setup | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

LlamaCloud supports direct integration with the Anthropic API for accessing Claude models. This provides a simple alternative to AWS Bedrock when you want direct access to Anthropic’s latest models without AWS infrastructure dependencies.

## Prerequisites

- A valid Anthropic account

- Anthropic API key from [Anthropic Console](https://console.anthropic.com/)

- Access and quota to supported Claude models:

  - Claude 3.5 Haiku
  - Claude 3.5 Sonnet (deprecated)
  - Claude 3.5 Sonnet V2 (deprecated)
  - Claude 3.7 Sonnet
  - Claude 4 Sonnet

## Environment Variables

The Anthropic API integration uses a single environment variable:

- `ANTHROPIC_API_KEY` - Your Anthropic API key (required)

## Configuration

Follow these steps to configure Anthropic API integration:

### Step 1: Create Kubernetes Secret

Create a secret with your Anthropic API key:

```
apiVersion: v1
kind: Secret
metadata:
  name: anthropic-credentials
type: Opaque
stringData:
  ANTHROPIC_API_KEY: "sk-ant-api03-your-api-key-here"
```

Apply the secret to your cluster:

Terminal window

```
kubectl apply -f anthropic-secret.yaml
```

### Step 2: Configure Helm Values

Reference the secret in your Helm configuration:

```
# External Secret
config:
  llms:
    anthropic:
      secret: "anthropic-credentials"


# or direct configuration (not recommended for production)
config:
  llms:
    anthropic:
      apiKey: "sk-ant-api03-your-api-key-here"
```

## Verification

After configuration, verify your Anthropic integration:

1. **Check Admin UI**: Verify Claude models appear in LlamaCloud admin interface
2. **Test functionality**: Upload a document to confirm Claude models are working

## Troubleshooting

### Common Issues

#### API Key Invalid

```
Error: Invalid API key
```

**Solution**:

- Verify your API key is correct and active in Anthropic Console
- Ensure the key starts with `sk-ant-api03-`
- Check that the key hasn’t expired

#### Authentication Failed

```
Error: Authentication failed
```

**Solution**:

- Confirm your Anthropic account is in good standing
- Verify the API key has the necessary permissions
- Check if your account has been suspended

#### Rate Limiting

```
Error: Rate limit exceeded
```

**Solution**:

- Check your Anthropic usage limits
- Consider upgrading your Anthropic plan
- Implement request throttling if needed
- Monitor usage patterns

#### Model Access Issues

```
Error: Model not available or access denied
```

**Solution**:

- Verify you have access to the specific Claude model
- Some models may require special access approval
- Check model availability in your region

#### Quota Exceeded

```
Error: Usage quota exceeded
```

**Solution**:

- Check your Anthropic account usage and limits
- Add credits to your Anthropic account
- Set up billing alerts
- Consider usage optimization

### Debug Steps

1. **Test API key directly**:

   Terminal window

   ```
   curl https://api.anthropic.com/v1/messages \
     -H "x-api-key: $ANTHROPIC_API_KEY" \
     -H "content-type: application/json" \
     -H "anthropic-version: 2023-06-01" \
     -d '{
       "model": "claude-3-5-sonnet-20241022",
       "max_tokens": 1024,
       "messages": [{"role": "user", "content": "Hello, Claude"}]
     }'
   ```

2. **Check secret mounting**:

   Terminal window

   ```
   kubectl get secret your-anthropic-secret -o yaml
   kubectl exec deployment/llamacloud-llamaparse -- env | grep ANTHROPIC
   ```

3. **Verify network connectivity**: Ensure your cluster can reach `api.anthropic.com`

4. **Check logs for detailed errors**:

   Terminal window

   ```
   kubectl logs deployment/llamacloud-llamaparse --tail=100 | grep -i error
   ```
