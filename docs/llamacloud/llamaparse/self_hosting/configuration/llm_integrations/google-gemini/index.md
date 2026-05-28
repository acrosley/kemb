---
title: Google Gemini API Setup | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

LlamaCloud supports Google Gemini API for direct access to Google’s AI models with simple API key authentication. This provides a straightforward alternative to Google Vertex AI when you don’t need enterprise Google Cloud Platform features.

## Prerequisites

- A valid Google account

- Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

- Access and quota for supported models:

  - Gemini 3.1 Pro
  - Gemini 3.0 Flash
  - Gemini 2.5 Flash
  - Gemini 2.5 Pro
  - Gemini 2.0 Flash
  - Gemini 2.0 Flash Lite

## Environment Variables

The Google Gemini API integration uses the following environment variables:

- `GOOGLE_GEMINI_API_KEY` - Your Google Gemini API key (required)
- `GOOGLE_GEMINI_BASE_URL` - Override the Gemini API endpoint (optional; defaults to `https://generativelanguage.googleapis.com`)

## Configuration

Follow these steps to configure Google Gemini API integration:

### Step 1: Get Google Gemini API Key

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Step 2: Create Kubernetes Secret

Create a secret with your Google Gemini API key:

```
apiVersion: v1
kind: Secret
metadata:
  name: gemini-credentials
type: Opaque
stringData:
  GOOGLE_GEMINI_API_KEY: "your-api-key-here"
```

Apply the secret:

Terminal window

```
kubectl apply -f gemini-secret.yaml
```

### Step 3: Configure Helm Values

Reference the secret in your Helm configuration:

```
# External Secret
config:
  llms:
    gemini:
      secret: "gemini-credentials"
      baseUrl: "https://generativelanguage.googleapis.com"  # Optional — override endpoint


# or direct configuration
config:
  llms:
    gemini:
      apiKey: "your-api-key-here"
      baseUrl: "https://generativelanguage.googleapis.com"  # Optional — override endpoint
```

The optional `baseUrl` / `GOOGLE_GEMINI_BASE_URL` override sends Gemini API traffic through a proxy or gateway (e.g. a self-hosted LLM gateway) instead of Google’s public endpoint. Leave unset to use the default `https://generativelanguage.googleapis.com`.

## Verification

After configuration, verify your Google Gemini integration:

1. **Verify in Admin UI**: Check available Google models in LlamaCloud admin interface

2. **Test functionality**: Upload a document to confirm Gemini models are working

## Troubleshooting

### Common Issues

#### API Key Invalid

```
Error: API key not valid
```

**Solution**:

- Ensure your API key is correctly set and hasn’t expired
- Verify the key is from Google AI Studio
- Check that the API key has proper permissions

#### Quota Exceeded

```
Error: Quota exceeded
```

**Solution**:

- Check your Google AI Studio quotas and usage limits
- Consider upgrading your plan or requesting quota increases
- Monitor API usage to avoid rate limiting

#### Model Access Issues

```
Error: Model not found or access denied
```

**Solution**:

- Verify the model is available in your region
- Check if you have access to the specific model
- Ensure your API key has model access permissions

### Debug Steps

1. **Test Gemini API directly**:

   Terminal window

   ```
   curl -H "Content-Type: application/json" \
        -H "x-goog-api-key: YOUR_API_KEY" \
        -d '{"contents":[{"parts":[{"text":"Hello"}]}]}' \
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
   ```

2. **Verify secret mounting**:

   Terminal window

   ```
   kubectl get secret gemini-credentials -o yaml
   kubectl describe pod <pod-name> | grep -A 20 Environment
   ```

3. **Check network connectivity**: Ensure your cluster can reach `generativelanguage.googleapis.com`
