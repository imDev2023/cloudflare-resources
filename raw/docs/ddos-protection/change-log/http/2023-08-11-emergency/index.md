---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2023-08-11 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-08-11-emergency/og.png?v=9d30f0dea55b9adb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-08-11 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-08-11-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...1de9523e | HTTP requests with unusual HTTP headers or URI path (signature #41). | N/A | block | |
| ...22807318 | HTTP requests from known botnets. | managed\_challenge | ddos\_dynamic | |
| ...aa03a345 | HTTP requests from known botnet (signature #68). | N/A | block | |
| ...efca86eb | HTTP requests from known botnet (signature #66). | N/A | block | |
| ...f93fb5d6 | HTTP requests from known botnet (signature #67). | N/A | block | |
