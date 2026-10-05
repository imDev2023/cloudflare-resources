---
description: Respect Strong ETags
title: Respect Strong ETags
image: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/respect-strong-etags/og.png?v=91c9331ab6998bc8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# Respect Strong ETags

Respect Strong ETags

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/respect-strong-etags/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to respect strong ETags for any hostname containing `example.com`:

- **When incoming requests match**: Custom filter expression
  - Using the Expression Builder:  
    `Hostname contains "example.com"`
  - Using the Expression Editor:  
    `(http.host contains "example.com")`
- **Then**:
  - **Cache eligibility**: Eligible for cache
  - **Setting**: Respect strong ETags
    - **Use strong ETag headers**: On
