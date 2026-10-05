---
description: Create a response header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the response.
title: Remove a response header
image: https://developers.cloudflare.com/rules/transform/examples/remove-response-header/og.png?v=1bb278cd68e005ae
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Remove a response header

Create a response header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the response.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/remove-response-header/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule removes the `cf-connecting-ip` header from the HTTP response:

Text in **Expression Editor**:

```txt
starts_with(http.request.uri.path, "/private/")
```

Selected operation under **Modify response header**: *Remove*

**Header name**: `cf-connecting-ip`
