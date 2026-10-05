---
description: Troubleshoot Cloudflare 1010 error code.
title: Error 1010
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1010/og.png?v=6bb4d7d72bb433e0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1010

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1010/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1010: The owner of this website has banned your access based on your browser's signature

This error indicates that access to the website is denied based on your browser's signature.

### Common cause

A website owner blocked your request based on your client's web browser.

### Resolution

Notify the website owner of the blocking. If you cannot determine how to contact the website owner, lookup contact information for the domain via the [Whois database ↗︎](https://lookup.icann.org/). Site owners can [turn off Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/#disable-browser-integrity-check) in the Security **Settings** page.

Note

Since the website owner performed the blocking, Cloudflare support cannot override a customer's security settings.
