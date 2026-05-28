---
title: Billing and Usage | Developer Documentation
description: Guide on managing your LlamaParse billing, usage tracking, and subscription plans.
---

LlamaParse is a subscription-based service. You can manage all billing and usage from Settings → Billing in your [LlamaParse dashboard](https://cloud.llamaindex.ai/). For credit costs per product, see the [Pricing](/llamaparse/general/pricing/index.md) page.

## Plans

|                 | Free       | Starter  | Pro      | Enterprise    |
| --------------- | ---------- | -------- | -------- | ------------- |
| Monthly credits | 10,000     | 40,000   | 400,000  | Custom        |
| Price           | $0/mo      | $50/mo   | $500/mo  | Contact sales |
| Rate limits     | 20 req/min | Standard | Standard | Custom        |
| Support         | Community  | Email    | Priority | Dedicated     |

All plans include access to every product (Parse, Extract, Classify, Split, Index). Plans differ in credit allocation, rate limits, and support level.

### Upgrading

To upgrade your plan:

1. Click **“Upgrade now”** in the bottom left of your dashboard, or go to Settings → Billing → Pricing.
2. Select the plan you want and enter payment details.
3. Your new plan takes effect immediately.

![plans](/_astro/plans.CWRewqK8_Z2dY4A6.png)

### Downgrading

You can downgrade to the Free plan at any time from Settings → Billing → Pricing. Click on your current plan’s settings to access cancellation options.

## What Happens When Credits Run Out

Behavior depends on your plan:

- **Paid plans (Starter, Pro)**: Pay-as-you-go usage is enabled by default. When your included credits are exhausted, you can continue using the platform and additional credits are billed at the standard rate ($1.25 per 1,000 credits).
- **Free plan**: When credits are exhausted, API requests that consume credits will return a `402` error (“You’ve exceeded the maximum number of credits for your plan”). Credits reset at the start of your next billing cycle.
- **Enterprise plans**: Overage behavior is configured per contract. Contact your account manager for details.

## Monitoring Usage

Navigate to Settings → Billing → Usage to view detailed usage analytics:

- Current credit usage against your monthly quota
- Usage breakdown by product and mode (Parse, Extract, Classify, etc.)
- Historical usage trends with interactive charts

![usage](/_astro/usage.C-2eFWgI_Z2uPq42.png)

You can also access real-time usage data [via the API](/cloud-api-reference/get-project-usage-api-v-1-projects-project-id-usage-get/index.md) for programmatic monitoring.

For tips on reducing credit usage, see [Cost Optimization Strategies](/llamaparse/general/pricing#cost-optimization-strategies/index.md) on the Pricing page.

## Invoices

Your complete invoice history is available in Settings → Billing → Invoices:

- All past invoices with dates and amounts
- Invoice status (Draft, Issued, Paid)
- Detailed billing periods
- Payment method management

![invoices](/_astro/invoices.DjPHUhh-_x3Sw8.png)

Each invoice can be downloaded or viewed in detail, showing exact breakdowns of your charges for the billing period.
