---
description: Create a CORS response header transform rule to add an `Access-Control-Allow-Origin` HTTP header to the response with wildcard as static value. (`cookiename=value`).
title: Add a wildcard CORS response header
image: https://developers.cloudflare.com/rules/transform/examples/add-cors-header/og.png?v=68918b8239d90034
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Add a wildcard CORS response header

Create a response header transform rule to add an `Access-Control-Allow-Origin` CORS HTTP header to the response with a static wildcard value.

Last updated Dec 10, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-cors-header/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule adds a header named `Access-Control-Allow-Origin` with a static wildcard value (`*`) to the HTTP response:

Text in **Expression Editor**:

```txt
(http.host eq "<YOUR_HOSTNAME>")
```

Selected operation under **Modify response header**: *Set static*

**Header name**: `Access-Control-Allow-Origin`

**Value**: `*`

You can also use an expression similar to the following to apply the CORS header to several specific hostnames:

```txt
(http.host in {"<YOUR_HOSTNAME_1>" "<YOUR_HOSTNAME_2>"})
```
