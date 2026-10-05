---
description: Create two URL rewrite rules (part of Transform Rules) to rewrite the path of the welcome page for visitors in specific countries.
title: Rewrite page path for visitors in specific countries
image: https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/og.png?v=927cc2f2519ed114
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Rewrite page path for visitors in specific countries

Create two URL rewrite rules (part of Transform Rules) to rewrite the path of the welcome page for visitors in specific countries.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To have a welcome page in two languages, create two URL rewrite rules with a static rewrite of the path component:

**URL rewrite rule #1**

Text in **Expression Editor**:

```txt
http.request.uri.path == "/welcome.html" && ip.src.country == "GB"
```

Text after **Path** > **Rewrite to** > *Static*:

```txt
/welcome-gb.html
```

**URL rewrite rule #2**

Text in **Expression Editor**:

```txt
http.request.uri.path == "/welcome.html" && ip.src.country == "PT"
```

Text after **Path** > **Rewrite to** > *Static*:

```txt
/welcome-pt.html
```
