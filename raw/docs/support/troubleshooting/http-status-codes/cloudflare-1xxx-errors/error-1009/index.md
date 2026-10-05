---
description: Troubleshoot Cloudflare 1009 error code.
title: Error 1009
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1009/og.png?v=dbfc4473a1faf310
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1009

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1009/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Errors 1009 Access Denied: Country or region banned

This error indicates that access to the website is denied from your country or region.

### Common causes

The owner of the website (for example, `example.com`) has banned the country or region your IP address from accessing the website.

### Resolution

- If you are a site visitor, contact the site owner and ask them to allow your IP address.
- If you are the site owner, ensure that the reported IP address is allowed under the [IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/) security feature.
