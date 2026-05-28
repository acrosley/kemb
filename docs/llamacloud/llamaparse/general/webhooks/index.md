---
title: Webhooks | Developer Documentation
---

Webhooks allow you to receive real-time notifications when events occur in your LlamaCloud jobs. Instead of continuously polling for status updates, you can configure webhook endpoints to be notified immediately when jobs complete, fail, or reach other states.

## Overview

LlamaCloud webhooks provide:

- **Real-time notifications** for jobs
- **Configurable event filtering** to receive only relevant events
- **Retry logic** with exponential backoff for reliability
- **Custom headers** support for authentication

## Supported Events

Currently, LlamaCloud supports the following webhook events:

### Extract Events

- `extract.pending` - Extract job has been queued and is waiting to be processed
- `extract.success` - Extract job completed successfully
- `extract.error` - Extract job failed with an error
- `extract.partial_success` - Extract job completed with some warnings or partial failures
- `extract.cancelled` - Extract job was cancelled before completion

### Parse Events

- `parse.pending` - Parse job has been queued and is waiting to be processed
- `parse.success` - Parse job completed successfully
- `parse.error` - Parse job failed with an error
- `parse.partial_success` - Parse job completed with some warnings or partial failures
- `parse.cancelled` - Parse job was cancelled before completion

## Configuration

Reference the full API schema here: <https://api.cloud.llamaindex.ai/redoc#tag/LlamaExtract/operation/run_job_api_v1_extraction_jobs_post>

### Basic Configuration

Configure webhooks by including webhook configurations in your API calls. You will want to include the webhook configurations as follows:

```
{ ...
  "webhook_configurations": [
    {
      "webhook_url": "string",
      "webhook_headers": {
        "property1": "string",
        "property2": "string"
      },
      "webhook_events": [
        "extract.pending",
        "extract.success",
        "extract.error"
      ],
      "webhook_output_format": "json"
    }
  ]
  ...
}
```

Here’s how to configure webhooks in Python (added as the webhook\_configurations parameter in the request body):

```
webhook_configurations = [
    {
        "webhook_url": "https://your-domain.com/webhook-endpoint",
        "webhook_events": ["extract.success", "extract.error", "parse.success", "parse.error"],
        "webhook_headers": {
            "Authorization": "Bearer your-token",
            "X-Custom-Header": "custom-value"
        },
        "webhook_output_format": "json"
    }
]
```

### Event Filtering

You can specify which events to receive by setting the `webhook_events` array. If not specified, all events will be sent.

```
# Receive only success and error events
webhook_configurations = [
    {
        "webhook_url": "https://your-domain.com/webhook",
        "webhook_events": ["extract.success", "extract.error", "parse.success", "parse.error"]
        "webhook_output_format": "json"
    }
]


# Receive all events (default behavior)
webhook_configurations = [
    {
        "webhook_url": "https://your-domain.com/webhook"
        "webhook_output_format": "json"
        # webhook_events omitted = receive all events
    }
]
```

### Custom Headers

Add custom headers for authentication or other purposes:

```
webhook_configurations = [
    {
        "webhook_url": "https://your-domain.com/webhook",
        "webhook_headers": {
            "Authorization": "Bearer your-secret-token",
            "X-Source": "llamacloud",
            "Content-Type": "application/json"  # This is set automatically
        }
        "webhook_output_format": "json"
    }
]
```

## Webhook Payload

When an event occurs, LlamaCloud will send a POST request to your webhook URL with the following payload structure:

```
{
    "event_id": "149744dd-9002-4411-a6c7-9635da372caa",
    "event_type": "parse.success",
    "timestamp": 1753985275.1154444,
    "data": {
        "id": "a9a57884-921e-4ec2-b555-f4e5a97ec02a",
        "job_id": "a9a57884-921e-4ec2-b555-f4e5a97ec02a"
    }
}
```

### Payload Fields

- `event_id`: Unique identifier for this webhook event
- `event_type`: The type of event that occurred (e.g., “extract.success”, “parse.success”)
- `timestamp`: Unix timestamp when the event occurred
- `data`: Event-specific data containing job details and results

### HTTP Headers

LlamaCloud includes these headers with webhook requests:

- `Content-Type: application/json`
- `User-Agent: llamaindex-webhook-service/1.0`
- `X-Webhook-Event-ID: {event_id}`
- `X-Webhook-Event-Type: {event_type}`
- Any custom headers you configured

## Retry Behavior

LlamaCloud implements automatic retry logic for webhook deliveries:

- **Maximum attempts**: 3 attempts by default
- **Exponential backoff**: Wait time doubles between attempts (1s, 2s, 4s)
- **Maximum wait time**: 60 seconds maximum between retries
- **Timeout**: 30-second timeout per request

A webhook delivery is considered successful if your endpoint returns any HTTP status code in the 200-299 range.
