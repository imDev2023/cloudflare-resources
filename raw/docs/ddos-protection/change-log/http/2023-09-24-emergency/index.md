---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2023-09-24 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-24-emergency/og.png?v=953fa26150fac08b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-09-24 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-24-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...0fb54442 | HTTP requests with unusual HTTP headers or URI path (signature #49). | N/A | block | |
| ...3dd5f188 | HTTP requests from known botnet (signature #71). | N/A | block | |
| ...97003a74 | HTTP requests with unusual HTTP headers or URI path (signature #17). | block | block | Expand rule to catch more attacks. |
