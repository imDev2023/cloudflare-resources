---
description: Optimize caching to reduce origin load.
title: Optimize caching
image: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/optimize-caching/og.png?v=00d30a247589d80c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Optimize caching

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/optimize-caching/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The more content is cached, the fewer requests go back to your origin server (whether due to legitimate or illegitimate traffic).

A few ways to optimize Cloudflare caching include:

- Creating [cache rules](https://developers.cloudflare.com/cache/how-to/cache-rules/) to customize the cache properties of specific HTTP requests.
- Enabling the [Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) feature, which dramatically increases cache hit ratios.
- Reviewing our other various [configuration options](https://developers.cloudflare.com/cache/get-started/), which may vary based on your plan and application setup.
