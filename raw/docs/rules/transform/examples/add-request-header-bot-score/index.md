---
description: Create a request header transform rule to add a `X-Bot-Score` HTTP header to the request with the current bot score.
title: Add a request header with the current bot score
image: https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/og.png?v=25db323163bd6cea
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Add a request header with the current bot score

Create a request header transform rule to add a `X-Bot-Score` HTTP header to the request with the current bot score.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following request header transform rule adds a header named `X-Bot-Score` with the current bot score to the HTTP request:

Text in **Expression Editor**:

```txt
starts_with(http.request.uri.path, "/en/")
```

Selected operation under **Modify request header**: *Set dynamic*

**Header name**: `X-Bot-Score`

**Value**: `to_string(cf.bot_management.score)`
