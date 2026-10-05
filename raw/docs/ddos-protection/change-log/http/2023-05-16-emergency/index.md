---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2023-05-16 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-05-16-emergency/og.png?v=55139d505c5c9237
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-05-16 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-05-16-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...311e414e | HTTP requests with unusual HTTP headers or URI path (signature #33). | N/A | ddos\_dynamic | Stop attacks from an active botnet. |
| ...ad16b3fb | HTTP requests from known botnet (signature #54). | N/A | block | |
