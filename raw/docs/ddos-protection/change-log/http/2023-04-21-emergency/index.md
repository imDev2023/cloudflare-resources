---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2023-04-21 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-04-21-emergency/og.png?v=e1312d0ce2b34807
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-04-21 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-04-21-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...d2f294d7 | HTTP requests trying to impersonate browsers. | ddos\_dynamic | ddos\_dynamic | Remove some rare false positives. |
| ...d3fb9259 | HTTP requests from known botnet (signature #51). | N/A | block | |
