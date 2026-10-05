---
description: Query String Sort
title: Query String Sort
image: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/query-string-sort/og.png?v=792561961e356eb1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# Query String Sort

Query String Sort

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/query-string-sort/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to sort query string parameters for caching purposes, for any hostname containing `example.com`:

- **When incoming requests match**: Custom filter expression
  - Using the Expression Builder:  
    `Hostname contains "example.com"`
  - Using the Expression Editor:  
    `(http.host contains "example.com")`
- **Then**:
  - **Cache eligibility**: Eligible for cache
  - **Setting**: Cache key
    - **Sort query string**: On
