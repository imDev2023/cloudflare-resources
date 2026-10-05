---
description: Troubleshoot Cloudflare error 10053.
title: Error 10053
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10053/og.png?v=5eb0c33e64821aaf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10053

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10053/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10053: Invalid redirect source URL with query string

This error indicates that the source URL contains an unsupported query string component.

### Common causes

This error occurs when the source URL of a URL redirect includes a query string component, which is not supported. Possible causes include copying a URL with query parameters, misconfiguration during setup, or attempting to redirect based on query parameters instead of the path.

### Resolution

Remove the query string from the redirect source URL. Refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/) for details on the supported URL components for redirect source URLs.
