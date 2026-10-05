---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2023-04-17"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-04-17/og.png?v=dc8194bce61e4ea4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-04-17

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-04-17/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Previously, only a subset of rules were exposed publicly. In rare situations, these rules can cause false positives. When this happens, you can customize their behavior using overrides.

Besides these rules, the DDoS managed rules contain other rules that do not cause issues. Until now, these rules were not shown in the dashboard or referenced in the documentation.

Cloudflare now shows all rules in the dashboard, including these high-confidence rules. This means that requests matching these rules will now have the correct rule identifier. The newly published rules are read-only and you cannot disable them.
