---
description: Troubleshoot Cloudflare 1041 error code.
title: Error 1041
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1041/og.png?v=c3153d4bfc8d5477
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1041

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1041/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1041: Invalid request rewrite (invalid header value)

This error indicates that the header value is not valid.

### Common causes

The added/modified header value is too long or it contains characters that are not allowed.

### Resolution

- Use a shorter value or expression to define the header value.
- Remove the characters that are not allowed. Refet to [Format of HTTP request header names and values](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/header-format/) in Developer Docs for more information on the allowed characters.
