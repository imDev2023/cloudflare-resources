---
description: Limits
title: Scan limits
image: https://developers.cloudflare.com/security-center/investigate/scan-limits/og.png?v=796fc70a74c9d442
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/security-center/llms.txt  
> Use this file to discover all available pages before exploring further.

# Scan limits

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/security-center/investigate/scan-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

URL scans are limited by search history, Public and Unlisted visibility, and requests per second across different Cloudflare plans.

| Cloudflare Plan | Search history | Public scans (per month) | Unlisted scans (per month) | Rate limit |
| --- | --- | --- | --- | --- |
| **Free / Radar** | last 50 scans | 5,000 | none | 1 per 10 seconds |
| **Self serve** | 30 days | 5,000 | 500 | 1 per 10 seconds |
| **Enterprise** | 12 months | 10,000 | 5,000 | 12 per second |
| **Cloudforce One** | Unlimited | 75,000 | 20,000 | 12 per second |
