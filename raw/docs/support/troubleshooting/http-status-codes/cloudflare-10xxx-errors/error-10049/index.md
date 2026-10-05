---
description: Troubleshoot Cloudflare error 10049.
title: Error 10049
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10049/og.png?v=48d004dc4b017421
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10049

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10049/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10049: Invalid scheme in redirect source URL

This error indicates that the source URL's scheme is invalid.

### Common causes

This error occurs when the source URL of a URL redirect has an invalid scheme, which may be due to a misspelled or unsupported scheme or because the scheme is missing or improperly formatted.

### Resolution

Review the source URL and ensure that it uses one of the supported schemes: `http`, `https`, or empty (no scheme information, which means that it applies to both schemes). Refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/) for details on the supported URL components for redirect source URLs.
