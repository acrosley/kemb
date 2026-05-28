---
title: Google Vertex AI Setup | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

LlamaCloud supports Google Vertex AI for enterprise-grade access to Google’s AI models through Google Cloud Platform. Vertex AI provides advanced features like private endpoints, enhanced security, and deep GCP integration compared to the direct Gemini API.

## Prerequisites

- A valid Google Cloud Platform account

- Google Cloud project with Vertex AI API enabled

- Service account with appropriate IAM permissions

- Access and quota for supported models:

  - Gemini 3.1 Pro
  - Gemini 3.0 Flash
  - Gemini 2.5 Flash
  - Gemini 2.5 Pro
  - Gemini 2.5 Flash Lite
  - Gemini 2.0 Flash
  - Gemini 2.0 Flash Lite

## Environment Variables

The Google Vertex AI integration uses the following environment variables:

- `GOOGLE_VERTEX_AI_ENABLED` - Set to “true” to enable Google Vertex AI (required)
- `GOOGLE_VERTEX_AI_PROJECT_ID` - Google Cloud project ID (required)
- `GOOGLE_VERTEX_AI_LOCATION` - Google Cloud location/region (optional, defaults to `us-central1`)
- `GOOGLE_VERTEX_AI_CREDENTIALS_JSON` - Service account credentials JSON string (required)
- `GOOGLE_VERTEX_AI_BASE_URL` - Override the Vertex AI endpoint (optional; defaults to `https://{location}-aiplatform.googleapis.com`)

## Configuration

Follow these steps to configure Google Vertex AI integration:

### Step 1: Setup Google Cloud Project

1. Create or use an existing Google Cloud project

2. Enable the Vertex AI API:

   Terminal window

   ```
   gcloud services enable aiplatform.googleapis.com
   ```

3. Ensure billing is enabled for the project

### Step 2: Create Service Account

Create a service account with the required IAM permissions:

#### Required IAM Permissions

Your service account needs the following permissions:

- `aiplatform.endpoints.predict`
- `aiplatform.endpoints.explain`
- `ml.models.predict` (for legacy model versions)

#### Option 1: Use Predefined Role

Terminal window

```
gcloud iam service-accounts create llamacloud-vertex \
    --description="Service account for LlamaCloud Vertex AI" \
    --display-name="LlamaCloud Vertex AI"


gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:llamacloud-vertex@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"
```

#### Option 2: Custom Role

Create a custom role with minimal permissions:

```
{
  "title": "LlamaCloud Vertex AI User",
  "description": "Custom role for LlamaCloud Vertex AI access",
  "stage": "GA",
  "includedPermissions": [
    "aiplatform.endpoints.predict",
    "aiplatform.endpoints.explain",
    "ml.models.predict"
  ]
}
```

### Step 3: Generate Service Account Key

Generate a JSON key for the service account:

Terminal window

```
gcloud iam service-accounts keys create llamacloud-vertex-key.json \
    --iam-account=llamacloud-vertex@PROJECT_ID.iam.gserviceaccount.com
```

### Step 4: Create Kubernetes Secret

Create a secret with your Vertex AI credentials:

```
apiVersion: v1
kind: Secret
metadata:
  name: vertex-ai-credentials
type: Opaque
stringData:
  GOOGLE_VERTEX_AI_ENABLED: "true"
  GOOGLE_VERTEX_AI_PROJECT_ID: "your-project-id"
  GOOGLE_VERTEX_AI_LOCATION: "us-central1"
  GOOGLE_VERTEX_AI_CREDENTIALS_JSON: |
    {
      "type": "service_account",
      "project_id": "your-project-id",
      "private_key_id": "key-id",
      "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
      "client_email": "llamacloud-vertex@your-project-id.iam.gserviceaccount.com",
      "client_id": "client-id",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/llamacloud-vertex%40your-project-id.iam.gserviceaccount.com"
    }
```

Apply the secret:

Terminal window

```
kubectl apply -f vertex-ai-secret.yaml
```

### Step 5: Configure Helm Values

Reference the secret in your Helm configuration:

```
# External Secret (recommended)
config:
  llms:
    googleVertexAi:
      secret: "vertex-ai-credentials"
      baseUrl: "https://us-central1-aiplatform.googleapis.com"  # Optional — override endpoint


# or direct configuration (not recommended for production)
config:
  llms:
    googleVertexAi:
      projectId: "your-project-id"
      location: "us-central1"
      credentialsJson: |
        {
          "type": "service_account",
          ...
        }
      baseUrl: "https://us-central1-aiplatform.googleapis.com"  # Optional — override endpoint
```

The optional `baseUrl` / `GOOGLE_VERTEX_AI_BASE_URL` override sends Vertex AI traffic through a proxy or gateway (e.g. a self-hosted LLM gateway) instead of Google Cloud’s regional endpoint. Leave unset to use the default regional endpoint derived from `location`.

## Verification

After configuration, verify your Google Vertex AI integration:

1. **Verify in Admin UI**: Check available Google models in LlamaCloud admin interface

2. **Test functionality**: Upload a document to confirm Vertex AI models are working

## Troubleshooting

### Common Issues

#### Service Account Permissions

```
Error: Permission denied
```

**Solution**:

- Verify your service account has the required IAM permissions
- Ensure `aiplatform.endpoints.predict` permission is granted
- Check that the service account is active and not disabled

#### Project Configuration

```
Error: Project not found or Vertex AI API not enabled
```

**Solution**:

- Ensure Vertex AI API is enabled in your Google Cloud project
- Verify the project ID is correct in your configuration
- Check that billing is enabled for the project

#### Credentials Issues

```
Error: Could not load credentials
```

**Solution**:

- Verify the service account JSON is properly formatted
- Ensure all required fields are present in the credentials JSON
- Check that the private key is properly escaped in the secret
- Verify the service account key hasn’t been deleted or expired

#### Region Restrictions

```
Error: Model not available in region
```

**Solution**:

- Check model availability in your specified region
- Try a different region (e.g., `us-central1`, `us-east1`)
- Some models may not be available in all regions

### Debug Steps

1. **Test Vertex AI authentication**:

   Terminal window

   ```
   gcloud auth activate-service-account --key-file=vertex-key.json
   gcloud ai models list --region=us-central1
   ```

2. **Verify secret mounting**:

   Terminal window

   ```
   kubectl get secret vertex-ai-credentials -o yaml
   kubectl describe pod <pod-name> | grep -A 20 Environment
   ```

3. **Check network connectivity**: Ensure your cluster can reach `aiplatform.googleapis.com`

4. **Test API call**:

   Terminal window

   ```
   curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json" \
     "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-pro:predict" \
     -d '{"instances": [{"content": "Hello"}]}'
   ```
