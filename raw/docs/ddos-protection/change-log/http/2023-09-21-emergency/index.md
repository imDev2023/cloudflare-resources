---
description: HTTP DDoS managed ruleset rule changes for this release.
title: 2023-09-21 - Emergency
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-21-emergency/og.png?v=9c6fbcaf9b2811b4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2023-09-21 - Emergency

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-21-emergency/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...1d73128d | HTTP requests from known botnet (signature #56). | block | block | Make the rule customizable as it might cause false positive in rare cases. |
| ...4a95ba67 | HTTP requests with unusual HTTP headers or URI path (signature #32). | ddos\_dynamic | ddos\_dynamic | Expand the scope of the rule to catch more attacks. |
| ...6fe7a312 | HTTP requests from known botnet (signature #70). | block | block | Update the rule to remove some rare false positives. |
