---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2024-02-19"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-19/og.png?v=8412eb87e169fcb1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2024-02-19

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-19/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...0fbfd5ae | HTTP requests from known botnet (signature #32). | block | ddos\_dynamic | |
| ...22807318 | HTTP requests from known botnets. | ddos\_dynamic | ddos\_dynamic | Expand rule logic to catch more attacks. |
| ...3ad719cd | HTTP requests from known botnet (signature #79). | ddos\_dynamic | ddos\_dynamic | Expand the rule scope to catch more attacks. |
