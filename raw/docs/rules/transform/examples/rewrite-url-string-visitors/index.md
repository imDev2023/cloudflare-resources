---
description: Create a transform rule to rewrite the request path from `/blog` to `/blog?sort-by=date`.
title: Rewrite URL query string
image: https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/og.png?v=3b309cfc35da7cdb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Rewrite URL query string

Create a transform rule to rewrite the request path from `/blog` to `/blog?sort-by=date`.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To rewrite a request to the `/blog` path to `/blog?sort-by=date`, create a URL rewrite rule with the following settings:

Text in **Expression Editor**:

```txt
http.request.uri.path == "/blog"
```

Text after **Query** > **Rewrite to** > *Static*:

```txt
sort-by=date
```

Additionally, set the path rewrite action of the same rule to *Preserve* so that the URL path does not change.
