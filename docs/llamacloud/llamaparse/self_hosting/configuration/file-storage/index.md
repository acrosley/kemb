---
title: File Storage | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

File storage is an integral part of LlamaCloud. Without it, many key features would not be possible. This page walks through how to configure file storage for your deployment — which buckets you need to create and for non-AWS deployments, how to configure the S3 Proxy to interact with them.

## Requirements

- A valid blob storage service. We recommend the following:

  - [Amazon S3](https://aws.amazon.com/s3/)
  - [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
  - [Google Cloud Storage](https://cloud.google.com/storage)

- Because LlamaCloud heavily relies on file storage, you will need to create the following buckets:

  - `llama-platform-parsed-documents`
  - `llama-platform-etl`
  - `llama-platform-external-components`
  - `llama-platform-file-parsing`
  - `llama-platform-raw-files`
  - `llama-cloud-parse-output`
  - `llama-platform-file-screenshots`
  - `llama-platform-extract-output` (for `LlamaExtract`)

## Connecting to AWS S3

Below are two ways to configure a connection to AWS S3:

### (Recommended) IAM Role for Service Accounts

We recommend that users create a new IAM Role and Policy for LlamaCloud. You can then attach the role ARN as a service account annotation.

```
// Example IAM Policy
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:*"], // this is not secure
      "Resource": [
        "arn:aws:s3:::llama-platform-parsed-documents",
        "arn:aws:s3:::llama-platform-parsed-documents/*",
        ...
      ]
    }
  ]
}
```

After creating something similar to the above policy, update the `backend`, `jobsService`, `jobsWorker`, and `llamaParse` service accounts with the EKS annotation.

```
# Example for the backend service account. Repeat for each of the services listed above.
backend:
  serviceAccountAnnotations:
      eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<role-name>
```

For more information, feel free to refer to the [official AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) about this topic.

### AWS Credentials

Create a user with a policy attached for the aforementioned s3 buckets. Afterwards, you can configure the platform to use the aws credentials of that user by setting the following values in your `values.yaml` file:

```
config:
  storageBuckets:
    provider: "aws"
    s3proxy:
      enabled: true
      containerPort: 8080
      config:
        JCLOUDS_PROVIDER: "aws-s3"
        JCLOUDS_IDENTITY: <AWS-ACCESS-KEY>
        JCLOUDS_CREDENTIAL: <AWS-SECRET-KEY>
        JCLOUDS_REGION: <AWS-REGION>  # e.g. "us-east-1"
        JCLOUDS_ENDPOINT: "https://s3.<AWS-REGION>.amazonaws.com"
```

## Overriding Default Bucket Names

We allow users to override the default bucket names in the `values.yaml` file.

```
  config:
    storageBuckets:
      parsedDocuments: "<your-bucket-name>"
      parsedEtl: "<your-bucket-name>"
      parsedExternalComponents: "<your-bucket-name>"
      parsedFileParsing: "<your-bucket-name>"
      parsedRawFile: "<your-bucket-name>"
      parseOutput: "<your-bucket-name>"
      parsedFileScreenshot: "<your-bucket-name>"
      extractOutput: "<your-bucket-name>"
      parseFileUpload: "<your-bucket-name>"
      parseFileOutput: "<your-bucket-name>"
```

## Advanced S3 Configuration

For deployments using KMS server-side encryption or custom S3-compatible backends, you may need to configure the S3 signature version. By default, the platform defers to botocore’s automatic region-based resolution. If your buckets use AWS KMS encryption and presigned URLs fail with a signature version error, set `S3_SIGNATURE_VERSION` to `s3v4`:

```
config:
  storageBuckets:
    signatureVersion: "s3v4"
```

Note

This is typically only needed when using KMS-encrypted S3 buckets in deployments where `AWS_REGION` is not set in the pod environment. IRSA provides credentials but does not always set the region, which can cause botocore to generate presigned URLs with the wrong signature version.

Alternatively, you can set `AWS_REGION` via `extraEnvVariables`:

```
config:
  storageBuckets:
    extraEnvVariables:
      AWS_REGION: "us-east-1"
```

## Connecting to Azure Blob Storage or Other Providers with S3Proxy

LlamaCloud was first developed on AWS, which means that we started by natively supporting S3. However, to make a self-hosted solution possible, we need a way for the platform to interact with other providers.

We leverage the open-source project [S3Proxy](https://github.com/gaul/s3proxy) to translate the S3 API requests into requests to other storage providers. A containerized deployment of S3Proxy is supported out of the box in our helm charts.

S3Proxy should always be set to `enabled: true`, even when deploying LlamaCloud on AWS. This causes S3Proxy to be deployed as a sidecar on several of the LlamaCloud pods.

The following is an example for how to connect your LlamaCloud deployment to Azure Blob Storage. For more examples of connecting to different providers, please refer to the project’s [Examples](https://github.com/gaul/s3proxy/wiki/Storage-backend-examples) page.

- [Azure Blob Storage with S3 Proxy](#tab-panel-189)

```
config:
  storageBuckets:
    provider: "azure"
    s3proxy:
      enabled: true
      containerPort: 8080
      config:
        S3PROXY_ENDPOINT: "http://0.0.0.0:80"
        S3PROXY_AUTHORIZATION: "none"
        S3PROXY_IGNORE_UNKNOWN_HEADERS: "true"
        S3PROXY_CORS_ALLOW_ORIGINS: "*"
        JCLOUDS_PROVIDER: "azureblob"
        JCLOUDS_REGION: "eastus" # Change to your region
        JCLOUDS_AZUREBLOB_AUTH: "azureKey"
        JCLOUDS_IDENTITY: "fill-out" # Change to your storage account name
        JCLOUDS_CREDENTIAL: "fill-out" # Change to your storage account key
        JCLOUDS_ENDPOINT: "fill-out" # Change to your storage account endpoint
```
