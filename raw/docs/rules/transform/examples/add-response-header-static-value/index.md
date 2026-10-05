---
description: Create a response header transform rule to add a `set-cookie` HTTP header to the response with a static value (`cookiename=value`).
title: Add a response header with a static value
image: https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/og.png?v=021f56fd42af3527
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Add a response header with a static value

Create a response header transform rule to add a `set-cookie` HTTP header to the response with a static value (`cookiename=value`).

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule adds a header named `set-cookie` with a static value (`cookiename=value`) to the HTTP response:

Text in **Expression Editor**:

```txt
starts_with(http.request.uri.path, "/en/")
```

Selected operation under **Modify response header**: *Add*

**Header name**: `set-cookie`

**Value**: `cookiename=value`

This rule would keep any existing `set-cookie` headers already present in the HTTP response.
