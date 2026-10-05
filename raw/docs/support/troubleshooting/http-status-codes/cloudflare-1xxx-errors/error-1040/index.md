---
description: Troubleshoot Cloudflare 1040 error code.
title: Error 1040
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1040/og.png?v=263c351238f3a27d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1040

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1040/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1040: Invalid request rewrite (header modification not allowed)

This error indicates that an attempt was made to modify a restricted HTTP header.

### Common cause

You are trying to modify an HTTP header that Request Header Transform Rules cannot change.

### Resolution

Make sure you are not trying to modify one of the [reserved HTTP request headers](https://developers.cloudflare.com/rules/transform/request-header-modification/#important-remarks).
