---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2022-11-02 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-11-02-emergency/og.png?v=56c3ed16bb94ed77
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2022-11-02 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-11-02-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...06a46ce3 | HTTP requests with unusual HTTP headers or URI path (signature #18). | N/A | block | N/A |
| ...81b5405c | HTTP requests from known botnet (signature #3). | block | block | Extend the rule to catch more attacks. |
