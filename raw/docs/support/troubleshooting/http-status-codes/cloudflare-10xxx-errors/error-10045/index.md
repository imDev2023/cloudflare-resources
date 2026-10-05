---
description: Troubleshoot Cloudflare error 10045.
title: Error 10045
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10045/og.png?v=1bec783d1bbe170b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10045

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10045/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10045: Invalid redirect source URL

This error indicates that the source URL for a redirect is not valid.

### Common causes

This error occurs when the source URL provided for a URL redirect is not valid, preventing the redirect from functioning properly due to missing components, such as the scheme (for instance, `http` or `https`) or improper formatting.

### Resolution

You need to specify a valid URL as the source URL. Refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/) for details on the supported URL components for redirect source URLs.
