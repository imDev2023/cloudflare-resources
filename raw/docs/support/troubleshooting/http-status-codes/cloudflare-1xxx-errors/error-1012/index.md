---
description: Troubleshoot Cloudflare 1012 error code.
title: Error 1012
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1012/og.png?v=08edeca7d8661ce7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1012

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1012/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1012: Access Denied

This error indicates that access to the website is denied.

### Common cause

A website owner forbids access based on malicious activity detected from the visitor's computer or network (ip\_address). The most likely cause is a virus or malware infection on the visitor's computer.

### Resolution

Update your antivirus software and run a full system scan. Cloudflare can not override the security settings the site owner has set for the domain. To request website access, contact the site owner to allow your IP address. If you cannot determine how to contact the website owner, lookup contact information for the domain via the [Whois database ↗︎](https://lookup.icann.org/).

Note

Since the website owner performed the blocking, Cloudflare support cannot override a customer's security settings.
