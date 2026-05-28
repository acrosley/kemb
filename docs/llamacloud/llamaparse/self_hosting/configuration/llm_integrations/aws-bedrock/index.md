---
title: AWS Bedrock Setup | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

LlamaCloud supports AWS Bedrock for accessing Anthropic Claude models as part of its multimodal AI capabilities. AWS Bedrock provides enterprise-grade access with advanced security, compliance, and AWS ecosystem integration. This page guides you through configuring AWS Bedrock integration with your self-hosted LlamaCloud deployment.

## Prerequisites

- A valid AWS account

- AWS Bedrock access enabled in your region

- Access and quota to the supported models:

  - **For LlamaParse Advanced Features**:

    - Anthropic Claude 3.7 Sonnet (`anthropic.claude-3-7-sonnet-20250219-v1:0`)
    - Anthropic Claude 3.5 Sonnet (`anthropic.claude-3-5-sonnet-20240620-v1:0`) (deprecated)
    - Anthropic Claude 3.5 Haiku (`anthropic.claude-3-5-haiku-20241022-v1:0`)
    - Anthropic Claude 4 Sonnet (`anthropic.claude-sonnet-4-20250514-v1:0`)

  - **For LlamaCloud Playground**:

    - Anthropic Claude 3.5 Sonnet V2 (deprecated)
    - Cohere Rerank 3.5 (Optional)

## Environment Variables

### Basic Configuration

- `AWS_ACCESS_KEY_ID` - AWS access key ID
- `AWS_SECRET_ACCESS_KEY` - AWS secret access key
- `AWS_REGION` - AWS region (e.g., `us-east-1`)

### Model Version Overrides (Optional)

- `BEDROCK_ANTHROPIC_SONNET_3_5_VERSION_NAME` - Override for Claude 3.5 Sonnet version (deprecated)

- `BEDROCK_ANTHROPIC_SONNET_3_7_VERSION_NAME` - Override for Claude 3.7 Sonnet version

- `BEDROCK_ANTHROPIC_HAIKU_3_5_VERSION_NAME` - Override for Claude 3.5 Haiku version

- `BEDROCK_ANTHROPIC_HAIKU_4_5_VERSION_NAME` - Override for Claude 4.5 Haiku version

- `BEDROCK_ANTHROPIC_SONNET_4_0_VERSION_NAME` - Override for Claude 4 Sonnet version

- `PREFERED_PREMIUM_MODE_MODEL` - Override the premium\_mode model.

## Configuration

Choose one of these methods to configure AWS Bedrock integration:

### Method 1: IAM Roles for Service Accounts (Recommended)

This method uses AWS IAM roles for secure, credential-free authentication.

#### Step 1: Create IAM Policy

