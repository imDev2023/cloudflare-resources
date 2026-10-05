---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2022-10-06 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-10-06-emergency/og.png?v=5f25852b8b9ba521
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2022-10-06 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-10-06-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...6fa59d23 | HTTP requests that are very likely coming from bots. | managed\_challenge | ddos\_dynamic | Block very large attacks instead of challenging them. |
| ...91b2849e | HTTP requests with unusual HTTP headers (signature #13). | block | block | Some attacks were only partially mitigated. Now the rule should stop attacks completely. |
