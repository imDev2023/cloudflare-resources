---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2022-05-03"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-05-03/og.png?v=41c7868ef5143fc7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2022-05-03

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-05-03/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...4cc1fcb6 | BETA - HTTP requests with unusual HTTP headers or URI path (signature #2). | log | N/A | |
| ...81b13394 | HTTP requests with unusual HTTP headers or URI path (signature #2). | block | block | Update the rule to catch more attacks than before. |
| ...863134d5 | HTTP requests from known bad user agents. | log | block | |
