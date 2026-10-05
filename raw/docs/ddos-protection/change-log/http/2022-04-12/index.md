---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2022-04-12"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-04-12/og.png?v=383b1141147871ce
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2022-04-12

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-04-12/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...61b90333 | HTTP requests with unusual HTTP headers or URI path (signature #15). | N/A | managed\_challenge | This rule is detecting floods of requests impersonating a browser. |
| ...81b13394 | HTTP requests with unusual HTTP headers or URI path (signature #2). | block | block | Updated the filter to detect attacks more easily |
