---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2023-03-10"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-03-10/og.png?v=3e37af9178566b65
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-03-10

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-03-10/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...97003a74 | HTTP requests with unusual HTTP headers or URI path (signature #17). | ddos\_dynamic | block | Detect new attacks with unusual HTTP attributes. |
| ...d2f294d7 | HTTP requests trying to impersonate browsers. | ddos\_dynamic | ddos\_dynamic | Expand the filter to catch more attacks. |
