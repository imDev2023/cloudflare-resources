---
description: Origin Cache Control
title: Origin Cache Control
image: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/origin-cache-control/og.png?v=23af6d3580d01903
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# Origin Cache Control

Origin Cache Control

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/origin-cache-control/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to determine edge cache behavior for any hostname containing `example.com`:

- **When incoming requests match**: Custom filter expression
  - Using the Expression Builder:  
    `Hostname contains "example.com"`
  - Using the Expression Editor:  
    `(http.host contains "example.com")`
- **Then**:
  - **Cache eligibility**: Eligible for cache
  - **Setting**: Origin Cache Control
    - **Enable Origin Cache Control**: Off
