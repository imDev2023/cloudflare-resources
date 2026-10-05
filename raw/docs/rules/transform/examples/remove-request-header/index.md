---
description: Create a request header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the request.
title: Remove a request header
image: https://developers.cloudflare.com/rules/transform/examples/remove-request-header/og.png?v=5622d2bee2f22c2f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Remove a request header

Create a request header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the request.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/remove-request-header/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following request header transform rule removes the `cf-connecting-ip` header from the HTTP request:

Text in **Expression Editor**:

```txt
starts_with(http.request.uri.path, "/private/")
```

Selected operation under **Modify request header**: *Remove*

**Header name**: `cf-connecting-ip`
