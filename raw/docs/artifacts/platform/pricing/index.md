---
description: Review Artifacts pricing information.
title: Pricing
image: https://developers.cloudflare.com/artifacts/platform/pricing/og.png?v=d91474ce3a62ac8e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/artifacts/llms.txt  
> Use this file to discover all available pages before exploring further.

# Pricing

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/artifacts/platform/pricing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Artifacts is currently only available on the Workers Paid plan.

Note

Cloudflare will begin billing for Artifacts operations and storage on October 14, 2026.

Artifacts pricing is billed on two dimensions:

- **Operations**: the number of repo operations, such as `create`, `push`, `pull`, and `clone`.
- **Storage**: the total amount of stored data, measured in gigabyte-months ( `GB-mo`).

## Artifacts pricing

| Unit | Workers Free | Workers Paid |
| --- | --- | --- |
| Operations (1,000 operations) | Unavailable | First 10,000 per month + $0.15 per additional 1,000 operations |
| Storage (GB-mo) | Unavailable | First 1 GB per month + $0.50 per additional GB-mo |

## Storage usage

Storage is billed using gigabyte-month (`GB-mo`) as the billing metric, identical to [Durable Objects SQL storage](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend). A `GB-mo` is calculated by averaging peak storage per day over a 30-day billing period.

- Storage is calculated across all repositories.
- Replicas do not add storage charges. Storage is replicated by default, and you do not need to manage repository availability or uptime.
- Repos remain stored until you explicitly delete them.
