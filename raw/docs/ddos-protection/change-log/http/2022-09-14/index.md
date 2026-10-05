---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2022-09-14"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-09-14/og.png?v=9b662881b135078f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2022-09-14

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-09-14/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...e4fe8e55 | User-Agent-aware DDoS Protection (Available only to Enterprise zones with Advanced DDoS service). | managed\_challenge | log | This rule is causing false positive in some rare occurrences, we are reverting it back to log by default (opt-in). |
