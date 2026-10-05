---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2024-01-05"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2024-01-05/og.png?v=dcf41ed42f79dfee
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2024-01-05

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2024-01-05/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...2de94fb2 | HTTP requests with unusual HTTP headers or URI path (signature #3). | block | block | Fine-tune the characteristics of the unusual requests. |
| ...177059f1 | HTTP requests from known botnet (signature #31). | block | N/A | Removed due to false positives. |
| ...6fe7a312 | HTTP requests from known botnet (signature #70). | block | N/A | Removed due to false positives. |
| ...82c0ed5f | HTTP requests from known botnet (signature #77). | N/A | block | |
| ...e4f3ea4d | HTTP requests from known botnet (signature #76). | N/A | block | |
