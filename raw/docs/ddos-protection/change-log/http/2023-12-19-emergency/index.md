---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2023-12-19 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-12-19-emergency/og.png?v=ccf5e198ef1a2cb2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-12-19 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-12-19-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...1fc1e601 | HTTP requests with unusual HTTP headers or URI path (signature #31). | block | block | Add more characteristics to the unusual HTTP headers or URI path. |
| ...22807318 | HTTP requests from known botnets. | log | ddos\_dynamic | Extend the rule to catch more attacks. |
| ...d2f294d7 | HTTP requests trying to impersonate browsers. | ddos\_dynamic | ddos\_dynamic | Change the rule to catch more attacks. |
