---
description: HTTP DDoS managed ruleset rule changes for this release.
title: "2022-07-06"
image: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-07-06/og.png?v=c0da9469407bdad8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# 2022-07-06

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-07-06/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

| Rule ID | Description | Previous Action | New Action | Notes |
| --- | --- | --- | --- | --- |
| ...444be2c3 | Location-Aware DDoS Protection (Available only to Enterprise zones with Advanced DDoS service). | N/A | log | Added new Location-Aware DDoS Protection for Enterprise accounts that are subscribed to the Advanced DDoS service. Location Aware DDoS Protection constantly learns a zone's traffic levels per country and region over time, creates a traffic profile and then flags or mitigates traffic that deviates from the profile. |
| ...863134d5 | HTTP requests from known bad user agents. | block | block | Requests matching this rule will not match any other. |
