---
description: Limit upper-tier data centers to your preferred region for data locality.
title: Regional Tiered Cache
image: https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/og.png?v=8e285b03c2df0502
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/smart-shield/llms.txt  
> Use this file to discover all available pages before exploring further.

# Regional Tiered Cache

Last updated Jun 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Availability

Regional Tiered Cache is included with Enterprise plans. Smart Shield Advanced, which includes Regional Tiered Cache, is currently only available to Enterprise customers. If you are interested in Smart Shield Advanced, contact our [Enterprise Sales team ↗︎](https://www.cloudflare.com/resource/contact-enterprise-sales/).

Regional Tiered Cache provides an additional layer of caching for customers who have a global traffic footprint and want to serve content faster by avoiding network latency when there is a cache `MISS` in a lower-tier, resulting in an upper-tier fetch in a data center located far away.

Regional Tiered Cache instructs Cloudflare to check a regional hub data center near the lower tier before going to the upper tier that may be outside of the region.
