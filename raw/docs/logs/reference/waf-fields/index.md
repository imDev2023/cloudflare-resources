---
description: Review WAF action and rule field values in logs.
title: WAF fields
image: https://developers.cloudflare.com/logs/reference/waf-fields/og.png?v=3eb7c5408f18026f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# WAF fields

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/reference/waf-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Web Application Firewall (WAF) contains rules managed by Cloudflare to block requests that contain malicious content.

## WAF Action

| Value | Action | Description |
| --- | --- | --- |
| `0` | Unknown | Take no other action. |
| `1` | Allow | Bypass all subsequent WAF rules. |
| `2` | Drop | Block with an HTTP 403 response. |
| `3` | Challenge Allow | Issue a Managed Challenge. |
| `4` | Challenge Drop | Unused. |
| `5` | Log | Take no action other than logging the event. |

## Deprecated fields for internal Cloudflare use

The values of these fields are subject to change by Cloudflare at any time and are irrelevant for customer data analysis:

- WAFFlags
- WAFMatchedVar
