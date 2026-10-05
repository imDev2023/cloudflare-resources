---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2024-01-23"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2024-01-23/og.png?v=357e982aa0fde886
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2024-01-23

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2024-01-23/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...1fc1e601 | HTTP requests with unusual HTTP headers or URI path (signature #31). | block | block | Add more characteristics to the unusual HTTP headers or URI path. |
| ...2de94fb2 | HTTP requests with unusual HTTP headers or URI path (signature #3). | ddos\_dynamic | block | Expand rule scope to catch more attacks. |
| ...2f8d9a4f | HTTP requests from known botnet (signature #78). | N/A | block | |
