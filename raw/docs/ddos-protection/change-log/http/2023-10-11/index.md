---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2023-10-11"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-10-11/og.png?v=ebe555f6451bfd73
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-10-11

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-10-11/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...35675e08 | HTTP requests with unusual HTTP headers or URI path (signature #24). | block | block | This rule can cause rare false positives with custom apps sending invalid headers. |
