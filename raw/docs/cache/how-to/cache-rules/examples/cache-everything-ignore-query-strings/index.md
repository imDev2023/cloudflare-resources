---
description: Cache Everything while ignoring query strings
title: Cache Everything while ignoring query strings
image: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything-ignore-query-strings/og.png?v=77d2703f5b604a83
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cache/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cache Everything while ignoring query strings

Cache Everything while ignoring query strings

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything-ignore-query-strings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

If you are migrating from Page Rules and you want to keep Page Rules behavior, you need to create two specific rules before creating this rule. For more details refer to [Migration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/).

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to adjust cache level for any hostname containing `example.com`:

- **When incoming requests match**: Custom filter expression
  - Using the Expression Builder:  
    `Hostname contains "example.com"`
  - Using the Expression Editor:  
    `(http.host contains "example.com")`
- **Then**:
  - **Cache eligibility**: Eligible for cache
  - **Setting**: Cache key
    - **Query string**: Ignore query string
