---
description: Troubleshoot Cloudflare error 10047.
title: Error 10047
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10047/og.png?v=647cd0aab4e682be
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10047

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10047/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10047: Invalid redirect status code

This error indicates that an unsupported or incorrectly formatted status code was specified for the URL redirect.

### Common causes

This error occurs when you specify a URL redirect status code that is not supported, typically due to entering an invalid number or using an unsupported or deprecated status code.

### Resolution

Use one of the supported status codes in the URL redirect: `301`, `302`, `307`, or `308`.
