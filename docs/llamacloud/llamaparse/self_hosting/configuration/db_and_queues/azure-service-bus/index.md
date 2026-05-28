---
title: Azure Service Bus as Job Queue | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

LlamaCloud’s job queue is AMQP-compatible. You can use Azure Service Bus instead of a self-managed RabbitMQ by supplying a Service Bus connection string in your Helm values.

## Prerequisites

- An Azure Service Bus namespace.

- Namespace tier: Standard or higher (Basic is not supported).

- A connection string with Manage, Send, and Listen permissions.

  - Manage is needed so LlamaCloud can validate and, if necessary, create the queues on startup.
  - How to find it: <https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues?tabs=connection-string>

## Configure via values.yaml (Recommended)

Update your `values.yaml` as follows:

```
rabbitmq:
  connectionString: "Endpoint=sb://<namespace>.servicebus.windows.net/;SharedAccessKeyName=<policy>;SharedAccessKey=<key>;EntityPath=<queue-name>"
```

## Configure via Kubernetes Secret (Optional)

For production, you may prefer a secret instead of inlining credentials.

LlamaCloud reads the Azure Service Bus connection string from the `JOB_QUEUE_CONNECTION_STRING` environment variable. When supplying a Kubernetes Secret via `rabbitmq.secret`, ensure the secret contains a key named `JOB_QUEUE_CONNECTION_STRING` whose value is the full Service Bus connection string.

1. Create a secret with the connection string:

Terminal window

```
kubectl create secret generic my-queue-secret \
  --from-literal=JOB_QUEUE_CONNECTION_STRING='Endpoint=sb://<namespace>.servicebus.windows.net/;SharedAccessKeyName=<policy>;SharedAccessKey=<key>;EntityPath=<queue-name>'
```

2. Reference the secret in `values.yaml`:

```
rabbitmq:
  secret: my-queue-secret
```

## Verify

- Upgrade your release and ensure pods start successfully.
- Services will log successful connections to the job queue; check `llamacloud-worker` and `llamacloud-parse` pods for confirmation.
