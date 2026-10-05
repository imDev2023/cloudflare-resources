---
description: Troubleshoot Cloudflare 1006 error code.
title: Error 1006, 1007, 1008 or 1106
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1006/og.png?v=9fe2cea713e2d855
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1006, 1007, 1008 or 1106

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1006/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Errors 1006, 1007, 1008 or 1106 Access Denied: Your IP address has been banned

This error indicates that access is denied because your IP address has been banned.

### Common causes

A Cloudflare customer blocked traffic from your client or browser.

Note

Error 1006 also occurs in the Cloudflare **Workers** app under the **Preview** tab when a customer uses **[Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/)** or any other Cloudflare security feature to block the Google Cloud Platform IPs that the **Preview** tab relies upon.

### Resolution

Request the website owner to investigate their Cloudflare security settings or allow your client IP address. Since the website owner blocked your request, Cloudflare support cannot override a customer's security settings.
