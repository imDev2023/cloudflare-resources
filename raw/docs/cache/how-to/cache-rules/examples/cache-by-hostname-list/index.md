---
description: Cache everything for hostnames in a list
title: Cache everything for hostnames in a list
image: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-by-hostname-list/og.png?v=54e644179aae6ace
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cache everything for hostnames in a list

Cache everything for hostnames in a list

Last updated Jun 12, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-by-hostname-list/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to cache everything for hostnames that match a [custom hostname list](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#lists-with-hostnames):

- **When incoming requests match**: Custom filter expression
  - Using the Expression Builder:  
    `Hostname is in list "my_hostnames"`
  - Using the Expression Editor:  
    `(http.host in $my_hostnames)`
- **Then**:
  - **Cache eligibility**: Eligible for cache

Note

The **is in list** operator requires an Enterprise plan. You must first [create a hostname list](https://developers.cloudflare.com/waf/tools/lists/create-dashboard/) in your account before you can reference it in a cache rule expression.
