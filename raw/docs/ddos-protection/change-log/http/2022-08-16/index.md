---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2022-08-16"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-08-16/og.png?v=e929cd28cc763d70
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2022-08-16

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-08-16/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...1712a123 | HTTP requests with unusual HTTP headers or URI path (signature #16). | block | block | Modify the rule to catch more attacks. |
| ...b757316c | BETA - HTTP requests with unusual HTTP headers or URI path (signature #16). | log | N/A | Observation filter removed, rule is now merged with ...1712a123 |
