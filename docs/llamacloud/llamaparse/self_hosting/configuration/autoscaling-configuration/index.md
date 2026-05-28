---
title: Autoscaling | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

Configure autoscaling for LlamaCloud services to automatically scale based on resource utilization or queue depth.

## Overview

LlamaCloud supports two autoscaling approaches:

1. **Standard HPA (Default)** - CPU/memory-based scaling using Kubernetes HPA
2. **KEDA-based scaling (Recommended for Production)** - Queue-depth based scaling for better workload responsiveness

Both options are configured through Helm values and provide automatic scaling based on different metrics to ensure optimal resource utilization.

## Autoscaling Options

### Standard HPA

- **Metrics**: CPU and memory utilization
- **Best for**: General workloads, development environments
- **Setup**: Enabled by default, no additional components required

### KEDA-based Scaling

- **Metrics**: Queue depth from LlamaCloud API
- **Best for**: Production workloads with variable processing queues
- **Setup**: Requires KEDA operator installation
- **Advantage**: Scales based on actual work to be done, not just resource usage

## Prerequisites

### For Standard HPA

- Kubernetes Metrics Server (usually pre-installed)

### For KEDA-based Scaling

- **KEDA Operator** installed in your Kubernetes cluster
- LlamaCloud version 0.5.8+ (for queue status API)

Note

For KEDA installation instructions, see the [official KEDA deployment guide](https://keda.sh/docs/2.18/deploy/). KEDA offers multiple installation methods including Helm, Operator Hub, YAML files, and MicroK8s deployment options.

## Helm Configuration

### Option 1: Standard HPA (Default)

By default, LlamaParse uses standard Kubernetes HPA based on CPU and memory metrics:

```
# Basic HPA configuration (enabled by default)
llamaParse:
  horizontalPodAutoscalerSpec:
    minReplicas: 2
    maxReplicas: 8
    metrics:
    - resource:
        name: cpu
        target:
          averageUtilization: 40
          type: Utilization
      type: Resource
    - resource:
        name: memory
        target:
          averageUtilization: 60
          type: Utilization
      type: Resource
    scaleTargetRef:
      apiVersion: apps/v1
      kind: Deployment
      name: llamacloud-parse
```

Other services can also be scaled in this way, e.g. `backend`.

### Option 2: KEDA Queue-Based Scaling (Recommended for Production)

We recommend KEDA-based configuration for more robust queue-depth based scaling in production. **Note: You must disable HPA when using KEDA.**

Note

**LlamaCloud Queue Status API**\
LlamaCloud exposes a `/api/queue-statusz` endpoint to monitor queue depth for scaling decisions. The API returns information about job queues including message counts, and KEDA specifically uses the `total_messages` field to determine when to scale up or down. You can filter queues using `?queue_prefix=parse_raw_file_job` to monitor only LlamaParse jobs. Available since LlamaCloud v0.5.8.

```
# KEDA configuration for queue-based scaling
extraObjects:
- apiVersion: keda.sh/v1alpha1
  kind: ScaledObject
  metadata:
    name: llamacloud-parse
    namespace: <your-namespace>
  spec:
    cooldownPeriod: 120
    initialCooldownPeriod: 0
    maxReplicaCount: 10
    minReplicaCount: 1
    pollingInterval: 15
    scaleTargetRef:
      apiVersion: apps/v1
      kind: Deployment
      name: llamacloud-parse
    triggers:
    - metadata:
        activationTargetQueueSize: "0"
        endpoint: "http://llamacloud:80/api/queue-statusz?queue_prefix=parse_raw_file_job"
        targetQueueSize: "20"
        taskQueue: llamacloud-all
      type: temporal
```

Note

For detailed configuration options and scaling behavior with KEDA’s metrics-api scaler, see the [KEDA Metrics API Scaler documentation](https://keda.sh/docs/2.17/scalers/metrics-api/).

## OCR Pod Scaling Based on LlamaParse Worker Pods

For workloads that use OCR services, you can configure KEDA to scale OCR pods based on the number of LlamaParse worker pods. This ensures OCR capacity matches parsing demand.

### KEDA Configuration for OCR Scaling

The OCR pod scaling uses KEDA’s ability to monitor the number of running LlamaParse Worker pods and applies the formula: `Min(3, llamaparse_pods / 3)` to determine the optimal number of OCR pods.

```
# OCR scaling configuration based on LlamaParse Worker pods
extraObjects:
- apiVersion: keda.sh/v1alpha1
  kind: ScaledObject
  metadata:
    name: llamacloud-ocr
    namespace: <your-namespace>
  spec:
    cooldownPeriod: 120
    initialCooldownPeriod: 0
    maxReplicaCount: 10
    minReplicaCount: 1
    pollingInterval: 15
    scaleTargetRef:
      apiVersion: apps/v1
      kind: Deployment
      name: llamacloud-ocr
    triggers:
    - metadata:
        activationTargetQueueSize: "0"
        endpoint: "http://llamacloud:80/api/queue-statusz?queue_prefix=parse_raw_file_job"
        targetQueueSize: "20"
        taskQueue: llamacloud-all
      type: temporal
```

### Scaling Logic

OCR pods scale based on parse job count using the formula `Min(3, estimated_parse_workers / 3)`. The target value of 60 assumes \~20 jobs per LlamaParse Worker pod, maintaining a 3:1 LlamaParse Worker to OCR pod ratio for optimal resource efficiency.

Note

**OCR Scaling Tips**

- Adjust `targetValue` based on your job processing rate per LlamaParse Worker pod
- Monitor utilization and tune the 3:1 scaling ratio as needed, especially if your documents usually have a lot of images or almost none
- If you’re running OCR on CPU pods instead of GPU, use the same rule as LlamaParse worker to have a 1:1 ratio.
