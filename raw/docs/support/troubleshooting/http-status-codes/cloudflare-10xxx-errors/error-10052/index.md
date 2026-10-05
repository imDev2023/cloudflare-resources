---
description: Troubleshoot Cloudflare error 10052.
title: Error 10052
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10052/og.png?v=793b8ba12e6878f5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10052

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10052/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10052: Invalid redirect source URL with port

This error indicates that the source URL includes an unsupported port.

### Common causes

This error occurs when the source URL of a URL redirect includes a port (for example, `https://example.com:8081`), which is not supported. Possible causes include using a custom or non-standard port, copying a URL from another environment that includes a port, or mistakenly using a development or testing URL.

### Resolution

Remove the port from the redirect source URL. Refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/) for details on the supported URL components for redirect source URLs.
