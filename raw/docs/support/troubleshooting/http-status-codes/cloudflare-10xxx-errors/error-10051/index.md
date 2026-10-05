---
description: Troubleshoot Cloudflare error 10051.
title: Error 10051
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10051/og.png?v=efb8ad9204616b7d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10051

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10051/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10051: Missing authority in redirect source URL

This error indicates that the source URL is missing a required authority component.

### Common causes

This error occurs when the source URL of a URL redirect does not include an authority component (for example, `http:///path`, without a hostname), which is mandatory.

### Resolution

Add an authority component to the redirect source URL (for example, include a hostname). Refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/) for details on the required URL components for redirect source URLs.
