---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2023-08-14"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-08-14/og.png?v=6e1a41d774d45d42
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-08-14

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-08-14/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...22807318 | HTTP requests from known botnets. | ddos\_dynamic | managed\_challenge | Expand the filter to catch more attacks. |
| ...d2f294d7 | HTTP requests trying to impersonate browsers. | ddos\_dynamic | ddos\_dynamic | Expand the filter to catch more attacks. |
