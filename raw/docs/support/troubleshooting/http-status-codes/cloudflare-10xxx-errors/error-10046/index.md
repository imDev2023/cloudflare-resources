---
description: Troubleshoot Cloudflare error 10046.
title: Error 10046
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10046/og.png?v=f6d9bd68e90454b5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 10046

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/error-10046/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 10046: Invalid redirect target URL

This error indicates that the target URL provided for a URL redirect is not valid.

### Common causes

This error occurs when the target URL provided for a URL redirect is not valid, preventing the redirect from functioning properly due to missing components, such as the scheme (for instance, `http` or `https`) or improper formatting.

### Resolution

You need to specify a valid URL as the target URL. Refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/) for details on the supported URL components for redirect target URLs.
