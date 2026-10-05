---
description: Troubleshoot Cloudflare error 10044.
title: Error 10044
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10044/og.png?v=e928ae87f879c7d5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10044

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10044/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10044: Target URL in redirect is too long

This error indicates that the target URL in a redirect exceeds the maximum allowed length.

### Common causes

This error occurs when the target URL value of a URL redirect is too long. The maximum length of a target URL is 32,768 characters. Possible causes of this error are:

- Dynamic URLs that contain excessive query parameters or tracking codes.
- Unnecessary path segments or redundant subdirectories in the URL.

### Resolution

You need to use a shorter URL as the target URL.
