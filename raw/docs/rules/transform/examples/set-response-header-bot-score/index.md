---
description: Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response with the current bot score.
title: Set a response header with the current bot score
image: https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/og.png?v=429db5c9788d0c32
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Set a response header with the current bot score

Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response with the current bot score.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule sets a header named `X-Bot-Score` to the current bot score in the HTTP response:

Text in **Expression Editor**:

```txt
starts_with(http.request.uri.path, "/en/")
```

Selected operation under **Modify response header**: *Set dynamic*

**Header name**: `X-Bot-Score`

**Value**: `to_string(cf.bot_management.score)`

This rule would overwrite any existing `X-Bot-Score` headers already present in the HTTP response.
