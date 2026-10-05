---
description: View Cache Reserve storage, read, and write operation metrics.
title: Cache Reserve analytics
image: https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/og.png?v=c6ddbbbbc7b39055
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/smart-shield/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cache Reserve analytics

Last updated Aug 25, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cache Reserve Analytics provides insights regarding your Cache Reserve usage. It allows you to check what content is stored in Cache Reserve, how often it is being accessed, how long it has been there and how much egress from your origin it is saving you.

You have access to the following metrics:

- **Egress savings (bandwidth)** - is an estimation based on response bytes served from Cache Reserve that did not need to be served from your origin server. These are represented as cache hits.
- **Requests served by Cache Reserve** - is the number of requests served by Cache Reserve (total).
- **Data storage summary** - is based on a representative sample of requests. Refer to [Sampling](https://developers.cloudflare.com/analytics/graphql-api/sampling/) for more details about how Cloudflare samples data.
  - **Current data stored** - is the data stored (currently) over time.
  - **Aggregate storage usage** - is the total of storage used for the selected timestamp.
- **Operations** - Class A (writes) and Class B (reads) operations over time.
