---
title: Validation Guide | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

This guide helps you verify that your LlamaCloud deployment on Azure is working correctly. Follow these steps after completing the [Azure Setup Guide](/llamaparse/self_hosting/cloud-specific-guides/azure/setup/index.md).

## Step 1: Verify Pod Status

Check that all LlamaCloud pods are running correctly:

Terminal window

```
# Check all pods are running
kubectl get pods -n llamacloud


# Expected output should show all pods as Running:
llamacloud-64f468d5cf-sqjq6                 1/1     Running
llamacloud-layout-6d97b84c58-rld8x          1/1     Running
llamacloud-ocr-5cc459bdd-99xgt              1/1     Running
llamacloud-operator-5d4c58b854-dwnjk        1/1     Running
llamacloud-parse-7ffbc786b5-r98w2           1/1     Running
llamacloud-telemetry-5fc9ff8c67-fv8xj       1/1     Running
llamacloud-web-b88d95588-rprhc              1/1     Running
llamacloud-worker-58b95ccc6f-vqmgx          1/1     Running
llamacloud-s3proxy-xxx                      1/1     Running
```

If any pods are not in `Running` state, check the logs:

Terminal window

```
kubectl logs deployment/llamacloud-telemetry -n llamacloud
```

## Step 2: Access UI and Test Authentication

### Access the LlamaCloud UI

**Port Forward (for testing)**

Terminal window

```
kubectl -n llamacloud port-forward svc/llamacloud-web 3000:80
```

Open `http://localhost:3000` in your browser.

**Production Access (if ingress configured)** If you have an ingress controller set up, access your configured domain.

### Test Authentication

1. **Navigate to LlamaCloud UI**
2. **Click Sign In** - should redirect to Microsoft Entra ID
3. **Complete OIDC flow** - authenticate with your Microsoft Entra ID credentials
4. **Verify successful login** - should return to LlamaCloud dashboard

## Step 3: Access Admin UI

After successful authentication, verify admin functionality:

1. **Navigate to Admin Settings** - Look for the admin/settings section in the UI
2. **Check License Status** - Verify your LlamaCloud license shows as “Active”
3. **Review LLM Availability** - Expand the LLM section to see provider and model status
4. **Check File Storage** - Expand to verify all required buckets show as “Available”
5. **Review Feature Availability** - Check that Parse, Extract, and Chat features work with your models

The admin UI displays three main expandable sections:

### License Status

- **License validity** and expiration date
- **Version information** of your deployment
- **Renewal reminders** if license is expiring

### LLM Availability

- **Provider status** (OpenAI, Anthropic, etc.)
- **Model validation** with ✅ for working models, ❌ for failed models
- **Error messages** for any model connectivity issues

![LLM Availability Admin UI](/_astro/admin_llm.D4c_e2I1_1wGm6g.png)

### File Storage Availability

- **Available buckets** - Should show all 8 required containers:

  - `llama-platform-parsed-documents`
  - `llama-platform-etl`
  - `llama-platform-external-components`
  - `llama-platform-file-parsing`
  - `llama-platform-raw-files`
  - `llama-cloud-parse-output`
  - `llama-platform-file-screenshots`
  - `llama-platform-extract-output`

- **Unavailable buckets** - Should be empty if properly configured

![File Storage Availability Admin UI](/_astro/admin_blob.BX4kmqyM_7Bki3.png)

### Feature Availability

- **Parse Features** - Shows preset modes (Fast, Balanced, Premium) and advanced parsing modes
- **Extract Features** - Shows schema generation and extraction mode availability
- **Chat Playground** - Shows available models for chat functionality

![Feature Availability Admin UI](/_astro/admin_features.D-xlkA4Z_Z2a9Nt8.png)

## Step 4: Test Basic Product Functionality

### Test Document Parsing

1. **Navigate to the Parse product** in the LlamaCloud UI
2. **Keep the default setting** (Cost-effective mode)
3. **Upload a test PDF** document
4. **Verify the parsing job completes successfully**

## Validation Checklist

Use this checklist to ensure your deployment is fully validated:

- [ ] All pods are in `Running` state
- [ ] Frontend is accessible via browser
- [ ] Microsoft Entra ID authentication works
- [ ] Admin UI license status shows as “Active”
- [ ] LLM models show ✅ status in admin UI
- [ ] All 8 required storage buckets show as “Available”
- [ ] Feature availability shows required capabilities working
- [ ] Can navigate to Parse product
- [ ] Can upload PDF documents
- [ ] Document parsing job completes successfully

## Next Steps

If you encounter any issues during validation, see the [Troubleshooting Guide](/llamaparse/self_hosting/cloud-specific-guides/azure/troubleshooting/index.md) for solutions to common problems.

Once validation is complete, your Azure LlamaCloud deployment is ready for use!
