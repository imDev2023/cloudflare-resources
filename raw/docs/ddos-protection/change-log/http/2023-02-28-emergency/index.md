---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2023-02-28 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-02-28-emergency/og.png?v=b086c1efdb277e58
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-02-28 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-02-28-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...97003a74 | HTTP requests with unusual HTTP headers or URI path (signature #17). | log | ddos\_dynamic | Enable mitigation on a subset of this rule that is known to only match attacks. |
