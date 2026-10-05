---
description: Learn how Workers roles control access to Durable Objects observability data and Data Studio.
title: Durable Objects roles and permissions
image: https://developers.cloudflare.com/workers/authorization/durable-objects/og.png?v=7bf91b31aebba028
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Durable Objects roles and permissions

Last updated Sep 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/authorization/durable-objects/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects do not have separate roles or permissions. Access to a Durable Object is determined by your access to the Worker that implements it.

To give a member, User Group, or API token access to a Durable Object, assign the appropriate Workers role at either the individual Worker scope or the Workers product scope. Refer to [Workers roles and permissions](https://developers.cloudflare.com/workers/authorization/workers/) for available roles and scopes.

## Observability access

`Metadata Read-Only` access to the implementing Worker includes Durable Object metrics, logs, and traces without granting access to data stored in the Durable Object. Granular authorization supports analytics for both SQLite-backed and KV-backed Durable Objects, with one current exception: the **Total KV storage** metric is unavailable for KV-backed Durable Objects.

## Data Studio access

[Durable Objects Data Studio](https://developers.cloudflare.com/durable-objects/observability/data-studio/) can query and modify data stored in SQLite-backed Durable Objects. Accessing Data Studio requires at least `Editor` access to the Worker that implements the Durable Object.

## Related resources

- [Workers roles and permissions](https://developers.cloudflare.com/workers/authorization/workers/)
- [Durable Objects metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/)
- [Durable Objects Data Studio](https://developers.cloudflare.com/durable-objects/observability/data-studio/)
