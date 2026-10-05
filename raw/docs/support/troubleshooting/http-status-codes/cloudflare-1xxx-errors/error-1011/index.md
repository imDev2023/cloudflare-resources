---
description: Troubleshoot Cloudflare 1011 error code.
title: Error 1011
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1011/og.png?v=08b3ebfffb21e0bf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1011

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1011/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1011: Access Denied (Hotlinking Denied)

This error indicates that access to the resource is denied due to hotlinking protection.

### Common cause

A request is made for a resource that uses [Cloudflare hotlink protection](https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/).

### Resolution

Notify the website owner of the blocking. If you cannot determine how to contact the website owner, lookup contact information for the domain via the [Whois database ↗︎](https://lookup.icann.org/).

Note

Since the website owner performed the blocking, Cloudflare support cannot override a customer's security settings.