Create an IAM policy with the following permissions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:CreateModelInvocationJob",
        "bedrock:ListInferenceProfiles"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:foundation-model/*",
        "arn:aws:bedrock:*:*:inference-profile/*"
      ]
    }
  ]
}
```

#### Step 2: Create IAM Role

1. Create an IAM role for EKS service accounts
2. Attach the policy to the role
3. Configure trust relationship for your EKS cluster

#### Step 3: Configure Helm Values

```
llamaParse:
  serviceAccountAnnotations:
    eks.amazonaws.com/role-arn: "arn:aws:iam::ACCOUNT-ID:role/ROLE-NAME"
```

#### Step 4: Override Model Versions (Optional)

If you need to override the default model versions, configure them directly in your Helm values:

```
config:
  llms:
    awsBedrock:
      # Optional: Override default model versions
      sonnet3_5ModelVersionName: "anthropic.claude-3-5-sonnet-20240620-v1:0"
      sonnet3_7ModelVersionName: "anthropic.claude-3-7-sonnet-20250219-v1:0"
      haiku3_5ModelVersionName: "anthropic.claude-3-5-haiku-20241022-v1:0"
      sonnet4_0ModelVersionName: "anthropic.claude-sonnet-4-20250514-v1:0"
      # Or use inference profile IDs
      # sonnet3_5ModelVersionName: "us.anthropic.claude-3-5-sonnet-20241022-v2:0"
      # sonnet3_7ModelVersionName: "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
      # haiku3_5ModelVersionName: "us.anthropic.claude-3-5-haiku-20241022-v1:0"
      # sonnet4_0ModelVersionName: "us.anthropic.claude-sonnet-4-20250514-v1:0"
```

For complete setup instructions, see the [AWS EKS IAM Roles documentation](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

### Method 2: Static AWS Credentials

#### Step 1: Create Kubernetes Secret

```
apiVersion: v1
kind: Secret
metadata:
  name: aws-bedrock-credentials
type: Opaque
stringData:
  AWS_ACCESS_KEY_ID: "AKIA..."
  AWS_SECRET_ACCESS_KEY: "your-secret-key"
  AWS_REGION: "us-east-1"
  # Optional: Override default model versions
  BEDROCK_ANTHROPIC_SONNET_3_5_VERSION_NAME: "anthropic.claude-3-5-sonnet-20240620-v1:0"
  BEDROCK_ANTHROPIC_SONNET_3_7_VERSION_NAME: "anthropic.claude-3-7-sonnet-20250219-v1:0"
  BEDROCK_ANTHROPIC_HAIKU_3_5_VERSION_NAME: "anthropic.claude-3-5-haiku-20241022-v1:0"
  BEDROCK_ANTHROPIC_HAIKU_4_5_VERSION_NAME: "anthropic.claude-haiku-4-5-20251001-v1:0"
  BEDROCK_ANTHROPIC_SONNET_4_0_VERSION_NAME: "anthropic.claude-sonnet-4-20250514-v1:0"
  PREFERED_PREMIUM_MODE_MODEL: "anthropic-sonnet-4.0"
```

#### Step 2: Configure Helm Values

```
# External Secret
config:
  llms:
    awsBedrock:
      secret: "aws-bedrock-credentials"


# or direct configuration (not recommended for production)
config:
  llms:
    awsBedrock:
      region: "us-east-1"
      accessKeyId: "AKIA..."
      secretAccessKey: "your-secret-key"
      sonnet3_5ModelVersionName: "anthropic.claude-3-5-sonnet-20240620-v1:0"
      sonnet3_7ModelVersionName: "anthropic.claude-3-7-sonnet-20250219-v1:0"
      haiku3_5ModelVersionName: "anthropic.claude-3-5-haiku-20241022-v1:0"
      sonnet4_0ModelVersionName: "anthropic.claude-sonnet-4-20250514-v1:0"
```

## AWS Bedrock Inference Profiles

AWS Bedrock inference profiles provide enhanced functionality for routing model requests across regions and cost tracking. Some newer Anthropic models require inference profiles instead of direct model IDs.

### When to Use Inference Profiles

- **Required for certain models**: Depending on the model and region, you may need to use inference profiles instead of direct model IDs
  - Please refer to the [AWS Inference Profiles Support Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) for more information
- **Cross-region routing**: Automatic request routing across multiple regions for improved availability
- **Cost tracking**: Detailed usage and cost tracking for applications
- **Enhanced reliability**: Better fault tolerance and availability

### Inference Profile ID Format

Inference profile IDs use a regional prefix format:

- **Claude 3.5 Sonnet**: `us.anthropic.claude-3-5-sonnet-20241022-v2:0`
- **Claude 3.7 Sonnet**: `us.anthropic.claude-3-7-sonnet-20250219-v1:0`
- **Claude 3.5 Haiku**: `us.anthropic.claude-3-5-haiku-20241022-v1:0`
- **Claude 4 Sonnet**: `us.anthropic.claude-sonnet-4-20250514-v1:0`

### Finding Inference Profile IDs

1. Navigate to the Amazon Bedrock console
2. Go to **Inference and Assessment** → **Cross-region Inference**
3. Copy the **Inference Profile ID** for your desired model

### Configuration with Inference Profiles

Use inference profile IDs instead of model IDs in your configuration:

```
apiVersion: v1
kind: Secret
metadata:
  name: aws-bedrock-credentials
type: Opaque
stringData:
  AWS_ACCESS_KEY_ID: "AKIA..."
  AWS_SECRET_ACCESS_KEY: "your-secret-key"
  AWS_REGION: "us-east-1"
  # Use inference profiles for newer models
  BEDROCK_ANTHROPIC_SONNET_3_5_VERSION_NAME: "us.anthropic.claude-3-5-sonnet-20241022-v2:0"
  BEDROCK_ANTHROPIC_SONNET_3_7_VERSION_NAME: "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
  BEDROCK_ANTHROPIC_HAIKU_3_5_VERSION_NAME: "us.anthropic.claude-3-5-haiku-20241022-v1:0"
  BEDROCK_ANTHROPIC_HAIKU_4_5_VERSION_NAME: "us.anthropic.claude-haiku-4-5-20251001-v1:0"
  BEDROCK_ANTHROPIC_SONNET_4_0_VERSION_NAME: "us.anthropic.claude-sonnet-4-20250514-v1:0"
  PREFERED_PREMIUM_MODE_MODEL: "anthropic-sonnet-4.0"
```

## Verification

After configuration, verify your AWS Bedrock integration:

1. **Check Admin UI**: Verify Claude models appear in LlamaCloud admin interface
2. **Test functionality**: Upload a document and use advanced parsing modes

## Troubleshooting

### Common Issues

#### Access Denied

```
Error: User is not authorized to perform bedrock:InvokeModel
```

**Solution**:

- Verify IAM permissions include all required actions
- Check that the resource ARNs include both foundation models and inference profiles
- Ensure the role is properly attached to the service account (for IRSA)

#### Model Not Found

```
Error: Could not resolve foundation model from model identifier
```

**Solution**:

- Verify the model ID or inference profile ID is correct
- Check that the model is available in your AWS region
- Try using an inference profile ID instead of direct model ID

#### On-Demand Throughput Error

```
Error: On-demand throughput is not supported for this model
```

**Solution**:

- This typically means the model requires an inference profile
- Switch to using the inference profile ID format
- Check the Bedrock console for the correct inference profile ID

#### Region Issues

```
Error: Model not available in region
```

**Solution**:

- Check model availability in your specified AWS region
- Consider switching to a region where the model is available
- Use cross-region inference profiles for better availability

#### Quota Exceeded

```
Error: Throttling exception or quota exceeded
```

**Solution**:

- Check your Bedrock quotas in AWS Console
- Request quota increases if needed
- Implement request throttling in your application

### Debug Steps

1. **Test AWS credentials directly**:

   Terminal window

   ```
   aws bedrock list-foundation-models --region us-east-1
   ```

2. **Test model invocation**:

   Terminal window

   ```
   aws bedrock-runtime invoke-model \
     --model-id anthropic.claude-3-5-sonnet-20240620-v1:0 \
     --body '{"messages":[{"role":"user","content":[{"type":"text","text":"Hello"}]}],"max_tokens":100,"anthropic_version":"bedrock-2023-05-31"}' \
     --cli-binary-format raw-in-base64-out \
     output.json
   ```

3. **Verify service account annotations** (for IRSA):

   Terminal window

   ```
   kubectl describe serviceaccount llamacloud-llamaparse
   ```

4. **Check secret mounting**:

   Terminal window

   ```
   kubectl describe pod <pod-name> | grep -A 20 Environment
   ```
