---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2023-11-10 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-11-10-emergency/og.png?v=86728be517829027
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-11-10 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-11-10-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...7d0f1e5f | HTTP requests from known botnet (signature #72). | N/A | block | |
| ...94547a95 | HTTP requests with unusual HTTP headers or URI path (signature #59). | N/A | ddos\_dynamic | |
| ...e269dfd6 | HTTP requests with unusual HTTP headers or URI path (signature #56). | log | block | Enable filter early to mitigate widespread impact. |
| ...f35a42a0 | HTTP requests with unusual HTTP headers or URI path (signature #57). | log | block | Enable filter early to mitigate widespread impact. |
