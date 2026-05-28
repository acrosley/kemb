---
title: Migration Guide: Extract v1 to v2 | Developer Documentation
description: Migrate from Extract v1 to v2 across UI, SDK, and REST API with endpoint and parameter mappings.
---

> **You only need this page if you already have Extract v1 integrations.** If you are starting fresh, use the v2 [Overview](/llamaparse/extract/index.md) and [SDK guide](/llamaparse/extract/sdk/index.md).

Extract v2 keeps the same core idea (schema-driven extraction) but changes how you configure and run jobs:

- **v1** centered on long-lived **Extraction Agents** and job runs tied to `extraction_agent_id`.
- **v2** centers on **Extraction Configurations** (saved or inline) and jobs created directly with `file_input` + configuration.
- **v2** also accepts a **Parse job ID** (`pjb-...`) as input, so you can parse once and extract many times.

## Quick migration checklist

- Replace v1 agent/job endpoints with v2 extract endpoints.
- Replace `extraction_agent_id` + `file_id` with `file_input` and either `configuration_id` or inline `configuration`.
- Replace v1 `config.extraction_mode` values (`FAST`, `BALANCED`, `MULTIMODAL`, `PREMIUM`) with v2 `configuration.tier` (`cost_effective`, `agentic`) plus optional `parse_tier`.
- Update status handling: v1 `SUCCESS`/`ERROR`/`PARTIAL_SUCCESS` becomes v2 `COMPLETED`/`FAILED`.
- If you currently manage agents, migrate to saved product configurations (`product_type=extract_v2`).
- Update SDK code from `client.extraction.*` patterns to `client.extract.*` patterns.

## Concept mapping

| Extract v1               | Extract v2                                             | What changed                                                   |
| ------------------------ | ------------------------------------------------------ | -------------------------------------------------------------- |
| Extraction Agent         | Extraction Configuration                               | Agent CRUD replaced by reusable configuration objects          |
| `extraction_agent_id`    | `configuration_id` (saved) or `configuration` (inline) | v2 job request always specifies config source                  |
| `file_id`                | `file_input`                                           | v2 accepts file ID (`dfl-...`) **or** parse job ID (`pjb-...`) |
| `config.extraction_mode` | `configuration.tier` (+ optional `parse_tier`)         | v2 separates extract and parse choices                         |
| `/jobs/{id}/result`      | `GET /api/v2/extract/{id}`                             | v2 returns `extract_result` on job resource                    |

## Endpoint mapping (REST API)

### Jobs

| v1                                            | v2                                                    |
| --------------------------------------------- | ----------------------------------------------------- |
| `POST /api/v1/extraction/jobs`                | `POST /api/v2/extract?project_id=...`                 |
| `GET /api/v1/extraction/jobs/{job_id}`        | `GET /api/v2/extract/{job_id}?project_id=...`         |
| `GET /api/v1/extraction/jobs/{job_id}/result` | `GET /api/v2/extract/{job_id}?project_id=...`         |
| *No equivalent cancel endpoint*               | `POST /api/v2/extract/{job_id}/cancel?project_id=...` |

### Config / schema

| v1                                                            | v2                                                                               |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `POST /api/v1/extraction/extraction-agents`                   | `POST /api/v1/beta/configurations?project_id=...` with `product_type=extract_v2` |
| `GET /api/v1/extraction/extraction-agents`                    | `GET /api/v1/beta/configurations?project_id=...&product_type=extract_v2`         |
| `POST /api/v1/extraction/extraction-agents/schema/validation` | `POST /api/v2/extract/schema/validation`                                         |
| `POST /api/v1/extraction/extraction-agents/schema/generate`   | `POST /api/v2/extract/schema/generate?project_id=...`                            |

## Request/response field mapping

### Create job request

| v1 (`POST /api/v1/extraction/jobs`) | v2 (`POST /api/v2/extract`)                          |
| ----------------------------------- | ---------------------------------------------------- |
| `extraction_agent_id`               | `configuration_id` **or** `configuration`            |
| `file_id`                           | `file_input`                                         |
| `data_schema_override`              | include schema in inline `configuration.data_schema` |
| `config_override`                   | inline `configuration` fields                        |

### Status mapping

| v1 status         | v2 status                                         |
| ----------------- | ------------------------------------------------- |
| `PENDING`         | `PENDING` or `RUNNING`                            |
| `SUCCESS`         | `COMPLETED`                                       |
| `PARTIAL_SUCCESS` | `COMPLETED` (inspect result/metadata for details) |
| `ERROR`           | `FAILED`                                          |
| `CANCELLED`       | `CANCELLED`                                       |

## Tier / mode mapping

v1 used `extraction_mode`; v2 uses extract and parse tiers explicitly.

| v1 `extraction_mode` | v2 `configuration.tier`                     | Typical v2 parse choice        |
| -------------------- | ------------------------------------------- | ------------------------------ |
| `FAST`               | `cost_effective`                            | `parse_tier: "cost_effective"` |
| `BALANCED`           | `cost_effective` (or `agentic` for quality) | `parse_tier: "agentic"`        |
| `MULTIMODAL`         | `agentic`                                   | `parse_tier: "agentic"`        |
| `PREMIUM`            | `agentic`                                   | `parse_tier: "agentic_plus"`   |

## SDK migration example (Python)

### v1 pattern

```
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="...")


agent = client.extraction.extraction_agents.create(
    name="invoice-agent",
    data_schema=schema,
    config={"extraction_mode": "BALANCED"},
)


job = client.extraction.jobs.create(
    extraction_agent_id=agent.id,
    file_id=file_id,
)
```

### v2 pattern

```
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="...")


job = client.extract.create(
    file_input=file_id,  # or parse_job.id
    configuration={
        "data_schema": schema,
        "tier": "agentic",
        "parse_tier": "agentic",
        "extraction_target": "per_doc",
        "cite_sources": True,
    },
)


job = client.extract.get(job.id)
print(job.extract_result)
```

## UI migration notes

In the v2 UI, you work with **Extraction Configurations** rather than **Extraction Agents**.

- v1 users who need the legacy UI can enable **Settings → General → Extract v1**.
- For v2 migration, recreate or import your schemas as configurations, then run jobs from those configurations.
- If you manage many recurring pipelines, save configs and reference them by `configuration_id`.

## Recommended migration path for production

1. Pick one existing v1 agent and port its schema/settings to a v2 configuration.
2. Run the same sample files in v1 and v2; compare extracted fields and metadata.
3. Update client code to treat job states as `PENDING`/`RUNNING`/`COMPLETED`/`FAILED`/`CANCELLED`.
4. Migrate batch flows to pass `configuration_id` in v2 job creation.
5. After validation, switch traffic to `/api/v2/extract` and keep v1 as fallback during rollout.

## See also

- [Extract Overview](/llamaparse/extract/index.md)
- [Extract SDK](/llamaparse/extract/sdk/index.md)
- [Extract REST API](/llamaparse/extract/api/index.md)
- [Using saved configurations](/llamaparse/extract/examples/using_saved_configurations/index.md)
- [Extract v1 docs (legacy)](/llamaparse/extract/v1/getting_started/index.md)
