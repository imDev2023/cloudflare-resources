---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2022-08-02"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-08-02/og.png?v=d34d9ae0bb0af515
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2022-08-02

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-08-02/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...1712a123 | HTTP requests with unusual HTTP headers or URI path (signature #16). | log | block | Allow requests matching this rule to match other rules too in order to catch more attacks. |
| ...d2f294d7 | HTTP requests trying to impersonate browsers. | ddos\_dynamic | ddos\_dynamic | Extend the scope of this filter to match a wider set of requests. |
