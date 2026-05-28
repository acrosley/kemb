---
title: Optional Feature Flags | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

LlamaCloud exposes a small set of optional environment-variable flags that toggle UI or behavior in self-hosted deployments. These are in addition to the defaults already baked into the Helm chart.

All flags are set via `extraEnvVariables` on the relevant pod (typically `frontend`) in your `values.yaml`.

## Frontend flags

Frontend flags are environment variables read by the LlamaCloud web app. Flags without a `NEXT_PUBLIC_` prefix are resolved **server-side at request time**, so they respond to ConfigMap / `extraEnvVariables` changes without rebuilding the image. `NEXT_PUBLIC_*` flags are inlined into the client bundle at build time and cannot be changed at runtime.

| Flag                                       | Default (BYOC) | Purpose                                                                                       |
| ------------------------------------------ | -------------- | --------------------------------------------------------------------------------------------- |
| `IS_INDEX_V1_ENABLED`                      | `true`         | Show the **Index** entry in the sidebar and on the project home page. Set to `false` to hide. |
| `NEXT_PUBLIC_IS_INDEX_PARSE_EDIT_DISABLED` | `false`        | Disable parse-config editing on an existing index (build-time inlined).                       |

### Overriding a frontend flag

To override a default, add it to `frontend.extraEnvVariables` in your `values.yaml`:

```
frontend:
  extraEnvVariables:
    - name: IS_INDEX_V1_ENABLED
      value: "false"
```

Values must be strings (`"true"` / `"false"`).

## Backend flags

Backend feature flags are read by the LlamaCloud API from the `backend` pod env. They follow the `IS_*_ENABLED` / `IS_*_DISABLED` naming convention.

| Flag                            | Default | Purpose                                                                |
| ------------------------------- | ------- | ---------------------------------------------------------------------- |
| `IS_INDEX_PARSE_EDIT_DISABLED`  | `false` | Server-side counterpart to `NEXT_PUBLIC_IS_INDEX_PARSE_EDIT_DISABLED`. |
| `IS_MANAGED_EMBEDDINGS_ENABLED` | `false` | Enable managed embeddings as a default for new projects.               |
| `IS_TEMPORAL_EXTRACT_ENABLED`   | `false` | Route new extract jobs through Temporal.                               |

### Overriding a backend flag

```
backend:
  extraEnvVariables:
    - name: IS_INDEX_PARSE_EDIT_DISABLED
      value: "true"
```

## Notes

- These flags only control *defaults* for a self-hosted deployment. In managed LlamaCloud, the same feature flags are resolved via PostHog; in BYOC/self-hosted, the env-var value is authoritative.
- When a frontend flag has a backend counterpart (e.g. `IS_*` in the API), set both consistently to avoid UI/API drift.
