---
description: Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response to a static value (`Cloudflare`).
title: Set response header with a static value
image: https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/og.png?v=a45ab09949dcf70b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Set response header with a static value

Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response to a static value (`Cloudflare`).

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule sets a header named `X-Source` to a static value (`Cloudflare`) in the HTTP response:

Text in **Expression Editor**:

```txt
starts_with(http.request.uri.path, "/en/")
```

Selected operation under **Modify response header**: *Set static*

**Header name**: `X-Source`

**Value**: `Cloudflare`

This rule would overwrite any existing `X-Source` headers already present in the HTTP response.
