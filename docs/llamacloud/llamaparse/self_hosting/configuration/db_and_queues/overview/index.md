---
title: Overview | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

LlamaCloud requires a few external dependencies — Postgres, MongoDB, Redis, and RabbitMQ.

## Requirements

We officially support the following versions of the dependencies:

- **Postgres**

  - Minimum Version `>=15.x`

  - Admin Access to the database. LlamaCloud will read/write and apply migrations.

  - We recommend `1 - 2 vCPUs` and `1 - 2 GBi RAM` as a starting point for the database. As your usage grows, you can scale the database accordingly.

  - Recommended Managed Services:

    - [Amazon RDS](https://aws.amazon.com/rds/)
    - [Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/single-server/quickstart-create-server-database-portal)
    - [Google Cloud SQL](https://cloud.google.com/curated-resources/cloud-sql)

- **MongoDB**

  - Minimum Version `>=7.x`

  - We recommend `1 - 2 vCPUs` and `1 - 2 GBi RAM` as a starting point for the database. As your usage grows, you can scale the database accordingly.

  - Recommended Managed Services:

    - [Amazon DocumentDB](https://aws.amazon.com/documentdb/)
    - [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/introduction)
    - [Google Cloud](https://cloud.google.com/mongodb)

- **RabbitMQ**

  - Minimum Version `>=3.11.x`

  - We recommend `200 - 500m vCPUs` and `500Mi - 2GBi RAM` as a starting point for the database. As your usage grows, you can scale the database accordingly.

  - Recommended Managed Services:

    - [Amazon MQ](https://aws.amazon.com/amazon-mq/)
    - [Azure Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) — see setup: [Azure Service Bus as Job Queue](/llamaparse/self_hosting/configuration/db_and_queues/azure-service-bus/index.md)
    - [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/google/rabbitmq)

- **Redis**

  - Minimum Version `>=7.x`

  - We recommend `200 - 500m vCPUs` and `500Mi - 2GBi RAM` as a starting point for the database. As your usage grows, you can scale the database accordingly.

  - Recommended Managed Services:

    - [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
    - [Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview)
    - [Google Cloud Memorystore](https://cloud.google.com/memorystore/docs/redis)

- **Temporal**

## External Dependency Configuration

To connect your LlamaCloud deployment to an external dependency, configure the necessary sections in your `values.yaml` file.

- [With Temporal Subchart (Recommended)](#tab-panel-564)
- [External Temporal](#tab-panel-565)

```
postgresql:
  host: "postgresql"
  port: "5432"
  database: "llamacloud"
  username: "llamacloud"
  password: "llamacloud"


mongodb:
  host: "mongodb"
  port: "27017"
  username: "root"
  password: "password"


rabbitmq:
  scheme: "amqp"
  host: "rabbitmq"
  port: "5672"
  username: "guest"
  password: "guest"


redis:
  scheme: "redis"
  host: "redis-master"
  port: "6379"
  db: 0


# Deploy Temporal as a subchart (host/port auto-configured)
temporal:
  deploy: true


# Temporal subchart configuration
temporal-subchart:
  server:
    config:
      persistence:
        default:
          sql:
            driver: postgres12
            host: <postgresql-host>
            port: 5432
            database: temporal
            user: <username>
            password: <password>
        visibility:
          sql:
            driver: postgres12
            host: <postgresql-host>
            port: 5432
            database: temporal_visibility
            user: <username>
            password: <password>
```

```
postgresql:
  host: "postgresql"
  port: "5432"
  database: "llamacloud"
  username: "llamacloud"
  password: "llamacloud"


mongodb:
  host: "mongodb"
  port: "27017"
  username: "root"
  password: "password"


rabbitmq:
  scheme: "amqp"
  host: "rabbitmq"
  port: "5672"
  username: "guest"
  password: "guest"


redis:
  scheme: "redis"
  host: "redis-master"
  port: "6379"
  db: 0


# Use an existing external Temporal deployment
temporal:
  deploy: false
  host: temporal-frontend
  port: 7233
```

## Example Postgresql Configuration

Example Postgresql installation:

```
helm upgrade --install postgresql \
    oci://registry-1.docker.io/bitnamicharts/postgresql \
    -f postgresql.yaml --wait --timeout 10m
```

postgresql.yaml

```
image:
  registry: docker.io
  repository: bitnamilegacy/postgresql


auth:
  enabled: true
  database: llamacloud
  username: llamacloud
  password: llamacloud


## Ref: https://github.com/bitnami/charts/blob/main/bitnami/postgresql/values.yaml#L481
primary:
  resources:
    requests:
      cpu: 250m
      memory: 128Mi
    limits:
      cpu: 250m
      memory: 256Mi


global:
  security:
    allowInsecureImages: true


resourcesPreset: micro
```

## Example MongoDB Configuration

Example MongoDB installation:

```
helm upgrade --install \
  mongodb oci://registry-1.docker.io/bitnamicharts/mongodb \
  -f mongodb.yaml --wait --timeout 10m
```

mongodb.yaml

```
image:
  registry: ghcr.io
  repository: xavidop/mongodb
  tag: '7.0'


auth:
  enabled: true
  rootUser: root
  rootPassword: password


global:
  security:
    allowInsecureImages: true


resourcesPreset: micro
```

## Example Redis Configuration

Example Redis installation:

```
helm upgrade --install redis \
  oci://registry-1.docker.io/bitnamicharts/redis \
  -f redis.yaml --wait --timeout 10m
```

redis.yaml

```
image:
  registry: docker.io
  repository: bitnamilegacy/redis


auth:
  enabled: false
  #password: "password"


tls:
  enabled: false


architecture: standalone


global:
  security:
    allowInsecureImages: true


resourcesPreset: micro
```

## Example RabbitMQ Configuration

Example RabbitMQ installation:

```
helm upgrade --install rabbitmq \
  oci://registry-1.docker.io/bitnamicharts/rabbitmq \
  -f rabbitmq.yaml --wait --timeout 10m
```

rabbimq.yaml

```
image:
  registry: docker.io
  repository: bitnamilegacy/rabbitmq
  digest: sha256:8a36cf44a55be2ae25cafa0376b89041412c50bbcab9fa0109713d60b2ec06fb


global:
  security:
    allowInsecureImages: true


auth:
  username: guest
  password: guest
  erlangCookie: secretcookie


resourcesPreset: micro
```

## Example Temporal Configuration

LlamaCloud supports two approaches for deploying Temporal:

### Option 1: Deploy Temporal as a Subchart (Recommended)

The simplest way to deploy Temporal is as a subchart within LlamaCloud. This approach automatically configures the Temporal host and port for LlamaCloud services.

In your `values.yaml`, set `temporal.deploy: true` and configure the `temporal-subchart` section:

```
# Deploy Temporal as a subchart
temporal:
  deploy: true


# Temporal subchart configuration
temporal-subchart:
  serviceAccount:
    create: true
    name: temporal-server


  web:
    additionalEnv:
      - name: TEMPORAL_CSRF_COOKIE_INSECURE
        value: "true"
    service:
      port: 80


  server:
    config:
      persistence:
        default:
          driver: "sql"
          sql:
            driver: postgres12
            host: <postgresql-host>
            port: 5432
            database: temporal
            user: <username>
            password: <password>
            maxConns: 20
            maxIdleConns: 20
            maxConnLifetime: "1h"


        visibility:
          driver: "sql"
          sql:
            driver: postgres12
            host: <postgresql-host>
            port: 5432
            database: temporal_visibility
            user: <username>
            password: <password>
            maxConns: 20
            maxIdleConns: 20
            maxConnLifetime: "1h"


  cassandra:
    enabled: false
  mysql:
    enabled: false
  postgresql:
    enabled: false
  prometheus:
    enabled: false
  grafana:
    enabled: false
  elasticsearch:
    enabled: false


  schema:
    createDatabase:
      enabled: true
    setup:
      enabled: true
    update:
      enabled: true
```

Tip

When using `temporal.deploy: true`, you don’t need to specify `temporal.host` or `temporal.port` - these are automatically configured to point to the subchart’s frontend service.

### Option 2: Use an External Temporal Deployment

If you already have a Temporal deployment or prefer to manage Temporal separately, you can connect LlamaCloud to an external Temporal instance.

First, install Temporal separately:

```
helm install --repo https://go.temporal.io/helm-charts \
  temporal temporal -f temporal.yaml
```

temporal.yaml

```
serviceAccount:
  create: true
  name: temporal-server


web:
  additionalEnv:
    - name: TEMPORAL_CSRF_COOKIE_INSECURE
      value: "true"
  service:
    port: 80


server:
  config:
    namespaces:
      create: true
    persistence:
      default:
        driver: "sql"
        sql:
          driver: postgres12
          host: <hostname>
          port: 5432
          database: temporal
          user: <username>
          password: <password>
          maxConns: 20
          maxIdleConns: 20
          maxConnLifetime: "1h"


      visibility:
        driver: "sql"
        sql:
          driver: postgres12
          host: <hostname>
          port: 5432
          database: temporal_visibility
          user: <username>
          password: <password>
          maxConns: 20
          maxIdleConns: 20
          maxConnLifetime: "1h"


cassandra:
  enabled: false
mysql:
  enabled: false
postgresql:
  enabled: false
prometheus:
  enabled: false
grafana:
  enabled: false
elasticsearch:
  enabled: false


schema:
  createDatabase:
    enabled: true
  setup:
    enabled: true
  update:
    enabled: true
```

Then configure LlamaCloud to connect to your external Temporal:

```
# LlamaCloud values.yaml
temporal:
  deploy: false
  host: temporal-frontend  # Your Temporal frontend service name
  port: 7233
```

## Complete Configuration Reference

For the most up-to-date and comprehensive configuration options, refer directly to our Helm repository:

- **[Complete values.yaml reference](https://github.com/run-llama/helm-charts/blob/main/charts/llamacloud/values.yaml)** - Full configuration options with detailed comments
- **[External dependencies example](https://github.com/run-llama/helm-charts/blob/main/charts/llamacloud/examples/external-deps-config.yaml)** - Complete working example for external dependencies
- **[Helm chart documentation](https://github.com/run-llama/helm-charts/blob/main/charts/llamacloud/README.md)** - Generated documentation with all configuration parameters

Tip

The Helm repository is the authoritative source for configuration. It’s always up-to-date with the latest chart version and includes working examples and tests.
