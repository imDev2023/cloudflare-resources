---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2024-02-06 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-06-emergency/og.png?v=857aa2d7aa4e1b8d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2024-02-06 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-06-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...1fc1e601 | HTTP requests with unusual HTTP headers or URI path (signature #31). | block | block | Modify characteristics of the unusual HTTP headers or URI path. |
| ...3a679c52 | Requests coming from known bad sources. | N/A | ddos\_dynamic | |
| ...3ad719cd | HTTP requests from known botnet (signature #79). | ddos\_dynamic | ddos\_dynamic | Expand the scope of the rule to match more attacks. |
