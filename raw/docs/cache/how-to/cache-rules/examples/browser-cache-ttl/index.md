---
description: Browser Cache TTL
title: Browser Cache TTL
image: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/browser-cache-ttl/og.png?v=ea5dade65bd4ef4b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# Browser Cache TTL

Browser Cache TTL

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/browser-cache-ttl/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

If you are migrating from Page Rules and you want to keep Page Rules behavior, you need to create two specific rules before creating this rule. For more details refer to [Migration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/).

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to adjust browser cache TTL for caching resources in the browser to one day for any hostname containing `example.com`:

- **When incoming requests match**: Custom filter expression
  - Using the Expression Builder:  
    `Hostname contains "example.com"`
  - Using the Expression Editor:  
    `(http.host contains "example.com")`
- **Then**:
  - **Cache eligibility**: Eligible for cache
  - **Browser TTL**: Override origin and use this TTL
  - **Input time-to-live (TTL)**: *1 day*
