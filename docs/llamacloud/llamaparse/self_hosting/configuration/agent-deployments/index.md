---
title: Agent Deployments | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

Users of your LlamaCloud install can build agents in code, deploy them through the UI or API, and get an HTTP endpoint at `/deployments/<agent-name>` that runs their agent as a pod in the cluster. LlamaCloud’s parent ingress already routes `/deployments/*` to the backend, so there’s no agent-specific ingress setup to do. But the components that actually build and run agent pods (a control plane API, a Kubernetes operator that reconciles `LlamaDeployment` custom resources, and an S3-compatible bucket for build artifacts and backups) live in a separate [`llama-agents`](https://github.com/run-llama/llama-agents/tree/main/charts/llama-agents) Helm chart.

As a cluster operator you have two choices: run `llama-agents` as an in-cluster subchart of LlamaCloud, or manage it separately. In-cluster is the common case.

Set `llamaAgents.deploy: true` and the LlamaCloud chart pulls the subchart in, wires the backend feature flag, and renders a NetworkPolicy allowing agent pods to reach the backend on port 8000.

```
llamaAgents:
  deploy: true
```

## Subchart values

Pass-through values go under `llama-agents-subchart`. The full surface lives in the upstream [`llama-agents` chart README](https://github.com/run-llama/llama-agents/tree/main/charts/llama-agents); the values below are the common ones.

### Object storage

The subchart needs an S3-compatible bucket for build artifacts, backups, and git repos. Credentials come from a K8s Secret containing `S3_ACCESS_KEY` and `S3_SECRET_KEY`.

```
llama-agents-subchart:
  controlPlane:
    objectStorage:
      s3:
        bucket: "my-llama-agents-bucket"
        region: "us-east-1"
        endpointUrl: ""        # leave empty for AWS; set for MinIO/s3proxy/etc.
      secretRef: "llama-agents-s3-credentials"
      backupEncryptionSecretRef: "llama-agents-backup-password"   # optional
```

Everything is namespaced inside the bucket under three configurable prefixes, so one bucket can be shared with other workloads (including LlamaCloud’s own file-storage buckets) as long as the prefixes don’t collide. A dedicated bucket is simpler if you want S3 lifecycle rules or IAM policies scoped only to agent artifacts.

| Key                                            | Default    | Purpose                                                             |
| ---------------------------------------------- | ---------- | ------------------------------------------------------------------- |
| `controlPlane.objectStorage.buildKeyPrefix`    | `builds/`  | Built agent artifacts                                               |
| `controlPlane.objectStorage.backupKeyPrefix`   | `backups/` | Backup archives (encrypted when `backupEncryptionSecretRef` is set) |
| `controlPlane.objectStorage.codeRepoKeyPrefix` | `git/`     | Code repositories                                                   |

### App namespace

Agent pods run in a separate `llama-agents` namespace by default, not the LlamaCloud release namespace. The control plane and operator themselves stay in the release namespace, and the LlamaCloud chart creates the apps namespace automatically.

```
llama-agents-subchart:
  apps:
    namespace: my-agents-ns
```

An empty string runs agent pods in the release namespace alongside the control plane and operator.

### Agent pod resources

The operator creates pods for each `LlamaDeployment`. The requests and limits applied to those pods come from these defaults:

```
llama-agents-subchart:
  operator:
    defaultAppRequests:
      cpu: "750m"
      memory: "2Gi"
    defaultAppLimits:
      cpu: ""            # empty = no limit
      memory: "4096Mi"
    maxDeployments: 0    # per-namespace cap, 0 = unlimited
```

For anything beyond uniform defaults (nodeSelector, tolerations, affinity, container-level overrides), set `operator.llamaDeploymentTemplate.spec.podSpec`. The operator uses it as the base PodSpec for every managed pod.

## CRDs

The subchart ships two CRDs, `LlamaDeployment` and `LlamaDeploymentTemplate`. Helm’s CRD lifecycle is the awkward part: CRDs bundled in a chart’s `crds/` directory install on first `helm install`, but `helm upgrade` never touches them and `helm uninstall` never removes them. So fresh installs work out of the box, but when the subchart bumps a CRD schema nothing updates unless you do it yourself.

For that, install the companion [`llama-agents-crds`](https://github.com/run-llama/llama-agents/tree/main/charts/llama-agents-crds) chart separately and upgrade it on its own cadence. The LlamaCloud chart advertises the version it’s validated against via `llamaAgents.crdVersion` in its `values.yaml`; pin to that when installing:

Terminal window

```
helm upgrade --install llama-agents-crds \
  --version <llamaAgents.crdVersion> \
  oci://registry-1.docker.io/llamaindex/llama-agents-crds
```

It uses `helm.sh/resource-policy: keep`, so `helm uninstall` on the CRD chart leaves the CRDs in place and won’t cascade-delete your `LlamaDeployment` resources.

For production BYOC we recommend installing `llama-agents-crds` from the start rather than relying on the first-install bundling, so CRD upgrades stay decoupled from LlamaCloud releases.

## Separately-managed control plane

Skip `deploy: true` if you want to run the `llama-agents` chart on its own release cadence, in a different namespace, or in a different cluster with pod-level connectivity back to this one. Leave `deploy: false` and point LlamaCloud at the control plane’s service address:

```
llamaAgents:
  controlPlaneUrl: "http://llama-agents-control-plane.llama-agents.svc.cluster.local:8000"
```

In this mode the LlamaCloud chart doesn’t deploy the subchart or render the NetworkPolicy, and CRDs don’t need to be present in this cluster. Use an internal address. The control plane API is not designed to be internet-exposed.

## Escape hatches

Two knobs change how agent pods talk to the backend. Most installs never need either.

| Value                             | Default | When to set                                                                                                                                                                                          |
| --------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `llamaAgents.allowBackendEgress`  | `true`  | Disable the chart’s default egress NetworkPolicy if you author your own. Only renders when `deploy: true`.                                                                                           |
| `llamaAgents.useBackendPublicUrl` | `false` | Route agent `LLAMA_CLOUD_BASE_URL` through the public ingress host instead of the in-cluster ClusterIP. Set this when your cluster’s network policy stack blocks agent-to-backend ClusterIP traffic. |

`useBackendPublicUrl` is applied at deployment creation time, so existing deployments keep their original URL until they are recreated.
