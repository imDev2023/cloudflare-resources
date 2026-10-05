---
description: Edge Cache TTL
title: Edge Cache TTL
image: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/edge-ttl/og.png?v=78ce7703dc1cf3a6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# Edge Cache TTL

Edge Cache TTL

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/edge-ttl/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to adjust edge cache TTL for caching resources on Cloudflare edge to one day, for any hostname containing `example.com`:

- **When incoming requests match**: Custom filter expression
  - Using the Expression Builder:  
    `Hostname contains "example.com"`
  - Using the Expression Editor:  
    `(http.host contains "example.com")`
- **Then**:
  - **Cache eligibility**: Eligible for cache
  - **Setting**: Edge TTL
    - Ignore cache-control header and use this TTL
      - **Input time-to-live (TTL)**: *1 day*
