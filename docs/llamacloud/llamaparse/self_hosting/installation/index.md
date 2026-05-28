---
title: Quick Start | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

Note

This page assumes that you are deploying the latest version of LlamaCloud. Please refer to the [release notes](https://github.com/run-llama/helm-charts/releases) for more information about previous versions.

## Before You Get Started

Welcome to LlamaCloud! Before you get started, please make sure you have the following prerequisites:

- **LlamaCloud License Key**. To obtain a LlamaCloud License Key, please contact us at [support@llamaindex.ai](mailto:contact@llamaindex.ai).

- **Kubernetes cluster `>=1.28.0`** and a working installation of `kubectl`.
  - We are largely aligned with the versions supported in [EKS](https://endoflife.date/amazon-eks), [AKS](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions?tabs=azure-cli), and [GKE](https://cloud.google.com/kubernetes-engine/versioning).

- **Helm `v3.7.0+`**
  - To install Helm, please refer to the [official Helm Documentation](https://helm.sh/docs/intro/install/).

- **OpenAI API Key** or **Azure OpenAI Credentials**. Configuring OpenAI credentials is the easiest way to get started with your deployment.

  - LlamaCloud tries to meet you at your organization’s needs and supports configuring more than OpenAI LLMs in including Anthropic, Bedrock, Vertex AI, and more.
  - Please refer to the docs in the **Configuration** section of the sidebar to learn more about configuring other LLMs.

- **File Storage**: LlamaCloud must leverage your cloud provider’s object storage to store files.
  - Please follow the [File Storage](/llamaparse/self_hosting/configuration/file-storage/index.md) documentation to configure your deployment.

- **Authentication Settings**:

  - **OIDC**. OIDC is our recommended authentication mode for production deployments.
  - **Basic Auth** (email/password): As of July 24th, 2025 (`v0.5.0`), we support both `oidc` and `basic` authentication methods. This is a simpler authentication mode more suitable for staging deployments.
  - For more information, please refer to the [Authentication Modes](/llamaparse/self_hosting/configuration/auth-modes/index.md) documentation.

- **Credentials to External Services (See below)**.

## External Services

**LLamaCloud** requires the following external services to be available: **Postgres**, **MongoDB**, **Temporal**, **RabbitMQ** and **Redis**.

Tip

**Temporal** can be deployed as a subchart within LlamaCloud by setting `temporal.deploy: true`. This is the recommended approach for getting started quickly. For production deployments, you may prefer to manage Temporal separately.

Please follow the [Database and Queues](/llamaparse/self_hosting/configuration/db_and_queues/overview/index.md) documentation to configure these services for your deployment.

## Hardware Requirements

- **Linux Instances running x86 CPUs**
  - We currently only linux/amd64 images. arm64 is not supported at this moment.
- **Ubuntu >=22.04**
- **>=12 vCPUs**
- **>=80Gbi Memory**

**Warning #1**: LlamaParse, LlamaIndex’s proprietary document parser, can be a very resource-intensive deployment to run, especially if you want to maximize performance.

**Warning #2**: The base CPU/memory requirements may increase if you are running containerized deployments of LlamaCloud dependencies. (More information in the following section)

## Configure and Install Your Deployment

This section will walk you through the steps to configure a minimal LlamaCloud deployment.

### Minimal `values.yaml` configuration

To get a minimal LlamaCloud deployment up and running, you can create a `values.yaml` file with the following content:

- [OpenAI w/ OIDC Auth](#tab-panel-36)
- [Azure OpenAI w/ OIDC Auth](#tab-panel-37)
- [OpenAI w/ Basic Auth](#tab-panel-38)
- [Azure OpenAI w/ Basic Auth](#tab-panel-39)

```
  license:
    key: <LLAMACLOUD-LICENSE-KEY>


  postgresql:
    host: "postgresql"
    port: "5432"
    database: "llamacloud"
    username: <POSTGRES-USERNAME>
    password: <POSTGRES-PASSWORD>


  mongodb:
    host: "mongodb"
    port: "27017"
    username: <MONGODB-USERNAME>
    password: <MONGODB-PASSWORD>


  rabbitmq:
    scheme: "amqp"
    host: "rabbitmq"
    port: "5672"
    username: <RABBITMQ-USERNAME>
    password: <RABBITMQ-PASSWORD>


  redis:
    scheme: "redis"
    host: "redis-master"
    port: "6379"
    db: 0


  # Deploy Temporal as a subchart (host/port auto-configured)
  temporal:
    deploy: true


  # Temporal subchart configuration (uses same PostgreSQL instance)
  temporal-subchart:
    server:
      config:
        persistence:
          default:
            sql:
              driver: postgres12
              host: "postgresql"
              port: 5432
              database: temporal
              user: <POSTGRES-USERNAME>
              password: <POSTGRES-PASSWORD>
          visibility:
            sql:
              driver: postgres12
              host: "postgresql"
              port: 5432
              database: temporal_visibility
              user: <POSTGRES-USERNAME>
              password: <POSTGRES-PASSWORD>


  config:
    llms:
      openAi:
        apiKey: <OPENAI-APIKEY>


    frontend:
      enabled: true
    parseOcr:
      gpu: true


    authentication:
      oidc:
        enabled: true
        discoveryUrl: "https://login.microsoftonline.com/<TENANT-ID>/v2.0/.well-known/openid-configuration"
        clientId: <CLIENT-ID>
        clientSecret: <CLIENT-SECRET>
```

```
  license:
    key: <LLAMACLOUD-LICENSE-KEY>


  postgresql:
    host: "postgresql"
    port: "5432"
    database: "llamacloud"
    username: <POSTGRES-USERNAME>
    password: <POSTGRES-PASSWORD>


  mongodb:
    host: "mongodb"
    port: "27017"
    username: <MONGODB-USERNAME>
    password: <MONGODB-PASSWORD>


  rabbitmq:
    scheme: "amqp"
    host: "rabbitmq"
    port: "5672"
    username: <RABBITMQ-USERNAME>
    password: <RABBITMQ-PASSWORD>


  redis:
    scheme: "redis"
    host: "redis-master"
    port: "6379"
    db: 0


  # Deploy Temporal as a subchart (host/port auto-configured)
  temporal:
    deploy: true


  # Temporal subchart configuration (uses same PostgreSQL instance)
  temporal-subchart:
    server:
      config:
        persistence:
          default:
            sql:
              driver: postgres12
              host: "postgresql"
              port: 5432
              database: temporal
              user: <POSTGRES-USERNAME>
              password: <POSTGRES-PASSWORD>
          visibility:
            sql:
              driver: postgres12
              host: "postgresql"
              port: 5432
              database: temporal_visibility
              user: <POSTGRES-USERNAME>
              password: <POSTGRES-PASSWORD>


  config:
    llms:
      azureOpenAi:
        secret: ""
        deployments: []


    frontend:
      enabled: true
    parseOcr:
      gpu: true


    authentication:
      oidc:
        enabled: true
        discoveryUrl: "https://login.microsoftonline.com/<TENANT-ID>/v2.0/.well-known/openid-configuration"
        clientId: <CLIENT-ID>
        clientSecret: <CLIENT-SECRET>
```

```
  license:
    key: <LLAMACLOUD-LICENSE-KEY>


  postgresql:
    host: "postgresql"
    port: "5432"
    database: "llamacloud"
    username: <POSTGRES-USERNAME>
    password: <POSTGRES-PASSWORD>


  mongodb:
    host: "mongodb"
    port: "27017"
    username: <MONGODB-USERNAME>
    password: <MONGODB-PASSWORD>


  rabbitmq:
    scheme: "amqp"
    host: "rabbitmq"
    port: "5672"
    username: <RABBITMQ-USERNAME>
    password: <RABBITMQ-PASSWORD>


  redis:
    scheme: "redis"
    host: "redis-master"
    port: "6379"
    db: 0


  # Deploy Temporal as a subchart (host/port auto-configured)
  temporal:
    deploy: true


  # Temporal subchart configuration (uses same PostgreSQL instance)
  temporal-subchart:
    server:
      config:
        persistence:
          default:
            sql:
              driver: postgres12
              host: "postgresql"
              port: 5432
              database: temporal
              user: <POSTGRES-USERNAME>
              password: <POSTGRES-PASSWORD>
          visibility:
            sql:
              driver: postgres12
              host: "postgresql"
              port: 5432
              database: temporal_visibility
              user: <POSTGRES-USERNAME>
              password: <POSTGRES-PASSWORD>


  config:
    llms:
      openAi:
        apiKey: <OPENAI-APIKEY>


    frontend:
      enabled: true
    parseOcr:
      gpu: true


    authentication:
      basicAuth:
        enabled: true
          validEmailDomain: "llamaindex.ai" # this is optional, but recommended for production deployments
          jwtSecret: <YOUR-JWT-SECRET>
```

```
  license:
    key: <LLAMACLOUD-LICENSE-KEY>


  postgresql:
    host: "postgresql"
    port: "5432"
    database: "llamacloud"
    username: <POSTGRES-USERNAME>
    password: <POSTGRES-PASSWORD>


  mongodb:
    host: "mongodb"
    port: "27017"
    username: <MONGODB-USERNAME>
    password: <MONGODB-PASSWORD>


  rabbitmq:
    scheme: "amqp"
    host: "rabbitmq"
    port: "5672"
    username: <RABBITMQ-USERNAME>
    password: <RABBITMQ-PASSWORD>


  redis:
    scheme: "redis"
    host: "redis-master"
    port: "6379"
    db: 0


  # Deploy Temporal as a subchart (host/port auto-configured)
  temporal:
    deploy: true


  # Temporal subchart configuration (uses same PostgreSQL instance)
  temporal-subchart:
    server:
      config:
        persistence:
          default:
            sql:
              driver: postgres12
              host: "postgresql"
              port: 5432
              database: temporal
              user: <POSTGRES-USERNAME>
              password: <POSTGRES-PASSWORD>
          visibility:
            sql:
              driver: postgres12
              host: "postgresql"
              port: 5432
              database: temporal_visibility
              user: <POSTGRES-USERNAME>
              password: <POSTGRES-PASSWORD>


  config:
    llms:
      azureOpenAi:
        secret: ""
        deployments: []


    frontend:
      enabled: true
    parseOcr:
      gpu: true


    authentication:
      basicAuth:
        enabled: true
        validEmailDomain: "llamaindex.ai" # this is optional, but recommended for production deployments
        jwtSecret: <YOUR-JWT-SECRET>
```

## Install the Helm chart

Terminal window

```
# Add the Helm repository
helm repo add llamaindex https://run-llama.github.io/helm-charts


# Update your local Helm chart cache
helm repo update


# Create the llamacloud namespace
kubectl create ns llamacloud


# Install the Helm chart
helm install llamacloud llamaindex/llamacloud -f values.yaml --namespace llamacloud
```

If you want to install a specific version of the Helm chart, you can specify the version:

Terminal window

```
helm install llamacloud llamaindex/llamacloud --version x.y.z -f values.yaml --namespace llamacloud
```

## Validate the installation

After installation, you will see the following output:

```
NNAME: llamacloud
LAST DEPLOYED: Tue Nov 18 10:12:03 2025
NAMESPACE: llamacloud
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Welcome to LlamaCloud!


View your deployment with the following:


  kubectl --namespace default get pods -n llamacloud


To view LlamaCloud UI in your browser:
  Run the following command:


  kubectl --namespace llamacloud port-forward svc/llamacloud-web 3000:80
```

If you list the pods with `kubectl get pods -n llamacloud`, you should see the following pods:

```
NAME                                        READY   STATUS      RESTARTS     AGE
llamacloud-64f468d5cf-sqjq6                 1/1     Running     0            2m56s
llamacloud-layout-6d97b84c58-rld8x          1/1     Running     0            2m56s
llamacloud-ocr-5cc459bdd-99xgt              1/1     Running     0            2m56s
llamacloud-operator-5d4c58b854-dwnjk        1/1     Running     0            2m56s
llamacloud-parse-7ffbc786b5-r98w2           1/1     Running     0            2m56s
llamacloud-telemetry-5fc9ff8c67-fv8xj       1/1     Running     0            2m56s
llamacloud-web-b88d95588-rprhc              1/1     Running     0            2m56s
llamacloud-worker-58b95ccc6f-vqmgx          1/1     Running     0            2m56s
```

Port forward the frontend service to access the LlamaCloud UI:

Terminal window

```
kubectl --namespace llamacloud port-forward svc/llamacloud-web 3000:80
```

Open your web browser and navigate to `http://localhost:3000`. You should see the LlamaCloud UI.

## Next Steps

Choose your deployment approach based on your needs:

### 🌩️ Cloud-Specific Deployment Guides

**Recommended for most users** - Complete, opinionated guides for major cloud providers:

**[📋 Choose Your Cloud Provider →](/llamaparse/self_hosting/cloud-specific-guides/overview/index.md)**

- **Azure**: AKS + Azure-native services with Microsoft Entra ID
- **AWS**: EKS + AWS-native services (coming soon)
- **GCP**: GKE + GCP-native services (coming soon)

*These guides provide end-to-end instructions using cloud-native services and enterprise authentication.*

### ⚙️ Custom Configuration Guides

**For advanced users** with specific requirements or non-standard setups:

- [Authentication Modes](/llamaparse/self_hosting/configuration/auth-modes/index.md) - Configure OIDC, basic auth, or custom authentication
- [File Storage](/llamaparse/self_hosting/configuration/file-storage/index.md) - Set up S3, Azure Blob, GCS, or other storage
- [Database and Queues](/llamaparse/self_hosting/configuration/db_and_queues/overview/index.md) - Configure external databases and message queues
- [LLM Integrations](/llamaparse/self_hosting/configuration/llm_integrations/overview/index.md) - Set up OpenAI, Azure OpenAI, Bedrock, or other LLMs
- [Ingress Configuration](/llamaparse/self_hosting/configuration/ingress/index.md) - Load balancers, SSL, and networking
- [Autoscaling Configuration](/llamaparse/self_hosting/configuration/autoscaling-configuration/index.md) - HPA and KEDA-based scaling for services
- [Service Tuning](/llamaparse/self_hosting/tuning/service-configurations/index.md) - Performance and scaling configurations

*Use these guides if you need custom integrations, have specific compliance requirements, or want to mix and match different services.*

### 🚰 Data Sink Configuration

Configure at least one [Data Sink](/llamaparse/cloud-index/integrations/data_sinks/index.md) to store the **vector embeddings** of your documents.

## More Examples and Guides

- there are many more configuration options available for each component. to see the full values.yaml specification, please refer to the [values.yaml](https://github.com/run-llama/helm-charts/blob/main/charts/llamacloud/values.yaml) file in the helm chart repository.
- To see how common scenarios are configured, please refer to the `values.yaml` [examples](https://github.com/run-llama/helm-charts/tree/main/charts/llamacloud/examples) directory in the Helm chart repository.
- Similarly, we have other configuration [docs](https://github.com/run-llama/helm-charts/tree/main/charts/llamacloud/docs) available there too for more advanced configurations.
